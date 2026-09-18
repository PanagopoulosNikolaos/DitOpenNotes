"""Past Exam Scenario: June 2025 Final Examination.

Full transcription and step-by-step mathematical solutions for Course 203:
Discrete Mathematics (June 2025), covering Groups A, B, C, and D.
"""

from models.scenario import Scenario, ExamExercise, GraphModel, GraphNode, GraphEdge, VennModel, InductionModel


def createPastExamJune2025() -> Scenario:
    """Constructs the June 2025 Final Exam scenario with all 9 themes and 4 groups.

    Returns:
        Scenario: Fully populated exam scenario.
    """
    exercises = [
        # THEME 1: Truth Tables
        ExamExercise(
            number=1,
            title="Προτασιακοί Τύποι & Πίνακες Αληθείας",
            points=2.0,
            topic="Προτασιακή Λογική (Propositional Logic)",
            statements={
                "Ομάδα Α": (
                    "Κατασκευάστε τον πίνακα αληθείας των ακόλουθων προτασιακών τύπων:<br/>"
                    "<b>α'. (1 μονάδα):</b> $((p \\to q) \\land (\\neg p \\to q)) \\to q$<br/>"
                    "<b>β'. (1 μονάδα):</b> $p \\to ((p \\to \\neg p) \\lor (p \\to q))$"
                ),
                "Ομάδα Β": (
                    "Κατασκευάστε τον πίνακα αληθείας των ακόλουθων προτασιακών τύπων:<br/>"
                    "<b>α'. (1 μονάδα):</b> $((p \\to q) \\land (\\neg q \\to q)) \\to q$<br/>"
                    "<b>β'. (1 μονάδα):</b> $p \\to ((p \\to \\neg q) \\lor (p \\to q))$"
                ),
                "Ομάδα Γ": (
                    "Κατασκευάστε τον πίνακα αληθείας των ακόλουθων προτασιακών τύπων:<br/>"
                    "<b>α'. (1 μονάδα):</b> $((p \\to q) \\land (\\top \\to q)) \\to q$<br/>"
                    "<b>β'. (1 μονάδα):</b> $p \\to ((p \\to \\top) \\lor (p \\to q))$"
                ),
                "Ομάδα Δ": (
                    "Κατασκευάστε τον πίνακα αληθείας των ακόλουθων προτασιακών τύπων:<br/>"
                    "<b>α'. (1 μονάδα):</b> $((p \\to q) \\land (\\bot \\to q)) \\to q$<br/>"
                    "<b>β'. (1 μονάδα):</b> $p \\to ((p \\to \\bot) \\lor (p \\to q))$"
                ),
            },
            steps={
                "Ομάδα Α": [
                    (
                        "<b>Επίλυση Ερωτήματος α':</b> $((p \\to q) \\land (\\neg p \\to q)) \\to q$<br/>"
                        "<div class=\"overflow-x-auto my-3\">"
                        "<table class=\"truth-table\">"
                        "<thead><tr>"
                        "<th>p</th><th>q</th><th>&not;p</th><th>p &rarr; q</th><th>&not;p &rarr; q</th><th>(p &rarr; q) &and; (&not;p &rarr; q)</th><th class=\"res-col\">((p &rarr; q) &and; (&not;p &rarr; q)) &rarr; q</th>"
                        "</tr></thead>"
                        "<tbody>"
                        "<tr><td>T</td><td>T</td><td class=\"val-false\">F</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-true res-col\">T</td></tr>"
                        "<tr><td>T</td><td>F</td><td class=\"val-false\">F</td><td class=\"val-false\">F</td><td class=\"val-true\">T</td><td class=\"val-false\">F</td><td class=\"val-true res-col\">T</td></tr>"
                        "<tr><td>F</td><td>T</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-true res-col\">T</td></tr>"
                        "<tr><td>F</td><td>F</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-false\">F</td><td class=\"val-false\">F</td><td class=\"val-true res-col\">T</td></tr>"
                        "</tbody></table></div>"
                        "<b>Συμπέρασμα:</b> Η τελική στήλη περιέχει μόνο την τιμή αληθείας <b>T</b> σε όλες τις γραμμές, συνεπώς ο τύπος είναι <b>Ταὐτολογία (Tautology)</b>."
                    ),
                    (
                        "<b>Επίλυση Ερωτήματος β':</b> $p \\to ((p \\to \\neg p) \\lor (p \\to q))$<br/>"
                        "<div class=\"overflow-x-auto my-3\">"
                        "<table class=\"truth-table\">"
                        "<thead><tr>"
                        "<th>p</th><th>q</th><th>&not;p</th><th>p &rarr; &not;p</th><th>p &rarr; q</th><th>(p &rarr; &not;p) &or; (p &rarr; q)</th><th class=\"res-col\">p &rarr; ((p &rarr; &not;p) &or; (p &rarr; q))</th>"
                        "</tr></thead>"
                        "<tbody>"
                        "<tr><td>T</td><td>T</td><td class=\"val-false\">F</td><td class=\"val-false\">F</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-true res-col\">T</td></tr>"
                        "<tr><td>T</td><td>F</td><td class=\"val-false\">F</td><td class=\"val-false\">F</td><td class=\"val-false\">F</td><td class=\"val-false\">F</td><td class=\"val-false res-col\">F</td></tr>"
                        "<tr><td>F</td><td>T</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-true res-col\">T</td></tr>"
                        "<tr><td>F</td><td>F</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-true res-col\">T</td></tr>"
                        "</tbody></table></div>"
                        "<b>Συμπέρασμα:</b> Ο τύπος είναι <b>Ενδεχόμενος (Contingency)</b>, ισοδύναμος με τον απλό τύπο $p \\to q$ (λαμβάνει F αποκλειστικά όταν $p=T, q=F$)."
                    ),
                ],
                "Ομάδα Β": [
                    (
                        "<b>Επίλυση Ερωτήματος α' (AM: 3323):</b> $((p \\to q) \\land (\\neg q \\to q)) \\to q$<br/>"
                        "<div class=\"overflow-x-auto my-3\">"
                        "<table class=\"truth-table\">"
                        "<thead><tr>"
                        "<th>p</th><th>q</th><th>&not;q</th><th>p &rarr; q</th><th>&not;q &rarr; q</th><th>(p &rarr; q) &and; (&not;q &rarr; q)</th><th class=\"res-col\">((p &rarr; q) &and; (&not;q &rarr; q)) &rarr; q</th>"
                        "</tr></thead>"
                        "<tbody>"
                        "<tr><td>T</td><td>T</td><td class=\"val-false\">F</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-true res-col\">T</td></tr>"
                        "<tr><td>T</td><td>F</td><td class=\"val-true\">T</td><td class=\"val-false\">F</td><td class=\"val-false\">F</td><td class=\"val-false\">F</td><td class=\"val-true res-col\">T</td></tr>"
                        "<tr><td>F</td><td>T</td><td class=\"val-false\">F</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-true res-col\">T</td></tr>"
                        "<tr><td>F</td><td>F</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-false\">F</td><td class=\"val-false\">F</td><td class=\"val-true res-col\">T</td></tr>"
                        "</tbody></table></div>"
                        "<b>Αναλυτική Εξήγηση Στηλών:</b><br/>"
                        "1. $\\neg q \\to q$: Ψευδές μόνο όταν $\\neg q = T$ και $q = F$, δηλαδή όταν $q = F$. Συνεπώς $\\neg q \\to q \\equiv q$.<br/>"
                        "2. $(p \\to q) \\land q \\equiv q$ (απορρόφηση).<br/>"
                        "3. Τελική συνεπαγωγή $q \\to q \\equiv \\top$.<br/>"
                        "<b>Συμπέρασμα:</b> Όλες οι γραμμές της τελικής στήλης έχουν τιμή <b>T</b>, άρα ο προτασιακός τύπος είναι <b>Ταὐτολογία (Tautology)</b>."
                    ),
                    (
                        "<b>Επίλυση Ερωτήματος β' (AM: 3323):</b> $p \\to ((p \\to \\neg q) \\lor (p \\to q))$<br/>"
                        "<div class=\"overflow-x-auto my-3\">"
                        "<table class=\"truth-table\">"
                        "<thead><tr>"
                        "<th>p</th><th>q</th><th>&not;q</th><th>p &rarr; &not;q</th><th>p &rarr; q</th><th>(p &rarr; &not;q) &or; (p &rarr; q)</th><th class=\"res-col\">p &rarr; ((p &rarr; &not;q) &or; (p &rarr; q))</th>"
                        "</tr></thead>"
                        "<tbody>"
                        "<tr><td>T</td><td>T</td><td class=\"val-false\">F</td><td class=\"val-false\">F</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-true res-col\">T</td></tr>"
                        "<tr><td>T</td><td>F</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-false\">F</td><td class=\"val-true\">T</td><td class=\"val-true res-col\">T</td></tr>"
                        "<tr><td>F</td><td>T</td><td class=\"val-false\">F</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-true res-col\">T</td></tr>"
                        "<tr><td>F</td><td>F</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-true res-col\">T</td></tr>"
                        "</tbody></table></div>"
                        "<b>Αναλυτική Εξήγηση Στηλών:</b><br/>"
                        "1. Η διάζευξη $(p \\to \\neg q) \\lor (p \\to q) \\equiv (\\neg p \\lor \\neg q) \\lor (\\neg p \\lor q) \\equiv \\neg p \\lor (\\neg q \\lor q) \\equiv \\neg p \\lor \\top \\equiv \\top$.<br/>"
                        "2. Συνεπώς, η τελική συνεπαγωγή $p \\to \\top \\equiv \\top$ είναι πάντοτε αληθής.<br/>"
                        "<b>Συμπέρασμα:</b> Όλες οι γραμμές της τελικής στήλης έχουν τιμή <b>T</b>, άρα ο προτασιακός τύπος είναι <b>Ταὐτολογία (Tautology)</b>."
                    ),
                ],
                "Ομάδα Γ": [
                    (
                        "<b>Επίλυση Ερωτήματος α':</b> $((p \\to q) \\land (\\top \\to q)) \\to q$<br/>"
                        "<div class=\"overflow-x-auto my-3\">"
                        "<table class=\"truth-table\">"
                        "<thead><tr>"
                        "<th>p</th><th>q</th><th>&top;</th><th>p &rarr; q</th><th>&top; &rarr; q</th><th>(p &rarr; q) &and; (&top; &rarr; q)</th><th class=\"res-col\">((p &rarr; q) &and; (&top; &rarr; q)) &rarr; q</th>"
                        "</tr></thead>"
                        "<tbody>"
                        "<tr><td>T</td><td>T</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-true res-col\">T</td></tr>"
                        "<tr><td>T</td><td>F</td><td class=\"val-true\">T</td><td class=\"val-false\">F</td><td class=\"val-false\">F</td><td class=\"val-false\">F</td><td class=\"val-true res-col\">T</td></tr>"
                        "<tr><td>F</td><td>T</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-true res-col\">T</td></tr>"
                        "<tr><td>F</td><td>F</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-false\">F</td><td class=\"val-false\">F</td><td class=\"val-true res-col\">T</td></tr>"
                        "</tbody></table></div>"
                        "<b>Συμπέρασμα:</b> Ο τύπος είναι <b>Ταὐτολογία (Tautology)</b>."
                    ),
                    (
                        "<b>Επίλυση Ερωτήματος β':</b> $p \\to ((p \\to \\top) \\lor (p \\to q))$<br/>"
                        "<div class=\"overflow-x-auto my-3\">"
                        "<table class=\"truth-table\">"
                        "<thead><tr>"
                        "<th>p</th><th>q</th><th>p &rarr; &top;</th><th>p &rarr; q</th><th>(p &rarr; &top;) &or; (p &rarr; q)</th><th class=\"res-col\">p &rarr; ((p &rarr; &top;) &or; (p &rarr; q))</th>"
                        "</tr></thead>"
                        "<tbody>"
                        "<tr><td>T</td><td>T</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-true res-col\">T</td></tr>"
                        "<tr><td>T</td><td>F</td><td class=\"val-true\">T</td><td class=\"val-false\">F</td><td class=\"val-true\">T</td><td class=\"val-true res-col\">T</td></tr>"
                        "<tr><td>F</td><td>T</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-true res-col\">T</td></tr>"
                        "<tr><td>F</td><td>F</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-true res-col\">T</td></tr>"
                        "</tbody></table></div>"
                        "<b>Συμπέρασμα:</b> Ο τύπος είναι <b>Ταὐτολογία (Tautology)</b>."
                    ),
                ],
                "Ομάδα Δ": [
                    (
                        "<b>Επίλυση Ερωτήματος α':</b> $((p \\to q) \\land (\\bot \\to q)) \\to q$<br/>"
                        "<div class=\"overflow-x-auto my-3\">"
                        "<table class=\"truth-table\">"
                        "<thead><tr>"
                        "<th>p</th><th>q</th><th>&bot;</th><th>p &rarr; q</th><th>&bot; &rarr; q</th><th>(p &rarr; q) &and; (&bot; &rarr; q)</th><th class=\"res-col\">((p &rarr; q) &and; (&bot; &rarr; q)) &rarr; q</th>"
                        "</tr></thead>"
                        "<tbody>"
                        "<tr><td>T</td><td>T</td><td class=\"val-false\">F</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-true res-col\">T</td></tr>"
                        "<tr><td>T</td><td>F</td><td class=\"val-false\">F</td><td class=\"val-false\">F</td><td class=\"val-true\">T</td><td class=\"val-false\">F</td><td class=\"val-true res-col\">T</td></tr>"
                        "<tr><td>F</td><td>T</td><td class=\"val-false\">F</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-true res-col\">T</td></tr>"
                        "<tr><td>F</td><td>F</td><td class=\"val-false\">F</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-false res-col\">F</td></tr>"
                        "</tbody></table></div>"
                        "<b>Συμπέρασμα:</b> Ο τύπος είναι <b>Ενδεχόμενος (Contingency)</b>, ισοδύναμος με $p \\lor q$ (Ψευδής όταν $p=F, q=F$)."
                    ),
                    (
                        "<b>Επίλυση Ερωτήματος β':</b> $p \\to ((p \\to \\bot) \\lor (p \\to q))$<br/>"
                        "<div class=\"overflow-x-auto my-3\">"
                        "<table class=\"truth-table\">"
                        "<thead><tr>"
                        "<th>p</th><th>q</th><th>p &rarr; &bot;</th><th>p &rarr; q</th><th>(p &rarr; &bot;) &or; (p &rarr; q)</th><th class=\"res-col\">p &rarr; ((p &rarr; &bot;) &or; (p &rarr; q))</th>"
                        "</tr></thead>"
                        "<tbody>"
                        "<tr><td>T</td><td>T</td><td class=\"val-false\">F</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-true res-col\">T</td></tr>"
                        "<tr><td>T</td><td>F</td><td class=\"val-false\">F</td><td class=\"val-false\">F</td><td class=\"val-false\">F</td><td class=\"val-false res-col\">F</td></tr>"
                        "<tr><td>F</td><td>T</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-true res-col\">T</td></tr>"
                        "<tr><td>F</td><td>F</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-true\">T</td><td class=\"val-true res-col\">T</td></tr>"
                        "</tbody></table></div>"
                        "<b>Συμπέρασμα:</b> Ο τύπος είναι <b>Ενδεχόμενος (Contingency)</b>, ισοδύναμος με $p \\to q$ (Ψευδής μόνο όταν $p=T, q=F$)."
                    ),
                ],
            },
            final_answers={
                "Ομάδα Α": "α'. Ταὐτολογία (T για όλες τις τιμές) | β'. Ενδεχόμενος (Ισοδύναμο με p -> q)",
                "Ομάδα Β": "α'. Ταὐτολογία (T για όλες τις τιμές) | β'. Ταὐτολογία (T για όλες τις τιμές)",
                "Ομάδα Γ": "α'. Ταὐτολογία (T για όλες τις τιμές) | β'. Ταὐτολογία (T για όλες τις τιμές)",
                "Ομάδα Δ": "α'. Ενδεχόμενος τύπος (ισοδύναμος με p v q) | β'. Ενδεχόμενος (ισοδύναμος με p -> q)",
            },
            pitfalls="Προσοχή: Τα σύμβολα T και F δεν είναι μεταβλητές, αλλά λογικές σταθερές. Στην Ομάδα Δ το α' ΔΕΝ είναι ταυτολογία (στη γραμμή F, F αποτιμάται σε F)!",
            interactive_type="truth_table",
        ),

        # THEME 2: Inclusion-Exclusion (PIE)
        ExamExercise(
            number=2,
            title="Αρχή Εγκλεισμού - Αποκλεισμού (PIE) & Σύνολα",
            points=1.0,
            topic="Θεωρία Συνόλων & Συνδυαστική",
            statements={
                "Ομάδα Α": "Έρευνα σε 256 άτομα για 3 χρώματα (R, G, B). |R|=169, |G|=100, |B|=64, |R∩G|=49, |G∩B|=36, |R∩B|=4, |R∩G∩B|=1. Υπολογίστε πόσοι δεν προτιμούν κανένα χρώμα.",
                "Ομάδα Β": "Έρευνα σε 256 άτομα για 3 χρώματα (R, G, B). |R|=169, |G|=100, |B|=64, |R∩G|=49, |G∩B|=36, |R∩B|=9, |R∩G∩B|=1. Υπολογίστε πόσοι δεν προτιμούν κανένα χρώμα.",
                "Ομάδα Γ": "Έρευνα σε 256 άτομα για 3 χρώματα (R, G, B). |R|=169, |G|=100, |B|=64, |R∩G|=49, |G∩B|=36, |R∩B|=16, |R∩G∩B|=1. Υπολογίστε πόσοι δεν προτιμούν κανένα χρώμα.",
                "Ομάδα Δ": "Έρευνα σε 256 άτομα για 3 χρώματα (R, G, B). |R|=169, |G|=100, |B|=64, |R∩G|=49, |G∩B|=36, |R∩B|=25, |R∩G∩B|=1. Υπολογίστε πόσοι δεν προτιμούν κανένα χρώμα.",
            },
            steps={
                "Ομάδα Α": [
                    "Εφαρμογή τύπου PIE: $|R \\cup G \\cup B| = |R| + |G| + |B| - (|R \\cap G| + |G \\cap B| + |R \\cap B|) + |R \\cap G \\cap B|$.",
                    "Αντικατάσταση: $|R \\cup G \\cup B| = 169 + 100 + 64 - (49 + 36 + 4) + 1 = 333 - 89 + 1 = 245$.",
                    "Συμπλήρωμα: $|(R \\cup G \\cup B)^c| = |\\Omega| - |R \\cup G \\cup B| = 256 - 245 = 11$ άτομα.",
                ],
                "Ομάδα Β": [
                    "Εφαρμογή τύπου PIE: $|R \\cup G \\cup B| = 169 + 100 + 64 - (49 + 36 + 9) + 1 = 333 - 94 + 1 = 240$.",
                    "Συμπλήρωμα: $256 - 240 = 16$ άτομα.",
                ],
                "Ομάδα Γ": [
                    "Εφαρμογή τύπου PIE: $|R \\cup G \\cup B| = 169 + 100 + 64 - (49 + 36 + 16) + 1 = 333 - 101 + 1 = 233$.",
                    "Συμπλήρωμα: $256 - 233 = 23$ άτομα.",
                ],
                "Ομάδα Δ": [
                    "Εφαρμογή τύπου PIE: $|R \\cup G \\cup B| = 169 + 100 + 64 - (49 + 36 + 25) + 1 = 333 - 110 + 1 = 224$.",
                    "Συμπλήρωμα: $256 - 224 = 32$ άτομα.",
                ],
            },
            final_answers={
                "Ομάδα Α": "11 συμμετέχοντες",
                "Ομάδα Β": "16 συμμετέχοντες",
                "Ομάδα Γ": "23 συμμετέχοντες",
                "Ομάδα Δ": "32 συμμετέχοντες",
            },
            pitfalls="Συχνό λάθος: Ξεχνιέται η πρόσθεση της τριπλής τομής στο τέλος του τύπου PIE (+ |R ∩ G ∩ B|).",
            interactive_type="venn",
        ),

        # THEME 3: Dice rolls & Primes
        ExamExercise(
            number=3,
            title="Πείραμα Ρίψης Διακεκριμένων Ζαριών",
            points=1.0,
            topic="Διακριτές Πιθανότητες & Απαρίθμηση",
            statements={
                "Ομάδα Α": "Ρίψη δύο διακεκριμένων d4. α'. Αποτελέσματα μορφής (άρτιος, περιττός), β'. Αποτελέσματα που αθροίζουν σε πρώτο αριθμό.",
                "Ομάδα Β": "Ρίψη δύο διακεκριμένων d8. α'. Αποτελέσματα μορφής (άρτιος, περιττός), β'. Αποτελέσματα που αθροίζουν σε πρώτο αριθμό.",
                "Ομάδα Γ": "Ρίψη δύο διακεκριμένων d12. α'. Αποτελέσματα μορφής (άρτιος, περιττός), β'. Αποτελέσματα που αθροίζουν σε πρώτο αριθμό.",
                "Ομάδα Δ": "Ρίψη δύο διακεκριμένων d20. α'. Αποτελέσματα μορφής (άρτιος, περιττός), β'. Αποτελέσματα που αθροίζουν σε πρώτο αριθμό.",
            },
            steps={
                "Ομάδα Α": [
                    "<b>Ερώτημα α':</b> Έδρες {1, 2, 3, 4}. Άρτιοι: {2, 4} (2 επιλογές), Περιττοί: {1, 3} (2 επιλογές). Πλήθος = $2 \\times 2 = 4$ ζεύγη: (2,1), (2,3), (4,1), (4,3).",
                    "<b>Ερώτημα β':</b> Πιθανά αθροίσματα από 2 έως 8. Πρώτοι αριθμοί $\\in \\{2, 3, 5, 7\\}$.",
                    "Άθροισμα 2: (1,1) [1]",
                    "Άθροισμα 3: (1,2), (2,1) [2]",
                    "Άθροισμα 5: (1,4), (2,3), (3,2), (4,1) [4]",
                    "Άθροισμα 7: (3,4), (4,3) [2]. Σύνολο = $1 + 2 + 4 + 2 = 9$ ζεύγη.",
                ],
                "Ομάδα Β": [
                    "<b>Ερώτημα α':</b> d8: 4 άρτιοι {2,4,6,8}, 4 περιττοί {1,3,5,7}. Πλήθος = $4 \\times 4 = 16$ αποτελέσματα.",
                    "<b>Ερώτημα β':</b> Πρώτα αθροίσματα $\\le 16$: {2, 3, 5, 7, 11, 13}. Καταμέτρηση ζευγών: 1 + 2 + 4 + 6 + 6 + 4 = 23 αποτελέσματα.",
                ],
                "Ομάδα Γ": [
                    "<b>Ερώτημα α':</b> d12: 6 άρτιοι, 6 περιττοί $\\implies 6 \\times 6 = 36$ αποτελέσματα.",
                    "<b>Ερώτημα β':</b> Πρώτα αθροίσματα $\\le 24$: {2, 3, 5, 7, 11, 13, 17, 19, 23}. Καταμέτρηση ζευγών = 51 αποτελέσματα.",
                ],
                "Ομάδα Δ": [
                    "<b>Ερώτημα α':</b> d20: 10 άρτιοι, 10 περιττοί $\\implies 10 \\times 10 = 100$ αποτελέσματα.",
                    "<b>Ερώτημα β':</b> Πρώτα αθροίσματα $\\le 40$: {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37}. Καταμέτρηση = 135 αποτελέσματα.",
                ],
            },
            final_answers={
                "Ομάδα Α": "α'. 4 ζεύγη, β'. 9 ζεύγη",
                "Ομάδα Β": "α'. 16 ζεύγη, β'. 23 ζεύγη",
                "Ομάδα Γ": "α'. 36 ζεύγη, β'. 51 ζεύγη",
                "Ομάδα Δ": "α'. 100 ζεύγη, β'. 135 ζεύγη",
            },
            pitfalls="Προσοχή: Τα ζάρια είναι διακεκριμένα, άρα το ζεύγος (1, 2) είναι διαφορετικό από το (2, 1)!",
        ),

        # THEME 4: Bayes Theorem
        ExamExercise(
            number=4,
            title="Θεώρημα Bayes & Εσφαλμένα Αρνητικά Αποτελέσματα",
            points=1.0,
            topic="Θεωρία Πιθανοτήτων (Probability & Bayes)",
            statements={
                "Ομάδα Α": "P(A)=1/2, P(B)=1/3, P(C)=1/6. False negative τεστ: 2% για A, 3% για B, 6% για C. α'. Πιθανότητα FN, β'. P(A|FN).",
                "Ομάδα Β": "P(A)=1/2, P(B)=1/3, P(C)=1/6. False negative τεστ: 2% για A, 3% για B, 12% για C. α'. Πιθανότητα FN, β'. P(A|FN).",
                "Ομάδα Γ": "P(A)=1/2, P(B)=1/3, P(C)=1/6. False negative τεστ: 2% για A, 3% για B, 18% για C. α'. Πιθανότητα FN, β'. P(A|FN).",
                "Ομάδα Δ": "P(A)=1/2, P(B)=1/3, P(C)=1/6. False negative τεστ: 2% για A, 3% για B, 24% για C. α'. Πιθανότητα FN, β'. P(A|FN).",
            },
            steps={
                "Ομάδα Α": [
                    "<b>Ερώτημα α' (Νόμος Ολικής Πιθανότητας):</b><br/>$$P(FN) = P(FN|A)P(A) + P(FN|B)P(B) + P(FN|C)P(C)$$",
                    "$$P(FN) = 0.02 \\cdot \\frac{1}{2} + 0.03 \\cdot \\frac{1}{3} + 0.06 \\cdot \\frac{1}{6} = 0.01 + 0.01 + 0.01 = 0.03 \\quad (3\\%)$$",
                    "<b>Ερώτημα β' (Θεώρημα Bayes):</b><br/>$$P(A|FN) = \\frac{P(FN|A)P(A)}{P(FN)} = \\frac{0.01}{0.03} = \\frac{1}{3} \\approx 33.33\\%$$",
                ],
                "Ομάδα Β": [
                    "$$P(FN) = 0.02(1/2) + 0.03(1/3) + 0.12(1/6) = 0.01 + 0.01 + 0.02 = 0.04 \\quad (4\\%)$$",
                    "$$P(A|FN) = \\frac{0.01}{0.04} = \\frac{1}{4} = 25\\%$$",
                ],
                "Ομάδα Γ": [
                    "$$P(FN) = 0.02(1/2) + 0.03(1/3) + 0.18(1/6) = 0.01 + 0.01 + 0.03 = 0.05 \\quad (5\\%)$$",
                    "$$P(A|FN) = \\frac{0.01}{0.05} = \\frac{1}{5} = 20\\%$$",
                ],
                "Ομάδα Δ": [
                    "$$P(FN) = 0.02(1/2) + 0.03(1/3) + 0.24(1/6) = 0.01 + 0.01 + 0.04 = 0.06 \\quad (6\\%)$$",
                    "$$P(A|FN) = \\frac{0.01}{0.06} = \\frac{1}{6} \\approx 16.67\\%$$",
                ],
            },
            final_answers={
                "Ομάδα Α": "α'. P(FN) = 0.03 (3%), β'. P(A|FN) = 1/3 (33.33%)",
                "Ομάδα Β": "α'. P(FN) = 0.04 (4%), β'. P(A|FN) = 1/4 (25.0%)",
                "Ομάδα Γ": "α'. P(FN) = 0.05 (5%), β'. P(A|FN) = 1/5 (20.0%)",
                "Ομάδα Δ": "α'. P(FN) = 0.06 (6%), β'. P(A|FN) = 1/6 (16.67%)",
            },
            pitfalls="Μην ξεχάσετε να μετατρέψετε τα ποσοστά σε δεκαδικούς αριθμούς κατά τον υπολογισμό (π.χ. 2% = 0.02).",
        ),

        # THEME 5: Relations & Properties
        ExamExercise(
            number=5,
            title="Έλεγχος Ιδιοτήτων Διμερών Σχέσεων",
            points=1.0,
            topic="Θεωρία Σχέσεων (Binary Relations)",
            statements={
                "Ομάδα Α": "S={1, 2, 3}, R={(1,1), (1,2), (2,1), (2,2), (3,3)}. Ελέγξτε: Ανακλαστική, Συμμετρική, Αντισυμμετρική, Μεταβατική.",
                "Ομάδα Β": "S={1, 2, 3}, R={(1,1), (1,2), (1,3), (2,2), (2,3), (3,3)}. Ελέγξτε: Ανακλαστική, Συμμετρική, Αντισυμμετρική, Μεταβατική.",
                "Ομάδα Γ": "S={1, 2, 3}, R={(1,1), (1,2), (2,3), (3,1), (3,3)}. Ελέγξτε: Ανακλαστική, Συμμετρική, Αντισυμμετρική, Μεταβατική.",
                "Ομάδα Δ": "S={1, 2, 3}, R={(1,1), (1,2), (2,1), (2,2), (2,3), (3,2)}. Ελέγξτε: Ανακλαστική, Συμμετρική, Αντισυμμετρική, Μεταβατική.",
            },
            steps={
                "Ομάδα Α": [
                    "<b>Ανακλαστική:</b> Περιέχει (1,1), (2,2), (3,3) $\\implies$ ΝΑΙ.",
                    "<b>Συμμετρική:</b> (1,2) $\\in R \\implies$ (2,1) $\\in R$. Όλα τα ζεύγη ικανοποιούνται $\\implies$ ΝΑΙ.",
                    "<b>Αντισυμμετρική:</b> Έχουμε (1,2) $\\in R$ και (2,1) $\\in R$ με $1 \\neq 2 \\implies$ ΟΧΙ.",
                    "<b>Μεταβατική:</b> (1,2) και (2,1) $\\implies$ (1,1) $\\in R$. (2,1) και (1,2) $\\implies$ (2,2) $\\in R$. Ισχύει $\\implies$ ΝΑΙ (Σχέση Ισοδυναμίας).",
                ],
                "Ομάδα Β": [
                    "<b>Ανακλαστική:</b> (1,1), (2,2), (3,3) $\\in R \\implies$ ΝΑΙ.",
                    "<b>Συμμετρική:</b> (1,2) $\\in R$ αλλά (2,1) $\\notin R \\implies$ ΟΧΙ.",
                    "<b>Αντισυμμετρική:</b> Δεν υπάρχει ζεύγος με $a \\neq b$ όπου και τα δύο $(a,b),(b,a) \\in R \\implies$ ΝΑΙ.",
                    "<b>Μεταβατική:</b> (1,2) και (2,3) $\\implies$ (1,3) $\\in R$. Ισχύει $\\implies$ ΝΑΙ (Μερική Διάταξη / Poset).",
                ],
                "Ομάδα Γ": [
                    "<b>Ανακλαστική:</b> (2,2) $\\notin R \\implies$ ΟΧΙ.",
                    "<b>Συμμετρική:</b> (1,2) $\\in R$ αλλά (2,1) $\\notin R \\implies$ ΟΧΙ.",
                    "<b>Αντισυμμετρική:</b> Κανένα αντίστροφο ζεύγος δεν συνυπάρχει $\\implies$ ΝΑΙ.",
                    "<b>Μεταβατική:</b> (1,2) και (2,3) $\\implies$ απαιτείται (1,3) $\\in R$, το οποίο ΔΕΝ υπάρχει $\\implies$ ΟΧΙ.",
                ],
                "Ομάδα Δ": [
                    "<b>Ανακλαστική:</b> (3,3) $\\notin R \\implies$ ΟΧΙ.",
                    "<b>Συμμετρική:</b> (1,2)<->(2,1) και (2,3)<->(3,2) $\\implies$ ΝΑΙ.",
                    "<b>Αντισυμμετρική:</b> (1,2) και (2,1) $\\implies$ ΟΧΙ.",
                    "<b>Μεταβατική:</b> (1,2) και (2,3) $\\implies$ απαιτεί (1,3) $\\in R$, που δεν υπάρχει $\\implies$ ΟΧΙ.",
                ],
            },
            final_answers={
                "Ομάδα Α": "Ανακλαστική: ΝΑΙ | Συμμετρική: ΝΑΙ | Αντισυμμετρική: ΟΧΙ | Μεταβατική: ΝΑΙ (Σχέση Ισοδυναμίας)",
                "Ομάδα Β": "Ανακλαστική: ΝΑΙ | Συμμετρική: ΟΧΙ | Αντισυμμετρική: ΝΑΙ | Μεταβατική: ΝΑΙ (Μερική Διάταξη)",
                "Ομάδα Γ": "Ανακλαστική: ΟΧΙ | Συμμετρική: ΟΧΙ | Αντισυμμετρική: ΝΑΙ | Μεταβατική: ΟΧΙ",
                "Ομάδα Δ": "Ανακλαστική: ΟΧΙ | Συμμετρική: ΝΑΙ | Αντισυμμετρική: ΟΧΙ | Μεταβατική: ΟΧΙ",
            },
            pitfalls="Συχνή παρανόηση: Μία σχέση μπορεί να ΜΗΝ είναι ούτε συμμετρική ούτε αντισυμμετρική, ή να είναι και τα δύο (αν είναι κενή ή περιέχει μόνο διαγώνια στοιχεία).",
        ),

        # THEME 6: Graph Isomorphism & Planarity
        ExamExercise(
            number=6,
            title="Ισομορφισμός Γραφημάτων & Τύπος Euler",
            points=2.0,
            topic="Θεωρία Γραφημάτων (Graph Theory)",
            statements={
                "Ομάδα Α": "G1 με V1={A..F}, E1 8 ακμές (περιέχει {B,E}). G2 με V2={1..6}, E2 8 ακμές. α'. Δείξτε αν G1 ~ G2, β'. Δείξτε ότι G1 είναι επίπεδο και επαληθεύστε τον τύπο Euler.",
                "Ομάδα Β": "G1 με V1={A..F}, E1 8 ακμές (περιέχει {B,F}). G2 με V2={1..6}, E2 8 ακμές. α'. Δείξτε αν G1 ~ G2, β'. Δείξτε ότι G1 είναι επίπεδο και επαληθεύστε τον τύπο Euler.",
                "Ομάδα Γ": "G1 με V1={A..F}, E1 8 ακμές (περιέχει {C,E}). G2 με V2={1..6}, E2 8 ακμές. α'. Δείξτε αν G1 ~ G2, β'. Δείξτε ότι G1 είναι επίπεδο και επαληθεύστε τον τύπο Euler.",
                "Ομάδα Δ": "G1 με V1={A..F}, E1 8 ακμές (περιέχει {C,F}). G2 με V2={1..6}, E2 8 ακμές. α'. Δείξτε αν G1 ~ G2, β'. Δείξτε ότι G1 είναι επίπεδο και επαληθεύστε τον τύπο Euler.",
            },
            steps={
                "Ομάδα Α": [
                    "<b>Ερώτημα α' (Ισομορφισμός):</b><br/>"
                    "1. $|V_1| = |V_2| = 6$.<br/>"
                    "2. $|E_1| = |E_2| = 8$.<br/>"
                    "3. Ακολουθία βαθμών G1: deg(A)=3, deg(B)=3, deg(C)=2, deg(D)=3, deg(E)=3, deg(F)=2. Ταξινόμηση: (3, 3, 3, 3, 2, 2).<br/>"
                    "Ακολουθία βαθμών G2: deg(1)=2, deg(2)=3, deg(3)=3, deg(4)=2, deg(5)=3, deg(6)=3. Ταξινόμηση: (3, 3, 3, 3, 2, 2).<br/>"
                    "4. Αμφιμονοσήμαντη αντιστοίχιση f: V1 -> V2 που διατηρεί τη γειτνίαση: A -> 2, B -> 5, C -> 4, D -> 3, E -> 6, F -> 1. Άρα $G_1 \\cong G_2$.",
                    "<b>Ερώτημα β' (Επιπεδότητα & Euler):</b><br/>"
                    "Το $G_1$ μπορεί να σχεδιαστεί στο επίπεδο χωρίς διασταυρώσεις ακμών (δεν περιέχει υπογράφο ομοιόμορφο με $K_5$ ή $K_{3,3}$, Θεώρημα Kuratowski).<br/>"
                    "Τύπος Euler: $V - E + R = 2 \\implies 6 - 8 + R = 2 \\implies R = 4$ περιοχές (3 εσωτερικές έδρες και 1 εξωτερική).",
                ],
                "Ομάδα Β": [
                    (
                        "<b>Ερώτημα α' (Ισομορφισμός - AM: 3323):</b><br/>"
                        "1. Πλήθος κορυφών: $|V_1| = |V_2| = 6$.<br/>"
                        "2. Πλήθος ακμών: $|E_1| = |E_2| = 8$.<br/>"
                        "3. Ακολουθία βαθμών $G_1$: $\\deg(A)=3, \\deg(B)=3, \\deg(C)=2, \\deg(D)=3, \\deg(E)=3, \\deg(F)=2$. Ταξινόμηση: $(3, 3, 3, 3, 2, 2)$.<br/>"
                        "Ακολουθία βαθμών $G_2$: $\\deg(1)=2, \\deg(2)=3, \\deg(3)=3, \\deg(4)=2, \\deg(5)=3, \\deg(6)=3$. Ταξινόμηση: $(3, 3, 3, 3, 2, 2)$.<br/>"
                        "4. Κατασκευάζουμε 1-1 και επί αντιστοίχιση $f: V_1 \\to V_2$ που διατηρεί τη γειτνίαση ακμών: $A \\mapsto 2, B \\mapsto 5, C \\mapsto 4, D \\mapsto 3, E \\mapsto 6, F \\mapsto 1$.<br/>"
                        "Όλες οι 8 ακμές διατηρούνται, άρα $G_1 \\cong G_2$."
                    ),
                    (
                        "<b>Ερώτημα β' (Επιπεδότητα & Τύπος Euler):</b><br/>"
                        "Το γράφημα $G_1$ είναι επίπεδο διότι δεν περιέχει ως υπογράφο υποδιαίρεση του $K_5$ ούτε του $K_{3,3}$ (Θεώρημα Kuratowski).<br/>"
                        "Επαλήθευση Τύπου Euler: $V - E + R = 2 \\implies 6 - 8 + R = 2 \\implies R = 4$ περιοχές (3 εσωτερικές έδρες και 1 εξωτερική/άπειρη έδρα)."
                    ),
                ],
                "Ομάδα Γ": [
                    "Επαλήθευση ακολουθίας βαθμών και ισομορφισμού. Euler: $V - E + R = 2 \\implies R = 4$.",
                ],
                "Ομάδα Δ": [
                    "Επαλήθευση ακολουθίας βαθμών και ισομορφισμού. Euler: $V - E + R = 2 \\implies R = 4$.",
                ],
            },
            final_answers={
                "Ομάδα Α": "α'. Τα γραφήματα είναι ισόμορφα (G1 ≅ G2), β'. Το G1 είναι επίπεδο με R = 4 περιοχές.",
                "Ομάδα Β": "α'. Τα γραφήματα είναι ισόμορφα, β'. Επίπεδο με R = 4 περιοχές.",
                "Ομάδα Γ": "α'. Τα γραφήματα είναι ισόμορφα, β'. Επίπεδο με R = 4 περιοχές.",
                "Ομάδα Δ": "α'. Τα γραφήματα είναι ισόμορφα, β'. Επίπεδο με R = 4 περιοχές.",
            },
            pitfalls="Στον υπολογισμό των περιοχών (R) του τύπου Euler, μην παραλείψετε την εξωτερική/άπειρη περιοχή!",
            interactive_type="graph",
        ),

        # THEME 7: Regular Expressions
        ExamExercise(
            number=7,
            title="Κανονικές Εκφράσεις επί του {0, 1}",
            points=0.5,
            topic="Τυπικές Γλώσσες & Αυτόματα (Formal Languages)",
            statements={
                "Ομάδα Α": "Γράψτε κανονική έκφραση για συμβολοσειρές επί του {0, 1} που περιέχουν τουλάχιστον 2 εμφανίσεις του 0.",
                "Ομάδα Β": "Γράψτε κανονική έκφραση για συμβολοσειρές επί του {0, 1} που περιέχουν ακριβώς 3 εμφανίσεις του 1.",
                "Ομάδα Γ": "Γράψτε κανονική έκφραση για συμβολοσειρές επί του {0, 1} που περιέχουν άρτιο αριθμό εμφανίσεων του 0.",
                "Ομάδα Δ": "Γράψτε κανονική έκφραση για συμβολοσειρές επί του {0, 1} που περιέχουν περιττό αριθμό εμφανίσεων του 1.",
            },
            steps={
                "Ομάδα Α": [
                    "Απαιτούνται δύο μηδενικά, με οποιονδήποτε αριθμό από 0 και 1 πριν, ενδιάμεσα και μετά: $(0 \\mid 1)^* 0 (0 \\mid 1)^* 0 (0 \\mid 1)^*$ ή $1^* 0 1^* 0 (0 \\mid 1)^*$.",
                ],
                "Ομάδα Β": [
                    "Ακριβώς τρία '1' σημαίνει ότι τα υπόλοιπα σύμβολα μπορούν να είναι μόνο '0': $0^* 1 0^* 1 0^* 1 0^*$.",
                ],
                "Ομάδα Γ": [
                    "Άρτιος αριθμός '0' (συμπεριλαμβανομένου του 0 μηδενικά): $(1^* 0 1^* 0 1^*)^* \\mid 1^*$. Πιο συμπαγώς: $(1^* \\mid 1^* 0 1^* 0 1^*)^*$.",
                ],
                "Ομάδα Δ": [
                    "Περιττός αριθμός '1': $0^* 1 0^* (0^* 1 0^* 1 0^*)^*$.",
                ],
            },
            final_answers={
                "Ομάδα Α": "(0 | 1)* 0 (0 | 1)* 0 (0 | 1)*  ή  1* 0 1* 0 (0 | 1)*",
                "Ομάδα Β": "0* 1 0* 1 0* 1 0*",
                "Ομάδα Γ": "(1 | 0 1* 0)*",
                "Ομάδα Δ": "0* 1 0* (0* 1 0* 1 0*)*",
            },
            pitfalls="Στην Ομάδα Β, αν χρησιμοποιηθεί το (0|1)* ανάμεσα στα '1', επιτρέπονται περισσότερα από 3 άσσοι, πράγμα λανθασμένο!",
            interactive_type="dfa",
        ),

        # THEME 8: Language Membership
        ExamExercise(
            number=8,
            title="Αναγνώριση Λέξεων από Κανονική Έκφραση",
            points=0.5,
            topic="Τυπικές Γλώσσες (RegEx Matching)",
            statements={
                "Ομάδα Α": "Ποιες από τις συμβολοσειρές {bat, bit, bot, but, bait, boat, bout} ανήκουν στο b(ε | a)(ε | i)t;",
                "Ομάδα Β": "Ποιες από τις συμβολοσειρές {bat, bit, bot, but, bait, boat, bout} ανήκουν στο bo(ε | a | u)t;",
                "Ομάδα Γ": "Ποιες από τις συμβολοσειρές {bat, bit, bot, but, bait, boat, bout} ανήκουν στο b(ε | o)a(ε | i)t;",
                "Ομάδα Δ": "Ποιες από τις συμβολοσειρές {bat, bit, bot, but, bait, boat, bout} ανήκουν στο b(ε | i)(ε | o | u)t;",
            },
            steps={
                "Ομάδα Α": [
                    "Η έκφραση παράγει λέξεις που ξεκινούν με 'b', ακολουθεί προαιρετικά 'a', προαιρετικά 'i', και τελειώνουν με 't'.",
                    "Πιθανές λέξεις: $bt$ (αν ε, ε), $bit$ (αν ε, i), $bat$ (αν a, ε), $bait$ (αν a, i).",
                    "Από τη δοθείσα λίστα ανήκουν οι: <b>bat, bit, bait</b>.",
                ],
                "Ομάδα Β": [
                    "Η έκφραση $bo(\\epsilon \\mid a \\mid u)t$ παράγει: $bot$ (αν ε), $boat$ (αν a), $bout$ (αν u).",
                    "Από τη λίστα ανήκουν οι: <b>bot, boat, bout</b>.",
                ],
                "Ομάδα Γ": [
                    "Η έκφραση $b(\\epsilon \\mid o)a(\\epsilon \\mid i)t$ παράγει: $bat, bait, boat$ (αν o, a, ε) και boait.",
                    "Από τη λίστα ανήκουν οι: <b>bat, bait, boat</b>.",
                ],
                "Ομάδα Δ": [
                    "Η έκφραση $b(\\epsilon \\mid i)(\\epsilon \\mid o \\mid u)t$ παράγει: $bt, bot, but, bit, biot, biut$.",
                    "Από τη λίστα ανήκουν οι: <b>bit, bot, but</b>.",
                ],
            },
            final_answers={
                "Ομάδα Α": "{bat, bit, bait}",
                "Ομάδα Β": "{bot, boat, bout}",
                "Ομάδα Γ": "{bat, bait, boat}",
                "Ομάδα Δ": "{bit, bot, but}",
            },
            pitfalls="Προσοχή: Το ε συμβολίζει την κενή συμβολοσειρά (μήκος μηδέν), όχι κενό διάστημα.",
        ),

        # THEME 9: Mathematical Induction
        ExamExercise(
            number=9,
            title="Μαθηματική Επαγωγή σε Γεωμετρική Πρόοδο",
            points=1.0,
            topic="Μαθηματική Επαγωγή (Mathematical Induction)",
            statements={
                "Ομάδα Α": "Δείξτε ότι για κάθε n >= 0: 1 + 3 + 3^2 + ... + 3^n = (3^(n+1) - 1) / 2.",
                "Ομάδα Β": "Δείξτε ότι για κάθε n >= 0: 1 + 5 + 5^2 + ... + 5^n = (5^(n+1) - 1) / 4.",
                "Ομάδα Γ": "Δείξτε ότι για κάθε n >= 0: 1 + 7 + 7^2 + ... + 7^n = (7^(n+1) - 1) / 6.",
                "Ομάδα Δ": "Δείξτε ότι για κάθε n >= 0: 1 + 11 + 11^2 + ... + 11^n = (11^(n+1) - 1) / 10.",
            },
            steps={
                "Ομάδα Α": [
                    "<b>Βασικό Βήμα (n = 0):</b><br/>LHS = $3^0 = 1$.<br/>RHS = $\\frac{3^{0+1}-1}{2} = \\frac{2}{2} = 1$. LHS = RHS = 1, άρα ισχύει.",
                    "<b>Επαγωγική Υπόθεση (n = k):</b><br/>Υποθέτουμε ότι ισχύει για $k \\ge 0$: $1 + 3 + \\dots + 3^k = \\frac{3^{k+1}-1}{2}$.",
                    "<b>Επαγωγικό Βήμα (n = k + 1):</b><br/>$$LHS = \\left(1 + 3 + \\dots + 3^k\\right) + 3^{k+1} = \\frac{3^{k+1}-1}{2} + 3^{k+1}$$"
                    "$$= \\frac{3^{k+1}-1 + 2 \\cdot 3^{k+1}}{2} = \\frac{3 \\cdot 3^{k+1}-1}{2} = \\frac{3^{k+2}-1}{2} = RHS$$",
                    "<b>Συμπέρασμα:</b> Από την αρχή της επαγωγής, ισχύει για κάθε $n \\ge 0$. (Q.E.D.)",
                ],
                "Ομάδα Β": [
                    (
                        "<b>Βασικό Βήμα (n = 0 - AM: 3323):</b><br/>"
                        "Αριστερό μέλος: $LHS = 5^0 = 1$.<br/>"
                        "Δεξί μέλος: $RHS = \\frac{5^{0+1}-1}{4} = \\frac{5-1}{4} = \\frac{4}{4} = 1$.<br/>"
                        "Εφόσον $LHS = RHS = 1$, η βάση της επαγωγής ισχύει για $n = 0$."
                    ),
                    (
                        "<b>Επαγωγική Υπόθεση & Επαγωγικό Βήμα (n = k + 1):</b><br/>"
                        "Υποθέτουμε ότι ισχύει για κάποιο αυθαίρετο $k \\ge 0$: $1 + 5 + 5^2 + \\dots + 5^k = \\frac{5^{k+1}-1}{4}$.<br/>"
                        "Θέλουμε να αποδείξουμε ότι ισχύει για $n = k + 1$, δηλαδή:<br/>"
                        "$$1 + 5 + \\dots + 5^k + 5^{k+1} = \\frac{5^{(k+1)+1}-1}{4} = \\frac{5^{k+2}-1}{4}$$"
                        "<b>Απόδειξη:</b><br/>"
                        "$$LHS = \\left(1 + 5 + \\dots + 5^k\\right) + 5^{k+1} = \\frac{5^{k+1}-1}{4} + 5^{k+1}$$"
                        "$$= \\frac{5^{k+1}-1 + 4 \\cdot 5^{k+1}}{4} = \\frac{(1+4) \\cdot 5^{k+1}-1}{4} = \\frac{5 \\cdot 5^{k+1}-1}{4} = \\frac{5^{k+2}-1}{4} = RHS$$<br/>"
                        "<b>Συμπέρασμα:</b> Από την αρχή της μαθηματικής επαγωγής, η ισότητα ισχύει για κάθε $n \\ge 0$. (Q.E.D.)"
                    ),
                ],
                "Ομάδα Γ": [
                    "Βάση: n=0 $\\implies 1 = (7-1)/6 = 1$.<br/>Επαγωγικό βήμα: $\\frac{7^{k+1}-1}{6} + 7^{k+1} = \\frac{7^{k+2}-1}{6}$.",
                ],
                "Ομάδα Δ": [
                    "Βάση: n=0 $\\implies 1 = (11-1)/10 = 1$.<br/>Επαγωγικό βήμα: $\\frac{11^{k+1}-1}{10} + 11^{k+1} = \\frac{11^{k+2}-1}{10}$.",
                ],
            },
            final_answers={
                "Ομάδα Α": "Αποδείχθηκε με μαθηματική επαγωγή (Q.E.D.)",
                "Ομάδα Β": "Αποδείχθηκε με μαθηματική επαγωγή (Q.E.D.)",
                "Ομάδα Γ": "Αποδείχθηκε με μαθηματική επαγωγή (Q.E.D.)",
                "Ομάδα Δ": "Αποδείχθηκε με μαθηματική επαγωγή (Q.E.D.)",
            },
            pitfalls="Στο επαγωγικό βήμα, πρέπει να δηλώνεται ρητά πού ακριβώς αντικαθίσταται η επαγωγική υπόθεση!",
            interactive_type="induction",
        ),
    ]

    return Scenario(
        id="past_exam_june_2025",
        title="Τελική Εξέταση Ιουνίου 2025",
        subtitle="Επίσημα Θέματα Εξέτασης — Ομάδες Α, Β, Γ, Δ",
        course_tag="Ιούνιος 2025",
        academic_year="2024 - 2025",
        total_points=10.0,
        duration_hours=3.0,
        exercises=exercises,
    )
