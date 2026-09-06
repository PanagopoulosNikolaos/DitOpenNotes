"""Practice Exam Scenario 3: Full Curriculum Electromagnetics, Loop Torques & Quantum Photons.

Verbatim transcription of practice exam 3 with three-part contract hover tooltips,
step-by-step KaTeX derivations, and SymPy Python verification code.
"""

from models.scenario import (
    Scenario,
    Paragraph,
    TextSegment,
    ExamQuestion,
    QuestionOption,
    CalculationStep,
    GivenParameter,
    DesignJustification,
)


def createSynthExam3FullSpectrum() -> Scenario:
    """Instantiates the Practice Exam 3 scenario.

    Returns:
        Scenario: Complete scenario container with verbatim text and solutions.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(
                    text="Εξέταση Αρχών Ηλεκτρομαγνητισμού & Τηλεπικοινωνιών (Εξάσκηση 3 — Πλήρες Φάσμα)\n",
                    is_highlight=False,
                ),
                TextSegment(
                    text="Μέρος Α: Θεωρία (4 μονάδες) | Μέρος Β: Ασκήσεις (6 μονάδες)\n",
                    is_highlight=False,
                ),
            ],
            accent_border_color=None,
        ),
        Paragraph(
            segments=[
                TextSegment(text="Μέρος Α: Θεωρία\nΘέμα 1:\n", is_highlight=False),
                TextSegment(text="1. Πώς συνδέεται η ", is_highlight=False),
                TextSegment(
                    text="ροή του ηλεκτρικού ρεύματος με το διάνυσμα πυκνότητας ρεύματος",
                    is_highlight=True,
                    category="field",
                    tag_label="I = ∬ J·dS",
                    tooltip="Classification: Ορισμός Ρεύματος από Πυκνότητα | Detection Clue: 'ροή ρεύματος με διάνυσμα πυκνότητας' | Application Rationale: I = ∬ J·dS, όπου J είναι η πυκνότητα ρεύματος ανά επιφάνεια.",
                ),
                TextSegment(text="; 2. Ποιο φυσικό μέγεθος περιγράφει την κίνηση φορτίων μέσα από επιφάνεια; 3. Διατυπώστε τους ", is_highlight=False),
                TextSegment(
                    text="δύο κανόνες του Kirchhoff",
                    is_highlight=True,
                    category="law",
                    tag_label="KIRCHHOFF",
                    tooltip="Classification: Κανόνες Κυκλωμάτων | Detection Clue: 'δύο κανόνες του Kirchhoff' | Application Rationale: Κόμβων (διατήρηση φορτίου) και Βρόχων (διατήρηση ενέργειας).",
                ),
                TextSegment(text=" και εξηγήστε την αρχή διατήρησης. 4. Ποια είναι η μαθηματική σχέση μεταξύ ", is_highlight=False),
                TextSegment(
                    text="ειδικής αντίστασης και ειδικής αγωγιμότητας",
                    is_highlight=True,
                    category="param",
                    tag_label="σ = 1/ρ",
                    tooltip="Classification: Καταστατική Σχέση Αγωγιμότητας | Detection Clue: 'ειδική αντίσταση και ειδική αγωγιμότητα' | Application Rationale: σ = 1 / ρ.",
                ),
                TextSegment(text="; 5. Ποιοι τρεις παράγοντες καθορίζουν την ηλεκτρική αντίσταση ενός αγωγού;\n", is_highlight=False),
                TextSegment(text="Θέμα 2:\n1. Περιγράψτε τη φύση των ", is_highlight=False),
                TextSegment(
                    text="μαγνητικών δυναμικών γραμμών",
                    is_highlight=True,
                    category="field",
                    tag_label="ΓΡΑΜΜΕΣ B",
                    tooltip="Classification: Μαγνητικές Γραμμές Πεδίου | Detection Clue: 'φύση μαγνητικών δυναμικών γραμμών' | Application Rationale: Είναι πάντοτε κλειστές καμπύλες επειδή div B = 0.",
                ),
                TextSegment(text=" και τη διαφορά τους από το ηλεκτροστατικό πεδίο. 2. Θεωρήστε ένα ακίνητο και ένα κινούμενο ηλεκτρικό φορτίο: τι δυνάμεις θα ασκηθούν μεταξύ τους; 3. Τι δύναμη δημιουργείται μεταξύ ", is_highlight=False),
                TextSegment(
                    text="παράλληλων συρμάτων με ρεύμα",
                    is_highlight=True,
                    category="law",
                    tag_label="F/L ΣΥΡΜΑΤΩΝ",
                    tooltip="Classification: Δύναμη Αμοιβαίας Επαγωγής | Detection Clue: 'παράλληλων συρμάτων' | Application Rationale: Ομόρροπα έλκονται, αντίρροπα απωθούνται.",
                ),
                TextSegment(text="; 4. Από ποιους παράγοντες εξαρτάται η μαγνητική επαγωγή B (Νόμος Biot-Savart); 5. Σύμφωνα με τον ", is_highlight=False),
                TextSegment(
                    text="νόμο του Gauss για τον μαγνητισμό",
                    is_highlight=True,
                    category="law",
                    tag_label="GAUSS B",
                    tooltip="Classification: 2η Εξίσωση Maxwell | Detection Clue: 'νόμο Gauss για μαγνητισμό' | Application Rationale: ∬ B·dS = 0, μη ύπαρξη μαγνητικών μονοπόλων.",
                ),
                TextSegment(text=", ποια είναι η συνολική μαγνητική ροή μέσα από οποιαδήποτε κλειστή επιφάνεια;", is_highlight=False),
            ],
            accent_border_color="accent",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Μέρος Β: Ασκήσεις\n", is_highlight=False),
                TextSegment(text="Άσκηση 3: Δύο φορτία ", is_highlight=False),
                TextSegment(
                    text="Q₁ = +5 μC (x=0) και Q₂ = -2 μC (x=3 m)",
                    is_highlight=True,
                    category="param",
                    tag_label="Q1, Q2",
                    tooltip="Classification: Σημειακά Φορτία | Detection Clue: Q1, Q2 | Application Rationale: Υπολογισμός δύναμης σε Q3 = +1 μC στο x = 6 m.",
                ),
                TextSegment(text=" ασκούν δύναμη σε Q₃ = +1 μC στο x = 6 m. Βρείτε τη συνολική δύναμη.\n", is_highlight=False),
                TextSegment(text="Άσκηση 4: Μακρύς κυλινδρικός αγωγός ", is_highlight=False),
                TextSegment(
                    text="R = 4 cm διαρρέεται από I = 50 A",
                    is_highlight=True,
                    category="param",
                    tag_label="ΚΥΛΙΝΔΡΟΣ R",
                    tooltip="Classification: Κυλινδρικός Αγωγός Ampère | Detection Clue: R = 4 cm, I = 50 A | Application Rationale: B(r<R) = μ_0 I r / (2π R^2) και B(r>R) = μ_0 I / (2π r).",
                ),
                TextSegment(text=" ομοιόμορφα κατανεμημένο. Υπολογίστε το B σε r = 2 cm και r = 8 cm.\n", is_highlight=False),
                TextSegment(text="Άσκηση 5: Επίπεδος πυκνωτής με κυκλικούς οπλισμούς ", is_highlight=False),
                TextSegment(
                    text="ακτίνας 10 cm, d = 1.0 mm και κ = 4",
                    is_highlight=True,
                    category="param",
                    tag_label="ΚΥΚΛΙΚΟΣ ΠΥΚΝΩΤΗΣ",
                    tooltip="Classification: Κυκλικός Πυκνωτής με Διηλεκτρικό | Detection Clue: r = 10 cm, d = 1 mm, κ = 4 | Application Rationale: A = π r^2, C = κ ε_0 A / d.",
                ),
                TextSegment(text=". Υπολογίστε τη χωρητικότητα C.\n", is_highlight=False),
                TextSegment(text="Άσκηση 6: Ηλεκτρόνιο επιταχύνεται από ", is_highlight=False),
                TextSegment(
                    text="V = 2500 V και εισέρχεται κάθετα σε B = 0.5 T",
                    is_highlight=True,
                    category="param",
                    tag_label="ΗΛΕΚΤΡΟΝΙΟ 2500V",
                    tooltip="Classification: Lorentz Επιτάχυνση & Μαγνητικό Πεδίο | Detection Clue: V = 2500 V, B = 0.5 T | Application Rationale: v = sqrt(2eV/m), F_B = e v B.",
                ),
                TextSegment(text=". Υπολογίστε ταχύτητα v και δύναμη F_B.\n", is_highlight=False),
                TextSegment(text="Άσκηση 7 & 8: Επίπεδο κύμα ", is_highlight=False),
                TextSegment(
                    text="E = 5 cos(2·10⁷ x - ωt) ŷ",
                    is_highlight=True,
                    category="field",
                    tag_label="E(x,t)",
                    tooltip="Classification: ΗΜ Κύμα με Διάδοση κατά +x | Detection Clue: k = 2*10^7 rad/m κατά x, πόλωση y | Application Rationale: λ = 2π/k, ω = ck, B(x,t) κατά +z, S και I.",
                ),
                TextSegment(text=". Βρείτε λ, ω, B(x,t), S(t) και μέση ένταση I.\n", is_highlight=False),
                TextSegment(text="Άσκηση 9: Δέσμη φωτός από ", is_highlight=False),
                TextSegment(
                    text="γυαλί (n₁ = 1.50) σε νερό (n₂ = 1.33) με θ₁ = 35°",
                    is_highlight=True,
                    category="law",
                    tag_label="ΔΙΑΘΛΑΣΗ SNELL",
                    tooltip="Classification: Διάθλαση Snell & Κρίσιμη Γωνία | Detection Clue: n1=1.50, n2=1.33, θ1=35° | Application Rationale: n1 sinθ1 = n2 sinθ2, sinθc = n2/n1.",
                ),
                TextSegment(text=". Υπολογίστε γωνία διάθλασης θ₂ και κρίσιμη γωνία θ_c.\n", is_highlight=False),
                TextSegment(text="Άσκηση 10: Γραμμική κατανομή φορτίου ", is_highlight=False),
                TextSegment(
                    text="λ = 3.0 nC/m κατά μήκος του άξονα x",
                    is_highlight=True,
                    category="field",
                    tag_label="ΓΡΑΜΜΙΚΟ λ",
                    tooltip="Classification: Απειρομήκης Γραμμική Κατανομή Φορτίου | Detection Clue: λ = 3.0 nC/m στον x | Application Rationale: E = λ / (2πε_0 y) ŷ.",
                ),
                TextSegment(text=". Υπολογίστε το ηλεκτρικό πεδίο στο σημείο y = 4.0 m.\n", is_highlight=False),
                TextSegment(text="Άσκηση 11: Ορθογώνιος βρόχος ", is_highlight=False),
                TextSegment(
                    text="5 cm × 10 cm, I = 2.0 A σε B = 0.2 T με γωνία 30°",
                    is_highlight=True,
                    category="param",
                    tag_label="ΡΟΠΗ ΒΡΟΧΟΥ",
                    tooltip="Classification: Μαγνητική Ροπή σε Ρευματοφόρο Βρόχο | Detection Clue: Διαστάσεις, ρεύμα, B, γωνία 30° | Application Rationale: m = I A, τ = m B sinθ.",
                ),
                TextSegment(text=". Υπολογίστε το μέτρο της ροπής τ.\n", is_highlight=False),
                TextSegment(text="Άσκηση 12: Πηγή εκπέμπει ", is_highlight=False),
                TextSegment(
                    text="φωτόνια με ενέργεια 2.5 eV",
                    is_highlight=True,
                    category="param",
                    tag_label="ΦΩΤΟΝΙΟ 2.5 eV",
                    tooltip="Classification: Ενέργεια Φωτονίου & Φάσμα | Detection Clue: E = 2.5 eV | Application Rationale: E = h f = h c / λ, ταξινόμηση στο ορατό φως.",
                ),
                TextSegment(text=". Βρείτε το μήκος κύματος σε nm και το είδος της ακτινοβολίας.", is_highlight=False),
            ],
            accent_border_color="accent",
        ),
    ]

    questions = [
        ExamQuestion(
            question_number=1,
            title="Κανόνες Kirchhoff & Θεμελιώδεις Αρχές",
            question_type="Theory Analysis",
            prompt_text="Διατυπώστε τους δύο κανόνες του Kirchhoff για τα ηλεκτρικά κυκλώματα και εξηγήστε την αρχή διατήρησης στην οποία βασίζεται κάθε κανόνας.",
            options=[],
            final_answer="1ος: Κόμβων (ΣI_in = ΣI_out) -> Διατήρηση Φορτίου | 2ος: Βρόχων (ΣV = 0) -> Διατήρηση Ενέργειας",
            detailed_justification="Σε κλειστό κύκλωμα το συνολικό φορτίο δεν συσσωρεύεται σε κόμβους, ενώ η κυκλοφορία του ηλεκτροστατικού πεδίου κατά μήκος κλειστού βρόχου μηδενίζεται (αστρόβιλο πεδίο).",
            common_pitfalls=["Ο 2ος κανόνας ισχύει επακριβώς όταν δεν υπάρχει χρονικά μεταβαλλόμενη μαγνητική ροή μέσα στον βρόχο."],
            related_theory_topic="Ηλεκτρικά Κυκλώματα & Νόμοι Kirchhoff",
        ),
        ExamQuestion(
            question_number=2,
            title="Νόμος Gauss για τον Μαγνητισμό",
            question_type="Theory Analysis",
            prompt_text="Σύμφωνα με τον νόμο του Gauss για τον μαγνητισμό, ποια είναι η συνολική μαγνητική ροή μέσα από οποιαδήποτε κλειστή επιφάνεια; Τι συνεπάγεται αυτό;",
            options=[],
            final_answer="Η ολική μαγνητική ροή είναι αυστηρά μηδέν (Φ_B = 0). Συνεπάγεται την παντελή απουσία απομονωμένων μαγνητικών μονοπόλων.",
            detailed_justification="Η διαφορική μορφή ∇·B = 0 δηλώνει ότι το μαγνητικό πεδίο είναι σωληνοειδές και οι δυναμικές γραμμές δεν έχουν πηγές ή καταβόθρες αλλά σχηματίζουν αδιάσπαστους κλειστούς βρόχους.",
            common_pitfalls=["Αν ποτέ ανακαλυφθεί μαγνητικό μονόπολο, η εξίσωση Maxwell θα τροποποιηθεί σε ∇·B = ρ_m."],
            related_theory_topic="2η Εξίσωση Maxwell & Μαγνητοστατική",
        ),
        ExamQuestion(
            question_number=3,
            title="Άσκηση 3: Δύναμη Coulomb σε Σύστημα 3 Φορτίων",
            question_type="Calculations",
            prompt_text=r"Δύο φορτία $Q_1 = +5\,\mu\text{C}$ στο $x = 0$ και $Q_2 = -2\,\mu\text{C}$ στο $x = 3\text{ m}$ ασκούν δύναμη σε $Q_3 = +1\,\mu\text{C}$ στο $x = 6\text{ m}$. Προσδιορίστε τη συνολική δύναμη στο $Q_3$.",
            given_parameters=[
                GivenParameter("Q_1", "+5 \\times 10^{-6} \\text{ C}", "Φορτίο στο x=0"),
                GivenParameter("Q_2", "-2 \\times 10^{-6} \\text{ C}", "Φορτίο στο x=3 m"),
                GivenParameter("Q_3", "+1 \\times 10^{-6} \\text{ C}", "Φορτίο στο x=6 m"),
            ],
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Προσδιορισμός μονοδιάστατης γεωμετρίας και αποστάσεων",
                    formula=r"r_{13} = |x_3 - x_1|, \quad r_{23} = |x_3 - x_2|",
                    substitution=r"x_1 = 0 \ \text{m}, \quad x_2 = 3.0 \ \text{m}, \quad x_3 = 6.0 \ \text{m} \implies r_{13} = 6.0 - 0 = 6.0 \ \text{m}, \quad r_{23} = 6.0 - 3.0 = 3.0 \ \text{m}",
                    result=r"r_{13} = 6.0 \ \text{m}, \quad r_{23} = 3.0 \ \text{m}",
                    rationale="Αποστάσεις μεταξύ των σημειακών φορτίων κατά μήκος του άξονα θέσεων x.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Διανυσματική άπωση Coulomb F_13 από το θετικό Q_1 στο θετικό Q_3",
                    formula=r"\vec{F}_{13} = +k_e \frac{Q_1 Q_3}{r_{13}^2} \hat{x}",
                    substitution=r"Q_1 = +5 \ \mu\text{C}, \ Q_3 = +1 \ \mu\text{C} \implies \text{Ομόσημα φορτία απωθούνται, άρα η δύναμη κατευθύνεται προς τα δεξιά } (+\hat{x})",
                    result=r"\vec{F}_{13} = +k_e \frac{Q_1 Q_3}{r_{13}^2} \hat{x}",
                    rationale="Η ηλεκτροστατική άπωση ωθεί το Q_3 μακριά από το Q_1 κατά μήκος του άξονα x.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Αριθμητικός υπολογισμός μέτρου και συνιστώσας της F_13",
                    formula=r"F_{13} = k_e \frac{Q_1 Q_3}{r_{13}^2}",
                    substitution=r"F_{13} = (8.988\times 10^9 \ \text{N}\cdot\text{m}^2/\text{C}^2) \frac{(5.0\times 10^{-6} \ \text{C})(1.0\times 10^{-6} \ \text{C})}{(6.0 \ \text{m})^2} = \frac{4.494\times 10^{-2}}{36.0}",
                    result=r"\vec{F}_{13} \approx +1.2483 \times 10^{-3} \ \text{N} \ \hat{x} = +1.25 \ \text{mN} \ \hat{x}",
                    rationale="Ασθενέστερη άπωση λόγω της μεγαλύτερης απόστασης των 6 μέτρων.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Διανυσματική έλξη Coulomb F_23 από το αρνητικό Q_2 στο θετικό Q_3",
                    formula=r"\vec{F}_{23} = -k_e \frac{|Q_2| Q_3}{r_{23}^2} \hat{x}",
                    substitution=r"F_{23} = (8.988\times 10^9) \frac{(2.0\times 10^{-6} \ \text{C})(1.0\times 10^{-6} \ \text{C})}{(3.0 \ \text{m})^2} = \frac{1.7976\times 10^{-2}}{9.0}",
                    result=r"\vec{F}_{23} \approx -1.9973 \times 10^{-3} \ \text{N} \ \hat{x} = -2.00 \ \text{mN} \ \hat{x}",
                    rationale="Επειδή το Q_2 είναι αρνητικό και βρίσκεται αριστερά του Q_3 (x=3 m), το έλκει προς τα αριστερά (-x).",
                ),
                CalculationStep(
                    step_number=5,
                    title="Εφαρμογή αρχής επαλληλίας για τη συνισταμένη δύναμη F_net",
                    formula=r"\vec{F}_{\text{net}} = \vec{F}_{13} + \vec{F}_{23} = (F_{13} - F_{23})\hat{x}",
                    substitution=r"F_{\text{net}} = +1.2483 \ \text{mN} - 1.9973 \ \text{mN} = -0.7490 \ \text{mN}",
                    result=r"\vec{F}_{\text{net}} \approx -0.75 \ \text{mN} \ \hat{x}",
                    rationale="Η ελκτική δύναμη από το κοντινότερο φορτίο Q_2 υπερισχύει της άπωσης από το Q_1.",
                ),
                CalculationStep(
                    step_number=6,
                    title="Τελικό μέτρο και φυσική κατεύθυνση κίνησης",
                    formula=r"|\vec{F}_{\text{net}}| = 7.49\times 10^{-4} \ \text{N}, \quad \hat{u}_F = -\hat{x}",
                    substitution=r"\text{Η συνισταμένη δύναμη επιταχύνει το } Q_3 \text{ προς τα αριστερά (προς το σημείο } x=3\text{ m})",
                    result=r"\vec{F}_{\text{net}} \approx 0.75 \ \text{mN} \quad (\pi\rho\omicron\varsigma \ \tau\alpha \ \alpha\rho\iota\sigma\tau\epsilon\rho\acute{\alpha})",
                    rationale="Η απόσταση r_23 είναι η μισή της r_13, γεγονός που τετραπλασιάζει την επίδραση του αντίστροφου τετραγώνου.",
                ),
            ],
            final_answer=r"\vec{F}_{\text{net}} \approx -0.75\text{ mN} \ \hat{x} \quad (\text{μέτρο } 7.5\times 10^{-4}\text{ N προς τα αριστερά})",
            detailed_justification="Αρχή επαλληλίας Coulomb στον μονοδιάστατο άξονα θέσεων.",
            common_pitfalls=["Προσοχή στις αποστάσεις: r_13 = 6 m, r_23 = 6 - 3 = 3 m."],
            related_theory_topic="Ηλεκτροστατική & Νόμος Coulomb",
        ),
        ExamQuestion(
            question_number=4,
            title="Άσκηση 4: Μαγνητικό Πεδίο στο Εσωτερικό και Εξωτερικό Κυλίνδρου",
            question_type="Calculations",
            prompt_text=r"Κυλινδρικός αγωγός με ακτίνα $R = 4\text{ cm}$ διαρρέεται από ομοιόμορφο ρεύμα $I = 50\text{ A}$. Υπολογίστε το $B$ σε: α) $r = 2\text{ cm}$ (εσωτερικά), β) $r = 8\text{ cm}$ (εξωτερικά).",
            given_parameters=[
                GivenParameter("R", "4 \\text{ cm} = 0.04 \\text{ m}", "Ακτίνα κυλίνδρου"),
                GivenParameter("I", "50 \\text{ A}", "Ολικό ρεύμα"),
                GivenParameter("r_1", "2 \\text{ cm} = 0.02 \\text{ m}", "Εσωτερική απόσταση"),
                GivenParameter("r_2", "8 \\text{ cm} = 0.08 \\text{ m}", "Εξωτερική απόσταση"),
            ],
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Υπολογισμός ομοιόμορφης πυκνότητας ρεύματος J στον αγωγό",
                    formula=r"J = \frac{I}{\pi R^2}",
                    substitution=r"R = 0.04 \ \text{m} \implies \pi R^2 = \pi (0.04)^2 \approx 5.0265\times 10^{-3} \ \text{m}^2, \quad J = \frac{50 \ \text{A}}{5.0265\times 10^{-3} \ \text{m}^2} \approx 9947.2 \ \text{A/m}^2",
                    result=r"J \approx 9.947 \times 10^3 \ \text{A/m}^2",
                    rationale="Η κατανομή του ρεύματος στη διατομή του κυλίνδρου είναι απόλυτα ομοιόμορφη.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Εφαρμογή νόμου Ampère για εσωτερικά σημεία (r <= R)",
                    formula=r"\oint \vec{B}\cdot d\vec{\ell} = B(2\pi r) = \mu_0 I_{\text{enc}} = \mu_0 J (\pi r^2) = \mu_0 I \frac{r^2}{R^2} \implies B_{\text{in}}(r) = \frac{\mu_0 I r}{2\pi R^2}",
                    substitution=r"\text{Μέσα στον κύλινδρο περικλείεται μόνο το τμήμα ρεύματος που διέρχεται από την επιφάνεια ακτίνας } r",
                    result=r"B_{\text{in}}(r) = \frac{\mu_0 I r}{2\pi R^2}",
                    rationale="Το μαγνητικό πεδίο στο εσωτερικό αυξάνεται γραμμικά με την απόσταση r από τον άξονα.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Αριθμητικός υπολογισμός στο εσωτερικό σημείο r_1 = 2 cm",
                    formula=r"B(r_1) = \frac{\mu_0 I r_1}{2\pi R^2}",
                    substitution=r"B(0.02) = \frac{(4\pi\times 10^{-7} \ \text{T}\cdot\text{m/A}) \times (50 \ \text{A}) \times (0.02 \ \text{m})}{2\pi \times (0.04 \ \text{m})^2} = \frac{2\times 10^{-7} \times 1.0}{0.0016} = 1.25\times 10^{-4} \ \text{T}",
                    result=r"B(2 \ \text{cm}) = 1.25 \times 10^{-4} \ \text{T} = 125 \ \mu\text{T}",
                    rationale="Εσωτερικό μαγνητικό πεδίο στο μέσο της ακτίνας του αγωγού.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Εφαρμογή νόμου Ampère για εξωτερικά σημεία (r >= R)",
                    formula=r"\oint \vec{B}\cdot d\vec{\ell} = B(2\pi r) = \mu_0 I_{\text{enc}} = \mu_0 I \implies B_{\text{out}}(r) = \frac{\mu_0 I}{2\pi r}",
                    substitution=r"\text{Έξω από τον κύλινδρο ολόκληρο το ρεύμα } I = 50 \ \text{A} \text{ περικλείεται από τον βρόχο}",
                    result=r"B_{\text{out}}(r) = \frac{\mu_0 I}{2\pi r}",
                    rationale="Εκτός του κυλίνδρου το πεδίο είναι ταυτόσημο με εκείνο ενός απειρομήκους γραμμικού σύρματος.",
                ),
                CalculationStep(
                    step_number=5,
                    title="Αριθμητικός υπολογισμός στο εξωτερικό σημείο r_2 = 8 cm",
                    formula=r"B(r_2) = \frac{\mu_0 I}{2\pi r_2}",
                    substitution=r"B(0.08) = \frac{(4\pi\times 10^{-7} \ \text{T}\cdot\text{m/A}) \times (50 \ \text{A})}{2\pi \times (0.08 \ \text{m})} = \frac{2\times 10^{-7} \times 50}{0.08} = \frac{1.0\times 10^{-5}}{0.08} = 1.25\times 10^{-4} \ \text{T}",
                    result=r"B(8 \ \text{cm}) = 1.25 \times 10^{-4} \ \text{T} = 125 \ \mu\text{T}",
                    rationale="Εξωτερικό μαγνητικό πεδίο σε διπλάσια απόσταση από την ακτίνα του κυλίνδρου.",
                ),
                CalculationStep(
                    step_number=6,
                    title="Συγκριτική επισκόπηση προφίλ πεδίου και μέγιστης τιμής",
                    formula=r"B_{\max} = B(R) = \frac{\mu_0 I}{2\pi R} = 250 \ \mu\text{T}",
                    substitution=r"B(R/2) = \frac{1}{2}B_{\max} = 125 \ \mu\text{T}, \quad B(2R) = \frac{1}{2}B_{\max} = 125 \ \mu\text{T}",
                    result=r"B(2 \ \text{cm}) = B(8 \ \text{cm}) = 125 \ \mu\text{T}",
                    rationale="Το πεδίο φτάνει στο μέγιστο στην επιφάνεια του κυλίνδρου και παίρνει ίσες τιμές στα σημεία r = R/2 και r = 2R.",
                ),
            ],
            final_answer=r"B(2\text{ cm}) = 125\ \mu\text{T}, \quad B(8\text{ cm}) = 125\ \mu\text{T}",
            detailed_justification="Εφαρμογή του νόμου Ampère με κυκλικό βρόχο τόσο μέσα όσο και έξω από τον αγωγό.",
            common_pitfalls=["Στο εσωτερικό περικλείεται μόνο κλάσμα του ρεύματος I_enc = I (r/R)²."],
            related_theory_topic="Νόμος Ampère σε Κυλινδρικές Συμμετρίες",
        ),
        ExamQuestion(
            question_number=5,
            title="Άσκηση 5: Χωρητικότητα Κυκλικού Πυκνωτή",
            question_type="Calculations",
            prompt_text=r"Επίπεδος πυκνωτής αποτελείται από δύο κυκλικούς οπλισμούς ακτίνας $R = 10\text{ cm}$ που απέχουν $d = 1.0\text{ mm}$ με διηλεκτρικό $\kappa = 4$. Υπολογίστε τη χωρητικότητα $C$.",
            given_parameters=[
                GivenParameter("R", "10 \\text{ cm} = 0.1 \\text{ m}", "Ακτίνα οπλισμών"),
                GivenParameter("d", "1.0 \\text{ mm} = 0.001 \\text{ m}", "Απόσταση οπλισμών"),
                GivenParameter(r"\kappa", "4", "Διηλεκτρική σταθερά"),
            ],
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Μετατροπή γεωμετρικών διαστάσεων σε μονάδες SI",
                    formula=r"R = 10 \ \text{cm} \times 10^{-2} \ \text{m/cm} = 0.10 \ \text{m}, \quad d = 1.0 \ \text{mm} \times 10^{-3} \ \text{m/mm} = 0.001 \ \text{m}",
                    substitution=r"R = 0.10 \ \text{m}, \quad d = 0.001 \ \text{m}",
                    result=r"R = 0.10 \ \text{m}, \quad d = 0.001 \ \text{m}",
                    rationale="Μετατροπή ακτίνας και απόστασης οπλισμών σε μέτρα.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Υπολογισμός εμβαδού κυκλικού οπλισμού A",
                    formula=r"A = \pi R^2",
                    substitution=r"A = \pi (0.10 \ \text{m})^2 = 0.01\pi \ \text{m}^2 \approx 0.0314159 \ \text{m}^2",
                    result=r"A \approx 3.1416 \times 10^{-2} \ \text{m}^2",
                    rationale="Εμβαδόν κυκλικού δίσκου.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Υπολογισμός χωρητικότητας στο κενό C_0",
                    formula=r"C_0 = \epsilon_0 \frac{A}{d}",
                    substitution=r"C_0 = (8.854\times 10^{-12} \ \text{F/m}) \times \frac{0.0314159 \ \text{m}^2}{0.001 \ \text{m}} = (8.854\times 10^{-12}) \times 31.4159",
                    result=r"C_0 \approx 2.7816 \times 10^{-10} \ \text{F} \approx 278.16 \ \text{pF}",
                    rationale="Χωρητικότητα του κυκλικού πυκνωτή χωρίς διηλεκτρικό.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Υπολογισμός χωρητικότητας C με διηλεκτρικό (κ = 4)",
                    formula=r"C = \kappa C_0 = \kappa \epsilon_0 \frac{A}{d}",
                    substitution=r"C = 4 \times (2.7816\times 10^{-10} \ \text{F}) \approx 1.1126\times 10^{-9} \ \text{F}",
                    result=r"C \approx 1.1126 \times 10^{-9} \ \text{F}",
                    rationale="Η παρουσία του διηλεκτρικού τετραπλασιάζει τη χωρητικότητα.",
                ),
                CalculationStep(
                    step_number=5,
                    title="Έκφραση αποτελέσματος σε νανοφαράντ (nF) και πικοφαράντ (pF)",
                    formula=r"C \approx 1.113 \ \text{nF} = 1113 \ \text{pF}",
                    substitution=r"1.1126\times 10^{-9} \ \text{F} \times 10^9 \ \text{nF/F} \approx 1.113 \ \text{nF}",
                    result=r"C \approx 1.113 \ \text{nF} = 1113 \ \text{pF}",
                    rationale="Τυπική χωρητικότητα για πυκνωτή διαστάσεων εργαστηρίου.",
                ),
            ],
            final_answer=r"C \approx 1.113\text{ nF} = 1113\text{ pF}",
            detailed_justification="Η χωρητικότητα εξαρτάται μόνο από το εμβαδόν A, την απόσταση d και το διηλεκτρικό κ.",
            common_pitfalls=["Προσοχή στο εμβαδόν κύκλου: A = π R², όχι 2π R (που είναι η περιφέρεια)."],
            related_theory_topic="Πυκνωτές & Χωρητικότητα",
        ),
        ExamQuestion(
            question_number=6,
            title="Άσκηση 6: Ταχύτητα & Δύναμη Lorentz Επιταχυνόμενου Ηλεκτρονίου",
            question_type="Calculations",
            prompt_text=r"Ηλεκτρόνιο επιταχύνεται από τάση $V = 2500\text{ V}$ και εισέρχεται κάθετα σε $B = 0.5\text{ T}$. Υπολογίστε: α) Ταχύτητα $v$. β) Δύναμη Lorentz $F_B$.",
            given_parameters=[
                GivenParameter("V", "2500 \\text{ V}", "Τάση επιτάχυνσης"),
                GivenParameter("B", "0.5 \\text{ T}", "Μαγνητικό πεδίο"),
                GivenParameter("e", "1.602 \\times 10^{-19} \\text{ C}", "Φορτίο ηλεκτρονίου"),
                GivenParameter("m_e", "9.109 \\times 10^{-31} \\text{ kg}", "Μάζα ηλεκτρονίου"),
            ],
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ηλεκτρικό έργο και μετατροπή δυναμικής σε κινητική ενέργεια",
                    formula=r"W = e V = \Delta K = \frac{1}{2} m_e v^2",
                    substitution=r"e V = (1.602\times 10^{-19} \ \text{C}) \times (2500 \ \text{V}) = 4.005\times 10^{-16} \ \text{J}",
                    result=r"\frac{1}{2} m_e v^2 = 4.005\times 10^{-16} \ \text{J}",
                    rationale="Η ηλεκτροστατική διαφορά δυναμικού επιταχύνει το ηλεκτρόνιο από την ηρεμία.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Αλγεβρική επίλυση ταχύτητας v",
                    formula=r"v = \sqrt{\frac{2 e V}{m_e}}",
                    substitution=r"v = \sqrt{\frac{2 \times 4.005\times 10^{-16} \ \text{J}}{9.109\times 10^{-31} \ \text{kg}}} = \sqrt{\frac{8.010\times 10^{-16}}{9.109\times 10^{-31}}} = \sqrt{8.7935\times 10^{14}}",
                    result=r"v \approx 2.9654 \times 10^7 \ \text{m/s}",
                    rationale="Ταχύτητα κατά την είσοδο στην περιοχή του μαγνητικού πεδίου.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Έλεγχος σχετικιστικών επιδράσεων",
                    formula=r"\frac{v}{c} = \frac{2.9654\times 10^7 \ \text{m/s}}{3.0\times 10^8 \ \text{m/s}} \approx 0.0988 \approx 9.88\%",
                    substitution=r"\gamma = \frac{1}{\sqrt{1 - (v/c)^2}} = \frac{1}{\sqrt{1 - 0.00977}} \approx 1.0049",
                    result=r"\gamma \approx 1.005 \quad (\sigma\phi\acute{\alpha}\lambda\mu\alpha < 0.5\%)",
                    rationale="Η ταχύτητα παραμένει κάτω από το 10% του c, συνεπώς η κλασική νευτώνεια μηχανική παρέχει εξαιρετική ακρίβεια.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Μαθηματική διατύπωση μαγνητικής δύναμης Lorentz",
                    formula=r"\vec{F}_B = -e (\vec{v} \times \vec{B}) \implies F_B = e v B \sin\theta",
                    substitution=r"\theta = 90^\circ \implies \sin(90^\circ) = 1 \implies F_B = e v B",
                    result=r"F_B = e v B",
                    rationale="Η κάθετη είσοδος στο ομογενές πεδίο μεγιστοποιεί τη μαγνητική δύναμη Lorentz.",
                ),
                CalculationStep(
                    step_number=5,
                    title="Αριθμητικός υπολογισμός δύναμης Lorentz F_B",
                    formula=r"F_B = e v B",
                    substitution=r"F_B = (1.602\times 10^{-19} \ \text{C}) \times (2.9654\times 10^7 \ \text{m/s}) \times (0.50 \ \text{T})",
                    result=r"F_B \approx 2.3753 \times 10^{-12} \ \text{N}",
                    rationale="Έντονη δύναμη εκτροπής σε μικροσκοπικό επίπεδο.",
                ),
                CalculationStep(
                    step_number=6,
                    title="Υπολογισμός ακτίνας κυκλοτρονικής τροχιάς R",
                    formula=r"R = \frac{m_e v}{e B}",
                    substitution=r"R = \frac{(9.109\times 10^{-31} \ \text{kg}) \times (2.9654\times 10^7 \ \text{m/s})}{(1.602\times 10^{-19} \ \text{C}) \times (0.50 \ \text{T})} = \frac{2.7012\times 10^{-23}}{8.01\times 10^{-20}} \approx 3.372\times 10^{-4} \ \text{m}",
                    result=r"R \approx 3.372 \times 10^{-4} \ \text{m} \approx 0.337 \ \text{mm}",
                    rationale="Το ηλεκτρόνιο περιστρέφεται σε κύκλο ακτίνας μόλις 0.34 mm.",
                ),
            ],
            final_answer=r"v \approx 2.97\times 10^7\text{ m/s}, \quad F_B \approx 2.38\times 10^{-12}\text{ N}",
            detailed_justification="Κινητική ενέργεια e V μετατρέπεται σε μαγνητική κεντρομόλο δύναμη Lorentz.",
            common_pitfalls=["Μην ξεχάσετε τον συντελεστή 2 στο v = sqrt(2eV/m)."],
            related_theory_topic="Μαγνητική Δύναμη Lorentz",
        ),
        ExamQuestion(
            question_number=7,
            title="Άσκηση 7 & 8: Επίπεδο Κύμα Υπεριώδους & Διάνυσμα Poynting",
            question_type="Calculations",
            prompt_text=r"Το ηλεκτρικό πεδίο κύματος είναι $\vec{E} = 5\cos(2\times 10^7 x - \omega t)\hat{y}$. Βρείτε: α) $\lambda, \omega$. β) Το $\vec{B}(x,t)$. γ) Το διάνυσμα Poynting $\vec{S}$. δ) Την ένταση $I$.",
            given_parameters=[
                GivenParameter("E_0", "5 \\text{ V/m}", "Πλάτος πεδίου E"),
                GivenParameter("k", "2 \\times 10^7 \\text{ rad/m}", "Κυματάριθμος κατά x"),
                GivenParameter("c", "3 \\times 10^8 \\text{ m/s}", "Ταχύτητα φωτός"),
            ],
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Εξαγωγή παραμέτρων κύματος από τη γενική μορφή",
                    formula=r"\vec{E}(x,t) = E_0 \cos(k x - \omega t)\hat{u}_E",
                    substitution=r"E_0 = 5 \ \text{V/m}, \quad k = 2\times 10^7 \ \text{rad/m}, \quad \hat{u}_k = +\hat{x}, \quad \hat{u}_E = +\hat{y}",
                    result=r"\vec{E}(x,t) = 5\cos(2\times 10^7 x - \omega t)\hat{y} \ \text{V/m}",
                    rationale="Το κύμα διαδίδεται προς τα θετικά x με ηλεκτρικό πεδίο πολωμένο κατά y.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Υπολογισμός μήκους κύματος λ και φασματική περιοχή",
                    formula=r"\lambda = \frac{2\pi}{k}",
                    substitution=r"\lambda = \frac{2\pi}{2\times 10^7 \ \text{rad/m}} = \pi \times 10^{-7} \ \text{m} \approx 3.1416\times 10^{-7} \ \text{m} = 314.16 \ \text{nm}",
                    result=r"\lambda \approx 314.2 \ \text{nm} \quad (\text{Υπεριώδες UV-B / UV-A})",
                    rationale="Μήκος κύματος στο υπεριώδες φάσμα (κάτω από το όριο του ορατού στα 400 nm).",
                ),
                CalculationStep(
                    step_number=3,
                    title="Υπολογισμός κυκλικής συχνότητας ω",
                    formula=r"\omega = c k",
                    substitution=r"\omega = (3.0\times 10^8 \ \text{m/s}) \times (2\times 10^7 \ \text{rad/m}) = 6.00\times 10^{15} \ \text{rad/s}",
                    result=r"\omega = 6.00 \times 10^{15} \ \text{rad/s}",
                    rationale="Σχέση διασποράς στο κενό v = c = ω/k.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Υπολογισμός γραμμικής συχνότητας f και περιόδου T",
                    formula=r"f = \frac{\omega}{2\pi}, \quad T = \frac{1}{f}",
                    substitution=r"f = \frac{6.00\times 10^{15}}{2\pi} \approx 9.5493\times 10^{14} \ \text{Hz}, \quad T = \frac{1}{9.5493\times 10^{14}} \approx 1.047\times 10^{-15} \ \text{s}",
                    result=r"f \approx 954.9 \ \text{THz}, \quad T \approx 1.047 \ \text{fs}",
                    rationale="Περίοδος ταλάντωσης της τάξης του ενός femtosecond.",
                ),
                CalculationStep(
                    step_number=5,
                    title="Υπολογισμός πλάτους μαγνητικού πεδίου B_0",
                    formula=r"B_0 = \frac{E_0}{c}",
                    substitution=r"B_0 = \frac{5 \ \text{V/m}}{3.0\times 10^8 \ \text{m/s}} \approx 1.6667\times 10^{-8} \ \text{T} = 16.67 \ \text{nT}",
                    result=r"B_0 \approx 1.667 \times 10^{-8} \ \text{T}",
                    rationale="Λόγος πλατών E_0 / B_0 = c στο κενό.",
                ),
                CalculationStep(
                    step_number=6,
                    title="Διανυσματικός προσδιορισμός και εξίσωση μαγνητικού πεδίου B(x,t)",
                    formula=r"\hat{u}_E \times \hat{u}_B = \hat{u}_k \implies \hat{y} \times \hat{u}_B = +\hat{x} \implies \hat{u}_B = +\hat{z}",
                    substitution=r"\hat{y} \times \hat{z} = +\hat{x}, \quad \vec{B}(x,t) = B_0 \cos(k x - \omega t)\hat{z}",
                    result=r"\vec{B}(x,t) = 1.667\times 10^{-8}\cos(2\times 10^7 x - 6\times 10^{15} t)\hat{z} \ \text{T}",
                    rationale="Το μαγνητικό πεδίο είναι κάθετο τόσο στο E όσο και στην κατεύθυνση διάδοσης x.",
                ),
                CalculationStep(
                    step_number=7,
                    title="Υπολογισμός στιγμιαίου διανύσματος Poynting S(x,t)",
                    formula=r"\vec{S} = \frac{1}{\mu_0}(\vec{E}\times\vec{B}) = \frac{E_0 B_0}{\mu_0}\cos^2(kx - \omega t)\hat{x}",
                    substitution=r"S_{\max} = \frac{5 \times 1.6667\times 10^{-8}}{4\pi\times 10^{-7}} = \frac{8.3335\times 10^{-8}}{1.2566\times 10^{-6}} \approx 0.06631 \ \text{W/m}^2",
                    result=r"\vec{S}(x,t) \approx 0.06631 \cos^2(2\times 10^7 x - 6\times 10^{15} t)\hat{x} \ \text{W/m}^2",
                    rationale="Ροή ηλεκτρομαγνητικής ισχύος κατά τον άξονα +x.",
                ),
                CalculationStep(
                    step_number=8,
                    title="Υπολογισμός μέσης έντασης ακτινοβολίας I",
                    formula=r"I = \langle |\vec{S}| \rangle = \frac{1}{2} S_{\max} = \frac{E_0^2}{2\mu_0 c}",
                    substitution=r"I = \frac{1}{2}(0.06631 \ \text{W/m}^2) = \frac{25}{2(4\pi\times 10^{-7})(3\times 10^8)} \approx 0.03316 \ \text{W/m}^2",
                    result=r"I \approx 0.03316 \ \text{W/m}^2 = 33.16 \ \text{mW/m}^2",
                    rationale="Μέση χρονική ένταση της υπεριώδους δέσμης.",
                ),
            ],
            final_answer=r"\lambda \approx 314.2\text{ nm}, \ \omega = 6\times 10^{15}\text{ rad/s}, \ \vec{B} \approx 1.67\times 10^{-8}\cos(...)\hat{z}\text{ T}, \ I \approx 33.16\text{ mW/m}^2",
            detailed_justification="Επίπεδο υπεριώδες κύμα με διάδοση κατά x και πόλωση κατά y.",
            common_pitfalls=["Συνδυασμός εξωτερικού γινομένου: ŷ × ẑ = x̂."],
            related_theory_topic="ΗΜ Κύματα & Poynting",
        ),
        ExamQuestion(
            question_number=8,
            title="Άσκηση 9: Διάθλαση Snell & Κρίσιμη Γωνία",
            question_type="Calculations",
            prompt_text=r"Φως από γυαλί ($n_1 = 1.50$) σε νερό ($n_2 = 1.33$) με $\theta_1 = 35^\circ$. Υπολογίστε τη γωνία διάθλασης $\theta_2$ και την κρίσιμη γωνία $\theta_c$.",
            given_parameters=[
                GivenParameter("n_1", "1.50", "Δείκτης διάθλασης γυαλιού"),
                GivenParameter("n_2", "1.33", "Δείκτης διάθλασης νερού"),
                GivenParameter(r"\theta_1", r"35^\circ", "Γωνία πρόσπτωσης"),
            ],
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ανάλυση οπτικών μέσων και συνθήκη ολικής ανάκλασης",
                    formula=r"n_1 = 1.50 > n_2 = 1.33 \implies \text{Μετάβαση προς αραιότερο μέσο}",
                    substitution=r"\text{Η ακτίνα επιταχύνεται και απομακρύνεται από την κάθετο, υφίσταται ολική ανάκλαση αν } \theta_1 \ge \theta_c",
                    result=r"\text{Ύπαρξη κρίσιμης γωνίας } \theta_c",
                    rationale="Η ολική ανάκλαση είναι εφικτή μόνο όταν n_1 > n_2.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Εξαγωγή τύπου κρίσιμης γωνίας θ_c",
                    formula=r"n_1 \sin\theta_c = n_2 \sin(90^\circ) \implies \sin\theta_c = \frac{n_2}{n_1} \implies \theta_c = \arcsin\left(\frac{n_2}{n_1}\right)",
                    substitution=r"\sin\theta_c = \frac{1.33}{1.50} \approx 0.88667",
                    result=r"\sin\theta_c \approx 0.88667",
                    rationale="Στην κρίσιμη γωνία η διαθλώμενη ακτίνα εφάπτεται της διεπιφάνειας (θ_2 = 90°).",
                ),
                CalculationStep(
                    step_number=3,
                    title="Αριθμητικός υπολογισμός κρίσιμης γωνίας θ_c",
                    formula=r"\theta_c = \arcsin(0.88667)",
                    substitution=r"\theta_c = \arcsin(0.88667) \approx 1.0895 \ \text{rad} \approx 62.457^\circ",
                    result=r"\theta_c \approx 62.46^\circ",
                    rationale="Όριο πέρα από το οποίο δεν υπάρχει διαθλώμενη δέσμη.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Έλεγχος συνθήκης διάθλασης έναντι ολικής ανάκλασης",
                    formula=r"\theta_1 < \theta_c \implies \text{Κανονική διάθλαση στο νερό}",
                    substitution=r"35^\circ < 62.46^\circ",
                    result=r"\text{Συμβαίνει κανονική διάθλαση}",
                    rationale="Η δέσμη εισέρχεται κανονικά στο δεύτερο μέσο διότι η γωνία πρόσπτωσης είναι κάτω από την κρίσιμη.",
                ),
                CalculationStep(
                    step_number=5,
                    title="Εφαρμογή νόμου Snell για τον υπολογισμό του ημιτόνου θ_2",
                    formula=r"n_1 \sin\theta_1 = n_2 \sin\theta_2 \implies \sin\theta_2 = \frac{n_1}{n_2}\sin\theta_1",
                    substitution=r"\sin\theta_2 = \frac{1.50}{1.33} \sin(35^\circ) \approx 1.12782 \times 0.573576 \approx 0.64689",
                    result=r"\sin\theta_2 \approx 0.64689",
                    rationale="Υπολογισμός του ημιτόνου της γωνίας διάθλασης.",
                ),
                CalculationStep(
                    step_number=6,
                    title="Υπολογισμός γωνίας διάθλασης θ_2 και επαλήθευση",
                    formula=r"\theta_2 = \arcsin(\sin\theta_2)",
                    substitution=r"\theta_2 = \arcsin(0.64689) \approx 0.7036 \ \text{rad} \approx 40.306^\circ",
                    result=r"\theta_2 \approx 40.31^\circ \quad (\theta_2 > \theta_1)",
                    rationale="Η γωνία διάθλασης είναι μεγαλύτερη της γωνίας πρόσπτωσης (40.31° > 35°), επιβεβαιώνοντας την απομάκρυνση από την κάθετο.",
                ),
            ],
            final_answer=r"\theta_2 \approx 40.31^\circ, \quad \theta_c \approx 62.46^\circ",
            detailed_justification="Νόμος Snell σε διεπιφάνεια μετάβασης προς οπτικά αραιότερο μέσο.",
            common_pitfalls=["Μην αντιστρέψετε τους δείκτες διάθλασης: n1 είναι το μέσο πρόσπτωσης και n2 το μέσο διάθλασης."],
            related_theory_topic="Οπτική & Νόμος Snell",
        ),
        ExamQuestion(
            question_number=9,
            title="Άσκηση 10: Ηλεκτρικό Πεδίο Απειρομήκους Γραμμικής Κατανομής Φορτίου",
            question_type="Calculations",
            prompt_text=r"Ομοιόμορφη γραμμική κατανομή φορτίου με $\lambda = 3.0\text{ nC/m}$ εκτείνεται στον άξονα x. Υπολογίστε το ηλεκτρικό πεδίο στο σημείο $y = 4.0\text{ m}$ του άξονα y.",
            given_parameters=[
                GivenParameter(r"\lambda", "3.0 \\times 10^{-9} \\text{ C/m}", "Γραμμική πυκνότητα"),
                GivenParameter("y", "4.0 \\text{ m}", "Απόσταση από τον άξονα"),
            ],
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Γεωμετρική ανάλυση και κυλινδρική συμμετρία συστήματος",
                    formula=r"\vec{r} = y \hat{y} \implies r = 4.0 \ \text{m}, \quad \vec{E} = E(y)\hat{y}",
                    substitution=r"\text{Λόγω απειρομήκους συμμετρίας κατά τον άξονα x, οι οριζόντιες συνιστώσες } E_x \text{ αλληλοαναιρούνται ανά ζεύγη}",
                    result=r"\vec{E}(0, y, 0) = E(y)\hat{y}",
                    rationale="Το ηλεκτρικό πεδίο είναι αυστηρά ακτινικό ως προς τη γραμμική κατανομή φορτίου.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Επιλογή επιφάνειας Gauss και διατύπωση νόμου Gauss",
                    formula=r"\oint_{\mathcal{S}} \vec{E}\cdot d\vec{A} = \frac{Q_{\text{enc}}}{\epsilon_0}",
                    substitution=r"\text{Επιλέγουμε ομοαξονικό κύλινδρο ακτίνας } y \text{ και μήκους } L. \text{ Η ροή από τις βάσεις μηδενίζεται (} \vec{E}\perp \hat{n} \text{)}",
                    result=r"E (2\pi y L) = \frac{\lambda L}{\epsilon_0}",
                    rationale="Η ροή διέρχεται αποκλειστικά από την παράπλευρη επιφάνεια του κυλίνδρου.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Αλγεβρική εξαγωγή έντασης ηλεκτρικού πεδίου",
                    formula=r"E = \frac{\lambda}{2\pi \epsilon_0 y} = \frac{2 k_e \lambda}{y}",
                    substitution=r"k_e = \frac{1}{4\pi\epsilon_0} \implies \frac{1}{2\pi\epsilon_0} = 2 k_e",
                    result=r"E = \frac{2 k_e \lambda}{y}",
                    rationale="Κλασικός τύπος ηλεκτρικού πεδίου απειρομήκους φορτισμένου σύρματος.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Αριθμητική αντικατάσταση και υπολογισμός τιμής",
                    formula=r"E = \frac{2 k_e \lambda}{y}",
                    substitution=r"E = \frac{2 \times (8.988\times 10^9 \ \text{N}\cdot\text{m}^2/\text{C}^2) \times (3.0\times 10^{-9} \ \text{C/m})}{4.0 \ \text{m}} = \frac{53.928}{4.0}",
                    result=r"E = 13.482 \ \text{N/C} = 13.482 \ \text{V/m}",
                    rationale="Ακριβής αριθμητικός υπολογισμός της έντασης.",
                ),
                CalculationStep(
                    step_number=5,
                    title="Διανυσματικό αποτέλεσμα και κατεύθυνση",
                    formula=r"\vec{E} = E \hat{y} = 13.48 \ \text{V/m} \ \hat{y}",
                    substitution=r"\lambda > 0 \implies \text{Το πεδίο απομακρύνεται από το θετικό σύρμα κατά } +\hat{y}",
                    result=r"\vec{E} \approx 13.48 \ \text{V/m} \ \hat{y}",
                    rationale="Το πεδίο εξασθενεί αντιστρόφως ανάλογα με την απόσταση 1/y.",
                ),
            ],
            final_answer=r"\vec{E} \approx 13.48\text{ V/m} \ \hat{y}",
            detailed_justification="Το ηλεκτρικό πεδίο απειρομήκους σύρματος εξασθενεί αντιστρόφως ανάλογα της απόστασης 1/y.",
            common_pitfalls=["Προσοχή: για γραμμικό φορτίο το πεδίο μειώνεται ως 1/r και ΟΧΙ ως 1/r²."],
            related_theory_topic="Νόμος Gauss σε Κυλινδρική Συμμετρία",
        ),
        ExamQuestion(
            question_number=10,
            title="Άσκηση 11: Μαγνητική Ροπή σε Ρευματοφόρο Βρόχο",
            question_type="Calculations",
            prompt_text=r"Ορθογώνιος βρόχος $5\text{ cm} \times 10\text{ cm}$ διαρρέεται από $I = 2.0\text{ A}$ σε $B = 0.2\text{ T}$. Υπολογίστε τη ροπή $\tau$ όταν η γωνία της καθέτου με το $B$ είναι $30^\circ$.",
            given_parameters=[
                GivenParameter("A", "5 \\text{ cm} \\times 10 \\text{ cm} = 0.005 \\text{ m}^2", "Εμβαδόν βρόχου"),
                GivenParameter("I", "2.0 \\text{ A}", "Ρεύμα βρόχου"),
                GivenParameter("B", "0.2 \\text{ T}", "Μαγνητικό πεδίο"),
                GivenParameter(r"\theta", r"30^\circ", "Γωνία καθέτου με το B"),
            ],
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Υπολογισμός εμβαδού ορθογώνιου βρόχου σε μονάδες SI",
                    formula=r"A = a \times b",
                    substitution=r"a = 5 \ \text{cm} = 0.05 \ \text{m}, \quad b = 10 \ \text{cm} = 0.10 \ \text{m} \implies A = (0.05 \ \text{m}) \times (0.10 \ \text{m}) = 0.005 \ \text{m}^2",
                    result=r"A = 5.0 \times 10^{-3} \ \text{m}^2",
                    rationale="Γεωμετρικό εμβαδόν επιφάνειας που περικλείει ο βρόχος.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Υπολογισμός μαγνητικής διπολικής ροπής m του βρόχου",
                    formula=r"m = N I A",
                    substitution=r"N = 1, \quad I = 2.0 \ \text{A}, \quad A = 0.005 \ \text{m}^2 \implies m = (1)(2.0 \ \text{A})(0.005 \ \text{m}^2) = 0.010 \ \text{A}\cdot\text{m}^2",
                    result=r"m = 1.0 \times 10^{-2} \ \text{A}\cdot\text{m}^2 \quad (\text{ή } \text{J/T})",
                    rationale="Η μαγνητική ροπή δείχνει κάθετα στο επίπεδο του βρόχου κατά τον κανόνα του δεξιού χεριού.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Διατύπωση εξίσωσης μηχανικής ροπής σε μαγνητικό δίπολο",
                    formula=r"\vec{\tau} = \vec{m} \times \vec{B} \implies \tau = m B \sin\theta",
                    substitution=r"\theta = 30^\circ \text{ είναι η γωνία μεταξύ του διανύσματος } \vec{m} \text{ (κάθετος στο βρόχο) και του πεδίου } \vec{B}",
                    result=r"\tau = m B \sin\theta",
                    rationale="Εξωτερικό γινόμενο μαγνητικής διπολικής ροπής και μαγνητικής επαγωγής.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Αριθμητική αντικατάσταση και υπολογισμός ροπής",
                    formula=r"\tau = m B \sin(30^\circ)",
                    substitution=r"\tau = (0.010 \ \text{A}\cdot\text{m}^2) \times (0.20 \ \text{T}) \times \sin(30^\circ) = (0.0020) \times 0.50 = 1.00\times 10^{-3} \ \text{N}\cdot\text{m}",
                    result=r"\tau = 1.00 \times 10^{-3} \ \text{N}\cdot\text{m}",
                    rationale="Μηχανική ροπή στρέψης που ασκείται στον αγώγιμο βρόχο.",
                ),
                CalculationStep(
                    step_number=5,
                    title="Έκφραση αποτελέσματος σε mN·m και φυσική τάση ευθυγράμμισης",
                    formula=r"\tau = 1.0 \ \text{mN}\cdot\text{m}",
                    substitution=r"\text{Η ροπή τείνει να περιστρέψει τον βρόχο ώστε το } \vec{m} \text{ να ευθυγραμμιστεί με το } \vec{B} \ (\theta \to 0^\circ)",
                    result=r"\tau = 1.0 \ \text{mN}\cdot\text{m}",
                    rationale="Βασική αρχή λειτουργίας γαλβανομέτρων και ηλεκτρικών κινητήρων.",
                ),
            ],
            final_answer=r"\tau = 1.0 \times 10^{-3}\text{ N}\cdot\text{m} = 1.0\text{ mN}\cdot\text{m}",
            detailed_justification="Θεμελιώδης αρχή λειτουργίας των ηλεκτροκινητήρων συνεχούς και εναλλασσόμενου ρεύματος.",
            common_pitfalls=["Προσοχή: η γωνία θ δίνεται ως προς την κάθετο στο επίπεδο του βρόχου, άρα χρησιμοποιούμε κατευθείαν sin(30°)."],
            related_theory_topic="Μαγνητική Διπολική Ροπή & Ηλεκτροκινητήρες",
        ),
        ExamQuestion(
            question_number=11,
            title="Άσκηση 12: Ενέργεια Φωτονίου, Μήκος Κύματος & Ταξινόμηση Φάσματος",
            question_type="Calculations",
            prompt_text=r"Πηγή εκπέμπει φωτόνια με ενέργεια $E = 2.5\text{ eV}$. α) Ποιο είναι το μήκος κύματος σε νανόμετρα; β) Τι είδος ακτινοβολίας είναι; Δίνονται: $h = 6.626 \times 10^{-34}\text{ J}\cdot\text{s}, 1\text{ eV} = 1.6 \times 10^{-19}\text{ J}$.",
            given_parameters=[
                GivenParameter("E", "2.5 \\text{ eV} = 4.0 \\times 10^{-19} \\text{ J}", "Ενέργεια φωτονίου"),
                GivenParameter("h", "6.626 \\times 10^{-34} \\text{ J}\\cdot\\text{s}", "Σταθερά Planck"),
                GivenParameter("c", "3 \\times 10^8 \\text{ m/s}", "Ταχύτητα φωτός"),
            ],
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Μετατροπή ενέργειας φωτονίου από ηλεκτρονιοβόλτ (eV) σε Joules (J)",
                    formula=r"E(\text{J}) = E(\text{eV}) \times e",
                    substitution=r"E = 2.5 \ \text{eV} \times (1.602\times 10^{-19} \ \text{J/eV}) = 4.005\times 10^{-19} \ \text{J}",
                    result=r"E \approx 4.005 \times 10^{-19} \ \text{J}",
                    rationale="Μετατροπή σε μονάδα ενέργειας του SI.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Εφαρμογή σχέσης Planck-Einstein για το μήκος κύματος",
                    formula=r"E = h f = \frac{h c}{\lambda} \implies \lambda = \frac{h c}{E}",
                    substitution=r"h c = (6.626\times 10^{-34} \ \text{J}\cdot\text{s}) \times (3.0\times 10^8 \ \text{m/s}) = 1.9878\times 10^{-25} \ \text{J}\cdot\text{m}",
                    result=r"\lambda = \frac{h c}{E}",
                    rationale="Σύνδεση κβαντικής ενέργειας φωτονίου με το κυματικό του μήκος.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Αριθμητικός υπολογισμός μήκους κύματος λ σε μέτρα",
                    formula=r"\lambda = \frac{1.9878\times 10^{-25} \ \text{J}\cdot\text{m}}{4.005\times 10^{-19} \ \text{J}}",
                    substitution=r"\lambda = \frac{1.9878\times 10^{-25}}{4.005\times 10^{-19}} \approx 4.9633\times 10^{-7} \ \text{m}",
                    result=r"\lambda \approx 4.963 \times 10^{-7} \ \text{m}",
                    rationale="Μήκος κύματος στο κενό.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Μετατροπή σε νανόμετρα (nm)",
                    formula=r"\lambda(\text{nm}) = \lambda(\text{m}) \times 10^9 \ \text{nm/m}",
                    substitution=r"\lambda = (4.9633\times 10^{-7} \ \text{m}) \times 10^9 \approx 496.3 \ \text{nm} \approx 497 \ \text{nm}",
                    result=r"\lambda \approx 497 \ \text{nm}",
                    rationale="Η τυπική μονάδα μέτρησης οπτικών μηκών κύματος.",
                ),
                CalculationStep(
                    step_number=5,
                    title="Ταξινόμηση στο ηλεκτρομαγνητικό φάσμα",
                    formula=r"400 \ \text{nm} \le \lambda \le 700 \ \text{nm} \implies \text{Ορατό Φάσμα (Κυανό / Πρασινομπλέ)}",
                    substitution=r"\lambda \approx 497 \ \text{nm} \in [480 \ \text{nm}, 520 \ \text{nm}]",
                    result=r"\text{Ορατό Φως (Cyan / Blue-Green)}",
                    rationale="Ακτινοβολία στην περιοχή μέγιστης ευαισθησίας της ανθρώπινης όρασης.",
                ),
            ],
            final_answer=r"\lambda \approx 497\text{ nm} \quad (\text{Ορατό Φως — Κυανό/Πράσινο})",
            detailed_justification="Σύνδεση κβαντικής θεωρίας φωτονίων (Planck) με την κλασική ηλεκτρομαγνητική κυματική οπτική.",
            common_pitfalls=["Μετατρέψτε πάντα τα electron-volts (eV) σε Joules πολλαπλασιάζοντας με 1.6×10⁻¹⁹."],
            related_theory_topic="Ηλεκτρομαγνητικό Φάσμα & Φωτόνια",
        ),
    ]

    justifications = [
        DesignJustification(
            title="Κβαντική Ενέργεια Φωτονίου (E = hf)",
            category="Quantum Wave",
            description="Η ενέργεια κάθε φωτονίου συνδέεται άμεσα με τη συχνότητα της κλασικής ηλεκτρομαγνητικής ταλάντωσης μέσω της σταθεράς Planck h.",
            rationale="Επιτρέπει την ταξινόμηση και κατανόηση της αλληλεπίδρασης της ακτινοβολίας με την ύλη.",
        ),
        DesignJustification(
            title="Μαγνητική Ροπή Βρόχου (τ = m × B)",
            category="Torque Law",
            description="Ρευματοφόρος βρόχος σε εξωτερικό μαγνητικό πεδίο δέχεται μηχανική ροπή που τείνει να ευθυγραμμίσει τη μαγνητική του διπολική ροπή με το εξωτερικό πεδίο.",
            rationale="Θεμέλιος νόμος για κάθε σύγχρονο ηλεκτροκινητήρα και ηλεκτρομηχανική διάταξη.",
        ),
    ]

    solution_code = '''"""Python verification script for Practice Exam 3."""

import math

def verify_practice_3() -> None:
    """Verifies all exercises from Practice Exam 3."""
    # Coulomb 3-charges
    k_e = 8.988e9
    F13 = k_e * 5e-6 * 1e-6 / 36.0
    F23 = k_e * 2e-6 * 1e-6 / 9.0
    F_net = F13 - F23
    print(f"3. Coulomb F_net = {F_net*1000:.3f} mN (left)")

    # Cylinder wire
    mu_0 = 4 * math.pi * 1e-7
    I = 50.0
    R = 0.04
    B_in = (mu_0 * I * 0.02) / (2 * math.pi * R**2)
    B_out = (mu_0 * I) / (2 * math.pi * 0.08)
    print(f"4. Cylinder: B(2cm) = {B_in*1e6:.1f} uT, B(8cm) = {B_out*1e6:.1f} uT")

    # Capacitor
    eps_0 = 8.854e-12
    C = 4.0 * eps_0 * (math.pi * 0.1**2) / 0.001
    print(f"5. Capacitor: C = {C*1e9:.3f} nF")

    # Electron in B
    e = 1.6e-19
    m = 9.11e-31
    v = math.sqrt(2 * e * 2500 / m)
    F_B = e * v * 0.5
    print(f"6. Electron: v = {v:.3e} m/s, F_B = {F_B:.3e} N")

    # Wave UV
    c = 3e8
    k = 2e7
    wavelength = 2 * math.pi / k
    f = c / wavelength
    intensity = 5.0**2 / (2 * mu_0 * c)
    print(f"7. Wave: lambda = {wavelength*1e9:.1f} nm, I = {intensity*1000:.2f} mW/m^2")

    # Snell
    sin_c = 1.33 / 1.50
    sin_2 = (1.50 / 1.33) * math.sin(math.radians(35))
    print(f"9. Snell: theta_c = {math.degrees(math.asin(sin_c)):.2f} deg, theta_2 = {math.degrees(math.asin(sin_2)):.2f} deg")

    # Wire field
    E_wire = 3e-9 / (2 * math.pi * eps_0 * 4.0)
    print(f"10. Line Charge: E = {E_wire:.2f} V/m")

    # Torque
    tau = 2.0 * (0.05 * 0.10) * 0.2 * math.sin(math.radians(30))
    print(f"11. Torque: tau = {tau*1000:.2f} mN*m")

    # Photon
    h = 6.626e-34
    lam_photon = h * c / (2.5 * e)
    print(f"12. Photon: lambda = {lam_photon*1e9:.1f} nm (Visible Cyan)")

if __name__ == "__main__":
    verify_practice_3()
'''

    return Scenario(
        id="synth_exam_3_full_spectrum",
        title="Θέμα Εξάσκησης 3 — Πλήρες Φάσμα & Μαγνητική Ροπή",
        subtitle="Πλήρης Επίλυση: Ampère Κυλίνδρου, Lorentz, Ροπή Βρόχου, UV Κύμα & Φωτόνια",
        course_tag="Practice Exam 03",
        duration_info="Διάρκεια: 3 ώρες | 10 Ερωτήσεις Θεωρίας & 10 Ασκήσεις Υπολογισμού",
        paragraphs=paragraphs,
        questions=questions,
        justifications=justifications,
        solution_code=solution_code,
    )
