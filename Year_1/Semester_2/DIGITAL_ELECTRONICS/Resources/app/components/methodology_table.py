"""Comparative methodology table mapping keywords and patterns to digital design solutions."""

from nicegui import ui


def renderMethodologyTable() -> None:
    """Renders the comprehensive keyword recognition table for digital electronics problems.

    Returns:
        None
    """
    table_rows = [
        {
            "category": "Αριθμητική",
            "clue": "Συμπλήρωμα ως προς 2, n-bit, Υπερχείλιση",
            "equation": r"[-B] = \overline{B} + 1, \quad V = C_{n-1} \oplus C_n",
            "method": "Πρόσημο στο MSB. Αντίστροφο + 1 για αρνητικούς. Υπερχείλιση μόνο σε πρόσθεση ομόσημων με ετερόσημο άθροισμα ή Cin != Cout στο MSB.",
        },
        {
            "category": "Ελαχιστοποίηση",
            "clue": "Συνάρτηση Σ m(...) + d(...), Ελάχιστο SOP",
            "equation": r"\text{K-Map Gray Code } \{00, 01, 11, 10\}",
            "method": "Ομαδοποίηση σε κύβους 2^k. Αξιοποίηση don't cares μόνο όταν μεγαλώνουν ομάδες. Εξαγωγή Essential PIs πρώτα.",
        },
        {
            "category": "Καθολική Σύνθεση",
            "clue": "Μόνο πύλες NOR ή μόνο πύλες NAND 2-εισόδων",
            "equation": r"\overline{x+y} = \overline{x} \cdot \overline{y}, \quad \overline{xy} = \overline{x} + \overline{y}",
            "method": "Διπλό συμπλήρωμα F = F''. De Morgan στον εσωτερικό όρο. Αντιστροφέας NOT: NOR(x,x) ή NAND(x,x).",
        },
        {
            "category": "Κίνδυνοι (Hazards)",
            "clue": "Στατικός Κίνδυνος 1 (Static-1 Hazard), Glitch",
            "equation": r"F = AB + \overline{A}C + BC \quad (\text{Consensus})",
            "method": "Εντοπισμός γειτονικών minterms σε διαφορετικούς κύβους. Προσθήκη του όρου συναίνεσης BC για γεφύρωση.",
        },
        {
            "category": "Σύνθεση MSI",
            "clue": "Υλοποίηση συνάρτησης με MUX 2^(n-1):1 ή Decoder",
            "equation": r"F = \sum m_i \implies \text{NAND}(\overline{Y_i}) \text{ σε Active-Low}",
            "method": "Στον MUX: n-1 μεταβλητές στις γραμμές επιλογής, η τελευταία μεταβλητή ως είσοδος D, D', 0, 1. Στον Decoder: πύλη NAND στις εξόδους.",
        },
        {
            "category": "Ακολουθιακά (FSM)",
            "clue": "Ανιχνευτής ακολουθίας με επικάλυψη (Overlapping)",
            "equation": r"\text{Mealy: } Z=f(Q,X) \quad \text{Moore: } Z=f(Q)",
            "method": "Ορισμός καταστάσεων ως προθέματα. Μετά το match, επιστροφή στο πρόθεμα του τελευταίου bit (όχι στο Reset).",
        },
        {
            "category": "Μετρητές JK",
            "clue": "Σύγχρονος μετρητής Modulo-N με JK-FF & Αυτοδιόρθωση",
            "equation": r"Q \to Q^+: (0\to0: 0,X; \; 0\to1: 1,X; \; 1\to0: X,1; \; 1\to1: X,0)",
            "method": "Πίνακας διεγέρσεων JK. Ελαχιστοποίηση με K-maps. Υπολογισμός επόμενης κατάστασης για unused states για αποφυγή deadlock.",
        },
        {
            "category": "VHDL RTL",
            "clue": "Περιγραφή συνδυαστικής/ακολουθιακής λογικής, αποτροπή latch",
            "equation": r"\text{process(clk, reset)} \quad \text{rising\_edge(clk)}",
            "method": "Πλήρης ανάθεση εξόδων σε όλους τους κλάδους if/case. Πλήρης λίστα ευαισθησίας σε συνδυαστικές διεργασίες.",
        },
    ]

    with ui.column().classes("w-full glass-panel gap-4 p-6 border border-[var(--border)]"):
        with ui.row().classes("items-center gap-2 border-b border-[var(--border)] pb-3"):
            ui.html('<i class="fa-solid fa-table-list text-[var(--accent)] text-lg"></i>')
            with ui.column().classes("gap-0"):
                ui.html('<h2 class="text-base md:text-lg font-bold text-[var(--text-1)] m-0">Πίνακας Αναγνώρισης Μοτίβων Εξέτασης & Τεχνικών Επίλυσης</h2>')
                ui.label("Συσχέτιση λέξεων-κλειδιών εκφώνησης με μαθηματικά μοντέλα και τεχνικές υλοποίησης.").classes("text-xs text-[var(--text-2)]")

        # Responsive Table Container
        with ui.element("div").classes("w-full overflow-x-auto"):
            table_html = [
                '<table class="w-full text-left text-xs border-collapse">',
                '<thead>',
                '<tr class="bg-[var(--table-header-bg)] border-b border-[var(--border)] text-[var(--text-1)]">',
                '<th class="p-3 font-bold">Κατηγορία</th>',
                '<th class="p-3 font-bold">Λέξεις-Κλειδιά & Ενδείξεις</th>',
                '<th class="p-3 font-bold">Κεντρικός Τύπος / Μοντέλο</th>',
                '<th class="p-3 font-bold">Μεθοδολογία Επίλυσης</th>',
                '</tr>',
                '</thead>',
                '<tbody>',
            ]

            for idx, r in enumerate(table_rows):
                bg_cls = 'bg-[var(--table-alt-bg)]' if idx % 2 == 1 else 'bg-[var(--bg-card)]'
                table_html.append(
                    f'<tr class="{bg_cls} border-b border-[var(--border)] hover:bg-[var(--surface-hover)] transition-colors">'
                    f'<td class="p-3 font-bold text-[var(--accent)] whitespace-nowrap">{r["category"]}</td>'
                    f'<td class="p-3 font-semibold text-[var(--text-1)]">{r["clue"]}</td>'
                    f'<td class="p-3 font-mono text-[var(--text-2)] latex-target">${r["equation"]}$</td>'
                    f'<td class="p-3 text-[var(--text-2)] leading-relaxed">{r["method"]}</td>'
                    f'</tr>'
                )

            table_html.append('</tbody></table>')
            ui.html("".join(table_html), tag="div").classes("w-full")

