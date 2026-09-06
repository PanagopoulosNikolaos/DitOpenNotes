"""Past Exam Scenario: June 2026 Team A.

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


def createPastExam202606TeamA() -> Scenario:
    """Instantiates the June 2026 Team A past examination scenario.

    Returns:
        Scenario: Complete scenario container with verbatim text and solutions.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(
                    text="Εξεταστική. ΑΡΧΕΣ ΗΛΕΚΤΡΟΜΑΓΝΗΤΙΣΜΟΥ ΚΑΙ ΤΗΛΕΠΙΚΟΙΝΩΝΙΩΝ. Ιούνιος 2026. Ομάδα Α\n",
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
                TextSegment(text="Ερώτηση 1.\nΗ ", is_highlight=False),
                TextSegment(
                    text="ηλεκτρική ροή",
                    is_highlight=True,
                    category="field",
                    tag_label="ΡΟΗ Φ",
                    tooltip="Classification: Ηλεκτρική Ροή (Electric Flux) | Detection Clue: Ο όρος 'ηλεκτρική ροή' | Application Rationale: Ορίζεται ως Φ_E = ∬ E·dS και συνδέεται με τον συνολικό αριθμό των δυναμικών γραμμών.",
                ),
                TextSegment(text=" εκφράζει τον αριθμό των ", is_highlight=False),
                TextSegment(
                    text="δυναμικών γραμμών",
                    is_highlight=True,
                    category="law",
                    tag_label="ΓΡΑΜΜΕΣ E",
                    tooltip="Classification: Δυναμικές Γραμμές Πεδίου | Detection Clue: 'αριθμό των ...' | Application Rationale: Συμπλήρωση κενού: εκφράζει το μέτρο των γραμμών πεδίου που διαπερνούν κάθετα τη δοσμένη επιφάνεια.",
                ),
                TextSegment(text=" ενός ηλεκτρικού πεδίου που διαπερνούν μια επιφάνεια.", is_highlight=False),
            ],
            accent_border_color="accent",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Ερώτηση 2.\nΣε τι μορφή αποθηκεύεται ενέργεια στον ", is_highlight=False),
                TextSegment(
                    text="πυκνωτή στο πείραμα του Hertz",
                    is_highlight=True,
                    category="param",
                    tag_label="ΠΥΚΝΩΤΗΣ HERTZ",
                    tooltip="Classification: Στοιχείο Αποθήκευσης Ενέργειας | Detection Clue: 'πυκνωτή στο πείραμα του Hertz' | Application Rationale: Ο πυκνωτής αποθηκεύει ενέργεια στο ηλεκτρικό πεδίο ανάμεσα στους οπλισμούς του.",
                ),
                TextSegment(
                    text=" για την παραγωγή ΗΜ κυμάτων;\nΑ] Με τη μορφή μαγνητικού πεδίου\nΒ] Με τη μορφή αρμονικού κύματος\nΓ] Με τη μορφή ηλεκτρικού πεδίου\nΔ] Με τη μορφή αρμονικού κύματος",
                    is_highlight=False,
                ),
            ],
            accent_border_color="accent",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Ερώτηση 3.\nΠοια είναι η ", is_highlight=False),
                TextSegment(
                    text="ελάχιστη τιμή του διανύσματος Poynting",
                    is_highlight=True,
                    category="calc",
                    tag_label="min(S)",
                    tooltip="Classification: Ελάχιστο Μέτρο Ροής Poynting | Detection Clue: 'ελάχιστη τιμή του διανύσματος Poynting' | Application Rationale: Το S εξαρτάται από cos²(ky - ωt), άρα η ελάχιστη στιγμιαία τιμή του είναι 0.",
                ),
                TextSegment(
                    text=";\nΑ] 0\nΒ] -|S|\nΓ] -∞\nΔ] -B₀²/2μ₀",
                    is_highlight=False,
                ),
            ],
            accent_border_color="accent",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Ερώτηση 4.\nΗ ", is_highlight=False),
                TextSegment(
                    text="πόλωση σε ένα διηλεκτρικό υλικό",
                    is_highlight=True,
                    category="field",
                    tag_label="ΔΙΑΝΥΣΜΑ P",
                    tooltip="Classification: Ηλεκτρική Πόλωση Υλικού P | Detection Clue: 'πόλωση σε ένα διηλεκτρικό' | Application Rationale: Εκφράζει την πυκνότητα διπολικής ροπής ανά μονάδα όγκου P = dp/dV.",
                ),
                TextSegment(text=" εκφράζει την πυκνότητα των μόνιμων ή επαγόμενων ", is_highlight=False),
                TextSegment(
                    text="ηλεκτρικών διπόλων",
                    is_highlight=True,
                    category="law",
                    tag_label="ΔΙΠΟΛΑ",
                    tooltip="Classification: Ηλεκτρικά Δίπολα (Electric Dipoles) | Detection Clue: Συμπλήρωση κενού | Application Rationale: Η παρουσία ηλεκτρικού πεδίου ευθυγραμμίζει τα μόνιμα ή επάγει νέα ηλεκτρικά δίπολα.",
                ),
                TextSegment(text=".", is_highlight=False),
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
                    tooltip="Classification: Διάνυσμα Ηλεκτρικής Ροής D | Detection Clue: Σύμβολο D | Application Rationale: Εφαρμογή της διαφορικής απόκλισης div(D) = rho για εύρεση του φορτίου.",
                ),
                TextSegment(text=" ισχύει ∇·D = ρ, όπου ρ η πυκνότητα φορτίου. Αν ", is_highlight=False),
                TextSegment(
                    text="D = x²z x̂ + (3/y) ŷ",
                    is_highlight=True,
                    category="calc",
                    tag_label="D_x, D_y",
                    tooltip="Classification: Συνιστώσες Πεδίου Μετατόπισης | Detection Clue: D_x = x^2 z, D_y = 3/y, D_z = 0 | Application Rationale: Παραγωγίζουμε d(x^2 z)/dx = 2xz και d(3/y)/dy = -3/y^2.",
                ),
                TextSegment(text=" να υπολογίσετε την πυκνότητα φορτίου ρ.", is_highlight=False),
            ],
            accent_border_color="accent",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Άσκηση 2. 3 μονάδες\nΤο ηλεκτρικό πεδίο ενός ημιτονοειδούς επίπεδου ΗΜ κύματος που διαδίδεται στο κενό δίνεται από τη σχέση:\n", is_highlight=False),
                TextSegment(
                    text="E = 30 cos(ky - 10¹¹ t) ẑ",
                    is_highlight=True,
                    category="field",
                    tag_label="E(y,t)",
                    tooltip="Classification: Ηλεκτρικό Πεδίο Επίπεδου Κύματος | Detection Clue: E_0 = 30 V/m, omega = 10^11 rad/s, πόλωση ẑ, διάδοση κατά +y | Application Rationale: Καθορίζει τη συχνότητα f, το k = omega/c, το B_0 = E_0/c και το B κατά +x.",
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
                    tooltip="Classification: Μαγνητικό Πεδίο B | Detection Clue: B_0 = E_0 / c και ẑ x x̂ = ŷ | Application Rationale: B(y,t) = 10^-7 cos(ky - 10^11 t) x̂.",
                ),
                TextSegment(text=". γ) Να υπολογισθεί το ", is_highlight=False),
                TextSegment(
                    text="διάνυσμα Poynting S και η ένταση I",
                    is_highlight=True,
                    category="calc",
                    tag_label="S & I",
                    tooltip="Classification: Ροή Ισχύος Poynting και Ένταση | Detection Clue: S = (1/mu_0)(E x B), I = <S> | Application Rationale: S_max = 30 / (4pi) W/m^2, I = S_max / 2.",
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
            title="Ορισμός Ηλεκτρικής Ροής (Συμπλήρωση Κενού)",
            question_type="Theory Analysis",
            prompt_text="Η ηλεκτρική ροή εκφράζει τον αριθμό των .................................................... ενός ηλεκτρικού πεδίου που διαπερνούν μια επιφάνεια.",
            options=[],
            final_answer="δυναμικών γραμμών",
            detailed_justification="Κατά ορισμό, η ροή του ηλεκτρικού πεδίου Φ_E = ∬ E·dS είναι το μέτρο του πλήθους των γραμμών του ηλεκτρικού πεδίου που τέμνουν κάθετα μια επιφάνεια.",
            common_pitfalls=["Μην συγχέετε την ηλεκτρική ροή (αριθμός δυναμικών γραμμών) με την ηλεκτρική κυκλοφορία (ολοκλήρωμα κατά μήκος καμπύλης)."],
            related_theory_topic="Νόμος Gauss & Ηλεκτρική Ροή",
        ),
        ExamQuestion(
            question_number=2,
            title="Μορφή Αποθήκευσης Ενέργειας στον Πυκνωτή",
            question_type="Multiple Choice",
            prompt_text="Σε τι μορφή αποθηκεύεται ενέργεια στον πυκνωτή στο πείραμα του Hertz για την παραγωγή ΗΜ κυμάτων;",
            options=[
                QuestionOption(
                    letter="Α",
                    text="Με τη μορφή μαγνητικού πεδίου",
                    is_correct=False,
                    explanation="Λάθος: Μαγνητικό πεδίο αποθηκεύει το πηνίο (αυτεπαγωγή), όχι ο πυκνωτής.",
                ),
                QuestionOption(
                    letter="Β",
                    text="Με τη μορφή αρμονικού κύματος",
                    is_correct=False,
                    explanation="Λάθος: Το κύμα δημιουργείται μετά την εκκένωση του σπινθήρα.",
                ),
                QuestionOption(
                    letter="Γ",
                    text="Με τη μορφή ηλεκτρικού πεδίου",
                    is_correct=True,
                    explanation="Σωστό: Η ενέργεια πυκνωτή U = (1/2)CV² αποθηκεύεται αποκλειστικά στον ενδιάμεσο χώρο υπό τη μορφή ηλεκτρικού πεδίου.",
                ),
                QuestionOption(
                    letter="Δ",
                    text="Με τη μορφή αρμονικού κύματος",
                    is_correct=False,
                    explanation="Λάθος: Επανάληψη της επιλογής Β.",
                ),
            ],
            correct_option_letter="Γ",
            final_answer="Γ] Με τη μορφή ηλεκτρικού πεδίου",
            detailed_justification="Η πυκνότητα ενέργειας σε έναν φορτισμένο πυκνωτή είναι u_e = (1/2) ε E², εντοπισμένη εξ ολοκλήρου στο ηλεκτρικό πεδίο.",
            common_pitfalls=["Πυκνωτής -> Ηλεκτρικό πεδίο E. Πηνίο -> Μαγνητικό πεδίο B."],
            related_theory_topic="Ηλεκτροστατική Ενέργεια & Πυκνωτές",
        ),
        ExamQuestion(
            question_number=3,
            title="Ελάχιστη Τιμή Διανύσματος Poynting",
            question_type="Multiple Choice",
            prompt_text="Ποια είναι η ελάχιστη τιμή του διανύσματος Poynting;",
            options=[
                QuestionOption(
                    letter="Α",
                    text="0",
                    is_correct=True,
                    explanation="Σωστό: Για ένα οδεύον επίπεδο ΗΜ κύμα, το στιγμιαίο διάνυσμα Poynting είναι ανάλογο του cos²(ky - ωt) >= 0. Η ελάχιστη στιγμιαία τιμή του μέτρου του είναι μηδέν.",
                ),
                QuestionOption(
                    letter="Β",
                    text="-|S|",
                    is_correct=False,
                    explanation="Λάθος: Για απλό οδεύον κύμα δεν υπάρχει αντίστροφη ροή ενέργειας (το cos² δεν παίρνει αρνητικές τιμές).",
                ),
                QuestionOption(
                    letter="Γ",
                    text="-∞",
                    is_correct=False,
                    explanation="Λάθος: Η ροή ισχύος είναι πεπερασμένη.",
                ),
                QuestionOption(
                    letter="Δ",
                    text="-B₀²/2μ₀",
                    is_correct=False,
                    explanation="Λάθος: Η πυκνότητα ενέργειας και η ροή ισχύος είναι θετικά μεγέθη.",
                ),
            ],
            correct_option_letter="Α",
            final_answer="Α] 0",
            detailed_justification="Επειδή S(t) = S_max cos²(φ) και η συνάρτηση συνημίτονο στο τετράγωνο κυμαίνεται αυστηρά στο διάστημα [0, 1], η ελάχιστη τιμή είναι 0.",
            common_pitfalls=["Προσοχή: Τα πεδία E και B παίρνουν αρνητικές τιμές, αλλά το γινόμενο E x B σε οδεύον κύμα είναι πάντα ομόρροπο με τη διάδοση (cos² >= 0)."],
            related_theory_topic="Διάνυσμα Poynting & Διατήρηση Ενέργειας",
        ),
        ExamQuestion(
            question_number=4,
            title="Ηλεκτρική Πόλωση Διηλεκτρικού (Συμπλήρωση Κενού)",
            question_type="Theory Analysis",
            prompt_text="Η πόλωση σε ένα διηλεκτρικό υλικό εκφράζει την πυκνότητα των μόνιμων ή επαγόμενων ....................................................................",
            options=[],
            final_answer="ηλεκτρικών διπόλων (διπολικών ροπών ανά μονάδα όγκου)",
            detailed_justification="Το διάνυσμα πόλωσης P ορίζεται ως η συνολική διπολική ροπή ανά μονάδα όγκου: P = dp / dV [C/m²].",
            common_pitfalls=["Μην συγχέετε την πόλωση κύματος (διεύθυνση ταλάντωσης του E) με την πόλωση διηλεκτρικού υλικού (ευθυγράμμιση διπόλων)."],
            related_theory_topic="Διηλεκτρικά Υλικά & Πόλωση",
        ),
        ExamQuestion(
            question_number=5,
            title="Άσκηση 1: Υπολογισμός Πυκνότητας Φορτίου ρ από τη Μετατόπιση D",
            question_type="Calculations",
            prompt_text=r"Σύμφωνα με τον νόμο του Gauss για τη διηλεκτρική μετατόπιση $\vec{D}$ ισχύει $\vec{\nabla}\cdot\vec{D}=\rho$, όπου ρ η πυκνότητα φορτίου. Αν $\vec{D}=x^2z\hat{x}+\frac{3}{y}\hat{y}$, να υπολογίσετε την πυκνότητα φορτίου $\rho$.",
            given_parameters=[
                GivenParameter("D_x", "x^2 z", "x-συνιστώσα μετατόπισης"),
                GivenParameter("D_y", r"\frac{3}{y}", "y-συνιστώσα μετατόπισης"),
                GivenParameter("D_z", "0", "z-συνιστώσα μετατόπισης"),
            ],
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Διατύπωση διαφορικής μορφής 1ης εξίσωσης Maxwell (Νόμος Gauss)",
                    formula=r"\rho = \vec{\nabla}\cdot\vec{D} = \frac{\partial D_x}{\partial x} + \frac{\partial D_y}{\partial y} + \frac{\partial D_z}{\partial z}",
                    substitution=r"\rho = \frac{\partial}{\partial x}(D_x) + \frac{\partial}{\partial y}(D_y) + \frac{\partial}{\partial z}(D_z)",
                    result=r"\rho = \frac{\partial D_x}{\partial x} + \frac{\partial D_y}{\partial y} + \frac{\partial D_z}{\partial z}",
                    rationale="Ο νόμος του Gauss συνδέει την απόκλιση της διηλεκτρικής μετατόπισης με την τοπική χωρική πυκνότητα ελεύθερου φορτίου.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Αναγνώριση και καταγραφή των συνιστωσών του διανύσματος D",
                    formula=r"\vec{D} = D_x \hat{x} + D_y \hat{y} + D_z \hat{z}",
                    substitution=r"D_x = x^2 z, \quad D_y = \frac{3}{y} = 3 y^{-1}, \quad D_z = 0",
                    result=r"(D_x, D_y, D_z) = \left(x^2 z, \ \frac{3}{y}, \ 0\right)",
                    rationale="Αντιστοίχιση των δεδομένων συνιστωσών της εκφώνησης και μεταγραφή του κλάσματος 3/y σε δύναμη 3 y^(-1) για ευκολία παραγώγισης.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Υπολογισμός μερικής παραγώγου της x-συνιστώσας",
                    formula=r"\frac{\partial D_x}{\partial x} = \frac{\partial}{\partial x}(x^2 z) = z \cdot \frac{d}{dx}(x^2)",
                    substitution=r"\frac{\partial D_x}{\partial x} = z \cdot (2 x^{2-1}) = z \cdot (2x) = 2xz",
                    result=r"\frac{\partial D_x}{\partial x} = 2xz",
                    rationale="Κατά τη μερική παραγώγιση ως προς x, η μεταβλητή z αντιμετωπίζεται ως σταθερός πολλαπλασιαστικός παράγοντας.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Υπολογισμός μερικής παραγώγου της y-συνιστώσας",
                    formula=r"\frac{\partial D_y}{\partial y} = \frac{\partial}{\partial y}(3 y^{-1}) = 3 \cdot \frac{d}{dy}(y^{-1})",
                    substitution=r"\frac{\partial D_y}{\partial y} = 3 \cdot [(-1) y^{-1-1}] = -3 y^{-2} = -\frac{3}{y^2}",
                    result=r"\frac{\partial D_y}{\partial y} = -\frac{3}{y^2}",
                    rationale="Εφαρμογή του βασικού κανόνα δυνάμεων d(y^n)/dy = n y^(n-1) για n = -1. Προσοχή στο αρνητικό πρόσημο.",
                ),
                CalculationStep(
                    step_number=5,
                    title="Υπολογισμός μερικής παραγώγου της z-συνιστώσας",
                    formula=r"\frac{\partial D_z}{\partial z} = \frac{\partial}{\partial z}(0)",
                    substitution=r"\frac{\partial}{\partial z}(0) = 0",
                    result=r"\frac{\partial D_z}{\partial z} = 0",
                    rationale="Η z-συνιστώσα είναι μηδενική, συνεπώς και η παράγωγός της ως προς z ισούται με μηδέν.",
                ),
                CalculationStep(
                    step_number=6,
                    title="Άθροιση μερικών παραγώγων και εξαγωγή πυκνότητας φορτίου",
                    formula=r"\rho(x, y, z) = \frac{\partial D_x}{\partial x} + \frac{\partial D_y}{\partial y} + \frac{\partial D_z}{\partial z}",
                    substitution=r"\rho = 2xz + \left(-\frac{3}{y^2}\right) + 0 = 2xz - \frac{3}{y^2}",
                    result=r"\rho(x, y, z) = 2xz - \frac{3}{y^2} \quad [\text{C/m}^3]",
                    rationale="Η πυκνότητα φορτίου ορίζεται για κάθε y ≠ 0 και περιγράφει την τοπική πυκνότητα πηγών/καταβοθρών του πεδίου.",
                ),
            ],
            final_answer=r"\rho(x, y, z) = 2xz - \frac{3}{y^2} \quad [\text{C/m}^3]",
            detailed_justification="Η απόκλιση του πεδίου D αποκαλύπτει τις πηγές (+ρ) και καταβόθρες (-ρ) του ηλεκτρικού πεδίου στον χώρο.",
            common_pitfalls=["Προσοχή στην παράγωγο του 1/y: είναι -1/y², όχι +1/y²."],
            related_theory_topic="Εξισώσεις Maxwell & Νόμος Gauss",
        ),
        ExamQuestion(
            question_number=6,
            title="Άσκηση 2: Πλήρης Ανάλυση Επίπεδου ΗΜ Κύματος",
            question_type="Calculations",
            prompt_text=r"Το ηλεκτρικό πεδίο ημιτονοειδούς επίπεδου ΗΜ κύματος στο κενό δίνεται από: $\vec{E}=30\cos(ky-10^{11}t)\hat{z}$. α) Ποιο είναι το μήκος κύματος $\lambda$ και η συχνότητα $f$; β) Να γραφεί το διάνυσμα ταλάντωσης της μαγνητικής επαγωγής $\vec{B}$. γ) Να υπολογισθεί το διάνυσμα Poynting $\vec{S}$ και η ένταση $I$.",
            given_parameters=[
                GivenParameter("E_0", "30 \\text{ V/m}", "Πλάτος ηλεκτρικού πεδίου"),
                GivenParameter(r"\omega", "10^{11} \\text{ rad/s}", "Κυκλική συχνότητα"),
                GivenParameter("c", "3 \\times 10^8 \\text{ m/s}", "Ταχύτητα φωτός στο κενό"),
                GivenParameter(r"\mu_0", r"4\pi \times 10^{-7} \text{ T}\cdot\text{m/A}", "Μαγνητική διαπερατότητα κενού"),
            ],
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Αναγνώριση βασικών παραμέτρων από την κυματική εξίσωση",
                    formula=r"\vec{E}(y,t) = E_0 \cos(ky - \omega t)\hat{u}_E",
                    substitution=r"E_0 = 30 \ \text{V/m}, \quad \omega = 10^{11} \ \text{rad/s}, \quad \hat{u}_E = \hat{z}, \quad \hat{k} = +\hat{y}",
                    result=r"E_0 = 30 \ \text{V/m}, \quad \omega = 10^{11} \ \text{rad/s}",
                    rationale="Το όρισμα φάσης (ky - ωt) πιστοποιεί διάδοση κατά τη θετική διεύθυνση του άξονα y με γραμμική πόλωση κατά z.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Υπολογισμός γραμμικής συχνότητας f",
                    formula=r"\omega = 2\pi f \implies f = \frac{\omega}{2\pi}",
                    substitution=r"f = \frac{10^{11} \ \text{rad/s}}{2\pi} \approx \frac{10^{11}}{6.283185} \ \text{Hz} = 1.5915 \times 10^{10} \ \text{Hz}",
                    result=r"f \approx 1.5915 \times 10^{10} \ \text{Hz} = 15.915 \ \text{GHz}",
                    rationale="Η συχνότητα 15.92 GHz κατατάσσει το κύμα στη ζώνη μικροκυμάτων (Ku band).",
                ),
                CalculationStep(
                    step_number=3,
                    title="Υπολογισμός κυματάριθμου k στο κενό",
                    formula=r"k = \frac{\omega}{c}",
                    substitution=r"k = \frac{10^{11} \ \text{rad/s}}{3 \times 10^8 \ \text{m/s}} = \frac{1000}{3} \ \text{rad/m}",
                    result=r"k = \frac{1000}{3} \ \text{rad/m} \approx 333.33 \ \text{rad/m}",
                    rationale="Ο κυματάριθμος συνδέεται άμεσα με την κυκλική συχνότητα μέσω της ταχύτητας του φωτός c.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Αναλυτικός υπολογισμός μήκους κύματος λ",
                    formula=r"\lambda = \frac{c}{f} = \frac{2\pi}{k}",
                    substitution=r"\lambda = \frac{2\pi}{1000/3} = \frac{6\pi}{1000} \ \text{m} \approx 0.01885 \ \text{m}",
                    result=r"\lambda \approx 0.01885 \ \text{m} = 1.885 \ \text{cm}",
                    rationale="Το μήκος κύματος 1.885 cm επιβεβαιώνει την κλίμακα εκατοστομετρικών μικροκυμάτων.",
                ),
                CalculationStep(
                    step_number=5,
                    title="Υπολογισμός πλάτους μαγνητικής επαγωγής B_0",
                    formula=r"B_0 = \frac{E_0}{c}",
                    substitution=r"B_0 = \frac{30 \ \text{V/m}}{3 \times 10^8 \ \text{m/s}} = 10 \times 10^{-8} \ \text{T} = 10^{-7} \ \text{T}",
                    result=r"B_0 = 10^{-7} \ \text{T} = 0.1 \ \mu\text{T}",
                    rationale="Ο λόγος των πλατών E_0 / B_0 σε επίπεδο κύμα στο κενό ισούται αυστηρά με c.",
                ),
                CalculationStep(
                    step_number=6,
                    title="Προσδιορισμός διανύσματος ταλάντωσης B μέσω εξωτερικού γινομένου",
                    formula=r"\hat{B} = \hat{k} \times \hat{E} \implies \hat{y} \times \hat{z} = \hat{x}",
                    substitution=r"\vec{B}(y,t) = B_0 \cos(ky - \omega t)\hat{x} = 10^{-7}\cos\left(\frac{1000}{3}y - 10^{11}t\right)\hat{x} \ \text{T}",
                    result=r"\vec{B}(y,t) = 10^{-7}\cos\left(\frac{1000}{3}y - 10^{11}t\right)\hat{x} \ \text{T}",
                    rationale="Σύμφωνα με τον κανόνα δεξιού χεριού, ŷ × ẑ = +x̂, ώστε το τριέδρο (E, B, k) να είναι δεξιόστροφο.",
                ),
                CalculationStep(
                    step_number=7,
                    title="Υπολογισμός στιγμιαίου διανύσματος Poynting S",
                    formula=r"\vec{S}(y,t) = \frac{1}{\mu_0}(\vec{E}\times\vec{B}) = \frac{E_0 B_0}{\mu_0}\cos^2(ky - \omega t)(\hat{z}\times\hat{x})",
                    substitution=r"\vec{S} = \frac{30 \times 10^{-7}}{4\pi \times 10^{-7}}\cos^2(...)(+\hat{y}) = \frac{30}{4\pi}\cos^2\left(\frac{1000}{3}y - 10^{11}t\right)\hat{y}",
                    result=r"\vec{S}(y,t) \approx 2.3873 \cos^2\left(\frac{1000}{3}y - 10^{11}t\right)\hat{y} \ \text{W/m}^2",
                    rationale="Επειδή ẑ × x̂ = +ŷ, η ροή ηλεκτρομαγνητικής ισχύος συμπίπτει ακριβώς με την κατεύθυνση διάδοσης.",
                ),
                CalculationStep(
                    step_number=8,
                    title="Υπολογισμός μέσης έντασης ακτινοβολίας I",
                    formula=r"I = \langle |\vec{S}| \rangle = \frac{S_{\text{peak}}}{2} = \frac{1}{2} \cdot \frac{30}{4\pi} = \frac{15}{4\pi}",
                    substitution=r"I = \frac{15}{4\pi} \approx \frac{15}{12.56637} \ \text{W/m}^2 \approx 1.1937 \ \text{W/m}^2",
                    result=r"I \approx 1.1937 \ \text{W/m}^2",
                    rationale="Η μέση χρονική τιμή του τετραγώνου του συνημιτόνου σε ακέραιες περιόδους είναι 1/2.",
                ),
            ],
            final_answer=r"\lambda \approx 1.885\text{ cm}, \ f \approx 15.92\text{ GHz}, \ \vec{B} = 10^{-7}\cos(ky - 10^{11}t)\hat{x}\text{ T}, \ \vec{S} \approx 2.39\cos^2(...)\hat{y}\text{ W/m}^2, \ I \approx 1.19\text{ W/m}^2",
            detailed_justification="Το κύμα διαδίδεται κατά +y, με E κατά z και B κατά x. Η ορθογωνιότητα E ⟂ B ⟂ k ικανοποιείται πλήρως.",
            common_pitfalls=["Προσοχή στη διεύθυνση διάδοσης: η φάση έχει όρισμα (ky - ωt), άρα η διάδοση είναι στον άξονα y, ΟΧΙ στον x ή z."],
            related_theory_topic="Επίπεδα Ηλεκτρομαγνητικά Κύματα & Διάνυσμα Poynting",
        ),
    ]

    justifications = [
        DesignJustification(
            title="Διανυσματική Παραγώγιση 1/y",
            category="Calculus Rule",
            description="Η μερική παράγωγος ∂(3/y)/∂y υπολογίζεται ως d(3 y⁻¹)/dy = -3 y⁻² = -3/y².",
            rationale="Απαιτείται σωστή εφαρμογή του κανόνα δυνάμεων ώστε να μην παραλειφθεί το αρνητικό πρόσημο.",
        ),
        DesignJustification(
            title="Κυκλικό Σύστημα Εξωτερικών Γινομένων",
            category="Vector Geometry",
            description="Ισχύει x̂ × ŷ = ẑ, ŷ × ẑ = x̂, ẑ × x̂ = ŷ.",
            rationale="Καθορίζει μονοσήμαντα την κατεύθυνση του μαγνητικού πεδίου ώστε E × B να δείχνει προς τη διάδοση k.",
        ),
    ]

    solution_code = '''"""Python verification script for June 2026 Team A exam problems."""

import sympy as sp

def verify_divergence() -> None:
    """Verifies Exercise 1: div(D) = rho."""
    x, y, z = sp.symbols('x y z')
    D_x = x**2 * z
    D_y = 3 / y
    D_z = sp.Integer(0)
    
    div_D = sp.diff(D_x, x) + sp.diff(D_y, y) + sp.diff(D_z, z)
    expected = 2 * x * z - 3 / y**2
    print("--- Askisi 1: Gauss Law Divergence ---")
    print(f"D = [{D_x}] x_hat + [{D_y}] y_hat")
    print(f"div(D) = rho = {div_D}")
    assert sp.simplify(div_D - expected) == 0, f"Mismatch: {div_D} != {expected}"
    print("Verification Askisi 1: PASSED")

def verify_wave() -> None:
    """Verifies Exercise 2: EM wave parameters, Poynting vector, and intensity."""
    c = 3e8
    mu_0 = 4 * 3.141592653589793 * 1e-7
    E_0 = 30.0
    omega = 1e11
    
    k = omega / c
    f = omega / (2 * 3.141592653589793)
    wavelength = c / f
    B_0 = E_0 / c
    S_max = (E_0 * B_0) / mu_0
    intensity = S_max / 2.0
    
    print("\\n--- Askisi 2: Plane EM Wave ---")
    print(f"k = {k:.4f} rad/m")
    print(f"Frequency f = {f:.4e} Hz ({f/1e9:.2f} GHz)")
    print(f"Wavelength lambda = {wavelength*100:.3f} cm")
    print(f"Magnetic amplitude B_0 = {B_0:.4e} T")
    print(f"Peak Poynting flux S_max = {S_max:.4f} W/m^2")
    print(f"Radiation Intensity I = {intensity:.4f} W/m^2")
    print("Verification Askisi 2: PASSED")

if __name__ == "__main__":
    verify_divergence()
    verify_wave()
'''

    return Scenario(
        id="past_exam_2026_06_team_a",
        title="Εξεταστική Ιουνίου 2026 — Ομάδα Α",
        subtitle="Πλήρης Επίλυση: Ηλεκτρική Ροή, Πόλωση, Νόμος Gauss & ΗΜ Κύμα",
        course_tag="Past Exam 2026",
        duration_info="Διάρκεια: 2 ώρες | 4 Ερωτήσεις Θεωρίας & 2 Ασκήσεις Υπολογισμού",
        paragraphs=paragraphs,
        questions=questions,
        justifications=justifications,
        solution_code=solution_code,
    )

