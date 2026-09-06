"""Comprehensive Master Theory Guide component for Electromagnetics curriculum."""

from nicegui import ui
from config import renderMathHtml


def renderTheoryPage() -> None:
    """Renders the comprehensive, self-contained Electromagnetics educational handbook.

    Returns:
        None
    """
    with ui.column().classes("w-full max-w-6xl mx-auto px-4 py-8 space-y-10 latex-target").props('id="theory-guide-container"'):
        # Title Hero
        with ui.column().classes("w-full glass-panel gap-3 p-8 border border-[var(--border-accent)]"):
            with ui.row().classes("items-center gap-3"):
                ui.html('<i class="fa-solid fa-atom text-[var(--accent)] text-3xl"></i>')
                with ui.column().classes("gap-1"):
                    ui.html('<h1 class="gradient-title text-2xl md:text-3xl font-black m-0">Εγχειρίδιο Θεωρίας Ηλεκτρομαγνητισμού & Τηλεπικοινωνιών</h1>')
                    ui.label("Πλήρες αναλυτικό σύγγραμμα: Διανυσματικός Λογισμός, Εξισώσεις Maxwell, ΗΜ Κύματα, Γραμμές Μεταφοράς και Χάρτης Smith.").classes("text-sm text-[var(--text-2)]")

        # SECTION 1: Vector Calculus & Differential Operators
        with ui.column().classes("w-full glass-panel gap-4 p-6 border border-[var(--border)]"):
            with ui.row().classes("items-center gap-3 pb-2 border-b border-[var(--border)]"):
                ui.html('<i class="fa-solid fa-calculator text-[var(--accent)] text-xl"></i>')
                ui.html('<h2 class="section-title m-0">1. Διανυσματικός Λογισμός & Διαφορικοί Τελεστές</h2>')

            section_1_text = r"""
Ο τελεστής **Ανάδελτα ($\nabla$)** σε Καρτεσιανές συντεταγμένες $(x, y, z)$ ορίζεται ως:
$$\nabla = \hat{x}\frac{\partial}{\partial x} + \hat{y}\frac{\partial}{\partial y} + \hat{z}\frac{\partial}{\partial z}$$

### 1.1 Κλίση Βαθμωτού Πεδίου (Gradient)
Συνδέει ένα βαθμωτό δυναμικό $V$ με ένα διανυσματικό πεδίο μέγιστου ρυθμού μεταβολής:
$$\nabla V = \frac{\partial V}{\partial x}\hat{x} + \frac{\partial V}{\partial y}\hat{y} + \frac{\partial V}{\partial z}\hat{z}$$
*Φυσική εφαρμογή:* Στην ηλεκτροστατική, η ένταση του πεδίου είναι η αρνητική κλίση του δυναμικού: $\vec{E} = -\nabla V$.

### 1.2 Απόκλιση Διανυσματικού Πεδίου (Divergence)
Εκφράζει την πυκνότητα ροής που πηγάζει από ή συγκλίνει σε ένα στοιχειώδες σημείο:
$$\nabla \cdot \vec{A} = \frac{\partial A_x}{\partial x} + \frac{\partial A_y}{\partial y} + \frac{\partial A_z}{\partial z}$$
*Φυσική εφαρμογή:* Νόμος του Gauss $\nabla \cdot \vec{D} = \rho_v$. Όταν $\nabla \cdot \vec{A} = 0$, το πεδίο ονομάζεται **σωληνοειδές** (ασυμπίεστο), όπως το $\vec{B}$.

### 1.3 Στροβιλισμός (Curl)
Μετρά την τάση ενός διανύσματος να περιστρέφεται γύρω από ένα σημείο:
$$\nabla \times \vec{A} = \begin{vmatrix} \hat{x} & \hat{y} & \hat{z} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ A_x & A_y & A_z \end{vmatrix} = \left(\frac{\partial A_z}{\partial y} - \frac{\partial A_y}{\partial z}\right)\hat{x} + \left(\frac{\partial A_x}{\partial z} - \frac{\partial A_z}{\partial x}\right)\hat{y} + \left(\frac{\partial A_y}{\partial x} - \frac{\partial A_x}{\partial y}\right)\hat{z}$$
*Φυσική εφαρμογή:* Νόμος Faraday $\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}$ και νόμος Ampère $\nabla \times \vec{H} = \vec{J} + \frac{\partial \vec{D}}{\partial t}$.

### 1.4 Θεμελιώδη Θεωρήματα Ολοκλήρωσης
- **Θεώρημα Gauss (Απόκλισης):** Μετατροπή όγκου σε κλειστή επιφάνεια:
  $$\iiint_V (\nabla \cdot \vec{A}) \, dV = \oiint_S \vec{A} \cdot d\vec{S}$$
- **Θεώρημα Stokes:** Μετατροπή επιφάνειας σε κλειστό περίγραμμα:
  $$\iint_S (\nabla \times \vec{A}) \cdot d\vec{S} = \oint_C \vec{A} \cdot d\vec{l}$$
"""
            ui.html(f'<div class="text-sm text-[var(--text-1)] leading-relaxed latex-target">{renderMathHtml(section_1_text)}</div>')

        # SECTION 2: The 4 Maxwell Equations
        with ui.column().classes("w-full glass-panel gap-4 p-6 border border-[var(--border)]"):
            with ui.row().classes("items-center gap-3 pb-2 border-b border-[var(--border)]"):
                ui.html('<i class="fa-solid fa-scale-balanced text-[var(--accent)] text-xl"></i>')
                ui.html('<h2 class="section-title m-0">2. Οι Τέσσερις Θεμελιώδεις Εξισώσεις Maxwell</h2>')

            table_maxwell = """
            <div class="overflow-x-auto w-full">
                <table class="dark-table shadow-sm">
                    <thead>
                        <tr>
                            <th>Ονομασία Νόμου</th>
                            <th>Διαφορική Μορφή</th>
                            <th>Ολοκληρωτική Μορφή</th>
                            <th>Φυσική Ερμηνεία & Σημασία</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="font-bold text-blue-600 dark:text-blue-300">Gauss (Ηλεκτρισμός)</td>
                            <td>$$\\nabla \\cdot \\vec{D} = \\rho_v$$</td>
                            <td>$$\\oiint_S \\vec{D} \\cdot d\\vec{S} = Q_{\\text{enc}}$$</td>
                            <td>Πηγές και καταβόθρες του ηλεκτρικού πεδίου είναι τα ελεύθερα ηλεκτρικά φορτία. Οι δυναμικές γραμμές είναι ανοικτές.</td>
                        </tr>
                        <tr>
                            <td class="font-bold text-orange-600 dark:text-orange-300">Gauss (Μαγνητισμός)</td>
                            <td>$$\\nabla \\cdot \\vec{B} = 0$$</td>
                            <td>$$\\oiint_S \\vec{B} \\cdot d\\vec{S} = 0$$</td>
                            <td>Δεν υπάρχουν απομονωμένα μαγνητικά μονόπολα. Οι μαγνητικές δυναμικές γραμμές είναι πάντα κλειστοί βρόχοι.</td>
                        </tr>
                        <tr>
                            <td class="font-bold text-emerald-600 dark:text-emerald-300">Faraday (Επαγωγή)</td>
                            <td>$$\\nabla \\times \\vec{E} = -\\frac{\\partial \\vec{B}}{\\partial t}$$</td>
                            <td>$$\\oint_C \\vec{E} \\cdot d\\vec{l} = -\\frac{d\\Phi_B}{dt}$$</td>
                            <td>Ένα χρονικά μεταβαλλόμενο μαγνητικό πεδίο επάγει ένα στροβιλιζόμενο ηλεκτρικό πεδίο (αρχή λειτουργίας γεννητριών).</td>
                        </tr>
                        <tr>
                            <td class="font-bold text-purple-600 dark:text-purple-300">Ampère-Maxwell</td>
                            <td>$$\\nabla \\times \\vec{H} = \\vec{J} + \\frac{\\partial \\vec{D}}{\\partial t}$$</td>
                            <td>$$\\oint_C \\vec{H} \\cdot d\\vec{l} = I_{\\text{enc}} + \\frac{d\\Phi_D}{dt}$$</td>
                            <td>Μαγνητικό πεδίο παράγεται τόσο από ρεύματα αγωγιμότητας $J$ όσο και από μεταβαλλόμενο ηλεκτρικό πεδίο (ρεύμα μετατόπισης).</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            """
            ui.html(table_maxwell)

            section_2_text = r"""
### Καταστατικές Σχέσεις Γραμμικών Ισότροπων Μέσων
- $\vec{D} = \epsilon \vec{E} = \epsilon_0 \epsilon_r \vec{E}$
- $\vec{B} = \mu \vec{H} = \mu_0 \mu_r \vec{H}$
- $\vec{J} = \sigma \vec{E}$ (Νόμος του Ohm σε τοπική/διαφορική μορφή)

Όπου:
- $\epsilon_0 \approx 8.854 \times 10^{-12} \text{ F/m}$ (διηλεκτρική σταθερά κενού)
- $\mu_0 = 4\pi \times 10^{-7} \text{ T}\cdot\text{m/A} \approx 1.257 \times 10^{-6} \text{ H/m}$ (μαγνητική διαπερατότητα κενού)
- $c = \frac{1}{\sqrt{\epsilon_0 \mu_0}} \approx 3 \times 10^8 \text{ m/s}$ (ταχύτητα φωτός στο κενό)
"""
            ui.html(f'<div class="text-sm text-[var(--text-1)] leading-relaxed latex-target">{renderMathHtml(section_2_text)}</div>')

        # SECTION 3: Harmonic Plane Waves & Poynting Vector
        with ui.column().classes("w-full glass-panel gap-4 p-6 border border-[var(--border)]"):
            with ui.row().classes("items-center gap-3 pb-2 border-b border-[var(--border)]"):
                ui.html('<i class="fa-solid fa-wave-square text-[var(--accent)] text-xl"></i>')
                ui.html('<h2 class="section-title m-0">3. Επίπεδα Ηλεκτρομαγνητικά Κύματα & Διάνυσμα Poynting</h2>')

            section_3_text = r"""
### 3.1 Εξίσωση Κύματος & Μορφή Πεδίων
Για αρμονικό κύμα πολωμένο κατά $\hat{y}$ που διαδίδεται προς τη διεύθυνση $+z$ στο κενό:
$$\vec{E}(z, t) = E_0 \cos(kz - \omega t)\hat{y}$$
$$\vec{B}(z, t) = B_0 \cos(kz - \omega t)(-\hat{x}) \quad \text{ή κατάλληλος άξονας ώστε } \hat{E} \times \hat{B} = \hat{k}$$

- **Σχέση Πλατών:** $E_0 = c B_0$.
- **Κυματάριθμος & Συχνότητα:** $k = \frac{2\pi}{\lambda}$, $\omega = 2\pi f$, $c = \lambda f = \frac{\omega}{k}$.
- **Εγγενής Εμπέδηση Κενού:**
  $$\eta_0 = \sqrt{\frac{\mu_0}{\epsilon_0}} \approx 120\pi \ \Omega \approx 376.73\ \Omega$$

### 3.2 Διάνυσμα Poynting & Ένταση Ακτινοβολίας
Το διάνυσμα Poynting εκφράζει την πυκνότητα ροής ισχύος (ισχύς ανά μονάδα επιφάνειας, $\text{W/m}^2$):
$$\vec{S} = \vec{E} \times \vec{H} = \frac{1}{\mu_0} (\vec{E} \times \vec{B})$$

Επειδή $\vec{E}$ και $\vec{B}$ ταλαντώνονται με $\cos(kz - \omega t)$:
$$\vec{S}(z, t) = \frac{E_0 B_0}{\mu_0} \cos^2(kz - \omega t) \hat{k}$$

Η **χρονική μέση τιμή** του $\cos^2$ σε μία περίοδο ισούται με $1/2$. Συνεπώς, η μέση ένταση ακτινοβολίας $I$ δίνεται από:
$$I = \langle |\vec{S}| \rangle = \frac{E_0 B_0}{2\mu_0} = \frac{E_0^2}{2\mu_0 c} = \frac{1}{2} c \epsilon_0 E_0^2 = \frac{E_0^2}{2\eta_0}$$
"""
            ui.html(f'<div class="text-sm text-[var(--text-1)] leading-relaxed latex-target">{renderMathHtml(section_3_text)}</div>')

        # SECTION 4: Transmission Lines & Smith Chart
        with ui.column().classes("w-full glass-panel gap-4 p-6 border border-[var(--border)]"):
            with ui.row().classes("items-center gap-3 pb-2 border-b border-[var(--border)]"):
                ui.html('<i class="fa-solid fa-network-wired text-[var(--accent)] text-xl"></i>')
                ui.html('<h2 class="section-title m-0">4. Γραμμές Μεταφοράς & Χάρτης Smith</h2>')

            section_4_text = r"""
### 4.1 Μοντέλο Κατανεμημένων Στοιχείων
Μια ομοιόμορφη γραμμή μεταφοράς περιγράφεται από παραμέτρους ανά μονάδα μήκους: Αντίσταση $R'$, Αυτεπαγωγή $L'$, Αγωγιμότητα $G'$, Χωρητικότητα $C'$.
Για **γραμμή χωρίς απώλειες** ($R' = 0, G' = 0$):
- **Χαρακτηριστική Εμπέδηση:** $Z_0 = \sqrt{\frac{L'}{C'}}$ (καθαρά πραγματική).
- **Ταχύτητα Διάδοσης:** $v_p = \frac{1}{\sqrt{L'C'}} = \frac{c}{\sqrt{\epsilon_r}}$.
- **Σταθερά Φάσης:** $\beta = \omega \sqrt{L'C'} = \frac{2\pi}{\lambda}$.

### 4.2 Συντελεστής Ανάκλασης ($\Gamma$) & Λόγος Στασίμων (VSWR)
Όταν μια γραμμή με χαρακτηριστική εμπέδηση $Z_0$ τερματίζεται σε φορτίο $Z_L$:
$$\Gamma_L = \frac{Z_L - Z_0}{Z_L + Z_0} = |\Gamma_L| e^{j\theta_L}$$

- **Πλήρης Προσαρμογή ($Z_L = Z_0$):** $\Gamma_L = 0$, κανένα στάσιμο κύμα.
- **Βραχυκύκλωμα ($Z_L = 0$):** $\Gamma_L = -1$.
- **Ανοικτοκύκλωμα ($Z_L = \infty$):** $\Gamma_L = +1$.

Ο **Λόγος Στάσιμων Κυμάτων Τάσης (VSWR)** ορίζεται ως:
$$\text{VSWR} = \frac{V_{\text{max}}}{V_{\text{min}}} = \frac{1 + |\Gamma_L|}{1 - |\Gamma_L|}, \quad 1 \le \text{VSWR} < \infty$$

### 4.3 Εμπέδηση Εισόδου σε Απόσταση $l$ από το Φορτίο
$$Z_{\text{in}}(l) = Z_0 \frac{Z_L + j Z_0 \tan(\beta l)}{Z_0 + j Z_L \tan(\beta l)}$$
*Ειδική περίπτωση $\lambda/4$ (Μετασχηματιστής Τετάρτου Κύματος):* $Z_{\text{in}}(\lambda/4) = \frac{Z_0^2}{Z_L}$.
"""
            ui.html(f'<div class="text-sm text-[var(--text-1)] leading-relaxed latex-target">{renderMathHtml(section_4_text)}</div>')

        # SECTION 5: Notation, Constants & Symbolism
        with ui.column().classes("w-full glass-panel gap-4 p-6 border border-[var(--border)]"):
            with ui.row().classes("items-center gap-3 pb-2 border-b border-[var(--border)]"):
                ui.html('<i class="fa-solid fa-list-check text-[var(--accent)] text-xl"></i>')
                ui.html('<h2 class="section-title m-0">5. Πίνακας Συμβολισμών, Μονάδων & Φυσικών Σταθερών</h2>')

            table_constants = """
            <div class="overflow-x-auto w-full">
                <table class="dark-table shadow-sm">
                    <thead>
                        <tr>
                            <th>Μέγεθος / Σύμβολο</th>
                            <th>Ονομασία & Περιγραφή</th>
                            <th>Μονάδα SI</th>
                            <th>Τυπική Τιμή / Τύπος Ορισμού</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="font-mono font-bold text-blue-500">$$\\vec{E}$$</td>
                            <td>Ένταση Ηλεκτρικού Πεδίου</td>
                            <td>$$\\text{V/m}$$ ή $$\\text{N/C}$$</td>
                            <td>$$\\vec{E} = -\\nabla V - \\frac{\\partial \\vec{A}}{\\partial t}$$</td>
                        </tr>
                        <tr>
                            <td class="font-mono font-bold text-blue-500">$$\\vec{D}$$</td>
                            <td>Διηλεκτρική Μετατόπιση (Πυκνότητα Ροής)</td>
                            <td>$$\\text{C/m}^2$$</td>
                            <td>$$\\vec{D} = \\epsilon_0 \\vec{E} + \\vec{P} = \\epsilon \\vec{E}$$</td>
                        </tr>
                        <tr>
                            <td class="font-mono font-bold text-orange-500">$$\\vec{B}$$</td>
                            <td>Μαγνητική Επαγωγή (Πυκνότητα Μαγνητικής Ροής)</td>
                            <td>$$\\text{Tesla (T)}$$ ή $$\\text{Wb/m}^2$$</td>
                            <td>$$\\vec{B} = \\nabla \\times \\vec{A}$$</td>
                        </tr>
                        <tr>
                            <td class="font-mono font-bold text-orange-500">$$\\vec{H}$$</td>
                            <td>Ένταση Μαγνητικού Πεδίου</td>
                            <td>$$\\text{A/m}$$</td>
                            <td>$$\\vec{B} = \\mu \\vec{H}$$</td>
                        </tr>
                        <tr>
                            <td class="font-mono font-bold text-emerald-500">$$c$$</td>
                            <td>Ταχύτητα Διάδοσης Φωτός στο Κενό</td>
                            <td>$$\\text{m/s}$$</td>
                            <td>$$2.99792458 \\times 10^8 \\approx 3 \\times 10^8 \\text{ m/s}$$</td>
                        </tr>
                        <tr>
                            <td class="font-mono font-bold text-emerald-500">$$\\mu_0$$</td>
                            <td>Μαγνητική Διαπερατότητα Κενού</td>
                            <td>$$\\text{T}\\cdot\\text{m/A}$$ ή $$\\text{H/m}$$</td>
                            <td>$$4\\pi \\times 10^{-7} \\approx 1.2566 \\times 10^{-6} \\text{ H/m}$$</td>
                        </tr>
                        <tr>
                            <td class="font-mono font-bold text-emerald-500">$$\\epsilon_0$$</td>
                            <td>Διηλεκτρική Σταθερά Κενού</td>
                            <td>$$\\text{F/m}$$</td>
                            <td>$$8.8541878 \\times 10^{-12} \\text{ F/m}$$</td>
                        </tr>
                        <tr>
                            <td class="font-mono font-bold text-purple-500">$$\\eta_0$$</td>
                            <td>Εγγενής Κυματική Εμπέδηση Κενού</td>
                            <td>$$\\Omega$$</td>
                            <td>$$\\sqrt{\\mu_0 / \\epsilon_0} \\approx 120\\pi \\approx 376.73 \\ \\Omega$$</td>
                        </tr>
                        <tr>
                            <td class="font-mono font-bold text-rose-500">$$\\vec{S}$$</td>
                            <td>Διάνυσμα Poynting (Ροή Ισχύος)</td>
                            <td>$$\\text{W/m}^2$$</td>
                            <td>$$\\vec{S} = \\frac{1}{\\mu_0} (\\vec{E} \\times \\vec{B})$$</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            """
            ui.html(table_constants)

