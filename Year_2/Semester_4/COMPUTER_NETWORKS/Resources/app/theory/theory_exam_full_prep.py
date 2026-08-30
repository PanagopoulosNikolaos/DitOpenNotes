"""Comprehensive Exam Preparation Guide (Πλήρης Οδηγός Προετοιμασίας Εξετάσεων).

Synthesizes all essential networking theory, mathematical formulas, fast mental calculation tricks,
decision matrices, routing algorithms, Cisco IOS configurations, and common exam pitfalls.
"""

from nicegui import ui


def renderTheoryExamFullPrep() -> None:
    """Renders the master exam preparation guide with synthesized formulas and matrices."""
    with ui.column().classes("w-full gap-6 text-[#f4f1ea] latex-target"):
        # Header Banner
        with ui.column().classes(
            "w-full glass-panel p-6 md:p-8 rounded-2xl border border-[rgba(224,107,58,0.4)] gap-3"
        ):
            with ui.row().classes("items-center gap-3"):
                ui.html('<i class="fa-solid fa-graduation-cap text-[#e06b3a] text-3xl md:text-4xl"></i>')
                with ui.column().classes("gap-0"):
                    ui.html(
                        '<h2 class="text-xl md:text-2xl font-black gradient-title m-0">'
                        "Πλήρης Οδηγός Προετοιμασίας Εξετάσεων (10/10 Exam Cheat Sheet)"
                        "</h2>"
                    )
                    ui.label(
                        "Συγκεντρωτικό τυπολόγιο με υποστήριξη LaTeX, πίνακες απόφασης, βήμα-προς-βήμα αλγόριθμοι, "
                        "εντολές Cisco IOS και κρίσιμα σημεία προσοχής για άριστη επίδοση στις εξετάσεις."
                    ).classes("text-xs md:text-sm text-[#b5b0a4]")

        # =========================================================================
        # SECTION 1: Fundamental Concepts, Architecture & Encapsulation
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-5"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-layer-group text-amber-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">1. Θεμελιώδεις Έννοι, Αρχιτεκτονική & Ενθυλάκωση</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs"):
                # Transmission Modes Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(224,107,58,0.25)] gap-2"):
                    ui.label("Τρόποι Ανταλλαγής Δεδομένων (Data Transmission Modes)").classes("font-bold text-[#e06b3a] text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Simplex (Μονοδρομική):</strong> Επικοινωνία μόνο προς 1 κατεύθυνση (π.χ. Τηλεόραση, Ραδιόφωνο).</li>
                        <li><strong class="text-stone-200">Half-Duplex (Ημιδιπλή):</strong> Επικοινωνία και προς τις 2 κατευθύνσεις, αλλά <em>όχι ταυτόχρονα</em> (π.χ. Walkie-Talkie).</li>
                        <li><strong class="text-stone-200">Full-Duplex (Πλήρως Διπλή):</strong> Επικοινωνία και προς τις 2 κατευθύνσεις <em>ταυτόχρονα</em> (π.χ. Τηλεφωνία, Full-Duplex Ethernet).</li>
                    </ul>
                    <div class="mt-2 p-2 rounded bg-[#141413] text-amber-300 font-semibold">
                        Προσοχή: Η Πολυπλεξία (Multiplexing - FDM/TDM) ΔΕΝ είναι τρόπος ανταλλαγής αλλά τεχνική συνένωσης σημάτων!
                    </div>
                    """)

                # OSI Layer & Devices Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(79,142,201,0.25)] gap-2"):
                    ui.label("Μοντέλο OSI, Επίπεδα & Συσκευές").classes("font-bold text-blue-400 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Layer 1 (Physical):</strong> Επαναλήπτης (Repeater), Διανομέας (Hub). Διαχειρίζονται bits χωρίς κατανόηση διευθύνσεων.</li>
                        <li><strong class="text-stone-200">Layer 2 (Data Link):</strong> Γέφυρα (Bridge), Μεταγωγέας (Switch). PDU: <em>Frame</em>. Διευθύνσεις MAC.</li>
                        <li><strong class="text-stone-200">Layer 3 (Network):</strong> Δρομολογητής (Router). PDU: <em>Packet / Datagram</em>. Διευθύνσεις IP.</li>
                        <li><strong class="text-stone-200">Layer 4 (Transport):</strong> TCP / UDP, Θύρες (Ports). PDU: <em>Segment</em>.</li>
                        <li><strong class="text-stone-200">Peer Processes (Ομότιμες):</strong> Διαδικασίες στο <em>ίδιο επίπεδο</em> σε διαφορετικούς κόμβους.</li>
                    </ul>
                    """)

                # Encapsulation & Address Behavior Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(16,185,129,0.25)] gap-2"):
                    ui.label("Ενθυλάκωση Δεδομένων & Μεταβολή Διευθύνσεων").classes("font-bold text-emerald-400 text-sm")
                    ui.html("""
                    <div class="formula-box text-xs mb-2">
                        $$\\text{Message} \\xrightarrow{\\text{L4}} \\text{Segment} \\xrightarrow{\\text{L3}} \\text{Packet} \\xrightarrow{\\text{L2}} \\text{Frame} \\xrightarrow{\\text{L1}} \\text{Bits}$$
                    </div>
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">IP Διεύθυνση (Layer 3):</strong> Παραμένει <em>σταθερή</em> από άκρο σε άκρο (εκτός NAT).</li>
                        <li><strong class="text-stone-200">MAC Διεύθυνση (Layer 2):</strong> <em>Αλλάζει σε κάθε hop</em> (κάθε router βάζει δικό του Source MAC και MAC επόμενου κόμβου).</li>
                    </ul>
                    """)

                # Control Plane vs Data Plane & Domains Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(245,158,11,0.25)] gap-2"):
                    ui.label("Control Plane vs Data Plane & Πεδία (Domains)").classes("font-bold text-amber-400 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Control Plane (Software):</strong> Υπολογισμός διαδρομών (OSPF, RIP, BGP) $\\rightarrow$ Πίνακας RIB.</li>
                        <li><strong class="text-stone-200">Data Plane (Hardware/ASIC):</strong> Προώθηση πακέτων νανοδευτερολέπτων $\\rightarrow$ Πίνακας FIB.</li>
                        <li><strong class="text-stone-200">Collision Domain:</strong> Κάθε θύρα Switch είναι ξεχωριστό collision domain. Στο Hub όλοι μοιράζονται το ίδιο.</li>
                        <li><strong class="text-stone-200">Broadcast Domain:</strong> Κάθε θύρα Router ορίζει ξεχωριστό broadcast domain.</li>
                    </ul>
                    """)

        # =========================================================================
        # SECTION 2: Master Formula Sheet & Delay Calculations
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-5"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-square-root-variable text-amber-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">2. Συγκεντρωτικό Τυπολόγιο Υπολογισμού Καθυστερήσεων & Χωρητικότητας</h3>')

            # Master Nodal Delay Formula Box
            with ui.column().classes("w-full p-4 rounded-xl bg-[#141413] border border-[rgba(224,107,58,0.35)] gap-2"):
                ui.label("Κομβική Καθυστέρηση (Nodal Delay)").classes("font-bold text-[#e06b3a] text-sm")
                ui.html("""
                <div class="formula-box text-sm">
                    $$d_{\\text{nodal}} = d_{\\text{proc}} + d_{\\text{queue}} + d_{\\text{trans}} + d_{\\text{prop}}$$
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-3 mt-2 text-xs text-[#b5b0a4]">
                    <div>
                        <strong class="text-stone-200">Μετάδοση (Transmission):</strong> $$d_{\\text{trans}} = \\frac{L}{R}$$
                        <br><span class="text-[#78756d]">L: bits πακέτου, R: ρυθμός μετάδοσης (bps). Εξαρτάται ΜΟΝΟ από μέγεθος και bandwidth.</span>
                    </div>
                    <div>
                        <strong class="text-stone-200">Διάδοση (Propagation):</strong> $$d_{\\text{prop}} = \\frac{l}{u}$$
                        <br><span class="text-[#78756d]">l: απόσταση (m), u: ταχύτητα ($2\\times 10^8\\text{ m/s}$ σε χαλκό/ίνα, $3\\times 10^8\\text{ m/s}$ σε αέρα).</span>
                    </div>
                </div>
                """)

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs"):
                # Multi-hop & Pipelining Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(16,185,129,0.3)] gap-2"):
                    ui.label("Store-and-Forward & Pipelining Πολλαπλών Πακέτων").classes("font-bold text-emerald-400 text-sm")
                    ui.html("""
                    <div class="formula-box text-xs mb-2">
                        $$T_{\\text{total}} = (N + P - 1) \\cdot \\frac{L}{R} + N \\cdot \\frac{l}{u} + (N-1) \\cdot d_{\\text{proc}}$$
                    </div>
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">N:</strong> Πλήθος ζεύξεων (hops) — <em>όχι πλήθος routers!</em> (π.χ. $A \\rightarrow R_1 \\rightarrow R_2 \\rightarrow B \\Rightarrow N=3$ hops).</li>
                        <li><strong class="text-stone-200">P:</strong> Πλήθος τεμαχισμένων πακέτων.</li>
                        <li><strong class="text-stone-200">1 Πακέτο:</strong> $$T_1 = N \\cdot \\left(\\frac{L}{R} + \\frac{l}{u}\\right)$$</li>
                    </ul>
                    """)

                # BDP & AM Exam Formula Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(245,158,11,0.3)] gap-2"):
                    ui.label("Γινόμενο Bandwidth-Delay (BDP) & Θέμα Α.Μ.").classes("font-bold text-amber-400 text-sm")
                    ui.html("""
                    <div class="formula-box text-xs mb-2">
                        $$\\text{BDP (Max Bits)} = R \\times d_{\\text{prop}} = (8000 \\cdot N) \\times (d \\cdot 10^{-3}) = 8 \\cdot N \\cdot d \\text{ bits}$$
                    </div>
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">N (Bandwidth):</strong> Αριθμός Μητρώου (KB/s) $\\rightarrow N \\times 1000 \\times 8\\text{ bps}$.</li>
                        <li><strong class="text-stone-200">d (Delay):</strong> Τελευταίο ψηφίο ΑΜ σε ms (αν $d=0 \\Rightarrow 5\\text{ ms}$ ή $6\\text{ ms}$).</li>
                        <li><strong class="text-stone-200">Sliding Window Condition:</strong> $$W \\ge R \\times \\text{RTT}$$ για 100% αξιοποίηση.</li>
                    </ul>
                    """)

                # Multi-hop RTT Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(79,142,201,0.3)] gap-2"):
                    ui.label("Υπολογισμός RTT σε Πολυ-κομβικές Διαδρομές").classes("font-bold text-blue-400 text-sm")
                    ui.html("""
                    <div class="formula-box text-xs mb-2">
                        $$\\text{RTT}_{A-C} = 2 \\cdot (d_{\\text{trans1}} + d_{\\text{prop1}} + d_{\\text{trans2}} + d_{\\text{prop2}}) + 3 \\cdot d_{\\text{proc}}$$
                    </div>
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li>Διαδρομή: $A \\xrightarrow{\\text{proc B}} B \\xrightarrow{\\text{proc C}} C \\xrightarrow{\\text{proc B}} B \\rightarrow A$.</li>
                        <li>Περιλαμβάνει 3 επεξεργασίες: στον $B$ (μετάβαση), στον $C$ (τερματισμός/αναστροφή), στον $B$ (επιστροφή).</li>
                    </ul>
                    """)

                # Traffic Intensity & Bottleneck Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(239,68,68,0.3)] gap-2"):
                    ui.label("Ένταση Κίνησης & Στενωπός (Bottleneck)").classes("font-bold text-red-400 text-sm")
                    ui.html("""
                    <div class="formula-box text-xs mb-2">
                        $$I = \\frac{L \\cdot a}{R}, \\quad \\text{Throughput} = \\min(R_1, R_2, \\dots, R_N)$$
                    </div>
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">I ~ 0:</strong> Μηδενική καθυστέρηση ουράς ($d_{\\text{queue}} \\approx 0$).</li>
                        <li><strong class="text-stone-200">I $\\rightarrow$ 1:</strong> Εκθετική αύξηση καθυστέρησης ουράς.</li>
                        <li><strong class="text-stone-200">I > 1:</strong> Άπειρη ουρά, βέβαιη απώλεια πακέτων (Packet Drop).</li>
                    </ul>
                    """)

        # =========================================================================
        # SECTION 3: Subnetting, CIDR & Longest Prefix Match (LPM)
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-5"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-network-wired text-emerald-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">3. Υποδικτύωση (Subnetting), CIDR & Longest Prefix Match (LPM)</h3>')

            # CIDR Subnetting Reference Table
            with ui.column().classes("w-full p-4 rounded-xl bg-[#201f1d] border border-[rgba(255,255,255,0.08)] gap-3"):
                ui.label("Πίνακας Μασκών Υποδικτύου & Wildcard Masks (Cisco OSPF)").classes("font-bold text-amber-300 text-sm")
                ui.html("""
                <div class="overflow-x-auto">
                    <table class="w-full text-left text-xs border-collapse">
                        <thead>
                            <tr class="border-b border-[rgba(255,255,255,0.1)] text-[#e06b3a]">
                                <th class="py-2 px-3">CIDR</th>
                                <th class="py-2 px-3">Subnet Mask</th>
                                <th class="py-2 px-3">Wildcard Mask</th>
                                <th class="py-2 px-3">Block Size ($2^{32-n}$)</th>
                                <th class="py-2 px-3">Ωφέλιμοι Hosts ($2^{32-n}-2$)</th>
                                <th class="py-2 px-3">Τυπική Χρήση</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-[rgba(255,255,255,0.05)] text-[#b5b0a4]">
                            <tr><td class="py-1.5 px-3 font-mono text-stone-200">/24</td><td class="py-1.5 px-3 font-mono">255.255.255.0</td><td class="py-1.5 px-3 font-mono text-amber-300">0.0.0.255</td><td class="py-1.5 px-3">256</td><td class="py-1.5 px-3 text-emerald-400 font-bold">254</td><td class="py-1.5 px-3">Standard LAN</td></tr>
                            <tr><td class="py-1.5 px-3 font-mono text-stone-200">/26</td><td class="py-1.5 px-3 font-mono">255.255.255.192</td><td class="py-1.5 px-3 font-mono text-amber-300">0.0.0.63</td><td class="py-1.5 px-3">64</td><td class="py-1.5 px-3 text-emerald-400 font-bold">62</td><td class="py-1.5 px-3">Τμήμα κτιρίου</td></tr>
                            <tr><td class="py-1.5 px-3 font-mono text-stone-200">/28</td><td class="py-1.5 px-3 font-mono">255.255.255.240</td><td class="py-1.5 px-3 font-mono text-amber-300">0.0.0.15</td><td class="py-1.5 px-3">16</td><td class="py-1.5 px-3 text-emerald-400 font-bold">14</td><td class="py-1.5 px-3">Μικρό subnet servers</td></tr>
                            <tr><td class="py-1.5 px-3 font-mono text-stone-200">/29</td><td class="py-1.5 px-3 font-mono">255.255.255.248</td><td class="py-1.5 px-3 font-mono text-amber-300">0.0.0.7</td><td class="py-1.5 px-3">8</td><td class="py-1.5 px-3 text-emerald-400 font-bold">6</td><td class="py-1.5 px-3">DMZ / Switch interconnect</td></tr>
                            <tr><td class="py-1.5 px-3 font-mono text-stone-200">/30</td><td class="py-1.5 px-3 font-mono">255.255.255.252</td><td class="py-1.5 px-3 font-mono text-amber-300">0.0.0.3</td><td class="py-1.5 px-3">4</td><td class="py-1.5 px-3 text-emerald-400 font-bold">2</td><td class="py-1.5 px-3">Point-to-Point Router Link</td></tr>
                        </tbody>
                    </table>
                </div>
                """)

            # LPM Step-by-Step Box
            with ui.column().classes("w-full p-4 rounded-xl bg-[#201f1d] border border-[rgba(16,185,129,0.3)] gap-2 text-xs"):
                ui.label("Κανόνας Longest Prefix Match (LPM) - Αποφάσεις Προώθησης").classes("font-bold text-emerald-400 text-sm")
                ui.label("Ο router επιλέγει την εγγραφή με το ΜΕΓΑΛΥΤΕΡΟ μήκος προθέματος (περισσότερα bits '1' στη μάσκα).").classes("text-[#b5b0a4]")
                ui.html("""
                <div class="p-3 rounded bg-[#141413] border border-[rgba(255,255,255,0.06)] font-mono space-y-1">
                    <div>1. <span class="text-blue-300">10.15.0.0/16</span> $\\rightarrow$ Eth0</div>
                    <div>2. <span class="text-amber-300">10.15.20.0/24</span> $\\rightarrow$ Eth1</div>
                    <div>3. <span class="text-emerald-300">10.15.20.128/25</span> $\\rightarrow$ Eth2</div>
                    <div>4. <span class="text-stone-400">0.0.0.0/0 (Default)</span> $\\rightarrow$ Eth3</div>
                </div>
                <ul class="m-0 pl-4 mt-2 space-y-1 text-[#b5b0a4]">
                    <li>IP <code class="text-stone-200">10.15.20.200</code>: Ταιριάζει με /16, /24, /25 $\\rightarrow$ <strong>Eth2 (/25 LPM)</strong></li>
                    <li>IP <code class="text-stone-200">10.15.20.50</code>: Ταιριάζει με /16, /24 $\\rightarrow$ <strong>Eth1 (/24 LPM)</strong></li>
                    <li>IP <code class="text-stone-200">10.15.21.5</code>: Ταιριάζει μόνο με /16 $\\rightarrow$ <strong>Eth0 (/16 LPM)</strong></li>
                    <li>IP <code class="text-stone-200">192.168.1.1</code>: Δεν ταιριάζει $\\rightarrow$ <strong>Eth3 (Default)</strong></li>
                </ul>
                """)

        # =========================================================================
        # SECTION 4: Data Link Layer & Error Control
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-5"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-shield-halved text-blue-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">4. Επίπεδο Ζεύξης Δεδομένων & Έλεγχος Σφαλμάτων (CSMA, Hamming, CRC)</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs"):
                # CSMA/CD vs CSMA/CA Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(79,142,201,0.3)] gap-2"):
                    ui.label("CSMA/CD (Ethernet) vs CSMA/CA (Wi-Fi)").classes("font-bold text-blue-300 text-sm")
                    ui.html("""
                    <div class="formula-box text-xs mb-2">
                        $$L_{\\text{min}} \\ge 2 \\cdot t_{\\text{prop}} \\cdot R = 2 \\cdot \\left(\\frac{l}{u}\\right) \\cdot R$$
                    </div>
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">CSMA/CD (802.3):</strong> Ανίχνευση σύγκρουσης κατά τη μετάδοση. Αν συμβεί σύγκρουση: Jam Signal + Exponential Backoff.</li>
                        <li><strong class="text-stone-200">CSMA/CA (802.11):</strong> Στο ασύρματο η ανίχνευση είναι αδύνατη (Hidden Terminal). Χρησιμοποιείται <em>αποφυγή</em> με Backoff timer και προαιρετικά <strong>RTS/CTS</strong>.</li>
                    </ul>
                    """)

                # Hamming Code Calculation Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(245,158,11,0.3)] gap-2"):
                    ui.label("Κώδικας Hamming (Single Error Correction)").classes("font-bold text-amber-300 text-sm")
                    ui.html("""
                    <div class="formula-box text-xs mb-2">
                        $$2^p \\ge d + p + 1 \\quad (d=8 \\Rightarrow p=4, \\text{ θέσεις } 1, 2, 4, 8)$$
                    </div>
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">$P_1$:</strong> Ελέγχει θέσεις 1, 3, 5, 7, 9, 11...</li>
                        <li><strong class="text-stone-200">$P_2$:</strong> Ελέγχει θέσεις 2, 3, 6, 7, 10, 11...</li>
                        <li><strong class="text-stone-200">$P_4$:</strong> Ελέγχει θέσεις 4, 5, 6, 7, 12...</li>
                        <li><strong class="text-stone-200">$P_8$:</strong> Ελέγχει θέσεις 8, 9, 10, 11, 12...</li>
                        <li><strong class="text-stone-200">Περιττή Ισοτιμία (Odd):</strong> Συνολικοί άσοι = περιττός αριθμός.</li>
                    </ul>
                    """)

                # CRC Modulo-2 Division Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(16,185,129,0.3)] gap-2"):
                    ui.label("Κυκλικός Έλεγχος Πλεονασμού (CRC)").classes("font-bold text-emerald-300 text-sm")
                    ui.html("""
                    <div class="formula-box text-xs mb-2">
                        $$\\text{Tx} = D \\cdot 2^r \\oplus R, \\quad R = (D \\cdot 2^r) \\bmod G$$
                    </div>
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li>Προσθέτουμε $r$ μηδενικά στο τέλος του $D$ (όπου $r = \\text{βαθμός πολυωνύμου} = \\text{μήκος } G - 1$).</li>
                        <li>Εκτελούμε διαίρεση Modulo-2 (XOR: $1\\oplus 1=0, 0\\oplus 0=0, 1\\oplus 0=1$).</li>
                        <li>Το υπόλοιπο $R$ ($r$ bits) αντικαθιστά τα μηδενικά στο τέλος.</li>
                    </ul>
                    """)

                # Checksum & Parity Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(239,68,68,0.3)] gap-2"):
                    ui.label("Parity Bits & Internet Checksum").classes("font-bold text-red-300 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Parity Bits:</strong> Αποκλειστικά για <em>ανίχνευση</em> σφαλμάτων 1 bit (ΔΕΝ διορθώνουν).</li>
                        <li><strong class="text-stone-200">Internet Checksum (IP/UDP/TCP):</strong> Άθροισμα λέξεων 16-bit με συμπλήρωμα ως προς 1 (1's complement addition) και αντιστροφή bits στο τέλος.</li>
                    </ul>
                    """)

        # =========================================================================
        # SECTION 5: ARP Protocol & Diagnostics
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-5"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-magnifying-glass text-cyan-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">5. Πρωτόκολλο ARP & Διαγνωστικά Εργαλεία (Traceroute)</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs"):
                # ARP Exchange Structure Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(6,182,212,0.3)] gap-2"):
                    ui.label("Δομή Μηνυμάτων ARP Request & Reply").classes("font-bold text-cyan-300 text-sm")
                    ui.html("""
                    <div class="p-2.5 rounded bg-[#141413] border border-[rgba(255,255,255,0.06)] font-mono space-y-1 text-xs">
                        <div class="text-amber-300 font-bold">ARP Request (Broadcast -> FF-FF-FF-FF-FF-FF):</div>
                        <div>Sender MAC: <span class="text-stone-200">71-65-F7-2B-08-53</span>, IP: <span class="text-stone-200">137.196.7.23</span></div>
                        <div>Target MAC: <span class="text-red-400">00-00-00-00-00-00</span>, IP: <span class="text-stone-200">137.196.7.14</span></div>
                        <div class="text-emerald-300 font-bold mt-2">ARP Reply (Unicast απευθείας στον Α):</div>
                        <div>Sender MAC: <span class="text-emerald-400">58-23-D7-FA-20-B0</span>, IP: <span class="text-stone-200">137.196.7.14</span></div>
                        <div>Target MAC: <span class="text-stone-200">71-65-F7-2B-08-53</span>, IP: <span class="text-stone-200">137.196.7.23</span></div>
                    </div>
                    <ul class="m-0 pl-4 mt-2 space-y-1 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">ARP Cache:</strong> Αποθηκεύει τις αντιστοιχίσεις για 15-20 λεπτά. Αν σταλεί πακέτο μετά από 5 λεπτά, <em>ΔΕΝ στέλνεται νέο ARP</em>!</li>
                        <li><strong class="text-stone-200">Εκτός LAN:</strong> Αν η IP προορισμού είναι εκτός τοπικού δικτύου, στέλνεται ARP request για τη MAC της <em>Default Gateway</em>.</li>
                    </ul>
                    """)

                # Traceroute Mechanism Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(6,182,212,0.3)] gap-2"):
                    ui.label("Εργαλείο Traceroute & Μηχανισμός TTL").classes("font-bold text-cyan-300 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-2 text-[#b5b0a4]">
                        <li>1. Αποστέλλει σειρά πακέτων IP με <strong class="text-stone-200">TTL = 1</strong>.</li>
                        <li>2. Ο 1ος router μειώνει το TTL σε 0, απορρίπτει το πακέτο και επιστρέφει μήνυμα σφάλματος <strong class="text-amber-300">ICMP Time Exceeded (Type 11)</strong>, αποκαλύπτοντας την IP του.</li>
                        <li>3. Η πηγή αυξάνει σε <strong class="text-stone-200">TTL = 2, 3...</strong> μέχρι να φτάσει στον προορισμό, ο οποίος απαντά με <strong class="text-emerald-300">ICMP Port Unreachable (Type 3)</strong> ή Echo Reply.</li>
                    </ul>
                    """)

        # =========================================================================
        # SECTION 6: Routing Protocols & Algorithms
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-5"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-route text-amber-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">6. Αλγόριθμοι & Πρωτόκολλα Δρομολόγησης (Dijkstra, Bellman-Ford, Cisco IOS)</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs"):
                # Link-State vs Distance Vector Comparison Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(245,158,11,0.3)] gap-2"):
                    ui.label("Link State (Dijkstra) vs Distance Vector (Bellman-Ford)").classes("font-bold text-amber-300 text-sm")
                    ui.html("""
                    <div class="overflow-x-auto">
                        <table class="w-full text-left text-xs border-collapse">
                            <thead>
                                <tr class="border-b border-[rgba(255,255,255,0.1)] text-[#e06b3a]">
                                    <th class="py-1 px-2">Χαρακτηριστικό</th>
                                    <th class="py-1 px-2">Link-State (LS)</th>
                                    <th class="py-1 px-2">Distance Vector (DV)</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-[rgba(255,255,255,0.05)] text-[#b5b0a4]">
                                <tr><td class="py-1 px-2 text-stone-200">Αλγόριθμος</td><td class="py-1 px-2">Dijkstra</td><td class="py-1 px-2">Bellman-Ford</td></tr>
                                <tr><td class="py-1 px-2 text-stone-200">Γνώση Τοπολογίας</td><td class="py-1 px-2">Πλήρης χάρτης σε όλους</td><td class="py-1 px-2">Μόνο άμεσοι γείτονες</td></tr>
                                <tr><td class="py-1 px-2 text-stone-200">Εξίσωση</td><td class="py-1 px-2">$D(v) = \\min(D(v), D(w)+c(w,v))$</td><td class="py-1 px-2">$d_x(y) = \\min_v \\{c(x,v)+d_v(y)\\}$</td></tr>
                                <tr><td class="py-1 px-2 text-stone-200">Πρωτόκολλα</td><td class="py-1 px-2 text-emerald-400">OSPF, IS-IS</td><td class="py-1 px-2 text-blue-400">RIP (max 15 hops)</td></tr>
                                <tr><td class="py-1 px-2 text-stone-200">Προβλήματα</td><td class="py-1 px-2">Υψηλή χρήση CPU/RAM</td><td class="py-1 px-2 text-red-400">Count-to-Infinity</td></tr>
                            </tbody>
                        </table>
                    </div>
                    """)

                # DV Loop Solutions & BGP Hot-Potato Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(224,107,58,0.3)] gap-2"):
                    ui.label("Αντιμετώπιση Βρόχων DV & BGP Hot-Potato").classes("font-bold text-[#e06b3a] text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Split Horizon:</strong> Δεν διαφημίζουμε πίσω σε έναν γείτονα μια διαδρομή που μάθαμε από αυτόν.</li>
                        <li><strong class="text-stone-200">Poisoned Reverse:</strong> Αν δρομολογώ προς τον Y μέσω του Z, διαφημίζω στον Z ότι το κόστος μου προς τον Y είναι $\\infty$.</li>
                        <li><strong class="text-stone-200">BGP Hot-Potato Routing:</strong> Επιλογή της πύλης εξόδου (egress router) που είναι <em>εσωτερικά πλησιέστερη στον αποστολέα</em> (ελάχιστο κόστος IGP), ώστε να ξεφορτωθεί το AS το πακέτο άμεσα.</li>
                    </ul>
                    """)

            # Cisco IOS CLI Commands Box
            with ui.column().classes("w-full p-4 rounded-xl bg-[#141413] border border-[rgba(79,142,201,0.3)] gap-2 text-xs"):
                ui.label("Εντολές Διαμόρφωσης Δρομολογητών Cisco IOS (Θέματα Εξετάσεων)").classes("font-bold text-blue-400 text-sm")
                with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full"):
                    ui.html("""
                    <div class="p-3 rounded bg-[#201f1d] border border-[rgba(255,255,255,0.06)] font-mono">
                        <div class="text-amber-300 font-bold mb-1">// OSPF Single Area 0 (με Wildcard Masks)</div>
                        <div>R>enable</div>
                        <div>R#configure terminal</div>
                        <div>R(config)#router ospf 1</div>
                        <div>R(config-router)#network 10.10.10.0 0.0.0.3 area 0</div>
                        <div>R(config-router)#network 10.10.23.0 0.0.0.3 area 0</div>
                        <div>R(config-router)#network 172.16.8.0 0.0.0.7 area 0</div>
                        <div>R(config-router)#network 192.168.1.0 0.0.0.255 area 0</div>
                        <div>R(config-router)#end</div>
                    </div>
                    """)
                    ui.html("""
                    <div class="p-3 rounded bg-[#201f1d] border border-[rgba(255,255,255,0.06)] font-mono">
                        <div class="text-emerald-300 font-bold mb-1">// RIP version 2</div>
                        <div>R>enable</div>
                        <div>R#configure terminal</div>
                        <div>R(config)#router rip</div>
                        <div>R(config-router)#version 2</div>
                        <div>R(config-router)#no auto-summary</div>
                        <div>R(config-router)#network 10.15.2.0</div>
                        <div>R(config-router)#network 10.15.3.0</div>
                        <div>R(config-router)#network 10.15.6.0</div>
                        <div>R(config-router)#end</div>
                    </div>
                    """)

        # =========================================================================
        # SECTION 7: Transport Layer (TCP) & Network Security
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-5"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-arrows-split-up-and-left text-emerald-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">7. Επίπεδο Μεταφοράς (TCP Congestion Control, BBR & Ασφάλεια)</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-3 gap-4 w-full text-xs"):
                # TCP Congestion Control Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(16,185,129,0.3)] gap-2"):
                    ui.label("Έλεγχος Συμφόρησης TCP").classes("font-bold text-emerald-300 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Slow Start:</strong> $CWND$ διπλασιάζεται κάθε RTT ($1 \\rightarrow 2 \\rightarrow 4...$) μέχρι το `ssthresh`.</li>
                        <li><strong class="text-stone-200">Congestion Avoidance:</strong> $CWND$ αυξάνεται γραμμικά κατά $+1\\text{ MSS}$ ανά RTT.</li>
                        <li><strong class="text-stone-200">Timeout:</strong> `ssthresh` = $CWND/2$, $CWND=1\\text{ MSS}$.</li>
                        <li><strong class="text-stone-200">3 Dup ACKs:</strong> Fast Recovery $\\rightarrow$ `ssthresh` = $CWND/2$, $CWND = \\text{ssthresh}$.</li>
                    </ul>
                    """)

                # TCP BBR Algorithm Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(79,142,201,0.3)] gap-2"):
                    ui.label("Αλγόριθμος TCP BBR").classes("font-bold text-blue-300 text-sm")
                    ui.html("""
                    <div class="formula-box text-xs mb-2">
                        $$CWND = RtProp \\times BtlBw$$
                    </div>
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">RtProp:</strong> $\\min(RTT)$ (π.χ. $5\\text{ ms} = 0,005\\text{ s}$).</li>
                        <li><strong class="text-stone-200">BtlBw:</strong> Ρυθμός στενωπού ($0,125\\text{ GB/s} = 10^8\\text{ B/s} = 8\\times 10^8\\text{ bps}$).</li>
                        <li><strong class="text-emerald-400">CWND:</strong> $0,005 \\times 8\\cdot 10^8 = 4.000.000\\text{ bits} \\ (500\\text{ KB})$.</li>
                    </ul>
                    """)

                # Karn's Rule & Security Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(245,158,11,0.3)] gap-2"):
                    ui.label("Κανόνας Karn & Firewalls").classes("font-bold text-amber-300 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Κανόνας Karn:</strong> Δεν λαμβάνουμε δείγματα $SampleRTT$ για πακέτα που επαναμεταδόθηκαν.</li>
                        <li><strong class="text-stone-200">RFC 7323:</strong> Timestamps Option για ακριβή υπολογισμό RTT.</li>
                        <li><strong class="text-stone-200">Stateless Firewall:</strong> Ελέγχει πακέτα μεμονωμένα (IP/Port).</li>
                        <li><strong class="text-stone-200">Stateful Inspection:</strong> Παρακολουθεί κατάσταση συνδέσεων TCP (State Table).</li>
                    </ul>
                    """)

        # =========================================================================
        # SECTION 8: 10/10 Master Exam Checklist
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-list-check text-[#e06b3a] text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">8. Ολοκληρωμένο Τσεκ-Λιστ Προετοιμασίας Εξετάσεων (10/10)</h3>')

            checklist_items = [
                "Διακρίνω Simplex, Half-Duplex, Full-Duplex και γνωρίζω ότι η Πολυπλεξία (FDM/TDM) δεν είναι τρόπος ανταλλαγής.",
                "Γνωρίζω ότι ο Repeater/Hub είναι Layer 1, το Switch Layer 2, και ο Router Layer 3.",
                "Κατανοώ ότι η IP διεύθυνση παραμένει σταθερή end-to-end ενώ η MAC αλλάζει σε κάθε hop/router.",
                "Διακρίνω Control Plane (Software / RIB) και Data Plane (Hardware / ASICs / FIB).",
                "Μπορώ να υπολογίσω το Nodal Delay (d_proc + d_queue + L/R + l/u) και γνωρίζω ότι το N μετράει hops (όχι routers).",
                "Εφαρμόζω τον τύπο Pipelining P πακέτων σε N hops: T = (N + P - 1)(L/R) + N(l/u) + (N-1)d_proc.",
                "Υπολογίζω άμεσα το BDP με βάση τον Α.Μ.: Max Bits = 8 * AM * delay_ms bits.",
                "Γνωρίζω τη συνθήκη Sliding Window W >= R * RTT για 100% αξιοποίηση καναλιού.",
                "Επιλύω ασκήσεις Υποδικτύωσης (CIDR /24, /26, /28, /29, /30) και υπολογίζω ωφέλιμους hosts (2^(32-n) - 2).",
                "Εφαρμόζω τον κανόνα Longest Prefix Match (LPM) για την εύρεση της σωστής θύρας εξόδου στον router.",
                "Γνωρίζω τον τύπο L_min >= 2 * t_prop * R στο CSMA/CD και τη διαφορά με το CSMA/CA (Wi-Fi RTS/CTS).",
                "Μπορώ να κατασκευάσω κώδικα Hamming (θέσεις δυνάμεων 2, περιττή/άρτια ισοτιμία) και διαίρεση CRC (Modulo-2 XOR).",
                "Γνωρίζω ότι το ARP Request είναι Broadcast (FF-FF-FF-FF-FF-FF) και το Reply Unicast, με ARP Cache 15-20 min.",
                "Κατανοώ τη λειτουργία Traceroute με διαδοχική αύξηση TTL και απαντήσεις ICMP Time Exceeded.",
                "Διακρίνω Single-Mode Fiber (Laser, 8-10 μm, μεγάλες αποστάσεις) vs Multi-Mode Fiber (LED, 50-62.5 μm).",
                "Γνωρίζω τη διαφορά GEO δορυφόρων (36.000 km, ~250 ms) vs LEO δορυφόρων (500-1500 km, ~10-20 ms, Starlink).",
                "Μπορώ να εκτελέσω βήμα-βήμα τον αλγόριθμο Dijkstra και να υπολογίσω εξισώσεις Bellman-Ford.",
                "Κατανοώ τα προβλήματα Count-to-Infinity, Split Horizon, Poisoned Reverse και το όριο 15 hops του RIP.",
                "Γνωρίζω τις εντολές Cisco IOS για OSPF (router ospf 1, network ... wildcard area 0) και RIPv2.",
                "Γνωρίζω τη δρομολόγηση Hot-Potato στο BGP, τις φάσεις TCP Congestion Control και τον τύπο CWND = RtProp * BtlBw του BBR.",
            ]

            with ui.column().classes("w-full gap-2 text-xs leading-relaxed"):
                for item in checklist_items:
                    with ui.row().classes("items-start gap-2 p-2 rounded-lg bg-[#201f1d] border border-[rgba(255,255,255,0.04)]"):
                        ui.html('<i class="fa-solid fa-square-check text-[#e06b3a] mt-0.5"></i>')
                        ui.label(item).classes("text-[#b5b0a4]")
