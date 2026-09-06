"""Methodology quick-guide 4-step cards component for Electromagnetics."""

from nicegui import ui


def renderMethodologyCards() -> None:
    """Renders the 4-step methodology cards guiding students through EM problem solving.

    Returns:
        None
    """
    with ui.column().classes("w-full glass-panel gap-4 no-print"):
        with ui.row().classes("items-center gap-3"):
            ui.html('<i class="fa-solid fa-compass text-[var(--accent)] text-xl"></i>')
            ui.html('<h2 class="text-xl font-bold text-[var(--text-1)] m-0">Μεθοδολογία Επίλυσης Θεμάτων ΗΜ (Βήμα-Βήμα)</h2>')

        with ui.grid().classes("grid-cols-1 md:grid-cols-4 gap-4 w-full"):
            # Step 1: Coordinate Systems & Symmetry
            with ui.column().classes(
                "p-4 rounded-xl bg-[var(--card-bg-subtle)] border-l-4 border-blue-500 border border-[var(--border)] gap-1 shadow-sm"
            ):
                with ui.row().classes("items-center gap-2"):
                    ui.html('<i class="fa-solid fa-shapes text-blue-500 text-sm"></i>')
                    ui.label("1. Συντεταγμένες & Συμμετρίες").classes("font-bold text-blue-600 dark:text-blue-300 text-sm")
                ui.label(
                    "Εντοπίζουμε τη γεωμετρία (Καρτεσιανή, Κυλινδρική, Σφαιρική) και τις κατευθύνσεις των αξόνων "
                    "x, y, z για την επιλογή των κατάλληλων μοναδιαίων διανυσμάτων."
                ).classes("text-xs text-[var(--text-2)] leading-relaxed")

            # Step 2: Maxwell Differential Mapping
            with ui.column().classes(
                "p-4 rounded-xl bg-[var(--card-bg-subtle)] border-l-4 border-emerald-500 border border-[var(--border)] gap-1 shadow-sm"
            ):
                with ui.row().classes("items-center gap-2"):
                    ui.html('<i class="fa-solid fa-calculator text-emerald-500 text-sm"></i>')
                    ui.label("2. Διαφορικοί Τελεστές Maxwell").classes("font-bold text-emerald-600 dark:text-emerald-300 text-sm")
                ui.label(
                    "Εφαρμόζουμε την απόκλιση Gauss div(D) = rho για εύρεση φορτίων ή τον στροβιλισμό curl(E) "
                    "και curl(H) για νόμους Faraday και Ampère."
                ).classes("text-xs text-[var(--text-2)] leading-relaxed")

            # Step 3: Harmonic Wave Vector Analysis
            with ui.column().classes(
                "p-4 rounded-xl bg-[var(--card-bg-subtle)] border-l-4 border-amber-500 border border-[var(--border)] gap-1 shadow-sm"
            ):
                with ui.row().classes("items-center gap-2"):
                    ui.html('<i class="fa-solid fa-wave-square text-amber-500 text-sm"></i>')
                    ui.label("3. Ανάλυση Επιπέδου Κύματος").classes("font-bold text-amber-600 dark:text-amber-300 text-sm")
                ui.label(
                    "Απομονώνουμε κυματάριθμο k, συχνότητα omega και διεύθυνση διάδοσης. Συνδέουμε τα πεδία μέσω "
                    "E0 = c B0 και του δεξιόστροφου τριέδρου (E, B, k)."
                ).classes("text-xs text-[var(--text-2)] leading-relaxed")

            # Step 4: Energy Flux & Poynting Vector
            with ui.column().classes(
                "p-4 rounded-xl bg-[var(--card-bg-subtle)] border-l-4 border-rose-500 border border-[var(--border)] gap-1 shadow-sm"
            ):
                with ui.row().classes("items-center gap-2"):
                    ui.html('<i class="fa-solid fa-bolt text-rose-500 text-sm"></i>')
                    ui.label("4. Ροή Ενέργειας & Ένταση").classes("font-bold text-rose-600 dark:text-rose-300 text-sm")
                ui.label(
                    "Υπολογίζουμε το εξωτερικό γινόμενο S = (1/mu0) (E x B) και τη μέση ένταση ακτινοβολίας "
                    "I = <S> = (1/2) c eps0 E0^2."
                ).classes("text-xs text-[var(--text-2)] leading-relaxed")

