"""Topic 6: Data Switching & Routing (Μεταγωγή & Δρομολόγηση) theory renderer.

Covers Packet vs Circuit Switching, Statistical Multiplexing, Store-and-Forward Pipelining,
the 4 Nodal Delays with LaTeX formulas, Traffic Intensity, Routing (Control Plane) vs Forwarding (Data Plane),
and Forwarding Tables with Longest Prefix Match (LPM).
"""

from nicegui import ui


def renderTopic6DataSwitchingAndRouting() -> None:
    """Renders the comprehensive theory module for Topic 6: Data Switching & Routing."""
    with ui.column().classes("w-full gap-6 text-[#f4f1ea] latex-target"):
        # Header Banner
        with ui.column().classes(
            "w-full glass-panel p-6 md:p-8 rounded-2xl border border-[rgba(224,107,58,0.35)] gap-3"
        ):
            with ui.row().classes("items-center gap-3"):
                ui.html('<i class="fa-solid fa-route text-[#e06b3a] text-3xl"></i>')
                with ui.column().classes("gap-0"):
                    ui.html('<h2 class="text-xl md:text-2xl font-bold gradient-title m-0">Θέμα 6: Μεταγωγή Δεδομένων & Δρομολόγηση</h2>')
                    ui.label(
                        "Μεταγωγή Πακέτου vs Κυκλώματος, Store-and-Forward, 4 Καθυστερήσεις, "
                        "Ένταση Κίνησης, Pipelining, Control vs Data Plane και Longest Prefix Match (LPM)."
                    ).classes("text-xs md:text-sm text-[#b5b0a4]")

        # =========================================================================
        # SECTION 1: Packet Switching vs Circuit Switching
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-shuffle text-blue-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">1. Μεταγωγή Πακέτου (Packet Switching) vs Μεταγωγή Κυκλώματος (Circuit Switching)</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs leading-relaxed"):
                # Packet Switching Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(224,107,58,0.3)] gap-2"):
                    ui.label("Μεταγωγή Πακέτου (Packet Switching)").classes("font-bold text-[#e06b3a] text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1.5 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Τεμαχισμός:</strong> Τα δεδομένα χωρίζονται σε διακριτά πακέτα ($L$ bits).</li>
                        <li><strong class="text-stone-200">Στατιστική Πολυπλεξία (Statistical Multiplexing):</strong> Οι πόροι του δικτύου δεσμεύονται δυναμικά κατά παραγγελία (on-demand), επιτρέποντας σε πολύ περισσότερους χρήστες να μοιράζονται τη ζεύξη.</li>
                        <li><strong class="text-stone-200">Αποτελεσματικότητα:</strong> Ιδανικό για διακοπτόμενη (bursty) κίνηση δεδομένων.</li>
                        <li><strong class="text-amber-300">Μειονέκτημα:</strong> Πιθανότητα εμφάνισης καθυστέρησης ουράς και απώλειας πακέτων (packet loss) σε περιόδους συμφόρησης.</li>
                    </ul>
                    """)

                # Circuit Switching Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(79,142,201,0.3)] gap-2"):
                    ui.label("Μεταγωγή Κυκλώματος (Circuit Switching)").classes("font-bold text-blue-400 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1.5 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Αποκλειστικοί Πόροι:</strong> Δέσμευση αποκλειστικού κυκλώματος/εύρους ζώνης σε όλη τη διαδρομή πριν τη μετάδοση (Call Setup).</li>
                        <li><strong class="text-stone-200">Πολυπλεξία:</strong> Διαχωρισμός με <strong>FDM</strong> (Frequency Division) ή <strong>TDM</strong> (Time Division).</li>
                        <li><strong class="text-stone-200">Εγγυημένη Απόδοση:</strong> Σταθερός ρυθμός, μηδενική καθυστέρηση ουράς ($d_{\\text{queue}} = 0$).</li>
                        <li><strong class="text-red-400">Μειονέκτημα:</strong> Σπατάλη πόρων αν το κανάλι παραμένει ανενεργό (idle capacity wasted) και καθυστέρηση εγκατάστασης κλήσης.</li>
                    </ul>
                    """)

        # =========================================================================
        # SECTION 2: The 4 Nodal Delays with LaTeX Formulas
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-stopwatch text-amber-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">2. Οι 4 Συνιστώσες της Κομβικής Καθυστέρησης (Nodal Delay)</h3>')

            with ui.column().classes("w-full p-4 rounded-xl bg-[#141413] border border-[rgba(224,107,58,0.35)] gap-2"):
                ui.html("""
                <div class="formula-box text-sm">
                    $$d_{\\text{nodal}} = d_{\\text{proc}} + d_{\\text{queue}} + d_{\\text{trans}} + d_{\\text{prop}}$$
                </div>
                """)

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs"):
                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-1"):
                    ui.label("1. Καθυστέρηση Επεξεργασίας (d_proc)").classes("font-bold text-blue-400")
                    ui.label("Χρόνος για έλεγχο επικεφαλίδων, επιβεβαίωση αθροίσματος ελέγχου (bit error checksum) και αναζήτηση θύρας εξόδου στον πίνακα δρομολόγησης. Τυπικά μικροδευτερόλεπτα (μs).").classes("text-[#b5b0a4]")

                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-1"):
                    ui.label("2. Καθυστέρηση Ουράς (d_queue)").classes("font-bold text-amber-400")
                    ui.label("Χρόνος αναμονής του πακέτου στον buffer εξόδου μέχρι να ελευθερωθεί ο δίαυλος. Εξαρτάται από την ένταση κίνησης I = (L*a)/R.").classes("text-[#b5b0a4]")

                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-1"):
                    ui.label("3. Καθυστέρηση Μετάδοσης (d_trans)").classes("font-bold text-[#e06b3a]")
                    ui.html("<div>Χρόνος διοχέτευσης όλων των bits του πακέτου πάνω στη ζεύξη: $$d_{\\text{trans}} = \\frac{L}{R}$$ όπου $L$: bits πακέτου, $R$: bandwidth (bps).</div>").classes("text-[#b5b0a4]")

                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-1"):
                    ui.label("4. Καθυστέρηση Διάδοσης (d_prop)").classes("font-bold text-emerald-400")
                    ui.html("<div>Χρόνος ταξιδιού ενός bit από την αρχή στο τέλος του μέσου: $$d_{\\text{prop}} = \\frac{l}{u}$$ όπου $l$: απόσταση (m), $u$: ταχύτητα φωτός στο μέσο.</div>").classes("text-[#b5b0a4]")

        # =========================================================================
        # SECTION 3: Store-and-Forward & Multi-packet Pipelining
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-bars-progress text-emerald-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">3. Store-and-Forward & Σωλήνωση Μετάδοσης (Pipelining)</h3>')

            ui.label(
                "Στη λειτουργία Store-and-Forward, ένας δρομολογητής πρέπει να παραλάβει ολόκληρο το πακέτο προτού "
                "ξεκινήσει τη μετάδοσή του στην επόμενη εξερχόμενη ζεύξη."
            ).classes("text-xs md:text-sm text-[#b5b0a4]")

            with ui.column().classes("w-full p-4 rounded-xl bg-[#141413] border border-[rgba(16,185,129,0.3)] font-mono text-xs text-[#fed7aa] space-y-2"):
                ui.html("""
                <div class="text-stone-300 font-bold">// Χρόνος μετάδοσης 1 πακέτου σε N πανομοιότυπες ζεύξεις:</div>
                <div class="text-emerald-400 text-sm">$$T_1 = N \\cdot \\left(\\frac{L}{R}\\right) + \\sum_{i=1}^{N} d_{\\text{prop},i}$$</div>
                <div class="text-stone-300 font-bold mt-2">// Χρόνος μετάδοσης P πακέτων με σωλήνωση (Pipelining):</div>
                <div class="text-emerald-400 text-sm">$$T_{\\text{total}} = (N + P - 1) \\cdot \\left(\\frac{L}{R}\\right) + \\sum_{i=1}^{N} d_{\\text{prop},i} + (N-1) \\cdot d_{\\text{proc}}$$</div>
                """)

        # =========================================================================
        # SECTION 4: Routing vs Forwarding & LPM Rule
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-table-list text-amber-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">4. Δρομολόγηση (Routing) vs Προώθηση (Forwarding) & Longest Prefix Match</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs"):
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(79,142,201,0.3)] gap-2"):
                    ui.label("Routing (Control Plane) vs Forwarding (Data Plane)").classes("font-bold text-blue-300 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1.5 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Δρομολόγηση (Routing):</strong> Συνολική δικτυακή διεργασία. Αλγόριθμοι (OSPF, BGP) υπολογίζουν από άκρο σε άκρο τις διαδρομές και κατασκευάζουν τον πίνακα <strong>RIB</strong>.</li>
                        <li><strong class="text-stone-200">Προώθηση (Forwarding):</strong> Τοπική διεργασία κόμβου. Μεταφορά πακέτου από θύρα εισόδου σε θύρα εξόδου σε νανοδευτερόλεπτα μέσω του πίνακα <strong>FIB</strong> στο hardware (ASICs).</li>
                    </ul>
                    """)

                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(245,158,11,0.3)] gap-2"):
                    ui.label("Κανόνας Longest Prefix Match (LPM)").classes("font-bold text-amber-300 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1.5 text-[#b5b0a4]">
                        <li>Ο δρομολογητής συγκρίνει την IP προορισμού με όλες τις εγγραφές του πίνακα προώθησης.</li>
                        <li>Αν η IP ταιριάζει με πολλαπλά υποδίκτυα, επιλέγεται <strong>ΠΑΝΤΑ</strong> η εγγραφή με το μεγαλύτερο μήκος προθέματος (πιο συγκεκριμένη μάσκα, π.χ. το /25 υπερισχύει του /24 και του /16).</li>
                    </ul>
                    """)
