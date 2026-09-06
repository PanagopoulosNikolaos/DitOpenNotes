"""General methodology table mapping exam problem patterns to exact solutions."""

from nicegui import ui


def renderMethodologyTable() -> None:
    """Renders the comprehensive recognition table from textual keywords to technical solutions.

    Returns:
        None
    """
    with ui.column().classes("w-full glass-panel gap-4 no-print"):
        with ui.row().classes("items-center gap-3"):
            ui.html('<i class="fa-solid fa-table-list text-[var(--accent)] text-xl"></i>')
            ui.html('<h2 class="text-xl md:text-2xl font-bold text-[var(--text-1)] m-0">Γενικός Οδηγός Αναγνώρισης (Μεθοδολογικός Πίνακας)</h2>')

        ui.label(
            "Χρησιμοποιήστε τον παρακάτω κανόνα για την αντιστοίχιση εκφωνήσεων σε τύπους και αλγορίθμους:"
        ).classes("text-xs text-[var(--text-2)]")

        table_content = """
        <div class="overflow-x-auto w-full">
            <table class="dark-table shadow-sm">
                <thead>
                    <tr>
                        <th style="width: 26%;">Στοιχείο προς Αναγνώριση</th>
                        <th style="width: 34%;">Πώς το εντοπίζουμε στην εκφώνηση</th>
                        <th style="width: 40%;">Κανόνες, Τύποι & Μέθοδοι</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td class="font-bold text-blue-600 dark:text-blue-300">
                            <i class="fa-solid fa-sitemap mr-1 text-blue-500"></i> Μοντέλο & Ενθυλάκωση
                        </td>
                        <td>
                            Λέξεις-κλειδιά: <strong>OSI, TCP/IP, επίπεδα, PDU, ενθυλάκωση (encapsulation)</strong>.
                        </td>
                        <td>
                            • OSI 7 επίπεδα &harr; TCP/IP 4 επίπεδα (App+Pres+Session &rarr; Application).<br>
                            • PDU: Data &rarr; Segment/Datagram &rarr; Packet &rarr; Frame &rarr; Bits.<br>
                            • MAC: 48-bit φυσική, L2 τοπική παράδοση. IP: 32-bit λογική, L3 δρομολόγηση.
                        </td>
                    </tr>
                    <tr>
                        <td class="font-bold text-amber-600 dark:text-amber-300">
                            <i class="fa-solid fa-network-wired mr-1 text-amber-500"></i> Υποδικτύωση / VLSM
                        </td>
                        <td>
                            <strong>«Βρείτε Network Address, Mask, First/Last, Broadcast»</strong>, δοσμένο δίκτυο τύπου <code>a.b.c.d/x</code> και λίστα host ανά υποδίκτυο.
                        </td>
                        <td>
                            • Χωρητικότητα: \\(2^h - 2 \\ge \\text{hosts} \\Rightarrow h\\) bits &rarr; prefix \\(32-h\\).<br>
                            • Ταξινόμηση αναγκών κατά φθίνουσα σειρά (μεγαλύτερο πρώτα).<br>
                            • Block = \\(256 - \\text{τελευταίο byte μάσκας}\\)· κάθε υποδίκτυο ξεκινά στο broadcast του προηγούμενου + 1.
                        </td>
                    </tr>
                    <tr>
                        <td class="font-bold text-emerald-600 dark:text-emerald-300">
                            <i class="fa-solid fa-scissors mr-1 text-emerald-500"></i> Κατάτμηση IP (Fragmentation)
                        </td>
                        <td>
                            Δοσμένα <strong>Total Length, Header Length, MTU εξερχόμενης ζεύξης</strong>, σημαίες DF/MF, Fragment Offset.
                        </td>
                        <td>
                            • Ωφέλιμα δεδομένα ανά τμήμα: \\(\\text{MTU} - 20\\) και <strong>πολλαπλάσιο του 8</strong>.<br>
                            • Offset σε μονάδες 8 bytes: \\(\\text{offset} = \\text{θέση} / 8\\).<br>
                            • MF=1 σε όλα εκτός τελευταίου· ίδιο Identification σε όλα τα τμήματα.
                        </td>
                    </tr>
                    <tr>
                        <td class="font-bold text-purple-600 dark:text-purple-300">
                            <i class="fa-solid fa-gauge-high mr-1 text-purple-500"></i> Έλεγχος Ροής & Συμφόρησης TCP
                        </td>
                        <td>
                            <strong>MSS, ssthresh, cwnd, RTT, διπλότυπα ACK, παράθυρο, ρυθμοαπόδοση (throughput)</strong>.
                        </td>
                        <td>
                            • Slow Start: cwnd διπλασιάζεται ανά RTT μέχρι ssthresh· μετά +1 MSS ανά RTT.<br>
                            • Απώλεια (3 dup ACK): Tahoe &rarr; cwnd=1, Reno &rarr; cwnd=ssthresh+3.<br>
                            • \\(\\text{Throughput} = W / \\text{RTT}\\)· \\(\\text{BDP} = R \\times \\text{RTT}\\).
                        </td>
                    </tr>
                    <tr>
                        <td class="font-bold text-rose-600 dark:text-rose-300">
                            <i class="fa-solid fa-route mr-1 text-rose-500"></i> Δρομολόγηση & Πίνακες
                        </td>
                        <td>
                            <strong>«Εκτελέστε Dijkstra», κόστη ζεύξεων, πίνακες δρομολόγησης, σύνοψη διαδρομών (summarization)</strong>, OSPF/RIP/BGP.
                        </td>
                        <td>
                            • Dijkstra: πρόσθεση \\(D(v) = \\min(D(v), D(u) + c(u,v))\\), ελάχιστο κάθε βήμα.<br>
                            • Πίνακες: Longest Prefix Match (η πιο εξειδικευμένη διαδρομή κερδίζει).<br>
                            • Σύνοψη: κοινά αρχικά bits των δικτύων &rarr; νέο πρόθεμα (π.χ. 16-19 &rarr; /22).
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
        """
        ui.html(table_content)
