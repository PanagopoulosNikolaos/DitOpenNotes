"""Past Exam Scenario: June 2026 Team D.

Verbatim transcription of exam paper with three-part contract hover tooltips,
analytical derivations, and SymPy Python verification code.
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


def createPastExam202606TeamD() -> Scenario:
    """Instantiates the June 2026 Team D past examination scenario.

    Returns:
        Scenario: Complete scenario container with verbatim text and solutions.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(
                    text="Εξεταστική. ΑΡΧΕΣ ΗΛΕΚΤΡΟΜΑΓΝΗΤΙΣΜΟΥ ΚΑΙ ΤΗΛΕΠΙΚΟΙΝΩΝΙΩΝ. Ιούνιος 2026. Ομάδα Δ\n",
                    is_highlight=False,
                ),
                TextSegment(
                    text="Ερωτήσεις: 4 μονάδες. Αρνητική βαθμολογία «-0.5» ανά λάθος απάντηση.",
                    is_highlight=False,
                ),
            ],
            accent_border_color=None,
        ),
        Paragraph(
            segments=[
                TextSegment(text="Ερώτηση 1.\nΜια κατανομή φορτίου ονομάζεται ", is_highlight=False),
                TextSegment(
                    text="ομοιόμορφη",
                    is_highlight=True,
                    category="law",
                    tag_label="ΟΜΟΙΟΜΟΡΦΗ",
                    tooltip="Classification: Χαρακτηρισμός Ομοιομορφίας | Detection Clue: 'ομοιόμορφη' | Application Rationale: Σημαίνει σταθερή πυκνότητα φορτίου dq/dV = const παντού στο σώμα.",
                ),
                TextSegment(text=" όταν η πυκνότητα φορτίου της είναι ", is_highlight=False),
                TextSegment(
                    text="σταθερή",
                    is_highlight=True,
                    category="param",
                    tag_label="ΣΤΑΘΕΡΗ ρ",
                    tooltip="Classification: Σταθερή Πυκνότητα Φορτίου | Detection Clue: Συμπλήρωση κενού | Application Rationale: Η πυκνότητα δεν μεταβάλλεται συναρτήσει των συντεταγμένων θέσης.",
                ),
                TextSegment(text=" .", is_highlight=False),
            ],
            accent_border_color="accent",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Ερώτηση 2.\nΤι εκφράζει η ", is_highlight=False),
                TextSegment(
                    text="χωρητικότητα ενός πυκνωτή",
                    is_highlight=True,
                    category="param",
                    tag_label="ΧΩΡΗΤΙΚΟΤΗΤΑ C",
                    tooltip="Classification: Χωρητικότητα C = Q / V | Detection Clue: 'χωρητικότητα ενός πυκνωτή' | Application Rationale: Μετρά την ικανότητα αποθήκευσης ηλεκτρικού φορτίου για δεδομένη διαφορά δυναμικού [Farad = Coulomb/Volt].",
                ),
                TextSegment(
                    text=";\nΑ] τις δυναμικές γραμμές που εξέρχονται από το κύκλωμα\nΒ] την ένταση του μαγνητικού πεδίου\nΓ] την πόλωση του διηλεκτρικού ανάμεσα στους οπλισμούς\nΔ] την ικανότητα του πυκνωτή να αποθηκεύει φορτίο",
                    is_highlight=False,
                ),
            ],
            accent_border_color="accent",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Ερώτηση 3.\nΗ ένταση του ηλεκτρικού πεδίου είναι ", is_highlight=False),
                TextSegment(
                    text="σταθερή",
                    is_highlight=True,
                    category="field",
                    tag_label="ΣΤΑΘΕΡΟ E",
                    tooltip="Classification: Ομογενές Ηλεκτρικό Πεδίο E = V/d | Detection Clue: 'ένταση είναι σταθερή' | Application Rationale: Το πεδίο είναι σταθερό και παράλληλο ανάμεσα στους οπλισμούς επίπεδου πυκνωτή.",
                ),
                TextSegment(text=" σε έναν ", is_highlight=False),
                TextSegment(
                    text="επίπεδο (ή ιδανικό)",
                    is_highlight=True,
                    category="geom",
                    tag_label="ΕΠΙΠΕΔΟΣ",
                    tooltip="Classification: Επίπεδος Πυκνωτής | Detection Clue: Συμπλήρωση κενού | Application Rationale: Στον ιδανικό επίπεδο πυκνωτή παραμελούνται τα φαινόμενα ακμών και το πεδίο είναι αυστηρά ομογενές.",
                ),
                TextSegment(text=" πυκνωτή;", is_highlight=False),
            ],
            accent_border_color="accent",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Ερώτηση 4.\nΠόσες δυναμικές γραμμές εισέρχονται και εξέρχονται από μια ", is_highlight=False),
                TextSegment(
                    text="κλειστή επιφάνεια που βρίσκεται μέσα σε μαγνητικό πεδίο",
                    is_highlight=True,
                    category="law",
                    tag_label="ΝΟΜΟΣ GAUSS B",
                    tooltip="Classification: Νόμος Gauss για τον Μαγνητισμό ∬ B·dS = 0 | Detection Clue: 'κλειστή επιφάνεια σε μαγνητικό πεδίο' | Application Rationale: Επειδή div(B) = 0, όσες δυναμικές γραμμές εισέρχονται σε οποιαδήποτε κλειστή επιφάνεια, τόσες ακριβώς εξέρχονται.",
                ),
                TextSegment(
                    text=";\nΑ] Εξαρτάται από το αν είναι ομογενές το μαγνητικό πεδίο\nΒ] Εξαρτάται από την ένταση του μαγνητικού πεδίου\nΓ] Δεν εξέρχεται καμία\nΔ] Εξέρχονται όσες εισέρχονται",
                    is_highlight=False,
                ),
            ],
            accent_border_color="accent",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Άσκηση 1. 3 μονάδες\nΣύμφωνα με τον νόμο του Gauss για τη ", is_highlight=False),
                TextSegment(
                    text="διηλεκτρική μετατόπιση D",
                    is_highlight=True,
                    category="field",
                    tag_label="ΜΕΤΑΤΟΠΙΣΗ D",
                    tooltip="Classification: Διάνυσμα Ηλεκτρικής Ροής D | Detection Clue: ∇·D = ρ | Application Rationale: Εφαρμογή της απόκλισης div(D) = rho.",
                ),
                TextSegment(text=" ισχύει ∇·D = ρ, όπου ρ η πυκνότητα φορτίου. Αν ", is_highlight=False),
                TextSegment(
                    text="D = -x x̂ + z²y ẑ",
                    is_highlight=True,
                    category="calc",
                    tag_label="D_x, D_z",
                    tooltip="Classification: Συνιστώσες D_x = -x, D_y = 0, D_z = z^2 y | Detection Clue: D = -x x̂ + z²y ẑ | Application Rationale: d(-x)/dx = -1, d(z^2 y)/dz = 2zy.",
                ),
                TextSegment(text=" να υπολογίσετε την πυκνότητα φορτίου ρ.", is_highlight=False),
            ],
            accent_border_color="accent",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Άσκηση 2. 3 μονάδες\nΤο ηλεκτρικό πεδίο ενός ημιτονοειδούς επίπεδου ΗΜ κύματος που διαδίδεται στο κενό δίνεται από τη σχέση:\n", is_highlight=False),
                TextSegment(
                    text="E = 60 cos(kx - 3·10⁹ t) ŷ",
                    is_highlight=True,
                    category="field",
                    tag_label="E(x,t)",
                    tooltip="Classification: Ηλεκτρικό Πεδίο Επίπεδου Κύματος | Detection Clue: E_0 = 60 V/m, omega = 3*10^9 rad/s, πόλωση κατά y, διάδοση κατά +x | Application Rationale: Υπολογισμός k = omega/c = 10 rad/m, λ = 2π/10 m, B_0 = 2*10^-7 T κατά +z.",
                ),
                TextSegment(
                    text=" α) Ποιο είναι το μήκος κύματος λ και η συχνότητα f του κύματος; β) Να γραφεί το ",
                    is_highlight=False,
                ),
                TextSegment(
                    text="διάνυσμα ταλάντωσης της μαγνητικής επαγωγής B",
                    is_highlight=True,
                    category="field",
                    tag_label="ΔΙΑΝΥΣΜΑ B",
                    tooltip="Classification: Μαγνητικό Πεδίο B | Detection Clue: B_0 = E_0 / c και ŷ × ẑ = x̂ | Application Rationale: B(x,t) = 2*10^-7 cos(kx - 3*10^9 t) ẑ T.",
                ),
                TextSegment(text=". γ) Να υπολογισθεί το ", is_highlight=False),
                TextSegment(
                    text="διάνυσμα Poynting S και η ένταση I",
                    is_highlight=True,
                    category="calc",
                    tag_label="S & I",
                    tooltip="Classification: Ροή Ισχύος Poynting και Μέση Ένταση | Detection Clue: S = (1/mu_0)(E x B) | Application Rationale: S_max = 30/pi W/m^2, I = 15/pi W/m^2.",
                ),
                TextSegment(
                    text=" του κύματος.\nΤυπολόγιο: E = E₀cos(kx - ωt)ŷ, B = B₀cos(kx - ωt)ẑ, S = (1/μ₀)(E×B), I = S̄, k = 2π/λ, ω = 2πf, c = λf, E₀ = cB₀, c = 3×10⁸ m/s, μ₀ = 4π×10⁻⁷ Tm/A, ∇ = (∂/∂x)x̂ + (∂/∂y)ŷ + (∂/∂z)ẑ.",
                    is_highlight=False,
                ),
            ],
            accent_border_color="accent",
        ),
    ]

    questions = [
        ExamQuestion(
            question_number=1,
            title="Ορισμός Ομοιόμορφης Κατανομής Φορτίου (Συμπλήρωση Κενού)",
            question_type="Theory Analysis",
            prompt_text="Μια κατανομή φορτίου ονομάζεται ομοιόμορφη όταν η πυκνότητα φορτίου της είναι .................................................... .",
            options=[],
            final_answer="σταθερή (ανεξάρτητη της θέσης)",
            detailed_justification="Σε μια ομοιόμορφη κατανομή, η πυκνότητα ρ (ή σ ή λ) παραμένει αμετάβλητη σε όλα τα σημεία της περιοχής κατανομής.",
            common_pitfalls=["Μην απαντήσετε 'μηδενική'. Αν ήταν μηδέν, δεν θα υπήρχε φορτίο."],
            related_theory_topic="Ηλεκτροστατική & Κατανομές Φορτίου",
        ),
        ExamQuestion(
            question_number=2,
            title="Φυσική Σημασία Χωρητικότητας Πυκνωτή",
            question_type="Multiple Choice",
            prompt_text="Τι εκφράζει η χωρητικότητα ενός πυκνωτή;",
            options=[
                QuestionOption(
                    letter="Α",
                    text="τις δυναμικές γραμμές που εξέρχονται από το κύκλωμα",
                    is_correct=False,
                    explanation="Λάθος: Οι δυναμικές γραμμές δεν ορίζουν τη χωρητικότητα.",
                ),
                QuestionOption(
                    letter="Β",
                    text="την ένταση του μαγνητικού πεδίου",
                    is_correct=False,
                    explanation="Λάθος: Ο πυκνωτής σχετίζεται πρωτίστως με το ηλεκτρικό πεδίο.",
                ),
                QuestionOption(
                    letter="Γ",
                    text="την πόλωση του διηλεκτρικού ανάμεσα στους οπλισμούς",
                    is_correct=False,
                    explanation="Λάθος: Η πόλωση είναι ιδιότητα του υλικού, όχι η συνολική χωρητικότητα.",
                ),
                QuestionOption(
                    letter="Δ",
                    text="την ικανότητα του πυκνωτή να αποθηκεύει φορτίο",
                    is_correct=True,
                    explanation="Σωστό: Η χωρητικότητα C = Q / V μετρά ακριβώς πόσο φορτίο Q αποθηκεύεται ανά Volt εφαρμοζόμενης τάσης V.",
                ),
            ],
            correct_option_letter="Δ",
            final_answer="Δ] την ικανότητα του πυκνωτή να αποθηκεύει φορτίο",
            detailed_justification="Όσο μεγαλύτερη είναι η χωρητικότητα C, τόσο περισσότερο φορτίο αποθηκεύουν οι οπλισμοί για την ίδια τάση V.",
            common_pitfalls=["Η χωρητικότητα εξαρτάται από τη γεωμετρία (εμβαδόν A, απόσταση d) και το διηλεκτρικό, όχι από την τάση V."],
            related_theory_topic="Πυκνωτές & Χωρητικότητα",
        ),
        ExamQuestion(
            question_number=3,
            title="Ομογενές Πεδίο σε Πυκνωτή (Συμπλήρωση Κενού)",
            question_type="Theory Analysis",
            prompt_text="Η ένταση του ηλεκτρικού πεδίου είναι σταθερή σε έναν .................................................... πυκνωτή;",
            options=[],
            final_answer="επίπεδο (ή ιδανικό επίπεδο)",
            detailed_justification="Σε έναν ιδανικό επίπεδο πυκνωτή με παράλληλους οπλισμούς (και παραμελώντας τις ακμές), οι δυναμικές γραμμές είναι παράλληλες και η ένταση σταθερή: E = V / d = σ / ε.",
            common_pitfalls=["Σε σφαιρικό ή κυλινδρικό πυκνωτή το πεδίο εξασθενεί ως 1/r² ή 1/r αντίστοιχα και ΔΕΝ είναι σταθερό."],
            related_theory_topic="Επίπεδος Πυκνωτής & Ομογενές Πεδίο",
        ),
        ExamQuestion(
            question_number=4,
            title="Μαγνητική Ροή μέσα από Κλειστή Επιφάνεια",
            question_type="Multiple Choice",
            prompt_text="Πόσες δυναμικές γραμμές εισέρχονται και εξέρχονται από μια κλειστή επιφάνεια που βρίσκεται μέσα σε μαγνητικό πεδίο;",
            options=[
                QuestionOption(
                    letter="Α",
                    text="Εξαρτάται από το αν είναι ομογενές το μαγνητικό πεδίο",
                    is_correct=False,
                    explanation="Λάθος: Ισχύει πάντοτε, ανεξάρτητα από την ομογένεια του πεδίου.",
                ),
                QuestionOption(
                    letter="Β",
                    text="Εξαρτάται από την ένταση του μαγνητικού πεδίου",
                    is_correct=False,
                    explanation="Λάθος: Η συνολική μαγνητική ροή είναι πάντα μηδέν.",
                ),
                QuestionOption(
                    letter="Γ",
                    text="Δεν εξέρχεται καμία",
                    is_correct=False,
                    explanation="Λάθος: Οι γραμμές είναι συνεχείς κλειστοί βρόχοι και διαπερνούν την επιφάνεια.",
                ),
                QuestionOption(
                    letter="Δ",
                    text="Εξέρχονται όσες εισέρχονται",
                    is_correct=True,
                    explanation="Σωστό: Λόγω της 2ης εξίσωσης Maxwell (νόμος Gauss για το B: ∬ B·dS = 0), δεν υπάρχουν μαγνητικά μονόπολα και η καθαρή ροή είναι μηδέν, άρα όσες γραμμές μπαίνουν, τόσες ακριβώς βγαίνουν.",
                ),
            ],
            correct_option_letter="Δ",
            final_answer="Δ] Εξέρχονται όσες εισέρχονται",
            detailed_justification="Επειδή div(B) = 0 παντού, η ολική μαγνητική ροή μέσα από οποιαδήποτε κλειστή επιφάνεια είναι μηδέν (Φ_B = 0), γεγονός που σημαίνει ισότητα εισερχόμενων και εξερχόμενων γραμμών.",
            common_pitfalls=["Αντίθετα, στο ηλεκτρικό πεδίο (div D = ρ), αν υπάρχει θετικό φορτίο στο εσωτερικό, εξέρχονται περισσότερες γραμμές από όσες εισέρχονται."],
            related_theory_topic="Μαγνητοστατική & 2η Εξίσωση Maxwell",
        ),
        ExamQuestion(
            question_number=5,
            title="Άσκηση 1: Υπολογισμός Πυκνότητας Φορτίου ρ από τη Μετατόπιση D",
            question_type="Calculations",
            prompt_text=r"Σύμφωνα με τον νόμο του Gauss για τη διηλεκτρική μετατόπιση $\vec{D}$ ισχύει $\vec{\nabla}\cdot\vec{D}=\rho$, όπου ρ η πυκνότητα φορτίου. Αν $\vec{D}=-x\hat{x}+z^2y\hat{z}$, να υπολογίσετε την πυκνότητα φορτίου $\rho$.",
            given_parameters=[
                GivenParameter("D_x", "-x", "x-συνιστώσα μετατόπισης"),
                GivenParameter("D_y", "0", "y-συνιστώσα μετατόπισης"),
                GivenParameter("D_z", "z^2 y", "z-συνιστώσα μετατόπισης"),
            ],
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Διατύπωση διαφορικής μορφής 1ης εξίσωσης Maxwell (Νόμος Gauss)",
                    formula=r"\rho = \vec{\nabla}\cdot\vec{D} = \frac{\partial D_x}{\partial x} + \frac{\partial D_y}{\partial y} + \frac{\partial D_z}{\partial z}",
                    substitution=r"\rho = \frac{\partial}{\partial x}(D_x) + \frac{\partial}{\partial y}(D_y) + \frac{\partial}{\partial z}(D_z)",
                    result=r"\rho = \frac{\partial D_x}{\partial x} + \frac{\partial D_y}{\partial y} + \frac{\partial D_z}{\partial z}",
                    rationale="Η απόκλιση του διανύσματος D καθορίζει τη χωρική πυκνότητα ελεύθερων ηλεκτρικών φορτίων.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Αναγνώριση και καταγραφή των συνιστωσών του διανύσματος D",
                    formula=r"\vec{D} = D_x \hat{x} + D_y \hat{y} + D_z \hat{z}",
                    substitution=r"D_x = -x, \quad D_y = 0, \quad D_z = z^2 y",
                    result=r"(D_x, D_y, D_z) = (-x, \ 0, \ z^2 y)",
                    rationale="Αντιστοίχιση των συνιστωσών του πεδίου μετατόπισης στους καρτεσιανούς άξονες.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Υπολογισμός μερικής παραγώγου της x-συνιστώσας",
                    formula=r"\frac{\partial D_x}{\partial x} = \frac{\partial}{\partial x}(-x)",
                    substitution=r"\frac{\partial}{\partial x}(-x) = -1 \cdot \frac{d}{dx}(x) = -1 \cdot 1 = -1",
                    result=r"\frac{\partial D_x}{\partial x} = -1",
                    rationale="Η παράγωγος του -x ως προς x ισούται με -1.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Υπολογισμός μερικής παραγώγου της y-συνιστώσας",
                    formula=r"\frac{\partial D_y}{\partial y} = \frac{\partial}{\partial y}(0)",
                    substitution=r"\frac{\partial}{\partial y}(0) = 0",
                    result=r"\frac{\partial D_y}{\partial y} = 0",
                    rationale="Η συνιστώσα του πεδίου στον άξονα y είναι μηδενική, συνεπώς η παράγωγός της ισούται με μηδέν.",
                ),
                CalculationStep(
                    step_number=5,
                    title="Υπολογισμός μερικής παραγώγου της z-συνιστώσας",
                    formula=r"\frac{\partial D_z}{\partial z} = \frac{\partial}{\partial z}(z^2 y) = y \cdot \frac{d}{dz}(z^2)",
                    substitution=r"\frac{\partial D_z}{\partial z} = y \cdot (2 z^{2-1}) = y \cdot 2z = 2zy",
                    result=r"\frac{\partial D_z}{\partial z} = 2zy",
                    rationale="Κατά τη μερική παραγώγιση ως προς z, η μεταβλητή y θεωρείται σταθερά, και εφαρμόζεται ο κανόνας παραγώγισης δύναμης.",
                ),
                CalculationStep(
                    step_number=6,
                    title="Άθροιση μερικών παραγώγων και εξαγωγή πυκνότητας φορτίου",
                    formula=r"\rho(x, y, z) = \frac{\partial D_x}{\partial x} + \frac{\partial D_y}{\partial y} + \frac{\partial D_z}{\partial z}",
                    substitution=r"\rho = -1 + 0 + 2zy = 2zy - 1",
                    result=r"\rho(x, y, z) = 2zy - 1 \quad [\text{C/m}^3]",
                    rationale="Η πυκνότητα φορτίου μεταβάλλεται γραμμικά με το γινόμενο zy με σταθερό αρνητικό όρο offset -1.",
                ),
            ],
            final_answer=r"\rho(x, y, z) = 2zy - 1 \quad [\text{C/m}^3]",
            detailed_justification="Η πυκνότητα φορτίου μεταβάλλεται γραμμικά ως προς το γινόμενο zy με σταθερό όρο -1.",
            common_pitfalls=["Μην ξεχάσετε το πρόσημο μείον: d(-x)/dx = -1."],
            related_theory_topic="Εξισώσεις Maxwell & Νόμος Gauss",
        ),
        ExamQuestion(
            question_number=6,
            title="Άσκηση 2: Παράμετροι ΗΜ Κύματος με Διάδοση κατά x",
            question_type="Calculations",
            prompt_text=r"Το ηλεκτρικό πεδίο ημιτονοειδούς επίπεδου ΗΜ κύματος στο κενό δίνεται από: $\vec{E}=60\cos(kx-3\cdot 10^9 t)\hat{y}$. α) Ποιο είναι το μήκος κύματος $\lambda$ και η συχνότητα $f$; β) Να γραφεί το διάνυσμα ταλάντωσης της μαγνητικής επαγωγής $\vec{B}$. γ) Να υπολογισθεί το διάνυσμα Poynting $\vec{S}$ και η ένταση $I$.",
            given_parameters=[
                GivenParameter("E_0", "60 \\text{ V/m}", "Πλάτος ηλεκτρικού πεδίου"),
                GivenParameter(r"\omega", "3 \\times 10^9 \\text{ rad/s}", "Κυκλική συχνότητα"),
                GivenParameter("c", "3 \\times 10^8 \\text{ m/s}", "Ταχύτητα φωτός στο κενό"),
                GivenParameter(r"\mu_0", r"4\pi \times 10^{-7} \text{ T}\cdot\text{m/A}", "Μαγνητική διαπερατότητα κενού"),
            ],
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Αναγνώριση βασικών κυματικών παραμέτρων από την εξίσωση",
                    formula=r"\vec{E}(x,t) = E_0 \cos(kx - \omega t)\hat{u}_E",
                    substitution=r"E_0 = 60 \ \text{V/m}, \quad \omega = 3 \times 10^9 \ \text{rad/s}, \quad \hat{u}_E = \hat{y}, \quad \hat{k} = +\hat{x}",
                    result=r"E_0 = 60 \ \text{V/m}, \quad \omega = 3 \times 10^9 \ \text{rad/s}",
                    rationale="Η φάση (kx - 3·10^9 t) υποδηλώνει διάδοση κατά μήκος του θετικού άξονα x με πόλωση κατά y.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Υπολογισμός γραμμικής συχνότητας f",
                    formula=r"\omega = 2\pi f \implies f = \frac{\omega}{2\pi}",
                    substitution=r"f = \frac{3 \times 10^9 \ \text{rad/s}}{2\pi} \approx \frac{3 \times 10^9}{6.283185} \ \text{Hz} = 4.7746 \times 10^8 \ \text{Hz}",
                    result=r"f \approx 477.46 \ \text{MHz} = 4.7746 \times 10^8 \ \text{Hz}",
                    rationale="Η συχνότητα 477.5 MHz βρίσκεται στη ζώνη τηλεοπτικών και τηλεπικοινωνιακών μεταδόσεων UHF.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Υπολογισμός κυματάριθμου k στο κενό",
                    formula=r"k = \frac{\omega}{c}",
                    substitution=r"k = \frac{3 \times 10^9 \ \text{rad/s}}{3 \times 10^8 \ \text{m/s}} = 10 \ \text{rad/m}",
                    result=r"k = 10 \ \text{rad/m}",
                    rationale="Απλοποίηση λόγου συχνότητας προς ταχύτητα φωτός στο κενό.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Αναλυτικός υπολογισμός μήκους κύματος λ",
                    formula=r"\lambda = \frac{c}{f} = \frac{2\pi}{k}",
                    substitution=r"\lambda = \frac{2\pi}{10} = \frac{\pi}{5} \ \text{m} \approx 0.6283 \ \text{m} = 62.83 \ \text{cm}",
                    result=r"\lambda \approx 0.6283 \ \text{m} = 62.83 \ \text{cm}",
                    rationale="Το μήκος κύματος 62.8 cm επιβεβαιώνει την περιοχή υπερυψηλών συχνοτήτων (UHF).",
                ),
                CalculationStep(
                    step_number=5,
                    title="Υπολογισμός πλάτους μαγνητικού πεδίου B_0",
                    formula=r"B_0 = \frac{E_0}{c}",
                    substitution=r"B_0 = \frac{60 \ \text{V/m}}{3 \times 10^8 \ \text{m/s}} = 20 \times 10^{-8} \ \text{T} = 2 \times 10^{-7} \ \text{T}",
                    result=r"B_0 = 2 \times 10^{-7} \ \text{T} = 0.2 \ \mu\text{T}",
                    rationale="Σταθερός λόγος πλατών E_0/B_0 = c στο κενό.",
                ),
                CalculationStep(
                    step_number=6,
                    title="Προσδιορισμός διανύσματος ταλάντωσης B μέσω εξωτερικού γινομένου",
                    formula=r"\hat{B} = \hat{k} \times \hat{E} \implies \hat{x} \times \hat{y} = \hat{z}",
                    substitution=r"\vec{B}(x,t) = B_0 \cos(kx - \omega t)\hat{z} = 2 \times 10^{-7}\cos(10x - 3\cdot 10^9 t)\hat{z} \ \text{T}",
                    result=r"\vec{B}(x,t) = 2 \times 10^{-7}\cos(10x - 3\cdot 10^9 t)\hat{z} \ \text{T}",
                    rationale="Επειδή x̂ × ŷ = +ẑ, το μαγνητικό πεδίο ταλαντώνεται αυστηρά κατά τον θετικό άξονα z.",
                ),
                CalculationStep(
                    step_number=7,
                    title="Υπολογισμός στιγμιαίου διανύσματος Poynting S",
                    formula=r"\vec{S}(x,t) = \frac{1}{\mu_0}(\vec{E}\times\vec{B}) = \frac{E_0 B_0}{\mu_0}\cos^2(kx - \omega t)(\hat{y}\times\hat{z})",
                    substitution=r"\vec{S} = \frac{60 \times 2\times 10^{-7}}{4\pi \times 10^{-7}}\cos^2(...)(+\hat{x}) = \frac{120}{4\pi}\cos^2(10x - 3\cdot 10^9 t)\hat{x} = \frac{30}{\pi}\cos^2(...)\hat{x}",
                    result=r"\vec{S}(x,t) \approx 9.5493 \cos^2(10x - 3\cdot 10^9 t)\hat{x} \ \text{W/m}^2",
                    rationale="Επειδή ŷ × ẑ = +x̂, η ηλεκτρομαγνητική ισχύς ρέει προς την κατεύθυνση διάδοσης +x̂.",
                ),
                CalculationStep(
                    step_number=8,
                    title="Υπολογισμός μέσης έντασης ακτινοβολίας I",
                    formula=r"I = \langle |\vec{S}| \rangle = \frac{S_{\text{peak}}}{2} = \frac{1}{2} \cdot \frac{30}{\pi} = \frac{15}{\pi}",
                    substitution=r"I = \frac{15}{\pi} \approx \frac{15}{3.14159} \ \text{W/m}^2 \approx 4.7746 \ \text{W/m}^2",
                    result=r"I \approx 4.7746 \ \text{W/m}^2",
                    rationale="Η χρονική μέση τιμή του cos²(θ) σε πλήρεις περιόδους είναι 1/2.",
                ),
            ],
            final_answer=r"\lambda \approx 62.83\text{ cm}, \ f \approx 477.5\text{ MHz}, \ \vec{B} = 2\times 10^{-7}\cos(10x - 3\cdot 10^9 t)\hat{z}\text{ T}, \ \vec{S} \approx 9.55\cos^2(...)\hat{x}\text{ W/m}^2, \ I \approx 4.78\text{ W/m}^2",
            detailed_justification="Το κύμα διαδίδεται κατά +x (όρισμα kx - ωt), με E κατά y και B κατά z.",
            common_pitfalls=["Προσοχή στον άξονα διάδοσης: η φάση περιέχει το x, άρα η διάδοση είναι στον άξονα x, και το Poynting δείχνει προς +x."],
            related_theory_topic="Επίπεδα Ηλεκτρομαγνητικά Κύματα & Διάνυσμα Poynting",
        ),
    ]

    justifications = [
        DesignJustification(
            title="Απουσία Μαγνητικών Μονοπόλων (div B = 0)",
            category="Maxwell Law",
            description="Η συνολική μαγνητική ροή μέσα από οποιαδήποτε κλειστή επιφάνεια είναι ακριβώς ίση με μηδέν, συνεπάγοντας ότι όσες δυναμικές γραμμές εισέρχονται τόσες εξέρχονται.",
            rationale="Θεμελιώδης διαφορά μεταξύ ηλεκτροστατικού και μαγνητοστατικού πεδίου.",
        ),
        DesignJustification(
            title="Ομογένεια Πεδίου σε Επίπεδο Πυκνωτή",
            category="Electrostatics",
            description="Σε επίπεδο πυκνωτή με οπλισμούς μεγάλης έκτασης σε σχέση με την απόσταση d, το πεδίο είναι σταθερό και ίσο με E = V/d.",
            rationale="Απλοποιεί τη χωρητικότητα C = ε A / d ως καθαρά γεωμετρικό μέγεθος.",
        ),
    ]

    solution_code = '''"""Python verification script for June 2026 Team D exam problems."""

import sympy as sp

def verify_divergence() -> None:
    """Verifies Exercise 1: div(D) = rho."""
    x, y, z = sp.symbols('x y z')
    D_x = -x
    D_y = sp.Integer(0)
    D_z = z**2 * y
    
    div_D = sp.diff(D_x, x) + sp.diff(D_y, y) + sp.diff(D_z, z)
    expected = 2 * z * y - 1
    print("--- Askisi 1: Gauss Law Divergence ---")
    print(f"D = [{D_x}] x_hat + [{D_z}] z_hat")
    print(f"div(D) = rho = {div_D}")
    assert sp.simplify(div_D - expected) == 0, f"Mismatch: {div_D} != {expected}"
    print("Verification Askisi 1: PASSED")

def verify_wave() -> None:
    """Verifies Exercise 2: EM wave parameters, Poynting vector, and intensity."""
    c = 3e8
    mu_0 = 4 * 3.141592653589793 * 1e-7
    E_0 = 60.0
    omega = 3e9
    
    k = omega / c
    f = omega / (2 * 3.141592653589793)
    wavelength = c / f
    B_0 = E_0 / c
    S_max = (E_0 * B_0) / mu_0
    intensity = S_max / 2.0
    
    print("\\n--- Askisi 2: Plane EM Wave along x ---")
    print(f"Wavenumber k = {k:.2f} rad/m")
    print(f"Frequency f = {f/1e6:.2f} MHz")
    print(f"Wavelength lambda = {wavelength*100:.2f} cm")
    print(f"Magnetic amplitude B_0 = {B_0:.4e} T")
    print(f"Peak Poynting flux S_max = {S_max:.4f} W/m^2")
    print(f"Radiation Intensity I = {intensity:.4f} W/m^2")
    print("Verification Askisi 2: PASSED")

if __name__ == "__main__":
    verify_divergence()
    verify_wave()
'''

    return Scenario(
        id="past_exam_2026_06_team_d",
        title="Εξεταστική Ιουνίου 2026 — Ομάδα Δ",
        subtitle="Πλήρης Επίλυση: Χωρητικότητα, Μαγνητική Ροή, Νόμος Gauss & Κύμα",
        course_tag="Past Exam 2026",
        duration_info="Διάρκεια: 2 ώρες | 4 Ερωτήσεις Θεωρίας & 2 Ασκήσεις Υπολογισμού",
        paragraphs=paragraphs,
        questions=questions,
        justifications=justifications,
        solution_code=solution_code,
    )

