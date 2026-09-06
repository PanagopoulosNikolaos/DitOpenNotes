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
                    title="Μαθηματική μορφή αρμονικού κύματος και εξαγωγή παραμέτρων",
                    formula=r"\vec{B}(z,t) = B_0 \cos(k z + \omega t)\hat{u}_B",
                    substitution=r"B_0 = 8.25\times 10^{-9} \ \text{T}, \quad \omega = 2.70\times 10^{15} \ \text{rad/s}, \quad \hat{u}_B = +\hat{x} \ (\hat{i})",
                    result=r"\vec{B}(z,t) = 8.25\times 10^{-9}\cos(k z + 2.70\times 10^{15} t)\hat{i} \ \text{T}",
                    rationale="Το μαγνητικό πεδίο ταλαντώνεται κατά τον άξονα x.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Προσδιορισμός κατεύθυνσης διάδοσης από τη φάση του κύματος",
                    formula=r"\phi(z,t) = k z + \omega t = \text{σταθερό} \implies v_{\text{phase}} = \frac{dz}{dt} = -\frac{\omega}{k} = -c",
                    substitution=r"\text{Το ομόσημο θετικό πρόσημο (+kz + ωt) σημαίνει ότι το μέτωπο κύματος μετατοπίζεται προς τα αρνητικά } z",
                    result=r"\hat{u}_k = -\hat{z} \quad (\text{Διάδοση προς τον αρνητικό άξονα } z)",
                    rationale="Η παρουσία του προσήμου συν (+ωt) επιβάλλει διάδοση αντίθετη της φοράς του άξονα z.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Υπολογισμός κυματάριθμου k",
                    formula=r"k = \frac{\omega}{c}",
                    substitution=r"k = \frac{2.70\times 10^{15} \ \text{rad/s}}{3\times 10^8 \ \text{m/s}} = 9.00\times 10^6 \ \text{rad/m}",
                    result=r"k = 9.00\times 10^6 \ \text{rad/m}",
                    rationale="Σχέση διασποράς στο κενό για ηλεκτρομαγνητικό κύμα.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Υπολογισμός γραμμικής συχνότητας f και περιόδου T",
                    formula=r"f = \frac{\omega}{2\pi}, \quad T = \frac{1}{f}",
                    substitution=r"f = \frac{2.70\times 10^{15}}{2\pi} \approx 4.2972\times 10^{14} \ \text{Hz}, \quad T = \frac{1}{4.2972\times 10^{14}} \approx 2.327\times 10^{-15} \ \text{s}",
                    result=r"f \approx 4.297\times 10^{14} \ \text{Hz} \approx 430 \ \text{THz}, \quad T \approx 2.327 \ \text{fs}",
                    rationale="Συχνότητα ταλάντωσης στην οπτική περιοχή (1 femtosecond = 10^-15 s).",
                ),
                CalculationStep(
                    step_number=5,
                    title="Υπολογισμός μήκους κύματος λ και φασματική ταξινόμηση",
                    formula=r"\lambda = \frac{c}{f} = \frac{2\pi}{k}",
                    substitution=r"\lambda = \frac{3\times 10^8 \ \text{m/s}}{4.2972\times 10^{14} \ \text{Hz}} = \frac{2\pi}{9.00\times 10^6 \ \text{rad/m}} \approx 6.9813\times 10^{-7} \ \text{m}",
                    result=r"\lambda \approx 698.1 \ \text{nm} \quad (\text{Ορατό Ερυθρό Φως})",
                    rationale="Μήκος κύματος στο ερυθρό άκρο του ορατού φάσματος (620-750 nm).",
                ),
                CalculationStep(
                    step_number=6,
                    title="Υπολογισμός πλάτους ηλεκτρικού πεδίου E_0",
                    formula=r"E_0 = c B_0",
                    substitution=r"E_0 = (3\times 10^8 \ \text{m/s}) \times (8.25\times 10^{-9} \ \text{T}) = 2.475 \ \text{V/m}",
                    result=r"E_0 = 2.475 \ \text{V/m}",
                    rationale="Θεμελιώδης σχέση πλάτους πεδίων στο κενό.",
                ),
                CalculationStep(
                    step_number=7,
                    title="Διανυσματικός προσδιορισμός πόλωσης και εξίσωση ηλεκτρικού πεδίου E(z,t)",
                    formula=r"\hat{u}_E \times \hat{u}_B = \hat{u}_k \implies \hat{u}_E \times (+\hat{x}) = -\hat{z} \implies \hat{u}_E = +\hat{y} \ (\hat{j})",
                    substitution=r"\text{Επειδή } \hat{y} \times \hat{x} = -\hat{z}, \text{ η κατεύθυνση πόλωσης είναι αυστηρά } +\hat{y}",
                    result=r"\vec{E}(z,t) = 2.475 \cos(9.00\times 10^6 z + 2.70\times 10^{15} t)\hat{j} \ \text{V/m}",
                    rationale="Η φορά του ηλεκτρικού πεδίου εξασφαλίζει ότι το διάνυσμα Poynting E x B δείχνει προς τα -z.",
                ),
                CalculationStep(
                    step_number=8,
                    title="Υπολογισμός μέσης έντασης ακτινοβολίας I",
                    formula=r"I = \langle |\vec{S}| \rangle = \frac{E_0 B_0}{2\mu_0} = \frac{1}{2} c \epsilon_0 E_0^2",
                    substitution=r"I = \frac{(2.475 \ \text{V/m}) \times (8.25\times 10^{-9} \ \text{T})}{2 \times (4\pi\times 10^{-7} \ \text{T}\cdot\text{m/A})} = \frac{2.041875\times 10^{-8}}{2.513274\times 10^{-6}} \approx 8.1245\times 10^{-3} \ \text{W/m}^2",
                    result=r"I \approx 8.125 \times 10^{-3} \ \text{W/m}^2 = 8.125 \ \text{mW/m}^2",
                    rationale="Μέση χρονική πυκνότητα ροής ενέργειας του ορατού κύματος.",
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
                    title="Προσδιορισμός γεωμετρίας θέσεων και σχετικών αποστάσεων",
                    formula=r"r_{12} = |x_2 - x_1|, \quad r_{32} = |x_3 - x_2|",
                    substitution=r"x_1 = 0 \ \text{m}, \quad x_2 = 3.0 \ \text{m}, \quad x_3 = 5.0 \ \text{m} \implies r_{12} = 3.0 - 0 = 3.0 \ \text{m}, \quad r_{32} = 5.0 - 3.0 = 2.0 \ \text{m}",
                    result=r"r_{12} = 3.0 \ \text{m}, \quad r_{32} = 2.0 \ \text{m}",
                    rationale="Αποστάσεις στον μονοδιάστατο άξονα x μεταξύ των φορτίων.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Διανυσματική δύναμη Coulomb F_12 από το q_1 στο q_2",
                    formula=r"\vec{F}_{12} = -k_e \frac{|q_1 q_2|}{r_{12}^2} \hat{x}",
                    substitution=r"q_1 > 0, \ q_2 < 0 \implies \text{Ελκτική δύναμη προς το } x=0 \ (\text{δηλαδή φορά } -\hat{x})",
                    result=r"\vec{F}_{12} = -k_e \frac{|q_1 q_2|}{r_{12}^2} \hat{x}",
                    rationale="Τα ετερόσημα φορτία q1 και q2 έλκονται, επομένως η δύναμη στο q2 έχει φορά προς τα αριστερά (-x).",
                ),
                CalculationStep(
                    step_number=3,
                    title="Αριθμητικός υπολογισμός μέτρου και συνιστώσας της F_12",
                    formula=r"F_{12} = k_e \frac{|q_1 q_2|}{r_{12}^2}",
                    substitution=r"F_{12} = (8.988\times 10^9 \ \text{N}\cdot\text{m}^2/\text{C}^2) \frac{(4.0\times 10^{-6} \ \text{C})(2.0\times 10^{-6} \ \text{C})}{(3.0 \ \text{m})^2} = \frac{7.1904\times 10^{-2}}{9.0}",
                    result=r"\vec{F}_{12} \approx -7.989 \times 10^{-3} \ \text{N} \ \hat{x} = -7.99 \ \text{mN} \ \hat{x}",
                    rationale="Ηλεκτροστατική έλξη από το πρώτο φορτίο.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Διανυσματική δύναμη Coulomb F_32 από το q_3 στο q_2",
                    formula=r"\vec{F}_{32} = +k_e \frac{|q_3 q_2|}{r_{32}^2} \hat{x}",
                    substitution=r"F_{32} = (8.988\times 10^9) \frac{(6.0\times 10^{-6} \ \text{C})(2.0\times 10^{-6} \ \text{C})}{(2.0 \ \text{m})^2} = \frac{0.107856}{4.0}",
                    result=r"\vec{F}_{32} \approx +2.6964 \times 10^{-2} \ \text{N} \ \hat{x} = +26.96 \ \text{mN} \ \hat{x}",
                    rationale="Επειδή το q3 είναι θετικό και βρίσκεται στα δεξιά (x=5 m), έλκει το αρνητικό q2 προς τα δεξιά (+x).",
                ),
                CalculationStep(
                    step_number=5,
                    title="Εφαρμογή αρχής επαλληλίας για τη συνισταμένη δύναμη F_net",
                    formula=r"\vec{F}_{\text{net}} = \vec{F}_{12} + \vec{F}_{32} = (F_{32} - F_{12})\hat{x}",
                    substitution=r"F_{\text{net}} = +26.964 \ \text{mN} - 7.989 \ \text{mN} = +18.975 \ \text{mN}",
                    result=r"\vec{F}_{\text{net}} \approx +18.98 \ \text{mN} \ \hat{x}",
                    rationale="Αλγεβρικό άθροισμα των αντίρροπων διανυσματικών δυνάμεων.",
                ),
                CalculationStep(
                    step_number=6,
                    title="Τελικό μέτρο, πρόσημο και φυσική κατεύθυνση συνισταμένης δύναμης",
                    formula=r"|\vec{F}_{\text{net}}| = 1.898\times 10^{-2} \ \text{N}, \quad \hat{u}_F = +\hat{x}",
                    substitution=r"\text{Επειδή } r_{32} < r_{12} \ (2\text{ m} < 3\text{ m}) \ \kappa\alpha\iota \ |q_3| > |q_1| \ (6 \ \mu\text{C} > 4 \ \mu\text{C}), \text{ η έλξη από το } q_3 \text{ κυριαρχεί}",
                    result=r"\vec{F}_{\text{net}} \approx 18.98 \ \text{mN} \ \hat{x} \quad (\text{προς τα δεξιά})",
                    rationale="Το φορτίο q2 επιταχύνεται προς τη θετική κατεύθυνση του άξονα x.",
                ),
            ],
            final_answer=r"\vec{F}_{\text{net}} \approx 18.98\text{ mN} \ \hat{x} \quad (\text{μέτρο } 1.90\times 10^{-2}\text{ N προς τα δεξιά})",
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
                    title="Μετατροπή μονάδων απόστασης και γεωμετρική συμμετρία",
                    formula=r"r = 5.0 \ \text{cm} \times 10^{-2} \ \text{m/cm} = 0.05 \ \text{m}",
                    substitution=r"r = 0.05 \ \text{m}",
                    result=r"r = 0.05 \ \text{m}",
                    rationale="Ο απειρομήκης αγωγός διαθέτει αξονική κυλινδρική συμμετρία γύρω από τον άξονά του.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Διατύπωση του νόμου του Ampère για κυκλικό βρόχο",
                    formula=r"\oint_{\mathcal{C}} \vec{B} \cdot d\vec{\ell} = \mu_0 I_{\text{enc}}",
                    substitution=r"\text{Λόγω συμμετρίας, το } B \text{ είναι εφαπτομενικό στον βρόχο και σταθερό σε μέτρο: } \oint B \, d\ell = B (2\pi r)",
                    result=r"B(2\pi r) = \mu_0 I",
                    rationale="Ο νόμος του Ampère συνδέει την κυκλοφορία του μαγνητικού πεδίου με το περικλειόμενο ρεύμα.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Αλγεβρική επίλυση ως προς το μέτρο της μαγνητικής επαγωγής B",
                    formula=r"B = \frac{\mu_0 I}{2\pi r}",
                    substitution=r"\text{Αναδιάταξη της εξίσωσης Ampère για απόσταση } r \text{ από τον αγωγό}",
                    result=r"B = \frac{\mu_0 I}{2\pi r}",
                    rationale="Κλασικός τύπος Biot-Savart / Ampère για ευθύγραμμο σύρμα.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Αριθμητική αντικατάσταση και υπολογισμός τιμής",
                    formula=r"B = \frac{\mu_0 I}{2\pi r}",
                    substitution=r"B = \frac{(4\pi\times 10^{-7} \ \text{T}\cdot\text{m/A}) \times (20 \ \text{A})}{2\pi \times (0.05 \ \text{m})} = \frac{2\times 10^{-7} \times 20}{0.05} = \frac{4.0\times 10^{-6}}{0.05}",
                    result=r"B = 8.00 \times 10^{-5} \ \text{T}",
                    rationale="Ακριβής υπολογισμός χωρίς προσεγγίσεις χάρη στην απλοποίηση του π.",
                ),
                CalculationStep(
                    step_number=5,
                    title="Τελική έκφραση σε μικροτέσλα (μT) και κανόνας δεξιού χεριού",
                    formula=r"B = 8.00\times 10^{-5} \ \text{T} = 80.0 \ \mu\text{T}",
                    substitution=r"\text{Φορά: Ομόκεντροι κύκλοι γύρω από το σύρμα σύμφωνα με τον κανόνα δεξιού χεριού } (\hat{u}_\phi)",
                    result=r"B = 80.0 \ \mu\text{T} \quad (0.80 \ \text{Gauss})",
                    rationale="Το πεδίο εξασθενεί αντιστρόφως ανάλογα με την απόσταση 1/r.",
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
                    title="Μετατροπή μονάδων επιφάνειας και απόστασης στο SI",
                    formula=r"A = 150 \ \text{cm}^2 \times 10^{-4} \ \text{m}^2/\text{cm}^2, \quad d = 2.0 \ \text{mm} \times 10^{-3} \ \text{m/mm}",
                    substitution=r"A = 150 \times 10^{-4} = 0.015 \ \text{m}^2, \quad d = 2.0\times 10^{-3} = 0.002 \ \text{m}",
                    result=r"A = 0.015 \ \text{m}^2, \quad d = 0.002 \ \text{m}",
                    rationale="Βασικές γεωμετρικές παράμετροι σε μονάδες SI.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Υπολογισμός χωρητικότητας στο κενό C_0",
                    formula=r"C_0 = \epsilon_0 \frac{A}{d}",
                    substitution=r"C_0 = (8.854\times 10^{-12} \ \text{F/m}) \times \frac{0.015 \ \text{m}^2}{0.002 \ \text{m}} = (8.854\times 10^{-12}) \times 7.5",
                    result=r"C_0 \approx 6.6405 \times 10^{-11} \ \text{F} \approx 66.41 \ \text{pF}",
                    rationale="Χωρητικότητα χωρίς την παρουσία διηλεκτρικού μέσου.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Υπολογισμός χωρητικότητας C με διηλεκτρικό υλικό (κ = 3.5)",
                    formula=r"C = \kappa C_0 = \kappa \epsilon_0 \frac{A}{d}",
                    substitution=r"C = 3.5 \times (6.6405\times 10^{-11} \ \text{F}) \approx 2.3242\times 10^{-10} \ \text{F}",
                    result=r"C \approx 2.324 \times 10^{-10} \ \text{F} \approx 232.4 \ \text{pF}",
                    rationale="Η σχετική διηλεκτρική διαπερατότητα πολλαπλασιάζει τη χωρητικότητα κατά κ = 3.5.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Υπολογισμός αποθηκευμένου ελεύθερου φορτίου Q",
                    formula=r"Q = C V",
                    substitution=r"Q = (2.3242\times 10^{-10} \ \text{F}) \times (24 \ \text{V}) \approx 5.578\times 10^{-9} \ \text{C}",
                    result=r"Q \approx 5.578 \times 10^{-9} \ \text{C} = 5.58 \ \text{nC}",
                    rationale="Φορτίο συσσωρευμένο στους οπλισμούς υπό σταθερή τάση 24 V.",
                ),
                CalculationStep(
                    step_number=5,
                    title="Υπολογισμός έντασης ηλεκτρικού πεδίου E μεταξύ των οπλισμών",
                    formula=r"E = \frac{V}{d}",
                    substitution=r"E = \frac{24 \ \text{V}}{0.002 \ \text{m}} = 12000 \ \text{V/m}",
                    result=r"E = 1.20 \times 10^4 \ \text{V/m} = 12.0 \ \text{kV/m}",
                    rationale="Επειδή ο πυκνωτής παραμένει συνδεδεμένος στην μπαταρία, το πεδίο παραμένει E = V/d ανεξάρτητα από το κ.",
                ),
                CalculationStep(
                    step_number=6,
                    title="Υπολογισμός αποθηκευμένης ηλεκτροστατικής ενέργειας U_E",
                    formula=r"U_E = \frac{1}{2} C V^2 = \frac{1}{2} Q V",
                    substitution=r"U_E = \frac{1}{2} (2.3242\times 10^{-10} \ \text{F}) \times (24 \ \text{V})^2 = \frac{1}{2} (2.3242\times 10^{-10}) \times 576",
                    result=r"U_E \approx 6.694 \times 10^{-8} \ \text{J} = 66.94 \ \text{nJ}",
                    rationale="Ενέργεια του ηλεκτροστατικού πεδίου εντός του πολωμένου διηλεκτρικού όγκου.",
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
                    title="Οπτική ανάλυση μέσων και συνθήκη ολικής ανάκλασης",
                    formula=r"n_1 = 1.52 > n_2 = 1.33 \implies \text{Μετάβαση από πυκνότερο σε αραιότερο μέσο}",
                    substitution=r"\text{Η ταχύτητα του φωτός αυξάνεται στο 2ο μέσο, επομένως η ακτίνα απομακρύνεται από την κάθετο}",
                    result=r"\text{Δυνατότητα εμφάνισης ολικής εσωτερικής ανάκλασης για } \theta_1 \ge \theta_c",
                    rationale="Η ολική ανάκλαση μπορεί να συμβεί μόνο όταν n_1 > n_2.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Εξαγωγή τύπου κρίσιμης γωνίας θ_c",
                    formula=r"n_1 \sin\theta_c = n_2 \sin(90^\circ) = n_2 \implies \sin\theta_c = \frac{n_2}{n_1} \implies \theta_c = \arcsin\left(\frac{n_2}{n_1}\right)",
                    substitution=r"\sin\theta_c = \frac{1.33}{1.52} \approx 0.87500",
                    result=r"\sin\theta_c \approx 0.87500",
                    rationale="Στην κρίσιμη γωνία η διαθλώμενη ακτίνα κινείται παράλληλα προς τη διαχωριστική επιφάνεια (θ_2 = 90°).",
                ),
                CalculationStep(
                    step_number=3,
                    title="Αριθμητικός υπολογισμός κρίσιμης γωνίας θ_c",
                    formula=r"\theta_c = \arcsin(0.87500)",
                    substitution=r"\theta_c = \arcsin(0.87500) \approx 1.0653 \ \text{rad} = 61.045^\circ",
                    result=r"\theta_c \approx 61.04^\circ",
                    rationale="Αυτή είναι η ελάχιστη γωνία για την οποία παρατηρείται ολική εσωτερική ανάκλαση.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Σύγκριση γωνίας πρόσπτωσης με την κρίσιμη γωνία",
                    formula=r"\theta_1 < \theta_c \implies \text{Κανονική διάθλαση}",
                    substitution=r"35^\circ < 61.04^\circ \implies \text{Δεν υπάρχει ολική ανάκλαση}",
                    result=r"\text{Ναι, η φωτεινή δέσμη διαθλάται στο νερό}",
                    rationale="Επειδή θ_1 < θ_c, μέρος της φωτεινής ισχύος εισέρχεται στο νερό υπό γωνία θ_2.",
                ),
                CalculationStep(
                    step_number=5,
                    title="Εφαρμογή νόμου Snell για τον υπολογισμό του ημιτόνου γωνίας διάθλασης",
                    formula=r"n_1 \sin\theta_1 = n_2 \sin\theta_2 \implies \sin\theta_2 = \frac{n_1}{n_2}\sin\theta_1",
                    substitution=r"\sin\theta_2 = \frac{1.52}{1.33} \sin(35^\circ) \approx 1.14286 \times 0.573576 \approx 0.655516",
                    result=r"\sin\theta_2 \approx 0.65552",
                    rationale="Ο λόγος των δεικτών διάθλασης καθορίζει τη γωνιακή εκτροπή της δέσμης.",
                ),
                CalculationStep(
                    step_number=6,
                    title="Υπολογισμός γωνίας διάθλασης θ_2 και έλεγχος φυσικής συνέπειας",
                    formula=r"\theta_2 = \arcsin(\sin\theta_2)",
                    substitution=r"\theta_2 = \arcsin(0.655516) \approx 0.7147 \ \text{rad} \approx 40.954^\circ",
                    result=r"\theta_2 \approx 40.95^\circ \quad (\theta_2 > \theta_1)",
                    rationale="Όπως αναμενόταν φυσικά, η γωνία στο οπτικά αραιότερο μέσο είναι μεγαλύτερη (40.95° > 35°).",
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
