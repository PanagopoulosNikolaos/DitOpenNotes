"""General methodology table component summarizing ER modeling extraction rules."""

from nicegui import ui


def renderMethodologyTable() -> None:
    """Renders the comprehensive reference guide table for text-to-ER extraction.

    Returns:
        None
    """
    with ui.column().classes("w-full glass-panel gap-4 no-print"):
        with ui.row().classes("items-center gap-3"):
            ui.html('<i class="fa-solid fa-table text-[var(--accent)] text-xl"></i>')
            ui.html('<h2 class="text-xl md:text-2xl font-bold text-[var(--text-1)] m-0">Γενικός Οδηγός Αναγνώρισης (Μεθοδολογικός Πίνακας)</h2>')

        ui.label(
            "Χρησιμοποιήστε τον παρακάτω κανόνα για την ανάλυση οποιουδήποτε γραπτού κειμένου απαιτήσεων:"
        ).classes("text-xs text-[var(--text-2)]")

        table_content = """
        <div class="overflow-x-auto w-full">
            <table class="dark-table shadow-sm">
                <thead>
                    <tr>
                        <th style="width: 25%;">Στοιχείο προς Αναγνώριση</th>
                        <th style="width: 35%;">Πώς το εντοπίζουμε στο κείμενο</th>
                        <th style="width: 40%;">Κανόνες & Κατηγοριοποίηση</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td class="font-bold text-blue-600 dark:text-blue-300">
                            <i class="fa-solid fa-cube mr-1 text-blue-500"></i> Οντότητες (Entities)
                        </td>
                        <td>
                            Συνήθως <strong>κύρια ουσιαστικά</strong> που περιγράφουν αντικείμενα, πρόσωπα, οργανισμούς ή έννοιες με αυτοτελή υπόσταση.
                        </td>
                        <td>
                            • <strong>Ισχυρή (Strong):</strong> Έχει δικό της μονοσήμαντο αναγνωριστικό.<br>
                            • <strong>Ασθενής (Weak):</strong> Δεν έχει πλήρες δικό της κλειδί και εξαρτάται υπαρκτικά από μια οντότητα-ιδιοκτήτη (Owner).
                        </td>
                    </tr>
                    <tr>
                        <td class="font-bold text-emerald-600 dark:text-emerald-300">
                            <i class="fa-solid fa-tag mr-1 text-emerald-500"></i> Γνωρίσματα (Attributes)
                        </td>
                        <td>
                            <strong>Χαρακτηριστικά, ιδιότητες ή πληροφορίες</strong> που αναφέρονται ότι καταγράφονται/διατηρούνται για μια οντότητα ή σχέση.
                        </td>
                        <td>
                            • <strong>Απλό (Atomic):</strong> Δεν διασπάται (π.χ. Φύλο).<br>
                            • <strong>Σύνθετο (Composite):</strong> Διασπάται σε επιμέρους στοιχεία (π.χ. Διεύθυνση).<br>
                            • <strong>Μονότιμο:</strong> 1 τιμή ανά στιγμιότυπο.<br>
                            • <strong>Πλειότιμο (Multi-valued):</strong> Πολλαπλές τιμές (π.χ. Τηλέφωνα, Εγκαταστάσεις).<br>
                            • <strong>Παράγωγο:</strong> Υπολογίζεται από άλλα στοιχεία (π.χ. Ηλικία).
                        </td>
                    </tr>
                    <tr>
                        <td class="font-bold text-amber-600 dark:text-amber-300">
                            <i class="fa-solid fa-key mr-1 text-amber-500"></i> Κλειδιά (Keys)
                        </td>
                        <td>
                            Φράσεις όπως <em>«μοναδικός κωδικός»</em>, <em>«αριθμός ταυτότητας»</em>, <em>«μοναδικό όνομα»</em>, <em>«ΑΦΜ»</em>.
                        </td>
                        <td>
                            • <strong>Υποψήφια (Candidate):</strong> Όλα τα εναλλακτικά μοναδικά πεδία.<br>
                            • <strong>Πρωτεύον (Primary Key - PK):</strong> Η τελική επιλογή μας.<br>
                            • <strong>Μερικό (Partial Key):</strong> Διακρίνει στιγμιότυπα ασθενούς οντότητας στον ίδιο ιδιοκτήτη.
                        </td>
                    </tr>
                    <tr>
                        <td class="font-bold text-rose-600 dark:text-rose-300">
                            <i class="fa-solid fa-code-branch mr-1 text-rose-500"></i> Σχέσεις & Πληθικότητα
                        </td>
                        <td>
                            <strong>Ρήματα ή ρηματικές φράσεις</strong> που συνδέουν οντότητες (π.χ. «ανήκει», «υλοποιεί», «συμμετέχει», «είναι υπεύθυνος»).
                        </td>
                        <td>
                            • <strong>Λόγοι Πληθικότητας:</strong> 1:1, 1:N, N:M (εξετάζουμε και τις δύο κατευθύνσεις: <em>1 A πόσα B; / 1 B πόσα A;</em>).<br>
                            • <strong>Συμμετοχή:</strong> Ολική (υποχρεωτική - διπλή γραμμή) ή Μερική (προαιρετική - απλή γραμμή).
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
        """
        ui.html(table_content)
