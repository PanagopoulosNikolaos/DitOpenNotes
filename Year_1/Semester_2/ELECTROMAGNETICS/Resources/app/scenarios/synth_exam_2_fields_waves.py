"""Practice Exam Scenario 2: Electromagnetic Fields, Waves, Coulomb Forces & Snell Refraction.

Verbatim transcription of practice exam 2 with three-part contract hover tooltips,
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


def createSynthExam2FieldsWaves() -> Scenario:
    """Instantiates the Practice Exam 2 scenario.

    Returns:
        Scenario: Complete scenario container with verbatim text and solutions.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(
                    text="Τεστ: Αρχές Ηλεκτρομαγνητισμού και Τηλεπικοινωνιών (Εξάσκηση 2)\n",
                    is_highlight=False,
                ),
                TextSegment(
                    text="Οδηγίες: Απαντήστε σαφώς και συνοπτικά. Σταθερές: ε₀ ≈ 8.85×10⁻¹² F/m, μ₀ = 4π×10⁻⁷ Tm/A, c ≈ 3×10⁸ m/s.",
                    is_highlight=False,
                ),
            ],
            accent_border_color=None,
        ),
        Paragraph(
            segments=[
                TextSegment(text="Μέρος Α: Ερωτήσεις Θεωρίας\n", is_highlight=False),
                TextSegment(text="1. ", is_highlight=False),
                TextSegment(
                    text="Σύγκριση Ηλεκτροστατικών και Μαγνητοστατικών Πεδίων",
                    is_highlight=True,
                    category="law",
                    tag_label="E vs B ΠΗΓΕΣ",
                    tooltip="Classification: Σύγκριση Θεμελιωδών Πεδίων | Detection Clue: 'πηγές, δυναμικές γραμμές' | Application Rationale: Ηλεκτροστατικό: πηγές ακίνητα φορτία, ανοικτές γραμμές (div D = ρ). Μαγνητοστατικό: πηγές κινούμενα φορτία/ρεύματα, κλειστές γραμμές (div B = 0).",
                ),
                TextSegment(text=": Περιγράψτε τις κύριες πηγές των ηλεκτροστατικών και μαγνητοστατικών πεδίων. Εξηγήστε τη διαφορά μεταξύ των δυναμικών γραμμών κάθε πεδίου και συνδέστε τη με τον Νόμο Gauss.\n", is_highlight=False),
                TextSegment(text="2. ", is_highlight=False),
                TextSegment(
                    text="Αγωγοί και Διηλεκτρικά σε Ηλεκτρικό Πεδίο",
                    is_highlight=True,
                    category="field",
                    tag_label="ΑΓΩΓΟΙ & ΔΙΗΛΕΚΤΡΙΚΑ",
                    tooltip="Classification: Συμπεριφορά Υλικών σε Πεδίο | Detection Clue: 'Αγωγοί και Διηλεκτρικά' | Application Rationale: Αγωγοί: ελεύθερα φορτία μηδενίζουν το πεδίο στο εσωτερικό (E_in = 0). Διηλεκτρικά: δέσμια δίπολα μειώνουν το πεδίο κατά E = E_0/κ.",
                ),
                TextSegment(text=": α) Τι συμβαίνει στα ελεύθερα φορτία εντός αγώγιμου υλικού όταν τοποθετείται σε εξωτερικό πεδίο; Περιγράψτε το τελικό πεδίο στο εσωτερικό. β) Εξηγήστε την ηλεκτρική πόλωση σε διηλεκτρικό και την επίδρασή της στο συνολικό πεδίο.", is_highlight=False),
            ],
            accent_border_color="accent",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Μέρος Β: Ασκήσεις\n", is_highlight=False),
                TextSegment(text="3. Επίπεδο Ηλεκτρομαγνητικό Κύμα:\nΤο μαγνητικό πεδίο δίνεται από τη σχέση: ", is_highlight=False),
                TextSegment(
                    text="B = (8.25·10⁻⁹ T) cos(kz + 2.70·10¹⁵ t) î",
                    is_highlight=True,
                    category="field",
                    tag_label="B(z,t)",
                    tooltip="Classification: Μαγνητικό Πεδίο Ανάστροφης Διάδοσης | Detection Clue: Όρισμα (kz + ωt) î | Application Rationale: Το πρόσημο +ωt υποδεικνύει διάδοση προς -z. Το E ταλαντώνεται κατά +j (ŷ) ώστε E x B να δείχνει προς -z.",
                ),
                TextSegment(text=".\nα) Προς ποια κατεύθυνση διαδίδεται; β) Βρείτε f και λ. γ) Γράψτε την εξίσωση για το E. δ) Υπολογίστε την ένταση I.\n", is_highlight=False),
                TextSegment(text="4. Ηλεκτροστατική Δύναμη:\nΤρία φορτία στον άξονα x: ", is_highlight=False),
                TextSegment(
                    text="q₁ = +4.0 μC (x = 0), q₂ = -2.0 μC (x = 3.0 m), q₃ = +6.0 μC (x = 5.0 m)",
                    is_highlight=True,
                    category="param",
                    tag_label="3 ΦΟΡΤΙΑ",
                    tooltip="Classification: Διάταξη Σημειακών Φορτίων | Detection Clue: q_1, q_2, q_3 σε θέσεις x | Application Rationale: Εφαρμογή αρχής επαλληλίας Coulomb στο κεντρικό φορτίο q_2.",
                ),
                TextSegment(text=".\nΥπολογίστε το μέτρο και την κατεύθυνση της συνολικής δύναμης στο q₂.\n", is_highlight=False),
                TextSegment(text="5. Μαγνητικό Πεδίο από Ρεύμα:\nΕυθύγραμμο σύρμα διαρρέεται από ", is_highlight=False),
                TextSegment(
                    text="I = 20 A",
                    is_highlight=True,
                    category="param",
                    tag_label="ΡΕΥΜΑ 20A",
                    tooltip="Classification: Ρεύμα Ευθύγραμμου Αγωγού | Detection Clue: I = 20 A, r = 5.0 cm | Application Rationale: B = μ_0 I / (2π r).",
                ),
                TextSegment(text=" σε απόσταση r = 5.0 cm. Υπολογίστε το B.\n", is_highlight=False),
                TextSegment(text="6. Επίπεδος Πυκνωτής με Διηλεκτρικό:\nΠυκνωτής με ", is_highlight=False),
                TextSegment(
                    text="A = 150 cm², d = 2.0 mm, κ = 3.5, V = 24 V",
                    is_highlight=True,
                    category="param",
                    tag_label="ΠΥΚΝΩΤΗΣ 24V",
                    tooltip="Classification: Παράμετροι Πυκνωτή | Detection Clue: A, d, κ, V | Application Rationale: C = κ ε_0 A/d, Q = CV, E = V/d.",
                ),
                TextSegment(text=".\nα) Ποια είναι η C; β) Πόσο φορτίο Q αποθηκεύεται; γ) Ποιο το πεδίο E;\n", is_highlight=False),
                TextSegment(text="7. Ανάκλαση και Διάθλαση:\nΔέσμη φωτός από ", is_highlight=False),
                TextSegment(
                    text="γυαλί (n₁ = 1.52) σε νερό (n₂ = 1.33) με θ₁ = 35°",
                    is_highlight=True,
                    category="law",
                    tag_label="ΝΟΜΟΣ SNELL",
                    tooltip="Classification: Διάθλαση Snell & Κρίσιμη Γωνία | Detection Clue: n_1, n_2, θ_1 | Application Rationale: sin(θ_c) = n_2/n_1, n_1 sin(θ_1) = n_2 sin(θ_2).",
                ),
                TextSegment(text=".\nα) Θα διαθλαστεί; Δικαιολογήστε υπολογίζοντας την κρίσιμη γωνία. β) Υπολογίστε τη γωνία διάθλασης θ₂.", is_highlight=False),
            ],
            accent_border_color="accent",
        ),
    ]

    questions = [
        ExamQuestion(
            question_number=1,
            title="Σύγκριση Ηλεκτροστατικών & Μαγνητοστατικών Πεδίων",
            question_type="Theory Analysis",
            prompt_text="Περιγράψτε τις κύριες πηγές των ηλεκτροστατικών και μαγνητοστατικών πεδίων. Εξηγήστε τη διαφορά μεταξύ των δυναμικών γραμμών κάθε πεδίου και συνδέστε τη με τον Νόμο Gauss.",
            options=[],
            final_answer="Ηλεκτροστατικό: Πηγές τα ακίνητα φορτία (ανοικτές γραμμές, div D = ρ). Μαγνητοστατικό: Πηγές τα ρεύματα (κλειστές γραμμές, div B = 0).",
            detailed_justification="Στο ηλεκτροστατικό πεδίο υπάρχουν απομονωμένα θετικά και αρνητικά φορτία (πηγές και καταβόθρες). Στο μαγνητικό πεδίο δεν υπάρχουν μονόπολα (div B = 0), άρα οι δυναμικές γραμμές είναι αναγκαστικά κλειστοί συνεχείς βρόχοι.",
            common_pitfalls=["Μην ξεχνάτε τη μαθηματική διατύπωση των νόμων Gauss: ∮ D·dS = Q_enc και ∮ B·dS = 0."],
            related_theory_topic="Ηλεκτροστατική & Μαγνητοστατική",
        ),
        ExamQuestion(
            question_number=2,
            title="Αγωγοί & Διηλεκτρικά σε Εξωτερικό Πεδίο",
            question_type="Theory Analysis",
            prompt_text="α) Τι συμβαίνει στα ελεύθερα φορτία αγωγού σε στατικό πεδίο; Περιγράψτε το τελικό πεδίο στο εσωτερικό. β) Εξηγήστε την ηλεκτρική πόλωση σε διηλεκτρικό και την επίδρασή της στο συνολικό πεδίο.",
            options=[],
            final_answer="Αγωγός: E_in = 0 (πλήρης εξουδετέρωση). Διηλεκτρικό: E = E_0 / κ (μερική μείωση λόγω δεσμίων διπόλων).",
            detailed_justification="Στον αγωγό τα ελεύθερα ηλεκτρόνια κινούνται ακαριαία στην επιφάνεια μέχρι να ακυρώσουν πλήρως το εξωτερικό πεδίο (E_internal = 0). Στο διηλεκτρικό δεν υπάρχουν ελεύθερα φορτία, αλλά τα δέσμια δίπολα προσανατολίζονται δημιουργώντας αντίθετο πεδίο πόλωσης P που εξασθενεί το αρχικό πεδίο κατά τον συντελεστή κ = ε_r.",
            common_pitfalls=["Στο διηλεκτρικό το πεδίο ΔΕΝ μηδενίζεται ποτέ, απλώς μειώνεται."],
            related_theory_topic="Αγωγοί, Διηλεκτρικά & Πόλωση",
        ),
        ExamQuestion(
            question_number=3,
            title="Άσκηση 3: Κύμα με Ανάστροφη Διάδοση κατά -z",
            question_type="Calculations",
            prompt_text=r"Το μαγνητικό πεδίο δίνεται από: $\vec{B} = (8.25 \times 10^{-9}\text{ T})\cos(kz + 2.70 \times 10^{15} t)\hat{i}$. α) Προς ποια κατεύθυνση διαδίδεται; β) Βρείτε $f$ και $\lambda$. γ) Γράψτε την εξίσωση για το $\vec{E}$. δ) Υπολογίστε την ένταση $I$.",
            given_parameters=[
                GivenParameter("B_0", "8.25 \\times 10^{-9} \\text{ T}", "Πλάτος μαγνητικού πεδίου"),
                GivenParameter(r"\omega", "2.70 \\times 10^{15} \\text{ rad/s}", "Κυκλική συχνότητα"),
                GivenParameter("c", "3 \\times 10^8 \\text{ m/s}", "Ταχύτητα φωτός στο κενό"),
                GivenParameter(r"\mu_0", r"4\pi \times 10^{-7} \text{ T}\cdot\text{m/A}", "Μαγνητική διαπερατότητα κενού"),
            ],
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Προσδιορισμός κατεύθυνσης διάδοσης",
                    formula=r"\phi = kz + \omega t \implies \text{Κατεύθυνση } -z \ (\text{ή } -\hat{k})",
                    substitution=r"\text{Το θετικό πρόσημο (+ωt) σημαίνει διάδοση προς τα αρνητικά } z",
                    result=r"\text{Κατεύθυνση: } -\hat{z} \ (\text{αρνητικός άξονας } z)",
                    rationale="Όταν τα πρόσημα των k και ω είναι ομόσημα (+kz + ωt), το κύμα ταξιδεύει προς τα -z.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Υπολογισμός συχνότητας f, κυματάριθμου k και μήκους κύματος λ",
                    formula=r"f = \frac{\omega}{2\pi}, \quad k = \frac{\omega}{c}, \quad \lambda = \frac{c}{f}",
                    substitution=r"f = \frac{2.70\times 10^{15}}{2\pi} \approx 4.297 \times 10^{14} \ \text{Hz}, \quad k = \frac{2.70\times 10^{15}}{3\times 10^8} = 9.0\times 10^6 \ \text{rad/m}, \quad \lambda = \frac{3\times 10^8}{4.297\times 10^{14}}",
                    result=r"f \approx 4.30 \times 10^{14} \ \text{Hz}, \quad \lambda \approx 6.981 \times 10^{-7} \ \text{m} = 698.1 \ \text{nm}",
                    rationale="Μήκος κύματος 698 nm στο ερυθρό τμήμα του ορατού φάσματος.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Προσδιορισμός πλάτους και διανύσματος ηλεκτρικού πεδίου E",
                    formula=r"E_0 = c B_0, \quad \hat{E} \times \hat{B} = \hat{k}_{\text{dir}} = -\hat{z} \implies \hat{E} \times \hat{x} = -\hat{z} \implies \hat{E} = +\hat{y}",
                    substitution=r"E_0 = (3\times 10^8)(8.25\times 10^{-9}) = 2.475 \ \text{V/m}, \quad \hat{y} \times \hat{x} = -\hat{z}",
                    result=r"\vec{E}(z,t) = 2.475 \cos(9.0\times 10^6 z + 2.70\times 10^{15} t)\hat{j} \quad [\text{V/m}]",
                    rationale="Επειδή ŷ × x̂ = -ẑ, το ηλεκτρικό πεδίο ταλαντώνεται κατά τον άξονα +y (ĵ).",
                ),
                CalculationStep(
                    step_number=4,
                    title="Υπολογισμός μέσης έντασης ακτινοβολίας I",
                    formula=r"I = \frac{E_0 B_0}{2\mu_0} = \frac{1}{2} c \epsilon_0 E_0^2",
                    substitution=r"I = \frac{2.475 \times 8.25\times 10^{-9}}{2 \times 4\pi\times 10^{-7}} = \frac{2.041875\times 10^{-8}}{2.51327\times 10^{-6}}",
                    result=r"I \approx 8.125 \times 10^{-3} \ \text{W/m}^2 = 8.125 \ \text{mW/m}^2",
                    rationale="Μέση ένταση ακτινοβολίας του ορατού κύματος.",
                ),
            ],
            final_answer=r"\text{Διάδοση: } -z, \ f \approx 4.30\times 10^{14}\text{ Hz}, \ \lambda \approx 698.1\text{ nm}, \ \vec{E} = 2.475\cos(...)\hat{j}\text{ V/m}, \ I \approx 8.13\text{ mW/m}^2",
            detailed_justification="Το πρόσημο + εμπρός από το ωt καθορίζει διάδοση προς τα -z, επιβάλλοντας E κατά +y.",
            common_pitfalls=["Προσοχή στο εξωτερικό γινόμενο: ŷ × x̂ = -ẑ, άρα το E είναι κατά +y και ΟΧΙ κατά -y."],
            related_theory_topic="Επίπεδα Ηλεκτρομαγνητικά Κύματα",
        ),
        ExamQuestion(
            question_number=4,
            title="Άσκηση 4: Ηλεκτροστατική Δύναμη Coulomb 3 Σημειακών Φορτίων",
            question_type="Calculations",
            prompt_text=r"Τρία σημειακά φορτία στον άξονα x: $q_1 = +4.0\,\mu\text{C}$ στο $x = 0$, $q_2 = -2.0\,\mu\text{C}$ στο $x = 3.0\text{ m}$, $q_3 = +6.0\,\mu\text{C}$ στο $x = 5.0\text{ m}$. Υπολογίστε το μέτρο και την κατεύθυνση της συνολικής δύναμης στο $q_2$.",
            given_parameters=[
                GivenParameter("q_1", "+4.0 \\times 10^{-6} \\text{ C}", "Φορτίο στο x=0"),
                GivenParameter("q_2", "-2.0 \\times 10^{-6} \\text{ C}", "Φορτίο στο x=3.0 m"),
                GivenParameter("q_3", "+6.0 \\times 10^{-6} \\text{ C}", "Φορτίο στο x=5.0 m"),
                GivenParameter("k_e", "8.988 \\times 10^9 \\text{ N}\\cdot\\text{m}^2/\\text{C}^2", "Ηλεκτροστατική σταθερά Coulomb"),
            ],
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Υπολογισμός δύναμης F_12 από το q_1 στο q_2",
                    formula=r"F_{12} = k_e \frac{|q_1 q_2|}{r_{12}^2} \quad (\text{Ελκτική προς } x=0, \text{δηλαδή } -\hat{x})",
                    substitution=r"F_{12} = 8.988\times 10^9 \frac{(4.0\times 10^{-6})(2.0\times 10^{-6})}{3.0^2} = \frac{7.1904\times 10^{-2}}{9}",
                    result=r"F_{12} \approx 7.989 \times 10^{-3} \ \text{N} = 7.99 \ \text{mN} \quad (\text{προς } -\hat{x})",
                    rationale="Ετερόσημα φορτία (θετικό q1 και αρνητικό q2) έλκονται, άρα το q2 έλκεται προς τα αριστερά.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Υπολογισμός δύναμης F_32 από το q_3 στο q_2",
                    formula=r"F_{32} = k_e \frac{|q_3 q_2|}{r_{23}^2} \quad (\text{Ελκτική προς } x=5, \text{δηλαδή } +\hat{x})",
                    substitution=r"r_{23} = 5.0 - 3.0 = 2.0 \ \text{m}, \quad F_{32} = 8.988\times 10^9 \frac{(6.0\times 10^{-6})(2.0\times 10^{-6})}{2.0^2} = \frac{0.107856}{4}",
                    result=r"F_{32} \approx 2.696 \times 10^{-2} \ \text{N} = 26.96 \ \text{mN} \quad (\text{προς } +\hat{x})",
                    rationale="Το q2 έλκεται από το θετικό q3 προς τα δεξιά.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Συνολική συνισταμένη δύναμη F_net στο q_2",
                    formula=r"\vec{F}_{\text{net}} = \vec{F}_{32} + \vec{F}_{12} = (F_{32} - F_{12})\hat{x}",
                    substitution=r"F_{\text{net}} = 26.96 \ \text{mN} - 7.99 \ \text{mN} = +18.97 \ \text{mN}",
                    result=r"\vec{F}_{\text{net}} \approx +18.97 \ \text{mN} \ \hat{x} \quad (\text{προς τα δεξιά})",
                    rationale="Η έλξη από το πλησιέστερο και ισχυρότερο q3 υπερισχύει.",
                ),
            ],
            final_answer=r"\vec{F}_{\text{net}} \approx 18.97\text{ mN} \ \hat{x} \quad (\text{μέτρο } 1.90\times 10^{-2}\text{ N προς τα δεξιά})",
            detailed_justification="Εφαρμογή της αρχής επαλληλίας του νόμου Coulomb στον άξονα x.",
            common_pitfalls=["Προσοχή στην απόσταση r_23: είναι 5 - 3 = 2 m, ΟΧΙ 5 m."],
            related_theory_topic="Ηλεκτροστατική & Νόμος Coulomb",
        ),
        ExamQuestion(
            question_number=5,
            title="Άσκηση 5: Μαγνητικό Πεδίο Ευθύγραμμου Ρευματοφόρου Αγωγού",
            question_type="Calculations",
            prompt_text=r"Μακρύ ευθύγραμμο σύρμα διαρρέεται από ρεύμα $I = 20\text{ A}$. Υπολογίστε το μαγνητικό πεδίο $B$ σε απόσταση $r = 5.0\text{ cm}$.",
            given_parameters=[
                GivenParameter("I", "20 \\text{ A}", "Ρεύμα αγωγού"),
                GivenParameter("r", "5.0 \\text{ cm} = 0.05 \\text{ m}", "Κάθετη απόσταση"),
                GivenParameter(r"\mu_0", r"4\pi \times 10^{-7} \text{ T}\cdot\text{m/A}", "Μαγνητική διαπερατότητα κενού"),
            ],
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Εφαρμογή νόμου Ampère",
                    formula=r"B = \frac{\mu_0 I}{2\pi r}",
                    substitution=r"B = \frac{4\pi\times 10^{-7} \times 20}{2\pi \times 0.05} = \frac{2\times 10^{-7} \times 20}{0.05} = \frac{4\times 10^{-6}}{0.05}",
                    result=r"B = 8.0 \times 10^{-5} \ \text{T} = 80 \ \mu\text{T}",
                    rationale="Το μαγνητικό πεδίο μειώνεται αντιστρόφως ανάλογα της απόστασης 1/r.",
                ),
            ],
            final_answer=r"B = 80\ \mu\text{T} = 8.0\times 10^{-5}\text{ T}",
            detailed_justification="Κλασική εφαρμογή του νόμου Ampère γύρω από απειρομήκη ευθύγραμμο αγωγό.",
            common_pitfalls=["Μετατρέψτε τα εκατοστά σε μέτρα: 5.0 cm = 0.05 m."],
            related_theory_topic="Μαγνητοστατική & Νόμος Ampère",
        ),
        ExamQuestion(
            question_number=6,
            title="Άσκηση 6: Επίπεδος Πυκνωτής με Διηλεκτρικό",
            question_type="Calculations",
            prompt_text=r"Επίπεδος πυκνωτής έχει $A = 150\text{ cm}^2$, $d = 2.0\text{ mm}$, $\kappa = 3.5$ και $V = 24\text{ V}$. α) Χωρητικότητα $C$. β) Φορτίο $Q$. γ) Ηλεκτρικό πεδίο $E$.",
            given_parameters=[
                GivenParameter("A", "150 \\text{ cm}^2 = 0.015 \\text{ m}^2", "Εμβαδόν οπλισμών"),
                GivenParameter("d", "2.0 \\text{ mm} = 0.002 \\text{ m}", "Απόσταση οπλισμών"),
                GivenParameter(r"\kappa", "3.5", "Διηλεκτρική σταθερά"),
                GivenParameter("V", "24 \\text{ V}", "Εφαρμοζόμενη τάση"),
            ],
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Υπολογισμός χωρητικότητας C",
                    formula=r"C = \kappa \epsilon_0 \frac{A}{d}",
                    substitution=r"C = 3.5 \times 8.854\times 10^{-12} \times \frac{0.015}{0.002} = 3.5 \times 8.854\times 10^{-12} \times 7.5",
                    result=r"C \approx 2.324 \times 10^{-10} \ \text{F} \approx 232.4 \ \text{pF}",
                    rationale="Χωρητικότητα με διηλεκτρικό.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Υπολογισμός αποθηκευμένου φορτίου Q",
                    formula=r"Q = C V",
                    substitution=r"Q = (2.324\times 10^{-10} \ \text{F})(24 \ \text{V})",
                    result=r"Q \approx 5.578 \times 10^{-9} \ \text{C} = 5.58 \ \text{nC}",
                    rationale="Φορτίο για τάση 24 V.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Υπολογισμός έντασης ηλεκτρικού πεδίου E",
                    formula=r"E = \frac{V}{d}",
                    substitution=r"E = \frac{24}{0.002}",
                    result=r"E = 12000 \ \text{V/m} = 12 \ \text{kV/m}",
                    rationale="Το πεδίο είναι ομογενές μεταξύ των οπλισμών.",
                ),
            ],
            final_answer=r"C \approx 232.4\text{ pF}, \quad Q \approx 5.58\text{ nC}, \quad E = 12\text{ kV/m}",
            detailed_justification="Το πεδίο E = V/d εξαρτάται μόνο από την τάση και την απόσταση, ενώ το φορτίο Q αυξάνεται λόγω του διηλεκτρικού.",
            common_pitfalls=["Προσοχή: το E = V/d παραμένει 12 kV/m όσο η πηγή διατηρεί την τάση V σταθερή."],
            related_theory_topic="Πυκνωτές & Διηλεκτρικά",
        ),
        ExamQuestion(
            question_number=7,
            title="Άσκηση 7: Ανάκλαση, Διάθλαση Snell & Κρίσιμη Γωνία",
            question_type="Calculations",
            prompt_text=r"Δέσμη φωτός ταξιδεύει από γυαλί ($n_1 = 1.52$) σε νερό ($n_2 = 1.33$) με γωνία πρόσπτωσης $\theta_1 = 35^\circ$. α) Θα διαθλαστεί; Υπολογίστε την κρίσιμη γωνία $\theta_c$. β) Υπολογίστε τη γωνία διάθλασης $\theta_2$.",
            given_parameters=[
                GivenParameter("n_1", "1.52", "Δείκτης διάθλασης γυαλιού"),
                GivenParameter("n_2", "1.33", "Δείκτης διάθλασης νερού"),
                GivenParameter(r"\theta_1", r"35^\circ", "Γωνία πρόσπτωσης"),
            ],
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Υπολογισμός κρίσιμης γωνίας ολικής ανάκλασης θ_c",
                    formula=r"\sin\theta_c = \frac{n_2}{n_1} \implies \theta_c = \arcsin\left(\frac{n_2}{n_1}\right)",
                    substitution=r"\sin\theta_c = \frac{1.33}{1.52} \approx 0.8750 \implies \theta_c = \arcsin(0.8750) \approx 61.04^\circ",
                    result=r"\theta_c \approx 61.04^\circ",
                    rationale="Η ολική ανάκλαση συμβαίνει μόνο όταν θ_1 >= θ_c.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Έλεγχος συνθήκης διάθλασης",
                    formula=r"\theta_1 < \theta_c \implies \text{Συμβαίνει κανονική διάθλαση}",
                    substitution=r"35^\circ < 61.04^\circ",
                    result=r"\text{Ναι, η ακτίνα διαθλάται στο νερό}",
                    rationale="Επειδή η γωνία πρόσπτωσης είναι μικρότερη της κρίσιμης, το φως εισέρχεται στο δεύτερο μέσο.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Υπολογισμός γωνίας διάθλασης θ_2 (Νόμος Snell)",
                    formula=r"n_1 \sin\theta_1 = n_2 \sin\theta_2 \implies \sin\theta_2 = \frac{n_1}{n_2}\sin\theta_1",
                    substitution=r"\sin\theta_2 = \frac{1.52}{1.33} \sin(35^\circ) = 1.14286 \times 0.57358 \approx 0.6555 \implies \theta_2 = \arcsin(0.6555)",
                    result=r"\theta_2 \approx 40.95^\circ",
                    rationale="Η ακτίνα απομακρύνεται από την κάθετο επειδή μεταβαίνει σε οπτικά αραιότερο μέσο (n2 < n1).",
                ),
            ],
            final_answer=r"\theta_c \approx 61.04^\circ \ (\text{Διαθλάται}), \quad \theta_2 \approx 40.95^\circ",
            detailed_justification="Νόμος του Snell στη διεπιφάνεια γυαλιού-νερού. Η γωνία διάθλασης είναι μεγαλύτερη της γωνίας πρόσπτωσης (40.95° > 35°).",
            common_pitfalls=["Βεβαιωθείτε ότι ο υπολογιστής σας είναι ρυθμισμένος σε Μοίρες (Degrees) και όχι σε Ακτίνια (Radians)."],
            related_theory_topic="Οπτική, Νόμος Snell & Ολική Ανάκλαση",
        ),
    ]

    justifications = [
        DesignJustification(
            title="Κριτήριο Ολικής Εσωτερικής Ανάκλασης",
            category="Snell Law",
            description="Η ολική ανάκλαση απαιτεί δύο αναγκαίες συνθήκες: 1) Μετάβαση από πυκνότερο σε αραιότερο μέσο (n1 > n2), και 2) Γωνία πρόσπτωσης μεγαλύτερη της κρίσιμης (θ1 > θc).",
            rationale="Αρχή λειτουργίας των οπτικών ινών και κυματοδηγών.",
        ),
        DesignJustification(
            title="Αρχή Επαλληλίας Ηλεκτροστατικών Δυνάμεων",
            category="Superposition",
            description="Η συνολική δύναμη σε ένα φορτίο είναι το διανυσματικό άθροισμα των επιμέρους δυνάμεων Coulomb που ασκούν όλα τα άλλα φορτία ανεξάρτητα.",
            rationale="Επιτρέπει την επίλυση πολύπλοκων συστημάτων φορτίων μέσω απλών διανυσματικών αθροισμάτων.",
        ),
    ]

    solution_code = '''"""Python verification script for Practice Exam 2."""

import math

def verify_practice_2() -> None:
    """Verifies all calculations for Practice Exam 2."""
    # 3. Wave
    c = 3e8
    mu_0 = 4 * math.pi * 1e-7
    B_0 = 8.25e-9
    omega = 2.70e15
    k = omega / c
    f = omega / (2 * math.pi)
    wavelength = c / f
    E_0 = c * B_0
    intensity = (E_0 * B_0) / (2 * mu_0)
    print("--- 3. EM Wave ---")
    print(f"k = {k:.2e} rad/m, f = {f:.3e} Hz, lambda = {wavelength*1e9:.1f} nm, E_0 = {E_0:.3f} V/m, I = {intensity*1000:.3f} mW/m^2")

    # 4. Coulomb forces
    k_e = 8.988e9
    q1 = 4.0e-6
    q2 = 2.0e-6
    q3 = 6.0e-6
    F12 = k_e * q1 * q2 / (3.0**2)
    F32 = k_e * q3 * q2 / (2.0**2)
    F_net = F32 - F12
    print("\\n--- 4. Coulomb Forces ---")
    print(f"F12 = {F12*1000:.2f} mN, F32 = {F32*1000:.2f} mN, F_net = {F_net*1000:.2f} mN (to right)")

    # 5. Magnetic field
    I = 20.0
    r = 0.05
    B = (mu_0 * I) / (2 * math.pi * r)
    print("\\n--- 5. Wire B-field ---")
    print(f"B = {B*1e6:.1f} uT")

    # 6. Capacitor
    eps_0 = 8.854e-12
    A = 150e-4
    d = 2e-3
    kappa = 3.5
    V = 24.0
    C = kappa * eps_0 * A / d
    Q = C * V
    E = V / d
    print("\\n--- 6. Capacitor ---")
    print(f"C = {C*1e12:.1f} pF, Q = {Q*1e9:.2f} nC, E = {E/1000:.1f} kV/m")

    # 7. Snell Law
    n1 = 1.52
    n2 = 1.33
    theta1_deg = 35.0
    theta1_rad = math.radians(theta1_deg)
    sin_crit = n2 / n1
    theta_c_deg = math.degrees(math.asin(sin_crit))
    sin_theta2 = (n1 / n2) * math.sin(theta1_rad)
    theta2_deg = math.degrees(math.asin(sin_theta2))
    print("\\n--- 7. Snell Law ---")
    print(f"Critical angle = {theta_c_deg:.2f} deg")
    print(f"Refracted angle = {theta2_deg:.2f} deg")

if __name__ == "__main__":
    verify_practice_2()
'''

    return Scenario(
        id="synth_exam_2_fields_waves",
        title="Θέμα Εξάσκησης 2 — Πεδία, Κύματα & Οπτική Snell",
        subtitle="Πλήρης Επίλυση: Θωράκιση, Ανάστροφο Κύμα, Coulomb, Αγωγοί & Snell",
        course_tag="Practice Exam 02",
        duration_info="Διάρκεια: 2.5 ώρες | 2 Ερωτήσεις Θεωρίας & 5 Ασκήσεις Υπολογισμού",
        paragraphs=paragraphs,
        questions=questions,
        justifications=justifications,
        solution_code=solution_code,
    )
