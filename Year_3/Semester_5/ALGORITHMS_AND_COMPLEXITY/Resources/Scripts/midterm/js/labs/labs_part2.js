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
   * Renders the Union-Find Forest Visualizer for Unit 04.
   *
   * Supports Union by Size, optional Path Compression on find, and Exercise 1/3 presets.
   * Methods: mount(container_el), resetSets(), findNode(x), unionSets(u, v), renderForestSvg().
   */
  class Unit04Lab {
    /**
     * Initializes 8 disjoint singleton sets indexed 1..8.
     */
    constructor() {
      this.node_count = 8;
      this.use_compression = true;
      this.resetSets();
    }

    /**
     * Resets parent and size arrays to singleton sets.
     */
    resetSets() {
      this.parent = [null];
      this.size = [null];
      for (let i = 1; i <= this.node_count; i += 1) {
        this.parent.push(i);
        this.size.push(1);
      }
      this.highlight_nodes = [];
      this.logs = ['Αρχική κατάσταση: 8 μοναδιαία σύνολα {1}..{8}.'];
    }

    /**
     * Finds the set representative for element x, optionally compressing the traversed path.
     *
     * Args:
     *     x (number): Node index in 1..8.
     *     silent (boolean): Suppresses trace log entry when called internally by union.
     *
     * Returns:
     *     number: Root representative index.
     */
    findNode(x, silent) {
      const path = [];
      let curr = x;
      while (this.parent[curr] !== curr) {
        path.push(curr);
        curr = this.parent[curr];
      }
      const root = curr;
      const changed = [];
      if (this.use_compression) {
        for (let i = 0; i < path.length; i += 1) {
          const node = path[i];
          if (this.parent[node] !== root) {
            this.parent[node] = root;
            changed.push('parent[' + node + ']=' + root);
          }
        }
      }
      if (!silent) {
        this.highlight_nodes = path.concat([root]);
        this.logs.unshift(
          'find(' + x + ') -> ρίζα ' + root + ' (διαδρομή μήκους ' + path.length + ')' +
          (this.use_compression ? (changed.length ? ' | Συμπίεση: ' + changed.join(', ') : ' | καμία αλλαγή') : ' | χωρίς συμπίεση')
        );
      }
      return root;
    }

    /**
     * Unites the sets containing u and v using Union by Size (smaller root ties to larger root).
     *
     * Args:
     *     u (number): First element index.
     *     v (number): Second element index.
     */
    unionSets(u, v) {
      const r1 = this.findNode(u, true);
      const r2 = this.findNode(v, true);
      if (r1 === r2) {
        this.highlight_nodes = [r1];
        this.logs.unshift('union(' + u + ', ' + v + '): ίδια ρίζα (' + r1 + ') -> καμία αλλαγή.');
        return;
      }
      let keep = r1;
      let attach = r2;
      // Tie-breaks equal sizes by keeping the smaller node index as root per Exercise 1.
      if (this.size[r1] < this.size[r2] || (this.size[r1] === this.size[r2] && r2 < r1)) {
        keep = r2;
        attach = r1;
      }
      this.parent[attach] = keep;
      this.size[keep] += this.size[attach];
      this.highlight_nodes = [keep, attach];
      this.logs.unshift('union(' + u + ', ' + v + '): parent[' + attach + '] = ' + keep + ', size[' + keep + '] = ' + this.size[keep] + '.');
    }

    /**
     * Computes tree layout coordinates and returns SVG markup for the Union-Find forest.
     *
     * Returns:
     *     string: SVG diagram showing parent pointers and root sizes.
     */
    renderForestSvg() {
      const children = {};
      const roots = [];
      for (let i = 1; i <= this.node_count; i += 1) {
        children[i] = [];
      }
      for (let i = 1; i <= this.node_count; i += 1) {
        if (this.parent[i] === i) {
          roots.push(i);
        } else {
          children[this.parent[i]].push(i);
        }
      }

      const positions = {};
      let leaf_cursor = 0;
      const max_depth_tracker = { max_d: 0 };

      const layoutSubtree = (node, depth) => {
        if (depth > max_depth_tracker.max_d) {
          max_depth_tracker.max_d = depth;
        }
        const ch = children[node];
        if (ch.length === 0) {
          const x = 52 + leaf_cursor * 76;
          leaf_cursor += 1;
          positions[node] = { x: x, y: 42 + depth * 64 };
          return x;
        }
        let sum_x = 0;
        for (let i = 0; i < ch.length; i += 1) {
          sum_x += layoutSubtree(ch[i], depth + 1);
        }
        const avg_x = sum_x / ch.length;
        positions[node] = { x: avg_x, y: 42 + depth * 64 };
        return avg_x;
      };

      for (let i = 0; i < roots.length; i += 1) {
        layoutSubtree(roots[i], 0);
      }

      const width = Math.max(660, leaf_cursor * 76 + 40);
      const height = Math.max(170, (max_depth_tracker.max_d + 1) * 64 + 44);
      let edges = '';
      let nodes = '';

      for (let i = 1; i <= this.node_count; i += 1) {
        if (this.parent[i] !== i) {
          const p = positions[this.parent[i]];
          const c = positions[i];
          edges += '<line x1="' + p.x + '" y1="' + p.y + '" x2="' + c.x + '" y2="' + c.y + '" stroke="var(--border-strong)" stroke-width="2" />';
        }
      }

      for (let i = 1; i <= this.node_count; i += 1) {
        const pos = positions[i];
        const is_root = this.parent[i] === i;
        const is_hl = this.highlight_nodes.indexOf(i) !== -1;
        const fill_c = is_hl ? 'var(--accent-primary)' : 'var(--bg-surface-elevated)';
        const stroke_c = is_root ? 'var(--accent-primary)' : 'var(--ink-muted)';
        const text_c = is_hl ? 'var(--ink-on-accent)' : 'var(--ink-bright)';
        nodes += '<g>' +
          '<circle cx="' + pos.x + '" cy="' + pos.y + '" r="19" fill="' + fill_c + '" stroke="' + stroke_c + '" stroke-width="2.2" />' +
          '<text x="' + pos.x + '" y="' + (pos.y + 5) + '" text-anchor="middle" fill="' + text_c + '" font-family="var(--font-mono)" font-size="14" font-weight="700">' + i + '</text>' +
          (is_root ? '<text x="' + pos.x + '" y="' + (pos.y - 23) + '" text-anchor="middle" fill="var(--accent-primary)" font-family="var(--font-mono)" font-size="11">sz=' + this.size[i] + '</text>' : '') +
          '</g>';
      }

      return '<svg class="svg-stage" viewBox="0 0 ' + width + ' ' + height + '">' + edges + nodes + '</svg>';
    }

    /**
     * Mounts the Union-Find interactive lab inside the target container.
     *
     * Args:
     *     container_el (HTMLElement): Host DOM element.
     */
    mount(container_el) {
      let opts = '';
      for (let i = 1; i <= this.node_count; i += 1) {
        opts += '<option value="' + i + '">' + i + '</option>';
      }

      let html = '<div class="card">';
      html += '<h3>Εργαστήριο Δάσους Union-Find (1..8)</h3>';
      html += '<div class="lab-toolbar">' +
        '<label class="lab-field">u: <select id="u04_u" class="select-control">' + opts + '</select></label>' +
        '<label class="lab-field">v: <select id="u04_v" class="select-control">' + opts.replace('value="2"', 'value="2" selected') + '</select></label>' +
        '<button type="button" class="btn btn-primary" id="u04_union_btn">union(u, v)</button>' +
        '<label class="lab-field">x: <select id="u04_x" class="select-control">' + opts.replace('value="8"', 'value="8" selected') + '</select></label>' +
        '<button type="button" class="btn btn-secondary" id="u04_find_btn">find(x)</button>' +
        '<label class="lab-field"><input type="checkbox" id="u04_comp_chk" ' + (this.use_compression ? 'checked' : '') + '> Συμπίεση Διαδρομής</label>' +
        '</div>';

      html += '<div class="lab-toolbar">' +
        '<button type="button" class="btn btn-ghost" id="u04_ex1_btn">Πρότυπο: Άσκηση 1 (Έως ύψος 3 &amp; find(8))</button>' +
        '<button type="button" class="btn btn-ghost" id="u04_h3_btn">Οριακό Δέντρο h=3 (χωρίς find)</button>' +
        '<button type="button" class="btn btn-ghost" id="u04_reset_btn">Επαναφορά</button>' +
        '</div>';

      html += this.renderForestSvg();

      html += '<div class="grid-2">' +
        '<div class="card-deep"><strong>Πίνακας parent[1..8]</strong><div class="array-strip" style="margin-top:8px;">' +
        this.parent.slice(1).map((p, idx) => '<div class="array-cell ' + (this.highlight_nodes.indexOf(idx + 1) !== -1 ? 'is-active' : '') + '"><span class="array-cell-idx">' + (idx + 1) + '</span><span class="array-cell-val">' + p + '</span></div>').join('') +
        '</div></div>' +
        '<div class="card-deep"><strong>Πίνακας size[1..8]</strong><div class="array-strip" style="margin-top:8px;">' +
        this.size.slice(1).map((s, idx) => '<div class="array-cell ' + (this.parent[idx + 1] === idx + 1 ? 'is-active' : '') + '"><span class="array-cell-idx">' + (idx + 1) + '</span><span class="array-cell-val">' + s + '</span></div>').join('') +
        '</div></div></div>';

      html += '<div class="trace-log">';
      for (let i = 0; i < Math.min(this.logs.length, 10); i += 1) {
        html += '<div class="trace-entry ' + (i === 0 ? 'is-highlight' : '') + '">' + escapeHtml(this.logs[i]) + '</div>';
      }
      html += '</div></div>';

      container_el.innerHTML = html;

      container_el.querySelector('#u04_comp_chk').addEventListener('change', (evt) => {
        this.use_compression = evt.target.checked;
      });
      container_el.querySelector('#u04_union_btn').addEventListener('click', () => {
        const u = Number(container_el.querySelector('#u04_u').value);
        const v = Number(container_el.querySelector('#u04_v').value);
        this.unionSets(u, v);
        this.mount(container_el);
      });
      container_el.querySelector('#u04_find_btn').addEventListener('click', () => {
        const x = Number(container_el.querySelector('#u04_x').value);
        this.findNode(x, false);
        this.mount(container_el);
      });
      container_el.querySelector('#u04_h3_btn').addEventListener('click', () => {
        this.resetSets();
        const pairs = [[1, 2], [3, 4], [5, 6], [1, 3], [7, 8], [5, 7], [1, 5]];
        for (let i = 0; i < pairs.length; i += 1) { this.unionSets(pairs[i][0], pairs[i][1]); }
        this.logs.unshift('Κατασκευάστηκε δέντρο ύψους h = 3 = log_2(8) (διαδρομή 8->7->5->1).');
        this.mount(container_el);
      });
      container_el.querySelector('#u04_ex1_btn').addEventListener('click', () => {
        this.use_compression = true;
        this.resetSets();
        const pairs = [[1, 2], [3, 4], [5, 6], [1, 3], [7, 8], [5, 7], [1, 5]];
        for (let i = 0; i < pairs.length; i += 1) { this.unionSets(pairs[i][0], pairs[i][1]); }
        this.findNode(8, false);
        this.findNode(4, false);
        this.unionSets(4, 8);
        this.mount(container_el);
      });
      container_el.querySelector('#u04_reset_btn').addEventListener('click', () => {
        this.resetSets();
        this.mount(container_el);
      });
    }
  }

  /**
   * Renders the Sorting Trace Stepper and Decision Tree Lower Bound Calculator for Unit 05.
   *
   * Generates deterministic execution snapshots for Merge-Sort and inPlaceQuickSort alongside n! bounds.
   * Methods: mount(container_el), buildSnapshots(), buildMergeSnapshots(arr), buildQuickSnapshots(arr), factorial(n).
   */
  class Unit05Lab {
    /**
     * Initializes default array input and lower-bound n parameter.
     */
    constructor() {
      this.arr = [6, 2, 8, 4, 1, 5];
      this.algo = 'merge';
      this.step_idx = 0;
      this.lb_n = 5;
      this.snapshots = [];
      this.buildSnapshots();
    }

    /**
     * Rebuilds the snapshot list for the selected sorting algorithm and input array.
     */
    buildSnapshots() {
      this.snapshots = this.algo === 'merge' ? this.buildMergeSnapshots(this.arr) : this.buildQuickSnapshots(this.arr);
      this.step_idx = 0;
    }

    /**
     * Records step-by-step Merge-Sort divisions and merges with exact comparison counts.
     *
     * Args:
     *     source (Array<number>): Input array to sort.
     *
     * Returns:
     *     Array<object>: Trace snapshot entries.
     */
    buildMergeSnapshots(source) {
      const snaps = [{ array: source.slice(), active: [], msg: 'Αρχικός πίνακας (' + source.length + ' στοιχεία).', comps: 0 }];
      let total_comps = 0;

      const sortRange = (arr, left, right) => {
        if (left >= right) {
          return;
        }
        const mid = Math.floor((left + right) / 2);
        snaps.push({
          array: arr.slice(),
          active: [left, mid, right],
          msg: 'Διαίρεση [' + left + '..' + right + '] σε [' + left + '..' + mid + '] και [' + (mid + 1) + '..' + right + '].',
          comps: total_comps
        });
        sortRange(arr, left, mid);
        sortRange(arr, mid + 1, right);

        const left_part = arr.slice(left, mid + 1);
        const right_part = arr.slice(mid + 1, right + 1);
        let i = 0;
        let j = 0;
        let k = left;
        let local_comps = 0;
        while (i < left_part.length && j < right_part.length) {
          local_comps += 1;
          total_comps += 1;
          if (left_part[i] <= right_part[j]) {
            arr[k] = left_part[i];
            i += 1;
          } else {
            arr[k] = right_part[j];
            j += 1;
          }
          k += 1;
        }
        while (i < left_part.length) { arr[k] = left_part[i]; i += 1; k += 1; }
        while (j < right_part.length) { arr[k] = right_part[j]; j += 1; k += 1; }

        const range_indices = [];
        for (let idx = left; idx <= right; idx += 1) { range_indices.push(idx); }
        snaps.push({
          array: arr.slice(),
          active: range_indices,
          msg: 'merge([' + left_part.join(',') + '], [' + right_part.join(',') + ']) -> [' + arr.slice(left, right + 1).join(',') + '] (' + local_comps + ' συγκρ.).',
          comps: total_comps
        });
      };

      const work = source.slice();
      sortRange(work, 0, work.length - 1);
      return snaps;
    }

    /**
     * Records step-by-step 3-way inPlaceQuickSort snapshots using pivot S[r].
     *
     * Args:
     *     source (Array<number>): Input array to sort.
     *
     * Returns:
     *     Array<object>: Trace snapshot entries.
     */
    buildQuickSnapshots(source) {
      const snaps = [{ array: source.slice(), active: [], msg: 'Αρχικός πίνακας (pivot = τελευταίο στοιχείο S[r]).', comps: 0 }];
      let total_comps = 0;

      const qsort = (arr, l, r) => {
        if (l >= r) {
          return;
        }
        const x = arr[r];
        let j = l;
        let k = r - 1;
        // Scan 1 separates elements < x from elements >= x.
        while (j <= k) {
          while (j <= k && arr[j] < x) { total_comps += 1; j += 1; }
          while (k >= j && arr[k] >= x) { total_comps += 1; k -= 1; }
          if (j < k) {
            const tmp = arr[j];
            arr[j] = arr[k];
            arr[k] = tmp;
            snaps.push({
              array: arr.slice(),
              active: [j, k, r],
              msg: 'Σάρωση 1 (pivot=' + x + '): ανταλλαγή A[' + j + '] <-> A[' + k + '].',
              comps: total_comps
            });
            j += 1;
            k -= 1;
          }
        }
        const h = j;
        // Scan 2 places all elements equal to pivot x at indices [h..k2].
        let j2 = h;
        let k2 = r;
        while (j2 <= k2) {
          while (j2 <= k2 && arr[j2] === x) { j2 += 1; }
          while (k2 >= j2 && arr[k2] > x) { k2 -= 1; }
          if (j2 < k2) {
            const tmp = arr[j2];
            arr[j2] = arr[k2];
            arr[k2] = tmp;
            j2 += 1;
            k2 -= 1;
          }
        }
        snaps.push({
          array: arr.slice(),
          active: [h, k2],
          msg: 'inPlacePartition([' + l + '..' + r + '], pivot=' + x + ') -> όρια (h=' + h + ', k=' + k2 + ').',
          comps: total_comps
        });
        qsort(arr, l, h - 1);
        qsort(arr, k2 + 1, r);
      };

      const work = source.slice();
      qsort(work, 0, work.length - 1);
      return snaps;
    }

    /**
     * Computes exact factorial n! for small integers.
     *
     * Args:
     *     n (number): Non-negative integer.
     *
     * Returns:
     *     number: Value of n!.
     */
    factorial(n) {
      let res = 1;
      for (let i = 2; i <= n; i += 1) { res *= i; }
      return res;
    }

    /**
     * Mounts the sorting stepper and decision tree calculator inside the host container.
     *
     * Args:
     *     container_el (HTMLElement): Host DOM element.
     */
    mount(container_el) {
      const snap = this.snapshots[this.step_idx] || this.snapshots[0];
      const fact_val = this.factorial(this.lb_n);
      const exact_min = Math.ceil(Math.log2(fact_val));
      const approx_bound = ((this.lb_n / 2) * Math.log2(this.lb_n / 2)).toFixed(2);

      let html = '<div class="grid-2">';
      html += '<div class="card">' +
        '<h3>Ιχνηλάτηση Merge-Sort &amp; inPlaceQuickSort</h3>' +
        '<div class="lab-toolbar">' +
          '<button type="button" class="btn ' + (this.algo === 'merge' ? 'btn-primary' : 'btn-secondary') + '" id="u05_m_btn">Merge-Sort</button>' +
          '<button type="button" class="btn ' + (this.algo === 'quick' ? 'btn-primary' : 'btn-secondary') + '" id="u05_q_btn">inPlaceQuickSort</button>' +
          '<label class="lab-field">A: <input type="text" id="u05_arr_in" class="input-control" value="' + escapeHtml(this.arr.join(', ')) + '" style="width:150px;"></label>' +
          '<button type="button" class="btn btn-ghost" id="u05_apply">Ορισμός</button>' +
        '</div>' +
        '<div class="lab-toolbar">' +
          '<button type="button" class="btn btn-secondary" id="u05_prev">Προηγούμενο</button>' +
          '<button type="button" class="btn btn-primary" id="u05_next">Επόμενο Βήμα (' + (this.step_idx + 1) + '/' + this.snapshots.length + ')</button>' +
          '<button type="button" class="btn btn-ghost" id="u05_rst">Αρχή</button>' +
        '</div>' +
        '<div class="array-strip">' +
          snap.array.map((v, i) => '<div class="array-cell ' + (snap.active.indexOf(i) !== -1 ? 'is-active' : '') + '"><span class="array-cell-idx">' + i + '</span><span class="array-cell-val">' + v + '</span></div>').join('') +
        '</div>' +
        '<div class="accent-callout"><strong>Βήμα ' + (this.step_idx + 1) + ':</strong> ' + escapeHtml(snap.msg) + '<br>Συνολικές συγκρίσεις: <code>' + snap.comps + '</code></div>' +
      '</div>';

      html += '<div class="card">' +
        '<h3>Υπολογιστής Κάτω Ορίου Δέντρου Αποφάσεων</h3>' +
        '<div class="lab-toolbar">' +
          '<label class="lab-field">n = <strong>' + this.lb_n + '</strong> <input type="range" id="u05_lb_slider" min="2" max="10" value="' + this.lb_n + '"></label>' +
        '</div>' +
        '<div class="table-wrap"><table class="data-table"><tbody>' +
          '<tr><td>Πλήθος μεταθέσεων (ελάχιστα φύλλα L &ge; n!)</td><td><code>' + fact_val.toLocaleString('en-US') + '</code></td></tr>' +
          '<tr><td>Ελάχιστες συγκρίσεις &lceil;log<sub>2</sub>(n!)&rceil;</td><td><code>' + exact_min + '</code> (2<sup>' + exact_min + '</sup> = ' + Math.pow(2, exact_min).toLocaleString('en-US') + ')</td></tr>' +
          '<tr><td>Αδυναμία με ' + (exact_min - 1) + ' συγκρίσεις</td><td><code>2<sup>' + (exact_min - 1) + '</sup> = ' + Math.pow(2, exact_min - 1).toLocaleString('en-US') + ' &lt; ' + fact_val.toLocaleString('en-US') + '</code></td></tr>' +
          '<tr><td>Κάτω φράγμα απόδειξης (n/2) log<sub>2</sub>(n/2)</td><td><code>' + approx_bound + '</code></td></tr>' +
        '</tbody></table></div>' +
      '</div>';
      html += '</div>';

      container_el.innerHTML = html;

      container_el.querySelector('#u05_m_btn').addEventListener('click', () => {
        this.algo = 'merge';
        this.buildSnapshots();
        this.mount(container_el);
      });
      container_el.querySelector('#u05_q_btn').addEventListener('click', () => {
        this.algo = 'quick';
        this.buildSnapshots();
        this.mount(container_el);
      });
      container_el.querySelector('#u05_apply').addEventListener('click', () => {
        const parsed = container_el.querySelector('#u05_arr_in').value
          .split(',').map((s) => Number(s.trim())).filter((v) => !Number.isNaN(v)).slice(0, 10);
        if (parsed.length >= 2) {
          this.arr = parsed;
          this.buildSnapshots();
          this.mount(container_el);
        }
      });
      container_el.querySelector('#u05_prev').addEventListener('click', () => {
        if (this.step_idx > 0) { this.step_idx -= 1; this.mount(container_el); }
      });
      container_el.querySelector('#u05_next').addEventListener('click', () => {
        if (this.step_idx < this.snapshots.length - 1) { this.step_idx += 1; this.mount(container_el); }
      });
      container_el.querySelector('#u05_rst').addEventListener('click', () => {
        this.step_idx = 0;
        this.mount(container_el);
      });
      container_el.querySelector('#u05_lb_slider').addEventListener('input', (evt) => {
        this.lb_n = Number(evt.target.value);
        this.mount(container_el);
      });
    }
  }

  /**
   * Renders the Greedy Method Lab (Knapsack, Task Scheduling Gantt, Huffman Builder) for Unit 06.
   *
   * Demonstrates Fractional vs 0-1 Knapsack, s_i vs f_i scheduling counterexamples, and Huffman coding.
   * Methods: mount(container_el), renderKnapsack(panel_el), renderSchedule(panel_el), renderHuffman(panel_el), scheduleIntervals(tasks, sort_by).
   */
  class Unit06Lab {
    /**
     * Initializes sub-tab state and Exercise 1/3 datasets.
     */
    constructor() {
      this.sub_tab = 'huffman';
      this.knapsack_w = 10;
      this.knapsack_items = [
        { name: 'A', w: 6, b: 36 },
        { name: 'B', w: 5, b: 25 },
        { name: 'C', w: 5, b: 25 }
      ];
      this.tasks = [
        { name: 'A', s: 1, f: 3 },
        { name: 'B', s: 2, f: 5 },
        { name: 'C', s: 5, f: 6 },
        { name: 'D', s: 4, f: 7 }
      ];
      this.huffman_input = 'A:15, B:7, C:6, D:6, E:5, F:2';
      this.decode_bits = '01101001110';
    }

    /**
     * Assigns intervals to machines greedily using the chosen sort key ('start' or 'finish').
     *
     * Args:
     *     intervals (Array<object>): Task list with name, s, f.
     *     sort_by (string): 'start' for optimal s_i sorting or 'finish' for flawed f_i sorting.
     *
     * Returns:
     *     Array<Array<object>>: List of machines each holding assigned task intervals.
     */
    scheduleIntervals(intervals, sort_by) {
      const sorted = intervals.slice().sort((a, b) => sort_by === 'start' ? (a.s - b.s || a.f - b.f) : (a.f - b.f || a.s - b.s));
      const machines = [];
      for (let i = 0; i < sorted.length; i += 1) {
        const task = sorted[i];
        let assigned = false;
        for (let m = 0; m < machines.length; m += 1) {
          const last = machines[m][machines[m].length - 1];
          if (last.f <= task.s) {
            machines[m].push(task);
            assigned = true;
            break;
          }
        }
        if (!assigned) {
          machines.push([task]);
        }
      }
      return machines;
    }

    /**
     * Mounts the 3-mode Greedy Method lab inside the host container.
     *
     * Args:
     *     container_el (HTMLElement): Host DOM element.
     */
    mount(container_el) {
      let html = '<div class="card">';
      html += '<div class="lab-toolbar">' +
        '<button type="button" class="btn ' + (this.sub_tab === 'huffman' ? 'btn-primary' : 'btn-secondary') + '" data-st="huffman">Κωδικοποίηση Huffman</button>' +
        '<button type="button" class="btn ' + (this.sub_tab === 'schedule' ? 'btn-primary' : 'btn-secondary') + '" data-st="schedule">Task Scheduling (s_i vs f_i)</button>' +
        '<button type="button" class="btn ' + (this.sub_tab === 'knapsack' ? 'btn-primary' : 'btn-secondary') + '" data-st="knapsack">Σακίδιο (Κλασματικό vs 0-1)</button>' +
        '</div><div id="u06_stage"></div></div>';
      container_el.innerHTML = html;

      const stage = container_el.querySelector('#u06_stage');
      if (this.sub_tab === 'knapsack') {
        this.renderKnapsack(stage);
      } else if (this.sub_tab === 'schedule') {
        this.renderSchedule(stage);
      } else {
        this.renderHuffman(stage);
      }

      const btns = container_el.querySelectorAll('[data-st]');
      for (let i = 0; i < btns.length; i += 1) {
        btns[i].addEventListener('click', (evt) => {
          this.sub_tab = evt.currentTarget.getAttribute('data-st');
          this.mount(container_el);
        });
      }
    }

    /**
     * Renders the Fractional vs 0-1 Knapsack density comparison panel.
     *
     * Args:
     *     panel_el (HTMLElement): Target panel element.
     */
    renderKnapsack(panel_el) {
      const sorted = this.knapsack_items.slice().sort((a, b) => (b.b / b.w) - (a.b / a.w));
      let rem_frac = this.knapsack_w;
      let val_frac = 0;
      const frac_picks = [];
      for (let i = 0; i < sorted.length; i += 1) {
        const it = sorted[i];
        const take = Math.min(it.w, rem_frac);
        if (take > 0) {
          rem_frac -= take;
          val_frac += (take / it.w) * it.b;
          frac_picks.push(it.name + ': ' + take + '/' + it.w);
        }
      }

      let rem_01 = this.knapsack_w;
      let val_greedy_01 = 0;
      const g01_picks = [];
      for (let i = 0; i < sorted.length; i += 1) {
        if (sorted[i].w <= rem_01) {
          rem_01 -= sorted[i].w;
          val_greedy_01 += sorted[i].b;
          g01_picks.push(sorted[i].name);
        }
      }

      let best_01 = 0;
      let best_set = [];
      const n = this.knapsack_items.length;
      for (let mask = 0; mask < (1 << n); mask += 1) {
        let sw = 0;
        let sb = 0;
        const names = [];
        for (let i = 0; i < n; i += 1) {
          if (mask & (1 << i)) { sw += this.knapsack_items[i].w; sb += this.knapsack_items[i].b; names.push(this.knapsack_items[i].name); }
        }
        if (sw <= this.knapsack_w && sb > best_01) { best_01 = sb; best_set = names; }
      }

      let html = '<h3>Σύγκριση Κλασματικού vs 0-1 Σακιδίου (W = ' + this.knapsack_w + ')</h3>';
      html += '<div class="table-wrap"><table class="data-table"><thead><tr><th>Αντικείμενο</th><th>Βάρος w_i</th><th>Όφελος b_i</th><th>Πυκνότητα v_i = b_i / w_i</th></tr></thead><tbody>';
      for (let i = 0; i < sorted.length; i += 1) {
        html += '<tr><td><code>' + sorted[i].name + '</code></td><td>' + sorted[i].w + '</td><td>' + sorted[i].b + '</td><td><strong>' + (sorted[i].b / sorted[i].w).toFixed(2) + '</strong></td></tr>';
      }
      html += '</tbody></table></div>';

      html += '<div class="grid-3" style="margin-top:14px;">' +
        '<div class="accent-callout"><strong>Κλασματικό (Άπληστη):</strong><br>Επιλογή: ' + frac_picks.join(', ') + '<br>Όφελος: <code>' + val_frac.toFixed(1) + '</code> (Βέλτιστο)</div>' +
        '<div class="scope-callout"><strong>0-1 (Άπληστη κατά v_i):</strong><br>Επιλογή: {' + g01_picks.join(', ') + '}<br>Όφελος: <code>' + val_greedy_01 + '</code> (Αποτυχία!)</div>' +
        '<div class="card-deep"><strong>0-1 Πραγματικό Βέλτιστο:</strong><br>Επιλογή: {' + best_set.join(', ') + '}<br>Όφελος: <code>' + best_01 + '</code></div>' +
        '</div>';
      panel_el.innerHTML = html;
    }

    /**
     * Renders side-by-side Gantt charts for Task Scheduling sorted by s_i vs f_i.
     *
     * Args:
     *     panel_el (HTMLElement): Target panel element.
     */
    renderSchedule(panel_el) {
      const m_start = this.scheduleIntervals(this.tasks, 'start');
      const m_finish = this.scheduleIntervals(this.tasks, 'finish');
      const max_t = 8;

      const drawGantt = (machines, title, note) => {
        const h = machines.length * 42 + 44;
        let svg = '<div class="card-deep"><strong>' + title + '</strong><p class="muted-text" style="margin:4px 0 8px 0;">' + note + '</p>';
        svg += '<svg class="svg-stage" viewBox="0 0 560 ' + h + '">';
        for (let t = 0; t <= max_t; t += 1) {
          const x = 60 + (t / max_t) * 470;
          svg += '<line x1="' + x + '" y1="12" x2="' + x + '" y2="' + (h - 22) + '" stroke="var(--border-subtle)" stroke-width="1" />';
          svg += '<text x="' + x + '" y="' + (h - 6) + '" text-anchor="middle" fill="var(--ink-subtle)" font-family="var(--font-mono)" font-size="11">' + t + '</text>';
        }
        for (let m = 0; m < machines.length; m += 1) {
          const y = 20 + m * 42;
          svg += '<text x="12" y="' + (y + 18) + '" fill="var(--ink-muted)" font-family="var(--font-mono)" font-size="12">M' + (m + 1) + '</text>';
          for (let k = 0; k < machines[m].length; k += 1) {
            const t = machines[m][k];
            const x1 = 60 + (t.s / max_t) * 470;
            const w = ((t.f - t.s) / max_t) * 470;
            svg += '<rect x="' + x1 + '" y="' + y + '" width="' + w + '" height="26" rx="5" fill="var(--accent-soft)" stroke="var(--accent-primary)" stroke-width="1.5" />';
            svg += '<text x="' + (x1 + w / 2) + '" y="' + (y + 17) + '" text-anchor="middle" fill="var(--ink-bright)" font-family="var(--font-mono)" font-size="11" font-weight="700">' + t.name + ' [' + t.s + ',' + t.f + ']</text>';
          }
        }
        svg += '</svg></div>';
        return svg;
      };

      panel_el.innerHTML =
        '<h3>Αντιπαράδειγμα Αποτυχίας Ταξινόμησης κατά f<sub>i</sub> (Άσκηση 3)</h3>' +
        '<div class="grid-2">' +
          drawGantt(m_start, 'ΣΩΣΤΟ: Κατά αύξουσα ώρα έναρξης s_i (' + m_start.length + ' μηχανές)', 'A=[1,3], B=[2,5], D=[4,7], C=[5,6] -> Βέλτιστο 2 μηχανές.') +
          drawGantt(m_finish, 'ΛΑΘΟΣ: Κατά αύξουσα ώρα λήξης f_i (' + m_finish.length + ' μηχανές)', 'C=[5,6] μπαίνει πριν τη D=[4,7], αναγκάζοντας 3η μηχανή!') +
        '</div>';
    }

    /**
     * Renders the interactive Huffman tree builder, code table, and bitstring decoder.
     *
     * Args:
     *     panel_el (HTMLElement): Target panel element.
     */
    renderHuffman(panel_el) {
      const pairs = this.huffman_input.split(',').map((s) => s.trim()).filter(Boolean);
      const leaves = [];
      let order_id = 0;
      for (let i = 0; i < pairs.length; i += 1) {
        const parts = pairs[i].split(':');
        if (parts.length === 2) {
          const sym = parts[0].trim();
          const freq = Number(parts[1].trim());
          if (sym && freq > 0) {
            leaves.push({ sym: sym, freq: freq, is_leaf: true, order: order_id += 1, left: null, right: null });
          }
        }
      }
      if (leaves.length < 2) {
        panel_el.innerHTML = '<p>Εισάγετε τουλάχιστον 2 σύμβολα (π.χ. A:15, B:7).</p>';
        return;
      }

      const pq = leaves.slice();
      const merges = [];
      let internal_idx = 1;
      while (pq.length > 1) {
        pq.sort((a, b) => (a.freq - b.freq) || (a.order - b.order));
        const n1 = pq.shift();
        const n2 = pq.shift();
        const combined = {
          sym: 'N' + internal_idx,
          freq: n1.freq + n2.freq,
          is_leaf: false,
          order: order_id += 1,
          left: n1,
          right: n2
        };
        internal_idx += 1;
        merges.push(n1.sym + '(' + n1.freq + ') + ' + n2.sym + '(' + n2.freq + ') -> ' + combined.sym + '(' + combined.freq + ')');
        pq.push(combined);
      }
      const root = pq[0];

      const codes = {};
      let total_bits = 0;
      const assignCodes = (node, prefix) => {
        if (node.is_leaf) {
          codes[node.sym] = prefix || '0';
          total_bits += node.freq * codes[node.sym].length;
          return;
        }
        assignCodes(node.left, prefix + '0');
        assignCodes(node.right, prefix + '1');
      };
      assignCodes(root, '');

      // Computes x/y coordinates for SVG drawing of the Huffman tree.
      let leaf_x = 0;
      const pos_map = new Map();
      let max_d = 0;
      const layout = (node, depth) => {
        if (depth > max_d) { max_d = depth; }
        if (node.is_leaf) {
          const x = 44 + leaf_x * 84;
          leaf_x += 1;
          pos_map.set(node, { x: x, y: 34 + depth * 56 });
          return x;
        }
        const lx = layout(node.left, depth + 1);
        const rx = layout(node.right, depth + 1);
        const mx = (lx + rx) / 2;
        pos_map.set(node, { x: mx, y: 34 + depth * 56 });
        return mx;
      };
      layout(root, 0);

      const svg_w = Math.max(540, leaf_x * 84 + 30);
      const svg_h = (max_d + 1) * 56 + 34;
      let edges_svg = '';
      let nodes_svg = '';
      const drawNode = (node) => {
        const p = pos_map.get(node);
        if (!node.is_leaf) {
          const lp = pos_map.get(node.left);
          const rp = pos_map.get(node.right);
          edges_svg += '<line x1="' + p.x + '" y1="' + p.y + '" x2="' + lp.x + '" y2="' + lp.y + '" stroke="var(--border-strong)" stroke-width="2" />';
          edges_svg += '<text x="' + ((p.x + lp.x) / 2 - 10) + '" y="' + ((p.y + lp.y) / 2) + '" fill="var(--accent-primary)" font-family="var(--font-mono)" font-size="11">0</text>';
          edges_svg += '<line x1="' + p.x + '" y1="' + p.y + '" x2="' + rp.x + '" y2="' + rp.y + '" stroke="var(--border-strong)" stroke-width="2" />';
          edges_svg += '<text x="' + ((p.x + rp.x) / 2 + 6) + '" y="' + ((p.y + rp.y) / 2) + '" fill="var(--accent-primary)" font-family="var(--font-mono)" font-size="11">1</text>';
          drawNode(node.left);
          drawNode(node.right);
        }
        nodes_svg += '<circle cx="' + p.x + '" cy="' + p.y + '" r="17" fill="' + (node.is_leaf ? 'var(--accent-soft)' : 'var(--bg-surface-elevated)') + '" stroke="' + (node.is_leaf ? 'var(--accent-primary)' : 'var(--ink-muted)') + '" stroke-width="2" />';
        nodes_svg += '<text x="' + p.x + '" y="' + (p.y + 4) + '" text-anchor="middle" fill="var(--ink-bright)" font-family="var(--font-mono)" font-size="11" font-weight="700">' + (node.is_leaf ? node.sym + ':' + node.freq : node.freq) + '</text>';
      };
      drawNode(root);

      // Decodes the user bitstring by walking from root to leaves.
      let decoded = '';
      let walker = root;
      for (let i = 0; i < this.decode_bits.length; i += 1) {
        const bit = this.decode_bits[i];
        if (bit === '0' && walker.left) { walker = walker.left; }
        else if (bit === '1' && walker.right) { walker = walker.right; }
        if (walker.is_leaf) {
          decoded += walker.sym;
          walker = root;
        }
      }

      let html = '<h3>Κατασκευαστής Κώδικα Huffman &amp; Αποκωδικοποιητής</h3>';
      html += '<div class="lab-toolbar">' +
        '<label class="lab-field">Συχνότητες: <input type="text" id="u06_hf_in" class="input-control" value="' + escapeHtml(this.huffman_input) + '" style="width:260px;"></label>' +
        '<button type="button" class="btn btn-primary" id="u06_hf_build">Κατασκευή Δέντρου</button>' +
        '<label class="lab-field">Bits: <input type="text" id="u06_bits_in" class="input-control" value="' + escapeHtml(this.decode_bits) + '" style="width:140px;"></label>' +
        '<span class="meta-pill accent">Αποκωδικοποίηση: ' + escapeHtml(decoded || '—') + '</span>' +
        '</div>';

      html += '<svg class="svg-stage" viewBox="0 0 ' + svg_w + ' ' + svg_h + '">' + edges_svg + nodes_svg + '</svg>';

      html += '<div class="grid-2" style="margin-top:12px;">' +
        '<div class="table-wrap"><table class="data-table"><thead><tr><th>Σύμβολο</th><th>f(c)</th><th>Κωδικός</th><th>f(c)&middot;d(c)</th></tr></thead><tbody>' +
        leaves.map((l) => '<tr><td><code>' + escapeHtml(l.sym) + '</code></td><td>' + l.freq + '</td><td><code>' + codes[l.sym] + '</code></td><td>' + (l.freq * codes[l.sym].length) + '</td></tr>').join('') +
        '<tr><td colspan="3"><strong>Συνολικό μήκος B(T)</strong></td><td><strong><code>' + total_bits + ' bits</code></strong></td></tr>' +
        '</tbody></table></div>' +
        '<div class="trace-log">' +
          merges.map((m, i) => '<div class="trace-entry">Βήμα ' + (i + 1) + ': ' + escapeHtml(m) + '</div>').join('') +
        '</div></div>';

      panel_el.innerHTML = html;

      panel_el.querySelector('#u06_hf_build').addEventListener('click', () => {
        this.huffman_input = panel_el.querySelector('#u06_hf_in').value;
        this.decode_bits = panel_el.querySelector('#u06_bits_in').value;
        this.renderHuffman(panel_el);
      });
    }
  }

  /**
   * Renders the Master Theorem Analyzer and 2D MaximaSet Visualizer for Unit 07.
   *
   * Evaluates Master Theorem Cases 1-3, regularity checks, gaps, and Pareto frontier sweeps.
   * Methods: mount(container_el), renderMasterPanel(panel_el), renderMaximaPanel(panel_el), computeMasterAnalysis().
   */
  class Unit07Lab {
    /**
     * Initializes Master Theorem parameters and Exercise 1 hotel coordinates.
     */
    constructor() {
      this.param_a = 3;
      this.param_b = 3;
      this.param_d = 1.5;
      this.param_k = 0;
      this.maxima_step = 3;
      this.points = [
        { name: 'H1', x: 2, y: 9 },
        { name: 'H2', x: 3, y: 5 },
        { name: 'H3', x: 5, y: 7 },
        { name: 'H4', x: 5, y: 4 },
        { name: 'H5', x: 8, y: 6 },
        { name: 'H6', x: 10, y: 3 }
      ];
    }

    /**
     * Evaluates the recurrence T(n) = aT(n/b) + n^d log^k n via the Master Theorem.
     *
     * Returns:
     *     object: Classification, critical exponent, regularity constant delta, and exam text.
     */
    computeMasterAnalysis() {
      const a = this.param_a;
      const b = this.param_b;
      const d = this.param_d;
      const k = this.param_k;
      const crit = Math.log(a) / Math.log(b);
      const eps = 1e-6;

      if (a < 1 || b <= 1) {
        return { status: 'Μη Εφαρμόσιμο', result: 'Απαιτούνται a >= 1 και b > 1.', detail: 'Παράμετροι εκτός προϋποθέσεων Master Theorem.' };
      }
      if (Math.abs(d - crit) <= eps) {
        if (k < 0) {
          return {
            status: 'Μη Εφαρμόσιμο (Χάσμα Περ. 1–2)',
            result: 'Λύση με Δέντρο Αναδρομής (π.χ. Θ(n log log n) για k=-1)',
            detail: 'Ο εκθέτης k = ' + k + ' < 0 δεν καλύπτεται από την Περίπτωση 2 (απαιτείται k >= 0), ούτε η διαφορά είναι πολυωνυμική n^ε.'
          };
        }
        return {
          status: 'Περίπτωση 2 (Ισορροπία Επιπέδων)',
          result: 'Θ(n^' + crit.toFixed(3).replace(/\.000$/, '') + ' log^' + (k + 1) + ' n)',
          detail: 'd = log_b(a) = ' + crit.toFixed(3) + ' και k = ' + k + ' >= 0, άρα προστίθεται παράγοντας log n.'
        };
      }
      if (d < crit - eps) {
        return {
          status: 'Περίπτωση 1 (Κυριαρχούν τα Φύλλα)',
          result: 'Θ(n^' + crit.toFixed(3).replace(/\.000$/, '') + ')',
          detail: 'f(n) = O(n^(log_b a - ε)) με ε = ' + (crit - d).toFixed(2) + ' > 0.'
        };
      }
      const delta = a / Math.pow(b, d);
      if (delta < 1) {
        return {
          status: 'Περίπτωση 3 (Κυριαρχεί η Ρίζα)',
          result: 'Θ(n^' + d + (k > 0 ? ' log^' + k + ' n' : '') + ')',
          detail: 'd > log_b(a) (' + d + ' > ' + crit.toFixed(3) + ') ΚΑΙ έλεγχος κανονικότητας: δ = a / b^d = ' + delta.toFixed(3) + ' < 1.'
        };
      }
      return {
        status: 'Αποτυχία Κανονικότητας',
        result: 'Μη Εφαρμόσιμο',
        detail: 'δ = a / b^d = ' + delta.toFixed(3) + ' >= 1.'
      };
    }

    /**
     * Mounts the Master Theorem analyzer and 2D MaximaSet visualizer inside the host container.
     *
     * Args:
     *     container_el (HTMLElement): Host DOM element.
     */
    mount(container_el) {
      container_el.innerHTML =
        '<div class="card" id="u07_master_box"></div>' +
        '<div class="card" id="u07_maxima_box"></div>';
      this.renderMasterPanel(container_el.querySelector('#u07_master_box'));
      this.renderMaximaPanel(container_el.querySelector('#u07_maxima_box'));
    }

    /**
     * Renders the interactive Master Theorem analyzer panel.
     *
     * Args:
     *     panel_el (HTMLElement): Target panel element.
     */
    renderMasterPanel(panel_el) {
      const res = this.computeMasterAnalysis();
      let html = '<h3>Αναλυτής Μάστερ Θεωρήματος: T(n) = a T(n/b) + n<sup>d</sup> log<sup>k</sup> n</h3>';
      html += '<div class="lab-toolbar">' +
        '<label class="lab-field">a: <input type="number" id="u07_a" class="input-control" step="1" min="1" value="' + this.param_a + '" style="width:70px;"></label>' +
        '<label class="lab-field">b: <input type="number" id="u07_b" class="input-control" step="1" min="2" value="' + this.param_b + '" style="width:70px;"></label>' +
        '<label class="lab-field">d: <input type="number" id="u07_d" class="input-control" step="0.5" min="0" value="' + this.param_d + '" style="width:76px;"></label>' +
        '<label class="lab-field">k: <input type="number" id="u07_k" class="input-control" step="1" value="' + this.param_k + '" style="width:70px;"></label>' +
        '<button type="button" class="btn btn-primary" id="u07_eval">Ανάλυση</button>' +
        '</div>';

      html += '<div class="lab-toolbar">' +
        '<button type="button" class="btn btn-ghost" data-pre="1,2,0,0">Binary Search</button>' +
        '<button type="button" class="btn btn-ghost" data-pre="2,2,1,0">Merge-Sort</button>' +
        '<button type="button" class="btn btn-ghost" data-pre="3,2,1,0">Karatsuba</button>' +
        '<button type="button" class="btn btn-ghost" data-pre="3,3,1.5,0">Άσκ. 2α (Περ. 3)</button>' +
        '<button type="button" class="btn btn-ghost" data-pre="2,2,1,-1">Χάσμα n/log n</button>' +
        '</div>';

      html += '<div class="accent-callout">' +
        '<div><strong>Κατάταξη:</strong> ' + escapeHtml(res.status) + '</div>' +
        '<div><strong>Αποτέλεσμα:</strong> <code>' + escapeHtml(res.result) + '</code></div>' +
        '<div><strong>Αιτιολόγηση:</strong> ' + escapeHtml(res.detail) + '</div>' +
        '</div>';
      panel_el.innerHTML = html;

      panel_el.querySelector('#u07_eval').addEventListener('click', () => {
        this.param_a = Number(panel_el.querySelector('#u07_a').value);
        this.param_b = Number(panel_el.querySelector('#u07_b').value);
        this.param_d = Number(panel_el.querySelector('#u07_d').value);
        this.param_k = Number(panel_el.querySelector('#u07_k').value);
        this.renderMasterPanel(panel_el);
      });
      const pre_btns = panel_el.querySelectorAll('[data-pre]');
      for (let i = 0; i < pre_btns.length; i += 1) {
        pre_btns[i].addEventListener('click', (evt) => {
          const parts = evt.currentTarget.getAttribute('data-pre').split(',').map(Number);
          this.param_a = parts[0];
          this.param_b = parts[1];
          this.param_d = parts[2];
          this.param_k = parts[3];
          this.renderMasterPanel(panel_el);
        });
      }
    }

    /**
     * Renders the 2D Pareto / MaximaSet geometric plane and step breakdown.
     *
     * Args:
     *     panel_el (HTMLElement): Target panel element.
     */
    renderMaximaPanel(panel_el) {
      const sorted = this.points.slice().sort((p, q) => (p.x - q.x) || (p.y - q.y));
      const mid = Math.floor(sorted.length / 2);
      const left_half = sorted.slice(0, mid);
      const right_half = sorted.slice(mid);

      const computeMaxima = (pts) => {
        const res = [];
        let max_y = -Infinity;
        for (let i = pts.length - 1; i >= 0; i -= 1) {
          if (pts[i].y > max_y) {
            res.unshift(pts[i]);
            max_y = pts[i].y;
          }
        }
        return res;
      };

      const m2 = computeMaxima(right_half);
      const q_point = m2[0];
      const final_maxima = computeMaxima(sorted);
      const final_names = final_maxima.map((p) => p.name);

      const width = 640;
      const height = 270;
      const toX = (x) => 48 + (x / 11) * 560;
      const toY = (y) => height - 34 - (y / 11) * 215;

      let svg = '<svg class="svg-stage" viewBox="0 0 ' + width + ' ' + height + '">';
      svg += '<line x1="48" y1="' + (height - 34) + '" x2="615" y2="' + (height - 34) + '" stroke="var(--border-strong)" stroke-width="1.5" />';
      svg += '<line x1="48" y1="20" x2="48" y2="' + (height - 34) + '" stroke="var(--border-strong)" stroke-width="1.5" />';

      if (this.maxima_step >= 2 && q_point) {
        const split_x = (toX(left_half[left_half.length - 1].x) + toX(right_half[0].x)) / 2;
        svg += '<line x1="' + split_x + '" y1="18" x2="' + split_x + '" y2="' + (height - 34) + '" stroke="var(--ink-muted)" stroke-dasharray="5,5" stroke-width="1.5" />';
      }
      if (this.maxima_step >= 3 && q_point) {
        // Draws dominance box x <= q.x and y <= q.y where left M1 points are pruned.
        svg += '<rect x="48" y="' + toY(q_point.y) + '" width="' + (toX(q_point.x) - 48) + '" height="' + ((height - 34) - toY(q_point.y)) + '" fill="var(--surface-putty-soft)" stroke="var(--border-strong)" stroke-dasharray="4,4" />';
        const poly_pts = final_maxima.map((p) => toX(p.x) + ',' + toY(p.y)).join(' ');
        svg += '<polyline points="' + poly_pts + '" fill="none" stroke="var(--accent-primary)" stroke-width="2" />';
      }

      for (let i = 0; i < sorted.length; i += 1) {
        const p = sorted[i];
        const px = toX(p.x);
        const py = toY(p.y);
        const survives = final_names.indexOf(p.name) !== -1;
        const is_q = q_point && p.name === q_point.name;
        const fill_c = (this.maxima_step >= 3 && !survives) ? 'var(--bg-surface-deep)' : 'var(--accent-primary)';
        const stroke_c = (this.maxima_step >= 3 && !survives) ? 'var(--ink-subtle)' : 'var(--accent-primary)';
        svg += '<circle cx="' + px + '" cy="' + py + '" r="' + (is_q ? 8 : 6) + '" fill="' + fill_c + '" stroke="' + stroke_c + '" stroke-width="2" />';
        svg += '<text x="' + (px + 8) + '" y="' + (py - 6) + '" fill="var(--ink-bright)" font-family="var(--font-mono)" font-size="11">' + p.name + '(' + p.x + ',' + p.y + ')' + (is_q && this.maxima_step >= 2 ? ' [q]' : '') + '</text>';
      }
      svg += '</svg>';

      let html = '<h3>Γεωμετρικός Οπτικοποιητής MaximaSet (Επίπεδο Pareto)</h3>';
      html += '<div class="lab-toolbar">' +
        '<button type="button" class="btn ' + (this.maxima_step === 1 ? 'btn-primary' : 'btn-secondary') + '" data-ms="1">1. Ταξινόμηση (x, y)</button>' +
        '<button type="button" class="btn ' + (this.maxima_step === 2 ? 'btn-primary' : 'btn-secondary') + '" data-ms="2">2. Διάσπαση L / G &amp; q in M2</button>' +
        '<button type="button" class="btn ' + (this.maxima_step === 3 ? 'btn-primary' : 'btn-secondary') + '" data-ms="3">3. Φιλτράρισμα M1 &amp; Pareto</button>' +
        '</div>';
      html += svg;
      html += '<div class="accent-callout">' +
        '<strong>Ταξινομημένο:</strong> ' + sorted.map((p) => p.name + '(' + p.x + ',' + p.y + ')').join(', ') + '<br>' +
        '<strong>Τελικό Σύνολο Μεγίστων:</strong> <code>{' + final_maxima.map((p) => p.name + '(' + p.x + ',' + p.y + ')').join(', ') + '}</code>' +
        '</div>';

      panel_el.innerHTML = html;

      const btns = panel_el.querySelectorAll('[data-ms]');
      for (let i = 0; i < btns.length; i += 1) {
        btns[i].addEventListener('click', (evt) => {
          this.maxima_step = Number(evt.currentTarget.getAttribute('data-ms'));
          this.renderMaximaPanel(panel_el);
        });
      }
    }
  }

  global_scope.MidtermApp = global_scope.MidtermApp || {};
  global_scope.MidtermApp.labs = global_scope.MidtermApp.labs || {};
  global_scope.MidtermApp.labs['04'] = new Unit04Lab();
  global_scope.MidtermApp.labs['05'] = new Unit05Lab();
  global_scope.MidtermApp.labs['06'] = new Unit06Lab();
  global_scope.MidtermApp.labs['07'] = new Unit07Lab();
})(window);
