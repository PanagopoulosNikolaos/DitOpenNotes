"""Topic 5: Communication Media (Μέσα Επικοινωνίας) theory renderer.

Covers Guided vs Unguided Media, Twisted Pair (UTP/STP Cat5e-Cat8, Crosstalk),
Coaxial Cable (Baseband vs Broadband), Optical Fiber (Total Internal Reflection, SMF Laser vs MMF LED),
Wireless/Radio, Satellite orbits (GEO vs LEO), and Shannon-Hartley Channel Capacity.
"""

from nicegui import ui


def renderTopic5CommunicationMedia() -> None:
    """Renders the comprehensive theory module for Topic 5: Communication Media."""
    with ui.column().classes("w-full gap-6 text-[#f4f1ea] latex-target"):
        # Header Banner
        with ui.column().classes(
            "w-full glass-panel p-6 md:p-8 rounded-2xl border border-[rgba(224,107,58,0.35)] gap-3"
        ):
            with ui.row().classes("items-center gap-3"):
                ui.html('<i class="fa-solid fa-network-wired text-[#e06b3a] text-3xl"></i>')
                with ui.column().classes("gap-0"):
                    ui.html('<h2 class="text-xl md:text-2xl font-bold gradient-title m-0">Θέμα 5: Μέσα Επικοινωνίας (Communication Media)</h2>')
                    ui.label(
                        "Καθοδηγούμενα & Μη Καθοδηγούμενα Μέσα, Συνεστραμμένο Ζεύγος (UTP/STP), Ομοαξονικό Καλώδιο, "
                        "Οπτικές Ίνες (SMF/MMF), Δορυφόροι και Θεώρημα Χωρητικότητας Shannon."
                    ).classes("text-xs md:text-sm text-[#b5b0a4]")

        # =========================================================================
        # SECTION 1: Guided Media (Twisted Pair & Coaxial)
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-lines-leaning text-amber-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">1. Καθοδηγούμενα Μέσα Χαλκού: Συνεστραμμένο Ζεύγος & Ομοαξονικό</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs"):
                # Twisted Pair Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(224,107,58,0.3)] gap-2"):
                    ui.label("Συνεστραμμένο Ζεύγος (Twisted Pair - UTP / STP)").classes("font-bold text-[#e06b3a] text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1.5 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Αρχή Συστροφής (Twisting):</strong> Δύο μονωμένοι αγωγοί χαλκού συστρέφονται σε ελικοειδή μορφή. Η συστροφή εξουδετερώνει την αλληλεπίδραση (Crosstalk) και τις ηλεκτρομαγνητικές παρεμβολές (EMI) μέσω διαφορικής σηματοδοσίας.</li>
                        <li><strong class="text-stone-200">UTP vs STP:</strong> Το UTP (Unshielded) είναι οικονομικό και ευέλικτο. Το STP (Shielded) διαθέτει μεταλλικό πλέγμα θωράκισης για βιομηχανικά περιβάλλοντα με έντονο θόρυβο.</li>
                        <li><strong class="text-stone-200">Κατηγορίες (Categories):</strong>
                            <br>• <span class="text-stone-200">Cat5e:</span> 100 MHz $\\rightarrow$ 1 Gbps (1000BASE-T έως 100m).
                            <br>• <span class="text-stone-200">Cat6 / 6a:</span> 250/500 MHz $\\rightarrow$ 10 Gbps (10GBASE-T).
                            <br>• <span class="text-stone-200">Cat7 / 8:</span> 600/2000 MHz $\\rightarrow$ 25/40 Gbps σε Data Centers.
                        </li>
                    </ul>
                    """)

                # Coaxial Cable Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(245,158,11,0.3)] gap-2"):
                    ui.label("Ομοαξονικό Καλώδιο (Coaxial Cable)").classes("font-bold text-amber-300 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1.5 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Κατασκευή:</strong> Κεντρικός χάλκινος αγωγός, διηλεκτρικό μονωτικό, εξωτερικό μεταλλικό πλέγμα θωράκισης και προστατευτικός μανδύας.</li>
                        <li><strong class="text-stone-200">Baseband (50 $\\Omega$):</strong> Ψηφιακή μετάδοση ενός καναλιού (παλιά Ethernet 10BASE2/10BASE5).</li>
                        <li><strong class="text-stone-200">Broadband (75 $\\Omega$):</strong> Αναλογική πολυπλεξία συχνοτήτων (FDM) σε πολλαπλά κανάλια (Καλωδιακή Τηλεόραση, HFC Cable DOCSIS).</li>
                        <li><strong class="text-stone-200">Χαρακτηριστικό:</strong> Υψηλότερη ανοσία στο θόρυβο σε σχέση με το UTP, αλλά πιο δύσκαμπτο και ακριβό στην εγκατάσταση.</li>
                    </ul>
                    """)

        # =========================================================================
        # SECTION 2: Optical Fiber (SMF vs MMF)
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-bolt text-cyan-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">2. Οπτικές Ίνες: Ολική Εσωτερική Ανάκλαση & Μονότροπες vs Πολύτροπες</h3>')

            ui.label(
                "Η οπτική ίνα μεταφέρει πληροφορία υπό μορφή φωτεινών παλμών μέσα από γυάλινο ή πλαστικό πυρήνα. "
                "Η διάδοση βασίζεται στην Ολική Εσωτερική Ανάκλαση (Total Internal Reflection), η οποία συμβαίνει όταν ο δείκτης "
                "διάθλασης του πυρήνα είναι μεγαλύτερος από εκείνον του περιβλήματος (n_core > n_cladding) και η γωνία πρόπτωσης "
                "υπερβαίνει την κρίσιμη γωνία θ_c."
            ).classes("text-xs md:text-sm text-[#b5b0a4]")

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs"):
                # Single-Mode Fiber Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(6,182,212,0.3)] gap-2"):
                    ui.label("Μονότροπη Οπτική Ίνα (Single-Mode Fiber - SMF)").classes("font-bold text-cyan-300 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1.5 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Διάμετρος Πυρήνα:</strong> Εξαιρετικά λεπτός ($8 – 10\\ \\mu\\text{m}$).</li>
                        <li><strong class="text-stone-200">Πηγή Φωτός:</strong> Laser (μήκη κύματος $1310\\text{ nm}, 1550\\text{ nm}$).</li>
                        <li><strong class="text-stone-200">Διασπορά:</strong> <em>Μηδενική τροπική διασπορά</em> (μόνο 1 φωτεινή ακτίνα/τρόπος διάδοσης).</li>
                        <li><strong class="text-emerald-400">Εμβέλεια:</strong> Δεκάδες έως εκατοντάδες χιλιόμετρα (Backbone, MAN, WAN, Υποβρύχια καλώδια).</li>
                    </ul>
                    """)

                # Multi-Mode Fiber Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(245,158,11,0.3)] gap-2"):
                    ui.label("Πολύτροπη Οπτική Ίνα (Multi-Mode Fiber - MMF)").classes("font-bold text-amber-300 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1.5 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Διάμετρος Πυρήνα:</strong> Ευρύτερος ($50 – 62,5\\ \\mu\\text{m}$).</li>
                        <li><strong class="text-stone-200">Πηγή Φωτός:</strong> LED / VCSEL (μήκος κύματος $850\\text{ nm}$).</li>
                        <li><strong class="text-amber-300">Τροπική Διασπορά:</strong> Πολλαπλές φωτεινές ακτίνες ανακλώνται με διαφορετικές γωνίες και φτάνουν σε διαφορετικούς χρόνους (Pulse Spreading).</li>
                        <li><strong class="text-red-400">Εμβέλεια:</strong> Περιορίζεται σε μικρές αποστάσεις (έως 300 – 550m σε Data Centers / LAN κτιρίων).</li>
                    </ul>
                    """)

        # =========================================================================
        # SECTION 3: Shannon Capacity & Radio Propagation
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-square-root-variable text-emerald-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">3. Θεώρημα Χωρητικότητας Shannon & Διάδοση Ραδιοκυμάτων</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs"):
                with ui.column().classes("p-4 rounded-xl bg-[#141413] border border-[rgba(16,185,129,0.3)] gap-2"):
                    ui.label("Θεώρημα Χωρητικότητας Καναλιού Shannon").classes("font-bold text-emerald-400 text-sm")
                    ui.html("""
                    <div class="formula-box text-xs mb-2">
                        $$C = B \\cdot \\log_2\\left(1 + \\text{SNR}\\right) = B \\cdot \\log_2\\left(1 + \\frac{S}{N}\\right)$$
                    </div>
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">C:</strong> Θεωρητική μέγιστη χωρητικότητα καναλιού (bps).</li>
                        <li><strong class="text-stone-200">B:</strong> Εύρος ζώνης συχνοτήτων (Bandwidth σε Hz).</li>
                        <li><strong class="text-stone-200">SNR:</strong> Λόγος ισχύος σήματος προς θόρυβο ($S/N$ ως γραμμικός λόγος, $\\text{SNR}_{\\text{dB}} = 10 \\log_{10}(S/N)$).</li>
                        <li><strong class="text-stone-200">Θεώρημα Nyquist (χωρίς θόρυβο):</strong> $$C_{\\text{max}} = 2B \\cdot \\log_2(M)$$</li>
                    </ul>
                    """)

                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(79,142,201,0.3)] gap-2"):
                    ui.label("Μηχανισμοί Διάδοσης Ασύρματων Σημάτων").classes("font-bold text-blue-300 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1.5 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Ανάκλαση (Reflection):</strong> Πρόσπτωση σε επιφάνειες με διαστάσεις πολύ μεγαλύτερες από το μήκος κύματος (π.χ. κτίρια, έδαφος).</li>
                        <li><strong class="text-stone-200">Περίθλαση (Diffraction):</strong> Κάμψη των κυμάτων γύρω από αδιαφανείς ακμές εμποδίων (Shadowing).</li>
                        <li><strong class="text-stone-200">Σκέδαση (Scattering):</strong> Διάχυση σε αντικείμενα με διαστάσεις τάξης μεγέθους μήκους κύματος (σταγόνες βροχής, φύλλα).</li>
                        <li><strong class="text-stone-200">Απώλεια Ελεύθερου Χώρου (Path Loss):</strong> Η ισχύς μειώνεται αναλογικά με το τετράγωνο της απόστασης ($1/d^2$).</li>
                    </ul>
                    """)
