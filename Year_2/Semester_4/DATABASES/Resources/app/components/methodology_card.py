"""Methodology quick-guide 4-step cards component."""

from nicegui import ui


def renderMethodologyCards() -> None:
    """Renders the 4-step methodology cards explaining how to analyze any ER problem.

    Returns:
        None
    """
    with ui.column().classes("w-full glass-panel gap-4 no-print"):
        with ui.row().classes("items-center gap-3"):
            ui.html('<i class="fa-solid fa-compass text-[#e06b3a] text-xl"></i>')
            ui.html('<h2 class="text-xl font-bold text-[#f4f1ea] m-0">Πώς Αναλύουμε Οποιοδήποτε Κείμενο (Βήμα-Βήμα)</h2>')

        with ui.grid().classes("grid-cols-1 md:grid-cols-4 gap-4 w-full"):
            # Step 1: Entities
            with ui.column().classes(
                "p-4 rounded-xl bg-[#201f1d] border-l-4 border-blue-500 border border-[rgba(255,255,255,0.06)] gap-1"
            ):
                with ui.row().classes("items-center gap-2"):
                    ui.html('<i class="fa-solid fa-cube text-blue-400 text-sm"></i>')
                    ui.label("1. Οντότητες (Entities)").classes("font-bold text-blue-300 text-sm")
                ui.label(
                    "Ψάχνουμε κύρια ουσιαστικά (πρόσωπα, αντικείμενα, έννοιες) που έχουν αυτόνομη "
                    "υπόσταση και για τα οποία διατηρούμε πληροφορίες."
                ).classes("text-xs text-[#b5b0a4] leading-relaxed")

            # Step 2: Attributes
            with ui.column().classes(
                "p-4 rounded-xl bg-[#201f1d] border-l-4 border-emerald-500 border border-[rgba(255,255,255,0.06)] gap-1"
            ):
                with ui.row().classes("items-center gap-2"):
                    ui.html('<i class="fa-solid fa-tag text-emerald-400 text-sm"></i>')
                    ui.label("2. Γνωρίσματα (Attributes)").classes("font-bold text-emerald-300 text-sm")
                ui.label(
                    "Εντοπίζουμε τις ιδιότητες / χαρακτηριστικά των οντοτήτων. Διακρίνουμε σε "
                    "Απλά, Σύνθετα, Πλειότιμα ή Παράγωγα."
                ).classes("text-xs text-[#b5b0a4] leading-relaxed")

            # Step 3: Keys
            with ui.column().classes(
                "p-4 rounded-xl bg-[#201f1d] border-l-4 border-amber-500 border border-[rgba(255,255,255,0.06)] gap-1"
            ):
                with ui.row().classes("items-center gap-2"):
                    ui.html('<i class="fa-solid fa-key text-amber-400 text-sm"></i>')
                    ui.label("3. Κλειδιά (Keys)").classes("font-bold text-amber-300 text-sm")
                ui.label(
                    "Ψάχνουμε λέξεις όπως «μοναδικός κωδικός», «ΑΔΤ». Επιλέγουμε το Πρωτεύον Κλειδί (PK) "
                    "και εντοπίζουμε τα Μερικά Κλειδιά."
                ).classes("text-xs text-[#b5b0a4] leading-relaxed")

            # Step 4: Relationships
            with ui.column().classes(
                "p-4 rounded-xl bg-[#201f1d] border-l-4 border-rose-500 border border-[rgba(255,255,255,0.06)] gap-1"
            ):
                with ui.row().classes("items-center gap-2"):
                    ui.html('<i class="fa-solid fa-code-branch text-rose-400 text-sm"></i>')
                    ui.label("4. Σχέσεις & Πληθικότητα").classes("font-bold text-rose-300 text-sm")
                ui.label(
                    "Ψάχνουμε ρήματα που συνδέουν οντότητες. Εξετάζουμε και τις δύο κατευθύνσεις "
                    "για τους λόγους 1:1, 1:N, N:M."
                ).classes("text-xs text-[#b5b0a4] leading-relaxed")
