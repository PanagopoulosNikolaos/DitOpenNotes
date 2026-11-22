(function (global_scope) {
  'use strict';

  /**
   * Escapes special HTML characters in strings before template injection.
   *
   * Args:
   *     raw_text (string): Raw string value.
   *
   * Returns:
   *     string: Escaped safe HTML string.
   */
  function escapeHtml(raw_text) {
    return String(raw_text)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  /**
   * Manages interactive Python Drop-In code completion puzzles with drag-and-drop and click placement.
   *
   * Renders code skeletons with dropzone slots above a tray of draggable/clickable tokens.
   * Methods: mount(container_el, unit_id, completed_set, on_complete_cb), renderPuzzle(container_el, unit_id, completed_set, on_complete_cb), handlePlaceToken(slot_id, token_id, container_el, unit_id, completed_set, on_complete_cb).
   */
  class DropInGameEngine {
    /**
     * Initializes puzzle selection, active token cursor, and slot state dictionaries.
     */
    constructor() {
      this.active_puzzle_idx = {};
      this.slot_states = {};
      this.selected_token_id = null;
      this.dragged_token_id = null;
      this.feedback_msg = '';
      this.feedback_kind = 'neutral';
    }

    /**
     * Mounts the Drop-In code completion game for the requested unit.
     *
     * Args:
     *     container_el (HTMLElement): Host DOM element inside the Playground tab.
     *     unit_id (string): Active unit identifier ('00'..'07').
     *     completed_set (Array<string>): Persisted array of completed puzzle/game IDs.
     *     on_complete_cb (Function): Callback invoked with puzzle_id when all slots are solved.
     */
    mount(container_el, unit_id, completed_set, on_complete_cb) {
      const all_puzzles = (global_scope.MidtermApp.dropin_puzzles || {})[unit_id] || [];
      if (all_puzzles.length === 0) {
        container_el.innerHTML = '<div class="card"><p>Δεν υπάρχουν διαθέσιμες ασκήσεις Drop-In για αυτή την ενότητα.</p></div>';
        return;
      }
      if (typeof this.active_puzzle_idx[unit_id] !== 'number') {
        this.active_puzzle_idx[unit_id] = 0;
      }
      this.renderPuzzle(container_el, unit_id, completed_set, on_complete_cb);
    }

    /**
     * Renders the active Drop-In puzzle stage, token tray, and event listeners.
     *
     * Args:
     *     container_el (HTMLElement): Host DOM element.
     *     unit_id (string): Unit identifier ('00'..'07').
     *     completed_set (Array<string>): Persisted completion list.
     *     on_complete_cb (Function): Completion callback.
     */
    renderPuzzle(container_el, unit_id, completed_set, on_complete_cb) {
      const puzzles = global_scope.MidtermApp.dropin_puzzles[unit_id];
      const idx = this.active_puzzle_idx[unit_id] || 0;
      const puzzle = puzzles[idx];
      if (!this.slot_states[puzzle.id]) {
        this.slot_states[puzzle.id] = {};
      }
      const filled_map = this.slot_states[puzzle.id];
      const slot_keys = Object.keys(puzzle.slots);
      const solved_count = slot_keys.filter((k) => Boolean(filled_map[k])).length;
      const is_done = solved_count === slot_keys.length || completed_set.indexOf(puzzle.id) !== -1;

      if (completed_set.indexOf(puzzle.id) !== -1 && solved_count < slot_keys.length) {
        // Restores visual lock state when returning to a previously completed puzzle.
        for (let i = 0; i < slot_keys.length; i += 1) {
          filled_map[slot_keys[i]] = puzzle.slots[slot_keys[i]].expected;
        }
      }

      const token_lookup = {};
      for (let i = 0; i < puzzle.tokens.length; i += 1) {
        token_lookup[puzzle.tokens[i].id] = puzzle.tokens[i];
      }
      const used_tokens = Object.values(filled_map);

      let html = '<div class="card">';
      html += '<div class="puzzle-header">' +
        '<div><h3>' + escapeHtml(puzzle.title) + '</h3>' +
        '<span class="meta-pill">' + escapeHtml(puzzle.source_tag) + '</span></div>' +
        (is_done ? '<span class="completion-badge">Ολοκληρώθηκε (' + slot_keys.length + '/' + slot_keys.length + ')</span>' : '<span class="meta-pill accent">' + solved_count + ' / ' + slot_keys.length + ' κενά</span>') +
        '</div>';

      if (puzzles.length > 1) {
        html += '<div class="lab-toolbar">';
        for (let i = 0; i < puzzles.length; i += 1) {
          const p = puzzles[i];
          const p_done = completed_set.indexOf(p.id) !== -1;
          html += '<button type="button" class="btn ' + (i === idx ? 'btn-primary' : 'btn-secondary') + '" data-pidx="' + i + '">' +
            escapeHtml(p.title.split(':')[0]) + (p_done ? ' [OK]' : '') + '</button>';
        }
        html += '</div>';
      }

      html += '<p class="muted-text">' + escapeHtml(puzzle.description) + ' Σύρετε ένα κομμάτι στο επισημασμένο κενό ή κάντε κλικ στο κομμάτι και έπειτα κλικ στο κενό.</p>';

      // Code canvas with inline dropzone targets.
      html += '<div class="code-stage">';
      for (let i = 0; i < puzzle.lines.length; i += 1) {
        const rendered_line = escapeHtml(puzzle.lines[i]).replace(/\{\{([a-zA-Z0-9_]+)\}\}/g, (_m, slot_id) => {
          const placed_id = filled_map[slot_id];
          if (placed_id && token_lookup[placed_id]) {
            return '<span class="drop-slot is-filled" data-slot-id="' + slot_id + '">' + escapeHtml(token_lookup[placed_id].label) + '</span>';
          }
          return '<button type="button" class="drop-slot" data-slot-id="' + slot_id + '" aria-label="Κενό κώδικα ' + slot_id + '">? ' + slot_id + '</button>';
        });
        html += '<div class="code-line"><span class="line-num">' + (i + 1) + '</span><span>' + rendered_line + '</span></div>';
      }
      html += '</div>';

      // Available token tray.
      html += '<div><div class="muted-text" style="margin-bottom:8px;">Διαθέσιμες Εντολές / Εκφράσεις (περιλαμβάνει παγίδες):</div>';
      html += '<div class="token-tray">';
      for (let i = 0; i < puzzle.tokens.length; i += 1) {
        const tok = puzzle.tokens[i];
        const is_used = used_tokens.indexOf(tok.id) !== -1;
        const is_sel = this.selected_token_id === tok.id && !is_used;
        html += '<button type="button" class="token-chip ' + (is_used ? 'is-used' : '') + (is_sel ? ' is-selected' : '') + '" ' +
          'draggable="' + (is_used ? 'false' : 'true') + '" data-token-id="' + tok.id + '"' + (is_used ? ' disabled' : '') + '>' +
          escapeHtml(tok.label) + '</button>';
      }
      html += '</div></div>';

      html += '<div class="lab-toolbar">' +
        '<button type="button" class="btn btn-secondary" id="dropin_hint_btn">Υπόδειξη</button>' +
        '<button type="button" class="btn btn-ghost" id="dropin_reset_btn">Επαναφορά</button>' +
        '</div>';

      if (this.feedback_msg) {
        html += '<div class="quiz-feedback ' + (this.feedback_kind === 'correct' ? 'is-correct' : (this.feedback_kind === 'wrong' ? 'is-wrong' : '')) + '">' +
          '<div>' + escapeHtml(this.feedback_msg) + '</div></div>';
      }
      html += '</div>';

      container_el.innerHTML = html;

      // Bind puzzle selector pills.
      const p_btns = container_el.querySelectorAll('[data-pidx]');
      for (let i = 0; i < p_btns.length; i += 1) {
        p_btns[i].addEventListener('click', (evt) => {
          this.active_puzzle_idx[unit_id] = Number(evt.currentTarget.getAttribute('data-pidx'));
          this.selected_token_id = null;
          this.feedback_msg = '';
          this.renderPuzzle(container_el, unit_id, completed_set, on_complete_cb);
        });
      }

      // Bind draggable and clickable token chips.
      const chips = container_el.querySelectorAll('.token-chip:not(:disabled)');
      for (let i = 0; i < chips.length; i += 1) {
        chips[i].addEventListener('click', (evt) => {
          const tid = evt.currentTarget.getAttribute('data-token-id');
          this.selected_token_id = this.selected_token_id === tid ? null : tid;
          this.renderPuzzle(container_el, unit_id, completed_set, on_complete_cb);
        });
        chips[i].addEventListener('dragstart', (evt) => {
          const tid = evt.currentTarget.getAttribute('data-token-id');
          this.dragged_token_id = tid;
          this.selected_token_id = tid;
          if (evt.dataTransfer) {
            evt.dataTransfer.setData('text/plain', tid);
          }
        });
      }

      // Bind dropzone slots (HTML5 drop + click-to-place).
      const slot_els = container_el.querySelectorAll('.drop-slot:not(.is-filled)');
      for (let i = 0; i < slot_els.length; i += 1) {
        slot_els[i].addEventListener('dragover', (evt) => {
          evt.preventDefault();
          evt.currentTarget.classList.add('is-over');
        });
        slot_els[i].addEventListener('dragleave', (evt) => {
          evt.currentTarget.classList.remove('is-over');
        });
        slot_els[i].addEventListener('drop', (evt) => {
          evt.preventDefault();
          evt.currentTarget.classList.remove('is-over');
          const slot_id = evt.currentTarget.getAttribute('data-slot-id');
          const dropped_id = (evt.dataTransfer && evt.dataTransfer.getData('text/plain')) || this.dragged_token_id;
          if (dropped_id) {
            this.handlePlaceToken(slot_id, dropped_id, container_el, unit_id, completed_set, on_complete_cb);
          }
        });
        slot_els[i].addEventListener('click', (evt) => {
          const slot_id = evt.currentTarget.getAttribute('data-slot-id');
          if (!this.selected_token_id) {
            this.feedback_kind = 'neutral';
            this.feedback_msg = 'Επιλέξτε πρώτα ένα κομμάτι από τα διαθέσιμα παρακάτω (ή σύρετέ το εδώ).';
            this.renderPuzzle(container_el, unit_id, completed_set, on_complete_cb);
            return;
          }
          this.handlePlaceToken(slot_id, this.selected_token_id, container_el, unit_id, completed_set, on_complete_cb);
        });
      }

      container_el.querySelector('#dropin_hint_btn').addEventListener('click', () => {
        const next_open = slot_keys.find((k) => !filled_map[k]);
        if (next_open) {
          this.feedback_kind = 'neutral';
          this.feedback_msg = 'Υπόδειξη (' + next_open + '): ' + puzzle.slots[next_open].hint;
          this.renderPuzzle(container_el, unit_id, completed_set, on_complete_cb);
        }
      });

      container_el.querySelector('#dropin_reset_btn').addEventListener('click', () => {
        this.slot_states[puzzle.id] = {};
        this.selected_token_id = null;
        this.feedback_kind = 'neutral';
        this.feedback_msg = 'Η άσκηση επαναφέρθηκε.';
        this.renderPuzzle(container_el, unit_id, completed_set, on_complete_cb);
      });
    }

    /**
     * Validates a placed token against the slot specification and updates game state.
     *
     * Args:
     *     slot_id (string): Target slot identifier inside the code snippet.
     *     token_id (string): Token identifier dropped or clicked by the student.
     *     container_el (HTMLElement): Host DOM element.
     *     unit_id (string): Active unit identifier.
     *     completed_set (Array<string>): Persisted completion list.
     *     on_complete_cb (Function): Completion callback.
     */
    handlePlaceToken(slot_id, token_id, container_el, unit_id, completed_set, on_complete_cb) {
      const puzzles = global_scope.MidtermApp.dropin_puzzles[unit_id];
      const puzzle = puzzles[this.active_puzzle_idx[unit_id] || 0];
      const slot_spec = puzzle.slots[slot_id];
      if (!slot_spec) {
        return;
      }

      if (token_id === slot_spec.expected) {
        this.slot_states[puzzle.id][slot_id] = token_id;
        this.selected_token_id = null;
        this.dragged_token_id = null;
        const slot_keys = Object.keys(puzzle.slots);
        const solved_now = slot_keys.filter((k) => Boolean(this.slot_states[puzzle.id][k])).length;
        if (solved_now === slot_keys.length) {
          this.feedback_kind = 'correct';
          this.feedback_msg = 'Άριστα! Όλα τα κενά της συνάρτησης συμπληρώθηκαν σωστά.';
          if (typeof on_complete_cb === 'function') {
            on_complete_cb(puzzle.id);
          }
        } else {
          this.feedback_kind = 'correct';
          this.feedback_msg = 'Σωστή τοποθέτηση στο ' + slot_id + '. Συνεχίστε στο επόμενο κενό.';
        }
        this.renderPuzzle(container_el, unit_id, completed_set, on_complete_cb);
      } else {
        this.feedback_kind = 'wrong';
        this.feedback_msg = 'Προσοχή στο ' + slot_id + ': ' + slot_spec.hint;
        const slot_btn = container_el.querySelector('[data-slot-id="' + slot_id + '"]');
        if (slot_btn) {
          slot_btn.classList.add('is-wrong');
          setTimeout(() => {
            this.renderPuzzle(container_el, unit_id, completed_set, on_complete_cb);
          }, 340);
        } else {
          this.renderPuzzle(container_el, unit_id, completed_set, on_complete_cb);
        }
      }
    }
  }

  global_scope.MidtermApp = global_scope.MidtermApp || {};
  global_scope.MidtermApp.dropin_engine = new DropInGameEngine();
})(window);
