"""Methodology quick-guide 4-step cards component."""

from nicegui import ui


def renderMethodologyCards() -> None:
    """Renders the 4-step methodology cards for analyzing any networks exam problem.

    Returns:
        None
    """
    with ui.column().classes("w-full glass-panel gap-4 no-print"):
        with ui.row().classes("items-center gap-3"):
            ui.html('<i class="fa-solid fa-compass text-[var(--accent)] text-xl"></i>')
            ui.html('<h2 class="text-xl font-bold text-[var(--text-1)] m-0">Πώς Λύνουμε Οποιοδήποτε Θέμα Δικτύων (Βήμα-Βήμα)</h2>')

        with ui.grid().classes("grid-cols-1 md:grid-cols-4 gap-4 w-full"):
            # Step 1: Read and classify the question
            with ui.column().classes(
                "p-4 rounded-xl bg-[var(--card-bg-subtle)] border-l-4 border-blue-500 border border-[var(--border)] gap-1 shadow-sm"
            ):
                with ui.row().classes("items-center gap-2"):
                    ui.html('<i class="fa-solid fa-book-open-reader text-blue-500 text-sm"></i>')
                    ui.label("1. Ανάγνωση & Ταξινόμηση").classes("font-bold text-blue-600 dark:text-blue-300 text-sm")
                ui.label(
                    "Εντοπίζουμε το πεδίο του θέματος (υποδικτύωση, κατάτμηση, δρομολόγηση, "
                    "έλεγχος ροής/συμφόρησης) και τι ακριβώς ζητείται: θεωρία, σύγκριση ή αριθμητικό αποτέλεσμα."
                ).classes("text-xs text-[var(--text-2)] leading-relaxed")

            # Step 2: Extract the given parameters
            with ui.column().classes(
                "p-4 rounded-xl bg-[var(--card-bg-subtle)] border-l-4 border-amber-500 border border-[var(--border)] gap-1 shadow-sm"
            ):
                with ui.row().classes("items-center gap-2"):
                    ui.html('<i class="fa-solid fa-list-check text-amber-500 text-sm"></i>')
                    ui.label("2. Εξαγωγή Δεδομένων").classes("font-bold text-amber-600 dark:text-amber-300 text-sm")
                ui.label(
                    "Καταγράφουμε κάθε δοσμένη παράμετρο (δίκτυο/πρόθεμα, hosts, MTU, MSS, ssthresh, "
                    "RTT, κόστη ζεύξεων) και ελέγχουμε τις συμπληρωματικές παραδοχές (π.χ. επικεφαλίδα 20 bytes)."
                ).classes("text-xs text-[var(--text-2)] leading-relaxed")

            # Step 3: Apply the matching method
            with ui.column().classes(
                "p-4 rounded-xl bg-[var(--card-bg-subtle)] border-l-4 border-purple-500 border border-[var(--border)] gap-1 shadow-sm"
            ):
                with ui.row().classes("items-center gap-2"):
                    ui.html('<i class="fa-solid fa-square-root-variable text-purple-500 text-sm"></i>')
                    ui.label("3. Εφαρμογή Μεθόδου / Τύπου").classes("font-bold text-purple-600 dark:text-purple-300 text-sm")
                ui.label(
                    "Επιλέγουμε τον τύπο ή τον αλγόριθμο από τον πίνακα αναγνώρισης: \\(2^h - 2\\) για hosts, "
                    "Bitwise AND για δίκτυο, βήμα block για εύρος, Dijkstra για Link-State, AIMD για συμφόρηση."
                ).classes("text-xs text-[var(--text-2)] leading-relaxed")

            # Step 4: Verify and present
            with ui.column().classes(
                "p-4 rounded-xl bg-[var(--card-bg-subtle)] border-l-4 border-emerald-500 border border-[var(--border)] gap-1 shadow-sm"
            ):
                with ui.row().classes("items-center gap-2"):
                    ui.html('<i class="fa-solid fa-clipboard-check text-emerald-500 text-sm"></i>')
                    ui.label("4. Επαλήθευση & Παρουσίαση").classes("font-bold text-emerald-600 dark:text-emerald-300 text-sm")
                ui.label(
                    "Ελέγχουμε το αποτέλεσμα (άθροισμα εύρους + broadcast = block, offsets πολλαπλάσια του 8, "
                    "σύγκλιση Dijkstra) και παρουσιάζουμε βήμα-βήμα με πίνακες και τελικό πλαίσιο απάντησης."
                ).classes("text-xs text-[var(--text-2)] leading-relaxed")
