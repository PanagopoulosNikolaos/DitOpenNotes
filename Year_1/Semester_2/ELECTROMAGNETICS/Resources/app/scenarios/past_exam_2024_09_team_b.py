"""Past Exam Scenario: September 2024 Team B.

Full verbatim transcription of exam paper with three-part contract hover tooltips,
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


def createPastExam202409TeamB() -> Scenario:
    """Instantiates the September 2024 Team B past examination scenario.

    Returns:
        Scenario: Complete scenario container with verbatim text and solutions.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(
                    text="Θέματα Εξεταστικής του μαθήματος ΑΡΧΕΣ ΗΜ ΚΑΙ ΤΗΛΕΠΙΚΟΙΝΩΝΙΩΝ, Σεπτ. 2024. Ομάδα Β\n",
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
                TextSegment(text="Ερώτηση 1. 1 μονάδα\nΠότε μια ", is_highlight=False),
                TextSegment(
                    text="κατανομή φορτίου",
                    is_highlight=True,
                    category="param",
                    tag_label="ΦΟΡΤΙΟ",
                    tooltip="Classification: Χωρική Κατανομή Φορτίου | Detection Clue: Φράση 'κατανομή φορτίου' | Application Rationale: Καθορίζει αν η πυκνότητα ρ είναι συνάρτηση θέσης ρ(r) ή σταθερά.",
                ),
                TextSegment(text=" ονομάζεται ", is_highlight=False),
                TextSegment(
                    text="ομοιόμορφη",
                    is_highlight=True,
                    category="law",
                    tag_label="ΟΜΟΙΟΜΟΡΦΙΑ",
                    tooltip="Classification: Χαρακτηρισμός Ομοιομορφίας | Detection Clue: Ο όρος 'ομοιόμορφη' | Application Rationale: Σημαίνει σταθερή χωρική πυκνότητα φορτίου dq/dV = const παντού στον όγκο.",
                ),
                TextSegment(
                    text=";\nΑ] όταν η πυκνότητα φορτίου είναι σταθερή\nΒ] όταν η πυκνότητα φορτίου είναι μια επιφάνεια Gauss\nΓ] όταν η πυκνότητα φορτίου είναι μηδενική\nΔ] όταν η πυκνότητα φορτίου είναι διανυσματική",
                    is_highlight=False,
                ),
            ],
            accent_border_color="accent",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Ερώτηση 2. 1 μονάδα\nΜε ποια ιδιότητα των κυμάτων συνδέεται η ", is_highlight=False),
                TextSegment(
                    text="στροφορμή",
                    is_highlight=True,
                    category="field",
                    tag_label="ΣΤΡΟΦΟΡΜΗ",
                    tooltip="Classification: Κυματική Στροφορμή (Angular Momentum) | Detection Clue: Η φυσική ιδιότητα στροφορμής φωτονίων/κυμάτων | Application Rationale: Συνδέεται άμεσα με την κυκλική ή ελλειπτική πόλωση του ηλεκτρομαγνητικού πεδίου.",
                ),
                TextSegment(
                    text=";\nΑ] Την πόλωση του κύματος\nΒ] Την ταχύτητα του φωτός\nΓ] Την ένταση του κύματος\nΔ] Το πλάτος ταλάντωσης του κύματος",
                    is_highlight=False,
                ),
            ],
            accent_border_color="accent",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Ερώτηση 3. 1 μονάδα\nΠώς ονομάζεται ο λόγος της ", is_highlight=False),
                TextSegment(
                    text="ταχύτητας του φωτός στο κενό ως προς την ταχύτητα του φωτός στη ύλη",
                    is_highlight=True,
                    category="param",
                    tag_label="c / v",
                    tooltip="Classification: Οπτικός Λόγος Ταχυτήτων | Detection Clue: Ορισμός n = c / v | Application Rationale: Ορίζει τον δείκτη διάθλασης (refractive index) του υλικού.",
                ),
                TextSegment(
                    text=";\nΑ] Δείκτης ανάκλασης\nΒ] Δείκτης πρόσπτωσης\nΓ] Δείκτης περίθλασης\nΔ] Δείκτης διάθλασης",
                    is_highlight=False,
                ),
            ],
            accent_border_color="accent",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Ερώτηση 4. 1 μονάδα\nΤι κατεύθυνση έχουν οι ", is_highlight=False),
                TextSegment(
                    text="δυναμικές γραμμές του μαγνητοστατικού πεδίου",
                    is_highlight=True,
                    category="field",
                    tag_label="ΓΡΑΜΜΕΣ B",
                    tooltip="Classification: Μαγνητικές Δυναμικές Γραμμές | Detection Clue: Δυναμικές γραμμές B | Application Rationale: Εξωτερικά κατευθύνονται από το Βόρειο προς το Νότιο πόλο και κλείνουν στο εσωτερικό (div B = 0).",
                ),
                TextSegment(
                    text=";\nΑ] Από το νότιο πόλο προς τον βόρειο πόλο\nΒ] Από τον νότιο πόλο προς το άπειρο\nΓ] Από το βόρειο πόλο προς στον νότιο πόλο\nΔ] Από τον βόρειο πόλο προς στο άπειρο",
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
                    tag_label="ΔΙΑΝΥΣΜΑ D",
                    tooltip="Classification: Διάνυσμα Ηλεκτρικής Ροής D | Detection Clue: Σύμβολο D | Application Rationale: Συνδέεται απευθείας με τα ελεύθερα φορτία μέσω της διαφορικής απόκλισης div(D) = rho.",
                ),
                TextSegment(text=" ισχύει ", is_highlight=False),
                TextSegment(
                    text="∇·D = ρ",
                    is_highlight=True,
                    category="law",
                    tag_label="ΝΟΜΟΣ GAUSS",
                    tooltip="Classification: 1η Εξίσωση Maxwell | Detection Clue: Διαφορική μορφή div(D) = rho | Application Rationale: Υπολογίζει απευθείας την πυκνότητα φορτίου μέσω μερικών παραγώγων.",
                ),
                TextSegment(text=", όπου ρ η πυκνότητα φορτίου. Αν ", is_highlight=False),
                TextSegment(
                    text="D = 5z x̂ + 12y³ ŷ + 0.3 ẑ",
                    is_highlight=True,
                    category="calc",
                    tag_label="ΣΥΝΙΣΤΩΣΕΣ D",
                    tooltip="Classification: Διανυσματικό Πεδίο Μετατόπισης | Detection Clue: D_x = 5z, D_y = 12y^3, D_z = 0.3 | Application Rationale: Εφαρμόζουμε d(D_x)/dx + d(D_y)/dy + d(D_z)/dz.",
                ),
                TextSegment(
                    text=" να υπολογίσετε την πυκνότητα φορτίου ρ. Δίνεται ότι ∇ = (∂/∂x)x̂ + (∂/∂y)ŷ + (∂/∂z)ẑ και ότι το εσωτερικό γινόμενο δίνεται από: a·b = a_x b_x + a_y b_y + a_z b_z.",
                    is_highlight=False,
                ),
            ],
            accent_border_color="accent",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Άσκηση 2. 3 μονάδες\nΤο ηλεκτρικό πεδίο ενός ημιτονοειδούς επίπεδου ΗΜ κύματος που διαδίδεται στο κενό δίνεται από τη σχέση: ", is_highlight=False),
                TextSegment(
                    text="E = 1.5 cos(10⁻⁸ z - ωt) ŷ",
                    is_highlight=True,
                    category="field",
                    tag_label="E(z,t)",
                    tooltip="Classification: Ηλεκτρικό Πεδίο Επίπεδου Κύματος | Detection Clue: E_0 = 1.5, k = 10^-8 rad/m, πόλωση κατά y, διάδοση κατά +z | Application Rationale: Καθορίζει το μήκος κύματος λ = 2π/k, τη συχνότητα f = c/λ και το B.",
                ),
                TextSegment(
                    text=" α) Ποιο είναι το μήκος κύματος λ και η συχνότητα f του κύματος; β) Να υπολογισθεί το ",
                    is_highlight=False,
                ),
                TextSegment(
                    text="διάνυσμα Poynting S",
                    is_highlight=True,
                    category="calc",
                    tag_label="POYNTING S",
                    tooltip="Classification: Διάνυσμα Ροής Ισχύος S | Detection Clue: S = (1/mu_0) (E x B) | Application Rationale: Υπολογίζει τη στιγμιαία διεύθυνση και πυκνότητα ροής ισχύος.",
                ),
                TextSegment(text=" γ) Να υπολογισθεί η ", is_highlight=False),
                TextSegment(
                    text="ένταση της ακτινοβολίας I",
                    is_highlight=True,
                    category="param",
                    tag_label="ΕΝΤΑΣΗ I",
                    tooltip="Classification: Χρονική Μέση Ένταση Ακτινοβολίας | Detection Clue: I = <S> = (1/2) c eps_0 E_0^2 | Application Rationale: Εκφράζει τη μέση ισχύ ανά μονάδα επιφάνειας.",
                ),
                TextSegment(
                    text=".\nΔίνεται ότι E = E₀cos(kx - ωt)ŷ, B = B₀cos(kx - ωt)ẑ, S = (1/μ₀)(E×B), I = S̄, k = 2π/λ, ω = 2πf, c = λf, E₀ = cB₀, c = 3×10⁸ m/s, μ₀ = 4π×10⁻⁷ Tm/A.",
                    is_highlight=False,
                ),
            ],
            accent_border_color="accent",
        ),
    ]

    questions = [
        ExamQuestion(
            question_number=1,
            title="Ομοιόμορφη Κατανομή Φορτίου",
            question_type="Multiple Choice",
            prompt_text="Πότε μια κατανομή φορτίου ονομάζεται ομοιόμορφη;",
            options=[
                QuestionOption(
                    letter="Α",
                    text="όταν η πυκνότητα φορτίου είναι σταθερή",
                    is_correct=True,
                    explanation="Σωστό: Ομοιόμορφη ονομάζεται η κατανομή όταν η πυκνότητα ρ (ή σ ή λ) διατηρεί την ίδια ακριβώς τιμή σε όλα τα σημεία του σώματος.",
                ),
                QuestionOption(
                    letter="Β",
                    text="όταν η πυκνότητα φορτίου είναι μια επιφάνεια Gauss",
                    is_correct=False,
                    explanation="Λάθος: Η επιφάνεια Gauss είναι νοητή μαθηματική επιφάνεια υπολογισμού ροής, όχι είδος πυκνότητας.",
                ),
                QuestionOption(
                    letter="Γ",
                    text="όταν η πυκνότητα φορτίου είναι μηδενική",
                    is_correct=False,
                    explanation="Λάθος: Αν η πυκνότητα είναι μηδενική δεν υφίσταται κατανομή φορτίου.",
                ),
                QuestionOption(
                    letter="Δ",
                    text="όταν η πυκνότητα φορτίου είναι διανυσματική",
                    is_correct=False,
                    explanation="Λάθος: Η πυκνότητα φορτίου ρ είναι βαθμωτό μέγεθος (Coulomb/m³), ποτέ διανυσματικό.",
                ),
            ],
            correct_option_letter="Α",
            final_answer="Α] όταν η πυκνότητα φορτίου είναι σταθερή",
            detailed_justification="Κατά ορισμό, ομογενής ή ομοιόμορφη κατανομή φορτίου σημαίνει dQ/dV = ρ = σταθερό, δηλαδή το φορτίο είναι ισοκατανεμημένο.",
            common_pitfalls=["Μην συγχέετε την πυκνότητα φορτίου ρ (βαθμωτό μέγεθος) με την πυκνότητα ρεύματος J (διανυσματικό μέγεθος)."],
            related_theory_topic="Ηλεκτροστατική & Κατανομές Φορτίου",
        ),
        ExamQuestion(
            question_number=2,
            title="Στροφορμή Κυμάτων και Πόλωση",
            question_type="Multiple Choice",
            prompt_text="Με ποια ιδιότητα των κυμάτων συνδέεται η στροφορμή;",
            options=[
                QuestionOption(
                    letter="Α",
                    text="Την πόλωση του κύματος",
                    is_correct=True,
                    explanation="Σωστό: Η στροφορμή (spin angular momentum) των ηλεκτρομαγνητικών κυμάτων συνδέεται άμεσα με την κυκλική πόλωση (περιστροφή του διανύσματος Ε).",
                ),
                QuestionOption(
                    letter="Β",
                    text="Την ταχύτητα του φωτός",
                    is_correct=False,
                    explanation="Λάθος: Η ταχύτητα c είναι σταθερά διάδοσης του μέσου και δεν σχετίζεται με τη στροφορμή.",
                ),
                QuestionOption(
                    letter="Γ",
                    text="Την ένταση του κύματος",
                    is_correct=False,
                    explanation="Λάθος: Η ένταση μετρά τη ροή ισχύος ανά επιφάνεια (πλάτος στο τετράγωνο).",
                ),
                QuestionOption(
                    letter="Δ",
                    text="Το πλάτος ταλάντωσης του κύματος",
                    is_correct=False,
                    explanation="Λάθος: Το πλάτος καθορίζει τη μέγιστη ένταση του πεδίου, όχι τον προσανατολισμό στροφορμής.",
                ),
            ],
            correct_option_letter="Α",
            final_answer="Α] Την πόλωση του κύματος",
            detailed_justification="Ένα κυκλικά πολωμένο ηλεκτρομαγνητικό κύμα μεταφέρει στροφορμή ±ℏ ανά φωτόνιο λόγω της συνεχούς περιστροφής του ηλεκτρικού διανύσματος.",
            common_pitfalls=["Προσοχή: Η γραμμική ορμή συνδέεται με τη διεύθυνση διάδοσης k, ενώ η στροφορμή με την πόλωση."],
            related_theory_topic="Ηλεκτρομαγνητικά Κύματα & Πόλωση",
        ),
        ExamQuestion(
            question_number=3,
            title="Δείκτης Διάθλασης Υλικού",
            question_type="Multiple Choice",
            prompt_text="Πώς ονομάζεται ο λόγος της ταχύτητας του φωτός στο κενό ως προς την ταχύτητα του φωτός στη ύλη;",
            options=[
                QuestionOption(
                    letter="Α",
                    text="Δείκτης ανάκλασης",
                    is_correct=False,
                    explanation="Λάθος: Ο συντελεστής ανάκλασης Γ αφορά λόγο πλατών κυμάτων.",
                ),
                QuestionOption(
                    letter="Β",
                    text="Δείκτης πρόσπτωσης",
                    is_correct=False,
                    explanation="Λάθος: Δεν υπάρχει τέτοιο φυσικό μέγεθος.",
                ),
                QuestionOption(
                    letter="Γ",
                    text="Δείκτης περίθλασης",
                    is_correct=False,
                    explanation="Λάθος: Η περίθλαση είναι κυματικό φαινόμενο κάμψης, όχι λόγος ταχυτήτων.",
                ),
                QuestionOption(
                    letter="Δ",
                    text="Δείκτης διάθλασης",
                    is_correct=True,
                    explanation="Σωστό: Ο απόλυτος δείκτης διάθλασης ορίζεται ως n = c / v >= 1.",
                ),
            ],
            correct_option_letter="Δ",
            final_answer="Δ] Δείκτης διάθλασης (n = c / v)",
            detailed_justification="Ο δείκτης διάθλασης n = c/v = sqrt(ε_r μ_r) εκφράζει πόσο επιβραδύνεται η φασική ταχύτητα του φωτός μέσα στο υλικό.",
            common_pitfalls=["Ο δείκτης διάθλασης για παθητικά φυσικά μέσα είναι πάντα n >= 1."],
            related_theory_topic="Οπτική & Διάδοση σε Υλικά",
        ),
        ExamQuestion(
            question_number=4,
            title="Κατεύθυνση Μαγνητικών Δυναμικών Γραμμών",
            question_type="Multiple Choice",
            prompt_text="Τι κατεύθυνση έχουν οι δυναμικές γραμμές του μαγνητοστατικού πεδίου;",
            options=[
                QuestionOption(
                    letter="Α",
                    text="Από το νότιο πόλο προς τον βόρειο πόλο",
                    is_correct=False,
                    explanation="Λάθος: Αυτή είναι η κατεύθυνση στο εσωτερικό του μαγνήτη, όχι η συμβατική εξωτερική διαδρομή.",
                ),
                QuestionOption(
                    letter="Β",
                    text="Από τον νότιο πόλο προς το άπειρο",
                    is_correct=False,
                    explanation="Λάθος: Οι μαγνητικές γραμμές δεν καταλήγουν στο άπειρο γιατί δεν υπάρχουν μονόπολα (div B = 0).",
                ),
                QuestionOption(
                    letter="Γ",
                    text="Από το βόρειο πόλο προς στον νότιο πόλο",
                    is_correct=True,
                    explanation="Σωστό: Εξωτερικά του μαγνήτη, οι δυναμικές γραμμές εξέρχονται από τον Βόρειο πόλο και εισέρχονται στον Νότιο.",
                ),
                QuestionOption(
                    letter="Δ",
                    text="Από τον βόρειο πόλο προς στο άπειρο",
                    is_correct=False,
                    explanation="Λάθος: Οι γραμμές του B είναι κλειστές καμπύλες και δεν εκτείνονται μονοπολικά στο άπειρο.",
                ),
            ],
            correct_option_letter="Γ",
            final_answer="Γ] Από το βόρειο πόλο προς στον νότιο πόλο",
            detailed_justification="Σύμφωνα με τον νόμο του Gauss για τον μαγνητισμό (div B = 0), οι γραμμές είναι συνεχείς κλειστοί βρόχοι που εξέρχονται από το N και εισέρχονται στο S.",
            common_pitfalls=["Στο ηλεκτρικό πεδίο οι γραμμές πηγάζουν από το + και καταλήγουν στο - ή στο άπειρο, αλλά στο μαγνητικό είναι κλειστές."],
            related_theory_topic="Μαγνητοστατική & Νόμος Gauss για το B",
        ),
        ExamQuestion(
            question_number=5,
            title="Άσκηση 1: Υπολογισμός Πυκνότητας Φορτίου ρ από τη Μετατόπιση D",
            question_type="Calculations",
            prompt_text=r"Σύμφωνα με τον νόμο του Gauss για τη διηλεκτρική μετατόπιση $\vec{D}$ ισχύει $\vec{\nabla}\cdot\vec{D}=\rho$. Αν $\vec{D}=5z\hat{x}+12y^3\hat{y}+0.3\hat{z}$, να υπολογίσετε την πυκνότητα φορτίου $\rho$.",
            given_parameters=[
                GivenParameter("D_x", "5z", "x-συνιστώσα μετατόπισης"),
                GivenParameter("D_y", "12y^3", "y-συνιστώσα μετατόπισης"),
                GivenParameter("D_z", "0.3", "z-συνιστώσα μετατόπισης"),
            ],
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Διατύπωση διαφορικής μορφής 1ης εξίσωσης Maxwell (Νόμος Gauss)",
                    formula=r"\rho = \vec{\nabla}\cdot\vec{D} = \frac{\partial D_x}{\partial x} + \frac{\partial D_y}{\partial y} + \frac{\partial D_z}{\partial z}",
                    substitution=r"\rho = \frac{\partial}{\partial x}(D_x) + \frac{\partial}{\partial y}(D_y) + \frac{\partial}{\partial z}(D_z)",
                    result=r"\rho = \frac{\partial D_x}{\partial x} + \frac{\partial D_y}{\partial y} + \frac{\partial D_z}{\partial z}",
                    rationale="Ο διαφορικός νόμος του Gauss συνδέει την απόκλιση της διηλεκτρικής μετατόπισης απευθείας με την τοπική χωρική πυκνότητα ελεύθερων φορτίων.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Αναγνώριση και καταγραφή των συνιστωσών του διανύσματος D",
                    formula=r"\vec{D} = D_x \hat{x} + D_y \hat{y} + D_z \hat{z}",
                    substitution=r"D_x = 5z, \quad D_y = 12y^3, \quad D_z = 0.3",
                    result=r"(D_x, D_y, D_z) = (5z, \ 12y^3, \ 0.3)",
                    rationale="Αντιστοίχιση των διανυσματικών συνιστωσών στους καρτεσιανούς άξονες x, y και z.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Υπολογισμός μερικής παραγώγου της x-συνιστώσας",
                    formula=r"\frac{\partial D_x}{\partial x} = \frac{\partial}{\partial x}(5z)",
                    substitution=r"\frac{\partial}{\partial x}(5z) = 5z \cdot \frac{\partial}{\partial x}(1) = 5z \cdot 0",
                    result=r"\frac{\partial D_x}{\partial x} = 0",
                    rationale="Κατά τη μερική παραγώγιση ως προς x, η μεταβλητή z θεωρείται σταθερή, συνεπώς η παράγωγος ισούται με μηδέν.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Υπολογισμός μερικής παραγώγου της y-συνιστώσας",
                    formula=r"\frac{\partial D_y}{\partial y} = \frac{\partial}{\partial y}(12y^3) = 12 \frac{d}{dy}(y^3)",
                    substitution=r"\frac{\partial D_y}{\partial y} = 12 \cdot (3y^{3-1}) = 12 \cdot 3y^2 = 36y^2",
                    result=r"\frac{\partial D_y}{\partial y} = 36y^2",
                    rationale="Εφαρμογή του κανόνα παραγώγισης δύναμης d(y^n)/dy = n y^(n-1) με σταθερό συντελεστή 12.",
                ),
                CalculationStep(
                    step_number=5,
                    title="Υπολογισμός μερικής παραγώγου της z-συνιστώσας",
                    formula=r"\frac{\partial D_z}{\partial z} = \frac{\partial}{\partial z}(0.3)",
                    substitution=r"\frac{\partial}{\partial z}(0.3) = 0",
                    result=r"\frac{\partial D_z}{\partial z} = 0",
                    rationale="Η παράγωγος οποιασδήποτε καθαρής σταθεράς είναι αυστηρά μηδέν.",
                ),
                CalculationStep(
                    step_number=6,
                    title="Άθροιση μερικών παραγώγων και εξαγωγή πυκνότητας φορτίου",
                    formula=r"\rho(x, y, z) = \frac{\partial D_x}{\partial x} + \frac{\partial D_y}{\partial y} + \frac{\partial D_z}{\partial z}",
                    substitution=r"\rho = 0 + 36y^2 + 0 = 36y^2",
                    result=r"\rho(x, y, z) = 36y^2 \quad [\text{C/m}^3]",
                    rationale="Η τελική συνάρτηση κατανομής φορτίου εξαρτάται αποκλειστικά από την τετραγωνική απόσταση y από το επίπεδο xz.",
                ),
            ],
            final_answer=r"\rho(x, y, z) = 36y^2 \quad [\text{C/m}^3]",
            detailed_justification="Η 1η εξίσωση Maxwell (Νόμος Gauss) συνδέει απευθείας την απόκλιση του D με την τοπική χωρική πυκνότητα ελεύθερου φορτίου.",
            common_pitfalls=["Προσοχή: μην παραγωγίζετε το 5z ως προς z στο πρώτο όρο. Ο πρώτος όρος είναι d(D_x)/dx."],
            related_theory_topic="Εξισώσεις Maxwell & Νόμος Gauss",
        ),
        ExamQuestion(
            question_number=6,
            title="Άσκηση 2: Παράμετροι Επιπέδου ΗΜ Κύματος & Διάνυσμα Poynting",
            question_type="Calculations",
            prompt_text=r"Το ηλεκτρικό πεδίο ημιτονοειδούς επίπεδου ΗΜ κύματος στο κενό δίνεται από: $\vec{E}=1.5\cos(10^{-8}z-\omega t)\hat{y}$. α) Ποιο είναι το μήκος κύματος $\lambda$ και η συχνότητα $f$; β) Υπολογίστε το διάνυσμα Poynting $\vec{S}$. γ) Υπολογίστε την ένταση ακτινοβολίας $I$.",
            given_parameters=[
                GivenParameter("E_0", "1.5 \\text{ V/m}", "Πλάτος ηλεκτρικού πεδίου"),
                GivenParameter("k", "10^{-8} \\text{ rad/m}", "Κυματάριθμος κατά z"),
                GivenParameter("c", "3 \\times 10^8 \\text{ m/s}", "Ταχύτητα φωτός στο κενό"),
                GivenParameter(r"\mu_0", r"4\pi \times 10^{-7} \text{ T}\cdot\text{m/A}", "Μαγνητική διαπερατότητα κενού"),
            ],
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Αναγνώριση βασικών κυματικών παραμέτρων από την εκφώνηση",
                    formula=r"\vec{E}(z,t) = E_0 \cos(kz - \omega t)\hat{u}_E",
                    substitution=r"E_0 = 1.5 \ \text{V/m}, \quad k = 10^{-8} \ \text{rad/m}, \quad \hat{u}_E = \hat{y}, \quad \hat{k} = +\hat{z}",
                    result=r"E_0 = 1.5 \ \text{V/m}, \quad k = 10^{-8} \ \text{rad/m}",
                    rationale="Η φάση (kz - ωt) υποδηλώνει διάδοση προς τη θετική κατεύθυνση του άξονα z με πόλωση κατά y.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Αναλυτικός υπολογισμός μήκους κύματος λ",
                    formula=r"\lambda = \frac{2\pi}{k}",
                    substitution=r"\lambda = \frac{2\pi}{10^{-8}} = 2\pi \times 10^8 \ \text{m}",
                    result=r"\lambda \approx 6.2832 \times 10^8 \ \text{m}",
                    rationale="Ο κυματάριθμος k εκφράζει την χωρική συχνότητα ανά 2π ακτίνια (m^-1).",
                ),
                CalculationStep(
                    step_number=3,
                    title="Αναλυτικός υπολογισμός κυκλικής συχνότητας ω",
                    formula=r"\omega = c \cdot k",
                    substitution=r"\omega = (3 \times 10^8 \ \text{m/s}) \times (10^{-8} \ \text{rad/m}) = 3 \ \text{rad/s}",
                    result=r"\omega = 3 \ \text{rad/s}",
                    rationale="Στο κενό ισχύει η γραμμική σχέση διασποράς ω = c k χωρίς παραμόρφωση φάσης.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Υπολογισμός γραμμικής συχνότητας f",
                    formula=r"f = \frac{\omega}{2\pi} = \frac{c}{\lambda}",
                    substitution=r"f = \frac{3}{2\pi} \approx \frac{3}{6.283185} \ \text{Hz}",
                    result=r"f \approx 0.4775 \ \text{Hz}",
                    rationale="Η συχνότητα εκφράζει τον ρυθμό πλήρων χρονικών ταλαντώσεων ανά δευτερόλεπτο.",
                ),
                CalculationStep(
                    step_number=5,
                    title="Υπολογισμός πλάτους μαγνητικού πεδίου B_0",
                    formula=r"B_0 = \frac{E_0}{c}",
                    substitution=r"B_0 = \frac{1.5 \ \text{V/m}}{3 \times 10^8 \ \text{m/s}} = 0.5 \times 10^{-8} \ \text{T} = 5 \times 10^{-9} \ \text{T}",
                    result=r"B_0 = 5 \times 10^{-9} \ \text{T} = 5 \ \text{nT}",
                    rationale="Τα πλάτη των ηλεκτρικών και μαγνητικών πεδίων συνδέονται σταθερά μέσω της ταχύτητας του φωτός c.",
                ),
                CalculationStep(
                    step_number=6,
                    title="Προσδιορισμός διεύθυνσης μαγνητικού πεδίου B μέσω εξωτερικού γινομένου",
                    formula=r"\hat{B} = \hat{k} \times \hat{E}",
                    substitution=r"\hat{B} = \hat{z} \times \hat{y} = -\hat{x}",
                    result=r"\vec{B}(z,t) = -5 \times 10^{-9}\cos(10^{-8}z - 3t)\hat{x} \ \text{T}",
                    rationale="Από τον κανόνα του δεξιού χεριού ẑ × ŷ = -x̂, εξασφαλίζοντας ότι η ροή ενέργειας δείχνει προς τα +z.",
                ),
                CalculationStep(
                    step_number=7,
                    title="Υπολογισμός στιγμιαίου διανύσματος Poynting S",
                    formula=r"\vec{S}(z,t) = \frac{1}{\mu_0}(\vec{E}\times\vec{B}) = \frac{E_0 B_0}{\mu_0}\cos^2(kz - \omega t)(\hat{y} \times (-\hat{x}))",
                    substitution=r"\vec{S} = \frac{1.5 \times 5\times 10^{-9}}{4\pi \times 10^{-7}}\cos^2(10^{-8}z - 3t)(+\hat{z}) = \frac{7.5 \times 10^{-9}}{1.2566 \times 10^{-6}}\cos^2(...)\hat{z}",
                    result=r"\vec{S}(z,t) \approx 5.968 \times 10^{-3} \cos^2(10^{-8}z - 3t)\hat{z} \ \text{W/m}^2",
                    rationale="Το διάνυσμα Poynting περιγράφει την στιγμιαία ροή ενέργειας ανά μονάδα επιφάνειας.",
                ),
                CalculationStep(
                    step_number=8,
                    title="Υπολογισμός μέσης έντασης ακτινοβολίας I",
                    formula=r"I = \langle |\vec{S}| \rangle = \frac{S_{\text{peak}}}{2} = \frac{E_0 B_0}{2\mu_0} = \frac{E_0^2}{2\mu_0 c}",
                    substitution=r"I = \frac{5.9683 \times 10^{-3}}{2} \approx 2.984 \times 10^{-3} \ \text{W/m}^2",
                    result=r"I \approx 2.984 \ \text{mW/m}^2 = 2.984 \times 10^{-3} \ \text{W/m}^2",
                    rationale="Η μέση τιμή της συνάρτησης cos²(θ) σε μία πλήρη περίοδο ισούται αυστηρά με 1/2.",
                ),
            ],
            final_answer=r"\lambda \approx 6.28\times 10^8\text{ m}, \ f \approx 0.477\text{ Hz}, \ \vec{S} \approx 5.97\times 10^{-3}\cos^2(10^{-8}z-3t)\hat{z}\text{ W/m}^2, \ I \approx 2.98\text{ mW/m}^2",
            detailed_justification="Η διάδοση του κύματος είναι κατά +z (πρόσημο -ωt), με E κατά y και B κατά -x, επιβεβαιώνοντας ότι E x B δείχνει προς τη διάδοση.",
            common_pitfalls=[
                "Μην ξεχνάτε το πρόσημο μείον στο διάνυσμα B: ŷ × (-x̂) = +ẑ. Αν το B ήταν κατά +x, το κύμα θα διαδιδόταν προς τα -z!",
                "Η ένταση I είναι η μέση τιμή και περιέχει τον παράγοντα 1/2, σε αντίθεση με το στιγμιαίο μέγιστο του S.",
            ],
            related_theory_topic="Επίπεδα Ηλεκτρομαγνητικά Κύματα & Διάνυσμα Poynting",
        ),
    ]

    justifications = [
        DesignJustification(
            title="Διαφορικός Νόμος Gauss (div D = ρ)",
            category="Maxwell Law",
            description="Η απόκλιση του διανύσματος ηλεκτρικής μετατόπισης D ισούται ακριβώς με την τοπική χωρική πυκνότητα ελεύθερων φορτίων ρ.",
            rationale="Επιτρέπει τον άμεσο αναλυτικό προσδιορισμό του φορτίου χωρίς την ανάγκη εκτέλεσης επιφανειακών ολοκληρωμάτων.",
        ),
        DesignJustification(
            title="Ορθογωνιότητα Τριέδρου Πεδίων (E, B, k)",
            category="Wave Property",
            description="Στα επίπεδα αρμονικά κύματα στο κενό τα διανύσματα E, B και k σχηματίζουν δεξιόστροφο ορθογώνιο σύστημα.",
            rationale="Εγγυάται τη διατήρηση της εγκάρσιας φύσης των ηλεκτρομαγνητικών κυμάτων (TEM - Transverse ElectroMagnetic).",
        ),
    ]

    solution_code = '''"""Python verification script for September 2024 Team B exam problems."""

import sympy as sp

def verify_divergence() -> None:
    """Verifies Exercise 1: div(D) = rho."""
    x, y, z = sp.symbols('x y z')
    D_x = 5 * z
    D_y = 12 * y**3
    D_z = sp.Float('0.3')
    
    div_D = sp.diff(D_x, x) + sp.diff(D_y, y) + sp.diff(D_z, z)
    print("--- Askisi 1: Gauss Law Divergence ---")
    print(f"D = [{D_x}] x_hat + [{D_y}] y_hat + [{D_z}] z_hat")
    print(f"div(D) = rho = {div_D} C/m^3")
    assert div_D == 36 * y**2, f"Expected 36*y^2, got {div_D}"
    print("Verification Askisi 1: PASSED")

def verify_plane_wave() -> None:
    """Verifies Exercise 2: EM wave parameters, Poynting vector, and intensity."""
    c = 3e8
    mu_0 = 4 * 3.141592653589793 * 1e-7
    E_0 = 1.5
    k = 1e-8
    
    wavelength = 2 * 3.141592653589793 / k
    omega = c * k
    f = omega / (2 * 3.141592653589793)
    B_0 = E_0 / c
    S_max = (E_0 * B_0) / mu_0
    intensity = S_max / 2.0
    
    print("\\n--- Askisi 2: Plane EM Wave ---")
    print(f"Wavelength lambda = {wavelength:.4e} m")
    print(f"Angular frequency omega = {omega:.2f} rad/s")
    print(f"Frequency f = {f:.4f} Hz")
    print(f"Magnetic amplitude B_0 = {B_0:.4e} T")
    print(f"Peak Poynting flux S_max = {S_max:.6f} W/m^2")
    print(f"Radiation Intensity I = {intensity:.6f} W/m^2")
    print("Verification Askisi 2: PASSED")

if __name__ == "__main__":
    verify_divergence()
    verify_plane_wave()
'''

    return Scenario(
        id="past_exam_2024_09_team_b",
        title="Εξεταστική Σεπτεμβρίου 2024 — Ομάδα Β",
        subtitle="Πλήρης Επίλυση: Νόμος Gauss, Διάνυσμα Poynting & Επίπεδο Κύμα",
        course_tag="Past Exam 2024",
        duration_info="Διάρκεια: 2 ώρες | 4 Ερωτήσεις Θεωρίας & 2 Ασκήσεις Υπολογισμού",
        paragraphs=paragraphs,
        questions=questions,
        justifications=justifications,
        solution_code=solution_code,
    )

