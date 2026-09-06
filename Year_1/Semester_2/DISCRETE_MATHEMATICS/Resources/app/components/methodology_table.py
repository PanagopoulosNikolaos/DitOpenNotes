"""Methodology recognition table component for Discrete Mathematics study instrument."""

from nicegui import ui
from config import renderMathHtml


def renderMethodologyTable() -> None:
    """Renders comparative table mapping textual triggers to exact mathematical solutions.

    Returns:
        None
    """
    rows = [
        {
            "keyword": "Πίνακας Αληθείας / Ταυτολογία",
            "module": "Προτασιακή Λογική",
            "formula": r"$2^n \text{ γραμμές}, p \to q \equiv \neg p \lor q$",
            "steps": r"1. Μεταβλητές $p, q, r$. 2. Ενδιάμεσες στήλες υποτύπων. 3. Έλεγχος τελικής στήλης: αν όλες $T \to$ ταυτολογία, αν όλες $F \to$ αντίφαση.",
            "trap": r"Η συνεπαγωγή $p \to q$ είναι ψευδής ΜΟΝΟ όταν $p=T, q=F$. Αν $p=F$, είναι κενά αληθής!",
        },
        {
            "keyword": "Απλοποίηση με Κανόνες Λογικής",
            "module": "Άλγεβρα Boole",
            "formula": r"$\neg(p \land q) \equiv \neg p \lor \neg q, p \lor \neg p \equiv \top$",
            "steps": r"1. Αντικατάσταση $a \to b$ με $\neg a \lor b$. 2. De Morgan για άρνηση παρενθέσεων. 3. Επιμεριστικοί και συμπληρώματος σε $\top / \bot$.",
            "trap": "Μην παραλείπετε την ονομασία των κανόνων σε κάθε γραμμή (απαιτείται στην εξέταση).",
        },
        {
            "keyword": "Συμμετέχοντες / Δεν αρέσει κανένα",
            "module": "Θεωρία Συνόλων",
            "formula": r"$|A \cup B \cup C| = \sum |A_i| - \sum |A_i \cap A_j| + |A \cap B \cap C|$",
            "steps": r"1. Καταγραφή δεδομένων. 2. Υπολογισμός $|A \cup B \cup C|$. 3. Συμπλήρωμα: $|U| - |A \cup B \cup C|$.",
            "trap": "Προσοχή στα πρόσημα: τα μονοσύνολα προστίθενται, οι τομές ανά 2 αφαιρούνται, η τομή ανά 3 προστίθεται.",
        },
        {
            "keyword": "Σφαιρίδια σε Κουτιά / Τμήματα",
            "module": "Συνδυαστική",
            "formula": r"$P(n, k) = \frac{n!}{(n-k)!}, C(n+k-1, k)$",
            "steps": r"1. Προσδιορισμός αν τα σφαιρίδια είναι διακεκριμένα ή όμοια. 2. Προσδιορισμός χωρητικότητας κουτιών ($\le 1$ ή άπειρη).",
            "trap": r"Αν τα αντικείμενα διαχωρίζονται σε διαστήματα γραμμάτων (π.χ. Α-Μ, Ν-Ω), αρκεί το μήκος των διαστημάτων: $C(n+k-1, k)$.",
        },
        {
            "keyword": "Διαγνωστικό Τεστ / False Negative",
            "module": "Πιθανότητες & Bayes",
            "formula": r"$P(V_i | T^-) = \frac{P(T^- | V_i)P(V_i)}{P(T^-)}$",
            "steps": r"1. Ορισμός γεγονότων. 2. Ολική πιθανότητα $P(T^-) = \sum P(T^- | V_i)P(V_i)$. 3. Τύπος Bayes για εκ των υστέρων πιθανότητα.",
            "trap": r"False Negative είναι $P(T^- | V)$ (τεστ αρνητικό ενώ υπάρχει ιός). Μην το μπερδεύετε με $P(V | T^-)$!",
        },
        {
            "keyword": "Ιδιότητες Σχέσεων (R επί S)",
            "module": "Σχέσεις",
            "formula": r"\text{Ανακλαστική, Συμμετρική, Αντισυμμετρική, Μεταβατική}",
            "steps": r"1. $(x,x) \in R \ \forall x$. 2. $(x,y) \in R \implies (y,x) \in R$. 3. $(x,y),(y,x) \implies x=y$. 4. $(x,y),(y,z) \implies (x,z) \in R$.",
            "trap": r"Αντισυμμετρία: επιτρέπονται τα $(x,x)$! Δεν σημαίνει 'μη συμμετρική'.",
        },
        {
            "keyword": "Ισομορφισμός Γραφημάτων",
            "module": "Θεωρία Γραφημάτων",
            "formula": r"f: V_1 \to V_2 \text{ αμφιμονοσήμαντη} \land (u,v) \in E_1 \iff (f(u), f(v)) \in E_2",
            "steps": r"1. Έλεγχος αναλλοίωτων: πλήθος κορυφών $|V|$, ακμών $|E|$, ακολουθία βαθμών. 2. Αν ταύτιση, κατασκευή απεικόνισης $f$.",
            "trap": "Ίδια ακολουθία βαθμών ΔΕΝ εγγυάται ισομορφισμό (π.χ. μήκη κύκλων). Πρέπει να δειχθεί η διατήρηση των ακμών.",
        },
        {
            "keyword": "Επίπεδο Γράφημα & Τύπος Euler",
            "module": "Θεωρία Γραφημάτων",
            "formula": r"v - e + f = 2, \ e \le 3v - 6 \ (v \ge 3)",
            "steps": r"1. Σχεδίαση χωρίς διασταυρώσεις ακμών. 2. Καταμέτρηση περιοχών $f$ (μαζί με την εξωτερική). 3. Επαλήθευση $v - e + f = 2$.",
            "trap": r"Μην ξεχνάτε την άπειρη εξωτερική περιοχή! Σε ασύνδετα γραφήματα ισχύει $v - e + f = 1 + c$.",
        },
        {
            "keyword": "Κανονικές Εκφράσεις / Συμβολοσειρές",
            "module": "Τυπικές Γλώσσες",
            "formula": r"L(r), \ \epsilon = \text{κενή συμβολοσειρά}, \ r^* = \text{Kleene star}",
            "steps": r"1. Ανάλυση περιγραφής. 2. Επιλογή δομικών στοιχείων (διάζευξη $|$, συνένωση $\cdot$, επανάληψη $*$). 3. Έλεγχος οριακών λέξεων.",
            "trap": r"Το $0^*$ περιλαμβάνει και το $\epsilon$ (0 εμφανίσεις, άρα άρτιο πλήθος). Για $\ge 1$ απαιτείται $00^*$ ή $0^+$.",
        },
        {
            "keyword": "Μαθηματική Επαγωγή",
            "module": "Μαθηματική Επαγωγή",
            "formula": r"P(n_0) \text{ αληθές} \land (\forall k \ge n_0, P(k) \implies P(k+1)) \implies \forall n \ge n_0 P(n)",
            "steps": r"1. Βάση: Έλεγχος για $n = n_0$. 2. Επαγωγική Υπόθεση: Έστω ισχύει για $n=k$. 3. Επαγωγικό Βήμα: Απόδειξη για $n=k+1$.",
            "trap": "Στο επαγωγικό βήμα πρέπει να διατυπώνεται καθαρά πού ακριβώς γίνεται η χρήση της Επαγωγικής Υπόθεσης.",
        },
    ]

    with ui.column().classes("w-full glass-panel p-6 gap-4 border border-[var(--border)]"):
        with ui.row().classes("w-full items-center gap-2 pb-2 border-b border-[var(--border)]"):
            ui.html('<i class="fa-solid fa-table-list text-[var(--accent)] text-lg"></i>')
            with ui.column().classes("gap-0"):
                ui.label("Συγκριτικός Πίνακας Αναγνώρισης Μοτίβων & Τεχνικών Επίλυσης").classes(
                    "text-base font-bold text-[var(--text-1)]"
                )
                ui.label("Χαρτογράφηση φράσεων εκφώνησης στο αντίστοιχο μαθηματικό πλαίσιο, τύπο και παγίδες.").classes(
                    "text-xs text-[var(--text-3)]"
                )

        with ui.column().classes("w-full overflow-x-auto"):
            table_html = [
                '<table class="w-full text-xs text-left border-collapse">',
                '<thead><tr class="bg-[var(--table-header-bg)] border-b border-[var(--border)] text-[var(--text-2)]">',
                '<th class="p-3 font-bold">Φράση-Κλειδί Εκφώνησης</th>',
                '<th class="p-3 font-bold">Θεματική Ενότητα</th>',
                '<th class="p-3 font-bold">Μαθηματικός Τύπος</th>',
                '<th class="p-3 font-bold">Βηματική Μεθοδολογία</th>',
                '<th class="p-3 font-bold text-red-500">Συχνή Παγίδα Εξέτασης</th>',
                '</tr></thead><tbody>',
            ]

            for row in rows:
                table_html.append(
                    f'<tr class="border-b border-[var(--border)] hover:bg-[var(--surface-hover)] transition-colors">'
                    f'<td class="p-3 font-bold text-[var(--text-1)] whitespace-nowrap"><i class="fa-solid fa-key text-[var(--accent)] mr-1.5"></i>{row["keyword"]}</td>'
                    f'<td class="p-3 text-[var(--blue-action)] font-semibold whitespace-nowrap">{row["module"]}</td>'
                    f'<td class="p-3 font-mono text-[var(--accent)] latex-target whitespace-nowrap">{row["formula"]}</td>'
                    f'<td class="p-3 text-[var(--text-2)] leading-relaxed min-w-[220px] latex-target">{renderMathHtml(row["steps"])}</td>'
                    f'<td class="p-3 text-red-500/90 leading-relaxed min-w-[200px] latex-target">{renderMathHtml(row["trap"])}</td>'
                    f'</tr>'
                )

            table_html.append('</tbody></table>')
            ui.html("".join(table_html))
