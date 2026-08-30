"""Topic 6: Data Switching & Routing (Μεταγωγή & Δρομολόγηση) theory renderer.

Covers Packet vs Circuit Switching, Statistical Multiplexing, Store-and-Forward,
the 4 Nodal Delays, Traffic Intensity, Routing vs Forwarding, and Longest Prefix Match.
"""

from nicegui import ui


def renderTopic6DataSwitchingAndRouting() -> None:
    """Renders the comprehensive theory module for Topic 6: Data Switching & Routing."""
    with ui.column().classes("w-full gap-6 text-[#f4f1ea]"):
        # Header Banner
        with ui.column().classes(
            "w-full glass-panel p-6 rounded-2xl border border-[rgba(224,107,58,0.35)] gap-3"
        ):
            with ui.row().classes("items-center gap-3"):
                ui.html('<i class="fa-solid fa-route text-[#e06b3a] text-2xl"></i>')
                with ui.column().classes("gap-0"):
                    ui.html('<h2 class="text-xl font-bold gradient-title m-0">Θέμα 6: Μεταγωγή Δεδομένων & Δρομολόγηση</h2>')
                    ui.label("Μεταγωγή Πακέτου vs Κυκλώματος, Store-and-Forward, 4 Καθυστερήσεις, Ένταση Κίνησης & LPM").classes("text-sm text-[#b5b0a4]")

        # Section 1: Packet vs Circuit Switching
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-shuffle text-blue-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">1. Μεταγωγή Πακέτου (Packet) vs Κυκλώματος (Circuit)</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs leading-relaxed"):
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(224,107,58,0.3)] gap-2"):
                    ui.label("Μεταγωγή Πακέτου (Packet Switching)").classes("font-bold text-[#e06b3a] text-sm")
                    ui.label(
                        "• Τα δεδομένα τεμαχίζονται σε διακριτά πακέτα.\n"
                        "• Στατιστική Πολυπλεξία (Statistical Multiplexing): Οι πόροι δεσμεύονται δυναμικά κατά παραγγελία (on-demand).\n"
                        "• Αποτελεσματικότερη αξιοποίηση εύρους ζώνης για διακοπτόμενη (bursty) κίνηση.\n"
                        "• Μειονέκτημα: Πιθανότητα συμφόρησης, καθυστέρηση ουράς και απώλεια πακέτων (packet loss)."
                    ).classes("text-[#b5b0a4] whitespace-pre-line")

                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(79,142,201,0.3)] gap-2"):
                    ui.label("Μεταγωγή Κυκλώματος (Circuit Switching)").classes("font-bold text-blue-400 text-sm")
                    ui.label(
                        "• Αποκλειστική δέσμευση φυσικών πόρων από άκρο σε άκρο πριν τη μετάδοση (Call Setup Phase).\n"
                        "• Μέθοδοι διαχωρισμού: FDM (Frequency Division) ή TDM (Time Division).\n"
                        "• Εγγυημένη απόδοση και σταθερή καθυστέρηση χωρίς ουρές.\n"
                        "• Μειονέκτημα: Αναποτελεσματικότητα αν το κύκλωμα παραμένει ανενεργό (idle resources wasted)."
                    ).classes("text-[#b5b0a4] whitespace-pre-line")

        # Section 2: The 4 Nodal Delays
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-stopwatch text-[#f59e0b] text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">2. Οι 4 Συνιστώσες της Κομβικής Καθυστέρησης (Nodal Delay)</h3>')

            with ui.column().classes("w-full p-4 rounded-xl bg-[#201f1d] border border-[rgba(245,158,11,0.3)] font-mono text-xs text-[#fed7aa]"):
                ui.label("d_nodal = d_proc + d_queue + d_trans + d_prop").classes("font-bold text-amber-300 text-sm")

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-3 w-full text-xs"):
                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-1"):
                    ui.label("1. Καθυστέρηση Επεξεργασίας (d_proc)").classes("font-bold text-blue-400")
                    ui.label("Έλεγχος σφαλμάτων (bit errors), επιλογή θύρας εξόδου στον πίνακα δρομολόγησης. Συνήθως μικροδευτερόλεπτα (μs).").classes("text-[#b5b0a4]")

                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-1"):
                    ui.label("2. Καθυστέρηση Ουράς (d_queue)").classes("font-bold text-amber-400")
                    ui.label("Χρόνος αναμονής στην ουρά εξόδου μέχρι να ελευθερωθεί ο δίαυλος. Εξαρτάται από την ένταση κίνησης I = (L*a)/R.").classes("text-[#b5b0a4]")

                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-1"):
                    ui.label("3. Καθυστέρηση Μετάδοσης (d_trans = L / R)").classes("font-bold text-[#e06b3a]")
                    ui.label("Χρόνος για να 'σπρωχτούν' όλα τα bits του πακέτου μεγέθους L (bits) πάνω στη ζεύξη ρυθμού R (bps).").classes("text-[#b5b0a4]")

                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-1"):
                    ui.label("4. Καθυστέρηση Διάδοσης (d_prop = d / s)").classes("font-bold text-emerald-400")
                    ui.label("Χρόνος για να ταξιδέψει ένα bit από την αρχή στο τέλος της ζεύξης μήκους d με ταχύτητα διάδοσης s (π.χ. 2*10^8 m/s).").classes("text-[#b5b0a4]")

        # Section 3: Store-and-Forward & Pipelining Formula
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-bars-progress text-emerald-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">3. Store-and-Forward & Σωλήνωση Μετάδοσης (Pipelining)</h3>')

            ui.label(
                "Στη λειτουργία Store-and-Forward, ένας δρομολογητής πρέπει να λάβει πλήρως ολόκληρο το πακέτο προτού ξεκινήσει "
                "τη μετάδοσή του στην επόμενη ζεύξη."
            ).classes("text-sm text-[#b5b0a4]")

            with ui.column().classes("w-full p-4 rounded-xl bg-[#201f1d] border border-[rgba(16,185,129,0.3)] font-mono text-xs text-[#fed7aa]"):
                ui.label("Χρόνος μετάδοσης 1 πακέτου σε N πανομοιότυπες ζεύξεις:").classes("text-stone-300 font-bold")
                ui.label("T_1 = N * (L / R) + N * (d / s)").classes("text-emerald-400 text-sm")
                ui.label("\nΧρόνος μετάδοσης P πακέτων (σωλήνωση / pipelining):").classes("text-stone-300 font-bold")
                ui.label("T_total = (N + P - 1) * (L / R) + N * (d / s)").classes("text-emerald-400 text-sm")
