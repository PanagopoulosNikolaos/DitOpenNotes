"""Topic 4: Access Technologies (Τεχνολογίες Πρόσβασης) theory renderer.

Covers Home Access (DSL/ADSL/VDSL, Cable HFC DOCSIS, FTTH PON/OLT/ONT),
Enterprise Access (Ethernet 802.3, Wi-Fi 802.11 a/b/g/n/ac/ax/be, CSMA/CA, RTS/CTS),
Mobile/Cellular (4G LTE, 5G NR eMBB/URLLC/mMTC, Network Slicing), and Satellites.
"""

from nicegui import ui


def renderTopic4AccessTechnologies() -> None:
    """Renders the comprehensive theory module for Topic 4: Access Technologies."""
    with ui.column().classes("w-full gap-6 text-[#f4f1ea] latex-target"):
        # Header Banner
        with ui.column().classes(
            "w-full glass-panel p-6 md:p-8 rounded-2xl border border-[rgba(224,107,58,0.35)] gap-3"
        ):
            with ui.row().classes("items-center gap-3"):
                ui.html('<i class="fa-solid fa-wifi text-[#e06b3a] text-3xl"></i>')
                with ui.column().classes("gap-0"):
                    ui.html('<h2 class="text-xl md:text-2xl font-bold gradient-title m-0">Θέμα 4: Τεχνολογίες Πρόσβασης (Access Technologies)</h2>')
                    ui.label(
                        "Οικιακή Πρόσβαση (DSL, HFC Cable, FTTH PON), Εταιρική Πρόσβαση (Ethernet, Wi-Fi 802.11), "
                        "Κινητή Τηλεφωνία (4G LTE, 5G NR, Network Slicing) και Δορυφορικά Δίκτυα."
                    ).classes("text-xs md:text-sm text-[#b5b0a4]")

        # =========================================================================
        # SECTION 1: Residential Access Technologies
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-house-signal text-amber-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">1. Οικιακές Τεχνολογίες Πρόσβασης (DSL, HFC Cable, FTTH)</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-3 gap-4 w-full text-xs"):
                # DSL Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(224,107,58,0.3)] gap-2"):
                    ui.label("DSL / VDSL (Χαλκός Τηλεφωνίας)").classes("font-bold text-[#e06b3a] text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1.5 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Υποδομή:</strong> Υφιστάμενο συνεστραμμένο ζεύγος χαλκού (τηλεφωνική γραμμή).</li>
                        <li><strong class="text-stone-200">Διαμόρφωση:</strong> DMT (Discrete Multi-Tone) σε διαφορετικές συχνότητες (Φωνή: 0-4 kHz, Upstream: 25-138 kHz, Downstream: 138-1104 kHz).</li>
                        <li><strong class="text-stone-200">Κέντρο:</strong> <strong>DSLAM</strong> (DSL Access Multiplexer) στο αστικό κέντρο του ISP.</li>
                        <li><strong class="text-amber-300">Περιορισμός:</strong> Αποκλειστική γραμμή (dedicated), αλλά η ταχύτητα πέφτει εκθετικά με την απόσταση (&gt; 3-5 km).</li>
                    </ul>
                    """)

                # HFC Cable Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(245,158,11,0.3)] gap-2"):
                    ui.label("HFC Cable (DOCSIS)").classes("font-bold text-amber-400 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1.5 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Υποδομή:</strong> Υβριδικό δίκτυο: Οπτική ίνα μέχρι τον κόμβο γειτονιάς (Fiber Node) και ομοαξονικό καλώδιο στα σπίτια.</li>
                        <li><strong class="text-stone-200">Πρωτόκολλο:</strong> <strong>DOCSIS</strong> (Data Over Cable Service Interface Specification).</li>
                        <li><strong class="text-stone-200">Κέντρο:</strong> <strong>CMTS</strong> (Cable Modem Termination System) στο headend.</li>
                        <li><strong class="text-red-400">Περιορισμός:</strong> Κοινόχρηστο μέσο (Shared Medium) — αν πολλοί γείτονες κατεβάζουν ταυτόχρονα, το bandwidth ανά χρήστη μειώνεται.</li>
                    </ul>
                    """)

                # FTTH Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(16,185,129,0.3)] gap-2"):
                    ui.label("FTTH (Fiber to the Home - PON)").classes("font-bold text-emerald-400 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1.5 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Υποδομή:</strong> Οπτική ίνα 100% από το κέντρο μέχρι την πρίζα του σπιτιού.</li>
                        <li><strong class="text-stone-200">Αρχιτεκτονική:</strong> <strong>PON</strong> (Passive Optical Network). Μηδενική ανάγκη για ρεύμα στο δρόμο.</li>
                        <li><strong class="text-stone-200">Εξαρτήματα:</strong> <strong>OLT</strong> (Optical Line Terminal) στο κέντρο, Παθητικοί Διαχωριστές (Splitters 1:32 / 1:64), και <strong>ONT</strong> (Optical Network Terminal) στο σπίτι.</li>
                        <li><strong class="text-emerald-300">Πλεονέκτημα:</strong> Τεράστια συμμετρική ταχύτητα (1-10 Gbps), μηδενική εξασθένιση απόστασης.</li>
                    </ul>
                    """)

        # =========================================================================
        # SECTION 2: Enterprise & Wireless Access (Ethernet & Wi-Fi)
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-building text-blue-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">2. Εταιρική & Ασύρματη Πρόσβαση (Ethernet & Wi-Fi)</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs"):
                # Ethernet Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(79,142,201,0.3)] gap-2"):
                    ui.label("Ενσύρματο Ethernet (IEEE 802.3)").classes("font-bold text-blue-300 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1.5 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Τοπολογία:</strong> Αστέρα (Star Topology) με κεντρικό Switch.</li>
                        <li><strong class="text-stone-200">Καλωδίωση:</strong> Συνεστραμμένο ζεύγος UTP/STP (Cat5e: 1 Gbps, Cat6/6a: 10 Gbps) μήκους έως 100 μέτρα.</li>
                        <li><strong class="text-stone-200">Full-Duplex:</strong> Ξεχωριστά ζεύγη για αποστολή (Tx) και λήψη (Rx) $\\rightarrow$ Μηδενικές συγκρούσεις στα σύγχρονα switches.</li>
                        <li><strong class="text-stone-200">CSMA/CD:</strong> Χρησιμοποιούνταν μόνο σε παλιά Shared Hubs/Bus τοπολογίες ($L_{\\text{min}} \\ge 2 \\cdot t_{\\text{prop}} \\cdot R$).</li>
                    </ul>
                    """)

                # Wi-Fi Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(245,158,11,0.3)] gap-2"):
                    ui.label("Ασύρματο Wi-Fi (IEEE 802.11)").classes("font-bold text-amber-300 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1.5 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Συχνότητες:</strong> 2.4 GHz (μεγάλη εμβέλεια, παρεμβολές), 5 GHz (υψηλότερη ταχύτητα), 6 GHz (Wi-Fi 6E/7).</li>
                        <li><strong class="text-stone-200">Πρωτόκολλο CSMA/CA:</strong> Αποφυγή συγκρούσεων (Collision Avoidance) με τυχαίο Backoff timer.</li>
                        <li><strong class="text-stone-200">Πρόβλημα Κρυμμένου Σταθμού (Hidden Terminal):</strong> Δύο σταθμοί εκτός εμβέλειας μεταξύ τους εκπέμπουν ταυτόχρονα στο Access Point (AP).</li>
                        <li><strong class="text-amber-300">Λύση:</strong> Μηχανισμός χειραψίας ελέγχου <strong>RTS / CTS</strong> (Request to Send / Clear to Send).</li>
                    </ul>
                    """)

        # =========================================================================
        # SECTION 3: Mobile & 5G Cellular Networks
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-tower-cell text-emerald-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">3. Κινητή Τηλεφωνία & 5G NR (New Radio)</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-3 gap-3 w-full text-xs"):
                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(16,185,129,0.25)] gap-1.5"):
                    ui.label("eMBB (Enhanced Mobile Broadband)").classes("font-bold text-emerald-400")
                    ui.label(
                        "• Τεράστιες ταχύτητες δεδομένων (έως 10-20 Gbps peak).\n"
                        "• Χρήση κυμάτων χιλιοστού (mmWave) και μαζικού MIMO (Multiple Input Multiple Output).\n"
                        "• Στοχεύει σε 4K/8K video streaming, AR/VR και πυκνοκατοικημένες περιοχές."
                    ).classes("text-[#b5b0a4] leading-relaxed")

                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(239,68,68,0.25)] gap-1.5"):
                    ui.label("URLLC (Ultra-Reliable Low-Latency)").classes("font-bold text-red-400")
                    ui.label(
                        "• Εξαιρετικά χαμηλή καθυστέρηση στον αέρα (< 1 ms).\n"
                        "• Αξιοπιστία 99.999% (five-nines) για κρίσιμες εφαρμογές.\n"
                        "• Στοχεύει σε αυτόνομη οδήγηση, τηλεχειρουργική και βιομηχανικό αυτοματισμό (Industry 4.0)."
                    ).classes("text-[#b5b0a4] leading-relaxed")

                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(79,142,201,0.25)] gap-1.5"):
                    ui.label("mMTC & Network Slicing").classes("font-bold text-blue-400")
                    ui.label(
                        "• mMTC: Υποστήριξη έως 1.000.000 συσκευών IoT ανά τετραγωνικό χιλιόμετρο.\n"
                        "• Network Slicing: Δημιουργία εικονικών, απομονωμένων λογικών δικτύων πάνω στην ίδια φυσική υποδομή για διαφορετικές απαιτήσεις SLA."
                    ).classes("text-[#b5b0a4] leading-relaxed")
