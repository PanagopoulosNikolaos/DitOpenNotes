(function (global_scope) {
  'use strict';

  /**
   * Formats lightweight inline markup such as backticked identifiers safely.
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
   * Normalizes a student's fill-in answer for tolerant comparison.
   *
   * Args:
   *     raw_value (string): Student input string.
   *
   * Returns:
   *     string: Lowercased, trimmed, comma-normalized answer string.
   */
  function normalizeAnswer(raw_value) {
    return String(raw_value || '')
      .trim()
      .toLowerCase()
      .replace(/,/g, '.')
      .replace(/\s+/g, '');
  }

  /**
   * Tracks student exercise progress and gamified streak strictly within the current session.
   *
   * Clears any legacy persisted storage on startup so reloads always begin completely fresh.
   * Methods: recordFillResult(fill_id, value, is_correct), resetFillExercises(fill_ids), recordTfAnswer(tf_key, choice_bool), resetTfUnit(unit_id), recordDrillAnswer(q_id, opt_idx), resetDrills(q_ids), markGameCompleted(challenge_id), unmarkGameCompleted(challenge_id), resetAllSession().
   */
  class SessionTracker {
    /**
     * Initializes clean in-memory session state and removes legacy localStorage keys.
     */
    constructor() {
      try {
        // Removes legacy persisted state so relaunches never keep old solved answers.
        global_scope.localStorage.removeItem('dit_algo504_midterm_v1');
      } catch (_err) {
        // Ignores private-mode storage restrictions gracefully.
      }
      this.resetAllSession();
    }

    /**
     * Resets all in-memory exercise answers, solved games, points, and streak to zero.
     */
    resetAllSession() {
      this.fill_answers = {};
      this.tf_answers = {};
      this.drill_answers = {};
      this.completed_games = [];
      this.current_streak = 0;
    }

    /**
     * Records a fill-in-the-blank submission and updates the active streak.
     *
     * Args:
     *     fill_id (string): Unique fill exercise identifier.
     *     value (string): Submitted answer string.
     *     is_correct (boolean): Whether the answer matched an expected solution.
     */
    recordFillResult(fill_id, value, is_correct) {
      this.fill_answers[fill_id] = {
        value: value,
        is_correct: is_correct,
        revealed: false,
        hint_shown: Boolean(this.fill_answers[fill_id] && this.fill_answers[fill_id].hint_shown)
      };
      this.current_streak = is_correct ? this.current_streak + 1 : 0;
    }

    /**
     * Toggles hint visibility for a fill exercise.
     *
     * Args:
     *     fill_id (string): Unique fill exercise identifier.
     */
    toggleFillHint(fill_id) {
      const prev = this.fill_answers[fill_id] || { value: '', is_correct: null, revealed: false, hint_shown: false };
      prev.hint_shown = !prev.hint_shown;
      this.fill_answers[fill_id] = prev;
    }

    /**
     * Reveals the canonical solution for a fill exercise without awarding points.
     *
     * Args:
     *     fill_id (string): Unique fill exercise identifier.
     */
    revealFillSolution(fill_id) {
      const prev = this.fill_answers[fill_id] || { value: '', is_correct: null, revealed: false, hint_shown: false };
      prev.revealed = true;
      this.fill_answers[fill_id] = prev;
    }

    /**
     * Clears one or more fill-in exercises back to their unsolved state.
     *
     * Args:
     *     fill_ids (Array<string>): Identifiers of fill exercises to reset.
     */
    resetFillExercises(fill_ids) {
      for (let i = 0; i < fill_ids.length; i += 1) {
        delete this.fill_answers[fill_ids[i]];
      }
    }

    /**
     * Records a True/False selection and updates streak status.
     *
     * Args:
     *     tf_key (string): Unique True/False statement key.
     *     choice_bool (boolean): Selected True or False boolean.
     *     is_correct (boolean): Whether the selection matches the canonical answer.
     */
    recordTfAnswer(tf_key, choice_bool, is_correct) {
      this.tf_answers[tf_key] = choice_bool;
      this.current_streak = is_correct ? this.current_streak + 1 : 0;
    }

    /**
     * Clears all True/False answers belonging to a specific unit.
     *
     * Args:
     *     unit_id (string): Unit identifier ('prereq', '00'..'07').
     */
    resetTfUnit(unit_id) {
      const prefix = 'tf_' + unit_id + '_';
      const keys = Object.keys(this.tf_answers);
      for (let i = 0; i < keys.length; i += 1) {
        if (keys[i].indexOf(prefix) === 0) {
          delete this.tf_answers[keys[i]];
        }
      }
    }

    /**
     * Records a multiple-choice drill answer and updates streak status.
     *
     * Args:
     *     q_id (string): Question identifier.
     *     opt_idx (number): Selected option index.
     *     is_correct (boolean): Whether the option is correct.
     */
    recordDrillAnswer(q_id, opt_idx, is_correct) {
      this.drill_answers[q_id] = opt_idx;
      this.current_streak = is_correct ? this.current_streak + 1 : 0;
    }

    /**
     * Clears multiple-choice drill answers for the given question IDs.
     *
     * Args:
     *     q_ids (Array<string>): Question identifiers to clear.
     */
    resetDrills(q_ids) {
      for (let i = 0; i < q_ids.length; i += 1) {
        delete this.drill_answers[q_ids[i]];
      }
    }

    /**
     * Marks an interactive Drop-In or Builder challenge as solved in this session.
     *
     * Args:
     *     challenge_id (string): Unique puzzle or builder game identifier.
     */
    markGameCompleted(challenge_id) {
      if (this.completed_games.indexOf(challenge_id) === -1) {
        this.completed_games.push(challenge_id);
        this.current_streak += 1;
      }
    }

    /**
     * Removes a challenge from the completed list when reset by the student.
     *
     * Args:
     *     challenge_id (string): Unique puzzle or builder game identifier.
     */
    unmarkGameCompleted(challenge_id) {
      const idx = this.completed_games.indexOf(challenge_id);
      if (idx !== -1) {
        this.completed_games.splice(idx, 1);
      }
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
      this.selected_count = 10;
      this.selected_unit = 'all';
    }

    /**
     * Starts a fresh Mock Exam session with shuffled questions matching filters.
     *
     * Args:
     *     question_count (number): Maximum number of questions to include.
     *     filter_unit (string): Specific unit ID ('prereq', '00'..'07') or 'all'.
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
   * Coordinates W3Schools-style linear tutorial navigation, inline examples, labs, exercises, and games.
   *
   * Connects SessionTracker, QuizEngine, IconLibrary, curriculum data, and interactive widgets.
   * Methods: init(), bindShellEvents(), navigate(nav_target), computeSessionStats(), updateSessionHud(), render().
   */
  class AppController {
    /**
     * Initializes controller dependencies, chapter order, reference catalog, and initial route.
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
      this.session = new SessionTracker();
      this.quiz_engine = new QuizEngine(this.quiz_bank);
      this.quiz_engine.startSession(10, 'all');

      this.chapter_order = ['prereq', '00', '01', '02', '03', '04', '05', '06', '07'];
      this.chapter_labels = {
        prereq: 'Προαπαιτούμενα',
        '00': '00 — Χάρτης',
        '01': '01 — Ανάλυση',
        '02': '02 — Σωροί',
        '03': '03 — Hash & Κούκος',
        '04': '04 — Union-Find',
        '05': '05 — Ταξινόμηση',
        '06': '06 — Άπληστη',
        '07': '07 — Διαίρει & Βασίλευε'
      };

      this.current_nav = 'unit:prereq';
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
     * Initializes static UI icons, binds shell events, updates HUD, and performs initial render.
     */
    init() {
      this.injectStaticIcons();
      this.bindShellEvents();
      this.updateSessionHud();
      this.render();
    }

    /**
     * Injects monochromatic SVG icons into static shell placeholders.
     */
    injectStaticIcons() {
      const slot_map = [
        ['brand_icon_slot', 'compass', 20],
        ['reset_session_icon', 'reset', 15],
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
     * Binds navigation rail, session reset button, modal controls, and keyboard shortcuts.
     */
    bindShellEvents() {
      const nav_items = document.querySelectorAll('[data-nav]');
      for (let i = 0; i < nav_items.length; i += 1) {
        nav_items[i].addEventListener('click', (evt) => {
          const target = evt.currentTarget.getAttribute('data-nav');
          this.navigate(target);
          this.closeMobileDrawer();
        });
      }

      const reset_session_btn = document.getElementById('btn_reset_session');
      if (reset_session_btn) {
        reset_session_btn.addEventListener('click', () => {
          this.resetEntireSession();
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
        if (evt.key === '0') {
          this.navigate('unit:prereq');
        } else if (evt.key >= '1' && evt.key <= '8') {
          const idx = Number(evt.key) - 1;
          this.navigate('unit:0' + idx);
        } else if (evt.key === 'm' || evt.key === 'M') {
          this.navigate('view:exam');
        } else if (evt.key === 'r' || evt.key === 'R') {
          this.navigate('view:reference');
        }
      });
    }

    /**
     * Resets all solved answers, points, streak, Drop-In puzzles, and Builder games for a clean session.
     */
    resetEntireSession() {
      this.session.resetAllSession();
      if (this.dropin_engine && typeof this.dropin_engine.resetAll === 'function') {
        this.dropin_engine.resetAll();
      }
      const game_keys = Object.keys(this.builder_games);
      for (let i = 0; i < game_keys.length; i += 1) {
        const game = this.builder_games[game_keys[i]];
        if (game && typeof game.resetAll === 'function') {
          game.resetAll();
        }
      }
      this.updateSessionHud();
      this.render();
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
     * Updates active route, scrolls smoothly to top, and re-renders the workspace.
     *
     * Args:
     *     nav_target (string): Route identifier ('unit:prereq', 'unit:00'..'unit:07', 'view:exam', 'view:reference').
     */
    navigate(nav_target) {
      this.current_nav = nav_target;
      this.render();
      global_scope.scrollTo({ top: 0, behavior: 'smooth' });
    }

    /**
     * Computes live solved totals, total exercises, points, and per-unit solved counts.
     *
     * Returns:
     *     object: Aggregated session metrics.
     */
    computeSessionStats() {
      let total_items = 0;
      let solved_items = 0;
      let points = 0;
      const per_unit = {};

      for (let c = 0; c < this.chapter_order.length; c += 1) {
        const uid = this.chapter_order[c];
        const unit = this.units_data[uid];
        let u_total = 0;
        let u_solved = 0;

        const fills = (unit && unit.fill_exercises) || [];
        for (let i = 0; i < fills.length; i += 1) {
          u_total += 1;
          const ans = this.session.fill_answers[fills[i].id];
          if (ans && ans.is_correct) {
            u_solved += 1;
            points += 10;
          }
        }

        const tfs = this.true_false_drills[uid] || [];
        for (let i = 0; i < tfs.length; i += 1) {
          u_total += 1;
          const chosen = this.session.tf_answers['tf_' + uid + '_' + i];
          if (typeof chosen === 'boolean' && chosen === tfs[i].answer) {
            u_solved += 1;
            points += 5;
          }
        }

        const mcqs = this.quiz_bank.filter((q) => q.unit_id === uid);
        for (let i = 0; i < mcqs.length; i += 1) {
          u_total += 1;
          if (this.session.drill_answers[mcqs[i].id] === mcqs[i].correct_index) {
            u_solved += 1;
            points += 10;
          }
        }

        if (this.builder_games[uid]) {
          u_total += 1;
          if (this.session.completed_games.indexOf('game_' + uid) !== -1) {
            u_solved += 1;
            points += 20;
          }
        }

        const dropins = this.dropin_puzzles[uid] || [];
        for (let i = 0; i < dropins.length; i += 1) {
          u_total += 1;
          if (this.session.completed_games.indexOf(dropins[i].id) !== -1) {
            u_solved += 1;
            points += 20;
          }
        }

        per_unit[uid] = { solved: u_solved, total: u_total };
        total_items += u_total;
        solved_items += u_solved;
      }

      return {
        solved: solved_items,
        total: total_items,
        points: points,
        streak: this.session.current_streak,
        games_done: this.session.completed_games.length,
        total_games: Object.keys(this.builder_games).length +
          Object.keys(this.dropin_puzzles).reduce((acc, k) => acc + this.dropin_puzzles[k].length, 0),
        per_unit: per_unit
      };
    }

    /**
     * Updates the sidebar session progress bar, points, streak, and per-unit badges.
     */
    updateSessionHud() {
      const stats = this.computeSessionStats();
      const ratio_el = document.getElementById('session_solved_ratio');
      const fill_el = document.getElementById('session_fill');
      const bar_el = document.getElementById('session_progressbar');
      const score_el = document.getElementById('session_score_label');

      if (ratio_el) {
        ratio_el.textContent = stats.solved + ' / ' + stats.total;
      }
      if (fill_el) {
        const pct = stats.total > 0 ? Math.min(100, (stats.solved / stats.total) * 100) : 0;
        fill_el.style.width = pct + '%';
      }
      if (bar_el) {
        bar_el.setAttribute('aria-valuemax', String(Math.max(1, stats.total)));
        bar_el.setAttribute('aria-valuenow', String(stats.solved));
      }
      if (score_el) {
        score_el.textContent = stats.points + ' pts | Σερί ' + stats.streak;
      }

      const status_badges = document.querySelectorAll('[data-status-unit]');
      for (let i = 0; i < status_badges.length; i += 1) {
        const uid = status_badges[i].getAttribute('data-status-unit');
        const unit_stat = stats.per_unit[uid];
        if (unit_stat && unit_stat.solved > 0) {
          status_badges[i].textContent = unit_stat.solved + '/' + unit_stat.total;
        } else {
          status_badges[i].textContent = '';
        }
      }

      const hud_pts = document.getElementById('gamified_hud_points');
      const hud_streak = document.getElementById('gamified_hud_streak');
      const hud_games = document.getElementById('gamified_hud_games');
      if (hud_pts) { hud_pts.textContent = stats.points + ' pts'; }
      if (hud_streak) { hud_streak.textContent = String(stats.streak); }
      if (hud_games) { hud_games.textContent = stats.games_done + ' / ' + stats.total_games; }
    }

    /**
     * Synchronizes topbar title, chapter badge, and active sidebar link.
     */
    updateTopbar() {
      const nav_items = document.querySelectorAll('[data-nav]');
      for (let i = 0; i < nav_items.length; i += 1) {
        const is_match = nav_items[i].getAttribute('data-nav') === this.current_nav;
        nav_items[i].classList.toggle('active', is_match);
      }

      const title_el = document.getElementById('topbar_title');
      const tag_el = document.getElementById('topbar_chapter_tag');

      if (this.current_nav.indexOf('unit:') === 0) {
        const uid = this.current_nav.split(':')[1];
        const unit = this.units_data[uid];
        if (unit) {
          title_el.textContent = unit.title;
          tag_el.textContent = unit.chapter;
        }
      } else if (this.current_nav === 'view:exam') {
        title_el.textContent = 'Προσομοίωση Προόδου (Mock Midterm)';
        tag_el.textContent = 'Τράπεζα ' + this.quiz_bank.length + ' Ερωτήσεων';
      } else {
        title_el.textContent = 'Συγκεντρωτικός Πίνακας Πολυπλοκοτήτων Προόδου';
        tag_el.textContent = 'Ενότητες 01–07';
      }
    }

    /**
     * Renders the active route inside the main workspace container.
     */
    render() {
      this.updateTopbar();
      this.updateSessionHud();
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
     * Builds the W3Schools-style Previous / Next chapter navigation bar markup.
     *
     * Args:
     *     unit_id (string): Active unit identifier.
     *
     * Returns:
     *     string: HTML markup for the lesson navigation bar.
     */
    buildLessonNavBar(unit_id) {
      const idx = this.chapter_order.indexOf(unit_id);
      const prev_id = idx > 0 ? this.chapter_order[idx - 1] : null;
      const next_id = idx !== -1 && idx < this.chapter_order.length - 1 ? this.chapter_order[idx + 1] : null;

      let html = '<div class="lesson-nav-bar">';
      if (prev_id) {
        html += '<button type="button" class="btn btn-secondary lesson-nav-btn" data-nav-jump="unit:' + prev_id + '">' +
          this.icons.getIcon('arrow_left', 16) +
          '<span>Προηγούμενο: ' + formatRichText(this.chapter_labels[prev_id]) + '</span></button>';
      } else {
        html += '<span></span>';
      }

      if (next_id) {
        html += '<button type="button" class="btn btn-primary lesson-nav-btn" data-nav-jump="unit:' + next_id + '">' +
          '<span>Επόμενο: ' + formatRichText(this.chapter_labels[next_id]) + '</span>' +
          this.icons.getIcon('arrow_right', 16) + '</button>';
      } else {
        html += '<button type="button" class="btn btn-primary lesson-nav-btn" data-nav-jump="view:exam">' +
          '<span>Τελική Προσομοίωση Προόδου</span>' +
          this.icons.getIcon('arrow_right', 16) + '</button>';
      }
      html += '</div>';
      return html;
    }

    /**
     * Renders a complete W3Schools-style linear lesson page for the selected unit.
     *
     * Args:
     *     main_el (HTMLElement): Main workspace element.
     *     unit_id (string): Unit identifier ('prereq' or '00'..'07').
     */
    renderUnitView(main_el, unit_id) {
      const unit = this.units_data[unit_id];
      if (!unit) {
        main_el.innerHTML = '<div class="card"><p>Η ενότητα δεν βρέθηκε.</p></div>';
        return;
      }

      const has_lab = Boolean(this.labs[unit_id] && typeof this.labs[unit_id].mount === 'function');
      const has_games = Boolean(this.builder_games[unit_id]) || ((this.dropin_puzzles[unit_id] || []).length > 0);
      const stats = this.computeSessionStats();

      let html = '<div class="panel-enter" style="display:flex;flex-direction:column;gap:24px;">';
      html += this.buildLessonNavBar(unit_id);

      // In-page section jump pills for immediate navigation without hiding sections behind tabs.
      html += '<div class="section-jump-bar" aria-label="Ενότητες μαθήματος">' +
        '<button type="button" class="jump-pill" data-scroll-to="sec_recap">1. Γρήγορη Επανάληψη</button>' +
        '<button type="button" class="jump-pill" data-scroll-to="sec_theory">2. Θεωρία &amp; Παραδείγματα</button>' +
        (has_lab ? '<button type="button" class="jump-pill" data-scroll-to="sec_lab">3. Δοκίμασέ το (Εργαστήριο)</button>' : '') +
        '<button type="button" class="jump-pill" data-scroll-to="sec_worked_code">Λυμένες Ασκήσεις &amp; Python</button>' +
        '<button type="button" class="jump-pill" data-scroll-to="sec_solve">Ασκήσεις για Επίλυση</button>' +
        (has_games ? '<button type="button" class="jump-pill" data-scroll-to="sec_games">Παιχνιδοποιημένες Ασκήσεις</button>' : '') +
        '<button type="button" class="jump-pill" data-scroll-to="sec_traps">Παγίδες &amp; SOS</button>' +
      '</div>';

      // Lesson Overview Banner
      html += '<section class="card">' +
        '<h2>' + formatRichText(unit.title) + '</h2>' +
        '<p>' + formatRichText(unit.summary) + '</p>' +
        '<div class="scope-callout">' +
          '<div style="display:flex;align-items:center;gap:8px;font-weight:700;color:var(--accent-btn);">' +
            this.icons.getIcon('alert', 16) + '<span>Όρια Ύλης &amp; Σημαντικές Εξαιρέσεις</span>' +
          '</div>' +
          '<ul class="bullet-list">' + unit.exclusions.map((e) => '<li>' + formatRichText(e) + '</li>').join('') + '</ul>' +
        '</div>' +
      '</section>';

      // Section 1: Fast Recap (for beginners or quick refresh)
      if (unit.fast_recap) {
        html += '<section id="sec_recap" class="w3-section">' +
          '<div class="recap-box">' +
            '<div class="card-header">' +
              '<div class="w3-section-title">' + this.icons.getIcon('zap', 20) + '<h2>' + formatRichText(unit.fast_recap.title) + '</h2></div>' +
              (unit_id !== 'prereq' ? '<button type="button" class="btn btn-secondary" data-nav-jump="unit:prereq">Θυμίσου τα Βασικά Μαθηματικά</button>' : '') +
            '</div>' +
            '<p>' + unit.fast_recap.intro_html + '</p>' +
            '<div class="recap-grid">' +
              unit.fast_recap.key_ideas.map((idea) =>
                '<div class="recap-item">' +
                  '<div class="recap-term">' + formatRichText(idea.term) + '</div>' +
                  '<div>' + formatRichText(idea.plain_explanation) + '</div>' +
                  '<div class="muted-text" style="font-size:0.86rem;"><code>' + formatRichText(idea.mini_example) + '</code></div>' +
                '</div>'
              ).join('') +
            '</div>' +
          '</div>' +
        '</section>';
      }

      // Section 2: Theory + Inline Solved Example Directly Underneath Each Concept
      html += '<section id="sec_theory" class="w3-section">' +
        '<div class="w3-section-header">' +
          '<div class="w3-section-title">' + this.icons.getIcon('book', 20) + '<h2>Θεωρία &amp; Λυμένα Παραδείγματα</h2></div>' +
          '<span class="meta-pill accent">' + unit.theory_cards.length + ' βασικές έννοιες</span>' +
        '</div>';

      for (let i = 0; i < unit.theory_cards.length; i += 1) {
        const card = unit.theory_cards[i];
        html += '<article class="concept-block">' +
          '<div class="concept-header">' +
            '<h3>' + formatRichText(card.title) + '</h3>' +
            '<span class="concept-num">Έννοια ' + (i + 1) + '</span>' +
          '</div>' +
          '<div class="math-block">' + card.formula_html + '</div>' +
          '<p>' + card.body_html + '</p>';

        if (card.inline_example) {
          html += '<div class="w3-example-card">' +
            '<div class="w3-example-label">' + this.icons.getIcon('lightbulb', 18) + '<span>' + formatRichText(card.inline_example.title) + '</span></div>' +
            '<div class="w3-example-inner">' +
              '<div><strong>Πρόβλημα:</strong> ' + card.inline_example.prompt_html + '</div>' +
              '<div>' + card.inline_example.steps_html + '</div>' +
              '<div class="accent-callout"><strong>Κρατάμε:</strong> ' + card.inline_example.takeaway_html + '</div>' +
            '</div>' +
          '</div>';
        }

        if (card.proof_title && card.proof_html) {
          html += '<div class="accordion">' +
            '<button type="button" class="accordion-trigger" aria-expanded="false">' +
              '<span>' + formatRichText(card.proof_title) + '</span>' +
              '<span class="accordion-chevron">' + this.icons.getIcon('chevron', 18) + '</span>' +
            '</button>' +
            '<div class="accordion-panel">' + card.proof_html + '</div>' +
          '</div>';
        }
        html += '</article>';
      }

      if (unit.comparison_table) {
        const tbl = unit.comparison_table;
        html += '<div class="card">' +
          '<h3>' + formatRichText(tbl.title) + '</h3>' +
          '<div class="table-wrap"><table class="data-table"><thead><tr>' +
            tbl.headers.map((h) => '<th>' + formatRichText(h) + '</th>').join('') +
          '</tr></thead><tbody>' +
            tbl.rows.map((r) => '<tr>' + r.map((c) => '<td>' + formatRichText(c) + '</td>').join('') + '</tr>').join('') +
          '</tbody></table></div>' +
        '</div>';
      }
      html += '</section>';

      // Section 3: Try It Yourself — Interactive Lab
      if (has_lab) {
        html += '<section id="sec_lab" class="w3-section">' +
          '<div class="w3-section-header">' +
            '<div class="w3-section-title">' + this.icons.getIcon('cpu', 20) + '<h2>Δοκίμασέ το: Διαδραστικό Εργαστήριο</h2></div>' +
            '<span class="meta-pill">Βηματική Εκτέλεση</span>' +
          '</div>' +
          '<div id="unit_lab_host" style="display:flex;flex-direction:column;gap:16px;"></div>' +
        '</section>';
      }

      // Section 4: Additional Exam-Level Solved Exercises & Clean Python Code
      const examples = this.code_examples[unit_id] || [];
      html += '<section id="sec_worked_code" class="w3-section">' +
        '<div class="w3-section-header">' +
          '<div class="w3-section-title">' + this.icons.getIcon('code', 20) + '<h2>Λυμένες Ασκήσεις Εξετάσεων &amp; Κώδικας Python</h2></div>' +
          '<span class="meta-pill">' + unit.worked_exercises.length + ' ασκήσεις Προόδου</span>' +
        '</div>' +
        '<div class="card">' +
          '<h3>Λυμένες Ασκήσεις Εξεταστικού Επιπέδου (Σημειώσεις &amp; Φροντιστήρια)</h3>' +
          '<p class="muted-text">Διαβάστε τη στρατηγική, προσπαθήστε να γράψετε τα βήματα στο χαρτί και ανοίξτε τη λύση για επαλήθευση.</p>' +
          '<div style="display:flex;flex-direction:column;gap:12px;">';

      for (let i = 0; i < unit.worked_exercises.length; i += 1) {
        const ex = unit.worked_exercises[i];
        html += '<div class="w3-example-card">' +
          '<h4>' + formatRichText(ex.title) + '</h4>' +
          '<p>' + ex.prompt_html + '</p>' +
          '<p class="muted-text"><strong>Στρατηγική:</strong> ' + ex.strategy_html + '</p>' +
          '<div class="accordion">' +
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

      if (examples.length > 0) {
        html += '<div class="card">' +
          '<h3>Παραδείγματα Κώδικα Python (Με Καθαρή Ονοματολογία)</h3>' +
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
      }
      html += '</section>';

      // Section 5: Exercises to Solve (Fill-in-the-blank + True/False + MCQs)
      const fill_items = unit.fill_exercises || [];
      const tf_items = this.true_false_drills[unit_id] || [];
      const unit_drills = this.quiz_bank.filter((q) => q.unit_id === unit_id);

      html += '<section id="sec_solve" class="w3-section">' +
        '<div class="w3-section-header">' +
          '<div class="w3-section-title">' + this.icons.getIcon('edit', 20) + '<h2>Ασκήσεις για Επίλυση (Έλεγξε τις Γνώσεις σου)</h2></div>' +
          '<span class="meta-pill accent">Επαναφέρονται Πλήρως</span>' +
        '</div>';

      if (fill_items.length > 0) {
        html += '<div class="card">' +
          '<div class="card-header">' +
            '<div><h3>1. Συμπλήρωσε την Απάντηση (W3Schools Style)</h3><p class="muted-text">Πληκτρολογήστε τη σωστή τιμή και πατήστε Έλεγχος (+10 πόντοι ανά άσκηση).</p></div>' +
            '<button type="button" class="btn btn-ghost" id="btn_reset_fills">' + this.icons.getIcon('reset', 15) + '<span>Επαναφορά Όλων</span></button>' +
          '</div>' +
          '<div id="unit_fill_host" style="display:flex;flex-direction:column;gap:14px;"></div>' +
        '</div>';
      }

      if (tf_items.length > 0) {
        html += '<div class="card">' +
          '<div class="card-header">' +
            '<div><h3>2. Γρήγορος Έλεγχος ΣΩΣΤΟ / ΛΑΘΟΣ</h3><p class="muted-text">Θέματα Φροντιστηρίου (+5 πόντοι ανά σωστή απάντηση).</p></div>' +
            '<button type="button" class="btn btn-ghost" id="btn_reset_tf">' + this.icons.getIcon('reset', 15) + '<span>Επαναφορά</span></button>' +
          '</div>' +
          '<div id="unit_tf_host" class="tf-list"></div>' +
        '</div>';
      }

      if (unit_drills.length > 0) {
        html += '<div class="card">' +
          '<div class="card-header">' +
            '<div><h3>3. Ερωτήσεις Πολλαπλής Επιλογής Ενότητας</h3><p class="muted-text">Επιλέξτε απάντηση για άμεση αιτιολόγηση (+10 πόντοι ανά σωστή απάντηση).</p></div>' +
            '<button type="button" class="btn btn-ghost" id="btn_reset_mcqs">' + this.icons.getIcon('reset', 15) + '<span>Επαναφορά</span></button>' +
          '</div>' +
          '<div id="unit_drills_host" style="display:flex;flex-direction:column;gap:16px;"></div>' +
        '</div>';
      }
      html += '</section>';

      // Section 6: Gamified Exercises (Builder Game + Python Drop-In Puzzles + Scoreboard)
      if (has_games) {
        html += '<section id="sec_games" class="w3-section">' +
          '<div class="w3-section-header">' +
            '<div class="w3-section-title">' + this.icons.getIcon('trophy', 20) + '<h2>Παιχνιδοποιημένες Ασκήσεις &amp; Προκλήσεις</h2></div>' +
            '<span class="meta-pill accent">+20 πόντοι ανά πρόκληση</span>' +
          '</div>' +
          '<div class="gamified-hud">' +
            '<div class="gamified-stat"><span class="gamified-stat-label">Πόντοι Συνεδρίας</span><span class="gamified-stat-val" id="gamified_hud_points">' + stats.points + ' pts</span></div>' +
            '<div class="gamified-stat"><span class="gamified-stat-label">Τρέχον Σερί</span><span class="gamified-stat-val" id="gamified_hud_streak">' + stats.streak + '</span></div>' +
            '<div class="gamified-stat"><span class="gamified-stat-label">Ολοκληρωμένα Παιχνίδια</span><span class="gamified-stat-val" id="gamified_hud_games">' + stats.games_done + ' / ' + stats.total_games + '</span></div>' +
          '</div>' +
          '<div id="pg_builder_host"></div>' +
          '<div id="pg_dropin_host"></div>' +
        '</section>';
      }

      // Section 7: Exam Traps & SOS Summary
      html += '<section id="sec_traps" class="w3-section">' +
        '<div class="w3-section-header">' +
          '<div class="w3-section-title">' + this.icons.getIcon('shield', 20) + '<h2>Εξεταστικές Παγίδες &amp; Σημεία SOS</h2></div>' +
        '</div>' +
        '<div class="card"><h3>Συχνές Παγίδες</h3><div class="grid-2">';
      for (let i = 0; i < unit.traps.length; i += 1) {
        const tr = unit.traps[i];
        html += '<div class="trap-card">' +
          '<div class="trap-wrong"><strong>Παγίδα:</strong> ' + formatRichText(tr.misconception) + '</div>' +
          '<div class="muted-text"><strong>Γιατί είναι λάθος:</strong> ' + formatRichText(tr.why_wrong) + '</div>' +
          '<div class="trap-rule"><strong>Ορθός Κανόνας:</strong> ' + formatRichText(tr.rule) + '</div>' +
        '</div>';
      }
      html += '</div></div>';
      html += '<div class="card"><h3>Σημεία SOS &amp; Γρήγορη Επανάληψη</h3>' +
        '<ul class="bullet-list">' + unit.sos_points.map((s) => '<li>' + formatRichText(s) + '</li>').join('') + '</ul>' +
      '</div></section>';

      html += this.buildLessonNavBar(unit_id);
      html += '</div>';

      main_el.innerHTML = html;

      // Binds chapter Prev/Next and jump links.
      const nav_jump_btns = main_el.querySelectorAll('[data-nav-jump]');
      for (let i = 0; i < nav_jump_btns.length; i += 1) {
        nav_jump_btns[i].addEventListener('click', (evt) => {
          this.navigate(evt.currentTarget.getAttribute('data-nav-jump'));
        });
      }

      const scroll_btns = main_el.querySelectorAll('[data-scroll-to]');
      for (let i = 0; i < scroll_btns.length; i += 1) {
        scroll_btns[i].addEventListener('click', (evt) => {
          const target_el = document.getElementById(evt.currentTarget.getAttribute('data-scroll-to'));
          if (target_el) {
            target_el.scrollIntoView({ behavior: 'smooth', block: 'start' });
          }
        });
      }

      this.bindAccordions(main_el);

      // Mounts Unit Lab.
      const lab_host = main_el.querySelector('#unit_lab_host');
      if (has_lab && lab_host) {
        this.labs[unit_id].mount(lab_host);
      }

      // Mounts Fill-in-the-blank exercises.
      const fill_host = main_el.querySelector('#unit_fill_host');
      if (fill_host) {
        this.renderFillExercises(fill_host, fill_items);
        const reset_fills_btn = main_el.querySelector('#btn_reset_fills');
        if (reset_fills_btn) {
          reset_fills_btn.addEventListener('click', () => {
            this.session.resetFillExercises(fill_items.map((item) => item.id));
            this.updateSessionHud();
            this.renderFillExercises(fill_host, fill_items);
          });
        }
      }

      // Mounts True/False drills.
      const tf_host = main_el.querySelector('#unit_tf_host');
      if (tf_host) {
        this.renderTrueFalseList(tf_host, unit_id, tf_items);
        const reset_tf_btn = main_el.querySelector('#btn_reset_tf');
        if (reset_tf_btn) {
          reset_tf_btn.addEventListener('click', () => {
            this.session.resetTfUnit(unit_id);
            this.updateSessionHud();
            this.renderTrueFalseList(tf_host, unit_id, tf_items);
          });
        }
      }

      // Mounts Unit MCQs.
      const drill_host = main_el.querySelector('#unit_drills_host');
      if (drill_host) {
        const renderUnitDrills = () => {
          this.renderQuestionList(drill_host, unit_drills, this.session.drill_answers, (q_id, opt_idx) => {
            const q_obj = unit_drills.find((item) => item.id === q_id);
            const is_ok = Boolean(q_obj && opt_idx === q_obj.correct_index);
            this.session.recordDrillAnswer(q_id, opt_idx, is_ok);
            this.updateSessionHud();
          });
        };
        renderUnitDrills();
        const reset_mcqs_btn = main_el.querySelector('#btn_reset_mcqs');
        if (reset_mcqs_btn) {
          reset_mcqs_btn.addEventListener('click', () => {
            this.session.resetDrills(unit_drills.map((q) => q.id));
            this.updateSessionHud();
            renderUnitDrills();
          });
        }
      }

      // Mounts Gamified Builder Game and Python Drop-In Puzzles.
      const handleGameComplete = (challenge_id) => {
        this.session.markGameCompleted(challenge_id);
        this.updateSessionHud();
      };
      const handleGameReset = (challenge_id) => {
        this.session.unmarkGameCompleted(challenge_id);
        this.updateSessionHud();
      };

      const builder_host = main_el.querySelector('#pg_builder_host');
      const builder_game = this.builder_games[unit_id];
      if (builder_host && builder_game && typeof builder_game.mount === 'function') {
        builder_game.mount(builder_host, handleGameComplete, handleGameReset);
      }

      const dropin_host = main_el.querySelector('#pg_dropin_host');
      if (dropin_host && this.dropin_engine) {
        this.dropin_engine.mount(dropin_host, unit_id, this.session.completed_games, handleGameComplete, handleGameReset);
      }
    }

    /**
     * Renders W3Schools-style interactive fill-in-the-blank exercises with Check, Hint, Reveal, and Reset.
     *
     * Args:
     *     host_el (HTMLElement): Container element for fill exercises.
     *     fill_items (Array<object>): Exercise definitions.
     */
    renderFillExercises(host_el, fill_items) {
      let html = '';
      for (let i = 0; i < fill_items.length; i += 1) {
        const item = fill_items[i];
        const state = this.session.fill_answers[item.id] || { value: '', is_correct: null, revealed: false, hint_shown: false };
        const status_cls = state.is_correct === true ? 'is-correct' : (state.is_correct === false ? 'is-wrong' : '');

        html += '<div class="fill-exercise-card ' + status_cls + '" data-fill-id="' + item.id + '">' +
          '<div><strong>#' + (i + 1) + '.</strong> ' + formatRichText(item.prompt) + '</div>' +
          '<div class="fill-input-row">' +
            '<input type="text" class="input-control" data-fill-input="' + item.id + '" placeholder="' + (item.placeholder || 'απάντηση') + '" value="' + String(state.value || '').replace(/"/g, '&quot;') + '" style="min-width:170px;">' +
            '<button type="button" class="btn btn-primary" data-fill-check="' + item.id + '">Έλεγχος</button>' +
            '<button type="button" class="btn btn-secondary" data-fill-hint="' + item.id + '">Υπόδειξη</button>' +
            '<button type="button" class="btn btn-secondary" data-fill-reveal="' + item.id + '">Λύση</button>' +
            '<button type="button" class="btn btn-ghost" data-fill-reset="' + item.id + '">Επαναφορά</button>' +
          '</div>';

        if (state.hint_shown) {
          html += '<div class="quiz-feedback"><div><strong>Υπόδειξη:</strong> ' + formatRichText(item.hint) + '</div></div>';
        }
        if (state.revealed) {
          html += '<div class="quiz-feedback"><div><strong>Αποδεκτή Λύση:</strong> <code>' + formatRichText(item.expected[0]) + '</code> — ' + formatRichText(item.explanation) + '</div></div>';
        } else if (state.is_correct === true) {
          html += '<div class="quiz-feedback is-correct">' +
            '<div class="feedback-badge">' + this.icons.getIcon('check', 16) + '<span>Σωστά! (+10 πόντοι)</span></div>' +
            '<div>' + formatRichText(item.explanation) + '</div></div>';
        } else if (state.is_correct === false) {
          html += '<div class="quiz-feedback is-wrong">' +
            '<div class="feedback-badge">' + this.icons.getIcon('alert', 16) + '<span>Προσπάθησε ξανά</span></div>' +
            '<div>Δες την υπόδειξη ή έλεγξε τους τύπους της θεωρίας.</div></div>';
        }
        html += '</div>';
      }

      host_el.innerHTML = html;

      const submitAnswer = (fill_id) => {
        const item = fill_items.find((x) => x.id === fill_id);
        const input_el = host_el.querySelector('[data-fill-input="' + fill_id + '"]');
        if (!item || !input_el) {
          return;
        }
        const raw_val = input_el.value;
        const norm_val = normalizeAnswer(raw_val);
        const is_ok = norm_val.length > 0 && item.expected.some((exp) => normalizeAnswer(exp) === norm_val);
        this.session.recordFillResult(fill_id, raw_val, is_ok);
        this.updateSessionHud();
        this.renderFillExercises(host_el, fill_items);
      };

      const check_btns = host_el.querySelectorAll('[data-fill-check]');
      for (let i = 0; i < check_btns.length; i += 1) {
        check_btns[i].addEventListener('click', (evt) => {
          submitAnswer(evt.currentTarget.getAttribute('data-fill-check'));
        });
      }

      const inputs = host_el.querySelectorAll('[data-fill-input]');
      for (let i = 0; i < inputs.length; i += 1) {
        inputs[i].addEventListener('keydown', (evt) => {
          if (evt.key === 'Enter') {
            evt.preventDefault();
            submitAnswer(evt.currentTarget.getAttribute('data-fill-input'));
          }
        });
      }

      const hint_btns = host_el.querySelectorAll('[data-fill-hint]');
      for (let i = 0; i < hint_btns.length; i += 1) {
        hint_btns[i].addEventListener('click', (evt) => {
          const fid = evt.currentTarget.getAttribute('data-fill-hint');
          const input_el = host_el.querySelector('[data-fill-input="' + fid + '"]');
          if (input_el && this.session.fill_answers[fid]) {
            this.session.fill_answers[fid].value = input_el.value;
          }
          this.session.toggleFillHint(fid);
          this.renderFillExercises(host_el, fill_items);
        });
      }

      const reveal_btns = host_el.querySelectorAll('[data-fill-reveal]');
      for (let i = 0; i < reveal_btns.length; i += 1) {
        reveal_btns[i].addEventListener('click', (evt) => {
          const fid = evt.currentTarget.getAttribute('data-fill-reveal');
          this.session.revealFillSolution(fid);
          this.renderFillExercises(host_el, fill_items);
        });
      }

      const reset_btns = host_el.querySelectorAll('[data-fill-reset]');
      for (let i = 0; i < reset_btns.length; i += 1) {
        reset_btns[i].addEventListener('click', (evt) => {
          const fid = evt.currentTarget.getAttribute('data-fill-reset');
          this.session.resetFillExercises([fid]);
          this.updateSessionHud();
          this.renderFillExercises(host_el, fill_items);
        });
      }
    }

    /**
     * Renders rapid-fire True/False statements with immediate explanation feedback.
     *
     * Args:
     *     host_el (HTMLElement): Host container for True/False rows.
     *     unit_id (string): Unit identifier ('prereq', '00'..'07').
     *     tf_items (Array<object>): List of { statement, answer, explanation } objects.
     */
    renderTrueFalseList(host_el, unit_id, tf_items) {
      let html = '';
      for (let i = 0; i < tf_items.length; i += 1) {
        const item = tf_items[i];
        const tf_key = 'tf_' + unit_id + '_' + i;
        const chosen = this.session.tf_answers[tf_key];
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
          (has_ans ? '<div class="muted-text" style="font-size:0.9rem;">' + formatRichText(item.explanation) + '</div>' : '') +
        '</div>';
      }
      host_el.innerHTML = html;

      const btns = host_el.querySelectorAll('[data-tf-val]');
      for (let i = 0; i < btns.length; i += 1) {
        btns[i].addEventListener('click', (evt) => {
          const row = evt.currentTarget.closest('[data-tf-idx]');
          const idx = Number(row.getAttribute('data-tf-idx'));
          const val = evt.currentTarget.getAttribute('data-tf-val') === 'true';
          const is_ok = tf_items[idx] && val === tf_items[idx].answer;
          this.session.recordTfAnswer('tf_' + unit_id + '_' + idx, val, is_ok);
          this.updateSessionHud();
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
     * Renders an interactive list of multiple-choice questions with instant Editorial Paper feedback.
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
            '<span class="meta-pill">' + (q.unit_id === 'prereq' ? 'Προαπαιτούμενα' : 'Ενότητα ' + q.unit_id) + ' | #' + (i + 1) + '</span>' +
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

      let unit_opts = '<option value="all">Όλες οι ενότητες (00–07 &amp; Βασικά)</option>';
      for (let i = 0; i < this.chapter_order.length; i += 1) {
        const uid = this.chapter_order[i];
        unit_opts += '<option value="' + uid + '" ' + (this.quiz_engine.selected_unit === uid ? 'selected' : '') + '>' + this.chapter_labels[uid] + '</option>';
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
            '<span class="array-cell-idx">' + uk + '</span>' +
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
