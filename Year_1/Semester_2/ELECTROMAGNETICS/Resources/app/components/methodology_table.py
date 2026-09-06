"""Comprehensive methodology table component for Electromagnetics problem patterns."""

from nicegui import ui


def renderMethodologyTable() -> None:
    """Renders the comprehensive reference table mapping textual patterns to EM formulas.

    Returns:
        None
    """
    with ui.column().classes("w-full glass-panel gap-4 no-print"):
        with ui.row().classes("items-center gap-3"):
            ui.html('<i class="fa-solid fa-table text-[var(--accent)] text-xl"></i>')
            ui.html('<h2 class="text-xl md:text-2xl font-bold text-[var(--text-1)] m-0">Πίνακας Αναγνώρισης Προβλημάτων & Μεθοδολογίας</h2>')

        ui.label(
            "Χρησιμοποιήστε τον παρακάτω πίνακα για άμεση αντιστοίχιση των δεδομένων της εκφώνησης στις εξισώσεις επίλυσης:"
        ).classes("text-xs text-[var(--text-2)]")

        table_content = """
        <div class="overflow-x-auto w-full">
            <table class="dark-table shadow-sm">
                <thead>
                    <tr>
                        <th style="width: 22%;">Τύπος Προβλήματος</th>
                        <th style="width: 28%;">Λέξεις-Κλειδιά & Αναγνώριση</th>
                        <th style="width: 28%;">Θεμελιώδεις Εξισώσεις</th>
                        <th style="width: 22%;">Συνήθεις Παγίδες / Προσοχή</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td class="font-bold text-blue-600 dark:text-blue-300">
                            <i class="fa-solid fa-calculator mr-1 text-blue-500"></i> Νόμος Gauss (Διαφορικός)
                        </td>
                        <td>
                            Δίνεται διάνυσμα $\\vec{D}$ και ζητείται η πυκνότητα φορτίου $\\rho$.
                        </td>
                        <td>
                            $$\\rho = \\vec{\\nabla} \\cdot \\vec{D} = \\frac{\\partial D_x}{\\partial x} + \\frac{\\partial D_y}{\\partial y} + \\frac{\\partial D_z}{\\partial z}$$
                        </td>
                        <td>
                            Παράγωγος σταθεράς είναι $0$. Μην ξεχνάτε τον κανόνα παραγώγισης πηλίκου $\\frac{d}{dy}(\\frac{1}{y}) = -\\frac{1}{y^2}$.
                        </td>
                    </tr>
                    <tr>
                        <td class="font-bold text-amber-600 dark:text-amber-300">
                            <i class="fa-solid fa-wave-square mr-1 text-amber-500"></i> Επίπεδο ΗΜ Κύμα
                        </td>
                        <td>
                            Ημιτονοειδής μορφή $\\vec{E} = E_0\\cos(kz - \\omega t)\\hat{u}$.
                        </td>
                        <td>
                            $$k = \\frac{2\\pi}{\\lambda}, \\quad \\omega = 2\\pi f, \\quad c = \\lambda f = \\frac{\\omega}{k}$$
                            $$E_0 = c B_0, \\quad \\hat{k} = \\hat{E} \\times \\hat{B}$$
                        </td>
                        <td>
                            Πρόσημο φάσης: $(kz - \\omega t) \\implies +z$ διάδοση, ενώ $(kz + \\omega t) \\implies -z$ διάδοση.
                        </td>
                    </tr>
                    <tr>
                        <td class="font-bold text-rose-600 dark:text-rose-300">
                            <i class="fa-solid fa-bolt mr-1 text-rose-500"></i> Διάνυσμα Poynting & Ένταση
                        </td>
                        <td>
                            Υπολογισμός στιγμιαίας και μέσης ροής ηλεκτρομαγνητικής ισχύος.
                        </td>
                        <td>
                            $$\\vec{S} = \\frac{1}{\\mu_0} \\vec{E} \\times \\vec{B}$$
                            $$I = \\bar{S} = \\frac{1}{2} c \\epsilon_0 E_0^2 = \\frac{E_0^2}{2\\mu_0 c}$$
                        </td>
                        <td>
                            Το $\\vec{S}$ ταλαντώνεται με διπλάσια συχνότητα $\\cos^2(...)$. Η χρονική μέση τιμή του $\\cos^2$ ισούται με $1/2$.
                        </td>
                    </tr>
                    <tr>
                        <td class="font-bold text-emerald-600 dark:text-emerald-300">
                            <i class="fa-solid fa-magnet mr-1 text-emerald-500"></i> Δυνάμεις Lorentz & Αγωγών
                        </td>
                        <td>
                            Κινούμενο φορτίο σε $\\vec{B}$ ή παράλληλοι ρευματοφόροι αγωγοί.
                        </td>
                        <td>
                            $$\\vec{F} = q(\\vec{E} + \\vec{v} \\times \\vec{B}), \\quad R = \\frac{mv}{qB}$$
                            $$\\frac{F}{L} = \\frac{\\mu_0 I_1 I_2}{2\\pi d}$$
                        </td>
                        <td>
                            Ομόρροπα ρεύματα έλκονται, αντίρροπα απωθούνται. Ακίνητο φορτίο δεν δέχεται μαγνητική δύναμη.
                        </td>
                    </tr>
                    <tr>
                        <td class="font-bold text-purple-600 dark:text-purple-300">
                            <i class="fa-solid fa-layer-group mr-1 text-purple-500"></i> Πυκνωτές & Διηλεκτρικά
                        </td>
                        <td>
                            Επίπεδοι ή κυλινδρικοί οπλισμοί με διηλεκτρικό $\\kappa$ ή $\\epsilon_r$.
                        </td>
                        <td>
                            $$C = \\kappa \\epsilon_0 \\frac{A}{d}, \\quad Q = C V, \\quad U = \\frac{1}{2} C V^2$$
                        </td>
                        <td>
                            Το διηλεκτρικό αυξάνει πάντα τη χωρητικότητα ($\\kappa > 1$). Στο εσωτερικό αγωγού σε ισορροπία $\\vec{E} = 0$.
                        </td>
                    </tr>
                    <tr>
                        <td class="font-bold text-teal-600 dark:text-teal-300">
                            <i class="fa-solid fa-arrows-split-up-and-left mr-1 text-teal-500"></i> Ανάκλαση & Διάθλαση Snell
                        </td>
                        <td>
                            Μετάβαση ακτίνας φωτός ανάμεσα σε δύο διαφανή οπτικά μέσα.
                        </td>
                        <td>
                            $$n_1 \\sin\\theta_1 = n_2 \\sin\\theta_2, \\quad \\sin\\theta_c = \\frac{n_2}{n_1} \\ (n_1 > n_2)$$
                        </td>
                        <td>
                            Η συχνότητα $f$ παραμένει αναλλοίωτη κατά τη διάθλαση. Ολική ανάκλαση συμβαίνει μόνο από πυκνότερο σε αραιότερο μέσο.
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
        """
        ui.html(table_content)

