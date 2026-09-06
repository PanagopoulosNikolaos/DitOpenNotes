"""Practice Exam Scenario 1: Comprehensive Electromagnetics & Transmission Foundations.

Verbatim transcription of practice exam 1 with three-part contract hover tooltips,
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


def createSynthExam1Comprehensive() -> Scenario:
    """Instantiates the Practice Exam 1 comprehensive scenario.

    Returns:
        Scenario: Complete scenario container with verbatim text and solutions.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(
                    text="Εξέταση Εξάσκησης 1: Θεωρία & Υπολογιστικές Ασκήσεις Ηλεκτρομαγνητισμού\n",
                    is_highlight=False,
                ),
                TextSegment(
                    text="Πλήρες σετ θεμάτων: Κανόνες Kirchhoff, Αγωγοί & Πυκνότητα J, Δυνάμεις Αγωγών, Φορτίο σε B, Πυκνωτές & ΗΜ Κύμα.",
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
                    text="Ηλεκτρικό Ρεύμα και Πυκνότητα Φορτίου",
                    is_highlight=True,
                    category="field",
                    tag_label="ΡΕΥΜΑ & J",
                    tooltip="Classification: Ηλεκτρικό Ρεύμα & Πυκνότητα Ρεύματος | Detection Clue: 'Ηλεκτρικό Ρεύμα και Πυκνότητα Φορτίου' | Application Rationale: I = ∬ J·dS, όπου J = n q v_d εκφράζει την κίνηση φορτίων ανά επιφάνεια.",
                ),
                TextSegment(text=": Πώς συνδέεται το ηλεκτρικό ρεύμα με την πυκνότητα ρεύματος; Ποιο φυσικό μέγεθος περιγράφει την κίνηση φορτίων μέσα από μια επιφάνεια;\n", is_highlight=False),
                TextSegment(text="2. ", is_highlight=False),
                TextSegment(
                    text="Κανόνες του Kirchhoff",
                    is_highlight=True,
                    category="law",
                    tag_label="KIRCHHOFF",
                    tooltip="Classification: Θεμελιώδεις Κανόνες Κυκλωμάτων | Detection Clue: 'Κανόνες του Kirchhoff' | Application Rationale: 1ος κανόνας κόμβων (διατήρηση φορτίου ΣI=0) και 2ος κανόνας βρόχων (διατήρηση ενέργειας ΣV=0).",
                ),
                TextSegment(text=": Ποια εξίσωση συνδέεται με τους κανόνες του Kirchhoff; Εξηγήστε συνοπτικά και τους δύο κανόνες.\n", is_highlight=False),
                TextSegment(text="3. ", is_highlight=False),
                TextSegment(
                    text="Αντίσταση και Αγωγιμότητα",
                    is_highlight=True,
                    category="param",
                    tag_label="R & σ",
                    tooltip="Classification: Παράμετροι Αγωγιμότητας | Detection Clue: 'Αντίσταση και Αγωγιμότητα' | Application Rationale: σ = 1/ρ, R = ρ L / A. Καθορίζονται από υλικό, μήκος, διατομή και θερμοκρασία.",
                ),
                TextSegment(text=": Πώς συνδέεται η ειδική αντίσταση με την ειδική αγωγιμότητα; Ποιοι παράγοντες καθορίζουν την ηλεκτρική αντίσταση ενός αγωγού;\n", is_highlight=False),
                TextSegment(text="4. ", is_highlight=False),
                TextSegment(
                    text="Δυναμικές Γραμμές Μαγνητοστατικού Πεδίου",
                    is_highlight=True,
                    category="field",
                    tag_label="ΓΡΑΜΜΕΣ B",
                    tooltip="Classification: Μαγνητικές Δυναμικές Γραμμές | Detection Clue: 'Δυναμικές Γραμμές Μαγνητοστατικού Πεδίου' | Application Rationale: Κλειστοί βρόχοι χωρίς αρχή και τέλος (div B = 0), εξωτερικά από Βόρειο σε Νότιο πόλο.",
                ),
                TextSegment(text=": Ποια είναι η κατεύθυνση των δυναμικών γραμμών ενός μαγνητοστατικού πεδίου;\n", is_highlight=False),
                TextSegment(text="5. ", is_highlight=False),
                TextSegment(
                    text="Δυνάμεις σε Φορτία",
                    is_highlight=True,
                    category="law",
                    tag_label="LORENTZ",
                    tooltip="Classification: Δυνάμεις Coulomb & Lorentz | Detection Clue: 'ακίνητο και ένα κινούμενο ηλεκτρικό φορτίο' | Application Rationale: Ασκείται μόνο ηλεκτροστατική δύναμη Coulomb, καθώς το ακίνητο φορτίο δεν γεννά μαγνητικό πεδίο.",
                ),
                TextSegment(text=": Θεωρήστε ένα ακίνητο και ένα κινούμενο ηλεκτρικό φορτίο. Τι είδους δυνάμεις θα ασκηθούν μεταξύ τους;\n", is_highlight=False),
                TextSegment(text="6. ", is_highlight=False),
                TextSegment(
                    text="Δυνάμεις Μεταξύ Αγωγών",
                    is_highlight=True,
                    category="law",
                    tag_label="ΠΑΡΑΛΛΗΛΟΙ",
                    tooltip="Classification: Μαγνητική Αλληλεπίδραση Ρευμάτων | Detection Clue: 'δύο παράλληλων ρευματοφόρων αγωγών' | Application Rationale: Ομόρροπα ρεύματα έλκονται, αντίρροπα απωθούνται: F/L = μ_0 I_1 I_2 / (2π d).",
                ),
                TextSegment(text=": Τι είδους δύναμη αναπτύσσεται μεταξύ δύο παράλληλων ρευματοφόρων αγωγών;\n", is_highlight=False),
                TextSegment(text="7. ", is_highlight=False),
                TextSegment(
                    text="Μαγνητική Επαγωγή B",
                    is_highlight=True,
                    category="field",
                    tag_label="BIOT-SAVART",
                    tooltip="Classification: Νόμος Biot-Savart | Detection Clue: 'Από ποια μεγέθη εξαρτάται η μαγνητική επαγωγή' | Application Rationale: dB = (μ_0 I / 4π) (dl x r̂) / r^2.",
                ),
                TextSegment(text=": Από ποια μεγέθη εξαρτάται η μαγνητική επαγωγή ενός μαγνητικού πεδίου;\n", is_highlight=False),
                TextSegment(text="8. ", is_highlight=False),
                TextSegment(
                    text="Διαφορές Δυναμικών Γραμμών",
                    is_highlight=True,
                    category="law",
                    tag_label="E vs B",
                    tooltip="Classification: Σύγκριση Πεδίων E και B | Detection Clue: 'Διαφορές Δυναμικών Γραμμών' | Application Rationale: Γραμμές E: ανοικτές (πηγές τα φορτία). Γραμμές B: κλειστές (απουσία μονοπόλων).",
                ),
                TextSegment(text=": Πώς διαφέρουν οι δυναμικές γραμμές ενός μαγνητικού πεδίου από αυτές ενός ηλεκτρικού πεδίου;", is_highlight=False),
            ],
            accent_border_color="accent",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Μέρος Β: Ασκήσεις Υπολογισμού\n", is_highlight=False),
                TextSegment(text="Άσκηση 1: Επίπεδο Ηλεκτρομαγνητικό Κύμα\nΤο ηλεκτρικό πεδίο δίνεται από τη σχέση: ", is_highlight=False),
                TextSegment(
                    text="E = 5 cos(7·10¹² y - ωt) ẑ",
                    is_highlight=True,
                    category="field",
                    tag_label="E(y,t)",
                    tooltip="Classification: ΗΜ Κύμα Υψηλής Συχνότητας | Detection Clue: k = 7*10^12 rad/m κατά y, πόλωση z | Application Rationale: Υπολογισμός T, f, λ, B(y,t) κατά +x, S και μέσης έντασης I.",
                ),
                TextSegment(text=". Βρείτε T, f, λ, B, S, I. Δίνονται: c = 3×10⁸ m/s, μ₀ = 4π×10⁻⁷ Tm/A.\n", is_highlight=False),
                TextSegment(text="Άσκηση 2: Ιδιότητες Αγωγού\nΚυλινδρικός αγωγός με ", is_highlight=False),
                TextSegment(
                    text="σ = 5.8·10⁷ S/m, r = 2 mm, L = 50 m, V = 10 V",
                    is_highlight=True,
                    category="param",
                    tag_label="ΑΓΩΓΟΣ",
                    tooltip="Classification: Παράμετροι Κυλινδρικού Αγωγού | Detection Clue: σ, r, L, V | Application Rationale: A = π r^2, R = L/(σ A), I = V/R, E = V/L, J = σ E.",
                ),
                TextSegment(text=". Υπολογίστε R, J, I, E.\n", is_highlight=False),
                TextSegment(text="Άσκηση 3: Δυνάμεις Μεταξύ Παράλληλων Συρμάτων\nΔύο σύρματα απέχουν ", is_highlight=False),
                TextSegment(
                    text="d = 20 cm με ρεύματα I₁ = 30 A και I₂ = 50 A",
                    is_highlight=True,
                    category="param",
                    tag_label="ΠΑΡΑΛΛΗΛΑ ΣΥΡΜΑΤΑ",
                    tooltip="Classification: Παράλληλα Ρεύματα | Detection Clue: d = 0.2 m, I_1 = 30 A, I_2 = 50 A | Application Rationale: B_1 = μ_0 I_1 / (2π d) και F/L = μ_0 I_1 I_2 / (2π d).",
                ),
                TextSegment(text=" προς την ίδια κατεύθυνση. Υπολογίστε B₁ και F/L.\n", is_highlight=False),
                TextSegment(text="Άσκηση 4: Κίνηση Φορτισμένου Σωματιδίου σε Μαγνητικό Πεδίο\nΗλεκτρόνιο επιταχύνεται από ", is_highlight=False),
                TextSegment(
                    text="V₀ = 500 V και εισέρχεται κάθετα σε B = 0.2 T",
                    is_highlight=True,
                    category="param",
                    tag_label="ΗΛΕΚΤΡΟΝΙΟ ΣΕ B",
                    tooltip="Classification: Κυκλοτρονική Κίνηση Φορτίου | Detection Clue: V_0 = 500 V, B = 0.2 T | Application Rationale: (1/2)m v^2 = e V_0, F_B = e v B, R = m v / (e B).",
                ),
                TextSegment(text=". Υπολογίστε v, F_B, R.\n", is_highlight=False),
                TextSegment(text="Άσκηση 5: Πυκνωτής με Διηλεκτρικό\nΕπίπεδος πυκνωτής με ", is_highlight=False),
                TextSegment(
                    text="A = 250 cm², d = 3 mm, κ = 4.5, V = 100 V",
                    is_highlight=True,
                    category="param",
                    tag_label="ΠΥΚΝΩΤΗΣ κ",
                    tooltip="Classification: Επίπεδος Πυκνωτής με Διηλεκτρικό | Detection Clue: A = 0.025 m^2, d = 0.003 m, κ = 4.5 | Application Rationale: C_0 = ε_0 A / d, C = κ C_0, Q = C V.",
                ),
                TextSegment(text=". Υπολογίστε C₀, C, Q. Δίνεται ε₀ = 8.854×10⁻¹² F/m.", is_highlight=False),
            ],
            accent_border_color="accent",
        ),
    ]

    questions = [
        ExamQuestion(
            question_number=1,
            title="Κανόνες Kirchhoff & Αρχές Διατήρησης",
            question_type="Theory Analysis",
            prompt_text="Ποια εξίσωση συνδέεται με τους κανόνες του Kirchhoff; Εξηγήστε συνοπτικά και τους δύο κανόνες του Kirchhoff.",
            options=[],
            final_answer="1ος Κανόνας Κόμβων (ΣI = 0) -> Διατήρηση Φορτίου | 2ος Κανόνας Βρόχων (ΣV = 0) -> Διατήρηση Ενέργειας",
            detailed_justification="Ο 1ος κανόνας απορρέει από την εξίσωση συνέχειας ∇·J = -∂ρ/∂t σε στάσιμη κατάσταση. Ο 2ος κανόνας απορρέει από το αστρόβιλο του ηλεκτροστατικού πεδίου ∮ E·dl = 0.",
            common_pitfalls=["Σε κυκλώματα υψηλών συχνοτήτων (AC με μεταβαλλόμενη μαγνητική ροή), ο 2ος κανόνας τροποποιείται λόγω επαγωγής Faraday."],
            related_theory_topic="Ηλεκτρικά Κυκλώματα & Νόμοι Kirchhoff",
        ),
        ExamQuestion(
            question_number=2,
            title="Δυνάμεις Μεταξύ Ακίνητου και Κινούμενου Φορτίου",
            question_type="Theory Analysis",
            prompt_text="Θεωρήστε ένα ακίνητο και ένα κινούμενο ηλεκτρικό φορτίο. Τι είδους δυνάμεις θα ασκηθούν μεταξύ τους;",
            options=[],
            final_answer="Ασκείται μόνο ηλεκτρική δύναμη Coulomb. Δεν ασκείται μαγνητική δύναμη.",
            detailed_justification="Το ακίνητο φορτίο q1 παράγει αποκλειστικά ηλεκτροστατικό πεδίο E, όχι μαγνητικό πεδίο B (αφού v1=0). Έτσι, στο κινούμενο φορτίο q2 ασκείται μόνο δύναμη F = q2 E. Αντίστοιχα, το κινούμενο q2 δημιουργεί B2, αλλά το q1 είναι ακίνητο (v1=0), άρα η μαγνητική δύναμη Lorentz q1(v1 × B2) είναι μηδέν!",
            common_pitfalls=["Κλασική παγίδα: Πολλοί υποθέτουν λανθασμένα ότι ασκείται μαγνητική δύναμη επειδή το ένα φορτίο κινείται."],
            related_theory_topic="Δυνάμεις Coulomb & Lorentz",
        ),
        ExamQuestion(
            question_number=3,
            title="Άσκηση 1: Επίπεδο Ηλεκτρομαγνητικό Κύμα",
            question_type="Calculations",
            prompt_text=r"Το ηλεκτρικό πεδίο ημιτονοειδούς επίπεδου ΗΜ κύματος στο κενό δίνεται από: $\vec{E} = 5 \cos(7 \times 10^{12} y - \omega t) \hat{z}$. Βρείτε: Α) Την περίοδο $T$, συχνότητα $f$ και μήκος κύματος $\lambda$. Β) Την εξίσωση του μαγνητικού πεδίου $\vec{B}$. Γ) Το διάνυσμα Poynting $\vec{S}$. Δ) Την ένταση $I$.",
            given_parameters=[
                GivenParameter("E_0", "5 \\text{ V/m}", "Πλάτος ηλεκτρικού πεδίου"),
                GivenParameter("k", "7 \\times 10^{12} \\text{ rad/m}", "Κυματάριθμος κατά y"),
                GivenParameter("c", "3 \\times 10^8 \\text{ m/s}", "Ταχύτητα φωτός στο κενό"),
                GivenParameter(r"\mu_0", r"4\pi \times 10^{-7} \text{ T}\cdot\text{m/A}", "Μαγνητική διαπερατότητα κενού"),
            ],
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Εξαγωγή δεδομένων και γενική εξίσωση αρμονικού κύματος",
                    formula=r"\vec{E}(y,t) = E_0 \cos(k y - \omega t) \hat{u}_E",
                    substitution=r"E_0 = 5 \ \text{V/m}, \quad k = 7\times 10^{12} \ \text{rad/m}, \quad \hat{u}_k = +\hat{y}, \quad \hat{u}_E = +\hat{z}",
                    result=r"\vec{E}(y,t) = 5\cos(7\times 10^{12}y - \omega t)\hat{z} \ \text{V/m}",
                    rationale="Η διάδοση γίνεται κατά τον άξονα +y (λόγω της μορφής ky - ωt) και η πόλωση είναι κατά τον άξονα z.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Υπολογισμός μήκους κύματος λ",
                    formula=r"\lambda = \frac{2\pi}{k}",
                    substitution=r"\lambda = \frac{2\pi}{7\times 10^{12} \ \text{rad/m}} = \frac{6.283185}{7\times 10^{12}} \approx 8.9760\times 10^{-13} \ \text{m}",
                    result=r"\lambda \approx 8.976\times 10^{-13} \ \text{m} = 0.898 \ \text{pm}",
                    rationale="Μήκος κύματος στην περιοχή των σκληρών ακτίνων γάμμα (gamma rays, 1 pm = 10^-12 m).",
                ),
                CalculationStep(
                    step_number=3,
                    title="Υπολογισμός κυκλικής συχνότητας ω",
                    formula=r"\omega = c k",
                    substitution=r"\omega = (3\times 10^8 \ \text{m/s}) \times (7\times 10^{12} \ \text{rad/m}) = 2.10\times 10^{21} \ \text{rad/s}",
                    result=r"\omega = 2.10\times 10^{21} \ \text{rad/s}",
                    rationale="Σχέση διασποράς στο κενό (v = c = ω/k).",
                ),
                CalculationStep(
                    step_number=4,
                    title="Υπολογισμός γραμμικής συχνότητας f και περιόδου T",
                    formula=r"f = \frac{\omega}{2\pi} = \frac{c}{\lambda}, \quad T = \frac{1}{f}",
                    substitution=r"f = \frac{2.10\times 10^{21}}{2\pi} \approx 3.3423\times 10^{20} \ \text{Hz}, \quad T = \frac{1}{3.3423\times 10^{20}} \approx 2.992\times 10^{-21} \ \text{s}",
                    result=r"f \approx 3.342\times 10^{20} \ \text{Hz}, \quad T \approx 2.992 \times 10^{-21} \ \text{s}",
                    rationale="Εξαιρετικά υψηλή συχνότητα και υπο-ατομική χρονική περίοδος ταλάντωσης.",
                ),
                CalculationStep(
                    step_number=5,
                    title="Υπολογισμός πλάτους μαγνητικού πεδίου B_0",
                    formula=r"B_0 = \frac{E_0}{c}",
                    substitution=r"B_0 = \frac{5 \ \text{V/m}}{3\times 10^8 \ \text{m/s}} \approx 1.6667\times 10^{-8} \ \text{T}",
                    result=r"B_0 \approx 1.667\times 10^{-8} \ \text{T} = 16.67 \ \text{nT}",
                    rationale="Στο ηλεκτρομαγνητικό κύμα ο λόγος των πλατών E_0 / B_0 ισούται ακριβώς με την ταχύτητα του φωτός c.",
                ),
                CalculationStep(
                    step_number=6,
                    title="Διανυσματικός προσδιορισμός και εξίσωση μαγνητικού πεδίου B(y,t)",
                    formula=r"\hat{u}_E \times \hat{u}_B = \hat{u}_k \implies \hat{z} \times \hat{u}_B = \hat{y} \implies \hat{u}_B = +\hat{x}",
                    substitution=r"\hat{z} \times \hat{x} = +\hat{y}, \quad \vec{B}(y,t) = B_0 \cos(k y - \omega t)\hat{x}",
                    result=r"\vec{B}(y,t) = 1.667\times 10^{-8} \cos(7\times 10^{12}y - 2.10\times 10^{21}t)\hat{x} \ \text{T}",
                    rationale="Τα διανύσματα E, B και k σχηματίζουν ορθογώνιο δεξιόστροφο σύστημα καρτεσιανών αξόνων.",
                ),
                CalculationStep(
                    step_number=7,
                    title="Υπολογισμός στιγμιαίου διανύσματος Poynting S(y,t)",
                    formula=r"\vec{S} = \frac{1}{\mu_0}(\vec{E}\times\vec{B}) = \frac{E_0 B_0}{\mu_0}\cos^2(ky - \omega t)(\hat{z}\times\hat{x})",
                    substitution=r"S_{\max} = \frac{5 \times 1.6667\times 10^{-8}}{4\pi\times 10^{-7}} = \frac{8.3335\times 10^{-8}}{1.2566\times 10^{-6}} \approx 0.06631 \ \text{W/m}^2",
                    result=r"\vec{S}(y,t) \approx 0.06631 \cos^2(7\times 10^{12}y - 2.10\times 10^{21}t)\hat{y} \ \text{W/m}^2",
                    rationale="Το διάνυσμα Poynting δείχνει πάντα προς την κατεύθυνση διάδοσης της ηλεκτρομαγνητικής ενέργειας (+y).",
                ),
                CalculationStep(
                    step_number=8,
                    title="Υπολογισμός μέσης έντασης ακτινοβολίας I",
                    formula=r"I = \langle |\vec{S}| \rangle = \frac{1}{2} S_{\max} = \frac{E_0^2}{2\mu_0 c}",
                    substitution=r"I = \frac{1}{2}(0.06631 \ \text{W/m}^2) = \frac{5^2}{2(4\pi\times 10^{-7})(3\times 10^8)} = \frac{25}{753.98} \approx 0.03316 \ \text{W/m}^2",
                    result=r"I \approx 0.03316 \ \text{W/m}^2 = 33.16 \ \text{mW/m}^2",
                    rationale="Η μέση χρονική τιμή του cos^2 ισούται με 1/2, δίνοντας τη μέση ένταση ακτινοβολίας.",
                ),
            ],
            final_answer=r"\lambda \approx 0.898\text{ pm}, \ f \approx 3.34\times 10^{20}\text{ Hz}, \ \vec{B} \approx 1.67\times 10^{-8}\cos(...)\hat{x}\text{ T}, \ I \approx 33.16\text{ mW/m}^2",
            detailed_justification="Εξαιρετικά υψηλής συχνότητας ηλεκτρομαγνητικό κύμα με πλήρη διανυσματικό προσδιορισμό.",
            common_pitfalls=["Προσοχή στις μονάδες: 1 pm = 10^-12 m."],
            related_theory_topic="Ηλεκτρομαγνητικά Κύματα & Διάνυσμα Poynting",
        ),
        ExamQuestion(
            question_number=4,
            title="Άσκηση 2: Ηλεκτρικές Ιδιότητες Κυλινδρικού Αγωγού",
            question_type="Calculations",
            prompt_text=r"Κυλινδρικός αγωγός με $\sigma = 5.8 \times 10^7\text{ S/m}$ (χαλκός) έχει ακτίνα $r = 2\text{ mm}$, μήκος $L = 50\text{ m}$ και τάση $V = 10\text{ V}$. Υπολογίστε: Α) Αντίσταση $R$. Β) Διάνυσμα πυκνότητας ρεύματος $\vec{J}$. Γ) Ρεύμα $I$. Δ) Ένταση ηλεκτρικού πεδίου $E$.",
            given_parameters=[
                GivenParameter(r"\sigma", "5.8 \\times 10^7 \\text{ S/m}", "Ειδική αγωγιμότητα χαλκού"),
                GivenParameter("r", "2 \\text{ mm} = 2 \\times 10^{-3} \\text{ m}", "Ακτίνα αγωγού"),
                GivenParameter("L", "50 \\text{ m}", "Μήκος αγωγού"),
                GivenParameter("V", "10 \\text{ V}", "Εφαρμοζόμενη τάση"),
            ],
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Υπολογισμός εμβαδού εγκάρσιας διατομής αγωγού A",
                    formula=r"A = \pi r^2",
                    substitution=r"r = 2 \ \text{mm} = 2\times 10^{-3} \ \text{m} \implies A = \pi (2\times 10^{-3} \ \text{m})^2 = 4\pi \times 10^{-6} \ \text{m}^2 \approx 1.2566\times 10^{-5} \ \text{m}^2",
                    result=r"A \approx 1.257\times 10^{-5} \ \text{m}^2",
                    rationale="Γεωμετρική διατομή του κυλινδρικού σύρματος.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Υπολογισμός ειδικής αντίστασης ρ από την ειδική αγωγιμότητα σ",
                    formula=r"\rho = \frac{1}{\sigma}",
                    substitution=r"\rho = \frac{1}{5.8\times 10^7 \ \text{S/m}} \approx 1.7241\times 10^{-8} \ \Omega\cdot\text{m}",
                    result=r"\rho \approx 1.724\times 10^{-8} \ \Omega\cdot\text{m}",
                    rationale="Η ειδική αντίσταση εκφράζει την εγγενή δυσκολία διέλευσης φορτίων ανά μονάδα όγκου του υλικού.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Υπολογισμός ολικής ωμικής αντίστασης R",
                    formula=r"R = \rho \frac{L}{A} = \frac{L}{\sigma A}",
                    substitution=r"R = \frac{50 \ \text{m}}{5.8\times 10^7 \ \text{S/m} \times 1.2566\times 10^{-5} \ \text{m}^2} = \frac{50}{728.85} \approx 0.06860 \ \Omega",
                    result=r"R \approx 0.06860 \ \Omega = 68.60 \ \text{m}\Omega",
                    rationale="Ο χαλκός παρουσιάζει εξαιρετικά χαμηλή αντίσταση για μήκος 50 μέτρων.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Υπολογισμός έντασης ηλεκτρικού πεδίου E εντός του αγωγού",
                    formula=r"E = \frac{V}{L}",
                    substitution=r"E = \frac{10 \ \text{V}}{50 \ \text{m}} = 0.20 \ \text{V/m}",
                    result=r"E = 0.20 \ \text{V/m}",
                    rationale="Η γραμμική πτώση δυναμικού κατά μήκος ομογενούς αγωγού δημιουργεί σταθερό ηλεκτρικό πεδίο.",
                ),
                CalculationStep(
                    step_number=5,
                    title="Υπολογισμός πυκνότητας ρεύματος J (Μικροσκοπικός Νόμος Ohm)",
                    formula=r"J = \sigma E",
                    substitution=r"J = (5.8\times 10^7 \ \text{S/m}) \times (0.20 \ \text{V/m}) = 1.16\times 10^7 \ \text{A/m}^2",
                    result=r"J = 1.16\times 10^7 \ \text{A/m}^2 = 11.6 \ \text{A/mm}^2",
                    rationale="Ο διαφορικός νόμος του Ohm συνδέει το τοπικό ηλεκτρικό πεδίο με την τοπική ροή φορτίων.",
                ),
                CalculationStep(
                    step_number=6,
                    title="Υπολογισμός ολικού ρεύματος I και επαλήθευση μακροσκοπικού νόμου Ohm",
                    formula=r"I = J A = \frac{V}{R}",
                    substitution=r"I = (1.16\times 10^7 \ \text{A/m}^2)(1.2566\times 10^{-5} \ \text{m}^2) \approx 145.77 \ \text{A}, \quad I = \frac{10 \ \text{V}}{0.06860 \ \Omega} \approx 145.77 \ \text{A}",
                    result=r"I \approx 145.77 \ \text{A}",
                    rationale="Απόλυτη συμφωνία μικροσκοπικού και μακροσκοπικού μοντέλου αγωγιμότητας.",
                ),
            ],
            final_answer=r"R \approx 0.0686\ \Omega, \ I \approx 145.77\text{ A}, \ E = 0.20\text{ V/m}, \ J = 1.16\times 10^7\text{ A/m}^2",
            detailed_justification="Συνδυασμός μακροσκοπικού νόμου Ohm (V = IR) και μικροσκοπικού διαφορικού νόμου (J = σ E).",
            common_pitfalls=["Προσοχή στη μετατροπή mm σε m: r = 2 mm = 2×10⁻³ m, άρα r² = 4×10⁻⁶ m²."],
            related_theory_topic="Αγωγοί & Νόμος Ohm σε Τοπική Μορφή",
        ),
        ExamQuestion(
            question_number=5,
            title="Άσκηση 3: Δυνάμεις Μεταξύ Παράλληλων Ρευματοφόρων Συρμάτων",
            question_type="Calculations",
            prompt_text=r"Δύο μακρά παράλληλα σύρματα απέχουν απόσταση $d = 20\text{ cm}$. Διαρρέονται από ομόρροπα ρεύματα $I_1 = 30\text{ A}$ και $I_2 = 50\text{ A}$. Προσδιορίστε: Α) Το μαγνητικό πεδίο $B_1$ στη θέση του 2ου σύρματος. Β) Τη δύναμη ανά μονάδα μήκους $F/L$ στο 2ο σύρμα.",
            given_parameters=[
                GivenParameter("d", "20 \\text{ cm} = 0.2 \\text{ m}", "Απόσταση συρμάτων"),
                GivenParameter("I_1", "30 \\text{ A}", "Ρεύμα 1ου σύρματος"),
                GivenParameter("I_2", "50 \\text{ A}", "Ρεύμα 2ου σύρματος"),
                GivenParameter(r"\mu_0", r"4\pi \times 10^{-7} \text{ T}\cdot\text{m/A}", "Μαγνητική διαπερατότητα κενού"),
            ],
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Εφαρμογή νόμου Ampère για το μαγνητικό πεδίο ευθύγραμμου αγωγού",
                    formula=r"\oint \vec{B}_1 \cdot d\vec{\ell} = B_1(2\pi d) = \mu_0 I_{\text{enc}} \implies B_1 = \frac{\mu_0 I_1}{2\pi d}",
                    substitution=r"\text{Λόγω κυλινδρικής συμμετρίας, το πεδίο είναι σταθερό κατά μήκος κυκλικού βρόχου ακτίνας } d",
                    result=r"B_1 = \frac{\mu_0 I_1}{2\pi d}",
                    rationale="Ο νόμος του Ampère εξάγει ακριβώς το πεδίο απειρομήκους ρευματοφόρου σύρματος.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Αριθμητικός υπολογισμός μαγνητικής επαγωγής B_1",
                    formula=r"B_1 = \frac{\mu_0 I_1}{2\pi d}",
                    substitution=r"B_1 = \frac{(4\pi \times 10^{-7} \ \text{T}\cdot\text{m/A}) \times (30 \ \text{A})}{2\pi \times 0.20 \ \text{m}} = \frac{2\times 10^{-7} \times 30}{0.20} = \frac{6.0\times 10^{-6}}{0.20}",
                    result=r"B_1 = 3.0 \times 10^{-5} \ \text{T} = 30 \ \mu\text{T}",
                    rationale="Το μαγνητικό πεδίο που δέχεται το δεύτερο σύρμα από το πρώτο.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Μαγνητική δύναμη Laplace σε στοιχειώδες τμήμα dl του 2ου σύρματος",
                    formula=r"d\vec{F}_2 = I_2 (d\vec{\ell}_2 \times \vec{B}_1)",
                    substitution=r"\text{Επειδή } d\vec{\ell}_2 \perp \vec{B}_1 \implies \sin(90^\circ) = 1 \implies dF_2 = I_2 B_1 d\ell",
                    result=r"dF_2 = I_2 B_1 d\ell",
                    rationale="Η δύναμη Lorentz ενσωματωμένη σε συνεχή κατανομή ρεύματος (νόμος Laplace).",
                ),
                CalculationStep(
                    step_number=4,
                    title="Αλγεβρική εξαγωγή της δύναμης ανά μονάδα μήκους F/L",
                    formula=r"\frac{F}{L} = I_2 B_1 = \frac{\mu_0 I_1 I_2}{2\pi d}",
                    substitution=r"\frac{F}{L} = \frac{(4\pi \times 10^{-7})(30)(50)}{2\pi (0.20)} = \frac{(2\times 10^{-7})(1500)}{0.20}",
                    result=r"\frac{F}{L} = \frac{\mu_0 I_1 I_2}{2\pi d}",
                    rationale="Η σχέση αυτή αποτελεί τον ιστορικό ορισμό του Ampère στο διεθνές σύστημα SI.",
                ),
                CalculationStep(
                    step_number=5,
                    title="Αριθμητικός υπολογισμός δύναμης ανά μονάδα μήκους",
                    formula=r"\frac{F}{L} = I_2 B_1",
                    substitution=r"\frac{F}{L} = (50 \ \text{A}) \times (3.0\times 10^{-5} \ \text{T}) = 1.50\times 10^{-3} \ \text{N/m}",
                    result=r"\frac{F}{L} = 1.50 \times 10^{-3} \ \text{N/m} = 1.50 \ \text{mN/m}",
                    rationale="Ένταση αμοιβαίας μηχανικής δύναμης ανά μέτρο αγωγού.",
                ),
                CalculationStep(
                    step_number=6,
                    title="Διανυσματικός προσδιορισμός φοράς (Κανόνας Δεξιού Χεριού)",
                    formula=r"\vec{B}_1 = +B_1 \hat{y}, \quad d\vec{\ell}_2 = +d\ell \hat{z} \implies \hat{F}_2 = \hat{z} \times \hat{y} = -\hat{x}",
                    substitution=r"\text{Η δύναμη στο 2ο σύρμα κατευθύνεται προς το 1ο σύρμα}",
                    result=r"\text{Δύναμη Ελκτική (Ομόρροπα Ρεύματα Έλκονται)}",
                    rationale="Δύο παράλληλοι αγωγοί που διαρρέονται από ομόρροπα ρεύματα έλκονται πάντοτε μεταξύ τους.",
                ),
            ],
            final_answer=r"B_1 = 30\ \mu\text{T}, \quad F/L = 1.50\text{ mN/m (Ελκτική Δύναμη)}",
            detailed_justification="Ορισμός του Ampère στο SI: δύο παράλληλοι αγωγοί με ομόρροπα ρεύματα έλκονται αμοιβαία.",
            common_pitfalls=["Αν τα ρεύματα ήταν αντίρροπα, η δύναμη θα ήταν απωστική."],
            related_theory_topic="Μαγνητοστατική & Δύναμη Μεταξύ Αγωγών",
        ),
        ExamQuestion(
            question_number=6,
            title="Άσκηση 4: Κυκλοτρονική Κίνηση Ηλεκτρονίου σε Μαγνητικό Πεδίο",
            question_type="Calculations",
            prompt_text=r"Ηλεκτρόνιο επιταχύνεται από διαφορά δυναμικού $V_0 = 500\text{ V}$ και εισέρχεται κάθετα σε ομογενές $B = 0.2\text{ T}$. Υπολογίστε: Α) Την ταχύτητα $v$. Β) Τη μαγνητική δύναμη $F_B$. Γ) Την ακτίνα κυκλικής τροχιάς $R$. Δίνονται: $e = 1.6 \times 10^{-19}\text{ C}, m_e = 9.11 \times 10^{-31}\text{ kg}$.",
            given_parameters=[
                GivenParameter("V_0", "500 \\text{ V}", "Τάση επιτάχυνσης"),
                GivenParameter("B", "0.2 \\text{ T}", "Ένταση μαγνητικού πεδίου"),
                GivenParameter("e", "1.602 \\times 10^{-19} \\text{ C}", "Φορτίο ηλεκτρονίου"),
                GivenParameter("m_e", "9.109 \\times 10^{-31} \\text{ kg}", "Μάζα ηρεμίας ηλεκτρονίου"),
            ],
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Εφαρμογή θεμελιώδους θεωρήματος έργου-ενέργειας κατά την επιτάχυνση",
                    formula=r"W = q \Delta V = e V_0 = \Delta K = \frac{1}{2} m_e v^2 - 0",
                    substitution=r"e V_0 = (1.602\times 10^{-19} \ \text{C}) \times (500 \ \text{V}) = 8.01\times 10^{-17} \ \text{J}",
                    result=r"\frac{1}{2} m_e v^2 = 8.01\times 10^{-17} \ \text{J}",
                    rationale="Η δυναμική ηλεκτρική ενέργεια μετατρέπεται πλήρως σε κινητική ενέργεια του ηλεκτρονίου.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Αλγεβρική επίλυση και υπολογισμός ταχύτητας v",
                    formula=r"v = \sqrt{\frac{2 e V_0}{m_e}}",
                    substitution=r"v = \sqrt{\frac{2 \times 8.01\times 10^{-17} \ \text{J}}{9.109\times 10^{-31} \ \text{kg}}} = \sqrt{1.7587\times 10^{14}} \approx 1.3262\times 10^7 \ \text{m/s}",
                    result=r"v \approx 1.326\times 10^7 \ \text{m/s} \quad (4.42\% \ c)",
                    rationale="Η ταχύτητα είναι ασφαλώς μη-σχετικιστική (v/c < 0.1), επιτρέποντας κλασική προσέγγιση.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Υπολογισμός μέτρου μαγνητικής δύναμης Lorentz F_B",
                    formula=r"F_B = |q| v B \sin\theta = e v B \sin(90^\circ) = e v B",
                    substitution=r"F_B = (1.602\times 10^{-19} \ \text{C}) \times (1.3262\times 10^7 \ \text{m/s}) \times (0.20 \ \text{T})",
                    result=r"F_B \approx 4.249\times 10^{-13} \ \text{N}",
                    rationale="Επειδή η ταχύτητα είναι κάθετη στο πεδίο (θ = 90°), η μαγνητική δύναμη λαμβάνει τη μέγιστη τιμή της.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Εξίσωση κεντρομόλου δύναμης για ομαλή κυκλική κίνηση",
                    formula=r"\Sigma F_r = m_e a_c \implies e v B = \frac{m_e v^2}{R}",
                    substitution=r"e B = \frac{m_e v}{R} \implies R = \frac{m_e v}{e B}",
                    result=r"R = \frac{m_e v}{e B}",
                    rationale="Η δύναμη Lorentz δρα αποκλειστικά ως κεντρομόλος, μεταβάλλοντας μόνο τη διεύθυνση της ταχύτητας.",
                ),
                CalculationStep(
                    step_number=5,
                    title="Αριθμητικός υπολογισμός ακτίνας κυκλοτρονικής τροχιάς R",
                    formula=r"R = \frac{m_e v}{e B}",
                    substitution=r"R = \frac{(9.109\times 10^{-31} \ \text{kg}) \times (1.3262\times 10^7 \ \text{m/s})}{(1.602\times 10^{-19} \ \text{C}) \times (0.20 \ \text{T})} = \frac{1.2080\times 10^{-23}}{3.204\times 10^{-20}} \approx 3.770\times 10^{-4} \ \text{m}",
                    result=r"R \approx 3.770\times 10^{-4} \ \text{m} = 0.377 \ \text{mm}",
                    rationale="Το ηλεκτρόνιο παγιδεύεται σε κυκλική τροχιά υπο-χιλιοστομετρικής ακτίνας.",
                ),
                CalculationStep(
                    step_number=6,
                    title="Υπολογισμός κυκλοτρονικής συχνότητας ω_c και περιόδου περιστροφής T_c",
                    formula=r"\omega_c = \frac{v}{R} = \frac{e B}{m_e}, \quad T_c = \frac{2\pi}{\omega_c}",
                    substitution=r"\omega_c = \frac{(1.602\times 10^{-19})(0.20)}{9.109\times 10^{-31}} \approx 3.517\times 10^{10} \ \text{rad/s}, \quad T_c = \frac{2\pi}{3.517\times 10^{10}} \approx 1.786\times 10^{-10} \ \text{s}",
                    result=r"\omega_c \approx 3.517\times 10^{10} \ \text{rad/s}, \quad T_c \approx 0.179 \ \text{ns}",
                    rationale="Η κυκλοτρονική συχνότητα είναι ανεξάρτητη της ταχύτητας και της ακτίνας (ισόχρονη περιστροφή).",
                ),
            ],
            final_answer=r"v \approx 1.33\times 10^7\text{ m/s}, \quad F_B \approx 4.25\times 10^{-13}\text{ N}, \quad R \approx 0.377\text{ mm}",
            detailed_justification="Η μαγνητική δύναμη δεν παράγει έργο, αλλά καμπυλώνει την τροχιά σε ομοιόμορφη κυκλική κίνηση.",
            common_pitfalls=["Προσοχή: η δύναμη είναι πάντα κάθετη στην ταχύτητα v, άρα το μέτρο της ταχύτητας παραμένει αυστηρά σταθερό."],
            related_theory_topic="Μαγνητική Δύναμη Lorentz & Κυκλότρον",
        ),
        ExamQuestion(
            question_number=7,
            title="Άσκηση 5: Επίπεδος Πυκνωτής με Διηλεκτρικό",
            question_type="Calculations",
            prompt_text=r"Επίπεδος πυκνωτής έχει οπλισμούς με εμβαδόν $A = 250\text{ cm}^2$ και απόσταση $d = 3\text{ mm}$. Α) Υπολογίστε $C_0$ στο κενό. Β) Εισάγεται διηλεκτρικό με $\kappa = 4.5$, υπολογίστε τη νέα χωρητικότητα $C$. Γ) Αν συνδεθεί σε πηγή $V = 100\text{ V}$, ποιο φορτίο $Q$ αποθηκεύεται; Δίνεται $\epsilon_0 = 8.854 \times 10^{-12}\text{ F/m}$.",
            given_parameters=[
                GivenParameter("A", "250 \\text{ cm}^2 = 0.025 \\text{ m}^2", "Εμβαδόν οπλισμών"),
                GivenParameter("d", "3 \\text{ mm} = 0.003 \\text{ m}", "Απόσταση οπλισμών"),
                GivenParameter(r"\kappa", "4.5", "Διηλεκτρική σταθερά"),
                GivenParameter("V", "100 \\text{ V}", "Εφαρμοζόμενη τάση"),
                GivenParameter(r"\epsilon_0", "8.854 \\times 10^{-12} \\text{ F/m}", "Διηλεκτρική σταθερά κενού"),
            ],
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Μετατροπή γεωμετρικών διαστάσεων σε μονάδες SI",
                    formula=r"A = 250 \ \text{cm}^2 \times 10^{-4} \ \text{m}^2/\text{cm}^2, \quad d = 3 \ \text{mm} \times 10^{-3} \ \text{m/mm}",
                    substitution=r"A = 250 \times 10^{-4} = 0.025 \ \text{m}^2, \quad d = 3\times 10^{-3} = 0.003 \ \text{m}",
                    result=r"A = 0.025 \ \text{m}^2, \quad d = 0.003 \ \text{m}",
                    rationale="Απαραίτητη μετατροπή για τη συμβατότητα με τις σταθερές SI.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Υπολογισμός χωρητικότητας στο κενό C_0",
                    formula=r"C_0 = \epsilon_0 \frac{A}{d}",
                    substitution=r"C_0 = (8.854\times 10^{-12} \ \text{F/m}) \times \frac{0.025 \ \text{m}^2}{0.003 \ \text{m}} = (8.854\times 10^{-12}) \times 8.3333",
                    result=r"C_0 \approx 7.3783 \times 10^{-11} \ \text{F} \approx 73.78 \ \text{pF}",
                    rationale="Χωρητικότητα επίπεδου πυκνωτή καθοριζόμενη αποκλειστικά από τη γεωμετρία στο κενό.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Υπολογισμός χωρητικότητας C με εισαγωγή διηλεκτρικού υλικού",
                    formula=r"C = \kappa C_0 = \epsilon_r C_0",
                    substitution=r"C = 4.5 \times (7.3783\times 10^{-11} \ \text{F}) \approx 3.3202\times 10^{-10} \ \text{F}",
                    result=r"C \approx 3.3202 \times 10^{-10} \ \text{F} \approx 332.02 \ \text{pF}",
                    rationale="Η πόλωση του διηλεκτρικού αυξάνει τη χωρητικότητα κατά συντελεστή κ = 4.5.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Υπολογισμός αποθηκευμένου ελεύθερου ηλεκτρικού φορτίου Q",
                    formula=r"Q = C V",
                    substitution=r"Q = (3.3202\times 10^{-10} \ \text{F}) \times (100 \ \text{V}) = 3.3202\times 10^{-8} \ \text{C}",
                    result=r"Q \approx 3.320 \times 10^{-8} \ \text{C} = 33.20 \ \text{nC}",
                    rationale="Σταθερή πηγή τάσης 100 V επιβάλλει αναλογική συσσώρευση φορτίου στους οπλισμούς.",
                ),
                CalculationStep(
                    step_number=5,
                    title="Υπολογισμός έντασης ηλεκτρικού πεδίου E εντός του διηλεκτρικού",
                    formula=r"E = \frac{V}{d}",
                    substitution=r"E = \frac{100 \ \text{V}}{0.003 \ \text{m}} = 3.3333\times 10^4 \ \text{V/m}",
                    result=r"E \approx 33.33 \ \text{kV/m}",
                    rationale="Εφόσον ο πυκνωτής παραμένει συνδεδεμένος στην πηγή, η τάση διατηρείται σταθερή και E = V/d.",
                ),
                CalculationStep(
                    step_number=6,
                    title="Υπολογισμός αποθηκευμένης ηλεκτροστατικής ενέργειας U_E",
                    formula=r"U_E = \frac{1}{2} C V^2 = \frac{1}{2} Q V",
                    substitution=r"U_E = \frac{1}{2} (3.3202\times 10^{-10} \ \text{F}) \times (100 \ \text{V})^2 = \frac{1}{2} (3.3202\times 10^{-10}) \times 10000",
                    result=r"U_E \approx 1.6601 \times 10^{-6} \ \text{J} = 1.660 \ \mu\text{J}",
                    rationale="Ηλεκτροστατική ενέργεια αποθηκευμένη στο πολωμένο διηλεκτρικό μέσο.",
                ),
            ],
            final_answer=r"C_0 \approx 73.78\text{ pF}, \quad C \approx 332.02\text{ pF}, \quad Q \approx 33.20\text{ nC}",
            detailed_justification="Η πόλωση του διηλεκτρικού υλικού επιτρέπει την αποθήκευση 4.5 φορές περισσότερου φορτίου για την ίδια τάση.",
            common_pitfalls=["Προσοχή στη μετατροπή cm² σε m²: 250 cm² = 250 × 10⁻⁴ m² = 0.025 m²."],
            related_theory_topic="Πυκνωτές & Διηλεκτρικά Υλικά",
        ),
    ]

    justifications = [
        DesignJustification(
            title="Κεντρομόλος Φύση Δύναμης Lorentz",
            category="Lorentz Law",
            description="Επειδή η μαγνητική δύναμη F = q(v × B) είναι πάντα κάθετη στο διάνυσμα ταχύτητας v, δεν παράγει έργο (W = 0) και μεταβάλλει μόνο την κατεύθυνση, εξαναγκάζοντας το σωματίδιο σε κυκλική τροχιά.",
            rationale="Θεμελιώδης αρχή σχεδιασμού επιταχυντών σωματιδίων και φασματογράφων μάζας.",
        ),
        DesignJustification(
            title="Τοπική Μορφή Νόμου Ohm (J = σ E)",
            category="Conduction Law",
            description="Σε αγώγιμο μέσο με ειδική αγωγιμότητα σ, η πυκνότητα ρεύματος είναι ανάλογη του τοπικού ηλεκτρικού πεδίου E.",
            rationale="Γεφυρώνει τη μικροσκοπική κίνηση των ηλεκτρονίων με τη μακροσκοπική αντίσταση του αγωγού.",
        ),
    ]

    solution_code = '''"""Python verification script for Practice Exam 1."""

import math

def verify_problems() -> None:
    """Verifies all computational exercises from Practice Exam 1."""
    # Problem 1: Plane EM wave
    c = 3e8
    mu_0 = 4 * math.pi * 1e-7
    E_0 = 5.0
    k = 7e12
    wavelength = 2 * math.pi / k
    omega = c * k
    f = omega / (2 * math.pi)
    T = 1 / f
    B_0 = E_0 / c
    S_max = (E_0 * B_0) / mu_0
    intensity = S_max / 2.0
    print("--- 1. Plane Wave ---")
    print(f"lambda = {wavelength:.4e} m, f = {f:.4e} Hz, I = {intensity*1000:.3f} mW/m^2")

    # Problem 2: Conductor
    sigma = 5.8e7
    r = 2e-3
    L = 50.0
    V = 10.0
    A = math.pi * r**2
    R = L / (sigma * A)
    I = V / R
    E = V / L
    J = sigma * E
    print("\\n--- 2. Conductor ---")
    print(f"R = {R:.5f} Ohm, I = {I:.2f} A, J = {J:.3e} A/m^2")

    # Problem 3: Parallel Wires
    d = 0.2
    I1 = 30.0
    I2 = 50.0
    B1 = (mu_0 * I1) / (2 * math.pi * d)
    force_per_len = (mu_0 * I1 * I2) / (2 * math.pi * d)
    print("\\n--- 3. Parallel Wires ---")
    print(f"B1 = {B1*1e6:.1f} uT, F/L = {force_per_len*1000:.2f} mN/m")

    # Problem 4: Electron in B-field
    e = 1.6e-19
    m = 9.11e-31
    V0 = 500.0
    B_field = 0.2
    v = math.sqrt(2 * e * V0 / m)
    F_B = e * v * B_field
    R_orbit = (m * v) / (e * B_field)
    print("\\n--- 4. Electron in B-Field ---")
    print(f"v = {v:.3e} m/s, F_B = {F_B:.3e} N, R = {R_orbit*1000:.3f} mm")

    # Problem 5: Capacitor
    eps_0 = 8.854e-12
    A_cap = 250e-4
    d_cap = 3e-3
    kappa = 4.5
    C0 = eps_0 * A_cap / d_cap
    C = kappa * C0
    Q = C * 100.0
    print("\\n--- 5. Capacitor ---")
    print(f"C0 = {C0*1e12:.2f} pF, C = {C*1e12:.2f} pF, Q = {Q*1e9:.2f} nC")

if __name__ == "__main__":
    verify_problems()
'''

    return Scenario(
        id="synth_exam_1_comprehensive",
        title="Θέμα Εξάσκησης 1 — Πλήρης Επισκόπηση Ηλεκτρομαγνητισμού",
        subtitle="Πλήρης Επίλυση: Kirchhoff, Αγωγοί, Δυνάμεις Lorentz, Πυκνωτές & ΗΜ Κύμα",
        course_tag="Practice Exam 01",
        duration_info="Διάρκεια: 2.5 ώρες | 8 Ερωτήσεις Θεωρίας & 5 Ασκήσεις Υπολογισμού",
        paragraphs=paragraphs,
        questions=questions,
        justifications=justifications,
        solution_code=solution_code,
    )

