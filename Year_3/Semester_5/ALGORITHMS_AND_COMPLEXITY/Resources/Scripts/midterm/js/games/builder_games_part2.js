(function (global_scope) {
  'use strict';

  /**
   * Escapes special HTML characters in text values.
   *
   * Args:
   *     raw_text (string): Raw string to sanitize.
   *
   * Returns:
   *     string: Safe escaped HTML string.
   */
  function escapeHtml(raw_text) {
    return String(raw_text)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  /**
   * Renders the Interactive 2x3 Maze Union-Find Game for Unit 04 (Recitation A Ch. 7 #3).
   *
   * Lets the student decide whether each wall merges two disjoint sets or creates a cycle.
   * Methods: mount(container_el, on_complete_cb), resetGame(), findRoot(node), applyWallDecision(should_remove, container_el, on_complete_cb), getCurrentSets().
   */
  class Unit04BuilderGame {
    /**
     * Initializes the 6-cell maze and 4 sequential wall choices.
     */
    constructor() {
      this.wall_sequence = [
        { u: 3, v: 6, label: '3-6' },
        { u: 2, v: 3, label: '2-3' },
        { u: 5, v: 6, label: '5-6' },
        { u: 2, v: 5, label: '2-5' }
      ];
      this.resetGame();
    }

    /**
     * Resets the maze Union-Find game back to its initial state.
     */
    resetAll() {
      this.resetGame();
    }

    /**
     * Resets Union-Find parent pointers and removed maze walls.
     */
    resetGame() {
      this.parent = [null, 1, 2, 3, 4, 5, 6];
      this.removed_walls = {};
      this.step_idx = 0;
      this.feedback_msg = '';
      this.feedback_kind = 'neutral';
    }

    /**
     * Finds the set representative root for a maze cell.
     *
     * Args:
     *     node (number): Cell index in 1..6.
     *
     * Returns:
     *     number: Root representative index.
     */
    findRoot(node) {
      let curr = node;
      while (this.parent[curr] !== curr) {
        curr = this.parent[curr];
      }
      return curr;
    }

    /**
     * Computes readable strings for all current disjoint sets in the maze.
     *
     * Returns:
     *     Array<string>: Formatted disjoint set strings.
     */
    getCurrentSets() {
      const groups = {};
      for (let i = 1; i <= 6; i += 1) {
        const r = this.findRoot(i);
        if (!groups[r]) {
          groups[r] = [];
        }
        groups[r].push(i);
      }
      return Object.values(groups).map((arr) => '{' + arr.join(', ') + '}');
    }

    /**
     * Evaluates the student's decision to remove or keep the active candidate wall.
     *
     * Args:
     *     should_remove (boolean): True if student chose to remove wall (union); false to keep.
     *     container_el (HTMLElement): Host DOM element.
     *     on_complete_cb (Function): Completion callback.
     *     on_reset_cb (Function): Reset callback.
     */
    applyWallDecision(should_remove, container_el, on_complete_cb, on_reset_cb) {
      if (this.step_idx >= this.wall_sequence.length) {
        return;
      }
      const wall = this.wall_sequence[this.step_idx];
      const ru = this.findRoot(wall.u);
      const rv = this.findRoot(wall.v);
      const are_disjoint = ru !== rv;

      if (should_remove === are_disjoint) {
        if (are_disjoint) {
          const keep = Math.min(ru, rv);
          const attach = Math.max(ru, rv);
          this.parent[attach] = keep;
          this.removed_walls[wall.label] = true;
        }
        this.step_idx += 1;
        this.feedback_kind = 'correct';
        if (this.step_idx === this.wall_sequence.length) {
          this.feedback_msg = 'Άριστα! Ο τοίχος 2-5 διατηρήθηκε για να μη σχηματιστεί κύκλος. Τελικές συνιστώσες: {1}, {4}, {2, 3, 5, 6}.';
          if (typeof on_complete_cb === 'function') {
            on_complete_cb('game_04');
          }
        } else {
          this.feedback_msg = are_disjoint
            ? 'Σωστά! Ο τοίχος ' + wall.label + ' ένωσε δύο ξένα σύνολα και αφαιρέθηκε.'
            : 'Σωστά! Τα κελιά ανήκουν ήδη στο ίδιο σύνολο.';
        }
      } else {
        this.feedback_kind = 'wrong';
        this.feedback_msg = are_disjoint
          ? 'Λάθος: τα κελιά ' + wall.u + ' και ' + wall.v + ' ανήκουν σε ΔΙΑΦΟΡΕΤΙΚΑ σύνολα (find(' + wall.u + ')=' + ru + ' != find(' + wall.v + ')=' + rv + '), άρα ο τοίχος πρέπει να αφαιρεθεί!'
          : 'Παγίδα κύκλου! Τα κελιά ' + wall.u + ' και ' + wall.v + ' έχουν ήδη την ίδια ρίζα (' + ru + '), άρα ΔΕΝ πρέπει να αφαιρεθεί ο τοίχος!';
      }
      this.mount(container_el, on_complete_cb, on_reset_cb);
    }

    /**
     * Mounts the interactive 2x3 maze Union-Find game inside the host container.
     *
     * Args:
     *     container_el (HTMLElement): Host DOM element.
     *     on_complete_cb (Function): Completion callback.
     *     on_reset_cb (Function): Reset callback.
     */
    mount(container_el, on_complete_cb, on_reset_cb) {
      const is_done = this.step_idx >= this.wall_sequence.length;
      const active_wall = is_done ? null : this.wall_sequence[this.step_idx];
      const sets_list = this.getCurrentSets();

      const cellClasses = (cell_id) => {
        const cls = ['maze-cell'];
        if (active_wall && (active_wall.u === cell_id || active_wall.v === cell_id)) {
          cls.push('is-active');
        }
        if ((cell_id === 2 && this.removed_walls['2-3']) || (cell_id === 5 && this.removed_walls['5-6'])) {
          cls.push('is-open-right');
        }
        if ((cell_id === 3 && this.removed_walls['2-3']) || (cell_id === 6 && this.removed_walls['5-6'])) {
          cls.push('is-open-left');
        }
        if ((cell_id === 2 && this.removed_walls['2-5']) || (cell_id === 3 && this.removed_walls['3-6'])) {
          cls.push('is-open-bottom');
        }
        if ((cell_id === 5 && this.removed_walls['2-5']) || (cell_id === 6 && this.removed_walls['3-6'])) {
          cls.push('is-open-top');
        }
        return cls.join(' ');
      };

      let html = '<div class="card">';
      html += '<div class="puzzle-header">' +
        '<div><h3>Παιχνίδι Κατασκευής Λαβυρίνθου με Union-Find (2&times;3)</h3>' +
        '<span class="meta-pill">Φροντιστήριο A — Κεφ. 7 #3</span></div>' +
        (is_done ? '<span class="completion-badge">Ολοκληρώθηκε (4/4)</span>' : '<span class="meta-pill accent">Βήμα ' + (this.step_idx + 1) + ' / 4</span>') +
        '</div>';

      html += '<p class="muted-text">Αποφασίστε σε κάθε βήμα αν ο υποψήφιος τοίχος πρέπει να διαγραφεί (ένωση ξένων συνόλων) ή να διατηρηθεί (αποφυγή κύκλου).</p>';

      html += '<div class="maze-grid">';
      for (let id = 1; id <= 6; id += 1) {
        html += '<div class="' + cellClasses(id) + '">' +
          '<span>' + id + '</span>' +
          '<span class="array-cell-idx">ρίζα ' + this.findRoot(id) + '</span>' +
        '</div>';
      }
      html += '</div>';

      html += '<div class="card-deep"><strong>Τρέχοντα Ξένα Σύνολα:</strong> <code>' + escapeHtml(sets_list.join('  ')) + '</code></div>';

      if (!is_done && active_wall) {
        html += '<div class="lab-toolbar">' +
          '<span class="meta-pill accent">Εξέταση Τοίχου: ' + active_wall.label + '</span>' +
          '<button type="button" class="btn btn-primary" id="g04_remove_btn">Αφαίρεση Τοίχου (Union)</button>' +
          '<button type="button" class="btn btn-secondary" id="g04_keep_btn">Διατήρηση Τοίχου (Ίδιο Σύνολο)</button>' +
          '<button type="button" class="btn btn-ghost" id="g04_reset_btn">Επαναφορά</button>' +
        '</div>';
      } else {
        html += '<div class="lab-toolbar"><button type="button" class="btn btn-ghost" id="g04_reset_btn">Παίξτε Ξανά</button></div>';
      }

      if (this.feedback_msg) {
        html += '<div class="quiz-feedback ' + (this.feedback_kind === 'correct' ? 'is-correct' : 'is-wrong') + '">' +
          '<div>' + escapeHtml(this.feedback_msg) + '</div></div>';
      }
      html += '</div>';

      container_el.innerHTML = html;

      const rem_btn = container_el.querySelector('#g04_remove_btn');
      const keep_btn = container_el.querySelector('#g04_keep_btn');
      if (rem_btn) {
        rem_btn.addEventListener('click', () => this.applyWallDecision(true, container_el, on_complete_cb, on_reset_cb));
      }
      if (keep_btn) {
        keep_btn.addEventListener('click', () => this.applyWallDecision(false, container_el, on_complete_cb, on_reset_cb));
      }
      container_el.querySelector('#g04_reset_btn').addEventListener('click', () => {
        this.resetGame();
        if (typeof on_reset_cb === 'function') {
          on_reset_cb('game_04');
        }
        this.mount(container_el, on_complete_cb, on_reset_cb);
      });
    }
  }

  /**
   * Renders the Manual Decision Tree Leaf Builder for n = 3 in Unit 05.
   *
   * Users drag or click each of the 3! = 6 permutations to its exact leaf path in the SVG decision tree.
   * Methods: mount(container_el, on_complete_cb), placeLeaf(leaf_id, perm_id, container_el, on_complete_cb).
   */
  class Unit05BuilderGame {
    /**
     * Initializes the 6 decision-tree leaf targets and permutation chips.
     */
    constructor() {
      this.leaves = [
        { id: 'l1', path_hint: 'x1<x2 (Ναι) -> x2<x3 (Ναι)', expected: 'p123', label: 'x1, x2, x3' },
        { id: 'l2', path_hint: 'x1<x2 (Ναι) -> x2<x3 (Όχι) -> x1<x3 (Ναι)', expected: 'p132', label: 'x1, x3, x2' },
        { id: 'l3', path_hint: 'x1<x2 (Ναι) -> x2<x3 (Όχι) -> x1<x3 (Όχι)', expected: 'p312', label: 'x3, x1, x2' },
        { id: 'l4', path_hint: 'x1<x2 (Όχι) -> x1<x3 (Ναι)', expected: 'p213', label: 'x2, x1, x3' },
        { id: 'l5', path_hint: 'x1<x2 (Όχι) -> x1<x3 (Όχι) -> x2<x3 (Ναι)', expected: 'p231', label: 'x2, x3, x1' },
        { id: 'l6', path_hint: 'x1<x2 (Όχι) -> x1<x3 (Όχι) -> x2<x3 (Όχι)', expected: 'p321', label: 'x3, x2, x1' }
      ];
      this.tokens = [
        { id: 'p312', label: '(x3, x1, x2)' },
        { id: 'p123', label: '(x1, x2, x3)' },
        { id: 'p231', label: '(x2, x3, x1)' },
        { id: 'p132', label: '(x1, x3, x2)' },
        { id: 'p321', label: '(x3, x2, x1)' },
        { id: 'p213', label: '(x2, x1, x3)' }
      ];
      this.placed = {};
      this.selected_perm = null;
      this.drag_perm = null;
      this.feedback_msg = '';
      this.feedback_kind = 'neutral';
    }

    /**
     * Resets the Decision Tree leaf builder back to its initial empty state.
     */
    resetAll() {
      this.placed = {};
      this.selected_perm = null;
      this.drag_perm = null;
      this.feedback_msg = '';
      this.feedback_kind = 'neutral';
    }

    /**
     * Validates placing a permutation chip into a decision-tree leaf slot.
     *
     * Args:
     *     leaf_id (string): Leaf target identifier ('l1'..'l6').
     *     perm_id (string): Selected permutation token ID.
     *     container_el (HTMLElement): Host DOM element.
     *     on_complete_cb (Function): Completion callback.
     *     on_reset_cb (Function): Reset callback.
     */
    placeLeaf(leaf_id, perm_id, container_el, on_complete_cb, on_reset_cb) {
      const leaf = this.leaves.find((l) => l.id === leaf_id);
      if (!leaf) {
        return;
      }
      if (leaf.expected === perm_id) {
        this.placed[leaf_id] = perm_id;
        this.selected_perm = null;
        this.feedback_kind = 'correct';
        const done = Object.keys(this.placed).length;
        if (done === this.leaves.length) {
          this.feedback_msg = 'Εξαιρετικά! Ολοκληρώσατε και τα 3! = 6 φύλλα του βέλτιστου δέντρου αποφάσεων (ύψος h = 3).';
          if (typeof on_complete_cb === 'function') {
            on_complete_cb('game_05');
          }
        } else {
          this.feedback_msg = 'Σωστό φύλλο (' + leaf.label + ') για το μονοπάτι ' + leaf.path_hint + '.';
        }
      } else {
        this.feedback_kind = 'wrong';
        this.feedback_msg = 'Λάθος φύλλο για το μονοπάτι: ' + leaf.path_hint + '. Ακολουθήστε προσεκτικά τις ανισότητες!';
      }
      this.mount(container_el, on_complete_cb, on_reset_cb);
    }

    /**
     * Mounts the n=3 Decision Tree Leaf Builder inside the host container.
     *
     * Args:
     *     container_el (HTMLElement): Host DOM element.
     *     on_complete_cb (Function): Completion callback.
     *     on_reset_cb (Function): Reset callback.
     */
    mount(container_el, on_complete_cb, on_reset_cb) {
      const done_cnt = Object.keys(this.placed).length;
      const is_done = done_cnt === this.leaves.length;
      const used_perms = Object.values(this.placed);

      // Draws the internal comparison tree matching Section 2.4 of Unit 05.
      const svg_tree =
        '<svg class="svg-stage" viewBox="0 0 680 210">' +
          '<line x1="340" y1="30" x2="170" y2="90" stroke="var(--border-strong)" stroke-width="2" />' +
          '<line x1="340" y1="30" x2="510" y2="90" stroke="var(--border-strong)" stroke-width="2" />' +
          '<text x="242" y="54" fill="var(--accent-primary)" font-size="11" font-family="var(--font-mono)">Ναι</text>' +
          '<text x="430" y="54" fill="var(--ink-muted)" font-size="11" font-family="var(--font-mono)">Όχι</text>' +
          '<line x1="170" y1="90" x2="72" y2="180" stroke="var(--border-strong)" stroke-width="2" />' +
          '<line x1="170" y1="90" x2="236" y2="150" stroke="var(--border-strong)" stroke-width="2" />' +
          '<line x1="236" y1="150" x2="184" y2="195" stroke="var(--border-strong)" stroke-width="2" />' +
          '<line x1="236" y1="150" x2="288" y2="195" stroke="var(--border-strong)" stroke-width="2" />' +
          '<line x1="510" y1="90" x2="405" y2="180" stroke="var(--border-strong)" stroke-width="2" />' +
          '<line x1="510" y1="90" x2="578" y2="150" stroke="var(--border-strong)" stroke-width="2" />' +
          '<line x1="578" y1="150" x2="526" y2="195" stroke="var(--border-strong)" stroke-width="2" />' +
          '<line x1="578" y1="150" x2="628" y2="195" stroke="var(--border-strong)" stroke-width="2" />' +
          '<rect x="292" y="14" width="96" height="30" rx="6" fill="var(--accent-soft)" stroke="var(--accent-primary)" stroke-width="2" />' +
          '<text x="340" y="34" text-anchor="middle" fill="var(--ink-bright)" font-family="var(--font-mono)" font-size="12" font-weight="700">x1 &lt; x2 ?</text>' +
          '<rect x="124" y="74" width="92" height="28" rx="6" fill="var(--bg-surface-elevated)" stroke="var(--ink-muted)" stroke-width="1.5" />' +
          '<text x="170" y="92" text-anchor="middle" fill="var(--ink-bright)" font-family="var(--font-mono)" font-size="12">x2 &lt; x3 ?</text>' +
          '<rect x="464" y="74" width="92" height="28" rx="6" fill="var(--bg-surface-elevated)" stroke="var(--ink-muted)" stroke-width="1.5" />' +
          '<text x="510" y="92" text-anchor="middle" fill="var(--ink-bright)" font-family="var(--font-mono)" font-size="12">x1 &lt; x3 ?</text>' +
          '<rect x="190" y="135" width="92" height="28" rx="6" fill="var(--bg-surface-elevated)" stroke="var(--ink-muted)" stroke-width="1.5" />' +
          '<text x="236" y="153" text-anchor="middle" fill="var(--ink-bright)" font-family="var(--font-mono)" font-size="12">x1 &lt; x3 ?</text>' +
          '<rect x="532" y="135" width="92" height="28" rx="6" fill="var(--bg-surface-elevated)" stroke="var(--ink-muted)" stroke-width="1.5" />' +
          '<text x="578" y="153" text-anchor="middle" fill="var(--ink-bright)" font-family="var(--font-mono)" font-size="12">x2 &lt; x3 ?</text>' +
          '<text x="72" y="198" text-anchor="middle" fill="var(--accent-primary)" font-family="var(--font-mono)" font-size="11">L1</text>' +
          '<text x="184" y="206" text-anchor="middle" fill="var(--accent-primary)" font-family="var(--font-mono)" font-size="11">L2</text>' +
          '<text x="288" y="206" text-anchor="middle" fill="var(--accent-primary)" font-family="var(--font-mono)" font-size="11">L3</text>' +
          '<text x="405" y="198" text-anchor="middle" fill="var(--accent-primary)" font-family="var(--font-mono)" font-size="11">L4</text>' +
          '<text x="526" y="206" text-anchor="middle" fill="var(--accent-primary)" font-family="var(--font-mono)" font-size="11">L5</text>' +
          '<text x="628" y="206" text-anchor="middle" fill="var(--accent-primary)" font-family="var(--font-mono)" font-size="11">L6</text>' +
        '</svg>';

      let html = '<div class="card">';
      html += '<div class="puzzle-header">' +
        '<div><h3>Χειροκίνητος Κατασκευαστής Φύλλων Δέντρου Αποφάσεων (n = 3)</h3>' +
        '<span class="meta-pill">Σημείωση 05 — 3! = 6 Μεταθέσεις</span></div>' +
        (is_done ? '<span class="completion-badge">Ολοκληρώθηκε (6/6)</span>' : '<span class="meta-pill accent">' + done_cnt + ' / 6 φύλλα</span>') +
        '</div>';

      html += '<p class="muted-text">Ακολουθήστε τα μονοπάτια συγκρίσεων (αριστερά = Ναι, δεξιά = Όχι) και τοποθετήστε την αντίστοιχη διάταξη εξόδου σε κάθε φύλλο L1..L6.</p>';
      html += svg_tree;

      html += '<div class="grid-3">';
      for (let i = 0; i < this.leaves.length; i += 1) {
        const l = this.leaves[i];
        const filled = Boolean(this.placed[l.id]);
        html += '<div class="card-deep">' +
          '<div class="muted-text" style="font-size:0.8rem;"><strong>L' + (i + 1) + ':</strong> ' + escapeHtml(l.path_hint) + '</div>' +
          '<button type="button" class="drop-slot ' + (filled ? 'is-filled' : '') + '" data-leaf-id="' + l.id + '" style="width:100%;margin-top:8px;">' +
            (filled ? '(' + escapeHtml(l.label) + ')' : 'Τοποθέτηση φύλλου L' + (i + 1)) +
          '</button>' +
        '</div>';
      }
      html += '</div>';

      html += '<div class="token-tray">';
      for (let i = 0; i < this.tokens.length; i += 1) {
        const tok = this.tokens[i];
        const is_used = used_perms.indexOf(tok.id) !== -1;
        const is_sel = this.selected_perm === tok.id && !is_used;
        html += '<button type="button" class="token-chip ' + (is_used ? 'is-used' : '') + (is_sel ? ' is-selected' : '') + '" ' +
          'draggable="' + (is_used ? 'false' : 'true') + '" data-perm-id="' + tok.id + '"' + (is_used ? ' disabled' : '') + '>' +
          escapeHtml(tok.label) + '</button>';
      }
      html += '</div>';

      html += '<div class="lab-toolbar"><button type="button" class="btn btn-ghost" id="g05_reset_btn">Επαναφορά</button></div>';
      if (this.feedback_msg) {
        html += '<div class="quiz-feedback ' + (this.feedback_kind === 'correct' ? 'is-correct' : 'is-wrong') + '">' +
          '<div>' + escapeHtml(this.feedback_msg) + '</div></div>';
      }
      html += '</div>';

      container_el.innerHTML = html;

      const chips = container_el.querySelectorAll('[data-perm-id]:not(:disabled)');
      for (let i = 0; i < chips.length; i += 1) {
        chips[i].addEventListener('click', (evt) => {
          const pid = evt.currentTarget.getAttribute('data-perm-id');
          this.selected_perm = this.selected_perm === pid ? null : pid;
          this.mount(container_el, on_complete_cb, on_reset_cb);
        });
        chips[i].addEventListener('dragstart', (evt) => {
          this.drag_perm = evt.currentTarget.getAttribute('data-perm-id');
          this.selected_perm = this.drag_perm;
        });
      }

      const slots = container_el.querySelectorAll('[data-leaf-id]:not(.is-filled)');
      for (let i = 0; i < slots.length; i += 1) {
        slots[i].addEventListener('dragover', (evt) => { evt.preventDefault(); evt.currentTarget.classList.add('is-over'); });
        slots[i].addEventListener('dragleave', (evt) => { evt.currentTarget.classList.remove('is-over'); });
        slots[i].addEventListener('drop', (evt) => {
          evt.preventDefault();
          evt.currentTarget.classList.remove('is-over');
          const lid = evt.currentTarget.getAttribute('data-leaf-id');
          if (this.drag_perm) {
            this.placeLeaf(lid, this.drag_perm, container_el, on_complete_cb, on_reset_cb);
          }
        });
        slots[i].addEventListener('click', (evt) => {
          const lid = evt.currentTarget.getAttribute('data-leaf-id');
          if (this.selected_perm) {
            this.placeLeaf(lid, this.selected_perm, container_el, on_complete_cb, on_reset_cb);
          }
        });
      }

      container_el.querySelector('#g05_reset_btn').addEventListener('click', () => {
        this.resetAll();
        if (typeof on_reset_cb === 'function') {
          on_reset_cb('game_05');
        }
        this.mount(container_el, on_complete_cb, on_reset_cb);
      });
    }
  }

  /**
   * Renders the Manual Interactive Huffman Tree Builder Game for Unit 06.
   *
   * Users merge active lowest-frequency nodes step by step until a single Huffman root forms.
   * Methods: mount(container_el, on_complete_cb), loadPreset(preset_key), tryMergeNodes(id_a, id_b, container_el, on_complete_cb), renderForestSvg().
   */
  class Unit06BuilderGame {
    /**
     * Initializes the manual Huffman tree builder with Exercise 1 and synthetic presets.
     */
    constructor() {
      this.preset = 'ex1';
      this.loadPreset('ex1');
    }

    /**
     * Loads initial frequency leaf nodes for the chosen preset.
     *
     * Args:
     *     preset_key (string): 'ex1' (6 symbols) or 'data' (4 symbols).
     */
    loadPreset(preset_key) {
      this.preset = preset_key;
      const spec = preset_key === 'ex1'
        ? [['A', 15], ['B', 7], ['C', 6], ['D', 6], ['E', 5], ['F', 2]]
        : [['A', 5], ['D', 3], ['T', 2], ['S', 1]];
      this.forest = spec.map((pair, i) => ({
        id: 'leaf_' + i,
        label: pair[0],
        freq: pair[1],
        left: null,
        right: null
      }));
      this.next_internal = 1;
      this.selected_node_id = null;
      this.feedback_msg = '';
      this.feedback_kind = 'neutral';
    }

    /**
     * Resets the Huffman builder back to default ex1 preset.
     */
    resetAll() {
      this.loadPreset('ex1');
    }

    /**
     * Validates and performs a greedy merge of two selected Huffman subtrees.
     *
     * Args:
     *     id_a (string): First subtree root ID.
     *     id_b (string): Second subtree root ID.
     *     container_el (HTMLElement): Host DOM element.
     *     on_complete_cb (Function): Completion callback.
     *     on_reset_cb (Function): Reset callback.
     */
    tryMergeNodes(id_a, id_b, container_el, on_complete_cb, on_reset_cb) {
      if (id_a === id_b) {
        this.selected_node_id = null;
        this.mount(container_el, on_complete_cb, on_reset_cb);
        return;
      }
      const n1 = this.forest.find((t) => t.id === id_a);
      const n2 = this.forest.find((t) => t.id === id_b);
      if (!n1 || !n2) {
        return;
      }

      const sorted_freqs = this.forest.map((t) => t.freq).sort((a, b) => a - b);
      const min_sum = sorted_freqs[0] + sorted_freqs[1];
      const chosen_sum = n1.freq + n2.freq;

      // Accepts any pair achieving the exact two-minimum frequency sum (handles equal-frequency ties).
      if (chosen_sum !== min_sum) {
        this.feedback_kind = 'wrong';
        this.feedback_msg = 'Λάθος συγχώνευση (' + n1.freq + ' + ' + n2.freq + ' = ' + chosen_sum + '): Πρέπει να ενώσετε τους 2 κόμβους με τις ΕΛΑΧΙΣΤΕΣ συχνότητες (' + sorted_freqs[0] + ' και ' + sorted_freqs[1] + ').';
        this.selected_node_id = null;
        this.mount(container_el, on_complete_cb, on_reset_cb);
        return;
      }

      const left_child = n1.freq <= n2.freq ? n1 : n2;
      const right_child = left_child === n1 ? n2 : n1;
      const merged = {
        id: 'N' + this.next_internal,
        label: 'N' + this.next_internal,
        freq: chosen_sum,
        left: left_child,
        right: right_child
      };
      this.next_internal += 1;
      this.forest = this.forest.filter((t) => t.id !== id_a && t.id !== id_b);
      this.forest.push(merged);
      this.selected_node_id = null;

      if (this.forest.length === 1) {
        const computeBits = (node, depth) => {
          if (!node.left && !node.right) {
            return node.freq * depth;
          }
          return computeBits(node.left, depth + 1) + computeBits(node.right, depth + 1);
        };
        const total_bits = computeBits(merged, 0);
        this.feedback_kind = 'correct';
        this.feedback_msg = 'Ολοκληρώθηκε το Δέντρο Huffman! Συνολικό μήκος B(T) = ' + total_bits + ' bits.';
        if (typeof on_complete_cb === 'function') {
          on_complete_cb('game_06');
        }
      } else {
        this.feedback_kind = 'correct';
        this.feedback_msg = 'Συγχωνεύτηκαν (' + left_child.label + ':' + left_child.freq + ') + (' + right_child.label + ':' + right_child.freq + ') -> ' + merged.label + '(' + merged.freq + ').';
      }
      this.mount(container_el, on_complete_cb, on_reset_cb);
    }

    /**
     * Renders the current forest of Huffman trees as an SVG diagram.
     *
     * Returns:
     *     string: SVG markup showing all active trees with 0/1 edge labels.
     */
    renderForestSvg() {
      let leaf_cursor = 0;
      let max_depth = 0;
      const pos_map = new Map();

      const layoutTree = (node, depth) => {
        if (depth > max_depth) { max_depth = depth; }
        if (!node.left && !node.right) {
          const x = 44 + leaf_cursor * 78;
          leaf_cursor += 1;
          pos_map.set(node, { x: x, y: 34 + depth * 54 });
          return x;
        }
        const lx = layoutTree(node.left, depth + 1);
        const rx = layoutTree(node.right, depth + 1);
        const mx = (lx + rx) / 2;
        pos_map.set(node, { x: mx, y: 34 + depth * 54 });
        return mx;
      };

      for (let i = 0; i < this.forest.length; i += 1) {
        layoutTree(this.forest[i], 0);
      }

      const width = Math.max(580, leaf_cursor * 78 + 30);
      const height = Math.max(150, (max_depth + 1) * 54 + 34);
      let edges = '';
      let nodes = '';

      const drawSubtree = (node, is_root) => {
        const p = pos_map.get(node);
        if (node.left && node.right) {
          const lp = pos_map.get(node.left);
          const rp = pos_map.get(node.right);
          edges += '<line x1="' + p.x + '" y1="' + p.y + '" x2="' + lp.x + '" y2="' + lp.y + '" stroke="var(--border-strong)" stroke-width="2" />';
          edges += '<text x="' + ((p.x + lp.x) / 2 - 10) + '" y="' + ((p.y + lp.y) / 2) + '" fill="var(--accent-primary)" font-family="var(--font-mono)" font-size="11">0</text>';
          edges += '<line x1="' + p.x + '" y1="' + p.y + '" x2="' + rp.x + '" y2="' + rp.y + '" stroke="var(--border-strong)" stroke-width="2" />';
          edges += '<text x="' + ((p.x + rp.x) / 2 + 6) + '" y="' + ((p.y + rp.y) / 2) + '" fill="var(--accent-primary)" font-family="var(--font-mono)" font-size="11">1</text>';
          drawSubtree(node.left, false);
          drawSubtree(node.right, false);
        }
        const is_sel = is_root && this.selected_node_id === node.id;
        const text = (!node.left && !node.right) ? node.label + ':' + node.freq : String(node.freq);
        nodes += '<g class="' + (is_root ? 'svg-node-interactive' : '') + (is_sel ? ' svg-node-selected' : '') + '" ' + (is_root ? 'data-hf-node="' + node.id + '"' : '') + '>' +
          '<circle cx="' + p.x + '" cy="' + p.y + '" r="18" fill="' + (is_sel ? 'var(--accent-primary)' : 'var(--bg-surface-elevated)') + '" stroke="' + (is_root ? 'var(--accent-primary)' : 'var(--ink-muted)') + '" stroke-width="2" />' +
          '<text x="' + p.x + '" y="' + (p.y + 4) + '" text-anchor="middle" fill="' + (is_sel ? 'var(--ink-on-accent)' : 'var(--ink-bright)') + '" font-family="var(--font-mono)" font-size="11" font-weight="700">' + escapeHtml(text) + '</text>' +
        '</g>';
      };

      for (let i = 0; i < this.forest.length; i += 1) {
        drawSubtree(this.forest[i], true);
      }

      return '<svg class="svg-stage" viewBox="0 0 ' + width + ' ' + height + '">' + edges + nodes + '</svg>';
    }

    /**
     * Mounts the manual Huffman tree builder inside the host container.
     *
     * Args:
     *     container_el (HTMLElement): Host DOM element.
     *     on_complete_cb (Function): Completion callback.
     *     on_reset_cb (Function): Reset callback.
     */
    mount(container_el, on_complete_cb, on_reset_cb) {
      const is_done = this.forest.length === 1;
      let html = '<div class="card">';
      html += '<div class="puzzle-header">' +
        '<div><h3>Χειροκίνητος Κατασκευαστής Δέντρου Huffman</h3>' +
        '<span class="meta-pill">Άσκηση 1 — Συγχώνευση 2 Ελάχιστων</span></div>' +
        (is_done ? '<span class="completion-badge">Δέντρο Ολοκληρώθηκε</span>' : '<span class="meta-pill accent">' + this.forest.length + ' εναπομείναντα δέντρα</span>') +
        '</div>';

      html += '<div class="lab-toolbar">' +
        '<button type="button" class="btn ' + (this.preset === 'ex1' ? 'btn-primary' : 'btn-secondary') + '" data-hfpre="ex1">Άσκηση 1 (A:15..F:2)</button>' +
        '<button type="button" class="btn ' + (this.preset === 'data' ? 'btn-primary' : 'btn-secondary') + '" data-hfpre="data">Συνθετικό "DATA" (4 σύμβολα)</button>' +
        '<button type="button" class="btn btn-ghost" id="g06_reset_btn">Επαναφορά</button>' +
        '</div>';

      html += '<p class="muted-text">Επιλέξτε διαδοχικά δύο ρίζες (κάντε κλικ σε 2 ρίζες στο δέντρο ή στα πλακίδια παρακάτω) για να τις συγχωνεύσετε. Πρέπει κάθε φορά να ενώνετε τις <strong>δύο μικρότερες συχνότητες</strong>.</p>';

      if (!is_done) {
        html += '<div class="token-tray">';
        for (let i = 0; i < this.forest.length; i += 1) {
          const t = this.forest[i];
          const is_sel = this.selected_node_id === t.id;
          html += '<button type="button" class="token-chip ' + (is_sel ? 'is-selected' : '') + '" data-hf-node="' + t.id + '">' +
            escapeHtml(t.label + ' (' + t.freq + ')') + '</button>';
        }
        html += '</div>';
      }

      html += this.renderForestSvg();

      if (this.feedback_msg) {
        html += '<div class="quiz-feedback ' + (this.feedback_kind === 'correct' ? 'is-correct' : 'is-wrong') + '">' +
          '<div>' + escapeHtml(this.feedback_msg) + '</div></div>';
      }
      html += '</div>';

      container_el.innerHTML = html;

      const pre_btns = container_el.querySelectorAll('[data-hfpre]');
      for (let i = 0; i < pre_btns.length; i += 1) {
        pre_btns[i].addEventListener('click', (evt) => {
          this.loadPreset(evt.currentTarget.getAttribute('data-hfpre'));
          if (typeof on_reset_cb === 'function') {
            on_reset_cb('game_06');
          }
          this.mount(container_el, on_complete_cb, on_reset_cb);
        });
      }
      container_el.querySelector('#g06_reset_btn').addEventListener('click', () => {
        this.loadPreset(this.preset);
        if (typeof on_reset_cb === 'function') {
          on_reset_cb('game_06');
        }
        this.mount(container_el, on_complete_cb, on_reset_cb);
      });

      const node_els = container_el.querySelectorAll('[data-hf-node]');
      for (let i = 0; i < node_els.length; i += 1) {
        node_els[i].addEventListener('click', (evt) => {
          const nid = evt.currentTarget.getAttribute('data-hf-node');
          if (this.forest.length <= 1) {
            return;
          }
          if (this.selected_node_id === null) {
            this.selected_node_id = nid;
            this.mount(container_el, on_complete_cb, on_reset_cb);
          } else {
            this.tryMergeNodes(this.selected_node_id, nid, container_el, on_complete_cb, on_reset_cb);
          }
        });
      }
    }
  }

  /**
   * Renders the Pareto Dominated-Point Eliminator & Master Theorem Matcher for Unit 07 (Recitation B Ch. 11).
   *
   * Combines geometric Pareto pruning (#5) and asymptotic recurrence matching (#2).
   * Methods: mount(container_el, on_complete_cb), tryEliminatePoint(pt_id, container_el, on_complete_cb), tryMatchRecurrence(rec_id, tok_id, container_el, on_complete_cb).
   */
  class Unit07BuilderGame {
    /**
     * Initializes Recitation B Ch. 11 #5 points and #2 recurrences.
     */
    constructor() {
      this.pareto_points = [
        { id: 'pt1', x: 5, y: 6, dominated: false, dom_by: '' },
        { id: 'pt2', x: 3, y: 9, dominated: false, dom_by: '' },
        { id: 'pt3', x: 4, y: 5, dominated: true, dom_by: '(5, 6)' },
        { id: 'pt4', x: 10, y: 1, dominated: false, dom_by: '' },
        { id: 'pt5', x: 7, y: 2, dominated: false, dom_by: '' },
        { id: 'pt6', x: 9, y: 0, dominated: true, dom_by: '(10, 1)' },
        { id: 'pt7', x: 0, y: 9, dominated: false, dom_by: '' }
      ];
      this.eliminated = {};
      this.recurrences = [
        { id: 'r1', expr: 'T(n) = 2T(n/2) + n', expected: 'm_nlogn_2', hint: 'a=2, b=2 -> log_2(2)=1, Περίπτωση 2' },
        { id: 'r2', expr: 'T(n) = 7T(n/3) + n', expected: 'm_n177', hint: 'log_3(7) ~ 1.77 > 1, Περίπτωση 1' },
        { id: 'r3', expr: 'T(n) = 8T(n/2) + n^2', expected: 'm_n3', hint: 'log_2(8) = 3 > 2, Περίπτωση 1' },
        { id: 'r4', expr: 'T(n) = T(n/2) + n log n', expected: 'm_nlogn_3', hint: 'log_2(1)=0 < 1, Περίπτωση 3 (κανονικότητα δ <= 1/2)' },
        { id: 'r5', expr: 'T(n) = T(n/2) + n^2', expected: 'm_n2', hint: 'log_2(1)=0 < 2, Περίπτωση 3 (δ = 1/4)' }
      ];
      this.match_tokens = [
        { id: 'm_n3', label: 'Θ(n^3) [Περ. 1]' },
        { id: 'm_nlogn_2', label: 'Θ(n log n) [Περ. 2]' },
        { id: 'm_n2', label: 'Θ(n^2) [Περ. 3]' },
        { id: 'm_n177', label: 'Θ(n^{log_3 7}) ~ Θ(n^1.77) [Περ. 1]' },
        { id: 'm_nlogn_3', label: 'Θ(n log n) [Περ. 3]' }
      ];
      this.matched = {};
      this.selected_tok = null;
      this.drag_tok = null;
      this.feedback_msg = '';
      this.feedback_kind = 'neutral';
    }

    /**
     * Resets both Unit 07 sub-challenges back to their initial empty state.
     */
    resetAll() {
      this.eliminated = {};
      this.matched = {};
      this.selected_tok = null;
      this.drag_tok = null;
      this.feedback_msg = '';
      this.feedback_kind = 'neutral';
    }

    /**
     * Checks whether the clicked point is dominated in Recitation B Ch. 11 #5.
     *
     * Args:
     *     pt_id (string): Clicked point ID.
     *     container_el (HTMLElement): Host DOM element.
     *     on_complete_cb (Function): Completion callback.
     *     on_reset_cb (Function): Reset callback.
     */
    tryEliminatePoint(pt_id, container_el, on_complete_cb, on_reset_cb) {
      const pt = this.pareto_points.find((p) => p.id === pt_id);
      if (!pt) {
        return;
      }
      if (pt.dominated) {
        this.eliminated[pt_id] = true;
        this.feedback_kind = 'correct';
        this.feedback_msg = 'Σωστά! Το σημείο (' + pt.x + ', ' + pt.y + ') κυριαρχείται από το ' + pt.dom_by + ' και απορρίπτεται.';
        this.checkCompletion(on_complete_cb);
      } else {
        this.feedback_kind = 'wrong';
        this.feedback_msg = 'Προσοχή! Το (' + pt.x + ', ' + pt.y + ') ΔΕΝ κυριαρχείται από κανένα άλλο σημείο (ανήκει στο MaximaSet).';
      }
      this.mount(container_el, on_complete_cb, on_reset_cb);
    }

    /**
     * Validates placing an asymptotic class token onto a Recitation B recurrence.
     *
     * Args:
     *     rec_id (string): Recurrence row ID.
     *     tok_id (string): Dropped/selected solution token ID.
     *     container_el (HTMLElement): Host DOM element.
     *     on_complete_cb (Function): Completion callback.
     *     on_reset_cb (Function): Reset callback.
     */
    tryMatchRecurrence(rec_id, tok_id, container_el, on_complete_cb, on_reset_cb) {
      const rec = this.recurrences.find((r) => r.id === rec_id);
      if (!rec) {
        return;
      }
      if (rec.expected === tok_id) {
        this.matched[rec_id] = tok_id;
        this.selected_tok = null;
        this.feedback_kind = 'correct';
        this.feedback_msg = 'Σωστή αντιστοίχιση για την ' + rec.expr + '!';
        this.checkCompletion(on_complete_cb);
      } else {
        this.feedback_kind = 'wrong';
        this.feedback_msg = 'Λάθος για ' + rec.expr + ': ' + rec.hint;
      }
      this.mount(container_el, on_complete_cb, on_reset_cb);
    }

    /**
     * Invokes completion callback once both Unit 07 sub-challenges are solved.
     *
     * Args:
     *     on_complete_cb (Function): Completion callback.
     */
    checkCompletion(on_complete_cb) {
      const elim_done = Boolean(this.eliminated.pt3 && this.eliminated.pt6);
      const match_done = Object.keys(this.matched).length === this.recurrences.length;
      if (elim_done && match_done && typeof on_complete_cb === 'function') {
        on_complete_cb('game_07');
      }
    }

    /**
     * Mounts the Unit 07 Pareto Eliminator and Master Theorem Matcher inside the host container.
     *
     * Args:
     *     container_el (HTMLElement): Host DOM element.
     *     on_complete_cb (Function): Completion callback.
     *     on_reset_cb (Function): Reset callback.
     */
    mount(container_el, on_complete_cb, on_reset_cb) {
      const elim_cnt = (this.eliminated.pt3 ? 1 : 0) + (this.eliminated.pt6 ? 1 : 0);
      const match_cnt = Object.keys(this.matched).length;
      const is_done = elim_cnt === 2 && match_cnt === 5;

      const toX = (x) => 40 + (x / 11) * 460;
      const toY = (y) => 205 - (y / 10) * 175;

      let svg = '<svg class="svg-stage" viewBox="0 0 540 230">' +
        '<line x1="40" y1="205" x2="515" y2="205" stroke="var(--border-strong)" stroke-width="1.5" />' +
        '<line x1="40" y1="18" x2="40" y2="205" stroke="var(--border-strong)" stroke-width="1.5" />';

      for (let i = 0; i < this.pareto_points.length; i += 1) {
        const p = this.pareto_points[i];
        const px = toX(p.x);
        const py = toY(p.y);
        const is_elim = Boolean(this.eliminated[p.id]);
        svg += '<g class="svg-node-interactive" data-pt-id="' + p.id + '" style="opacity:' + (is_elim ? '0.28' : '1') + ';">' +
          '<circle cx="' + px + '" cy="' + py + '" r="8" fill="' + (is_elim ? 'var(--bg-surface-deep)' : 'var(--accent-primary)') + '" stroke="var(--accent-primary)" stroke-width="2" />' +
          '<text x="' + (px + 10) + '" y="' + (py - 4) + '" fill="var(--ink-bright)" font-family="var(--font-mono)" font-size="11">(' + p.x + ',' + p.y + ')</text>' +
        '</g>';
      }
      svg += '</svg>';

      const tok_map = {};
      for (let i = 0; i < this.match_tokens.length; i += 1) {
        tok_map[this.match_tokens[i].id] = this.match_tokens[i];
      }
      const used_toks = Object.values(this.matched);

      let html = '<div class="card">';
      html += '<div class="puzzle-header">' +
        '<div><h3>Εργαστήριο Προκλήσεων Φροντιστηρίου B (Κεφ. 11 #2 &amp; #5)</h3>' +
        '<span class="meta-pill">Pareto (' + elim_cnt + '/2) &amp; Master Theorem (' + match_cnt + '/5)</span></div>' +
        (is_done ? '<span class="completion-badge">Ολοκληρώθηκαν Και τα Δύο</span>' : '') +
        '</div>';

      html += '<div class="grid-2">';
      html += '<div class="card-deep">' +
        '<h4>1. Εξάλειψη Κυριαρχούμενων Σημείων (#5)</h4>' +
        '<p class="muted-text">Κάντε κλικ στα <strong>2 κυριαρχούμενα</strong> σημεία για να τα αφαιρέσετε (κρατώντας τα 5 μη κυριαρχούμενα).</p>' +
        svg +
      '</div>';

      html += '<div class="card-deep">' +
        '<h4>2. Αντιστοίχιση Master Theorem (#2)</h4>' +
        '<p class="muted-text">Επιλέξτε/σύρετε τη σωστή πολυπλοκότητα σε κάθε αναδρομική εξίσωση:</p>' +
        '<div style="display:flex;flex-direction:column;gap:8px;margin-bottom:10px;">';
      for (let i = 0; i < this.recurrences.length; i += 1) {
        const rec = this.recurrences[i];
        const m_id = this.matched[rec.id];
        html += '<div style="display:flex;align-items:center;justify-content:space-between;gap:8px;flex-wrap:wrap;">' +
          '<code>' + escapeHtml(rec.expr) + '</code>' +
          '<button type="button" class="drop-slot ' + (m_id ? 'is-filled' : '') + '" data-rec-id="' + rec.id + '">' +
            (m_id ? escapeHtml(tok_map[m_id].label) : '? Πολυπλοκότητα') +
          '</button>' +
        '</div>';
      }
      html += '</div><div class="token-tray">';
      for (let i = 0; i < this.match_tokens.length; i += 1) {
        const tok = this.match_tokens[i];
        const is_used = used_toks.indexOf(tok.id) !== -1;
        const is_sel = this.selected_tok === tok.id && !is_used;
        html += '<button type="button" class="token-chip ' + (is_used ? 'is-used' : '') + (is_sel ? ' is-selected' : '') + '" ' +
          'draggable="' + (is_used ? 'false' : 'true') + '" data-mtok-id="' + tok.id + '"' + (is_used ? ' disabled' : '') + '>' +
          escapeHtml(tok.label) + '</button>';
      }
      html += '</div></div></div>';

      html += '<div class="lab-toolbar"><button type="button" class="btn btn-ghost" id="g07_reset_btn">Επαναφορά</button></div>';
      if (this.feedback_msg) {
        html += '<div class="quiz-feedback ' + (this.feedback_kind === 'correct' ? 'is-correct' : 'is-wrong') + '">' +
          '<div>' + escapeHtml(this.feedback_msg) + '</div></div>';
      }
      html += '</div>';

      container_el.innerHTML = html;

      const pts = container_el.querySelectorAll('[data-pt-id]');
      for (let i = 0; i < pts.length; i += 1) {
        pts[i].addEventListener('click', (evt) => {
          this.tryEliminatePoint(evt.currentTarget.getAttribute('data-pt-id'), container_el, on_complete_cb, on_reset_cb);
        });
      }

      const mtoks = container_el.querySelectorAll('[data-mtok-id]:not(:disabled)');
      for (let i = 0; i < mtoks.length; i += 1) {
        mtoks[i].addEventListener('click', (evt) => {
          const tid = evt.currentTarget.getAttribute('data-mtok-id');
          this.selected_tok = this.selected_tok === tid ? null : tid;
          this.mount(container_el, on_complete_cb, on_reset_cb);
        });
        mtoks[i].addEventListener('dragstart', (evt) => {
          this.drag_tok = evt.currentTarget.getAttribute('data-mtok-id');
          this.selected_tok = this.drag_tok;
        });
      }

      const rslots = container_el.querySelectorAll('[data-rec-id]:not(.is-filled)');
      for (let i = 0; i < rslots.length; i += 1) {
        rslots[i].addEventListener('dragover', (evt) => { evt.preventDefault(); evt.currentTarget.classList.add('is-over'); });
        rslots[i].addEventListener('dragleave', (evt) => { evt.currentTarget.classList.remove('is-over'); });
        rslots[i].addEventListener('drop', (evt) => {
          evt.preventDefault();
          evt.currentTarget.classList.remove('is-over');
          const rid = evt.currentTarget.getAttribute('data-rec-id');
          if (this.drag_tok) {
            this.tryMatchRecurrence(rid, this.drag_tok, container_el, on_complete_cb, on_reset_cb);
          }
        });
        rslots[i].addEventListener('click', (evt) => {
          const rid = evt.currentTarget.getAttribute('data-rec-id');
          if (this.selected_tok) {
            this.tryMatchRecurrence(rid, this.selected_tok, container_el, on_complete_cb, on_reset_cb);
          }
        });
      }

      container_el.querySelector('#g07_reset_btn').addEventListener('click', () => {
        this.resetAll();
        if (typeof on_reset_cb === 'function') {
          on_reset_cb('game_07');
        }
        this.mount(container_el, on_complete_cb, on_reset_cb);
      });
    }
  }

  global_scope.MidtermApp = global_scope.MidtermApp || {};
  global_scope.MidtermApp.builder_games = global_scope.MidtermApp.builder_games || {};
  global_scope.MidtermApp.builder_games['04'] = new Unit04BuilderGame();
  global_scope.MidtermApp.builder_games['05'] = new Unit05BuilderGame();
  global_scope.MidtermApp.builder_games['06'] = new Unit06BuilderGame();
  global_scope.MidtermApp.builder_games['07'] = new Unit07BuilderGame();
})(window);
