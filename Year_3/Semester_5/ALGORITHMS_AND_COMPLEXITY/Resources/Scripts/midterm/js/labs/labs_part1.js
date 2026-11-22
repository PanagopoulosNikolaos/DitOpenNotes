(function (global_scope) {
  'use strict';

  /**
   * Escapes special HTML characters in user-supplied or dynamic text.
   *
   * Args:
   *     raw_text (string): Raw text string to sanitize.
   *
   * Returns:
   *     string: HTML-safe string.
   */
  function escapeHtml(raw_text) {
    return String(raw_text)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  /**
   * Renders the Strategy Chooser and Seven Functions Growth Explorer for Unit 00.
   *
   * Manages interactive problem classification and growth-rate scaling tables.
   * Methods: mount(container_el), renderStrategyChooser(panel_el), renderGrowthExplorer(panel_el), formatGrowthValue(val).
   */
  class Unit00Lab {
    /**
     * Initializes default slider state and strategy decision catalog.
     */
    constructor() {
      this.current_n = 16;
      this.selected_category = 'sets';
      this.selected_sub = 'cuckoo';
      this.strategy_catalog = {
        sets: {
          label: 'Δυναμικά Σύνολα / Εγγραφές',
          options: {
            heap: {
              label: 'Συνεχής εξαγωγή ελαχίστου (Order Book, Huffman)',
              tech: 'Δυαδικός Σωρός (1-indexed min-heap)',
              complexity: 'insert/removeMin: O(log n) χειρότερη, min: O(1), Bottom-Up: O(n)',
              unit: '02'
            },
            hash: {
              label: 'Γρήγορη αναζήτηση κατά κλειδί (μικρό φορτίο α <= 1/2)',
              tech: 'Πίνακας Κατακερματισμού (Chaining / Linear / Double)',
              complexity: 'O(1) αναμενόμενη, O(n) χειρότερη (χρήση DEFUNCT)',
              unit: '03'
            },
            cuckoo: {
              label: 'Αυστηρό O(1) χειρότερη στην αναζήτηση/διαγραφή (Routers)',
              tech: 'Κατακερματισμός Κούκου (T1, T2 με N >= 2n)',
              complexity: 'get/remove: O(1) χειρότερη, put: O(1) επιμερισμένη',
              unit: '03'
            },
            union_find: {
              label: 'Συνένωση ξένων συνόλων & ερωτήματα ισοδυναμίας',
              tech: 'Union-Find (Δέντρα + Ένωση κατά μέγεθος + Συμπίεση διαδρομής)',
              complexity: 'O((n + m) α(n)) χειρότερη / επιμερισμένη (α(n) <= 4)',
              unit: '04'
            }
          }
        },
        sorting: {
          label: 'Ταξινόμηση n Στοιχείων',
          options: {
            small: {
              label: 'Πολύ μικρό σύνολο (n < 1.000) ή σχεδόν ταξινομημένο',
              tech: 'Insertion-Sort (ή Selection-Sort)',
              complexity: 'O(n^2) χειρότερη, Ω(n) καλύτερη για Insertion-Sort, O(1) χώρος',
              unit: '02 / 05'
            },
            disk: {
              label: 'Τεράστιο σύνολο (> 1M) σε δίσκο / απαίτηση σταθερότητας',
              tech: 'Merge-Sort (σειριακή προσπέλαση)',
              complexity: 'O(n log n) χειρότερη, O(n) επιπλέον χώρος',
              unit: '05'
            },
            ram_fast: {
              label: 'Μεγάλο σύνολο στη RAM με μέγιστη πρακτική ταχύτητα',
              tech: 'Τυχαιοποιημένος inPlaceQuickSort (τριμερής διαμερισμός)',
              complexity: 'O(n log n) αναμενόμενη, O(n^2) χειρότερη, O(log n) στοίβα',
              unit: '05'
            },
            ram_strict: {
              label: 'Μεγάλο σύνολο με σκληρό O(n log n) χειρότερης & O(1) χώρο',
              tech: 'Heap-Sort (επί-τόπου με max-heap)',
              complexity: 'O(n log n) χειρότερη, O(1) επιπλέον χώρος',
              unit: '02 / 05'
            }
          }
        },
        optimization: {
          label: 'Βελτιστοποίηση (Greedy vs Divide & Conquer)',
          options: {
            fractional: {
              label: 'Διαιρετοί πόροι με μέγιστο όφελος',
              tech: 'Άπληστη Μέθοδος: Fractional Knapsack (κατά b_i / w_i)',
              complexity: 'O(n log n) χειρότερη (αποτυγχάνει στο 0-1 Knapsack)',
              unit: '06'
            },
            scheduling: {
              label: 'Ελάχιστος αριθμός μηχανών για διαστήματα [s_i, f_i]',
              tech: 'Άπληστη Μέθοδος: Task Scheduling (ταξινόμηση κατά s_i)',
              complexity: 'O(n log n) χειρότερη με min-heap (ΟΧΙ κατά f_i)',
              unit: '06'
            },
            dc_sub: {
              label: 'Ανεξάρτητα υποπροβλήματα n/b με αποδοτική σύνθεση',
              tech: 'Διαίρει και Βασίλευε (Karatsuba, MaximaSet, Master Theorem)',
              complexity: 'Karatsuba: Θ(n^1.585), MaximaSet: Θ(n log n)',
              unit: '07'
            }
          }
        }
      };
    }

    /**
     * Mounts the Unit 00 lab UI inside the target container.
     *
     * Args:
     *     container_el (HTMLElement): Host DOM element for the lab.
     */
    mount(container_el) {
      container_el.innerHTML =
        '<div class="grid-2">' +
          '<div class="card" id="u00_chooser_box"></div>' +
          '<div class="card" id="u00_growth_box"></div>' +
        '</div>';
      this.renderStrategyChooser(container_el.querySelector('#u00_chooser_box'));
      this.renderGrowthExplorer(container_el.querySelector('#u00_growth_box'));
    }

    /**
     * Renders the interactive Strategy Chooser wizard.
     *
     * Args:
     *     panel_el (HTMLElement): Target panel element for the wizard.
     */
    renderStrategyChooser(panel_el) {
      const cat_keys = Object.keys(this.strategy_catalog);
      const current_cat = this.strategy_catalog[this.selected_category];
      const sub_keys = Object.keys(current_cat.options);
      if (!current_cat.options[this.selected_sub]) {
        this.selected_sub = sub_keys[0];
      }
      const chosen = current_cat.options[this.selected_sub];

      let html = '<h3>Διαδραστικός Επιλογέας Στρατηγικής (Strategy Chooser)</h3>';
      html += '<p class="muted-text">Επιλέξτε τύπο προβλήματος και απαίτηση εκφώνησης για να δείτε τη βέλτιστη επιλογή Προόδου.</p>';
      html += '<div class="lab-toolbar">';
      for (let i = 0; i < cat_keys.length; i += 1) {
        const key = cat_keys[i];
        const active_cls = key === this.selected_category ? 'btn-primary' : 'btn-secondary';
        html += '<button type="button" class="btn ' + active_cls + '" data-cat="' + key + '">' + escapeHtml(this.strategy_catalog[key].label) + '</button>';
      }
      html += '</div>';

      html += '<div class="quiz-options">';
      for (let j = 0; j < sub_keys.length; j += 1) {
        const sk = sub_keys[j];
        const is_sel = sk === this.selected_sub;
        html += '<button type="button" class="quiz-option ' + (is_sel ? 'is-correct' : '') + '" data-sub="' + sk + '">' +
          '<span>' + escapeHtml(current_cat.options[sk].label) + '</span>' +
          '<span class="meta-pill">' + escapeHtml(current_cat.options[sk].unit) + '</span>' +
          '</button>';
      }
      html += '</div>';

      html += '<div class="accent-callout">' +
        '<div><strong>Επιλογή:</strong> ' + escapeHtml(chosen.tech) + '</div>' +
        '<div><strong>Πολυπλοκότητα:</strong> <code>' + escapeHtml(chosen.complexity) + '</code></div>' +
        '</div>';

      panel_el.innerHTML = html;

      const cat_btns = panel_el.querySelectorAll('[data-cat]');
      for (let i = 0; i < cat_btns.length; i += 1) {
        cat_btns[i].addEventListener('click', (evt) => {
          this.selected_category = evt.currentTarget.getAttribute('data-cat');
          this.renderStrategyChooser(panel_el);
        });
      }
      const sub_btns = panel_el.querySelectorAll('[data-sub]');
      for (let i = 0; i < sub_btns.length; i += 1) {
        sub_btns[i].addEventListener('click', (evt) => {
          this.selected_sub = evt.currentTarget.getAttribute('data-sub');
          this.renderStrategyChooser(panel_el);
        });
      }
    }

    /**
     * Formats large numerical values concisely for the growth table.
     *
     * Args:
     *     val (number): Numeric step count to format.
     *
     * Returns:
     *     string: Formatted integer or scientific notation string.
     */
    formatGrowthValue(val) {
      if (!isFinite(val)) {
        return '> 10^308';
      }
      if (val >= 1e6) {
        return val.toExponential(2);
      }
      return Math.round(val).toLocaleString('en-US');
    }

    /**
     * Renders the Seven Functions Growth Explorer with live n scaling.
     *
     * Args:
     *     panel_el (HTMLElement): Target panel element for the growth explorer.
     */
    renderGrowthExplorer(panel_el) {
      const n = this.current_n;
      const log_n = Math.log2(n);
      const rows = [
        { name: '1 (Σταθερή)', val: '1', dbl: 'x 1 (αμετάβλητη)' },
        { name: 'log n', val: log_n.toFixed(2), dbl: '+ 1 (προσθετικά)' },
        { name: 'n (Γραμμική)', val: this.formatGrowthValue(n), dbl: 'x 2' },
        { name: 'n log n', val: this.formatGrowthValue(n * log_n), dbl: '2n log n + 2n' },
        { name: 'n^2 (Τετραγωνική)', val: this.formatGrowthValue(n * n), dbl: 'x 4' },
        { name: 'n^3 (Κυβική)', val: this.formatGrowthValue(n * n * n), dbl: 'x 8' },
        { name: '2^n (Εκθετική)', val: n > 1000 ? '~ 10^' + Math.round(n * 0.30103) : this.formatGrowthValue(Math.pow(2, n)), dbl: 'Τετραγωνισμός (2^n)^2' }
      ];

      let html = '<h3>Εξερευνητής Επτά Συναρτήσεων Αύξησης</h3>';
      html += '<div class="lab-toolbar">' +
        '<label class="lab-field">n = <strong id="u00_n_val">' + n + '</strong> ' +
        '<input type="range" id="u00_n_slider" min="4" max="1024" step="4" value="' + n + '"></label>' +
        '<button type="button" class="btn btn-ghost" data-preset="8">8</button>' +
        '<button type="button" class="btn btn-ghost" data-preset="16">16</button>' +
        '<button type="button" class="btn btn-ghost" data-preset="64">64</button>' +
        '<button type="button" class="btn btn-ghost" data-preset="1024">1024</button>' +
        '</div>';

      html += '<div class="table-wrap"><table class="data-table"><thead><tr><th>Συνάρτηση</th><th>Τιμή f(n)</th><th>Διπλασιασμός (n &rarr; 2n)</th></tr></thead><tbody>';
      for (let i = 0; i < rows.length; i += 1) {
        html += '<tr><td><code>' + rows[i].name + '</code></td><td><code>' + rows[i].val + '</code></td><td>' + rows[i].dbl + '</td></tr>';
      }
      html += '</tbody></table></div>';
      panel_el.innerHTML = html;

      const slider = panel_el.querySelector('#u00_n_slider');
      slider.addEventListener('input', (evt) => {
        this.current_n = Number(evt.target.value);
        this.renderGrowthExplorer(panel_el);
      });
      const presets = panel_el.querySelectorAll('[data-preset]');
      for (let i = 0; i < presets.length; i += 1) {
        presets[i].addEventListener('click', (evt) => {
          this.current_n = Number(evt.currentTarget.getAttribute('data-preset'));
          this.renderGrowthExplorer(panel_el);
        });
      }
    }
  }

  /**
   * Renders the MaxsubFastest Stepper and Extendable Array Amortized Simulator for Unit 01.
   *
   * Manages step-by-step Kadane/MaxsubFastest tracing and cyber-dollar amortized accounting.
   * Methods: mount(container_el), renderMaxsubPanel(panel_el), renderAmortizedPanel(panel_el), addElements(count).
   */
  class Unit01Lab {
    /**
     * Initializes default array inputs and amortized array simulation state.
     */
    constructor() {
      this.arr = [3, -5, 4, -1, 6, -8, 5];
      this.step_t = 0;
      this.strategy = 'double';
      this.resetAmortized();
    }

    /**
     * Resets the extendable array simulator back to initial capacity 1.
     */
    resetAmortized() {
      this.ext_size = 0;
      this.ext_capacity = 1;
      this.total_ops = 0;
      this.total_copies = 0;
      this.bank_dollars = 0;
      this.ext_logs = ['Αρχικοποίηση: size = 0, capacity = 1, bank = 0 cyber-δολάρια.'];
    }

    /**
     * Simulates adding count elements to the extendable array under the active strategy.
     *
     * Args:
     *     count (number): Number of consecutive add operations to execute.
     */
    addElements(count) {
      for (let c = 0; c < count; c += 1) {
        let copied_now = 0;
        if (this.ext_size === this.ext_capacity) {
          copied_now = this.ext_size;
          this.total_copies += copied_now;
          this.total_ops += copied_now;
          this.ext_capacity = this.strategy === 'double' ? this.ext_capacity * 2 : this.ext_capacity + 4;
          if (this.strategy === 'double') {
            // Overflow consumes 1 cyber-dollar per copied item from the accumulated credit.
            this.bank_dollars -= copied_now;
          }
        }
        this.ext_size += 1;
        this.total_ops += 1;
        if (this.strategy === 'double') {
          // Each add is charged 3 cyber-dollars: 1 for insertion and 2 stored on the new item.
          this.bank_dollars += 2;
        }
        if (copied_now > 0 || count === 1) {
          this.ext_logs.unshift(
            'add #' + this.ext_size + ': ' +
            (copied_now > 0 ? 'Υπερχείλιση (' + copied_now + ' αντιγραφές -> cap=' + this.ext_capacity + ')' : 'Άμεση εισαγωγή (1 πράξη)') +
            (this.strategy === 'double' ? ' | Υπόλοιπο: ' + this.bank_dollars + ' cyber-$' : '')
          );
        }
      }
      if (this.ext_logs.length > 25) {
        this.ext_logs = this.ext_logs.slice(0, 25);
      }
    }

    /**
     * Mounts both Unit 01 interactive simulators into the host container.
     *
     * Args:
     *     container_el (HTMLElement): Host DOM container.
     */
    mount(container_el) {
      container_el.innerHTML =
        '<div class="card" id="u01_maxsub_box"></div>' +
        '<div class="card" id="u01_amortized_box"></div>';
      this.renderMaxsubPanel(container_el.querySelector('#u01_maxsub_box'));
      this.renderAmortizedPanel(container_el.querySelector('#u01_amortized_box'));
    }

    /**
     * Renders the interactive MaxsubFastest stepper and trace table.
     *
     * Args:
     *     panel_el (HTMLElement): Target panel element.
     */
    renderMaxsubPanel(panel_el) {
      const trace = [{ t: 0, val: '—', sum_cand: '—', mt: 0, best: 0 }];
      let prev_m = 0;
      let best_m = 0;
      for (let i = 0; i < this.arr.length; i += 1) {
        const cand = prev_m + this.arr[i];
        const mt = Math.max(0, cand);
        best_m = Math.max(best_m, mt);
        trace.push({ t: i + 1, val: this.arr[i], sum_cand: cand, mt: mt, best: best_m });
        prev_m = mt;
      }

      if (this.step_t > this.arr.length) {
        this.step_t = this.arr.length;
      }
      const curr = trace[this.step_t];

      let html = '<h3>Βηματική Ιχνηλάτηση: MaxsubFastest (O(n) χειρότερη)</h3>';
      html += '<div class="lab-toolbar">' +
        '<label class="lab-field">Πίνακας A: <input type="text" id="u01_arr_in" class="input-control" value="' + escapeHtml(this.arr.join(', ')) + '"></label>' +
        '<button type="button" class="btn btn-secondary" id="u01_apply_arr">Εφαρμογή</button>' +
        '<button type="button" class="btn btn-ghost" id="u01_preset_8">8 στοιχεία</button>' +
        '<button type="button" class="btn btn-secondary" id="u01_prev">Προηγούμενο</button>' +
        '<button type="button" class="btn btn-primary" id="u01_next">Επόμενο Βήμα (t+1)</button>' +
        '<button type="button" class="btn btn-ghost" id="u01_reset">Επαναφορά</button>' +
        '</div>';

      html += '<div class="array-strip">';
      for (let i = 0; i < this.arr.length; i += 1) {
        const active_cls = (i + 1) === this.step_t ? 'is-active' : '';
        html += '<div class="array-cell ' + active_cls + '"><span class="array-cell-idx">A[' + (i + 1) + ']</span><span class="array-cell-val">' + this.arr[i] + '</span></div>';
      }
      html += '</div>';

      html += '<div class="accent-callout">' +
        '<strong>Τρέχον Βήμα t = ' + curr.t + ':</strong> ' +
        'M<sub>t-1</sub> + A[t] = <code>' + curr.sum_cand + '</code> &rarr; ' +
        'M<sub>t</sub> = max{0, M<sub>t-1</sub> + A[t]} = <code>' + curr.mt + '</code> | ' +
        'Καλύτερο m = <code>' + curr.best + '</code>' +
        '</div>';

      html += '<div class="table-wrap"><table class="data-table"><thead><tr><th>t</th><th>A[t]</th><th>M_{t-1} + A[t]</th><th>M_t</th><th>Καλύτερο m</th></tr></thead><tbody>';
      for (let r = 0; r <= this.step_t; r += 1) {
        const row = trace[r];
        html += '<tr><td>' + row.t + '</td><td>' + row.val + '</td><td>' + row.sum_cand + '</td><td><strong>' + row.mt + '</strong></td><td><strong>' + row.best + '</strong></td></tr>';
      }
      html += '</tbody></table></div>';

      panel_el.innerHTML = html;

      panel_el.querySelector('#u01_apply_arr').addEventListener('click', () => {
        const parsed = panel_el.querySelector('#u01_arr_in').value
          .split(',')
          .map((s) => Number(s.trim()))
          .filter((v) => !Number.isNaN(v))
          .slice(0, 12);
        if (parsed.length > 0) {
          this.arr = parsed;
          this.step_t = 0;
          this.renderMaxsubPanel(panel_el);
        }
      });
      panel_el.querySelector('#u01_preset_8').addEventListener('click', () => {
        this.arr = [-2, 4, -1, 5, -9, 3, 4, -2];
        this.step_t = 0;
        this.renderMaxsubPanel(panel_el);
      });
      panel_el.querySelector('#u01_prev').addEventListener('click', () => {
        if (this.step_t > 0) {
          this.step_t -= 1;
          this.renderMaxsubPanel(panel_el);
        }
      });
      panel_el.querySelector('#u01_next').addEventListener('click', () => {
        if (this.step_t < this.arr.length) {
          this.step_t += 1;
          this.renderMaxsubPanel(panel_el);
        }
      });
      panel_el.querySelector('#u01_reset').addEventListener('click', () => {
        this.step_t = 0;
        this.renderMaxsubPanel(panel_el);
      });
    }

    /**
     * Renders the extendable array amortized analysis simulator.
     *
     * Args:
     *     panel_el (HTMLElement): Target panel element.
     */
    renderAmortizedPanel(panel_el) {
      const avg_cost = this.ext_size > 0 ? (this.total_ops / this.ext_size).toFixed(2) : '0.00';

      let html = '<h3>Προσομοιωτής Επεκτάσιμου Πίνακα &amp; Cyber-Δολαρίων</h3>';
      html += '<div class="lab-toolbar">' +
        '<button type="button" class="btn ' + (this.strategy === 'double' ? 'btn-primary' : 'btn-secondary') + '" id="u01_strat_dbl">Διπλασιασμός (x2)</button>' +
        '<button type="button" class="btn ' + (this.strategy === 'inc' ? 'btn-primary' : 'btn-secondary') + '" id="u01_strat_inc">Βηματική (+4)</button>' +
        '<button type="button" class="btn btn-secondary" id="u01_add_1">add (1)</button>' +
        '<button type="button" class="btn btn-secondary" id="u01_add_16">add (+16)</button>' +
        '<button type="button" class="btn btn-ghost" id="u01_ext_reset">Επαναφορά</button>' +
        '</div>';

      html += '<div class="grid-3">' +
        '<div class="card-deep"><div class="muted-text">Μέγεθος / Χωρητικότητα</div><div><code>' + this.ext_size + ' / ' + this.ext_capacity + '</code></div></div>' +
        '<div class="card-deep"><div class="muted-text">Συνολικό T(n) &amp; Μέσο T(n)/n</div><div><code>' + this.total_ops + ' πράξεις (' + avg_cost + ' / add)</code></div></div>' +
        '<div class="card-deep"><div class="muted-text">' + (this.strategy === 'double' ? 'Υπόλοιπο (3 cyber-$ / add)' : 'Συνολικές Αντιγραφές') + '</div><div><code>' + (this.strategy === 'double' ? this.bank_dollars + ' cyber-$' : this.total_copies) + '</code></div></div>' +
        '</div>';

      const shown_cap = Math.min(this.ext_capacity, 32);
      html += '<div class="array-strip">';
      for (let i = 0; i < shown_cap; i += 1) {
        const filled = i < this.ext_size;
        html += '<div class="array-cell ' + (filled ? 'is-active' : '') + '"><span class="array-cell-idx">' + i + '</span><span class="array-cell-val">' + (filled ? 'x' : '—') + '</span></div>';
      }
      if (this.ext_capacity > 32) {
        html += '<span class="meta-pill">... σύνολο ' + this.ext_capacity + ' κελιά</span>';
      }
      html += '</div>';

      html += '<div class="trace-log">';
      for (let i = 0; i < this.ext_logs.length; i += 1) {
        html += '<div class="trace-entry ' + (i === 0 ? 'is-highlight' : '') + '">' + escapeHtml(this.ext_logs[i]) + '</div>';
      }
      html += '</div>';

      panel_el.innerHTML = html;

      panel_el.querySelector('#u01_strat_dbl').addEventListener('click', () => {
        this.strategy = 'double';
        this.resetAmortized();
        this.renderAmortizedPanel(panel_el);
      });
      panel_el.querySelector('#u01_strat_inc').addEventListener('click', () => {
        this.strategy = 'inc';
        this.resetAmortized();
        this.renderAmortizedPanel(panel_el);
      });
      panel_el.querySelector('#u01_add_1').addEventListener('click', () => {
        this.addElements(1);
        this.renderAmortizedPanel(panel_el);
      });
      panel_el.querySelector('#u01_add_16').addEventListener('click', () => {
        this.addElements(16);
        this.renderAmortizedPanel(panel_el);
      });
      panel_el.querySelector('#u01_ext_reset').addEventListener('click', () => {
        this.resetAmortized();
        this.renderAmortizedPanel(panel_el);
      });
    }
  }

  /**
   * Renders the 1-Indexed Binary Min-Heap Visualizer for Unit 02.
   *
   * Supports insert with upheap, removeMin with smaller-child downheap, and Bottom-Up construction.
   * Methods: mount(container_el), insertKey(val), removeMin(), downheapFrom(start_idx), buildBottomUp(keys), renderTreeSvg().
   */
  class Unit02Lab {
    /**
     * Initializes the heap with Exercise 1 keys already built via inserts.
     */
    constructor() {
      // Uses 1-indexed storage: heap[0] remains unused per textbook convention.
      this.heap = [null, 3, 11, 6, 18, 14, 25, 9, 20];
      this.active_indices = [];
      this.logs = ['Φορτώθηκε ο σωρός της Άσκησης 1: [3, 11, 6, 18, 14, 25, 9, 20].'];
    }

    /**
     * Inserts a key at the end of the 1-indexed array and restores heap order via upheap.
     *
     * Args:
     *     val (number): Key to insert into the min-heap.
     */
    insertKey(val) {
      if (this.heap.length >= 32) {
        this.logs.unshift('Όριο απεικόνισης 31 κόμβων.');
        return;
      }
      this.heap.push(val);
      let idx = this.heap.length - 1;
      const swaps = [];
      while (idx > 1) {
        const parent = Math.floor(idx / 2);
        if (this.heap[parent] > this.heap[idx]) {
          const tmp = this.heap[parent];
          this.heap[parent] = this.heap[idx];
          this.heap[idx] = tmp;
          swaps.push('A[' + idx + ']<->A[' + parent + ']');
          idx = parent;
        } else {
          break;
        }
      }
      this.active_indices = [idx];
      this.logs.unshift('insert(' + val + '): ' + (swaps.length ? 'upheap: ' + swaps.join(', ') : 'καμία ανταλλαγή.'));
    }

    /**
     * Removes and returns the minimum root key, placing the last node at root and running downheap.
     */
    removeMin() {
      const n = this.heap.length - 1;
      if (n <= 0) {
        this.logs.unshift('Ο σωρός είναι κενός.');
        return;
      }
      const min_val = this.heap[1];
      if (n === 1) {
        this.heap.pop();
        this.active_indices = [];
        this.logs.unshift('removeMin() -> ' + min_val + ' (ο σωρός άδειασε).');
        return;
      }
      const last_val = this.heap.pop();
      this.heap[1] = last_val;
      const swaps = this.downheapFrom(1);
      this.active_indices = [1];
      this.logs.unshift('removeMin() -> ' + min_val + ' (A[n]=' + last_val + ' στη ρίζα): ' + (swaps.length ? 'downheap: ' + swaps.join(', ') : 'καμία ανταλλαγή.'));
    }

    /**
     * Performs downheap from start_idx by always comparing and selecting the smaller child.
     *
     * Args:
     *     start_idx (number): 1-based starting node index.
     *
     * Returns:
     *     Array<string>: Formatted swap descriptions for the trace log.
     */
    downheapFrom(start_idx) {
      const n = this.heap.length - 1;
      let idx = start_idx;
      const swaps = [];
      while (2 * idx <= n) {
        const left = 2 * idx;
        const right = 2 * idx + 1;
        // Selects smaller child strictly so heap-order holds over both subtrees.
        let smaller = left;
        if (right <= n && this.heap[right] < this.heap[left]) {
          smaller = right;
        }
        if (this.heap[idx] > this.heap[smaller]) {
          const tmp = this.heap[idx];
          this.heap[idx] = this.heap[smaller];
          this.heap[smaller] = tmp;
          swaps.push('A[' + idx + ']<->A[' + smaller + '] (μικρ. παιδί ' + this.heap[idx] + ')');
          idx = smaller;
        } else {
          break;
        }
      }
      return swaps;
    }

    /**
     * Builds a min-heap in O(n) via Bottom-Up downheaps from floor(n/2) down to 1.
     *
     * Args:
     *     keys (Array<number>): Input key sequence.
     */
    buildBottomUp(keys) {
      this.heap = [null].concat(keys.slice(0, 15));
      const n = this.heap.length - 1;
      let total_swaps = 0;
      for (let i = Math.floor(n / 2); i >= 1; i -= 1) {
        const swaps = this.downheapFrom(i);
        total_swaps += swaps.length;
      }
      this.active_indices = [];
      this.logs.unshift('Bottom-Up Heapify (' + n + ' κλειδιά): ' + total_swaps + ' ανταλλαγές συνολικά σε O(n).');
    }

    /**
     * Generates an inline SVG diagram of the binary heap tree.
     *
     * Returns:
     *     string: SVG markup using Architectural Draft CSS variables.
     */
    renderTreeSvg() {
      const n = this.heap.length - 1;
      const width = 680;
      const depth = n > 0 ? Math.floor(Math.log2(n)) : 0;
      const height = Math.max(180, (depth + 1) * 64 + 30);
      if (n <= 0) {
        return '<svg class="svg-stage" viewBox="0 0 680 120"><text x="340" y="65" text-anchor="middle" fill="var(--ink-muted)" font-size="14">Κενός Σωρός</text></svg>';
      }

      const coords = [null];
      for (let i = 1; i <= n; i += 1) {
        const level = Math.floor(Math.log2(i));
        const pos_in_level = i - Math.pow(2, level);
        const count_in_level = Math.pow(2, level);
        const x = ((pos_in_level + 0.5) / count_in_level) * width;
        const y = 34 + level * 62;
        coords.push({ x: x, y: y });
      }

      let edges_svg = '';
      for (let i = 2; i <= n; i += 1) {
        const p = Math.floor(i / 2);
        edges_svg += '<line x1="' + coords[p].x + '" y1="' + coords[p].y + '" x2="' + coords[i].x + '" y2="' + coords[i].y + '" stroke="var(--border-strong)" stroke-width="2" />';
      }

      let nodes_svg = '';
      for (let i = 1; i <= n; i += 1) {
        const is_act = this.active_indices.indexOf(i) !== -1;
        const fill_color = is_act ? 'var(--accent-primary)' : 'var(--bg-surface-elevated)';
        const stroke_color = is_act ? 'var(--accent-primary)' : 'var(--ink-muted)';
        const text_color = is_act ? 'var(--ink-on-accent)' : 'var(--ink-bright)';
        nodes_svg +=
          '<g>' +
            '<circle cx="' + coords[i].x + '" cy="' + coords[i].y + '" r="18" fill="' + fill_color + '" stroke="' + stroke_color + '" stroke-width="2" />' +
            '<text x="' + coords[i].x + '" y="' + (coords[i].y + 5) + '" text-anchor="middle" fill="' + text_color + '" font-family="var(--font-mono)" font-size="13" font-weight="700">' + this.heap[i] + '</text>' +
            '<text x="' + coords[i].x + '" y="' + (coords[i].y - 22) + '" text-anchor="middle" fill="var(--ink-subtle)" font-family="var(--font-mono)" font-size="10">[' + i + ']</text>' +
          '</g>';
      }

      return '<svg class="svg-stage" viewBox="0 0 ' + width + ' ' + height + '">' + edges_svg + nodes_svg + '</svg>';
    }

    /**
     * Mounts the heap visualizer and controls into the host container.
     *
     * Args:
     *     container_el (HTMLElement): Host DOM element.
     */
    mount(container_el) {
      let html = '<div class="card">';
      html += '<h3>Εργαστήριο Δυαδικού Σωρού (1-Indexed Min-Heap)</h3>';
      html += '<div class="lab-toolbar">' +
        '<label class="lab-field">Κλειδί: <input type="number" id="u02_key_in" class="input-control" value="5" style="width:84px;"></label>' +
        '<button type="button" class="btn btn-primary" id="u02_ins_btn">insert(k)</button>' +
        '<button type="button" class="btn btn-secondary" id="u02_rem_btn">removeMin()</button>' +
        '<button type="button" class="btn btn-secondary" id="u02_bu_btn">Bottom-Up (Άσκηση 1)</button>' +
        '<button type="button" class="btn btn-ghost" id="u02_ex1_btn">Φόρτωση Άσκησης 1</button>' +
        '<button type="button" class="btn btn-ghost" id="u02_clear_btn">Καθαρισμός</button>' +
        '</div>';

      html += this.renderTreeSvg();

      html += '<div><div class="muted-text" style="margin-bottom:6px;">Αναπαράσταση 1-indexed Πίνακα (A[0] αχρησιμοποίητο):</div><div class="array-strip">';
      for (let i = 1; i < this.heap.length; i += 1) {
        const act_cls = this.active_indices.indexOf(i) !== -1 ? 'is-active' : '';
        html += '<div class="array-cell ' + act_cls + '"><span class="array-cell-idx">A[' + i + ']</span><span class="array-cell-val">' + this.heap[i] + '</span></div>';
      }
      html += '</div></div>';

      html += '<div class="trace-log">';
      for (let i = 0; i < Math.min(this.logs.length, 12); i += 1) {
        html += '<div class="trace-entry ' + (i === 0 ? 'is-highlight' : '') + '">' + escapeHtml(this.logs[i]) + '</div>';
      }
      html += '</div></div>';

      container_el.innerHTML = html;

      container_el.querySelector('#u02_ins_btn').addEventListener('click', () => {
        const val = Number(container_el.querySelector('#u02_key_in').value);
        if (!Number.isNaN(val)) {
          this.insertKey(val);
          this.mount(container_el);
        }
      });
      container_el.querySelector('#u02_rem_btn').addEventListener('click', () => {
        this.removeMin();
        this.mount(container_el);
      });
      container_el.querySelector('#u02_bu_btn').addEventListener('click', () => {
        this.buildBottomUp([18, 11, 25, 6, 14, 9, 3, 20]);
        this.mount(container_el);
      });
      container_el.querySelector('#u02_ex1_btn').addEventListener('click', () => {
        this.heap = [null];
        const seq = [18, 11, 25, 6, 14, 9, 3, 20];
        for (let i = 0; i < seq.length; i += 1) {
          this.insertKey(seq[i]);
        }
        this.logs.unshift('Εκτελέστηκαν διαδοχικά 8 εισαγωγές Άσκησης 1 -> [3, 11, 6, 18, 14, 25, 9, 20].');
        this.mount(container_el);
      });
      container_el.querySelector('#u02_clear_btn').addEventListener('click', () => {
        this.heap = [null];
        this.active_indices = [];
        this.logs = ['Ο σωρός καθαρίστηκε.'];
        this.mount(container_el);
      });
    }
  }

  /**
   * Renders the Hash Table Collision & Cuckoo Hashing Simulator for Unit 03.
   *
   * Supports Linear Probing with DEFUNCT, Double Hashing, and 2-table Cuckoo eviction chains.
   * Methods: mount(container_el), switchMode(new_mode), hashOpen(k, j), putOpen(k), getOpen(k), removeOpen(k), putCuckoo(k).
   */
  class Unit03Lab {
    /**
     * Initializes hash tables for Open Addressing (N=11) and Cuckoo Hashing (N=7).
     */
    constructor() {
      this.mode = 'linear';
      this.size_n = 11;
      this.prime_q = 7;
      this.open_table = new Array(this.size_n).fill(null);
      this.cuckoo_n = 7;
      this.t1 = new Array(this.cuckoo_n).fill(null);
      this.t2 = new Array(this.cuckoo_n).fill(null);
      this.last_probed = [];
      this.logs = ['Επιλέξτε λειτουργία ή φορτώστε τα παραδείγματα των Ασκήσεων 1 & 2.'];
    }

    /**
     * Computes open-addressing probe index for step j.
     *
     * Args:
     *     key (number): Integer key to hash.
     *     j (number): Probe step offset starting at 0.
     *
     * Returns:
     *     number: Bucket index in [0, size_n - 1].
     */
    hashOpen(key, j) {
      const h1 = ((key % this.size_n) + this.size_n) % this.size_n;
      if (this.mode === 'linear') {
        return (h1 + j) % this.size_n;
      }
      const step = this.prime_q - (((key % this.prime_q) + this.prime_q) % this.prime_q);
      return (h1 + j * step) % this.size_n;
    }

    /**
     * Inserts a key into the open-addressing hash table, reusing DEFUNCT markers.
     *
     * Args:
     *     key (number): Integer key to insert.
     */
    putOpen(key) {
      const seq = [];
      let first_defunct = -1;
      for (let j = 0; j < this.size_n; j += 1) {
        const idx = this.hashOpen(key, j);
        seq.push(idx);
        const cell = this.open_table[idx];
        if (cell === null) {
          const target = first_defunct !== -1 ? first_defunct : idx;
          this.open_table[target] = key;
          this.last_probed = seq;
          this.logs.unshift('put(' + key + '): ανιχνεύσεις [' + seq.join(', ') + '] -> θέση ' + target + ' (' + seq.length + ' ανιχ.).');
          return;
        }
        if (cell === 'DEFUNCT' && first_defunct === -1) {
          first_defunct = idx;
        } else if (cell === key) {
          this.last_probed = seq;
          this.logs.unshift('put(' + key + '): υπάρχει ήδη στη θέση ' + idx + '.');
          return;
        }
      }
      if (first_defunct !== -1) {
        this.open_table[first_defunct] = key;
        this.last_probed = seq;
        this.logs.unshift('put(' + key + '): επαναχρησιμοποίηση DEFUNCT στη θέση ' + first_defunct + '.');
      } else {
        this.logs.unshift('put(' + key + '): Ο πίνακας είναι πλήρης!');
      }
    }

    /**
     * Searches for key in the open-addressing table, continuing past DEFUNCT cells.
     *
     * Args:
     *     key (number): Integer key to locate.
     */
    getOpen(key) {
      const seq = [];
      for (let j = 0; j < this.size_n; j += 1) {
        const idx = this.hashOpen(key, j);
        seq.push(idx);
        const cell = this.open_table[idx];
        if (cell === null) {
          this.last_probed = seq;
          this.logs.unshift('get(' + key + '): ανιχνεύσεις [' + seq.join(', ') + '] -> ΔΕΝ ΒΡΕΘΗΚΕ (κενό στο ' + idx + ').');
          return;
        }
        if (cell === key) {
          this.last_probed = seq;
          this.logs.unshift('get(' + key + '): ανιχνεύσεις [' + seq.join(', ') + '] -> ΒΡΕΘΗΚΕ στη θέση ' + idx + ' (' + seq.length + ' ανιχ.).');
          return;
        }
      }
      this.last_probed = seq;
      this.logs.unshift('get(' + key + '): ΔΕΝ ΒΡΕΘΗΚΕ.');
    }

    /**
     * Deletes a key by placing a DEFUNCT tombstone so probe chains stay intact.
     *
     * Args:
     *     key (number): Integer key to remove.
     */
    removeOpen(key) {
      const seq = [];
      for (let j = 0; j < this.size_n; j += 1) {
        const idx = this.hashOpen(key, j);
        seq.push(idx);
        const cell = this.open_table[idx];
        if (cell === null) {
          this.last_probed = seq;
          this.logs.unshift('remove(' + key + '): δεν υπάρχει στον πίνακα.');
          return;
        }
        if (cell === key) {
          // Leaves DEFUNCT marker instead of null so subsequent keys stay reachable.
          this.open_table[idx] = 'DEFUNCT';
          this.last_probed = seq;
          this.logs.unshift('remove(' + key + '): θέση ' + idx + ' -> DEFUNCT (ανιχνεύσεις: ' + seq.join(', ') + ').');
          return;
        }
      }
    }

    /**
     * Executes Cuckoo Hashing insertion with cycle detection after n + 1 displacements.
     *
     * Args:
     *     key (number): Integer key to place in T1 or T2.
     */
    putCuckoo(key) {
      const h1 = (x) => ((x % this.cuckoo_n) + this.cuckoo_n) % this.cuckoo_n;
      const h2 = (x) => Math.floor(Math.abs(x) / this.cuckoo_n) % this.cuckoo_n;
      const p1 = h1(key);
      const p2 = h2(key);
      if (this.t1[p1] === key || this.t2[p2] === key) {
        this.logs.unshift('put(' + key + '): υπάρχει ήδη σε T1[' + p1 + '] ή T2[' + p2 + '].');
        return;
      }
      const existing_n = this.t1.filter((v) => v !== null).length + this.t2.filter((v) => v !== null).length;
      const limit = existing_n + 1;
      let curr = key;
      let use_t1 = true;
      const chain = [];

      for (let step = 0; step < limit; step += 1) {
        if (use_t1) {
          const idx = h1(curr);
          const displaced = this.t1[idx];
          this.t1[idx] = curr;
          chain.push(curr + '->T1[' + idx + ']');
          if (displaced === null) {
            this.logs.unshift('Cuckoo put(' + key + '): ' + chain.join(' | ') + ' (Ολοκληρώθηκε).');
            return;
          }
          curr = displaced;
        } else {
          const idx = h2(curr);
          const displaced = this.t2[idx];
          this.t2[idx] = curr;
          chain.push(curr + '->T2[' + idx + ']');
          if (displaced === null) {
            this.logs.unshift('Cuckoo put(' + key + '): ' + chain.join(' | ') + ' (Ολοκληρώθηκε).');
            return;
          }
          curr = displaced;
        }
        use_t1 = !use_t1;
      }

      this.logs.unshift('ΚΥΚΛΟΣ Cuckoo στο put(' + key + ') μετά από ' + limit + ' τοποθετήσεις (' + chain.join(' | ') + ') -> Απαιτείται REHASH!');
    }

    /**
     * Switches between linear probing, double hashing, and cuckoo hashing modes.
     *
     * Args:
     *     new_mode (string): One of 'linear', 'double', or 'cuckoo'.
     */
    switchMode(new_mode) {
      this.mode = new_mode;
      this.open_table = new Array(this.size_n).fill(null);
      this.t1 = new Array(this.cuckoo_n).fill(null);
      this.t2 = new Array(this.cuckoo_n).fill(null);
      this.last_probed = [];
      this.logs = ['Λειτουργία: ' + new_mode + '.'];
    }

    /**
     * Mounts the Hash Tables & Cuckoo lab into the target container.
     *
     * Args:
     *     container_el (HTMLElement): Host DOM element.
     */
    mount(container_el) {
      let html = '<div class="card">';
      html += '<h3>Εργαστήριο Κατακερματισμού &amp; Κούκου</h3>';
      html += '<div class="lab-toolbar">' +
        '<button type="button" class="btn ' + (this.mode === 'linear' ? 'btn-primary' : 'btn-secondary') + '" data-mode="linear">Γραμμική Ανίχνευση (N=11)</button>' +
        '<button type="button" class="btn ' + (this.mode === 'double' ? 'btn-primary' : 'btn-secondary') + '" data-mode="double">Διπλός Κατακερματισμός (N=11, q=7)</button>' +
        '<button type="button" class="btn ' + (this.mode === 'cuckoo' ? 'btn-primary' : 'btn-secondary') + '" data-mode="cuckoo">Κατακερματισμός Κούκου (N=7)</button>' +
        '</div>';

      if (this.mode !== 'cuckoo') {
        const count = this.open_table.filter((v) => v !== null && v !== 'DEFUNCT').length;
        const alpha = count / this.size_n;
        const exp_probes = alpha < 1 ? (1 / (1 - alpha)).toFixed(2) : 'inf';
        html += '<div class="lab-toolbar">' +
          '<label class="lab-field">Κλειδί k: <input type="number" id="u03_key_in" class="input-control" value="47" style="width:90px;"></label>' +
          '<button type="button" class="btn btn-primary" id="u03_put">put(k)</button>' +
          '<button type="button" class="btn btn-secondary" id="u03_get">get(k)</button>' +
          '<button type="button" class="btn btn-secondary" id="u03_rem">remove(k)</button>' +
          '<button type="button" class="btn btn-ghost" id="u03_ex1">Φόρτωση {3,14,25,36,47}</button>' +
          '<button type="button" class="btn btn-ghost" id="u03_clr">Καθαρισμός</button>' +
          '</div>';

        html += '<div class="grid-3">' +
          '<div class="card-deep"><div class="muted-text">Συντελεστής α = n / N</div><div><code>' + count + ' / ' + this.size_n + ' = ' + alpha.toFixed(2) + '</code></div></div>' +
          '<div class="card-deep"><div class="muted-text">Αναμενόμενες Ανιχνεύσεις 1/(1-α)</div><div><code>' + exp_probes + '</code></div></div>' +
          '<div class="card-deep"><div class="muted-text">Όριο α <= 1/2</div><div><code>' + (alpha <= 0.5 ? 'Εντός ορίου O(1)' : 'Υπέρβαση -> Rehash!') + '</code></div></div>' +
          '</div>';

        html += '<div class="array-strip">';
        for (let i = 0; i < this.size_n; i += 1) {
          const val = this.open_table[i];
          const cls = val === 'DEFUNCT' ? 'is-defunct' : (this.last_probed.indexOf(i) !== -1 ? 'is-active' : '');
          html += '<div class="array-cell ' + cls + '"><span class="array-cell-idx">' + i + '</span><span class="array-cell-val">' + (val === null ? '—' : val) + '</span></div>';
        }
        html += '</div>';
      } else {
        html += '<div class="lab-toolbar">' +
          '<label class="lab-field">Κλειδί k: <input type="number" id="u03_key_in" class="input-control" value="107" style="width:90px;"></label>' +
          '<button type="button" class="btn btn-primary" id="u03_cuckoo_put">put(k)</button>' +
          '<button type="button" class="btn btn-ghost" id="u03_ex2">Άσκηση 2: {9, 58, 107}</button>' +
          '<button type="button" class="btn btn-ghost" id="u03_clr">Καθαρισμός</button>' +
          '</div>';
        html += '<p class="muted-text"><code>h1(k) = k mod 7</code> | <code>h2(k) = floor(k/7) mod 7</code></p>';
        html += '<div class="grid-2">' +
          '<div class="card-deep"><strong>Πίνακας T1</strong><div class="array-strip" style="margin-top:10px;">' +
          this.t1.map((v, idx) => '<div class="array-cell ' + (v !== null ? 'is-active' : '') + '"><span class="array-cell-idx">T1[' + idx + ']</span><span class="array-cell-val">' + (v === null ? '—' : v) + '</span></div>').join('') +
          '</div></div>' +
          '<div class="card-deep"><strong>Πίνακας T2</strong><div class="array-strip" style="margin-top:10px;">' +
          this.t2.map((v, idx) => '<div class="array-cell ' + (v !== null ? 'is-active' : '') + '"><span class="array-cell-idx">T2[' + idx + ']</span><span class="array-cell-val">' + (v === null ? '—' : v) + '</span></div>').join('') +
          '</div></div></div>';
      }

      html += '<div class="trace-log">';
      for (let i = 0; i < Math.min(this.logs.length, 10); i += 1) {
        html += '<div class="trace-entry ' + (i === 0 ? 'is-highlight' : '') + '">' + escapeHtml(this.logs[i]) + '</div>';
      }
      html += '</div></div>';

      container_el.innerHTML = html;

      const mode_btns = container_el.querySelectorAll('[data-mode]');
      for (let i = 0; i < mode_btns.length; i += 1) {
        mode_btns[i].addEventListener('click', (evt) => {
          this.switchMode(evt.currentTarget.getAttribute('data-mode'));
          this.mount(container_el);
        });
      }

      if (this.mode !== 'cuckoo') {
        container_el.querySelector('#u03_put').addEventListener('click', () => {
          const k = Number(container_el.querySelector('#u03_key_in').value);
          if (!Number.isNaN(k)) { this.putOpen(k); this.mount(container_el); }
        });
        container_el.querySelector('#u03_get').addEventListener('click', () => {
          const k = Number(container_el.querySelector('#u03_key_in').value);
          if (!Number.isNaN(k)) { this.getOpen(k); this.mount(container_el); }
        });
        container_el.querySelector('#u03_rem').addEventListener('click', () => {
          const k = Number(container_el.querySelector('#u03_key_in').value);
          if (!Number.isNaN(k)) { this.removeOpen(k); this.mount(container_el); }
        });
        container_el.querySelector('#u03_ex1').addEventListener('click', () => {
          this.open_table = new Array(this.size_n).fill(null);
          const keys = [3, 14, 25, 36, 47];
          for (let i = 0; i < keys.length; i += 1) { this.putOpen(keys[i]); }
          this.mount(container_el);
        });
      } else {
        container_el.querySelector('#u03_cuckoo_put').addEventListener('click', () => {
          const k = Number(container_el.querySelector('#u03_key_in').value);
          if (!Number.isNaN(k)) { this.putCuckoo(k); this.mount(container_el); }
        });
        container_el.querySelector('#u03_ex2').addEventListener('click', () => {
          this.t1 = new Array(this.cuckoo_n).fill(null);
          this.t2 = new Array(this.cuckoo_n).fill(null);
          this.putCuckoo(9);
          this.putCuckoo(58);
          this.putCuckoo(107);
          this.mount(container_el);
        });
      }
      container_el.querySelector('#u03_clr').addEventListener('click', () => {
        this.switchMode(this.mode);
        this.mount(container_el);
      });
    }
  }

  global_scope.MidtermApp = global_scope.MidtermApp || {};
  global_scope.MidtermApp.labs = global_scope.MidtermApp.labs || {};
  global_scope.MidtermApp.labs['00'] = new Unit00Lab();
  global_scope.MidtermApp.labs['01'] = new Unit01Lab();
  global_scope.MidtermApp.labs['02'] = new Unit02Lab();
  global_scope.MidtermApp.labs['03'] = new Unit03Lab();
})(window);
