"""Mock Exam 5 (Gotchas) scenario module for Discrete Mathematics.

Transcribes Mock Exam 5 verbatim with interactive highlights, and provides
step-by-step master solutions across Groups A, B, C, D for all 3 questions.
"""

from models.scenario import (
    Scenario,
    Paragraph,
    TextSegment,
    ExamQuestion,
    CalculationStep,
    DiagramNode,
    DiagramEdge,
    DesignJustification,
)


def createMockExam5GotchasScenario() -> Scenario:
    """Constructs the Scenario instance for Mock Exam 5 (Gotchas).

    Returns:
        Scenario: Complete scenario with verbatim text, annotations, and worked solutions.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="Τμήμα Πληροφορικής και Τηλεπικοινωνιών — Πανεπιστήμιο Ιωαννίνων\n"),
                TextSegment(text="Σπυρίδων Τζίμας • Εαρινό Εξάμηνο 2025\n"),
                TextSegment(text="203: Διακριτά Μαθηματικά — Εικονική Εξέταση 5 (Με Παγίδες)\n\n"),
                TextSegment(text="Η βαθμολογική αξία της εξέτασης είναι 10 μονάδες. Η χρονική διάρκεια είναι 3 ώρες. "),
                TextSegment(text="Επιτρέπεται στυλό μόνο μπλε και μαύρου χρώματος. Επιτρέπεται μολύβι μόνο για γραφή στο πρόχειρο. Καλή Επιτυχία!"),
            ]
        ),
        Paragraph(
            accent_border_color="var(--blue-action)",
            segments=[
                TextSegment(text="Θέμα 1. (3 μονάδες) ", is_highlight=True, category="set", tag_label="Q1-SUBSETS-GOTCHA", badge_class="badge-set", tooltip="Classification: Subsets, Power Sets & Truth Values\nDetection Clue: 'Αν A ⊆ B ∪ C τότε... Το κενό σύνολο ∅ είναι στοιχείο του δυναμοσυνόλου P(?)'\nApplication Rationale: Clarifies subtle differences between membership ∈ and subset ⊆, plus counterexample construction"),
                TextSegment(text="Προσδιορίστε αν οι ακόλουθες προτάσεις είναι Αληθείς ή Ψευδείς και αιτιολογήστε την απάντησή σας:\n\n"),
                TextSegment(text="α'. (1.5 μονάδα) Αν A ⊆ B ∪ C, τότε απαραίτητα (A ⊆ B) ή (A ⊆ C).\n"),
                TextSegment(text="β'. (1.5 μονάδα) Το κενό σύνολο ∅ είναι στοιχείο του δυναμοσυνόλου P((?)).\n\n"),
                TextSegment(text="Ομάδα Α: (?) = ∅ | Ομάδα Β: (?) = {∅} | Ομάδα Γ: (?) = {1, 2} | Ομάδα Δ: (?) = {{∅}}\n"),
                TextSegment(text="(Παγίδα: Διακρίνετε σωστά το «ανήκει» (∈) από το «υποσύνολο» (⊆))."),
            ]
        ),
        Paragraph(
            accent_border_color="var(--accent)",
            segments=[
                TextSegment(text="Θέμα 2. (4 μονάδες) ", is_highlight=True, category="automata", tag_label="Q2-NFA-TO-DFA", badge_class="badge-automata", tooltip="Classification: NFA to DFA Subset Construction Algorithm\nDetection Clue: 'NFA που αναγνωρίζει τη γλώσσα L = (0 ∪ 1)*(?)(0 ∪ 1)*... ισοδύναμο DFA'\nApplication Rationale: Converts non-deterministic transitions into equivalent deterministic power-set states"),
                TextSegment(text="Θεωρήστε το Μη-Ντετερμινιστικό Πεπερασμένο Αυτόματο (NFA) N που αναγνωρίζει τη γλώσσα L = (0 ∪ 1)*(?)(0 ∪ 1)*. "),
                TextSegment(text="Μετατρέψτε το σε ισοδύναμο DFA χρησιμοποιώντας τον αλγόριθμο κατασκευής υποσυνόλων.\n\n"),
                TextSegment(text="Ομάδα Α: (?) = 00 | Ομάδα Β: (?) = 11 | Ομάδα Γ: (?) = 01 | Ομάδα Δ: (?) = 10\n\n"),
                TextSegment(text="Πόσες καταστάσεις έχει το ελάχιστο DFA που προκύπτει;"),
            ]
        ),
        Paragraph(
            accent_border_color="var(--purple)",
            segments=[
                TextSegment(text="Θέμα 3. (3 μονάδες) ", is_highlight=True, category="logic", tag_label="Q3-COMPOSITION", badge_class="badge-logic", tooltip="Classification: Function Composition Properties (Injectivity/Surjectivity)\nDetection Clue: 'συνάρτηση f: A → B και g: B → C... σύνθεση g ∘ f είναι (?)...'\nApplication Rationale: Identifies which property is strictly inherited (if g ∘ f is 1-1 => f is 1-1, if onto => g is onto) with counterexamples"),
                TextSegment(text="Έχουμε μία συνάρτηση f: A → B και μία g: B → C. Αν η σύνθεση g ∘ f είναι (?), τι μπορούμε να συμπεράνουμε με βεβαιότητα για τις f και g;\n\n"),
                TextSegment(text="Ομάδα Α: (?) = αμφιμονότιμη (1-1, injective)\n"),
                TextSegment(text="Ομάδα Β: (?) = επί (surjective)\n"),
                TextSegment(text="Ομάδα Γ: (?) = αμφιμονότιμη ΚΑΙ η f είναι επί\n"),
                TextSegment(text="Ομάδα Δ: (?) = επί ΚΑΙ η g είναι αμφιμονότιμη\n\n"),
                TextSegment(text="Δώστε ένα αντιπαράδειγμα για την ιδιότητα που ΔΕΝ κληρονομείται υποχρεωτικά."),
            ]
        ),
    ]

    questions = [
        # QUESTION 1
        ExamQuestion(
            question_number=1,
            title="Παγίδες Θεωρίας Συνόλων: Υποσύνολα vs Στοιχεία Δυναμοσυνόλου",
            question_type="Θεωρία Συνόλων",
            prompt_text=(
                "Προσδιορίστε αν οι ακόλουθες προτάσεις είναι Αληθείς ή Ψευδείς και αιτιολογήστε:\n\n"
                "**α'. (1.5 μονάδα)** Αν $A \\subseteq B \\cup C$, τότε απαραίτητα $(A \\subseteq B)$ ή $(A \\subseteq C)$.\n\n"
                "**β'. (1.5 μονάδα)** Το κενό σύνολο $\\emptyset$ είναι στοιχείο του δυναμοσυνόλου $P((?))$.\n"
                "- **Ομάδα Α:** $(?) = \\emptyset$\n"
                "- **Ομάδα Β:** $(?) = \\{\\emptyset\\}$\n"
                "- **Ομάδα Γ:** $(?) = \\{1, 2\\}$\n"
                "- **Ομάδα Δ:** $(?) = \\{\\{\\emptyset\\}\\}$"
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ερώτημα α' — Ανάλυση Πρότασης A ⊆ B ∪ C",
                    formula=r"\text{Πρόταση: } A \subseteq B \cup C \implies (A \subseteq B) \lor (A \subseteq C)",
                    substitution=(
                        r"\text{Αντιπαράδειγμα: } B = \{1\}, \ C = \{2\}, \ A = \{1, 2\}. \\ "
                        r"B \cup C = \{1, 2\} \implies A \subseteq B \cup C \ (\checkmark). \\ "
                        r"\text{Όμως: } A \not\subseteq B \ (2 \notin B) \quad \text{και} \quad A \not\subseteq C \ (1 \notin C)."
                    ),
                    result=r"\mathbf{ΨΕΥΔΗΣ} \text{ (False) — Καταρρίπτεται με αντιπαράδειγμα}",
                    rationale="Ένα σύνολο A μπορεί να 'γεφυρώνει' δύο σύνολα B και C έχοντας στοιχεία και στα δύο χωρίς να περιέχεται εξ ολοκλήρου σε κανένα.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ερώτημα β' — Το ∅ ως στοιχείο του P(?) για όλες τις Ομάδες",
                    formula=r"\forall X, \ \emptyset \subseteq X \iff \emptyset \in P(X)",
                    substitution=(
                        r"\text{Εξ ορισμού, το δυναμοσύνολο } P(X) \text{ είναι το σύνολο ΟΛΩΝ των υποσυνόλων του } X. \\ "
                        r"\text{Επειδή το κενό σύνολο } \emptyset \text{ είναι υποσύνολο ΚΑΘΕ συνόλου } X \ (\emptyset \subseteq X), \\ "
                        r"\text{έπεται υποχρεωτικά ότι } \emptyset \in P(X) \text{ για ΟΠΟΙΟΔΗΠΟΤΕ σύνολο } X! \\ "
                        r"\text{Συνεπώς: } \emptyset \in P(\emptyset), \ \emptyset \in P(\{\emptyset\}), \ \emptyset \in P(\{1,2\}), \ \emptyset \in P(\{\{\emptyset\}\}) \implies \mathbf{ΠΑΝΤΑ \ ΑΛΗΘΕΣ}."
                    ),
                    result=r"\mathbf{ΑΛΗΘΗΣ} \text{ (True) για ΟΛΕΣ τις Ομάδες Α, Β, Γ, Δ}",
                    rationale="Η παγίδα βασίζεται στη σύγχυση του ∅ ως στοιχείου έναντι υποσυνόλου. Στο δυναμοσύνολο, κάθε υποσύνολο του X γίνεται στοιχείο του P(X).",
                ),
            ],
            final_answer="α': Ψευδής (με αντιπαράδειγμα A={1,2}, B={1}, C={2})\nβ': Αληθής για ΟΛΕΣ τις Ομάδες (Α, Β, Γ, Δ) αφού ∅ ⊆ X ισχύει για κάθε X, άρα ∅ ∈ P(X) πάντα",
            detailed_justification="Το ερώτημα β' αποτελεί χαρακτηριστική παγίδα εξετάσεων: ανεξάρτητα από το ποιο σύνολο (?) δίνεται (είτε είναι το ∅, είτε το {∅}, είτε το {1,2}), το κενό σύνολο ∅ είναι πάντα υποσύνολό του, και επομένως ανήκει πάντα στο δυναμοσύνολό του.",
            common_pitfalls=[
                "Στο β', πολλοί απαντούν ψευδές για το P(∅) νομίζοντας ότι είναι κενό. Το P(∅) = {∅}, δηλαδή έχει 1 στοιχείο: το ∅!",
            ],
            related_theory_topic="Δυναμοσύνολα & Θεωρία Συνόλων",
        ),

        # QUESTION 2
        ExamQuestion(
            question_number=2,
            title="Κατασκευή Υποσυνόλων (NFA σε DFA) για L = (0 ∪ 1)*(?)(0 ∪ 1)*",
            question_type="Αυτόματα & Τυπικές Γλώσσες",
            prompt_text=(
                "Θεωρήστε το NFA που αναγνωρίζει τη γλώσσα $L = (0 \\cup 1)^*(?)(0 \\cup 1)^*$.\n"
                "Μετατρέψτε το σε ισοδύναμο DFA με κατασκευή υποσυνόλων:\n\n"
                "- **Ομάδα Α:** $(?) = 00$\n"
                "- **Ομάδα Β:** $(?) = 11$\n"
                "- **Ομάδα Γ:** $(?) = 01$\n"
                "- **Ομάδα Δ:** $(?) = 10$\n\n"
                "Πόσες καταστάσεις έχει το ελάχιστο DFA που προκύπτει;"
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ομάδα Α — Γλώσσα L = (0 ∪ 1)* 00 (0 ∪ 1)* (Περιέχει 00)",
                    formula=r"\text{Καταστάσεις NFA: } \{q_0, q_1, q_2\} \text{ με } q_2 \text{ τελική}",
                    substitution=(
                        r"\text{Κατάσταση DFA } A = \{q_0\} \text{ (αρχική)}: \delta(A, 0) = \{q_0, q_1\} = B, \ \delta(A, 1) = \{q_0\} = A. \\ "
                        r"\text{Κατάσταση DFA } B = \{q_0, q_1\}: \delta(B, 0) = \{q_0, q_1, q_2\} = C \text{ (αποδεκτή)}, \ \delta(B, 1) = \{q_0\} = A. \\ "
                        r"\text{Κατάσταση DFA } C = \{q_0, q_1, q_2\}: \delta(C, 0) = \{q_0, q_1, q_2\} = C, \ \delta(C, 1) = \{q_0, q_2\} \equiv C."
                    ),
                    result=r"\text{Το ελάχιστο DFA έχει ακριβώς } \mathbf{3} \text{ καταστάσεις}",
                    rationale="Κατάσταση 1: κανένα πρόσφατο 0. Κατάσταση 2: τελευταίο σύμβολο 0. Κατάσταση 3: εντοπίστηκε 00 (παγίδα αποδοχής).",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ομάδες Β, Γ, Δ — Αποτελέσματα Ελαχιστοποίησης",
                    formula=r"\text{Μήκος υποσυμβολοσειράς } k = 2",
                    substitution=(
                        r"\text{Για κάθε υποσυμβολοσειρά μήκους 2 (00, 11, 01, 10), το ελάχιστο DFA απαιτεί: } \\ "
                        r"1. \text{Αρχική κατάσταση (πρόθεμα μήκους 0)} \\ "
                        r"2. \text{Ενδιάμεση κατάσταση (αντιστοιχεί στο πρώτο σύμβολο)} \\ "
                        r"3. \text{Τελική κατάσταση (εντοπίστηκε η λέξη, παραμονή με 0, 1)} \implies \mathbf{3} \text{ καταστάσεις}."
                    ),
                    result=r"\text{Όλες οι ομάδες καταλήγουν σε ελάχιστο DFA με } \mathbf{3} \text{ καταστάσεις}",
                    rationale="Όλες οι κατασκευές υποσυνόλων παράγουν είτε 3 είτε 4 καταστάσεις, όπου η 4η συγχωνεύεται ως ισοδύναμη με την τελική.",
                ),
            ],
            final_answer="Το ελάχιστο DFA έχει ακριβώς 3 καταστάσεις για όλες τις Ομάδες (Α, Β, Γ, Δ).",
            detailed_justification="Η γλώσσα απαιτεί την αναγνώριση οποιασδήποτε λέξης περιέχει μια συγκεκριμένη υποσυμβολοσειρά μήκους 2. Μετά την πρώτη εμφάνιση της υποσυμβολοσειράς, το αυτόματο εισέρχεται σε μία τελική κατάσταση παγίδα (sink accept state).",
            common_pitfalls=[
                "Διατήρηση μη προσβάσιμων ή ισοδύναμων καταστάσεων: Χωρίς ελαχιστοποίηση ο αλγόριθμος μπορεί να δείχνει 4 καταστάσεις, αλλά οι 2 τελικές καταστάσεις είναι ισοδύναμες.",
            ],
            related_theory_topic="Κατασκευή Υποσυνόλων & Ελαχιστοποίηση DFA",
        ),

        # QUESTION 3
        ExamQuestion(
            question_number=3,
            title="Ιδιότητες Σύνθεσης Συναρτήσεων g ∘ f (1-1 και Επί)",
            question_type="Σχέσεις & Συναρτήσεις",
            prompt_text=(
                "Έχουμε συναρτήσεις $f: A \\to B$ και $g: B \\to C$.\n\n"
                "Αν η σύνθεση $g \\circ f$ είναι (?):\n"
                "- **Ομάδα Α:** $(?) = $ αμφιμονότιμη (1-1, injective)\n"
                "- **Ομάδα Β:** $(?) = $ επί (surjective)\n"
                "- **Ομάδα Γ:** $(?) = $ αμφιμονότιμη ΚΑΙ η $f$ είναι επί\n"
                "- **Ομάδα Δ:** $(?) = $ επί ΚΑΙ η $g$ είναι αμφιμονότιμη\n\n"
                "Τι συμπεραίνουμε με βεβαιότητα για τις $f$ και $g$; Δώστε αντιπαράδειγμα για την ιδιότητα που ΔΕΝ ισχύει υποχρεωτικά."
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ομάδα Α — g ∘ f είναι 1-1",
                    formula=r"(g \circ f)(x) = (g \circ f)(y) \implies x = y",
                    substitution=(
                        r"\text{Συμπέρασμα: Η } f \text{ είναι υποχρεωτικά 1-1. Η } g \text{ ΔΕΝ είναι απαραίτητα 1-1.} \\ "
                        r"\text{Απόδειξη: Έστω } f(x) = f(y) \implies g(f(x)) = g(f(y)) \implies (g \circ f)(x) = (g \circ f)(y) \implies x = y. \\ "
                        r"\text{Αντιπαράδειγμα για } g: A=\{1\}, B=\{a, b\}, C=\{c\}, f(1)=a, g(a)=c, g(b)=c. "
                        r"g \circ f: 1 \mapsto c \text{ (1-1), αλλά η } g \text{ δεν είναι 1-1 (g(a)=g(b)).}"
                    ),
                    result=r"f \text{ είναι υποχρεωτικά 1-1} \mid g \text{ μπορεί να ΜΗΝ είναι 1-1}",
                    rationale="Η εσωτερική συνάρτηση f πρέπει να διατηρεί τη μοναδικότητα. Η εξωτερική g αρκεί να είναι 1-1 μόνο πάνω στην εικόνα f(A).",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ομάδα Β — g ∘ f είναι επί",
                    formula=r"\forall c \in C, \ \exists a \in A: (g \circ f)(a) = c",
                    substitution=(
                        r"\text{Συμπέρασμα: Η } g \text{ είναι υποχρεωτικά επί. Η } f \text{ ΔΕΝ είναι απαραίτητα επί.} \\ "
                        r"\text{Απόδειξη: } c = g(f(a)) = g(b) \text{ όπου } b = f(a) \in B \implies \forall c \in C \ \exists b \in B: g(b) = c. \\ "
                        r"\text{Αντιπαράδειγμα για } f: A=\{1\}, B=\{a, b\}, C=\{c\}, f(1)=a, g(a)=c, g(b)=c. "
                        r"g \circ f \text{ είναι επί, αλλά η } f \text{ δεν είναι επί (το } b \notin f(A))."
                    ),
                    result=r"g \text{ είναι υποχρεωτικά επί} \mid f \text{ μπορεί να ΜΗΝ είναι επί}",
                    rationale="Η εξωτερική συνάρτηση g καλύπτει όλο το C. Η εσωτερική f δεν χρειάζεται να καλύπτει όλο το B.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Ομάδες Γ & Δ — Επιπλέον Συνθήκες",
                    formula=r"\text{Ομάδα Γ: } g \circ f \text{ 1-1 και } f \text{ επί} \implies f \text{ αμφιμονοσήμαντη} \implies g = (g \circ f) \circ f^{-1} \text{ είναι 1-1}",
                    substitution=(
                        r"\text{Ομάδα Γ: } \mathbf{ΚΑΙ οι δύο } f \text{ και } g \text{ είναι 1-1!} \\ "
                        r"\text{Ομάδα Δ: } g \circ f \text{ επί και } g \text{ 1-1} \implies g \text{ αμφιμονοσήμαντη} \implies f = g^{-1} \circ (g \circ f) \implies \mathbf{ΚΑΙ οι δύο επί!}"
                    ),
                    result=r"\text{Ομάδα Γ: ΚΑΙ οι δύο 1-1} \mid \text{Ομάδα Δ: ΚΑΙ οι δύο επί}",
                    rationale="Όταν η μία συνάρτηση είναι αμφιμονοσήμαντη, επιτρέπει την αντιστροφή της και μεταβιβάζει την ιδιότητα στην άλλη.",
                ),
            ],
            final_answer="Ομάδα Α: Η f είναι υποχρεωτικά 1-1 (η g όχι απαραίτητα)\nΟμάδα Β: Η g είναι υποχρεωτικά επί (η f όχι απαραίτητα)\nΟμάδα Γ: Και οι δύο f και g είναι 1-1\nΟμάδα Δ: Και οι δύο f και g είναι επί",
            detailed_justification="Θεμελιώδες θεώρημα σύνθεσης: g ∘ f injective ⇒ f injective. g ∘ f surjective ⇒ g surjective. Τα αντιπαραδείγματα βασίζονται στο ότι το ενδιάμεσο σύνολο B μπορεί να είναι μεγαλύτερο από την εικόνα f(A).",
            common_pitfalls=[
                "Αντιστροφή ρόλων: Πολλοί γράφουν ότι 'η g είναι 1-1' (λάθος, μόνο η f είναι αναγκαστικά 1-1).",
            ],
            related_theory_topic="Συναρτήσεις, 1-1, Επί & Σύνθεση",
        ),
    ]

    diagram_nodes = [
        DiagramNode(id="A", label="A", node_type="state", x=120, y=160),
        DiagramNode(id="B", label="B", node_type="state", x=280, y=160),
        DiagramNode(id="C", label="C", node_type="state", x=440, y=160),
    ]

    diagram_edges = [
        DiagramEdge(source_id="A", target_id="B", label="f"),
        DiagramEdge(source_id="B", target_id="C", label="g"),
        DiagramEdge(source_id="A", target_id="C", label="g ∘ f", path_d="M 120 184 C 280 250, 280 250, 440 184", color="var(--accent)"),
    ]

    justifications = [
        DesignJustification(
            title="Θεμελιώδες Θεώρημα Σύνθεσης",
            category="Functions",
            description="Η σύνθεση διατηρεί τη μοναδικότητα από την είσοδο και την κάλυψη στην έξοδο.",
            rationale="Εξηγεί αυστηρά γιατί g ∘ f injective ⇒ f injective, και g ∘ f surjective ⇒ g surjective.",
        ),
    ]

    solution_code = '''# Verification Script for Mock Exam 5 (Course 203)

# Q1: Power Set Verification
def verify_empty_set_in_powerset():
    test_sets = [set(), {1, 2}, frozenset([frozenset()])]
    for s in test_sets:
        # Check if empty set is subset
        assert set().issubset(s), "Empty set must be subset of any set!"
    print("Mock Exam 5 - Q1: Empty set ∅ is subset of all test sets => always in P(S)!")

verify_empty_set_in_powerset()

# Q3: Function Composition Counterexamples
# A = {1}, B = {'a', 'b'}, C = {'c'}
# f(1) = 'a', g('a') = 'c', g('b') = 'c'
# g(f(1)) = 'c' => g ∘ f is 1-1 and onto
f = {1: 'a'}
g = {'a': 'c', 'b': 'c'}
g_circ_f = {x: g[f[x]] for x in f}

print("Mock Exam 5 - Q3 Counterexample:")
print(f"g ∘ f = {g_circ_f} (is 1-1 and onto C={{'c'}})")
print(f"f values: {list(f.values())} (is 1-1, but not onto B={{'a', 'b'}})")
print(f"g values: {list(g.values())} (is onto C, but not 1-1 since g('a')=g('b'))")
'''

    return Scenario(
        id="mock_exam_5_gotchas",
        title="Εικονική Εξέταση 5 (Με Παγίδες)",
        subtitle="203: Διακριτά Μαθηματικά — Δυναμοσύνολα, Κατασκευή Υποσυνόλων & Σύνθεση",
        course_tag="Εικονική Εξέταση",
        duration_info="3 Ώρες (10 Μονάδες)",
        paragraphs=paragraphs,
        questions=questions,
        diagram_nodes=diagram_nodes,
        diagram_edges=diagram_edges,
        justifications=justifications,
        solution_code=solution_code,
    )
