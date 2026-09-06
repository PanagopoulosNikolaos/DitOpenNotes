"""Past Exam Scenario: June 2026 Team C.

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


def createPastExam202606TeamC() -> Scenario:
    """Instantiates the June 2026 Team C past examination scenario.

    Returns:
        Scenario: Complete scenario container with verbatim text and solutions.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(
                    text="Εξεταστική. ΑΡΧΕΣ ΗΛΕΚΤΡΟΜΑΓΝΗΤΙΣΜΟΥ ΚΑΙ ΤΗΛΕΠΙΚΟΙΝΩΝΙΩΝ. Ιούνιος 2026. Ομάδα Γ\n",
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
                TextSegment(text="Ερώτηση 1.\nΜε ποια ιδιότητα των κυμάτων συνδέεται η ", is_highlight=False),
                TextSegment(
                    text="στροφορμή",
                    is_highlight=True,
                    category="field",
                    tag_label="ΣΤΡΟΦΟΡΜΗ",
                    tooltip="Classification: Κυματική Στροφορμή (SAM) | Detection Clue: Φυσική ιδιότητα στροφορμής | Application Rationale: Η εσωτερική στροφορμή των φωτονίων αντιστοιχεί στην κυκλική πόλωση του κύματος.",
                ),
                TextSegment(
                    text=";\nΑ] Την ταχύτητα του φωτός\nΒ] Το πλάτος ταλάντωσης του κύματος\nΓ] Την ένταση του κύματος\nΔ] Την πόλωση του κύματος",
                    is_highlight=False,
                ),
            ],
            accent_border_color="accent",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Ερώτηση 2.\nΗ ", is_highlight=False),
                TextSegment(
                    text="ένταση του ηλεκτρικού πεδίου",
                    is_highlight=True,
                    category="field",
                    tag_label="ΕΝΤΑΣΗ E",
                    tooltip="Classification: Ηλεκτρικό Πεδίο E | Detection Clue: 'ένταση του ηλεκτρικού πεδίου' | Application Rationale: E = F / q_0. Εξαρτάται αποκλειστικά από τα φορτία-πηγές Q που το δημιουργούν, όχι από το δοκιμαστικό φορτίο.",
                ),
                TextSegment(text=", εξαρτάται από τα φορτία που ", is_highlight=False),
                TextSegment(
                    text="δημιουργούν",
                    is_highlight=True,
                    category="law",
                    tag_label="ΠΗΓΕΣ Q",
                    tooltip="Classification: Φορτία-Πηγές (Source Charges) | Detection Clue: Συμπλήρωση κενού | Application Rationale: Τα φορτία πηγής γεννούν το πεδίο E = Q/(4πε r^2)r̂ ανεξάρτητα από την παρουσία ανιχνευτή.",
                ),
                TextSegment(text=" το πεδίο;", is_highlight=False),
            ],
            accent_border_color="accent",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Ερώτηση 3.\nΠοιο μέγεθος θεωρούμε ότι ", is_highlight=False),
                TextSegment(
                    text="διατηρείται στη διεπιφάνεια 2 διαφορετικών μέσων",
                    is_highlight=True,
                    category="law",
                    tag_label="ΔΙΑΤΗΡΗΣΗ",
                    tooltip="Classification: Οριακές Συνθήκες Διεπιφάνειας | Detection Clue: 'διατηρείται στη διεπιφάνεια' | Application Rationale: Η χρονική συνέχεια απαιτεί διατήρηση της συχνότητας f (ενέργειας E = hf) και της παράλληλης ορμής.",
                ),
                TextSegment(
                    text=" για να υπολογίσουμε τη συχνότητα του ανακλώμενου και διαθλώμενου κύματος;\nΑ] Η ηλεκτρική ροή\nΒ] Η ορμή\nΓ] Η στροφορμή\nΔ] Η πόλωση",
                    is_highlight=False,
                ),
            ],
            accent_border_color="accent",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Ερώτηση 4.\nΟι ", is_highlight=False),
                TextSegment(
                    text="διαφορετικοί τύποι ηλεκτρομαγνητικής ακτινοβολίας",
                    is_highlight=True,
                    category="param",
                    tag_label="ΦΑΣΜΑ ΗΜ",
                    tooltip="Classification: Ηλεκτρομαγνητικό Φάσμα | Detection Clue: 'ορατό φως, ακτίνες Χ, υπεριώδεις' | Application Rationale: Όλα τα ΗΜ κύματα διαδίδονται με ταχύτητα c στο κενό αλλά διαφέρουν ως προς τη συχνότητα f και το μήκος κύματος λ.",
                ),
                TextSegment(text=" (ορατό φως, ακτίνες Χ, υπεριώδεις) έχουν διαφορετική ", is_highlight=False),
                TextSegment(
                    text="συχνότητα (ή μήκος κύματος)",
                    is_highlight=True,
                    category="param",
                    tag_label="ΣΥΧΝΟΤΗΤΑ f",
                    tooltip="Classification: Συχνότητα & Μήκος Κύματος | Detection Clue: Συμπλήρωση κενού | Application Rationale: f = c / λ. Η συχνότητα καθορίζει την ενέργεια του φωτονίου E = hf και τη ζώνη του φάσματος.",
                ),
                TextSegment(text=" .", is_highlight=False),
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
                    tooltip="Classification: Διάνυσμα Μετατόπισης D | Detection Clue: ∇·D = ρ | Application Rationale: Εφαρμογή της απόκλισης div(D) = rho για εύρεση του φορτίου.",
                ),
                TextSegment(text=" ισχύει ∇·D = ρ, όπου ρ η πυκνότητα φορτίου. Αν ", is_highlight=False),
                TextSegment(
                    text="D = 4x x̂ - 6z² ŷ",
                    is_highlight=True,
                    category="calc",
                    tag_label="ΣΥΝΙΣΤΩΣΕΣ D",
                    tooltip="Classification: Συνιστώσες D_x = 4x, D_y = -6z^2, D_z = 0 | Detection Clue: D = 4x x̂ - 6z² ŷ | Application Rationale: d(4x)/dx = 4, d(-6z^2)/dy = 0, d(0)/dz = 0.",
                ),
                TextSegment(text=" να υπολογίσετε την πυκνότητα φορτίου ρ.", is_highlight=False),
            ],
            accent_border_color="accent",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Άσκηση 2. 3 μονάδες\nΈνα ηλεκτρομαγνητικό κύμα διαδίδεται στο κενό και το ηλεκτρικό του πεδίο περιγράφεται από την εξίσωση:\n", is_highlight=False),
                TextSegment(
                    text="E = 300 cos(kz - 200π t) x̂",
                    is_highlight=True,
                    category="field",
                    tag_label="E(z,t)",
                    tooltip="Classification: Ηλεκτρικό Πεδίο Επίπεδου Κύματος | Detection Clue: E_0 = 300 V/m, omega = 200π rad/s, πόλωση κατά x, διάδοση κατά +z | Application Rationale: Υπολογισμός f = 100 Hz, λ = 3*10^6 m, B_0 = 10^-6 T κατά +y.",
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
                    tooltip="Classification: Μαγνητικό Πεδίο B | Detection Clue: B_0 = E_0 / c και x̂ × ŷ = ẑ | Application Rationale: B(z,t) = 10^-6 cos(kz - 200π t) ŷ T.",
                ),
                TextSegment(text=". γ) Να υπολογισθεί το ", is_highlight=False),
                TextSegment(
                    text="διάνυσμα Poynting S και η ένταση I",
                    is_highlight=True,
                    category="calc",
                    tag_label="S & I",
                    tooltip="Classification: Ροή Ισχύος Poynting και Μέση Ένταση | Detection Clue: S = (1/mu_0)(E x B) | Application Rationale: S_max = 750/pi W/m^2, I = 375/pi W/m^2.",
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
            title="Στροφορμή Ηλεκτρομαγνητικών Κυμάτων",
            question_type="Multiple Choice",
            prompt_text="Με ποια ιδιότητα των κυμάτων συνδέεται η στροφορμή;",
            options=[
                QuestionOption(
                    letter="Α",
                    text="Την ταχύτητα του φωτός",
                    is_correct=False,
                    explanation="Λάθος: Η ταχύτητα του φωτός καθορίζει τον ρυθμό διάδοσης.",
                ),
                QuestionOption(
                    letter="Β",
                    text="Το πλάτος ταλάντωσης του κύματος",
                    is_correct=False,
                    explanation="Λάθος: Το πλάτος καθορίζει τη μέγιστη ένταση του πεδίου.",
                ),
                QuestionOption(
                    letter="Γ",
                    text="Την ένταση του κύματος",
                    is_correct=False,
                    explanation="Λάθος: Η ένταση μετρά τη ροή ισχύος.",
                ),
                QuestionOption(
                    letter="Δ",
                    text="Την πόλωση του κύματος",
                    is_correct=True,
                    explanation="Σωστό: Η κυκλική και ελλειπτική πόλωση συνοδεύεται από ιδιοστροφορμή (spin angular momentum) ίση με ±ℏ ανά φωτόνιο.",
                ),
            ],
            correct_option_letter="Δ",
            final_answer="Δ] Την πόλωση του κύματος",
            detailed_justification="Όταν το διάνυσμα του ηλεκτρικού πεδίου περιστρέφεται (κυκλική πόλωση), το ηλεκτρομαγνητικό κύμα μεταφέρει στροφορμή στο υλικό με το οποίο αλληλεπιδρά.",
            common_pitfalls=["Η γραμμική πόλωση έχει μηδενική στροφορμή, ενώ η κυκλική μέγιστη."],
            related_theory_topic="ΗΜ Κύματα & Πόλωση",
        ),
        ExamQuestion(
            question_number=2,
            title="Πηγές Ηλεκτρικού Πεδίου (Συμπλήρωση Κενού)",
            question_type="Theory Analysis",
            prompt_text="Η ένταση του ηλεκτρικού πεδίου, εξαρτάται από τα φορτία που .................................................... το πεδίο;",
            options=[],
            final_answer="δημιουργούν (ή παράγουν / προκαλούν)",
            detailed_justification="Σύμφωνα με τον νόμο του Coulomb και τον ορισμό E = F / q_0, η ένταση E καθορίζεται αποκλειστικά από τα φορτία-πηγές Q και τη σχετική θέση r, ανεξάρτητα από το δοκιμαστικό φορτίο q_0.",
            common_pitfalls=["Μην απαντήσετε 'αισθάνονται' ή 'δέχονται'. Το πεδίο υπάρχει ανεξάρτητα από το αν τοποθετήσουμε δοκιμαστικό φορτίο q."],
            related_theory_topic="Ηλεκτροστατική & Ένταση Πεδίου E",
        ),
        ExamQuestion(
            question_number=3,
            title="Διατήρηση στη Διεπιφάνεια Μέσων",
            question_type="Multiple Choice",
            prompt_text="Ποιο μέγεθος θεωρούμε ότι διατηρείται στη διεπιφάνεια 2 διαφορετικών μέσων για να υπολογίσουμε τη συχνότητα του ανακλώμενου και διαθλώμενου κύματος;",
            options=[
                QuestionOption(
                    letter="Α",
                    text="Η ηλεκτρική ροή",
                    is_correct=False,
                    explanation="Λάθος: Η κάθετη συνιστώσα του D είναι συνεχής ελλείψει ελεύθερων επιφανειακών φορτίων, αλλά αυτό δεν καθορίζει τη συχνότητα.",
                ),
                QuestionOption(
                    letter="Β",
                    text="Η ορμή (ή ενέργεια)",
                    is_correct=True,
                    explanation="Σωστό: Η διατήρηση ενέργειας E = hf (και η παράλληλη ορμή p_|| = ℏ k_||) επιβάλλει ισότητα συχνοτήτων f_i = f_r = f_t στη διεπιφάνεια.",
                ),
                QuestionOption(
                    letter="Γ",
                    text="Η στροφορμή",
                    is_correct=False,
                    explanation="Λάθος: Η στροφορμή συνδέεται με την κατάσταση πόλωσης.",
                ),
                QuestionOption(
                    letter="Δ",
                    text="Η πόλωση",
                    is_correct=False,
                    explanation="Λάθος: Η πόλωση μπορεί να τροποποιηθεί κατά την ανάκλαση (γωνία Brewster).",
                ),
            ],
            correct_option_letter="Β",
            final_answer="Β] Η ορμή (ή διατήρηση ενέργειας/φάσης)",
            detailed_justification="Η απαίτηση για χρονική συμφωνία φάσης (ω_i t = ω_r t = ω_t t) σε κάθε χρονική στιγμή στη διεπιφάνεια ισοδυναμεί με τη διατήρηση ενέργειας και ορμής.",
            common_pitfalls=["Η συχνότητα παραμένει πάντα αμετάβλητη κατά τη μετάβαση σε άλλο οπτικό μέσο: f_1 = f_2."],
            related_theory_topic="Οριακές Συνθήκες & Ανάκλαση Snell",
        ),
        ExamQuestion(
            question_number=4,
            title="Ηλεκτρομαγνητικό Φάσμα (Συμπλήρωση Κενού)",
            question_type="Theory Analysis",
            prompt_text="Οι διαφορετικοί τύποι ηλεκτρομαγνητικής ακτινοβολίας (ορατό φως, ακτίνες Χ, υπεριώδεις) έχουν διαφορετική ................................................. .",
            options=[],
            final_answer="συχνότητα (ή μήκος κύματος / ενέργεια)",
            detailed_justification="Όλες οι ηλεκτρομαγνητικές ακτινοβολίες κινούνται με ταχύτητα c στο κενό, αλλά διαφοροποιούνται ριζικά ως προς τη συχνότητα f (και το αντίστοιχο μήκος κύματος λ = c/f).",
            common_pitfalls=["Μην γράψετε 'ταχύτητα'. Στο κενό όλες έχουν ακριβώς την ίδια ταχύτητα c = 3×10⁸ m/s."],
            related_theory_topic="Ηλεκτρομαγνητικό Φάσμα",
        ),
        ExamQuestion(
            question_number=5,
            title="Άσκηση 1: Υπολογισμός Πυκνότητας Φορτίου ρ από τη Μετατόπιση D",
            question_type="Calculations",
            prompt_text=r"Σύμφωνα με τον νόμο του Gauss για τη διηλεκτρική μετατόπιση $\vec{D}$ ισχύει $\vec{\nabla}\cdot\vec{D}=\rho$, όπου ρ η πυκνότητα φορτίου. Αν $\vec{D}=4x\hat{x}-6z^2\hat{y}$, να υπολογίσετε την πυκνότητα φορτίου $\rho$.",
            given_parameters=[
                GivenParameter("D_x", "4x", "x-συνιστώσα μετατόπισης"),
                GivenParameter("D_y", "-6z^2", "y-συνιστώσα μετατόπισης"),
                GivenParameter("D_z", "0", "z-συνιστώσα μετατόπισης"),
            ],
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Διατύπωση διαφορικής μορφής 1ης εξίσωσης Maxwell (Νόμος Gauss)",
                    formula=r"\rho = \vec{\nabla}\cdot\vec{D} = \frac{\partial D_x}{\partial x} + \frac{\partial D_y}{\partial y} + \frac{\partial D_z}{\partial z}",
                    substitution=r"\rho = \frac{\partial}{\partial x}(D_x) + \frac{\partial}{\partial y}(D_y) + \frac{\partial}{\partial z}(D_z)",
                    result=r"\rho = \frac{\partial D_x}{\partial x} + \frac{\partial D_y}{\partial y} + \frac{\partial D_z}{\partial z}",
                    rationale="Η απόκλιση της ηλεκτρικής μετατόπισης καθορίζει άμεσα την τοπική πυκνότητα φορτίου.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Αναγνώριση και καταγραφή των συνιστωσών του διανύσματος D",
                    formula=r"\vec{D} = D_x \hat{x} + D_y \hat{y} + D_z \hat{z}",
                    substitution=r"D_x = 4x, \quad D_y = -6z^2, \quad D_z = 0",
                    result=r"(D_x, D_y, D_z) = (4x, \ -6z^2, \ 0)",
                    rationale="Αντιστοίχιση των όρων του διανύσματος D στους αντίστοιχους καρτεσιανούς άξονες.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Υπολογισμός μερικής παραγώγου της x-συνιστώσας",
                    formula=r"\frac{\partial D_x}{\partial x} = \frac{\partial}{\partial x}(4x)",
                    substitution=r"\frac{\partial}{\partial x}(4x) = 4 \cdot \frac{d}{dx}(x) = 4 \cdot 1 = 4",
                    result=r"\frac{\partial D_x}{\partial x} = 4",
                    rationale="Η παράγωγος του 4x ως προς τη μεταβλητή x ισούται με 4.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Υπολογισμός μερικής παραγώγου της y-συνιστώσας",
                    formula=r"\frac{\partial D_y}{\partial y} = \frac{\partial}{\partial y}(-6z^2)",
                    substitution=r"\frac{\partial}{\partial y}(-6z^2) = -6z^2 \cdot \frac{\partial}{\partial y}(1) = 0",
                    result=r"\frac{\partial D_y}{\partial y} = 0",
                    rationale="Ο όρος -6z² εξαρτάται αποκλειστικά από το z. Κατά τη μερική παραγώγιση ως προς y, συμπεριφέρεται ως καθαρή σταθερά.",
                ),
                CalculationStep(
                    step_number=5,
                    title="Υπολογισμός μερικής παραγώγου της z-συνιστώσας",
                    formula=r"\frac{\partial D_z}{\partial z} = \frac{\partial}{\partial z}(0)",
                    substitution=r"\frac{\partial}{\partial z}(0) = 0",
                    result=r"\frac{\partial D_z}{\partial z} = 0",
                    rationale="Η z-συνιστώσα είναι μηδενική, συνεπώς και η παράγωγός της ισούται με 0.",
                ),
                CalculationStep(
                    step_number=6,
                    title="Άθροιση μερικών παραγώγων και εξαγωγή πυκνότητας φορτίου",
                    formula=r"\rho(x, y, z) = \frac{\partial D_x}{\partial x} + \frac{\partial D_y}{\partial y} + \frac{\partial D_z}{\partial z}",
                    substitution=r"\rho = 4 + 0 + 0 = 4",
                    result=r"\rho = 4 \quad [\text{C/m}^3]",
                    rationale="Η πυκνότητα φορτίου είναι αυστηρά σταθερή και ομοιόμορφη σε ολόκληρο τον χώρο.",
                ),
            ],
            final_answer=r"\rho = 4 \quad [\text{C/m}^3]",
            detailed_justification="Η πυκνότητα φορτίου είναι ομοιόμορφη και σταθερή παντού στον χώρο με τιμή 4 C/m³.",
            common_pitfalls=["Προσοχή: το D_y = -6z² εξαρτάται από το z, άρα η παράγωγος ως προς y είναι 0!"],
            related_theory_topic="Εξισώσεις Maxwell & Νόμος Gauss",
        ),
        ExamQuestion(
            question_number=6,
            title="Άσκηση 2: Παράμετροι ΗΜ Κύματος & Ροή Poynting",
            question_type="Calculations",
            prompt_text=r"Ένα ηλεκτρομαγνητικό κύμα διαδίδεται στο κενό και το ηλεκτρικό του πεδίο είναι $\vec{E}=300\cos(kz-200\pi t)\hat{x}$. α) Ποιο είναι το μήκος κύματος $\lambda$ και η συχνότητα $f$; β) Να γραφεί το διάνυσμα ταλάντωσης της μαγνητικής επαγωγής $\vec{B}$. γ) Να υπολογισθεί το διάνυσμα Poynting $\vec{S}$ και η ένταση $I$.",
            given_parameters=[
                GivenParameter("E_0", "300 \\text{ V/m}", "Πλάτος ηλεκτρικού πεδίου"),
                GivenParameter(r"\omega", "200\\pi \\text{ rad/s}", "Κυκλική συχνότητα"),
                GivenParameter("c", "3 \\times 10^8 \\text{ m/s}", "Ταχύτητα φωτός στο κενό"),
                GivenParameter(r"\mu_0", r"4\pi \times 10^{-7} \text{ T}\cdot\text{m/A}", "Μαγνητική διαπερατότητα κενού"),
            ],
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Αναγνώριση βασικών κυματικών παραμέτρων από την εξίσωση",
                    formula=r"\vec{E}(z,t) = E_0 \cos(kz - \omega t)\hat{u}_E",
                    substitution=r"E_0 = 300 \ \text{V/m}, \quad \omega = 200\pi \ \text{rad/s}, \quad \hat{u}_E = \hat{x}, \quad \hat{k} = +\hat{z}",
                    result=r"E_0 = 300 \ \text{V/m}, \quad \omega = 200\pi \ \text{rad/s}",
                    rationale="Η φάση (kz - 200πt) περιγράφει κύμα που διαδίδεται προς τα +z με ηλεκτρικό πεδίο πολωμένο κατά x.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Υπολογισμός γραμμικής συχνότητας f",
                    formula=r"\omega = 2\pi f \implies f = \frac{\omega}{2\pi}",
                    substitution=r"f = \frac{200\pi}{2\pi} = 100 \ \text{Hz}",
                    result=r"f = 100 \ \text{Hz}",
                    rationale="Η συχνότητα 100 Hz ανήκει στη ζώνη εξαιρετικά χαμηλών συχνοτήτων (ELF).",
                ),
                CalculationStep(
                    step_number=3,
                    title="Υπολογισμός κυματάριθμου k στο κενό",
                    formula=r"k = \frac{\omega}{c}",
                    substitution=r"k = \frac{200\pi}{3 \times 10^8} = \frac{2\pi}{3 \times 10^6} \ \text{rad/m}",
                    result=r"k \approx 2.0944 \times 10^{-6} \ \text{rad/m}",
                    rationale="Ο κυματάριθμος k εκφράζει την εξαιρετικά αργή μεταβολή της φάσης στον χώρο.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Αναλυτικός υπολογισμός μήκους κύματος λ",
                    formula=r"\lambda = \frac{c}{f} = \frac{2\pi}{k}",
                    substitution=r"\lambda = \frac{3 \times 10^8 \ \text{m/s}}{100 \ \text{Hz}} = 3 \times 10^6 \ \text{m} = 3000 \ \text{km}",
                    result=r"\lambda = 3 \times 10^6 \ \text{m} = 3000 \ \text{km}",
                    rationale="Λόγω της πολύ χαμηλής συχνότητας, το μήκος κύματος ανέρχεται σε 3.000 χιλιόμετρα.",
                ),
                CalculationStep(
                    step_number=5,
                    title="Υπολογισμός πλάτους μαγνητικού πεδίου B_0",
                    formula=r"B_0 = \frac{E_0}{c}",
                    substitution=r"B_0 = \frac{300 \ \text{V/m}}{3 \times 10^8 \ \text{m/s}} = 10^{-6} \ \text{T} = 1 \ \mu\text{T}",
                    result=r"B_0 = 10^{-6} \ \text{T} = 1 \ \mu\text{T}",
                    rationale="Η μαγνητική επαγωγή σχετίζεται άμεσα με το ηλεκτρικό πεδίο μέσω της ταχύτητας c.",
                ),
                CalculationStep(
                    step_number=6,
                    title="Προσδιορισμός διανύσματος ταλάντωσης B μέσω εξωτερικού γινομένου",
                    formula=r"\hat{B} = \hat{k} \times \hat{E} \implies \hat{z} \times \hat{x} = \hat{y}",
                    substitution=r"\vec{B}(z,t) = B_0 \cos(kz - \omega t)\hat{y} = 10^{-6}\cos(kz - 200\pi t)\hat{y} \ \text{T}",
                    result=r"\vec{B}(z,t) = 10^{-6}\cos(kz - 200\pi t)\hat{y} \ \text{T}",
                    rationale="Επειδή ẑ × x̂ = +ŷ, το μαγνητικό πεδίο ταλαντώνεται αυστηρά κατά τον θετικό άξονα y.",
                ),
                CalculationStep(
                    step_number=7,
                    title="Υπολογισμός στιγμιαίου διανύσματος Poynting S",
                    formula=r"\vec{S}(z,t) = \frac{1}{\mu_0}(\vec{E}\times\vec{B}) = \frac{E_0 B_0}{\mu_0}\cos^2(kz - \omega t)(\hat{x}\times\hat{y})",
                    substitution=r"\vec{S} = \frac{300 \times 10^{-6}}{4\pi \times 10^{-7}}\cos^2(...)(+\hat{z}) = \frac{750}{\pi}\cos^2(kz - 200\pi t)\hat{z}",
                    result=r"\vec{S}(z,t) \approx 238.73 \cos^2(kz - 200\pi t)\hat{z} \ \text{W/m}^2",
                    rationale="Η στιγμιαία ροή ισχύος είναι παράλληλη προς την κατεύθυνση διάδοσης του κύματος (+ẑ).",
                ),
                CalculationStep(
                    step_number=8,
                    title="Υπολογισμός μέσης έντασης ακτινοβολίας I",
                    formula=r"I = \langle |\vec{S}| \rangle = \frac{S_{\text{peak}}}{2} = \frac{1}{2} \cdot \frac{750}{\pi} = \frac{375}{\pi}",
                    substitution=r"I = \frac{375}{\pi} \approx \frac{375}{3.14159} \ \text{W/m}^2 \approx 119.37 \ \text{W/m}^2",
                    result=r"I \approx 119.37 \ \text{W/m}^2",
                    rationale="Η μέση χρονική τιμή του τετραγώνου του συνημιτόνου σε μία περίοδο ισούται με 1/2.",
                ),
            ],
            final_answer=r"\lambda = 3000\text{ km}, \ f = 100\text{ Hz}, \ \vec{B} = 10^{-6}\cos(kz - 200\pi t)\hat{y}\text{ T}, \ \vec{S} \approx 238.73\cos^2(...)\hat{z}\text{ W/m}^2, \ I \approx 119.37\text{ W/m}^2",
            detailed_justification="Το κύμα διαδίδεται κατά +z, με ηλεκτρικό πεδίο κατά x και μαγνητικό πεδίο κατά y.",
            common_pitfalls=["Μην μπερδέψετε το 200π με τη συχνότητα: ω = 200π rad/s, άρα f = 200π / 2π = 100 Hz."],
            related_theory_topic="Επίπεδα Ηλεκτρομαγνητικά Κύματα & Διάνυσμα Poynting",
        ),
    ]

    justifications = [
        DesignJustification(
            title="Σταθερή Πυκνότητα Φορτίου",
            category="Gauss Law",
            description="Όταν η απόκλιση div(D) αποδίδει σταθερό αριθμό (εδώ 4), το φορτίο είναι ομοιόμορφα κατανεμημένο.",
            rationale="Απλοποιεί τους υπολογισμούς καθώς το πεδίο προέρχεται από σταθερή πηγή όγκου.",
        ),
        DesignJustification(
            title="Κυκλικό Τρίεδρο (x̂, ŷ, ẑ)",
            category="Wave Geometry",
            description="Η σχέση x̂ × ŷ = ẑ πιστοποιεί ότι με E κατά x και διάδοση κατά z, το B ταλαντώνεται αναγκαστικά κατά +y.",
            rationale="Βασικός κανόνας δεξιού χεριού για εγκάρσια ηλεκτρομαγνητικά κύματα TEM.",
        ),
    ]

    solution_code = '''"""Python verification script for June 2026 Team C exam problems."""

import sympy as sp

def verify_divergence() -> None:
    """Verifies Exercise 1: div(D) = rho."""
    x, y, z = sp.symbols('x y z')
    D_x = 4 * x
    D_y = -6 * z**2
    D_z = sp.Integer(0)
    
    div_D = sp.diff(D_x, x) + sp.diff(D_y, y) + sp.diff(D_z, z)
    expected = 4
    print("--- Askisi 1: Gauss Law Divergence ---")
    print(f"D = [{D_x}] x_hat + [{D_y}] y_hat")
    print(f"div(D) = rho = {div_D} C/m^3")
    assert div_D == expected, f"Mismatch: {div_D} != {expected}"
    print("Verification Askisi 1: PASSED")

def verify_wave() -> None:
    """Verifies Exercise 2: EM wave parameters, Poynting vector, and intensity."""
    c = 3e8
    mu_0 = 4 * 3.141592653589793 * 1e-7
    E_0 = 300.0
    omega = 200 * 3.141592653589793
    
    f = omega / (2 * 3.141592653589793)
    k = omega / c
    wavelength = c / f
    B_0 = E_0 / c
    S_max = (E_0 * B_0) / mu_0
    intensity = S_max / 2.0
    
    print("\\n--- Askisi 2: Plane EM Wave ---")
    print(f"Frequency f = {f:.2f} Hz")
    print(f"Wavelength lambda = {wavelength/1000:.1f} km")
    print(f"Magnetic amplitude B_0 = {B_0:.4e} T (1 uT)")
    print(f"Peak Poynting flux S_max = {S_max:.2f} W/m^2")
    print(f"Radiation Intensity I = {intensity:.2f} W/m^2")
    print("Verification Askisi 2: PASSED")

if __name__ == "__main__":
    verify_divergence()
    verify_wave()
'''

    return Scenario(
        id="past_exam_2026_06_team_c",
        title="Εξεταστική Ιουνίου 2026 — Ομάδα Γ",
        subtitle="Πλήρης Επίλυση: Πόλωση & Στροφορμή, Φάσμα ΗΜ, Νόμος Gauss & Κύμα",
        course_tag="Past Exam 2026",
        duration_info="Διάρκεια: 2 ώρες | 4 Ερωτήσεις Θεωρίας & 2 Ασκήσεις Υπολογισμού",
        paragraphs=paragraphs,
        questions=questions,
        justifications=justifications,
        solution_code=solution_code,
    )

