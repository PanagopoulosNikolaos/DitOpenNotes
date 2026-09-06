"""Methodology cards component providing 4-step problem-solving framework."""

from nicegui import ui


def renderMethodologyCards() -> None:
    """Renders 4 sequential methodology cards for solving digital electronics exam problems.

    Returns:
        None
    """
    cards_data = [
        {
            "step": "Βήμα 1",
            "title": "Αναπαράσταση Δεδομένων & Αριθμητική",
            "icon": "fa-solid fa-binary text-blue-500",
            "desc": "Εντοπισμός μήκους λέξης n-bit, προσημασμένης κωδικοποίησης (C2/C1/SM), κανόνων υπερχείλισης V = Cin ⊕ Cout και ορίων εύρους [-2^(n-1), +2^(n-1)-1].",
        },
        {
            "step": "Βήμα 2",
            "title": "Ελαχιστοποίηση Boole & K-Map",
            "icon": "fa-solid fa-table-cells text-orange-500",
            "desc": "Τοποθέτηση minterms και don't cares σε χάρτη Gray, σχηματισμός μέγιστων ομάδων 2^k, εξαγωγή essential prime implicants και σύνθεση με πύλες NAND/NOR.",
        },
        {
            "step": "Βήμα 3",
            "title": "Ακολουθιακή Σύνθεση & FSM",
            "icon": "fa-solid fa-arrows-spin text-purple-500",
            "desc": "Επιλογή μοντέλου Mealy/Moore, ορισμός καταστάσεων με πρόθεμα, πίνακας διεγέρσεων Flip-Flop (D/JK/T), K-maps και έλεγχος αυτοδιόρθωσης (self-starting).",
        },
        {
            "step": "Βήμα 4",
            "title": "Περιγραφή Υλικού σε VHDL",
            "icon": "fa-solid fa-code text-emerald-500",
            "desc": "Δήλωση Entity (διαύλοι STD_LOGIC_VECTOR), διαχωρισμός σύγχρονης/συνδυαστικής διεργασίας, πλήρης λίστα ευαισθησίας και αποτροπή δημιουργίας latch.",
        },
    ]

    with ui.column().classes("w-full gap-4"):
        with ui.row().classes("items-center gap-2"):
            ui.html('<i class="fa-solid fa-compass-drafting text-[var(--accent)] text-lg"></i>')
            ui.html('<h2 class="text-lg md:text-xl font-bold text-[var(--text-1)] m-0">Μεθοδολογία Επίλυσης Θεμάτων Εξετάσεων (4 Φάσεις)</h2>')

        with ui.grid().classes("grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 w-full"):
            for card in cards_data:
                with ui.column().classes(
                    "p-5 rounded-2xl glass-panel border border-[var(--border)] gap-2 hover:border-[var(--border-accent)] transition-all shadow-sm"
                ):
                    with ui.row().classes("w-full justify-between items-center"):
                        ui.html(f'<span class="text-[0.7rem] font-black uppercase px-2 py-0.5 rounded-full bg-[var(--surface-2)] text-[var(--accent)] border border-[var(--border-accent)]">{card["step"]}</span>')
                        ui.html(f'<i class="{card["icon"]} text-base"></i>')
                    ui.html(f'<h3 class="text-sm font-bold text-[var(--text-1)] m-0">{card["title"]}</h3>')
                    ui.label(card["desc"]).classes("text-xs text-[var(--text-2)] leading-relaxed")

