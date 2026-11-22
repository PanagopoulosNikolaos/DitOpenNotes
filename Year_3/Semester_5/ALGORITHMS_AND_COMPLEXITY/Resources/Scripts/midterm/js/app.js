(function (global_scope) {
  'use strict';

  /**
   * Formats lightweight inline markup such as backticked identifiers and arrows safely.
   *
   * Args:
   *     raw_text (string): Input text that may contain backticks.
   *
   * Returns:
   *     string: Formatted HTML string with code tags and escaped HTML entities.
   */
  function formatRichText(raw_text) {
    const escaped = String(raw_text)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;');
    return escaped.replace(/`([^`]+)`/g, '<code>$1</code>');
  }

  /**
   * Manages persistence of student mastery and drill progress in localStorage.
   *
   * Encapsulates safe read/write storage operations with an in-memory fallback.
   * Methods: loadState(), saveState(), toggleUnitMastery(unit_id), isUnitMastered(unit_id), recordDrillAnswer(q_id, opt_idx).
   */
  class StorageManager {
    /**
     * Initializes storage key and loads persisted student progress.
     */
    constructor() {
      this.storage_key = 'dit_algo504_midterm_v1';
      this.state = this.loadState();
    }

    /**
     * Loads persisted state from localStorage or returns clean defaults.
     *
     * Returns:
     *     object: State object containing mastered_units and drill_answers.
     */
    loadState() {
      const defaults = {
        mastered_units: [],
        drill_answers: {},
        completed_games: [],
        tf_answers: {},
        last_nav: 'unit:00',
        last_tab: 'overview'
      };
      try {
        const raw = global_scope.localStorage.getItem(this.storage_key);
        if (!raw) {
          return defaults;
        }
        const parsed = JSON.parse(raw);
        return {
          mastered_units: Array.isArray(parsed.mastered_units) ? parsed.mastered_units : [],
          drill_answers: parsed.drill_answers && typeof parsed.drill_answers === 'object' ? parsed.drill_answers : {},
          completed_games: Array.isArray(parsed.completed_games) ? parsed.completed_games : [],
          tf_answers: parsed.tf_answers && typeof parsed.tf_answers === 'object' ? parsed.tf_answers : {},
          last_nav: typeof parsed.last_nav === 'string' ? parsed.last_nav : 'unit:00',
          last_tab: typeof parsed.last_tab === 'string' ? parsed.last_tab : 'overview'
        };
      } catch (_err) {
        return defaults;
      }
    }

    /**
     * Persists the current state dictionary to localStorage safely.
     */
    saveState() {
      try {
        global_scope.localStorage.setItem(this.storage_key, JSON.stringify(this.state));
      } catch (_err) {
        // Ignores storage quota or private-mode restrictions gracefully.
      }
    }

    /**
     * Checks whether a given unit ID has been marked mastered.
     *
     * Args:
     *     unit_id (string): Unit identifier ('00' through '07').
     *
     * Returns:
     *     boolean: True if the unit is marked mastered.
     */
    isUnitMastered(unit_id) {
      return this.state.mastered_units.indexOf(unit_id) !== -1;
    }

    /**
     * Toggles mastery status for the requested unit and saves state.
     *
     * Args:
     *     unit_id (string): Unit identifier ('00' through '07').
     *
     * Returns:
     *     boolean: Resulting mastery state after toggle.
     */
    toggleUnitMastery(unit_id) {
      const idx = this.state.mastered_units.indexOf(unit_id);
      if (idx === -1) {
        this.state.mastered_units.push(unit_id);
      } else {
        this.state.mastered_units.splice(idx, 1);
      }
      this.saveState();
      return idx === -1;
    }

    /**
     * Records a student answer for a unit practice drill question.
     *
     * Args:
     *     q_id (string): Unique question identifier.
     *     opt_idx (number): Selected option index.
     */
    recordDrillAnswer(q_id, opt_idx) {
      this.state.drill_answers[q_id] = opt_idx;
      this.saveState();
    }

    /**
     * Marks an interactive Drop-In or Builder challenge ID as completed.
     *
     * Args:
     *     challenge_id (string): Unique puzzle or builder game identifier.
     */
    markGameCompleted(challenge_id) {
      if (this.state.completed_games.indexOf(challenge_id) === -1) {
        this.state.completed_games.push(challenge_id);
        this.saveState();
      }
    }

    /**
     * Records a student answer for a True/False recitation statement.
     *
     * Args:
     *     tf_key (string): Unique True/False statement identifier.
     *     choice_bool (boolean): Selected True or False boolean value.
     */
    recordTfAnswer(tf_key, choice_bool) {
      this.state.tf_answers[tf_key] = choice_bool;
      this.saveState();
    }
  }

  /**
   * Manages interactive Mock Midterm Exam sessions and per-unit diagnostic scoring.
   *
   * Selects shuffled question subsets, records responses, and computes unit weakness summaries.
   * Methods: startSession(question_count, filter_unit), answerQuestion(q_id, opt_idx), computeReport().
   */
  class QuizEngine {
    /**
     * Initializes the quiz engine with the full MidTerm question bank.
     *
     * Args:
     *     question_bank (Array<object>): Array of MidTerm quiz questions.
     */
    constructor(question_bank) {
      this.question_bank = question_bank || [];
      this.active_questions = [];
      this.user_answers = {};
      this.exam_submitted = false;
      this.selected_count = 10;
      this.selected_unit = 'all';
    }

    /**
     * Starts a fresh Mock Exam session with shuffled questions matching filters.
     *
     * Args:
     *     question_count (number): Maximum number of questions to include.
     *     filter_unit (string): Specific unit ID ('00'..'07') or 'all'.
     */
    startSession(question_count, filter_unit) {
      this.selected_count = question_count;
      this.selected_unit = filter_unit;
      let pool = this.question_bank.slice();
      if (filter_unit && filter_unit !== 'all') {
        pool = pool.filter((q) => q.unit_id === filter_unit);
      }
      // Performs Fisher-Yates shuffle so exam sessions vary on each run.
      for (let i = pool.length - 1; i > 0; i -= 1) {
        const j = Math.floor(Math.random() * (i + 1));
        const tmp = pool[i];
        pool[i] = pool[j];
        pool[j] = tmp;
      }
      this.active_questions = pool.slice(0, Math.min(question_count, pool.length));
      this.user_answers = {};
      this.exam_submitted = false;
    }

    /**
     * Records a selected option for an active exam question.
     *
     * Args:
     *     q_id (string): Question identifier.
     *     opt_idx (number): Zero-based index of chosen option.
     */
    answerQuestion(q_id, opt_idx) {
      this.user_answers[q_id] = opt_idx;
    }

    /**
     * Computes overall and per-unit accuracy metrics for the active exam session.
     *
     * Returns:
     *     object: Summary containing total, answered, correct, and per_unit map.
     */
    computeReport() {
      let correct = 0;
      let answered = 0;
      const per_unit = {};
      for (let i = 0; i < this.active_questions.length; i += 1) {
        const q = this.active_questions[i];
        if (!per_unit[q.unit_id]) {
          per_unit[q.unit_id] = { total: 0, correct: 0 };
        }
        per_unit[q.unit_id].total += 1;
        const chosen = this.user_answers[q.id];
        if (typeof chosen === 'number') {
          answered += 1;
          if (chosen === q.correct_index) {
            correct += 1;
            per_unit[q.unit_id].correct += 1;
          }
        }
      }
      return {
        total: this.active_questions.length,
        answered: answered,
        correct: correct,
        per_unit: per_unit
      };
    }
  }

  /**
   * Coordinates navigation, rendering, progressive disclosure, labs, and exam views.
   *
   * Connects StorageManager, QuizEngine, IconLibrary, curriculum data, and interactive labs.
   * Methods: init(), bindShellEvents(), navigate(nav_target, tab_name), render(), renderUnitView(unit_id), renderExamView(), renderReferenceView().
   */
  class AppController {
    /**
     * Initializes controller dependencies, reference complexity catalog, and initial route.
     */
    constructor() {
      this.icons = global_scope.MidtermApp.icons;
      this.units_data = global_scope.MidtermApp.units_data || {};
      this.quiz_bank = global_scope.MidtermApp.quiz_bank || [];
      this.labs = global_scope.MidtermApp.labs || {};
      this.code_examples = global_scope.MidtermApp.code_examples || {};
      this.dropin_puzzles = global_scope.MidtermApp.dropin_puzzles || {};
      this.true_false_drills = global_scope.MidtermApp.true_false_drills || {};
      this.dropin_engine = global_scope.MidtermApp.dropin_engine;
      this.builder_games = global_scope.MidtermApp.builder_games || {};
      this.storage = new StorageManager();
      this.quiz_engine = new QuizEngine(this.quiz_bank);
      this.quiz_engine.startSession(10, 'all');

      let puzzle_total = Object.keys(this.builder_games).length;
      const drop_keys = Object.keys(this.dropin_puzzles);
      for (let i = 0; i < drop_keys.length; i += 1) {
        puzzle_total += this.dropin_puzzles[drop_keys[i]].length;
      }
      this.total_challenges = puzzle_total;

      this.current_nav = this.storage.state.last_nav || 'unit:00';
      this.current_tab = this.storage.state.last_tab || 'overview';
      this.ref_filter_unit = 'all';
      this.ref_search_query = '';

      this.complexity_rows = [
        { unit: '01', name: '`arrayMax`', worst: 'Θ(n) (7n-2)', best_expected: 'Θ(n) καλύτερη (5n)', space: 'O(1)', note: 'Επαναληπτικός· προτιμάται του recursiveMax' },
        { unit: '01', name: '`MaxsubSlow` / `Faster` / `Fastest`', worst: 'O(n^3) / O(n^2) / O(n)', best_expected: 'Θ(n^3) / Θ(n^2) / Θ(n)', space: 'O(1) / O(n) / O(n or 1)', note: 'M_t = max{0, M_{t-1} + A[t]}' },
        { unit: '01', name: 'Επεκτάσιμος πίνακας (+c)', worst: 'O(n) resize, O(n^2) σύνολο', best_expected: 'O(n) επιμερισμένη', space: 'O(n)', note: 'k = n/c αντικαταστάσεις' },
        { unit: '01', name: 'Επεκτάσιμος πίνακας (x2)', worst: 'O(n) resize, 3n-1 σύνολο', best_expected: 'O(1) επιμερισμένη', space: 'O(n)', note: '3 cyber-δολάρια ανά add' },
        { unit: '02', name: '`Selection-Sort` (μη ταξινομημένη PQ)', worst: 'Θ(n^2)', best_expected: 'Θ(n^2) καλύτερη', space: 'O(1) επί-τόπου', note: 'insert O(1), removeMin O(n)' },
        { unit: '02', name: '`Insertion-Sort` (ταξινομημένη PQ)', worst: 'O(n^2)', best_expected: 'Ω(n) καλύτερη', space: 'O(1) επί-τόπου, σταθερός', note: 'Ιδανικός για n < 1K ή σχεδόν ταξινομημένα' },
        { unit: '02', name: 'Δυαδικός Σωρός (`insert`, `removeMin`)', worst: 'O(log n)', best_expected: 'min() O(1) χειρότερη', space: 'O(n) (1-indexed)', note: 'Παιδιά 2i, 2i+1, γονέας floor(i/2)' },
        { unit: '02', name: '`Bottom-Up Heap` κατασκευή', worst: 'O(n)', best_expected: 'Θ(n)', space: 'O(1) επιπλέον', note: 'Διαδρομές δεξιά-μετά-αριστερά (<= 2/κόμβο)' },
        { unit: '02', name: '`Heap-Sort`', worst: 'O(n log n)', best_expected: 'Ω(n log n) διακριτά', space: 'O(1) επί-τόπου (max-heap)', note: 'Εγγυημένο O(n log n) & O(1) χώρος' },
        { unit: '03', name: 'Αταξινόμητη Λίστα (`Map ADT`)', worst: 'put O(1), get/remove O(n)', best_expected: '—', space: 'O(n)', note: 'Μόνο για πολύ μικρούς πίνακες' },
        { unit: '03', name: '`Hash Table` (`Chaining`, `Linear`, `Double`)', worst: 'O(n)', best_expected: 'O(1) αναμενόμενη (α<=1/2)', space: 'O(N+n) / O(N)', note: 'Linear Probing: 1/(1-α) ανιχνεύσεις, DEFUNCT' },
        { unit: '03', name: '`Cuckoo Hashing`', worst: 'get/remove O(1), put O(n)', best_expected: 'put O(1) επιμερισμένη', space: 'O(N) με N >= 2n', note: 'Κλειδί μόνο σε T1[h1(k)] ή T2[h2(k)]' },
        { unit: '04', name: '`Union-Find` (λίστα, μικρό στο μεγάλο)', worst: 'find O(1), σύνολο O(n log n + m)', best_expected: 'union O(log n) επιμερισμένη', space: 'O(n)', note: '<= floor(log_2 n) μετακινήσεις/στοιχείο' },
        { unit: '04', name: '`Union-Find` (δέντρα, ένωση κατά μέγεθος)', worst: 'find O(log n), union O(1)', best_expected: 'O((n+m) log n) σύνολο', space: 'O(n)', note: 'Ύψος h <= floor(log_2 n)' },
        { unit: '04', name: '`Union-Find` (μέγεθος + συμπίεση διαδρομής)', worst: 'O((n+m) α(n)) σύνολο', best_expected: 'O(α(n)) επιμερισμένη', space: 'O(n)', note: 'α(n) <= 4 πρακτικά (7.3.1 εκτός ύλης)' },
        { unit: '05', name: '`Merge-Sort`', worst: 'O(n log n)', best_expected: 'Θ(n log n), σταθερός', space: 'O(n)', note: 'Σειριακή προσπέλαση, ιδανικός για δίσκο (>1M)' },
        { unit: '05', name: '`Quick-Sort` (τυχαιοποιημένος / επί-τόπου)', worst: 'O(n^2)', best_expected: 'O(n log n) αναμενόμενη', space: 'O(log n) αναμεν. στοίβα', note: 'Τριμερής διαμερισμός, ταχύτερος στη RAM' },
        { unit: '05', name: 'Κάτω Όριο Ταξινόμησης Συγκρίσεων', worst: 'Ω(n log n)', best_expected: '—', space: '—', note: 'Δέντρο αποφάσεων με >= n! φύλλα' },
        { unit: '06', name: '`Fractional Knapsack`', worst: 'O(n log n)', best_expected: '—', space: 'O(n)', note: 'Φθίνουσα b_i / w_i· αποτυγχάνει στο 0-1' },
        { unit: '06', name: '`Task Scheduling` (ελάχιστες μηχανές)', worst: 'O(n log n)', best_expected: '—', space: 'O(n)', note: 'Ταξινόμηση κατά ώρα έναρξης s_i + min-heap' },
        { unit: '06', name: '`Huffman Coding`', worst: 'O(n + d log d)', best_expected: 'O(n) για σταθερό αλφάβητο', space: 'O(d)', note: 'n = |X|, d διακριτά σύμβολα, prefix-free' },
        { unit: '07', name: '`Binary Search`', worst: 'Θ(log n)', best_expected: 'O(1) καλύτερη', space: 'O(1) επαναληπτική', note: 'T(n) = T(n/2) + 1 (Περ. 2 Master Theorem)' },
        { unit: '07', name: '`Karatsuba` πολλαπλασιασμός', worst: 'Θ(n^{log_2 3}) ~ Θ(n^1.585)', best_expected: '—', space: 'O(n)', note: 'T(n) = 3T(n/2) + n (3 αντί 4 κλήσεις)' },
        { unit: '07', name: '`MaximaSet` (Pareto Frontier)', worst: 'Θ(n log n)', best_expected: '—', space: 'O(n)', note: 'Λεξικογραφική διάσπαση & φιλτράρισμα M1 από q in M2' }
      ];
    }

    /**
     * Initializes static UI icons, binds event listeners, and performs initial render.
     */
    init() {
      this.injectStaticIcons();
      this.bindShellEvents();
      this.updateMasteryHud();
      this.render();
    }

    /**
     * Injects monochromatic SVG icons into static shell placeholders.
     */
    injectStaticIcons() {
      const slot_map = [
        ['brand_icon_slot', 'compass', 20],
        ['nav_exam_icon', 'award', 18],
        ['nav_ref_icon', 'table', 18],
        ['mobile_menu_icon', 'menu', 20],
        ['shortcuts_btn_icon', 'keyboard', 18],
        ['close_modal_icon', 'x', 18]
      ];
      for (let i = 0; i < slot_map.length; i += 1) {
        const el = document.getElementById(slot_map[i][0]);
        if (el) {
          el.innerHTML = this.icons.getIcon(slot_map[i][1], slot_map[i][2]);
        }
      }
    }

    /**
     * Binds navigation rail, topbar buttons, modal controls, and keyboard shortcuts.
     */
    bindShellEvents() {
      const nav_items = document.querySelectorAll('[data-nav]');
      for (let i = 0; i < nav_items.length; i += 1) {
        nav_items[i].addEventListener('click', (evt) => {
          const target = evt.currentTarget.getAttribute('data-nav');
          this.navigate(target, 'overview');
          this.closeMobileDrawer();
        });
      }

      const mobile_btn = document.getElementById('btn_mobile_menu');
      const backdrop = document.getElementById('sidebar_backdrop');
      if (mobile_btn) {
        mobile_btn.addEventListener('click', () => {
          document.getElementById('app_sidebar').classList.toggle('is-open');
          backdrop.classList.toggle('is-open');
        });
      }
      if (backdrop) {
        backdrop.addEventListener('click', () => this.closeMobileDrawer());
      }

      const mastery_btn = document.getElementById('btn_toggle_mastery');
      if (mastery_btn) {
        mastery_btn.addEventListener('click', () => {
          if (this.current_nav.indexOf('unit:') === 0) {
            const unit_id = this.current_nav.split(':')[1];
            this.storage.toggleUnitMastery(unit_id);
            this.updateMasteryHud();
            this.updateTopbar();
          }
        });
      }

      const modal = document.getElementById('shortcuts_modal');
      const open_modal_btn = document.getElementById('btn_shortcuts_modal');
      const close_modal_btn = document.getElementById('btn_close_modal');
      if (open_modal_btn && modal) {
        open_modal_btn.addEventListener('click', () => { modal.hidden = false; });
      }
      if (close_modal_btn && modal) {
        close_modal_btn.addEventListener('click', () => { modal.hidden = true; });
      }
      if (modal) {
        modal.addEventListener('click', (evt) => {
          if (evt.target === modal) { modal.hidden = true; }
        });
      }

      document.addEventListener('keydown', (evt) => {
        const tag = evt.target && evt.target.tagName ? evt.target.tagName.toLowerCase() : '';
        if (tag === 'input' || tag === 'textarea' || tag === 'select') {
          return;
        }
        if (evt.key === 'Escape') {
          if (modal) { modal.hidden = true; }
          this.closeMobileDrawer();
          return;
        }
        if (evt.key >= '1' && evt.key <= '8') {
          const idx = Number(evt.key) - 1;
          this.navigate('unit:0' + idx, this.current_tab);
        } else if (evt.key === 'm' || evt.key === 'M') {
          this.navigate('view:exam', 'overview');
        } else if (evt.key === 'r' || evt.key === 'R') {
          this.navigate('view:reference', 'overview');
        }
      });
    }

    /**
     * Closes the responsive mobile navigation drawer.
     */
    closeMobileDrawer() {
      const sb = document.getElementById('app_sidebar');
      const bd = document.getElementById('sidebar_backdrop');
      if (sb) { sb.classList.remove('is-open'); }
      if (bd) { bd.classList.remove('is-open'); }
    }

    /**
     * Updates active route and tab state, persists it, and re-renders the workspace.
     *
     * Args:
     *     nav_target (string): Route identifier ('unit:00'..'unit:07', 'view:exam', 'view:reference').
     *     tab_name (string): Unit tab identifier ('overview', 'theory', 'lab', 'practice').
     */
    navigate(nav_target, tab_name) {
      this.current_nav = nav_target;
      if (tab_name) {
        this.current_tab = tab_name;
      }
      this.storage.state.last_nav = this.current_nav;
      this.storage.state.last_tab = this.current_tab;
      this.storage.saveState();
      this.render();
    }

    /**
     * Updates the sidebar mastery progress bar and completion checkmarks.
     */
    updateMasteryHud() {
      const mastered = this.storage.state.mastered_units;
      const ratio_el = document.getElementById('mastery_ratio');
      const fill_el = document.getElementById('mastery_fill');
      const bar_el = document.getElementById('mastery_progressbar');
      if (ratio_el) {
        ratio_el.textContent = mastered.length + ' / 8';
      }
      if (fill_el) {
        fill_el.style.width = ((mastered.length / 8) * 100) + '%';
      }
      if (bar_el) {
        bar_el.setAttribute('aria-valuenow', String(mastered.length));
      }
      const status_badges = document.querySelectorAll('[data-status-unit]');
      for (let i = 0; i < status_badges.length; i += 1) {
        const uid = status_badges[i].getAttribute('data-status-unit');
        status_badges[i].innerHTML = this.storage.isUnitMastered(uid) ? this.icons.getIcon('check', 15) : '';
      }

      const done_games = this.storage.state.completed_games.length;
      const ch_ratio = document.getElementById('challenges_ratio');
      const ch_fill = document.getElementById('challenges_fill');
      const ch_bar = document.getElementById('challenges_progressbar');
      if (ch_ratio) {
        ch_ratio.textContent = done_games + ' / ' + this.total_challenges;
      }
      if (ch_fill) {
        const pct = this.total_challenges > 0 ? Math.min(100, (done_games / this.total_challenges) * 100) : 0;
        ch_fill.style.width = pct + '%';
      }
      if (ch_bar) {
        ch_bar.setAttribute('aria-valuemax', String(this.total_challenges));
        ch_bar.setAttribute('aria-valuenow', String(done_games));
      }
    }

    /**
     * Synchronizes topbar title, chapter badge, mastery button, and active sidebar link.
     */
    updateTopbar() {
      const nav_items = document.querySelectorAll('[data-nav]');
      for (let i = 0; i < nav_items.length; i += 1) {
        const is_match = nav_items[i].getAttribute('data-nav') === this.current_nav;
        nav_items[i].classList.toggle('active', is_match);
      }

      const title_el = document.getElementById('topbar_title');
      const tag_el = document.getElementById('topbar_chapter_tag');
      const mastery_btn = document.getElementById('btn_toggle_mastery');
      const mastery_icon = document.getElementById('mastery_btn_icon');
      const mastery_text = document.getElementById('mastery_btn_text');

      if (this.current_nav.indexOf('unit:') === 0) {
        const uid = this.current_nav.split(':')[1];
        const unit = this.units_data[uid];
        if (unit) {
          title_el.textContent = unit.title;
          tag_el.textContent = unit.chapter;
        }
        mastery_btn.style.display = 'inline-flex';
        const is_done = this.storage.isUnitMastered(uid);
        mastery_btn.classList.toggle('is-active', is_done);
        mastery_icon.innerHTML = this.icons.getIcon('check', 16);
        mastery_text.textContent = is_done ? 'Ολοκληρώθηκε' : 'Σήμανση Ολοκλήρωσης';
      } else if (this.current_nav === 'view:exam') {
        title_el.textContent = 'Προσομοίωση Προόδου (Mock Midterm)';
        tag_el.textContent = 'Τράπεζα ' + this.quiz_bank.length + ' Ερωτήσεων';
        mastery_btn.style.display = 'none';
      } else {
        title_el.textContent = 'Συγκεντρωτικός Πίνακας Πολυπλοκοτήτων Προόδου';
        tag_el.textContent = 'Ενότητες 01–07';
        mastery_btn.style.display = 'none';
      }
    }

    /**
     * Renders the active route inside the main workspace container.
     */
    render() {
      this.updateTopbar();
      const main_el = document.getElementById('app_main');
      if (!main_el) {
        return;
      }
      if (this.current_nav.indexOf('unit:') === 0) {
        this.renderUnitView(main_el, this.current_nav.split(':')[1]);
      } else if (this.current_nav === 'view:exam') {
        this.renderExamView(main_el);
      } else {
        this.renderReferenceView(main_el);
      }
    }

    /**
     * Renders a unit workspace with 4 segmented tabs (Overview, Theory, Lab, Practice).
     *
     * Args:
     *     main_el (HTMLElement): Main workspace element.
     *     unit_id (string): Unit identifier ('00'..'07').
     */
    renderUnitView(main_el, unit_id) {
      const unit = this.units_data[unit_id];
      if (!unit) {
        main_el.innerHTML = '<div class="card"><p>Η ενότητα δεν βρέθηκε.</p></div>';
        return;
      }

      const tabs = [
        { id: 'overview', label: 'Πλαίσιο & Ύλη', icon: 'compass' },
        { id: 'theory', label: 'Θεωρία & Αποδείξεις', icon: 'book' },
        { id: 'lab', label: 'Διαδραστικό Εργαστήριο', icon: 'cpu' },
        { id: 'playground', label: 'Κώδικας & Παιχνίδια', icon: 'layers' },
        { id: 'practice', label: 'Εξάσκηση & Παγίδες', icon: 'shield' }
      ];

      let tab_html = '<div class="tab-bar" role="tablist">';
      for (let i = 0; i < tabs.length; i += 1) {
        const t = tabs[i];
        const act = t.id === this.current_tab ? 'active' : '';
        tab_html += '<button type="button" role="tab" class="tab-btn ' + act + '" data-tab="' + t.id + '">' +
          this.icons.getIcon(t.icon, 16) +
          '<span>' + t.label + '</span></button>';
      }
      tab_html += '</div><section id="unit_tab_body" class="panel-enter" style="display:flex;flex-direction:column;gap:18px;"></section>';

      main_el.innerHTML = tab_html;

      const tab_btns = main_el.querySelectorAll('[data-tab]');
      for (let i = 0; i < tab_btns.length; i += 1) {
        tab_btns[i].addEventListener('click', (evt) => {
          this.current_tab = evt.currentTarget.getAttribute('data-tab');
          this.storage.state.last_tab = this.current_tab;
          this.storage.saveState();
          this.renderUnitView(main_el, unit_id);
        });
      }

      const body_el = main_el.querySelector('#unit_tab_body');
      if (this.current_tab === 'overview') {
        this.renderUnitOverview(body_el, unit);
      } else if (this.current_tab === 'theory') {
        this.renderUnitTheory(body_el, unit);
      } else if (this.current_tab === 'lab') {
        this.renderUnitLab(body_el, unit_id);
      } else if (this.current_tab === 'playground') {
        this.renderUnitPlayground(body_el, unit_id);
      } else {
        this.renderUnitPractice(body_el, unit);
      }
    }

    /**
     * Renders Tab 1: Overview, Exclusions, Learning Objectives, and Teaching Flow.
     *
     * Args:
     *     body_el (HTMLElement): Tab panel body container.
     *     unit (object): Structured unit curriculum entry.
     */
    renderUnitOverview(body_el, unit) {
      let html = '<div class="card stagger-item">' +
        '<h2>Εννοιολογικό Πλαίσιο</h2>' +
        '<p>' + formatRichText(unit.summary) + '</p>' +
        '<div class="scope-callout">' +
          '<div style="display:flex;align-items:center;gap:8px;font-weight:600;color:var(--accent-primary);">' +
            this.icons.getIcon('alert', 16) + '<span>Όρια Εξεταστέας Ύλης &amp; Εξαιρέσεις</span>' +
          '</div>' +
          '<ul class="bullet-list">' + unit.exclusions.map((e) => '<li>' + formatRichText(e) + '</li>').join('') + '</ul>' +
        '</div>' +
      '</div>';

      html += '<div class="grid-2">' +
        '<div class="card card-interactive stagger-item">' +
          '<h3>Μαθησιακοί Στόχοι</h3>' +
          '<ul class="bullet-list">' + unit.objectives.map((o) => '<li>' + formatRichText(o) + '</li>').join('') + '</ul>' +
        '</div>' +
        '<div class="card card-interactive stagger-item">' +
          '<h3>Διδακτική Πορεία Μελέτης</h3>' +
          '<ul class="bullet-list">' + unit.teaching_flow.map((f) => '<li>' + formatRichText(f) + '</li>').join('') + '</ul>' +
        '</div>' +
      '</div>';

      if (unit.dependencies && unit.dependencies.length > 0) {
        html += '<div class="card stagger-item"><h3>Συνδέσεις με Άλλες Ενότητες Προόδου</h3><div class="grid-2">';
        for (let i = 0; i < unit.dependencies.length; i += 1) {
          const dep = unit.dependencies[i];
          html += '<div class="card-deep">' +
            '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">' +
              '<span class="meta-pill accent">Ενότητα ' + dep.target + '</span>' +
              '<button type="button" class="btn btn-ghost" data-jump-unit="' + dep.target + '">Μετάβαση</button>' +
            '</div>' +
            '<p class="muted-text">' + formatRichText(dep.reason) + '</p>' +
          '</div>';
        }
        html += '</div></div>';
      }

      body_el.innerHTML = html;

      const jump_btns = body_el.querySelectorAll('[data-jump-unit]');
      for (let i = 0; i < jump_btns.length; i += 1) {
        jump_btns[i].addEventListener('click', (evt) => {
          this.navigate('unit:' + evt.currentTarget.getAttribute('data-jump-unit'), 'overview');
        });
      }
    }

    /**
     * Renders Tab 2: Theory Concept Cards, Expandable Proofs, and Comparison Table.
     *
     * Args:
     *     body_el (HTMLElement): Tab panel body container.
     *     unit (object): Structured unit curriculum entry.
     */
    renderUnitTheory(body_el, unit) {
      let html = '';
      for (let i = 0; i < unit.theory_cards.length; i += 1) {
        const card = unit.theory_cards[i];
        html += '<div class="card stagger-item">' +
          '<h3>' + formatRichText(card.title) + '</h3>' +
          '<div class="math-block">' + card.formula_html + '</div>' +
          '<p>' + card.body_html + '</p>' +
          '<div class="accordion">' +
            '<button type="button" class="accordion-trigger" aria-expanded="false">' +
              '<span>' + formatRichText(card.proof_title) + '</span>' +
              '<span class="accordion-chevron">' + this.icons.getIcon('chevron', 18) + '</span>' +
            '</button>' +
            '<div class="accordion-panel">' + card.proof_html + '</div>' +
          '</div>' +
        '</div>';
      }

      if (unit.comparison_table) {
        const tbl = unit.comparison_table;
        html += '<div class="card stagger-item">' +
          '<h3>' + formatRichText(tbl.title) + '</h3>' +
          '<div class="table-wrap"><table class="data-table"><thead><tr>' +
            tbl.headers.map((h) => '<th>' + formatRichText(h) + '</th>').join('') +
          '</tr></thead><tbody>' +
            tbl.rows.map((r) => '<tr>' + r.map((c) => '<td>' + formatRichText(c) + '</td>').join('') + '</tr>').join('') +
          '</tbody></table></div>' +
        '</div>';
      }

      body_el.innerHTML = html;
      this.bindAccordions(body_el);
    }

    /**
     * Renders Tab 3: Interactive Algorithm Lab for the active unit.
     *
     * Args:
     *     body_el (HTMLElement): Tab panel body container.
     *     unit_id (string): Unit identifier ('00'..'07').
     */
    renderUnitLab(body_el, unit_id) {
      const lab = this.labs[unit_id];
      if (!lab || typeof lab.mount !== 'function') {
        body_el.innerHTML = '<div class="card"><p>Δεν υπάρχει διαθέσιμο εργαστήριο για αυτή την ενότητα.</p></div>';
        return;
      }
      lab.mount(body_el);
    }

    /**
     * Renders Tab 4: Interactive Builder Game, Python Drop-In Puzzles, and Python Code Examples.
     *
     * Args:
     *     body_el (HTMLElement): Tab panel body container.
     *     unit_id (string): Unit identifier ('00'..'07').
     */
    renderUnitPlayground(body_el, unit_id) {
      const examples = this.code_examples[unit_id] || [];
      let html = '<div id="pg_builder_host" class="stagger-item"></div>';
      html += '<div id="pg_dropin_host" class="stagger-item"></div>';

      html += '<div class="card stagger-item">' +
        '<h3>Παραδείγματα Κώδικα Python (Πρότυπα Σημειώσεων &amp; Φροντιστηρίου)</h3>' +
        '<p class="muted-text">Αναπτύξτε κάθε υλοποίηση για να μελετήσετε τη δομή, τις συμβάσεις ονοματολογίας και τα σχόλια πολυπλοκότητας.</p>' +
        '<div style="display:flex;flex-direction:column;gap:12px;">';

      for (let i = 0; i < examples.length; i += 1) {
        const ex = examples[i];
        html += '<div class="accordion">' +
          '<button type="button" class="accordion-trigger" aria-expanded="false">' +
            '<span style="display:flex;flex-wrap:wrap;align-items:center;gap:10px;">' +
              '<span>' + formatRichText(ex.title) + '</span>' +
              '<span class="meta-pill">' + formatRichText(ex.source_tag) + '</span>' +
              '<span class="meta-pill accent">' + formatRichText(ex.complexity) + '</span>' +
            '</span>' +
            '<span class="accordion-chevron">' + this.icons.getIcon('chevron', 18) + '</span>' +
          '</button>' +
          '<div class="accordion-panel"><pre><code>' +
            String(ex.code).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;') +
          '</code></pre></div>' +
        '</div>';
      }
      html += '</div></div>';

      body_el.innerHTML = html;
      this.bindAccordions(body_el);

      const handleComplete = (challenge_id) => {
        this.storage.markGameCompleted(challenge_id);
        this.updateMasteryHud();
      };

      const builder_host = body_el.querySelector('#pg_builder_host');
      const builder_game = this.builder_games[unit_id];
      if (builder_host && builder_game && typeof builder_game.mount === 'function') {
        builder_game.mount(builder_host, handleComplete);
      }

      const dropin_host = body_el.querySelector('#pg_dropin_host');
      if (dropin_host && this.dropin_engine) {
        this.dropin_engine.mount(dropin_host, unit_id, this.storage.state.completed_games, handleComplete);
      }
    }

    /**
     * Renders Tab 4: Interactive Unit Drills, Worked Exercises, Traps, and SOS Summary.
     *
     * Args:
     *     body_el (HTMLElement): Tab panel body container.
     *     unit (object): Structured unit curriculum entry.
     */
    renderUnitPractice(body_el, unit) {
      const unit_drills = this.quiz_bank.filter((q) => q.unit_id === unit.unit_id);
      const tf_items = this.true_false_drills[unit.unit_id] || [];

      let html = '';
      if (tf_items.length > 0) {
        html += '<div class="card stagger-item">' +
          '<div class="card-header"><h3>Γρήγορος Έλεγχος ΣΩΣΤΟ / ΛΑΘΟΣ (Θέματα Φροντιστηρίου)</h3><span class="meta-pill accent">' + tf_items.length + ' προτάσεις</span></div>' +
          '<div id="unit_tf_host" class="tf-list"></div>' +
        '</div>';
      }

      html += '<div class="card stagger-item">' +
        '<div class="card-header"><h3>Ερωτήσεις Πολλαπλής Επιλογής Ενότητας</h3><span class="meta-pill accent">' + unit_drills.length + ' ερωτήσεις</span></div>' +
        '<div id="unit_drills_host" style="display:flex;flex-direction:column;gap:18px;"></div>' +
      '</div>';

      html += '<div class="card stagger-item">' +
        '<h3>Λυμένες Ασκήσεις Εξεταστικού Επιπέδου (Προοδευτική Αποκάλυψη)</h3>' +
        '<p class="muted-text">Δοκιμάστε πρώτα να διαμορφώσετε τη λύση μόνοι σας πριν ανοίξετε το πλαίσιο λύσης.</p>' +
        '<div style="display:flex;flex-direction:column;gap:12px;">';
      for (let i = 0; i < unit.worked_exercises.length; i += 1) {
        const ex = unit.worked_exercises[i];
        html += '<div class="card-deep">' +
          '<h4 style="margin-bottom:8px;">' + formatRichText(ex.title) + '</h4>' +
          '<p>' + ex.prompt_html + '</p>' +
          '<p class="muted-text"><strong>Στρατηγική:</strong> ' + ex.strategy_html + '</p>' +
          '<div class="accordion" style="margin-top:10px;">' +
            '<button type="button" class="accordion-trigger" aria-expanded="false">' +
              '<span>Αποκάλυψη Πλήρους Λύσης &amp; Ελέγχου</span>' +
              '<span class="accordion-chevron">' + this.icons.getIcon('chevron', 18) + '</span>' +
            '</button>' +
            '<div class="accordion-panel">' +
              '<div>' + ex.solution_html + '</div>' +
              '<div class="accent-callout" style="margin-top:10px;"><strong>Έλεγχος:</strong> ' + ex.check_html + '</div>' +
            '</div>' +
          '</div>' +
        '</div>';
      }
      html += '</div></div>';

      html += '<div class="card stagger-item"><h3>Εξεταστικές Παγίδες</h3><div class="grid-2">';
      for (let i = 0; i < unit.traps.length; i += 1) {
        const tr = unit.traps[i];
        html += '<div class="trap-card">' +
          '<div class="trap-wrong"><strong>Παγίδα:</strong> ' + formatRichText(tr.misconception) + '</div>' +
          '<div class="muted-text"><strong>Γιατί είναι λάθος:</strong> ' + formatRichText(tr.why_wrong) + '</div>' +
          '<div class="trap-rule"><strong>Ορθός Κανόνας:</strong> ' + formatRichText(tr.rule) + '</div>' +
        '</div>';
      }
      html += '</div></div>';

      html += '<div class="card stagger-item"><h3>Σημεία SOS &amp; Γρήγορη Επανάληψη</h3>' +
        '<ul class="bullet-list">' + unit.sos_points.map((s) => '<li>' + formatRichText(s) + '</li>').join('') + '</ul>' +
      '</div>';

      body_el.innerHTML = html;
      this.bindAccordions(body_el);

      const tf_host = body_el.querySelector('#unit_tf_host');
      if (tf_host) {
        this.renderTrueFalseList(tf_host, unit.unit_id, tf_items);
      }

      const drill_host = body_el.querySelector('#unit_drills_host');
      if (drill_host) {
        this.renderQuestionList(drill_host, unit_drills, this.storage.state.drill_answers, (q_id, opt_idx) => {
          this.storage.recordDrillAnswer(q_id, opt_idx);
        });
      }
    }

    /**
     * Renders rapid-fire True/False recitation statements with immediate explanation feedback.
     *
     * Args:
     *     host_el (HTMLElement): Host container for True/False rows.
     *     unit_id (string): Unit identifier ('00'..'07').
     *     tf_items (Array<object>): List of { statement, answer, explanation } objects.
     */
    renderTrueFalseList(host_el, unit_id, tf_items) {
      let html = '';
      for (let i = 0; i < tf_items.length; i += 1) {
        const item = tf_items[i];
        const tf_key = 'tf_' + unit_id + '_' + i;
        const chosen = this.storage.state.tf_answers[tf_key];
        const has_ans = typeof chosen === 'boolean';
        const is_ok = has_ans && chosen === item.answer;

        html += '<div class="tf-row ' + (has_ans ? (is_ok ? 'is-correct' : 'is-wrong') : '') + '" data-tf-idx="' + i + '">' +
          '<div class="tf-top">' +
            '<div><strong>#' + (i + 1) + '.</strong> ' + formatRichText(item.statement) + '</div>' +
            '<div class="tf-actions">' +
              '<button type="button" class="btn ' + (has_ans && chosen === true ? 'btn-primary' : 'btn-secondary') + '" data-tf-val="true">ΣΩΣΤΟ</button>' +
              '<button type="button" class="btn ' + (has_ans && chosen === false ? 'btn-primary' : 'btn-secondary') + '" data-tf-val="false">ΛΑΘΟΣ</button>' +
            '</div>' +
          '</div>' +
          (has_ans ? '<div class="muted-text" style="font-size:0.88rem;">' + formatRichText(item.explanation) + '</div>' : '') +
        '</div>';
      }
      host_el.innerHTML = html;

      const btns = host_el.querySelectorAll('[data-tf-val]');
      for (let i = 0; i < btns.length; i += 1) {
        btns[i].addEventListener('click', (evt) => {
          const row = evt.currentTarget.closest('[data-tf-idx]');
          const idx = Number(row.getAttribute('data-tf-idx'));
          const val = evt.currentTarget.getAttribute('data-tf-val') === 'true';
          this.storage.recordTfAnswer('tf_' + unit_id + '_' + idx, val);
          this.renderTrueFalseList(host_el, unit_id, tf_items);
        });
      }
    }

    /**
     * Binds progressive-disclosure accordion expand/collapse triggers inside a container.
     *
     * Args:
     *     container_el (HTMLElement): Container wrapping accordion elements.
     */
    bindAccordions(container_el) {
      const triggers = container_el.querySelectorAll('.accordion-trigger');
      for (let i = 0; i < triggers.length; i += 1) {
        triggers[i].addEventListener('click', (evt) => {
          const btn = evt.currentTarget;
          const acc = btn.closest('.accordion');
          const will_open = !acc.classList.contains('is-open');
          acc.classList.toggle('is-open', will_open);
          btn.setAttribute('aria-expanded', will_open ? 'true' : 'false');
        });
      }
    }

    /**
     * Renders an interactive list of multiple-choice questions with instant Architectural Draft feedback.
     *
     * Args:
     *     host_el (HTMLElement): Target DOM element.
     *     questions (Array<object>): Questions to render.
     *     answer_map (object): Map of q_id to selected option index.
     *     on_select_cb (Function): Callback invoked with (q_id, opt_idx) upon click.
     */
    renderQuestionList(host_el, questions, answer_map, on_select_cb) {
      let html = '';
      for (let i = 0; i < questions.length; i += 1) {
        const q = questions[i];
        const chosen = answer_map[q.id];
        const has_answered = typeof chosen === 'number';
        const is_correct = has_answered && chosen === q.correct_index;

        html += '<div class="card-deep" data-qid="' + q.id + '">' +
          '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">' +
            '<span class="meta-pill">Ενότητα ' + q.unit_id + ' | #' + (i + 1) + '</span>' +
          '</div>' +
          '<p style="font-weight:600;color:var(--ink-bright);">' + formatRichText(q.prompt) + '</p>' +
          '<div class="quiz-options">';

        for (let k = 0; k < q.options.length; k += 1) {
          let cls = '';
          if (has_answered) {
            if (k === q.correct_index) {
              cls = 'is-correct';
            } else if (k === chosen) {
              cls = 'is-wrong';
            }
          }
          html += '<button type="button" class="quiz-option ' + cls + '" data-opt="' + k + '">' +
            '<span>' + formatRichText(q.options[k]) + '</span>' +
            (has_answered && k === q.correct_index ? this.icons.getIcon('check', 16) : (has_answered && k === chosen ? this.icons.getIcon('x', 16) : '')) +
          '</button>';
        }
        html += '</div>';

        if (has_answered) {
          html += '<div class="quiz-feedback ' + (is_correct ? 'is-correct' : 'is-wrong') + '">' +
            '<div class="feedback-badge">' +
              this.icons.getIcon(is_correct ? 'check' : 'alert', 16) +
              '<span>' + (is_correct ? 'Σωστή απάντηση' : 'Προσοχή — Ελέγξτε τη θεωρία') + '</span>' +
            '</div>' +
            '<div>' + formatRichText(q.explanation) + '</div>' +
          '</div>';
        }
        html += '</div>';
      }

      host_el.innerHTML = html;

      const cards = host_el.querySelectorAll('[data-qid]');
      for (let i = 0; i < cards.length; i += 1) {
        const q_id = cards[i].getAttribute('data-qid');
        const opts = cards[i].querySelectorAll('[data-opt]');
        for (let j = 0; j < opts.length; j += 1) {
          opts[j].addEventListener('click', (evt) => {
            const opt_idx = Number(evt.currentTarget.getAttribute('data-opt'));
            on_select_cb(q_id, opt_idx);
            this.renderQuestionList(host_el, questions, answer_map, on_select_cb);
          });
        }
      }
    }

    /**
     * Renders the configurable Mock Midterm Exam workspace.
     *
     * Args:
     *     main_el (HTMLElement): Main workspace element.
     */
    renderExamView(main_el) {
      const report = this.quiz_engine.computeReport();
      const pct = report.total > 0 ? Math.round((report.correct / report.total) * 100) : 0;

      let unit_opts = '<option value="all">Όλες οι ενότητες (00–07)</option>';
      for (let i = 0; i <= 7; i += 1) {
        const uid = '0' + i;
        unit_opts += '<option value="' + uid + '" ' + (this.quiz_engine.selected_unit === uid ? 'selected' : '') + '>Ενότητα ' + uid + '</option>';
      }

      let html = '<div class="card panel-enter">' +
        '<h2>Προσομοίωση Γραπτής Προόδου</h2>' +
        '<p class="muted-text">Ρυθμίστε το μέγεθος του τεστ ή εστιάστε σε συγκεκριμένη ενότητα. Κάθε ερώτηση ελέγχει ασυμπτωτική περίπτωση, ιχνηλάτηση ή εξεταστική παγίδα.</p>' +
        '<div class="lab-toolbar">' +
          '<label class="lab-field">Πλήθος: <select id="exam_cnt_sel" class="select-control">' +
            '<option value="10" ' + (this.quiz_engine.selected_count === 10 ? 'selected' : '') + '>10 ερωτήσεις</option>' +
            '<option value="20" ' + (this.quiz_engine.selected_count === 20 ? 'selected' : '') + '>20 ερωτήσεις</option>' +
            '<option value="' + this.quiz_bank.length + '" ' + (this.quiz_engine.selected_count >= this.quiz_bank.length ? 'selected' : '') + '>Όλες (' + this.quiz_bank.length + ')</option>' +
          '</select></label>' +
          '<label class="lab-field">Ενότητα: <select id="exam_unit_sel" class="select-control">' + unit_opts + '</select></label>' +
          '<button type="button" class="btn btn-primary" id="exam_new_btn">' + this.icons.getIcon('reset', 16) + '<span>Νέα Προσομοίωση</span></button>' +
        '</div>' +
        '<div class="grid-3">' +
          '<div class="card-deep"><div class="muted-text">Απαντημένες</div><div><code>' + report.answered + ' / ' + report.total + '</code></div></div>' +
          '<div class="card-deep"><div class="muted-text">Σωστές</div><div><code>' + report.correct + ' / ' + report.total + ' (' + pct + '%)</code></div></div>' +
          '<div class="card-deep"><div class="muted-text">Εκτίμηση Ετοιμότητας</div><div><code>' + (report.answered === 0 ? 'Σε αναμονή' : (pct >= 80 ? 'Εξαιρετική' : (pct >= 60 ? 'Καλή — έλεγχος παγίδων' : 'Χρειάζεται επανάληψη'))) + '</code></div></div>' +
        '</div>';

      const unit_keys = Object.keys(report.per_unit).sort();
      if (report.answered > 0 && unit_keys.length > 0) {
        html += '<div class="card-deep"><strong>Διάγνωση ανά Ενότητα:</strong><div class="array-strip" style="margin-top:10px;">';
        for (let i = 0; i < unit_keys.length; i += 1) {
          const uk = unit_keys[i];
          const st = report.per_unit[uk];
          html += '<div class="array-cell ' + (st.correct === st.total ? 'is-active' : '') + '">' +
            '<span class="array-cell-idx">Εν. ' + uk + '</span>' +
            '<span class="array-cell-val">' + st.correct + '/' + st.total + '</span>' +
          '</div>';
        }
        html += '</div></div>';
      }

      html += '<div id="exam_q_host" style="display:flex;flex-direction:column;gap:16px;"></div></div>';
      main_el.innerHTML = html;

      main_el.querySelector('#exam_new_btn').addEventListener('click', () => {
        const cnt = Number(main_el.querySelector('#exam_cnt_sel').value);
        const uid = main_el.querySelector('#exam_unit_sel').value;
        this.quiz_engine.startSession(cnt, uid);
        this.renderExamView(main_el);
      });

      const q_host = main_el.querySelector('#exam_q_host');
      this.renderQuestionList(q_host, this.quiz_engine.active_questions, this.quiz_engine.user_answers, (q_id, opt_idx) => {
        this.quiz_engine.answerQuestion(q_id, opt_idx);
        this.renderExamView(main_el);
      });
    }

    /**
     * Renders the searchable Master Complexity Reference Table across units 01-07.
     *
     * Args:
     *     main_el (HTMLElement): Main workspace element.
     */
    renderReferenceView(main_el) {
      const q = this.ref_search_query.trim().toLowerCase();
      const filtered = this.complexity_rows.filter((row) => {
        const match_unit = this.ref_filter_unit === 'all' || row.unit === this.ref_filter_unit;
        const match_text = !q ||
          row.name.toLowerCase().indexOf(q) !== -1 ||
          row.worst.toLowerCase().indexOf(q) !== -1 ||
          row.best_expected.toLowerCase().indexOf(q) !== -1 ||
          row.note.toLowerCase().indexOf(q) !== -1;
        return match_unit && match_text;
      });

      let html = '<div class="card panel-enter">' +
        '<h2>Συγκεντρωτικός Πίνακας Πολυπλοκοτήτων Προόδου</h2>' +
        '<p class="muted-text">Αναζητήστε αλγόριθμο, δομή δεδομένων ή περίπτωση πολυπλοκότητας (χειρότερη, αναμενόμενη, επιμερισμένη).</p>' +
        '<div class="lab-toolbar">' +
          '<input type="text" id="ref_search_in" class="input-control" placeholder="Αναζήτηση (π.χ. Cuckoo, O(n log n), επιμερισμένη)..." value="' + this.ref_search_query.replace(/"/g, '&quot;') + '" style="flex:1;min-width:220px;">' +
          '<button type="button" class="btn ' + (this.ref_filter_unit === 'all' ? 'btn-primary' : 'btn-secondary') + '" data-rf="all">Όλες</button>';

      for (let i = 1; i <= 7; i += 1) {
        const uid = '0' + i;
        html += '<button type="button" class="btn ' + (this.ref_filter_unit === uid ? 'btn-primary' : 'btn-secondary') + '" data-rf="' + uid + '">' + uid + '</button>';
      }
      html += '</div>';

      html += '<div class="table-wrap"><table class="data-table"><thead><tr>' +
        '<th>Εν.</th><th>Αλγόριθμος / Δομή</th><th>Χειρότερη Περίπτωση</th><th>Καλύτερη / Αναμενόμενη / Επιμερισμένη</th><th>Επιπλέον Χώρος</th><th>Κρίσιμη Παρατήρηση</th>' +
      '</tr></thead><tbody>' +
        filtered.map((r) =>
          '<tr>' +
            '<td><span class="meta-pill">' + r.unit + '</span></td>' +
            '<td>' + formatRichText(r.name) + '</td>' +
            '<td><code>' + formatRichText(r.worst) + '</code></td>' +
            '<td>' + formatRichText(r.best_expected) + '</td>' +
            '<td><code>' + formatRichText(r.space) + '</code></td>' +
            '<td class="muted-text">' + formatRichText(r.note) + '</td>' +
          '</tr>'
        ).join('') +
      '</tbody></table></div></div>';

      main_el.innerHTML = html;

      const search_in = main_el.querySelector('#ref_search_in');
      search_in.addEventListener('input', (evt) => {
        this.ref_search_query = evt.target.value;
        this.renderReferenceView(main_el);
        const restored = main_el.querySelector('#ref_search_in');
        if (restored) {
          restored.focus();
          restored.setSelectionRange(restored.value.length, restored.value.length);
        }
      });

      const filter_btns = main_el.querySelectorAll('[data-rf]');
      for (let i = 0; i < filter_btns.length; i += 1) {
        filter_btns[i].addEventListener('click', (evt) => {
          this.ref_filter_unit = evt.currentTarget.getAttribute('data-rf');
          this.renderReferenceView(main_el);
        });
      }
    }
  }

  document.addEventListener('DOMContentLoaded', () => {
    const controller = new AppController();
    global_scope.MidtermApp.controller = controller;
    controller.init();
  });
})(window);
