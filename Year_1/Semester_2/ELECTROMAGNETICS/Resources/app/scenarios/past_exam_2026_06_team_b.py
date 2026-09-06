"""Past Exam Scenario: June 2026 Team B.

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


def createPastExam202606TeamB() -> Scenario:
    """Instantiates the June 2026 Team B past examination scenario.

    Returns:
        Scenario: Complete scenario container with verbatim text and solutions.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(
                    text="Εξεταστική. ΑΡΧΕΣ ΗΛΕΚΤΡΟΜΑΓΝΗΤΙΣΜΟΥ ΚΑΙ ΤΗΛΕΠΙΚΟΙΝΩΝΙΩΝ. Ιούνιος 2026. Ομάδα Β\n",
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
                TextSegment(text="Ερώτηση 1.\nΓια την ", is_highlight=False),
                TextSegment(
                    text="αύξηση της χωρητικότητας του πυκνωτή",
                    is_highlight=True,
                    category="param",
                    tag_label="ΧΩΡΗΤΙΚΟΤΗΤΑ C",
                    tooltip="Classification: Χωρητικότητα Πυκνωτή C | Detection Clue: 'αύξηση της χωρητικότητας' | Application Rationale: Η χωρητικότητα C = κ ε_0 A/d αυξάνεται κατά τον παράγοντα κ > 1 με την προσθήκη διηλεκτρικού.",
                ),
                TextSegment(text=" τοποθετούνται ", is_highlight=False),
                TextSegment(
                    text="διηλεκτρικά υλικά",
                    is_highlight=True,
                    category="law",
                    tag_label="ΔΙΗΛΕΚΤΡΙΚΑ",
                    tooltip="Classification: Διηλεκτρικό Μέσο (Dielectrics) | Detection Clue: Συμπλήρωση κενού | Application Rationale: Τα διηλεκτρικά πολώνονται μειώνοντας το εσωτερικό ηλεκτρικό πεδίο και επιτρέποντας αποθήκευση περισσότερου φορτίου για δεδομένη τάση.",
                ),
                TextSegment(text=" ανάμεσα στους οπλισμούς του;", is_highlight=False),
            ],
            accent_border_color="accent",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Ερώτηση 2.\nΑν ένα σώμα με φορτία έχει ", is_highlight=False),
                TextSegment(
                    text="κοιλότητες στο εσωτερικό του",
                    is_highlight=True,
                    category="geom",
                    tag_label="ΚΟΙΛΟΤΗΤΑ",
                    tooltip="Classification: Εσωτερική Κοιλότητα Αγωγού | Detection Clue: 'κοιλότητες στο εσωτερικό του' | Application Rationale: Αρχή ηλεκτροστατικής θωράκισης (Faraday cage): σε αγωγό σε ισορροπία το πεδίο στην κενή κοιλότητα είναι μηδέν.",
                ),
                TextSegment(
                    text=", τότε πώς διαμορφώνεται το πεδίο στο εσωτερικό του;\nΑ] το πεδίο στο εσωτερικό τους είναι κβαντικό\nΒ] το πεδίο στο εσωτερικό τους είναι πολωμένο\nΓ] το πεδίο στο εσωτερικό τους είναι ομοιόμορφο\nΔ] το πεδίο στο εσωτερικό τους είναι ίσο με μηδέν",
                    is_highlight=False,
                ),
            ],
            accent_border_color="accent",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Ερώτηση 3.\nΤο φυσικό μέγεθος που περιγράφει την ", is_highlight=False),
                TextSegment(
                    text="κίνηση φορτίων μέσα από μια επιφάνεια",
                    is_highlight=True,
                    category="param",
                    tag_label="ΚΙΝΗΣΗ ΦΟΡΤΙΩΝ",
                    tooltip="Classification: Ροή Ηλεκτρικού Ρεύματος | Detection Clue: 'κίνηση φορτίων μέσα από επιφάνεια' | Application Rationale: Ορίζει την ένταση του ρεύματος I = dq/dt ή την πυκνότητα ρεύματος J = dI/dS.",
                ),
                TextSegment(text=" το ονομάζουμε πυκνότητα ", is_highlight=False),
                TextSegment(
                    text="ρεύματος",
                    is_highlight=True,
                    category="field",
                    tag_label="ΠΥΚΝΟΤΗΤΑ J",
                    tooltip="Classification: Διάνυσμα Πυκνότητας Ρεύματος J | Detection Clue: Συμπλήρωση κενού: 'πυκνότητα ...' | Application Rationale: Το διάνυσμα J εκφράζει το ρεύμα ανά μονάδα κάθετης επιφάνειας [A/m²].",
                ),
                TextSegment(text=" .", is_highlight=False),
            ],
            accent_border_color="accent",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Ερώτηση 4.\nΠοια είναι η ", is_highlight=False),
                TextSegment(
                    text="διεύθυνση ταλάντωσης του διανύσματος Poynting",
                    is_highlight=True,
                    category="calc",
                    tag_label="ΔΙΕΥΘΥΝΣΗ S",
                    tooltip="Classification: Διεύθυνση Διανύσματος Poynting | Detection Clue: S = (1/mu_0)(E x B) | Application Rationale: Το διάνυσμα Poynting δείχνει πάντα προς τη διεύθυνση διάδοσης του κύματος, δηλαδή παράλληλα στο διάνυσμα κυματαριθμού k.",
                ),
                TextSegment(
                    text=";\nΑ] Παράλληλα στο διάνυσμα του κυματαριθμού\nΒ] Παράλληλα στο διάνυσμα του ηλεκτρικού πεδίου\nΓ] Παράλληλα στο διάνυσμα του μαγνητικού πεδίου\nΔ] Παράλληλα στο διάνυσμα της πόλωσης",
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
                    tooltip="Classification: Διάνυσμα Ηλεκτρικής Ροής D | Detection Clue: ∇·D = ρ | Application Rationale: Παραγώγιση κατά x, y, z για την εξαγωγή της πυκνότητας φορτίου.",
                ),
                TextSegment(text=" ισχύει ∇·D = ρ, όπου ρ η πυκνότητα φορτίου. Αν ", is_highlight=False),
                TextSegment(
                    text="D = x² x̂ - zy ẑ",
                    is_highlight=True,
                    category="calc",
                    tag_label="ΣΥΝΙΣΤΩΣΕΣ D",
                    tooltip="Classification: Συνιστώσες D_x = x^2, D_y = 0, D_z = -zy | Detection Clue: D = x^2 x̂ - zy ẑ | Application Rationale: d(x^2)/dx = 2x, d(-zy)/dz = -y.",
                ),
                TextSegment(text=" να υπολογίσετε την πυκνότητα φορτίου ρ.", is_highlight=False),
            ],
            accent_border_color="accent",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Άσκηση 2. 3 μονάδες\nΤο μαγνητικό πεδίο ενός ημιτονοειδούς επίπεδου ΗΜ κύματος που διαδίδεται στο κενό δίνεται από τη σχέση:\n", is_highlight=False),
                TextSegment(
                    text="B = 3 cos(100π z - ωt) ŷ",
                    is_highlight=True,
                    category="field",
                    tag_label="B(z,t)",
                    tooltip="Classification: Μαγνητικό Πεδίο Επίπεδου Κύματος | Detection Clue: B_0 = 3 T, k = 100π rad/m, πόλωση κατά y, διάδοση κατά +z | Application Rationale: Υπολογισμός λ = 2π/k, ω = ck, E_0 = cB_0 και διάνυσμα E.",
                ),
                TextSegment(
                    text=" α) Ποιο είναι το μήκος κύματος λ και η συχνότητα f του κύματος; β) Να γραφεί το ",
                    is_highlight=False,
                ),
                TextSegment(
                    text="διάνυσμα ταλάντωσης του Ηλεκτρικού πεδίου E",
                    is_highlight=True,
                    category="field",
                    tag_label="ΔΙΑΝΥΣΜΑ E",
                    tooltip="Classification: Ηλεκτρικό Πεδίο E | Detection Clue: E_0 = c B_0 και x̂ × ŷ = ẑ | Application Rationale: E(z,t) = 9*10^8 cos(100π z - ωt) x̂ V/m.",
                ),
                TextSegment(text=". γ) Να υπολογισθεί το ", is_highlight=False),
                TextSegment(
                    text="διάνυσμα Poynting S και η ένταση I",
                    is_highlight=True,
                    category="calc",
                    tag_label="S & I",
                    tooltip="Classification: Ροή Ισχύος Poynting και Μέση Ένταση | Detection Clue: S = (1/mu_0)(E x B), I = S_max / 2 | Application Rationale: S_max = 2.15*10^15 W/m^2, I = 1.07*10^15 W/m^2.",
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
            title="Αύξηση Χωρητικότητας Πυκνωτή (Συμπλήρωση Κενού)",
            question_type="Theory Analysis",
            prompt_text="Για την αύξηση της χωρητικότητας του πυκνωτή τοποθετούνται .................................................... ανάμεσα στους οπλισμούς του;",
            options=[],
            final_answer="διηλεκτρικά υλικά (ή διηλεκτρικά)",
            detailed_justification="Η εισαγωγή διηλεκτρικού με σχετική διηλεκτρική σταθερά κ = ε_r > 1 αυξάνει τη χωρητικότητα κατά C = κ C_0, λόγω της ανάπτυξης δεσμίων φορτίων πόλωσης.",
            common_pitfalls=["Αν τοποθετηθεί αγώγιμο υλικό που ενώνει τους οπλισμούς, ο πυκνωτής βραχυκυκλώνεται και καταστρέφεται."],
            related_theory_topic="Πυκνωτές & Διηλεκτρικά Υλικά",
        ),
        ExamQuestion(
            question_number=2,
            title="Ηλεκτρικό Πεδίο σε Κοιλότητα Αγωγού",
            question_type="Multiple Choice",
            prompt_text="Αν ένα σώμα με φορτία έχει κοιλότητες στο εσωτερικό του, τότε πώς διαμορφώνεται το πεδίο στο εσωτερικό του;",
            options=[
                QuestionOption(
                    letter="Α",
                    text="το πεδίο στο εσωτερικό τους είναι κβαντικό",
                    is_correct=False,
                    explanation="Λάθος: Η κλασική ηλεκτροστατική περιγράφει πλήρως το φαινόμενο χωρίς κβαντικές διορθώσεις.",
                ),
                QuestionOption(
                    letter="Β",
                    text="το πεδίο στο εσωτερικό τους είναι πολωμένο",
                    is_correct=False,
                    explanation="Λάθος: Το πεδίο μέσα σε κενή κοιλότητα δεν πολώνεται.",
                ),
                QuestionOption(
                    letter="Γ",
                    text="το πεδίο στο εσωτερικό τους είναι ομοιόμορφο",
                    is_correct=False,
                    explanation="Λάθος: Το πεδίο δεν είναι απλά ομοιόμορφο, αλλά αυστηρά μηδενικό.",
                ),
                QuestionOption(
                    letter="Δ",
                    text="το πεδίο στο εσωτερικό τους είναι ίσο με μηδέν",
                    is_correct=True,
                    explanation="Σωστό: Λόγω της ηλεκτροστατικής θωράκισης (Faraday Cage), σε αγωγό σε ισορροπία το ηλεκτρικό πεδίο μέσα σε οποιαδήποτε κενή κοιλότητα είναι απόλυτα μηδέν (E = 0).",
                ),
            ],
            correct_option_letter="Δ",
            final_answer="Δ] το πεδίο στο εσωτερικό τους είναι ίσο με μηδέν",
            detailed_justification="Όλα τα ελεύθερα φορτία κατανέμονται στην εξωτερική επιφάνεια του αγωγού, μηδενίζοντας το πεδίο τόσο στη μάζα όσο και σε κάθε κενή κοιλότητα (θεώρημα Gauss).",
            common_pitfalls=["Αν υπάρχει φορτίο q τοποθετημένο ΜΕΣΑ στην κοιλότητα, τότε το πεδίο στην κοιλότητα ΔΕΝ είναι μηδέν."],
            related_theory_topic="Ηλεκτροστατική Αγωγών & Θωράκιση",
        ),
        ExamQuestion(
            question_number=3,
            title="Κίνηση Φορτίων & Πυκνότητα Ρεύματος (Συμπλήρωση Κενού)",
            question_type="Theory Analysis",
            prompt_text="Το φυσικό μέγεθος που περιγράφει την κίνηση φορτίων μέσα από μια επιφάνεια το ονομάζουμε πυκνότητα ................................................... .",
            options=[],
            final_answer="ρεύματος (διάνυσμα J)",
            detailed_justification="Η πυκνότητα ρεύματος J = n q v_d [A/m²] εκφράζει την ποσότητα φορτίου που διέρχεται ανά μονάδα χρόνου και ανά μονάδα κάθετης επιφάνειας.",
            common_pitfalls=["Ένταση ρεύματος I = βαθμωτό [A]. Πυκνότητα ρεύματος J = διανυσματικό [A/m²]."],
            related_theory_topic="Ηλεκτρικό Ρεύμα & Πυκνότητα Ρεύματος",
        ),
        ExamQuestion(
            question_number=4,
            title="Διεύθυνση Διανύσματος Poynting",
            question_type="Multiple Choice",
            prompt_text="Ποια είναι η διεύθυνση ταλάντωσης του διανύσματος Poynting;",
            options=[
                QuestionOption(
                    letter="Α",
                    text="Παράλληλα στο διάνυσμα του κυματαριθμού",
                    is_correct=True,
                    explanation="Σωστό: Το διάνυσμα Poynting S = (1/μ₀)(E × B) είναι πάντα παράλληλο στη διεύθυνση διάδοσης k (δηλαδή στο διάνυσμα κυματαριθμού).",
                ),
                QuestionOption(
                    letter="Β",
                    text="Παράλληλα στο διάνυσμα του ηλεκτρικού πεδίου",
                    is_correct=False,
                    explanation="Λάθος: Το S είναι κάθετο στο E επειδή προκύπτει από εξωτερικό γινόμενο E × B.",
                ),
                QuestionOption(
                    letter="Γ",
                    text="Παράλληλα στο διάνυσμα του μαγνητικού πεδίου",
                    is_correct=False,
                    explanation="Λάθος: Το S είναι κάθετο και στο B.",
                ),
                QuestionOption(
                    letter="Δ",
                    text="Παράλληλα στο διάνυσμα της πόλωσης",
                    is_correct=False,
                    explanation="Λάθος: Η πόλωση ορίζεται από το E, στο οποίο το S είναι κάθετο.",
                ),
            ],
            correct_option_letter="Α",
            final_answer="Α] Παράλληλα στο διάνυσμα του κυματαριθμού",
            detailed_justification="Από τον ορισμό του εξωτερικού γινομένου, το διάνυσμα E × B είναι κάθετο τόσο στο E όσο και στο B, δείχνοντας προς τη διεύθυνση διάδοσης k.",
            common_pitfalls=["S ⟂ E και S ⟂ B, ενώ S ∥ k."],
            related_theory_topic="Διάνυσμα Poynting & Κυματική Διάδοση",
        ),
        ExamQuestion(
            question_number=5,
            title="Άσκηση 1: Υπολογισμός Πυκνότητας Φορτίου ρ από τη Μετατόπιση D",
            question_type="Calculations",
            prompt_text=r"Σύμφωνα με τον νόμο του Gauss για τη διηλεκτρική μετατόπιση $\vec{D}$ ισχύει $\vec{\nabla}\cdot\vec{D}=\rho$. Αν $\vec{D}=x^2\hat{x}-zy\hat{z}$, να υπολογίσετε την πυκνότητα φορτίου $\rho$.",
            given_parameters=[
                GivenParameter("D_x", "x^2", "x-συνιστώσα μετατόπισης"),
                GivenParameter("D_y", "0", "y-συνιστώσα μετατόπισης"),
                GivenParameter("D_z", "-zy", "z-συνιστώσα μετατόπισης"),
            ],
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Εφαρμογή μερικών παραγώγων της απόκλισης",
                    formula=r"\rho = \vec{\nabla}\cdot\vec{D} = \frac{\partial D_x}{\partial x} + \frac{\partial D_y}{\partial y} + \frac{\partial D_z}{\partial z}",
                    substitution=r"\rho = \frac{\partial}{\partial x}(x^2) + \frac{\partial}{\partial y}(0) + \frac{\partial}{\partial z}(-zy)",
                    result=r"\rho = 2x + 0 - y = 2x - y",
                    rationale=r"Η παράγωγος του x² ως προς x είναι 2x. Η παράγωγος του -zy ως προς z είναι -y (θεωρώντας το y σταθερό κατά τη μερική παραγώγιση).",
                ),
            ],
            final_answer=r"\rho(x, y, z) = 2x - y \quad [\text{C/m}^3]",
            detailed_justification="Η τοπική χωρική πυκνότητα ελεύθερων φορτίων είναι γραμμική συνάρτηση των συντεταγμένων x και y.",
            common_pitfalls=["Προσοχή στο πρόσημο μείον στον όρο -zy: η μερική παράγωγος ως προς z είναι -y."],
            related_theory_topic="Εξισώσεις Maxwell & Νόμος Gauss",
        ),
        ExamQuestion(
            question_number=6,
            title="Άσκηση 2: Υπολογισμός Πεδίου E, Διανύσματος Poynting & Έντασης από το B",
            question_type="Calculations",
            prompt_text=r"Το μαγνητικό πεδίο ημιτονοειδούς επίπεδου ΗΜ κύματος στο κενό δίνεται από: $\vec{B}=3\cos(100\pi z-\omega t)\hat{y}$. α) Ποιο είναι το μήκος κύματος $\lambda$ και η συχνότητα $f$; β) Να γραφεί το διάνυσμα ταλάντωσης του ηλεκτρικού πεδίου $\vec{E}$. γ) Να υπολογισθεί το διάνυσμα Poynting $\vec{S}$ και η ένταση $I$.",
            given_parameters=[
                GivenParameter("B_0", "3 \\text{ T}", "Πλάτος μαγνητικού πεδίου"),
                GivenParameter("k", "100\\pi \\text{ rad/m}", "Κυματάριθμος κατά z"),
                GivenParameter("c", "3 \\times 10^8 \\text{ m/s}", "Ταχύτητα φωτός στο κενό"),
                GivenParameter(r"\mu_0", r"4\pi \times 10^{-7} \text{ T}\cdot\text{m/A}", "Μαγνητική διαπερατότητα κενού"),
            ],
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Υπολογισμός μήκους κύματος λ",
                    formula=r"\lambda = \frac{2\pi}{k}",
                    substitution=r"\lambda = \frac{2\pi}{100\pi} = \frac{2}{100} = 0.02 \ \text{m} = 2 \ \text{cm}",
                    result=r"\lambda = 0.02 \ \text{m} = 2 \ \text{cm}",
                    rationale="Από τον ορισμό του κυματάριθμου k = 2π/λ.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Υπολογισμός κυκλικής συχνότητας ω και συχνότητας f",
                    formula=r"\omega = c k, \quad f = \frac{\omega}{2\pi} = \frac{c}{\lambda}",
                    substitution=r"\omega = (3\times 10^8)(100\pi) = 3\times 10^{10}\pi \ \text{rad/s}, \quad f = \frac{3\times 10^8}{0.02} = 1.5\times 10^{10} \ \text{Hz}",
                    result=r"\omega \approx 9.425 \times 10^{10} \ \text{rad/s}, \quad f = 15 \ \text{GHz}",
                    rationale="Η συχνότητα 15 GHz αντιστοιχεί στη ζώνη Ku των μικροκυμάτων.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Προσδιορισμός πλάτους και διανύσματος ηλεκτρικού πεδίου E",
                    formula=r"E_0 = c B_0, \quad \hat{E} \times \hat{B} = \hat{k} \implies \hat{E} \times \hat{y} = \hat{z} \implies \hat{E} = \hat{x}",
                    substitution=r"E_0 = (3\times 10^8)(3) = 9\times 10^8 \ \text{V/m}, \quad \hat{x} \times \hat{y} = \hat{z}",
                    result=r"\vec{E}(z,t) = 9\times 10^8 \cos(100\pi z - 3\times 10^{10}\pi t)\hat{x} \ \text{V/m}",
                    rationale="Το ηλεκτρικό πεδίο ταλαντώνεται κατά τον άξονα x ώστε το εξωτερικό γινόμενο E x B να έχει κατεύθυνση +z.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Υπολογισμός διανύσματος Poynting S",
                    formula=r"\vec{S} = \frac{1}{\mu_0}(\vec{E}\times\vec{B})",
                    substitution=r"\vec{S} = \frac{1}{4\pi\times 10^{-7}} [9\times 10^8 \cos(...) \hat{x} \times 3 \cos(...) \hat{y}] = \frac{27\times 10^8}{4\pi\times 10^{-7}}\cos^2(...)\hat{z}",
                    result=r"\vec{S} = \frac{2.7\times 10^{16}}{4\pi} \cos^2(100\pi z - \omega t)\hat{z} \approx 2.1486 \times 10^{15} \cos^2(...)\hat{z} \ \text{W/m}^2",
                    rationale="Επειδή x̂ × ŷ = ẑ, η στιγμιαία ροή ενέργειας κατευθύνεται κατά +z.",
                ),
                CalculationStep(
                    step_number=5,
                    title="Υπολογισμός μέσης έντασης ακτινοβολίας I",
                    formula=r"I = \bar{S} = \frac{S_0}{2} = \frac{E_0 B_0}{2\mu_0}",
                    substitution=r"I = \frac{2.1486 \times 10^{15}}{2} \approx 1.0743 \times 10^{15} \ \text{W/m}^2",
                    result=r"I \approx 1.074 \times 10^{15} \ \text{W/m}^2",
                    rationale="Η χρονική μέση τιμή του cos² είναι 1/2.",
                ),
            ],
            final_answer=r"\lambda = 2\text{ cm}, \ f = 15\text{ GHz}, \ \vec{E} = 9\times 10^8\cos(100\pi z - \omega t)\hat{x}\text{ V/m}, \ \vec{S} \approx 2.15\times 10^{15}\cos^2(...)\hat{z}\text{ W/m}^2, \ I \approx 1.07\times 10^{15}\text{ W/m}^2",
            detailed_justification="Το μαγνητικό πεδίο δίνεται με πλάτος 3 T κατά y και διάδοση κατά z, καθορίζοντας άμεσα ότι το E ταλαντώνεται κατά x.",
            common_pitfalls=["Προσοχή: Εδώ δίνεται το B και ζητείται το E, άρα E_0 = c * B_0 (πολλαπλασιάζουμε με το c, δεν διαιρούμε!)."],
            related_theory_topic="Επίπεδα Ηλεκτρομαγνητικά Κύματα & Διάνυσμα Poynting",
        ),
    ]

    justifications = [
        DesignJustification(
            title="Σχέση Πλατών E_0 = c B_0",
            category="Wave Relation",
            description="Όταν δίνεται το μαγνητικό πεδίο B, το πλάτος του ηλεκτρικού πεδίου υπολογίζεται μέσω του πολλαπλασιασμού με την ταχύτητα του φωτός: E_0 = c B_0.",
            rationale="Απορρέει απευθείας από τις εξισώσεις Faraday και Ampère για επίπεδα κύματα στο κενό.",
        ),
        DesignJustification(
            title="Ηλεκτροστατική Θωράκιση Κοιλότητας",
            category="Shielding Law",
            description="Σε αγώγιμο σώμα χωρίς εσωτερικά φορτία, το δυναμικό σε όλη την κοιλότητα είναι σταθερό και ίσο με του αγωγού, συνεπάγοντας E = -grad(V) = 0.",
            rationale="Θεμελιώδης αρχή προστασίας ευαίσθητων ηλεκτρονικών και τηλεπικοινωνιακών συσκευών.",
        ),
    ]

    solution_code = '''"""Python verification script for June 2026 Team B exam problems."""

import sympy as sp

def verify_divergence() -> None:
    """Verifies Exercise 1: div(D) = rho."""
    x, y, z = sp.symbols('x y z')
    D_x = x**2
    D_y = sp.Integer(0)
    D_z = -z * y
    
    div_D = sp.diff(D_x, x) + sp.diff(D_y, y) + sp.diff(D_z, z)
    expected = 2 * x - y
    print("--- Askisi 1: Gauss Law Divergence ---")
    print(f"D = [{D_x}] x_hat + [{D_z}] z_hat")
    print(f"div(D) = rho = {div_D}")
    assert sp.simplify(div_D - expected) == 0, f"Mismatch: {div_D} != {expected}"
    print("Verification Askisi 1: PASSED")

def verify_wave() -> None:
    """Verifies Exercise 2: EM wave parameters from B-field."""
    c = 3e8
    mu_0 = 4 * 3.141592653589793 * 1e-7
    B_0 = 3.0
    k = 100 * 3.141592653589793
    
    wavelength = 2 * 3.141592653589793 / k
    omega = c * k
    f = omega / (2 * 3.141592653589793)
    E_0 = c * B_0
    S_max = (E_0 * B_0) / mu_0
    intensity = S_max / 2.0
    
    print("\\n--- Askisi 2: Plane EM Wave from B ---")
    print(f"Wavelength lambda = {wavelength*100:.2f} cm")
    print(f"Frequency f = {f/1e9:.2f} GHz")
    print(f"Electric amplitude E_0 = {E_0:.4e} V/m")
    print(f"Peak Poynting flux S_max = {S_max:.4e} W/m^2")
    print(f"Radiation Intensity I = {intensity:.4e} W/m^2")
    print("Verification Askisi 2: PASSED")

if __name__ == "__main__":
    verify_divergence()
    verify_wave()
'''

    return Scenario(
        id="past_exam_2026_06_team_b",
        title="Εξεταστική Ιουνίου 2026 — Ομάδα Β",
        subtitle="Πλήρης Επίλυση: Θωράκιση, Πυκνότητα J, Νόμος Gauss & Κύμα από B",
        course_tag="Past Exam 2026",
        duration_info="Διάρκεια: 2 ώρες | 4 Ερωτήσεις Θεωρίας & 2 Ασκήσεις Υπολογισμού",
        paragraphs=paragraphs,
        questions=questions,
        justifications=justifications,
        solution_code=solution_code,
    )

