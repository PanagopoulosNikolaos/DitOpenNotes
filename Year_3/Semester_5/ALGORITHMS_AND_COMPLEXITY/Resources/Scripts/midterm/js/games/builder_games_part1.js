(function (global_scope) {
  'use strict';

  /**
   * Escapes special HTML characters in text values.
   *
   * Args:
   *     raw_text (string): Raw string to sanitize.
   *
   * Returns:
   *     string: Escaped safe HTML text.
   */
  function escapeHtml(raw_text) {
    return String(raw_text)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  /**
   * Renders the Growth Function Ranking Game for Unit 00 (Recitation A Ch. 1 #2).
   *
   * Allows reordering 10 asymptotic functions via drag-and-drop, click-swap, or arrow buttons.
   * Methods: mount(container_el, on_complete_cb), swapTiles(idx_a, idx_b), verifyOrder(container_el, on_complete_cb).
   */
  class Unit00BuilderGame {
    /**
     * Initializes expected canonical order and scrambled starting tiles.
     */
    constructor() {
      this.expected_order = [
        '1000', 'log log n', 'log n', 'n^(1/2)', 'n',
        'n log n', 'n^2', 'n^3', '2^n', 'n!'
      ];
      this.current_order = [
        'n log n', '1000', 'n^2', 'log n', 'n!',
        'n^(1/2)', 'log log n', '2^n', 'n', 'n^3'
      ];
      this.selected_idx = null;
      this.drag_idx = null;
      this.checked_results = null;
      this.is_completed = false;
    }

    /**
     * Resets the growth ranking puzzle back to its initial scrambled state.
     */
    resetAll() {
      this.current_order = [
        'n log n', '1000', 'n^2', 'log n', 'n!',
        'n^(1/2)', 'log log n', '2^n', 'n', 'n^3'
      ];
      this.selected_idx = null;
      this.drag_idx = null;
      this.checked_results = null;
      this.is_completed = false;
    }

    /**
     * Swaps two positions in the current growth-function ordering.
     *
     * Args:
     *     idx_a (number): First tile index.
     *     idx_b (number): Second tile index.
     */
    swapTiles(idx_a, idx_b) {
      if (idx_a === idx_b) {
        return;
      }
      const tmp = this.current_order[idx_a];
      this.current_order[idx_a] = this.current_order[idx_b];
      this.current_order[idx_b] = tmp;
      this.checked_results = null;
    }

    /**
     * Checks whether all 10 functions match the strict asymptotic growth order.
     *
     * Args:
     *     container_el (HTMLElement): Host DOM element.
     *     on_complete_cb (Function): Callback invoked with 'game_00' when solved.
     */
    verifyOrder(container_el, on_complete_cb, on_reset_cb) {
      let correct_count = 0;
      const flags = [];
      for (let i = 0; i < this.expected_order.length; i += 1) {
        const ok = this.current_order[i] === this.expected_order[i];
        flags.push(ok);
        if (ok) {
          correct_count += 1;
        }
      }
      this.checked_results = flags;
      if (correct_count === this.expected_order.length) {
        this.is_completed = true;
        if (typeof on_complete_cb === 'function') {
          on_complete_cb('game_00');
        }
      } else {
        this.is_completed = false;
        if (typeof on_reset_cb === 'function') {
          on_reset_cb('game_00');
        }
      }
      this.mount(container_el, on_complete_cb, on_reset_cb);
    }

    /**
     * Mounts the Growth Function Ranking Game inside the host container.
     *
     * Args:
     *     container_el (HTMLElement): Host DOM container.
     *     on_complete_cb (Function): Completion callback.
     *     on_reset_cb (Function): Reset callback.
     */
    mount(container_el, on_complete_cb, on_reset_cb) {
      let html = '<div class="card">';
      html += '<div class="puzzle-header">' +
        '<div><h3>Παιχνίδι Διάταξης Ρυθμού Αύξησης (10 Συναρτήσεις)</h3>' +
        '<span class="meta-pill">Φροντιστήριο A — Κεφ. 1 #2</span></div>' +
        (this.is_completed ? '<span class="completion-badge">Ολοκληρώθηκε (10/10)</span>' : '<span class="meta-pill accent">Βραδύτερη (1) &rarr; Ταχύτερη (10)</span>') +
        '</div>';

      html += '<p class="muted-text">Κατατάξτε τις συναρτήσεις από τη βραδύτερη (θέση 1) προς την ταχύτερη (θέση 10). Σύρετε μία κάρτα πάνω σε άλλη, επιλέξτε δύο κάρτες για ανταλλαγή ή χρησιμοποιήστε τα κουμπιά Πάνω/Κάτω.</p>';

      html += '<div class="rank-list">';
      for (let i = 0; i < this.current_order.length; i += 1) {
        const fn_label = this.current_order[i];
        let state_cls = '';
        if (this.checked_results) {
          state_cls = this.checked_results[i] ? ' is-correct' : ' is-wrong';
        } else if (this.selected_idx === i) {
          state_cls = ' is-selected';
        }
        html += '<div class="rank-tile' + state_cls + '" draggable="true" data-ridx="' + i + '">' +
          '<div style="display:flex;align-items:center;gap:12px;">' +
            '<span class="meta-pill">#' + (i + 1) + '</span>' +
            '<code>' + escapeHtml(fn_label) + '</code>' +
          '</div>' +
          '<div style="display:flex;gap:6px;">' +
            '<button type="button" class="btn btn-ghost" data-move="up" data-idx="' + i + '"' + (i === 0 ? ' disabled' : '') + '>Πάνω</button>' +
            '<button type="button" class="btn btn-ghost" data-move="down" data-idx="' + i + '"' + (i === this.current_order.length - 1 ? ' disabled' : '') + '>Κάτω</button>' +
          '</div>' +
        '</div>';
      }
      html += '</div>';

      html += '<div class="lab-toolbar">' +
        '<button type="button" class="btn btn-primary" id="g00_check_btn">Έλεγχος Διάταξης</button>' +
        '<button type="button" class="btn btn-ghost" id="g00_reset_btn">Ανακάτεμα</button>' +
        '</div>';

      if (this.checked_results) {
        const right = this.checked_results.filter(Boolean).length;
        html += '<div class="quiz-feedback ' + (this.is_completed ? 'is-correct' : 'is-wrong') + '">' +
          '<div>' + (this.is_completed
            ? 'Τέλεια! 1000 &lt;&lt; log log n &lt;&lt; log n &lt;&lt; n^(1/2) &lt;&lt; n &lt;&lt; n log n &lt;&lt; n^2 &lt;&lt; n^3 &lt;&lt; 2^n &lt;&lt; n!.'
            : 'Σωστές θέσεις: ' + right + ' / 10. Διορθώστε τις θέσεις με διακεκομμένο περίγραμμα.') +
          '</div></div>';
      }
      html += '</div>';

      container_el.innerHTML = html;

      const tiles = container_el.querySelectorAll('.rank-tile');
      for (let i = 0; i < tiles.length; i += 1) {
        tiles[i].addEventListener('dragstart', (evt) => {
          this.drag_idx = Number(evt.currentTarget.getAttribute('data-ridx'));
        });
        tiles[i].addEventListener('dragover', (evt) => {
          evt.preventDefault();
        });
        tiles[i].addEventListener('drop', (evt) => {
          evt.preventDefault();
          const drop_idx = Number(evt.currentTarget.getAttribute('data-ridx'));
          if (this.drag_idx !== null) {
            this.swapTiles(this.drag_idx, drop_idx);
            this.drag_idx = null;
            this.selected_idx = null;
            this.mount(container_el, on_complete_cb, on_reset_cb);
          }
        });
        tiles[i].addEventListener('click', (evt) => {
          if (evt.target.closest('[data-move]')) {
            return;
          }
          const idx = Number(evt.currentTarget.getAttribute('data-ridx'));
          if (this.selected_idx === null) {
            this.selected_idx = idx;
          } else {
            this.swapTiles(this.selected_idx, idx);
            this.selected_idx = null;
          }
          this.mount(container_el, on_complete_cb, on_reset_cb);
        });
      }

      const move_btns = container_el.querySelectorAll('[data-move]');
      for (let i = 0; i < move_btns.length; i += 1) {
        move_btns[i].addEventListener('click', (evt) => {
          const dir = evt.currentTarget.getAttribute('data-move');
          const idx = Number(evt.currentTarget.getAttribute('data-idx'));
          const target = dir === 'up' ? idx - 1 : idx + 1;
          this.swapTiles(idx, target);
          this.selected_idx = null;
          this.mount(container_el, on_complete_cb, on_reset_cb);
        });
      }

      container_el.querySelector('#g00_check_btn').addEventListener('click', () => {
        this.verifyOrder(container_el, on_complete_cb, on_reset_cb);
      });
      container_el.querySelector('#g00_reset_btn').addEventListener('click', () => {
        this.resetAll();
        if (typeof on_reset_cb === 'function') {
          on_reset_cb('game_00');
        }
        this.mount(container_el, on_complete_cb, on_reset_cb);
      });
    }
  }

  /**
   * Renders the O(n^2) Membership Classifier Game for Unit 01 (Recitation A Ch. 1 #3).
   *
   * Users drag or click 10 functions into two buckets: O(n^2) vs Not O(n^2).
   * Methods: mount(container_el, on_complete_cb), classifyItem(item_id, bucket_name, container_el, on_complete_cb).
   */
  class Unit01BuilderGame {
    /**
     * Initializes the 10 classification items and tracking state.
     */
    constructor() {
      this.items = [
        { id: 'f1', label: 'n', in_on2: true },
        { id: 'f2', label: 'n^(1/2)', in_on2: true },
        { id: 'f3', label: '2n^2', in_on2: true },
        { id: 'f4', label: 'n^2 + 1000n', in_on2: true },
        { id: 'f5', label: 'n^3', in_on2: false },
        { id: 'f6', label: 'n^2/100 + 1', in_on2: true },
        { id: 'f7', label: 'n^2 + n + n log n', in_on2: true },
        { id: 'f8', label: 'n^3 + n^2', in_on2: false },
        { id: 'f9', label: '2^n', in_on2: false },
        { id: 'f10', label: 'n + log n', in_on2: true }
      ];
      this.placed = {};
      this.selected_item_id = null;
      this.drag_item_id = null;
      this.feedback_msg = '';
      this.feedback_kind = 'neutral';
    }

    /**
     * Resets the O(n^2) classification game to its initial empty state.
     */
    resetAll() {
      this.placed = {};
      this.selected_item_id = null;
      this.drag_item_id = null;
      this.feedback_msg = '';
      this.feedback_kind = 'neutral';
    }

    /**
     * Validates placing an item into either the O(n^2) bucket or Not-O(n^2) bucket.
     *
     * Args:
     *     item_id (string): Identifier of the function chip.
     *     bucket_name (string): 'yes' for O(n^2) or 'no' for Not O(n^2).
     *     container_el (HTMLElement): Host DOM element.
     *     on_complete_cb (Function): Completion callback.
     *     on_reset_cb (Function): Reset callback.
     */
    classifyItem(item_id, bucket_name, container_el, on_complete_cb, on_reset_cb) {
      const item = this.items.find((it) => it.id === item_id);
      if (!item) {
        return;
      }
      const wants_yes = bucket_name === 'yes';
      if (item.in_on2 === wants_yes) {
        this.placed[item_id] = bucket_name;
        this.selected_item_id = null;
        this.feedback_kind = 'correct';
        const done_count = Object.keys(this.placed).length;
        if (done_count === this.items.length) {
          this.feedback_msg = 'Συγχαρητήρια! Ταξινομήσατε σωστά και τις 10 συναρτήσεις ως προς το O(n^2).';
          if (typeof on_complete_cb === 'function') {
            on_complete_cb('game_01');
          }
        } else {
          this.feedback_msg = 'Σωστά! Η ' + item.label + (item.in_on2 ? ' φράσσεται από c * n^2.' : ' αυξάνει αυστηρά ταχύτερα από n^2.');
        }
      } else {
        this.feedback_kind = 'wrong';
        this.feedback_msg = 'Λάθος κατηγορία για τη ' + item.label + ': ' +
          (item.in_on2 ? 'Ο κυρίαρχος όρος είναι <= n^2, άρα ΑΝΗΚΕΙ στο O(n^2).' : 'Υπερβαίνει κάθε σταθερό πολλαπλάσιο του n^2, άρα ΔΕΝ ανήκει.');
      }
      this.mount(container_el, on_complete_cb, on_reset_cb);
    }

    /**
     * Mounts the O(n^2) classification game inside the host container.
     *
     * Args:
     *     container_el (HTMLElement): Host DOM element.
     *     on_complete_cb (Function): Completion callback.
     *     on_reset_cb (Function): Reset callback.
     */
    mount(container_el, on_complete_cb, on_reset_cb) {
      const placed_count = Object.keys(this.placed).length;
      const is_done = placed_count === this.items.length;

      let html = '<div class="card">';
      html += '<div class="puzzle-header">' +
        '<div><h3>Ταξινομητής Ασυμπτωτικού Άνω Ορίου: Ποιες είναι O(n^2);</h3>' +
        '<span class="meta-pill">Φροντιστήριο A — Κεφ. 1 #3</span></div>' +
        (is_done ? '<span class="completion-badge">Ολοκληρώθηκε (10/10)</span>' : '<span class="meta-pill accent">' + placed_count + ' / 10 ταξινομημένες</span>') +
        '</div>';
      html += '<p class="muted-text">Σύρετε κάθε συνάρτηση στο σωστό καλάθι (ή επιλέξτε συνάρτηση και κάντε κλικ στο καλάθι).</p>';

      html += '<div class="token-tray">';
      for (let i = 0; i < this.items.length; i += 1) {
        const it = this.items[i];
        const is_used = Boolean(this.placed[it.id]);
        const is_sel = this.selected_item_id === it.id && !is_used;
        html += '<button type="button" class="token-chip ' + (is_used ? 'is-used' : '') + (is_sel ? ' is-selected' : '') + '" ' +
          'draggable="' + (is_used ? 'false' : 'true') + '" data-item-id="' + it.id + '"' + (is_used ? ' disabled' : '') + '>' +
          escapeHtml(it.label) + '</button>';
      }
      html += '</div>';

      const yes_items = this.items.filter((it) => this.placed[it.id] === 'yes');
      const no_items = this.items.filter((it) => this.placed[it.id] === 'no');

      html += '<div class="grid-2">' +
        '<div class="dropzone-bucket" data-bucket="yes">' +
          '<strong>Ανήκει στο O(n^2) (f(n) <= c * n^2)</strong>' +
          '<div class="array-strip">' + yes_items.map((it) => '<span class="meta-pill accent">' + escapeHtml(it.label) + '</span>').join('') + '</div>' +
        '</div>' +
        '<div class="dropzone-bucket" data-bucket="no">' +
          '<strong>ΔΕΝ ανήκει στο O(n^2)</strong>' +
          '<div class="array-strip">' + no_items.map((it) => '<span class="meta-pill">' + escapeHtml(it.label) + '</span>').join('') + '</div>' +
        '</div>' +
      '</div>';

      html += '<div class="lab-toolbar"><button type="button" class="btn btn-ghost" id="g01_reset_btn">Επαναφορά</button></div>';

      if (this.feedback_msg) {
        html += '<div class="quiz-feedback ' + (this.feedback_kind === 'correct' ? 'is-correct' : 'is-wrong') + '">' +
          '<div>' + escapeHtml(this.feedback_msg) + '</div></div>';
      }
      html += '</div>';

      container_el.innerHTML = html;

      const chips = container_el.querySelectorAll('[data-item-id]:not(:disabled)');
      for (let i = 0; i < chips.length; i += 1) {
        chips[i].addEventListener('click', (evt) => {
          const id = evt.currentTarget.getAttribute('data-item-id');
          this.selected_item_id = this.selected_item_id === id ? null : id;
          this.mount(container_el, on_complete_cb, on_reset_cb);
        });
        chips[i].addEventListener('dragstart', (evt) => {
          this.drag_item_id = evt.currentTarget.getAttribute('data-item-id');
          this.selected_item_id = this.drag_item_id;
        });
      }

      const buckets = container_el.querySelectorAll('[data-bucket]');
      for (let i = 0; i < buckets.length; i += 1) {
        buckets[i].addEventListener('dragover', (evt) => {
          evt.preventDefault();
          evt.currentTarget.classList.add('is-over');
        });
        buckets[i].addEventListener('dragleave', (evt) => {
          evt.currentTarget.classList.remove('is-over');
        });
        buckets[i].addEventListener('drop', (evt) => {
          evt.preventDefault();
          evt.currentTarget.classList.remove('is-over');
          const b = evt.currentTarget.getAttribute('data-bucket');
          if (this.drag_item_id) {
            this.classifyItem(this.drag_item_id, b, container_el, on_complete_cb, on_reset_cb);
          }
        });
        buckets[i].addEventListener('click', (evt) => {
          const b = evt.currentTarget.getAttribute('data-bucket');
          if (this.selected_item_id) {
            this.classifyItem(this.selected_item_id, b, container_el, on_complete_cb, on_reset_cb);
          }
        });
      }

      container_el.querySelector('#g01_reset_btn').addEventListener('click', () => {
        this.resetAll();
        if (typeof on_reset_cb === 'function') {
          on_reset_cb('game_01');
        }
        this.mount(container_el, on_complete_cb, on_reset_cb);
      });
    }
  }

  /**
   * Renders the Manual Interactive Binary Heap Tree Builder for Unit 02.
   *
   * Users directly click/drag tree nodes to swap values until zero heap-order violations remain.
   * Methods: mount(container_el, on_complete_cb), loadPreset(mode_key), findViolations(), handleNodeSwap(idx_a, idx_b, container_el, on_complete_cb), renderInteractiveTreeSvg(violations).
   */
  class Unit02BuilderGame {
    /**
     * Initializes the manual heap tree puzzle modes.
     */
    constructor() {
      this.mode = 'min_repair';
      this.selected_node = null;
      this.feedback_msg = '';
      this.feedback_kind = 'neutral';
      this.loadPreset('min_repair');
    }

    /**
     * Loads a scrambled or downheap puzzle array into the 1-indexed tree.
     *
     * Args:
     *     mode_key (string): 'min_repair', 'max_recitation', or 'manual_downheap'.
     */
    loadPreset(mode_key) {
      this.mode = mode_key;
      this.selected_node = null;
      this.feedback_msg = '';
      if (mode_key === 'min_repair') {
        this.heap = [null, 18, 6, 14, 3, 11, 25, 9];
      } else if (mode_key === 'max_recitation') {
        // Keys from Recitation A Ch. 5 #4 scrambled for manual Max-Heap arrangement.
        this.heap = [null, 5, 12, 7, 9, 16, 11];
      } else {
        // Root 20 violates min-heap order and requires swapping down via smaller child (6, then 9).
        this.heap = [null, 20, 11, 6, 18, 14, 25, 9];
      }
    }

    /**
     * Identifies parent-child edges violating Min-Heap or Max-Heap order.
     *
     * Returns:
     *     Array<Array<number>>: Pairs [parent_idx, child_idx] that violate heap property.
     */
    findViolations() {
      const is_max = this.mode === 'max_recitation';
      const n = this.heap.length - 1;
      const bad_edges = [];
      for (let i = 2; i <= n; i += 1) {
        const p = Math.floor(i / 2);
        const violates = is_max ? this.heap[p] < this.heap[i] : this.heap[p] > this.heap[i];
        if (violates) {
          bad_edges.push([p, i]);
        }
      }
      return bad_edges;
    }

    /**
     * Resets the heap tree puzzle back to the default preset.
     */
    resetAll() {
      this.loadPreset('min_repair');
    }

    /**
     * Swaps two nodes in the tree and checks downheap trap rules and completion.
     *
     * Args:
     *     idx_a (number): First 1-indexed node position.
     *     idx_b (number): Second 1-indexed node position.
     *     container_el (HTMLElement): Host DOM element.
     *     on_complete_cb (Function): Completion callback.
     *     on_reset_cb (Function): Reset callback.
     */
    handleNodeSwap(idx_a, idx_b, container_el, on_complete_cb, on_reset_cb) {
      if (idx_a === idx_b) {
        this.selected_node = null;
        this.mount(container_el, on_complete_cb, on_reset_cb);
        return;
      }

      // Enforces the smaller-child downheap rule specifically during manual_downheap mode.
      if (this.mode === 'manual_downheap') {
        const parent = Math.min(idx_a, idx_b);
        const child = Math.max(idx_a, idx_b);
        if (Math.floor(child / 2) !== parent) {
          this.feedback_kind = 'wrong';
          this.feedback_msg = 'Στο downheap ανταλλάσσουμε μόνο γονέα με άμεσο παιδί του!';
          this.selected_node = null;
          this.mount(container_el, on_complete_cb, on_reset_cb);
          return;
        }
        const left = 2 * parent;
        const right = 2 * parent + 1;
        const n = this.heap.length - 1;
        const smaller = (right <= n && this.heap[right] < this.heap[left]) ? right : left;
        if (child !== smaller) {
          this.feedback_kind = 'wrong';
          this.feedback_msg = 'Παγίδα! Στο downheap επιλέγουμε ΠΑΝΤΑ το μικρότερο παιδί (' + this.heap[smaller] + '), όχι το ' + this.heap[child] + '!';
          this.selected_node = null;
          this.mount(container_el, on_complete_cb, on_reset_cb);
          return;
        }
      }

      const tmp = this.heap[idx_a];
      this.heap[idx_a] = this.heap[idx_b];
      this.heap[idx_b] = tmp;
      this.selected_node = null;

      const remaining = this.findViolations();
      if (remaining.length === 0) {
        this.feedback_kind = 'correct';
        this.feedback_msg = 'Συγχαρητήρια! Ο σωρός ικανοποιεί πλήρως τη σωρειακή διάταξη χωρίς καμία παραβίαση.';
        if (typeof on_complete_cb === 'function') {
          on_complete_cb('game_02');
        }
      } else {
        this.feedback_kind = 'correct';
        this.feedback_msg = 'Έγινε ανταλλαγή A[' + idx_a + '] <-> A[' + idx_b + ']. Παραμένουν ' + remaining.length + ' παραβιάσεις.';
      }
      this.mount(container_el, on_complete_cb, on_reset_cb);
    }

    /**
     * Renders the interactive SVG tree with clickable nodes and dashed violating edges.
     *
     * Args:
     *     violations (Array<Array<number>>): List of violating [parent, child] edge pairs.
     *
     * Returns:
     *     string: Interactive SVG markup.
     */
    renderInteractiveTreeSvg(violations) {
      const n = this.heap.length - 1;
      const width = 640;
      const depth = Math.floor(Math.log2(n));
      const height = (depth + 1) * 68 + 32;

      const bad_lookup = {};
      for (let i = 0; i < violations.length; i += 1) {
        bad_lookup[violations[i][0] + '-' + violations[i][1]] = true;
      }

      const coords = [null];
      for (let i = 1; i <= n; i += 1) {
        const lvl = Math.floor(Math.log2(i));
        const pos = i - Math.pow(2, lvl);
        const cnt = Math.pow(2, lvl);
        coords.push({ x: ((pos + 0.5) / cnt) * width, y: 36 + lvl * 66 });
      }

      let edges_svg = '';
      for (let i = 2; i <= n; i += 1) {
        const p = Math.floor(i / 2);
        const is_bad = Boolean(bad_lookup[p + '-' + i]);
        edges_svg += '<line x1="' + coords[p].x + '" y1="' + coords[p].y + '" x2="' + coords[i].x + '" y2="' + coords[i].y + '" ' +
          'class="' + (is_bad ? 'svg-edge-violation' : '') + '" stroke="var(--border-strong)" stroke-width="2" />';
      }

      let nodes_svg = '';
      for (let i = 1; i <= n; i += 1) {
        const is_sel = this.selected_node === i;
        nodes_svg += '<g class="svg-node-interactive ' + (is_sel ? 'svg-node-selected' : '') + '" data-heap-node="' + i + '">' +
          '<circle cx="' + coords[i].x + '" cy="' + coords[i].y + '" r="21" fill="' + (is_sel ? 'var(--accent-primary)' : 'var(--bg-surface-elevated)') + '" stroke="' + (is_sel ? 'var(--accent-primary)' : 'var(--ink-muted)') + '" stroke-width="2" />' +
          '<text x="' + coords[i].x + '" y="' + (coords[i].y + 5) + '" text-anchor="middle" fill="' + (is_sel ? 'var(--ink-on-accent)' : 'var(--ink-bright)') + '" font-family="var(--font-mono)" font-size="14" font-weight="700">' + this.heap[i] + '</text>' +
          '<text x="' + coords[i].x + '" y="' + (coords[i].y - 24) + '" text-anchor="middle" fill="var(--ink-subtle)" font-family="var(--font-mono)" font-size="10">[' + i + ']</text>' +
          '</g>';
      }

      return '<svg class="svg-stage" viewBox="0 0 ' + width + ' ' + height + '">' + edges_svg + nodes_svg + '</svg>';
    }

    /**
     * Mounts the manual heap tree builder inside the host container.
     *
     * Args:
     *     container_el (HTMLElement): Host DOM element.
     *     on_complete_cb (Function): Completion callback.
     *     on_reset_cb (Function): Reset callback.
     */
    mount(container_el, on_complete_cb, on_reset_cb) {
      const violations = this.findViolations();
      const is_done = violations.length === 0;
      const is_max = this.mode === 'max_recitation';

      let html = '<div class="card">';
      html += '<div class="puzzle-header">' +
        '<div><h3>Χειροκίνητος Κατασκευαστής Δέντρου Σωρού (Node Swapper)</h3>' +
        '<span class="meta-pill">' + (is_max ? 'Φροντιστήριο A — Κεφ. 5 #4 (Max-Heap)' : 'Σημείωση 02 (Min-Heap)') + '</span></div>' +
        (is_done ? '<span class="completion-badge">Έγκυρος Σωρός</span>' : '<span class="meta-pill accent">' + violations.length + ' παραβιάσεις ακμών</span>') +
        '</div>';

      html += '<div class="lab-toolbar">' +
        '<button type="button" class="btn ' + (this.mode === 'min_repair' ? 'btn-primary' : 'btn-secondary') + '" data-hmode="min_repair">Επισκευή Min-Heap</button>' +
        '<button type="button" class="btn ' + (this.mode === 'max_recitation' ? 'btn-primary' : 'btn-secondary') + '" data-hmode="max_recitation">Max-Heap [5,12,7,9,16,11]</button>' +
        '<button type="button" class="btn ' + (this.mode === 'manual_downheap' ? 'btn-primary' : 'btn-secondary') + '" data-hmode="manual_downheap">Χειροκίνητο downheap</button>' +
        '<button type="button" class="btn btn-ghost" id="g02_reset_btn">Επαναφορά</button>' +
        '</div>';

      html += '<p class="muted-text">Κάντε κλικ σε έναν κόμβο του δέντρου (ή κελί του πίνακα) και έπειτα κλικ σε δεύτερο κόμβο για να τους ανταλλάξετε. Οι διακεκομμένες ακμές δείχνουν παραβίαση διάταξης (' + (is_max ? 'γονέας >= παιδιά' : 'γονέας <= παιδιά') + ').</p>';

      html += this.renderInteractiveTreeSvg(violations);

      html += '<div class="array-strip">';
      for (let i = 1; i < this.heap.length; i += 1) {
        const is_sel = this.selected_node === i;
        html += '<button type="button" class="array-cell ' + (is_sel ? 'is-active' : '') + '" data-heap-node="' + i + '" style="cursor:pointer;">' +
          '<span class="array-cell-idx">A[' + i + ']</span>' +
          '<span class="array-cell-val">' + this.heap[i] + '</span>' +
          '</button>';
      }
      html += '</div>';

      if (this.feedback_msg) {
        html += '<div class="quiz-feedback ' + (this.feedback_kind === 'correct' ? 'is-correct' : 'is-wrong') + '">' +
          '<div>' + escapeHtml(this.feedback_msg) + '</div></div>';
      }
      html += '</div>';

      container_el.innerHTML = html;

      const mode_btns = container_el.querySelectorAll('[data-hmode]');
      for (let i = 0; i < mode_btns.length; i += 1) {
        mode_btns[i].addEventListener('click', (evt) => {
          this.loadPreset(evt.currentTarget.getAttribute('data-hmode'));
          if (typeof on_reset_cb === 'function') {
            on_reset_cb('game_02');
          }
          this.mount(container_el, on_complete_cb, on_reset_cb);
        });
      }

      container_el.querySelector('#g02_reset_btn').addEventListener('click', () => {
        this.loadPreset(this.mode);
        if (typeof on_reset_cb === 'function') {
          on_reset_cb('game_02');
        }
        this.mount(container_el, on_complete_cb, on_reset_cb);
      });

      const node_els = container_el.querySelectorAll('[data-heap-node]');
      for (let i = 0; i < node_els.length; i += 1) {
        node_els[i].addEventListener('click', (evt) => {
          const idx = Number(evt.currentTarget.getAttribute('data-heap-node'));
          if (this.selected_node === null) {
            this.selected_node = idx;
            this.mount(container_el, on_complete_cb, on_reset_cb);
          } else {
            this.handleNodeSwap(this.selected_node, idx, container_el, on_complete_cb, on_reset_cb);
          }
        });
      }
    }
  }

  /**
   * Renders the Manual Hash Table Slot Placer Game for Unit 03.
   *
   * Users drag or click each incoming key into its exact collision-resolved bucket [0..10].
   * Methods: mount(container_el, on_complete_cb), resetGame(new_mode), expectedIndex(key), tryPlaceKey(bucket_idx, container_el, on_complete_cb).
   */
  class Unit03BuilderGame {
    /**
     * Initializes the hash placement challenge with keys from Exercise 1.
     */
    constructor() {
      this.mode = 'linear';
      this.keys = [3, 14, 25, 36, 47];
      this.resetGame('linear');
    }

    /**
     * Resets the hash table placer game back to default linear mode.
     */
    resetAll() {
      this.resetGame('linear');
    }

    /**
     * Resets the hash bucket array and queue pointer for the chosen collision strategy.
     *
     * Args:
     *     new_mode (string): 'linear' or 'double'.
     */
    resetGame(new_mode) {
      this.mode = new_mode;
      this.table = new Array(11).fill(null);
      this.step = 0;
      this.feedback_msg = '';
      this.feedback_kind = 'neutral';
    }

    /**
     * Computes the exact target bucket index for the given key.
     *
     * Args:
     *     key (number): Integer key being inserted.
     *
     * Returns:
     *     number: Expected empty slot index in [0, 10].
     */
    expectedIndex(key) {
      const h = key % 11;
      const d = 7 - (key % 7);
      for (let j = 0; j < 11; j += 1) {
        const idx = this.mode === 'linear' ? (h + j) % 11 : (h + j * d) % 11;
        if (this.table[idx] === null) {
          return idx;
        }
      }
      return -1;
    }

    /**
     * Checks whether the student placed the active key into the correct bucket.
     *
     * Args:
     *     bucket_idx (number): Clicked/dropped bucket index.
     *     container_el (HTMLElement): Host DOM element.
     *     on_complete_cb (Function): Completion callback.
     *     on_reset_cb (Function): Reset callback.
     */
    tryPlaceKey(bucket_idx, container_el, on_complete_cb, on_reset_cb) {
      if (this.step >= this.keys.length) {
        return;
      }
      const key = this.keys[this.step];
      const expected = this.expectedIndex(key);
      if (bucket_idx === expected) {
        this.table[bucket_idx] = key;
        this.step += 1;
        this.feedback_kind = 'correct';
        if (this.step === this.keys.length) {
          this.feedback_msg = 'Άριστα! Τοποθετήσατε όλα τα κλειδιά στη σωστή θέση (' + (this.mode === 'linear' ? 'πρωτογενής συστάδα 3..7' : 'διασπορά διπλού κατακερματισμού') + ').';
          if (typeof on_complete_cb === 'function') {
            on_complete_cb('game_03');
          }
        } else {
          this.feedback_msg = 'Σωστά! Το ' + key + ' τοποθετήθηκε στη θέση ' + bucket_idx + '.';
        }
      } else {
        const h = key % 11;
        const d = 7 - (key % 7);
        this.feedback_kind = 'wrong';
        this.feedback_msg = 'Λάθος θέση (' + bucket_idx + ') για το ' + key + ': h(' + key + ') = ' + h +
          (this.mode === 'double' ? ', βήμα d(' + key + ') = 7 - (' + key + ' mod 7) = ' + d : ', βήμα +1') + '.';
      }
      this.mount(container_el, on_complete_cb, on_reset_cb);
    }

    /**
     * Mounts the manual hash table placer game inside the host container.
     *
     * Args:
     *     container_el (HTMLElement): Host DOM element.
     *     on_complete_cb (Function): Completion callback.
     *     on_reset_cb (Function): Reset callback.
     */
    mount(container_el, on_complete_cb, on_reset_cb) {
      const is_done = this.step >= this.keys.length;
      const current_key = is_done ? null : this.keys[this.step];

      let html = '<div class="card">';
      html += '<div class="puzzle-header">' +
        '<div><h3>Χειροκίνητη Τοποθέτηση σε Πίνακα Κατακερματισμού (N = 11)</h3>' +
        '<span class="meta-pill">Άσκηση 1 — h(k) = k mod 11</span></div>' +
        (is_done ? '<span class="completion-badge">Ολοκληρώθηκε (5/5)</span>' : '<span class="meta-pill accent">Κλειδί ' + (this.step + 1) + ' / ' + this.keys.length + '</span>') +
        '</div>';

      html += '<div class="lab-toolbar">' +
        '<button type="button" class="btn ' + (this.mode === 'linear' ? 'btn-primary' : 'btn-secondary') + '" data-hpm="linear">Γραμμική Ανίχνευση</button>' +
        '<button type="button" class="btn ' + (this.mode === 'double' ? 'btn-primary' : 'btn-secondary') + '" data-hpm="double">Διπλός Κατακερματισμός (q=7)</button>' +
        '<button type="button" class="btn btn-ghost" id="g03_reset_btn">Επαναφορά</button>' +
        '</div>';

      html += '<p class="muted-text">' +
        (this.mode === 'double' ? 'Υπολογίστε <code>d(k) = 7 - (k mod 7)</code> και σύρετε (ή κάντε κλικ) στο σωστό κελί [0..10].' : 'Δοκιμάστε διαδοχικές θέσεις <code>(h(k) + j) mod 11</code> και κάντε κλικ στο 1ο ελεύθερο κελί.') +
        '</p>';

      if (!is_done) {
        html += '<div class="token-tray">' +
          '<span class="muted-text" style="align-self:center;">Επόμενο κλειδί προς εισαγωγή:</span>' +
          '<span class="token-chip is-selected" draggable="true" id="g03_active_chip">' + current_key + '</span>' +
          '</div>';
      }

      html += '<div class="array-strip">';
      for (let i = 0; i < 11; i += 1) {
        const val = this.table[i];
        html += '<button type="button" class="array-cell ' + (val !== null ? 'is-active' : '') + '" data-bidx="' + i + '" style="cursor:pointer;">' +
          '<span class="array-cell-idx">' + i + '</span>' +
          '<span class="array-cell-val">' + (val === null ? '?' : val) + '</span>' +
          '</button>';
      }
      html += '</div>';

      if (this.feedback_msg) {
        html += '<div class="quiz-feedback ' + (this.feedback_kind === 'correct' ? 'is-correct' : 'is-wrong') + '">' +
          '<div>' + escapeHtml(this.feedback_msg) + '</div></div>';
      }
      html += '</div>';

      container_el.innerHTML = html;

      const mode_btns = container_el.querySelectorAll('[data-hpm]');
      for (let i = 0; i < mode_btns.length; i += 1) {
        mode_btns[i].addEventListener('click', (evt) => {
          this.resetGame(evt.currentTarget.getAttribute('data-hpm'));
          if (typeof on_reset_cb === 'function') {
            on_reset_cb('game_03');
          }
          this.mount(container_el, on_complete_cb, on_reset_cb);
        });
      }
      container_el.querySelector('#g03_reset_btn').addEventListener('click', () => {
        this.resetGame(this.mode);
        if (typeof on_reset_cb === 'function') {
          on_reset_cb('game_03');
        }
        this.mount(container_el, on_complete_cb, on_reset_cb);
      });

      const cells = container_el.querySelectorAll('[data-bidx]');
      for (let i = 0; i < cells.length; i += 1) {
        cells[i].addEventListener('dragover', (evt) => { evt.preventDefault(); });
        cells[i].addEventListener('drop', (evt) => {
          evt.preventDefault();
          const b_idx = Number(evt.currentTarget.getAttribute('data-bidx'));
          this.tryPlaceKey(b_idx, container_el, on_complete_cb, on_reset_cb);
        });
        cells[i].addEventListener('click', (evt) => {
          const b_idx = Number(evt.currentTarget.getAttribute('data-bidx'));
          this.tryPlaceKey(b_idx, container_el, on_complete_cb, on_reset_cb);
        });
      }
    }
  }

  global_scope.MidtermApp = global_scope.MidtermApp || {};
  global_scope.MidtermApp.builder_games = global_scope.MidtermApp.builder_games || {};
  global_scope.MidtermApp.builder_games['00'] = new Unit00BuilderGame();
  global_scope.MidtermApp.builder_games['01'] = new Unit01BuilderGame();
  global_scope.MidtermApp.builder_games['02'] = new Unit02BuilderGame();
  global_scope.MidtermApp.builder_games['03'] = new Unit03BuilderGame();
})(window);
