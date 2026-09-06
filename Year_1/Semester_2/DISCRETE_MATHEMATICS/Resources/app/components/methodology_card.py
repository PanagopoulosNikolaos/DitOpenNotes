"""Methodology quick guide cards component for Discrete Mathematics study instrument."""

from nicegui import ui


def renderMethodologyCards() -> None:
    """Renders 4 sequential methodology guidance cards for discrete mathematical analysis.

    Returns:
        None
    """
    cards_data = [
        {
            "step": "1",
            "title": "Αναγνώριση & Ταξινόμηση Μοντέλου",
            "icon": "fa-solid fa-brain",
            "color": "var(--amber)",
            "description": "Εντοπίστε το μαθηματικό πεδίο: Προτασιακή Λογική, Θεωρία Συνόλων, Μοντέλο Σφαιρίδια-Κουτιά, Bayes, Σχέσεις, Γραφήματα, Αυτόματα ή Επαγωγή.",
            "checklist": [
                "Προσδιορίστε αν ζητείται απόδειξη ταυτολογίας ή πίνακας αληθείας",
                "Ελέγξτε αν τα αντικείμενα είναι διακεκριμένα ή όμοια (Κουτιά-Σφαιρίδια)",
                "Αναγνωρίστε αν πρόκειται για απλό ή πολυγράφημα / επίπεδο",
            ],
        },
        {
            "step": "2",
            "title": "Απομόνωση Παραμέτρων & Συνθηκών",
            "icon": "fa-solid fa-filter",
            "color": "var(--blue-action)",
            "description": "Καταγράψτε με ακρίβεια τα δεδομένα, τα μεγέθη πληθικότητας $|A|$, τις εκτιμώμενες πιθανότητες και τις συνθήκες ορίων.",
            "checklist": [
                "Ελέγξτε αν τα γεγονότα διαμερίζουν το σύμπαν U (Ολική Πιθανότητα)",
                "Καταγράψτε τη βάση επαγωγής (π.χ. n = 0 ή n = 1)",
                "Σημειώστε τυχόν περιορισμούς χωρητικότητας (το πολύ 1 ή άπειρη)",
            ],
        },
        {
            "step": "3",
            "title": "Τυπική Μαθηματική Παραγωγή",
            "icon": "fa-solid fa-calculator",
            "color": "var(--accent)",
            "description": "Εφαρμόστε τους αυστηρούς μαθηματικούς τύπους και τις ιδιότητες βήμα προς βήμα, δικαιολογώντας κάθε επιμέρους ισοδυναμία.",
            "checklist": [
                "Αναφέρετε το όνομα κάθε κανόνα λογικής (De Morgan, Επιμεριστικός)",
                "Εφαρμόστε τον τύπο Euler (v - e + f = 2) για επίπεδα γραφήματα",
                "Κατασκευάστε τον πίνακα μεταβάσεων για DFA / κατασκευή υποσυνόλων",
            ],
        },
        {
            "step": "4",
            "title": "Έλεγχος Παγίδων & Επαλήθευση",
            "icon": "fa-solid fa-shield-halved",
            "color": "var(--green-ok)",
            "description": "Επαληθεύστε τα αποτελέσματα με αντιπαραδείγματα, νόμους συμμετρίας και συνήθεις παγίδες των εξετάσεων.",
            "checklist": [
                "Ελέγξτε αν το άθροισμα των βαθμών είναι άρτιο (Λήμμα Χειραψιών)",
                "Βεβαιωθείτε ότι P(A|B) ∈ [0, 1] και ότι το κενό σύνολο ∅ ∈ P(S)",
                "Ελέγξτε αν η σχέση είναι κενά μεταβατική (vacuous truth)",
            ],
        },
    ]

    with ui.column().classes("w-full gap-4"):
        with ui.row().classes("w-full items-center gap-2 pb-1 border-b border-[var(--border)]"):
            ui.html('<i class="fa-solid fa-compass text-[var(--accent)] text-lg"></i>')
            ui.label("Μεθοδολογία Επίλυσης & Βηματικός Οδηγός Εξέτασης").classes(
                "text-base font-bold text-[var(--text-1)]"
            )

        with ui.grid().classes("grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 w-full"):
            for card in cards_data:
                with ui.column().classes("glass-panel p-4 gap-3 relative border border-[var(--border)]"):
                    with ui.row().classes("w-full items-center justify-between"):
                        with ui.row().classes("items-center gap-2"):
                            ui.html(f'<i class="{card["icon"]} text-sm" style="color: {card["color"]};"></i>')
                            ui.label(f"Βήμα {card['step']}").classes("text-xs font-black uppercase tracking-wider text-[var(--text-3)]")
                        ui.html(f'<span class="w-6 h-6 rounded-full flex items-center justify-center text-xs font-black" style="background: {card["color"]}18; color: {card["color"]};">{card["step"]}</span>')

                    ui.label(card["title"]).classes("text-sm font-bold text-[var(--text-1)] leading-tight")
                    ui.label(card["description"]).classes("text-xs text-[var(--text-2)] leading-relaxed")

                    with ui.column().classes("w-full gap-1 pt-2 border-t border-[var(--border)] text-xs text-[var(--text-3)]"):
                        for check in card["checklist"]:
                            with ui.row().classes("items-start gap-1.5 leading-snug"):
                                ui.html('<i class="fa-solid fa-angle-right text-[0.65rem] mt-1 text-[var(--accent)]"></i>')
                                ui.label(check).classes("text-[0.75rem]")
