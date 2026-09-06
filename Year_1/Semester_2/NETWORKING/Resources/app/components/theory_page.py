"""Comprehensive Master Theory Guide for Computer Networks exams.

Covers the complete curriculum required to score full marks on the official
exams: reference models, encapsulation, the access layer, IPv4 addressing,
subnetting/VLSM/CIDR, the internet layer protocols, fragmentation, NAT, the
transport layer (TCP/UDP, ports, sequence numbers, sliding window, congestion
control), routing algorithms, formula references, and exam traps.
"""

from nicegui import ui
from .methodology_card import renderMethodologyCards
from .methodology_table import renderMethodologyTable


def _panelHeader(icon: str, title: str, subtitle: str, color_class: str) -> None:
    """Renders the standard header row of a theory panel.

    Args:
        icon (str): FontAwesome icon class suffix.
        title (str): Panel title.
        subtitle (str): One-line panel description.
        color_class (str): Tailwind text color class for the icon.

    Returns:
        None
    """
    with ui.row().classes("items-center gap-3 border-b border-[var(--border)] pb-4 w-full"):
        ui.html(f'<i class="fa-solid fa-{icon} {color_class} text-2xl"></i>')
        with ui.column().classes("gap-0"):
            ui.html(f'<h2 class="text-lg md:text-xl font-bold text-[var(--text-1)] m-0">{title}</h2>')
            ui.label(subtitle).classes("text-xs text-[var(--text-3)] mt-1")


def _miniCard(icon: str, color: str, title: str, body: str) -> None:
    """Renders a single compact concept card inside a grid.

    Args:
        icon (str): FontAwesome icon classes.
        color (str): Tailwind border color class.
        title (str): Card title.
        body (str): Card body (may include inline KaTeX).

    Returns:
        None
    """
    with ui.column().classes(f"p-4 rounded-xl bg-[var(--card-bg-subtle)] border-l-4 {color} border border-[var(--border)] gap-1.5"):
        with ui.row().classes("items-center gap-2"):
            ui.html(f'<i class="{icon} text-sm"></i>')
            ui.label(title).classes("font-bold text-sm text-[var(--text-1)]")
        ui.label(body).classes("text-xs text-[var(--text-2)] leading-relaxed")


def renderTheoryPage() -> None:
    """Renders the complete theory, methodology, formula, and trap handbook."""
    with ui.column().classes("w-full max-w-6xl mx-auto px-4 py-8 space-y-10 print-section"):
        # Page hero banner
        with ui.column().classes(
            "w-full glass-panel p-6 md:p-8 rounded-2xl border border-[var(--border-accent)] gap-4"
        ):
            with ui.row().classes("items-center gap-3"):
                ui.html('<i class="fa-solid fa-book-open-reader text-[var(--accent)] text-2xl md:text-3xl"></i>')
                with ui.column().classes("gap-0"):
                    ui.html(
                        '<h1 class="text-2xl md:text-3xl font-black gradient-title m-0">'
                        "Πλήρης Θεωρητικός Οδηγός Δικτύων Υπολογιστών"
                        "</h1>"
                    )
                    ui.label(
                        "Ολοκληρωμένο εγχειρίδιο για πλήρη βαθμολογία στις εξετάσεις: μοντέλα αναφοράς, "
                        "διευθυνσιοδότηση IPv4/IPv6, υποδικτύωση VLSM/CIDR, κατάτμηση, TCP/UDP, "
                        "έλεγχο ροής & συμφόρησης, και αλγορίθμους δρομολόγησης."
                    ).classes("text-sm text-[var(--text-2)] mt-1")

            with ui.row().classes("gap-3 flex-wrap text-xs"):
                for icon, color, label in [
                    ("fa-layer-group", "text-blue-400", "Μοντέλα OSI & TCP/IP"),
                    ("fa-sitemap", "text-amber-400", "VLSM & CIDR Μεθοδολογία"),
                    ("fa-scissors", "text-emerald-400", "Κατάτμηση & Πρωτόκολλα Internet"),
                    ("fa-gauge-high", "text-purple-400", "TCP: Ροή & Συμφόρηση"),
                    ("fa-route", "text-rose-400", "Δρομολόγηση Dijkstra/DV"),
                ]:
                    with ui.row().classes(
                        "items-center gap-1.5 px-3 py-1.5 rounded-lg bg-[var(--badge-bg)] border border-[var(--border)] text-[var(--text-1)]"
                    ):
                        ui.html(f'<i class="fa-solid {icon} {color}"></i>')
                        ui.label(label)

        # SECTION 1: Methodology cards and exam strategy
        with ui.column().classes("w-full gap-4"):
            renderMethodologyCards()

            with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
                _panelHeader(
                    "lightbulb", "Στρατηγική Γραπτού: Πώς Γράφουμε για 10/10",
                    "Κανόνες παρουσίασης που μετατρέπουν τη σωστή λύση σε πλήρη βαθμολογία.",
                    "text-amber-500",
                )
                with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full"):
                    _miniCard(
                        "fa-solid fa-list-ol text-blue-500", "border-blue-500",
                        "Δομή Λύσης κατά Βήματα",
                        "Κάθε υπολογιστικό βήμα ξεκινά από τον governing τύπο, συνεχίζει με την υποκατάσταση "
                        "τιμών και κλείνει με αριθμητικό αποτέλεσμα. Ποτέ σκέτο αποτέλεσμα χωρίς παραγωγή.",
                    )
                    _miniCard(
                        "fa-solid fa-table text-emerald-500", "border-emerald-500",
                        "Πίνακες για Πολυμερή Αποτελέσματα",
                        "VLSM, κατάτμηση και πίνακες δρομολόγησης παρουσιάζονται ΠΑΝΤΑ σε πίνακα με στήλες "
                        "(Δίκτυο, Μάσκα, First/Last, Broadcast) — έτσι ελέγχεται κάθε γραμμή ξεχωριστά.",
                    )
                    _miniCard(
                        "fa-solid fa-shield-halved text-purple-500", "border-purple-500",
                        "Επαλήθευση Πριν την Παράδοση",
                        "Usable + 2 = συνολικές διευθύνσεις· τα offsets των τμημάτων πολλαπλάσια του 8· "
                        "άθροισμα κόστους διαδρομής Dijkstra· σύγκλιση πίνακα DV.",
                    )
                    _miniCard(
                        "fa-solid fa-language text-rose-500", "border-rose-500",
                        "Ορολογία στην Ορολογία της Ύλης",
                        "Χρησιμοποιούμε τους όρους της ύλης: PDU, encapsulation, ssthresh, cwnd, convergence, "
                        "count-to-infinity, longest prefix match.",
                    )

        # SECTION 2: Methodology table
        renderMethodologyTable()

        # SECTION 3: Fundamental definitions and TCP/IP functions
        with ui.column().classes("w-full glass-panel p-6 md:p-8 rounded-2xl gap-5"):
            _panelHeader(
                "fa-circle-info", "3. Θεμελιώδεις Ορισμοί & Λειτουργίες TCP/IP",
                "Δίκτυο, πρωτόκολλο, βασικές λειτουργίες της στοίβας και οργανισμοί τυποποίησης.",
                "text-blue-500",
            )
            ui.html(
                r"""
                <div class="overflow-x-auto w-full">
                    <table class="dark-table">
                        <thead><tr><th style="width: 30%;">Έννοια</th><th>Ορισμός & Σημειώσεις</th></tr></thead>
                        <tbody>
                            <tr><td class="font-bold text-blue-600 dark:text-blue-300">Δίκτυο Υπολογιστών</td>
                            <td>Σύνολο υπολογιστών ή συσκευών που επικοινωνούν μέσω ενός ή περισσότερων κοινών μέσων μετάδοσης.</td></tr>
                            <tr><td class="font-bold text-blue-600 dark:text-blue-300">Πρωτόκολλο Δικτύου</td>
                            <td>Σύστημα κοινών κανόνων που διέπει τη μετάδοση δεδομένων μεταξύ δικτυακών πόρων.</td></tr>
                            <tr><td class="font-bold text-blue-600 dark:text-blue-300">TCP/IP</td>
                            <td>Πλήρες σύστημα πρωτοκόλλων που ορίζει επεξεργασία, μετάδοση και λήψη δεδομένων σε δίκτυο που το εφαρμόζει.</td></tr>
                            <tr><td class="font-bold text-blue-600 dark:text-blue-300">Λειτουργίες Στοίβας</td>
                            <td>Λογική διευθυνσιοδότηση (32-bit IP), δρομολόγηση (routers), επίλυση ονομάτων (DNS/WINS), έλεγχος λαθών & ροής, υποστήριξη εφαρμογών (ports).</td></tr>
                            <tr><td class="font-bold text-blue-600 dark:text-blue-300">Ανάλυση IP Διεύθυνσης</td>
                            <td>Η διεύθυνση χωρίζεται σε <strong>net_ID</strong> + <strong>subnet_ID</strong> + <strong>host_ID</strong> με τη βοήθεια της μάσκας.</td></tr>
                            <tr><td class="font-bold text-blue-600 dark:text-blue-300">Οργανισμοί</td>
                            <td>IAB (πολιτική), IETF (επιτροπές τυποποίησης), IRTF (έρευνα), ICANN (εκχωρήσεις), InterNIC (λίστα παρόχων). Τα <strong>RFC</strong> είναι τα επίσημα τεχνικά έγγραφα τυποποίησης.</td></tr>
                        </tbody>
                    </table>
                </div>
                """
            )

        # SECTION 4: OSI vs TCP/IP, encapsulation, MAC vs IP
        with ui.column().classes("w-full glass-panel p-6 md:p-8 rounded-2xl gap-5"):
            _panelHeader(
                "fa-layer-group", "4. Μοντέλα Αναφοράς: OSI &harr; TCP/IP, Ενθυλάκωση & PDUs",
                "Η αντιστοίχιση των επιπέδων, τα PDUs ανά επίπεδο, και MAC vs IP διεύθυνση.",
                "text-blue-500",
            )
            ui.html(
                r"""
                <div class="overflow-x-auto w-full">
                    <table class="dark-table">
                        <thead>
                            <tr><th>OSI (7 Επίπεδα)</th><th>TCP/IP (4 Επίπεδα)</th><th>PDU</th><th>Πρωτόκολλα</th><th>Βασικός Ρόλος</th></tr>
                        </thead>
                        <tbody>
                            <tr><td>7. Εφαρμογής + 6. Παρουσίασης + 5. Συνόδου</td><td><strong>Εφαρμογής</strong></td><td>Data / Message</td><td>HTTP/S, FTP, SMTP, DNS, TELNET, SNMP, SSH</td><td>Υπηρεσίες δικτύου σε εφαρμογές, μορφοποίηση, κρυπτογράφηση, διαχείριση συνόδων</td></tr>
                            <tr><td>4. Μεταφοράς</td><td><strong>Μεταφοράς</strong></td><td>Segment (TCP) / Datagram (UDP)</td><td>TCP, UDP</td><td>Έλεγχος λαθών & ροής, ports, αξιόπιστη μεταφορά</td></tr>
                            <tr><td>3. Δικτύου</td><td><strong>Internet</strong></td><td>Packet / Datagram</td><td>IP, ICMP, ARP, IGMP, OSPF</td><td>Λογική διευθυνσιοδότηση & δρομολόγηση</td></tr>
                            <tr><td>2. Σύνδεσης Δεδομένων + 1. Φυσικό</td><td><strong>Πρόσβασης Δικτύου</strong></td><td>Frame &rarr; Bits</td><td>Ethernet, WiFi (802.11), PPP, ARP</td><td>Διαμόρφωση πλαισίων, μέθοδος πρόσβασης MAC, μετατροπή σε σήματα</td></tr>
                        </tbody>
                    </table>
                </div>
                """
            )
            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full"):
                _miniCard(
                    "fa-solid fa-box-archive text-amber-500", "border-amber-500",
                    "Ενθυλάκωση / Απο-ενθυλάκωση",
                    "Αποστολή: Data &rarr; Segment/Datagram (Header L4) &rarr; Packet (Header IP) &rarr; "
                    "Frame (Header+Trailer L2) &rarr; Bits. Λήψη: αντίστροφη απο-ενθυλάκωση σε κάθε επίπεδο "
                    "μέχρι τα δεδομένα της εφαρμογής.",
                )
                _miniCard(
                    "fa-solid fa-fingerprint text-emerald-500", "border-emerald-500",
                    "MAC vs IP Διεύθυνση",
                    "MAC: 48-bit <strong>φυσική/σταθερή</strong> (καμένα στη NIC), επίπεδο 2, τοπική παράδοση "
                    "στον ίδιο σύνδεσμο. IP: 32-bit <strong>λογική/ιεραρχική</strong> (στατική/DHCP), επίπεδο 3, "
                    "δρομολόγηση μεταξύ δικτύων. Το ARP γεφυρώνει τα δύο (IP &rarr; MAC).",
                )
                _miniCard(
                    "fa-solid fa-code-branch text-purple-500", "border-purple-500",
                    "Υποεπίπεδα Επιπέδου Πρόσβασης",
                    "LLC (Logical Link Control): έλεγχος λαθών εισερχόμενων/εξερχόμενων πλαισίων. "
                    "MAC (Media Access Control): μέθοδος πρόσβασης & διαμόρφωση πλαισίου. "
                    "PHY: καλώδια, κανόνες καλωδίωσης, μετατροπή σε σήματα.",
                )
                _miniCard(
                    "fa-solid fa-wave-square text-rose-500", "border-rose-500",
                    "Τοπολογίες LAN & Ασύρματα",
                    "Bus, Star (hub/switch), Ring (Token Ring, FDDI με 2 οπτικές ίνες), Mesh. "
                    "IEEE 802.11: PHY μορφές FHSS, DSSS, OFDM (802.11a), HR/DSSS (802.11b).",
                )
            ui.html(
                r"""
                <div class="overflow-x-auto w-full">
                    <table class="dark-table">
                        <thead><tr><th>Τεχνολογία Ethernet</th><th>Μέσο</th><th>Ταχύτητα</th><th>Μέγιστη Απόσταση</th></tr></thead>
                        <tbody>
                            <tr><td>10BASE-2 / 10BASE-5</td><td>Λεπτό / Παχύ ομοαξονικό</td><td>10 Mbps</td><td>185 m / 500 m</td></tr>
                            <tr><td>10BASE-T / 10BASE-F</td><td>CAT3-5 UTP / Οπτικές Ίνες</td><td>10 Mbps</td><td>100 m / 2000 m</td></tr>
                            <tr><td>100BASE-TX / 100BASE-FX</td><td>CAT5 UTP / Οπτικές Ίνες</td><td>100 Mbps</td><td>100 m / 2000 m</td></tr>
                            <tr><td>1000BASE-T / 1000BASE-SX,LX</td><td>CAT5 UTP / Οπτικές Ίνες</td><td>1 Gbps</td><td>200 m / 500-3000 m</td></tr>
                            <tr><td>10Gigabit</td><td>Multimode fiber</td><td>10 Gbps</td><td>300-600 m</td></tr>
                        </tbody>
                    </table>
                </div>
                """
            )
            with ui.column().classes("w-full p-5 rounded-xl bg-[var(--card-bg-subtle)] border border-[var(--border)] gap-2"):
                ui.label("Μαθηματικά Φυσικού Επιπέδου (SNR & Μέγιστος Ρυθμός)").classes("font-bold text-sm text-[var(--text-1)]")
                ui.html(
                    r"""
                    <div class="katex-target">
                        <p class="text-xs text-[var(--text-2)] m-0">Σχέση σήματος/θορύβου σε dB:</p>
                        \[ SNR_{dB} = 10 \log_{10}\left(\frac{S}{N}\right) \]
                        <p class="text-xs text-[var(--text-2)] m-0">Μέγιστος ρυθμός σε θορυβωδέστερο κανάλι (Shannon):</p>
                        \[ C_{max} = B \log_2\left(1 + \frac{S}{N}\right) \]
                        <p class="text-xs text-[var(--text-2)] m-0">Παράδειγμα ADSL: \(B = 1\,MHz\), \(SNR = 40\,dB \Rightarrow S/N = 10^4\), οπότε \(C_{max} \approx 10.7\,Mbps\).</p>
                    </div>
                    """
                )

        # SECTION 5: IPv4 addressing
        with ui.column().classes("w-full glass-panel p-6 md:p-8 rounded-2xl gap-5"):
            _panelHeader(
                "fa-location-dot", "5. Διευθυνσιοδότηση IPv4: Κλάσεις, Ιδιωτικά Εύρη, Ειδικές Διευθύνσεις",
                "Δομή net_ID/host_ID, πλήρης πίνακας κλάσεων, RFC 1918, και μετατροπές δυαδικού.",
                "text-amber-500",
            )
            ui.html(
                r"""
                <div class="overflow-x-auto w-full">
                    <table class="dark-table">
                        <thead>
                            <tr><th>Κλάση</th><th>Αρχικά Bits</th><th>Πρώτο Οκτάδιο</th><th>Προεπιλεγμένη Μάσκα</th><th>Μορφή</th><th>Hosts / Δίκτυο</th></tr>
                        </thead>
                        <tbody>
                            <tr><td><strong>A</strong></td><td>0</td><td>0-127</td><td>255.0.0.0 (/8)</td><td>N.H.H.H</td><td>\(2^{24} - 2 = 16.777.214\)</td></tr>
                            <tr><td><strong>B</strong></td><td>10</td><td>128-191</td><td>255.255.0.0 (/16)</td><td>N.N.H.H</td><td>\(2^{16} - 2 = 65.534\)</td></tr>
                            <tr><td><strong>C</strong></td><td>110</td><td>192-223</td><td>255.255.255.0 (/24)</td><td>N.N.N.H</td><td>\(2^{8} - 2 = 254\)</td></tr>
                            <tr><td><strong>D</strong></td><td>1110</td><td>224-239</td><td>-</td><td>Multicast</td><td>-</td></tr>
                            <tr><td><strong>E</strong></td><td>1111</td><td>240-255</td><td>-</td><td>Δεσμευμένη</td><td>-</td></tr>
                        </tbody>
                    </table>
                </div>
                """
            )
            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full"):
                _miniCard(
                    "fa-solid fa-lock text-blue-500", "border-blue-500",
                    "Ιδιωτικά Εύρη (RFC 1918)",
                    "10.0.0.0/8 (10.0.0.0-10.255.255.255), 172.16.0.0/12 (172.16.0.0-172.31.255.255), "
                    "192.168.0.0/16 (192.168.0.0-192.168.255.255). Δεν δρομολογούνται στο δημόσιο Internet "
                    "(χρειάζονται NAT).",
                )
                _miniCard(
                    "fa-solid fa-triangle-exclamation text-amber-500", "border-amber-500",
                    "Ειδικές Διευθύνσεις",
                    "127.0.0.1 (loopback/localhost), 0.0.0.0 (&laquo;οποιαδήποτε/άγνωστη&raquo;, DHCP discovery), "
                    "255.255.255.255 (τοπική broadcast), NetID.hosts-όλα-1 (broadcast δικτύου), "
                    "169.254.x.x (APIPA όταν αποτύχει το DHCP).",
                )
                _miniCard(
                    "fa-solid fa-binary text-emerald-500", "border-emerald-500",
                    "Μετατροπή Δυαδικό &harr; Δεκαδικό",
                    "Δύναμεις θέσης: 128 64 32 16 8 4 2 1. Π.χ. 10110111 = 183. Αντίστροφα: διαδοχικές "
                    "διαιρέσεις με το 2 και ανάγνωση υπολοίπων από κάω προς τα πάνω. Π.χ. 207 = 11001111.",
                )
                _miniCard(
                    "fa-solid fa-shuffle text-purple-500", "border-purple-500",
                    "CIDR & Μάσκες",
                    "Το a.b.c.d/x δηλώνει x bits δικτύου. Ισοδυναμίες προς αποστήθιση: /8=255.0.0.0, "
                    "/16=255.255.0.0, /20=255.255.240.0, /22=255.255.252.0, /24=255.255.255.0, "
                    "/26=255.255.255.192, /27=255.255.255.224, /28=255.255.255.240, /30=255.255.255.252.",
                )

        # SECTION 6: Subnetting and VLSM methodology
        with ui.column().classes("w-full glass-panel p-6 md:p-8 rounded-2xl gap-5"):
            _panelHeader(
                "fa-sitemap", "6. Υποδικτύωση, VLSM & Σύνοψη Διαδρομών (CIDR)",
                "Η βήμα-βήμα μεθοδολογία που λύνει κάθε άσκηση υποδικτύωσης σε 4 κινήσεις.",
                "text-amber-500",
            )
            with ui.column().classes("w-full gap-2"):
                for idx, (t, b) in enumerate([
                    ("Βήμα 1 — Ταξινόμηση Αναγκών",
                     "Ταξινομούμε τις ανάγκες σεhosts κατά ΦΘΙΝΟΥΣΑ σειρά. Στο VLSM το μεγαλύτερο δίκτυο "
                     "παίρνει τη μικρότερη μάσκα (περισσότερα host bits) πρώτο, ώστε να μη δημιουργηθούν "
                     "επικαλύψεις και κενά."),
                    ("Βήμα 2 — Εύρεση Host Bits",
                     r"Για κάθε ανάγκη \(H\) υπολογίζουμε το ελάχιστο \(h\) με \(2^h - 2 \ge H\). "
                     r"Ο νέος πρόλογος είναι \(32 - h\). Το \(-2\) αφαιρεί τη διεύθυνση δικτύου (όλα 0) "
                     "και το broadcast (όλα 1) του Host-ID."),
                    ("Βήμα 3 — Μάσκα & Βήμα Block",
                     r"Η μάσκα προκύπτει από \(h\) μηδενικά bits. Το βήμα (block size) του ενδιαφέροντος "
                     r"οκταδίου είναι \(256 - \text{τιμή μάσκας}\): /26 &rarr; 192 &rarr; βήμα 64, "
                     r"/27 &rarr; 224 &rarr; βήμα 32, /30 &rarr; 252 &rarr; βήμα 4."),
                    ("Βήμα 4 — Κατανομή Διευθύνσεων",
                     "Κάθε υποδίκτυο ξεκινά στο broadcast του προηγούμενου + 1. First usable = δίκτυο + 1, "
                     "Last usable = broadcast - 1. Παρουσιάζουμε πάντα πίνακα με όλες τις στήλες."),
                ], start=1):
                    with ui.row().classes(f"p-4 rounded-xl bg-[var(--card-bg-subtle)] border-l-4 border-amber-500 border border-[var(--border)] gap-3 items-start"):
                        ui.html(f'<span class="tag-label bg-[var(--badge-bg)] text-[var(--amber)] border border-[var(--border)]" style="font-size:0.7rem;">{idx}</span>')
                        with ui.column().classes("gap-1"):
                            ui.label(t).classes("font-bold text-sm text-[var(--text-1)]")
                            ui.html(f'<p class="text-xs text-[var(--text-2)] leading-relaxed m-0">{b}</p>')

            ui.html(
                r"""
                <div class="overflow-x-auto w-full">
                    <table class="dark-table">
                        <thead><tr><th>Πρόθεμα</th><th>Μάσκα</th><th>Host Bits</th><th>Χρησιμοποιήσιμοι Hosts</th><th>Τυπική Χρήση</th></tr></thead>
                        <tbody>
                            <tr><td>/25</td><td>255.255.255.128</td><td>7</td><td>\(2^7-2 = 126\)</td><td>Μικρά τμήματα</td></tr>
                            <tr><td>/26</td><td>255.255.255.192</td><td>6</td><td>\(2^6-2 = 62\)</td><td>~60 σταθμοί</td></tr>
                            <tr><td>/27</td><td>255.255.255.224</td><td>5</td><td>\(2^5-2 = 30\)</td><td>~28 σταθμοί</td></tr>
                            <tr><td>/28</td><td>255.255.255.240</td><td>4</td><td>\(2^4-2 = 14\)</td><td>~12 σταθμοί</td></tr>
                            <tr><td>/30</td><td>255.255.255.252</td><td>2</td><td>\(2^2-2 = 2\)</td><td>Ζεύξεις σημείου-προς-σημείο</td></tr>
                        </tbody>
                    </table>
                </div>
                """
            )
            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full"):
                _miniCard(
                    "fa-solid fa-object-group text-blue-500", "border-blue-500",
                    "Σύνοψη Διαδρομών (Supernetting)",
                    "Γράφουμε τα δίκτυα σε δυαδικό, βρίσκουμε τα <strong>κοινά αρχικά bits</strong> και "
                    "ορίζουμε νέο πρόθεμα. Π.χ. 192.168.16-19.0/24: τρίτο οκτάδιο 000100xx &rarr; 4 κοινά bits "
                    "&rarr; σύνοψη 192.168.16.0/22 (μάσκα 255.255.252.0).",
                )
                _miniCard(
                    "fa-solid fa-globe text-emerald-500", "border-emerald-500",
                    "IPv6 σε Συντομία",
                    "128-bit, 8 εξαδικές ομάδες. Συμπίεση: αφαίρεση αρχικών μηδενικών ανά ομάδα και "
                    "<strong>μία μόνο φορά</strong> αντικατάσταση της μεγαλύτερης ακολουθίας μηδενικών με :: "
                    "(π.χ. 2001:0DB8:0:0:0:0:0:1 &rarr; 2001:DB8::1, loopback = ::1). Υποδικτύωση με πρόλογα "
                    "(π.χ. /48 &rarr; /51 δίνει \(2^3 = 8\) υποδίκτυα).",
                )

        # SECTION 7: Internet layer protocols
        with ui.column().classes("w-full glass-panel p-6 md:p-8 rounded-2xl gap-5"):
            _panelHeader(
                "fa-scissors", "7. Επίπεδο Internet: IP Datagram, Κατάτμηση, ARP, ICMP, TTL, NAT, IGMP",
                "Πεδία επικεφαλίδας IPv4, μηχανική κατάτμησης, ανάλυση διευθύνσεων και μετάφραση NAT.",
                "text-emerald-500",
            )
            ui.html(
                r"""
                <div class="overflow-x-auto w-full">
                    <table class="dark-table">
                        <thead><tr><th>Πεδίο Επικεφαλίδας IPv4</th><th>Ρόλος & Τιμές Εξετάσεων</th></tr></thead>
                        <tbody>
                            <tr><td class="font-bold">Version / IHL</td><td>4 (IPv4) / Ελάχιστο IHL = 5 &rarr; <strong>20 bytes</strong> ελάχιστη επικεφαλίδα (λέξεις των 32 bits).</td></tr>
                            <tr><td class="font-bold">Total Length</td><td>Συνολικό μήκος datagram σε bytes (επικεφαλίδα + δεδομένα).</td></tr>
                            <tr><td class="font-bold">Identification</td><td>Κοινή ταυτότητα όλων των τμημάτων του ίδιου αρχικού πακέτου.</td></tr>
                            <tr><td class="font-bold">Flags (DF / MF)</td><td>DF=1 &rarr; <strong>απαγόρευση κατάτμησης</strong> (παγίδα!). MF=1 &rarr; ακολουθούν κι άλλα τμήματα (0 μόνο στο τελευταίο).</td></tr>
                            <tr><td class="font-bold">Fragment Offset</td><td>Θέση των δεδομένων του τμήματος σε <strong>μονάδες των 8 bytes</strong>: \(\text{offset} = \text{θέση byte} / 8\).</td></tr>
                            <tr><td class="font-bold">Time to Live (TTL)</td><td>Μειώνεται κατά 1 ανά δρομολογητή· σε 0 το πακέτο απορρίπτεται με ICMP Time Exceeded (Τύπος 11). Βάση του traceroute.</td></tr>
                            <tr><td class="font-bold">Protocol</td><td>6 = TCP, 17 = UDP, 1 = ICMP, 2 = IGMP.</td></tr>
                            <tr><td class="font-bold">Header Checksum</td><td>Άθροισμα λέξεων 16-bit, πρόσθεση κρατουμένων (wrap-around), συμπλήρωμα ως προς 1. Επαληθεύεται σε κάθε hop.</td></tr>
                        </tbody>
                    </table>
                </div>
                """
            )
            with ui.column().classes("w-full p-5 rounded-xl bg-[var(--card-bg-subtle)] border border-[var(--border)] gap-2"):
                ui.label("Μηχανική Κατάτμησης (Fragmentation) — ο Πλήρης Αλγόριθμος").classes("font-bold text-sm text-[var(--text-1)]")
                ui.html(
                    r"""
                    <div class="katex-target">
                        <p class="text-xs text-[var(--text-2)] m-0">Παράδειγμα: Total Length 3000 B, Header 20 B, MTU 1500 B:</p>
                        \[ \text{Δεδομένα} = 3000 - 20 = 2980\,B, \qquad \text{ανά τμήμα} = 1500 - 20 = 1480\,B \;\; (1480 / 8 = 185, \text{ακέραιο}) \]
                        \[ F_1: 1480 + 20 = 1500\,B,\; MF{=}1,\; \text{offset } 0 \;\big|\; F_2: 1500\,B,\; MF{=}1,\; \text{offset } 185 \;\big|\; F_3: 40\,B,\; MF{=}0,\; \text{offset } 370 \]
                        <p class="text-xs text-[var(--text-2)] m-0">Επανασύνθεση: τελευταίο τμήμα (MF=0) &rarr; \(\text{δεδομένα} = \text{offset} \times 8 + (\text{length} - 20)\).</p>
                    </div>
                    """
                )
            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full"):
                _miniCard(
                    "fa-solid fa-magnifying-glass-location text-blue-500", "border-blue-500",
                    "ARP (Address Resolution Protocol)",
                    "Δοθείσης IP εντός τοπικού δικτύου, ο αποστολέας στέλνει <strong>ARP Request σε "
                    "broadcast</strong> (&laquo;Ποιος έχει την IP X;&raquo;) και ο κάτοχος απαντά "
                    "<strong>ARP Reply σε unicast</strong> με τη MAC του. Η αντιστοίχιση αποθηκεύεται σε ARP cache.",
                )
                _miniCard(
                    "fa-solid fa-tower-broadcast text-purple-500", "border-purple-500",
                    "ICMP — Τύποι Μηνυμάτων",
                    "Echo Request/Reply (ping), Source Quench (÷ρηνός δρομολογητής δεν παρακολουθεί τον όγκο), "
                    "Destination Unreachable, Time Exceeded (TTL=0), Fragmentation Needed. Δομή: Type + Code + Checksum + Data.",
                )
                _miniCard(
                    "fa-solid fa-right-left text-amber-500", "border-amber-500",
                    "NAT (Network Address Translation)",
                    "Μεταφράζει Inside Local (ιδιωτική IP:θύρα) &rarr; Inside Global (δημόσια IP:θύρα) με μοναδικές "
                    "θυρες ανά σύνδεση. Ο πίνακας μετάφρασης δρομολογεί την επιστρεφόμενη κίνηση: "
                    "203.0.113.5:1024 &rarr; 192.168.1.10:5000.",
                )
                _miniCard(
                    "fa-solid fa-people-group text-emerald-500", "border-emerald-500",
                    "IGMP & Multicasting",
                    "Διαχείριση συμμετοχής σε ομάδες multicast (Class D). Μηνύματα: Query (224.0.0.1), Membership "
                    "Report (διεύθυνση ομάδας), Leave Report (224.0.0.2). Αντιστοίχιση MAC: τελευταία 23 bits της "
                    "διεύθυνσης ομάδας + πρόθεμα 01:00:5E.",
                )

        # SECTION 8: Transport layer
        with ui.column().classes("w-full glass-panel p-6 md:p-8 rounded-2xl gap-5"):
            _panelHeader(
                "fa-gauge-high", "8. Επίπεδο Μεταφοράς: TCP vs UDP, Ports, Παράθυρα & Συμφόρηση",
                "Ό,τι χρειάζεται για θέματα μεταφοράς: χειραψία, seq/ACK, sliding window, AIMD, BDP.",
                "text-purple-500",
            )
            ui.html(
                r"""
                <div class="overflow-x-auto w-full">
                    <table class="dark-table">
                        <thead><tr><th>Χαρακτηριστικό</th><th>TCP</th><th>UDP</th></tr></thead>
                        <tbody>
                            <tr><td class="font-bold">Τύπος σύνδεσης</td><td>Με σύνδεση (connection-oriented)</td><td>Χωρίς σύνδεση (connectionless)</td></tr>
                            <tr><td class="font-bold">Αξιοπιστία</td><td>Επιβεβαιώσεις, επαναμεταδόσεις, ταξινόμηση</td><td>Μη αξιόπιστο (best effort)</td></tr>
                            <tr><td class="font-bold">Ταχύτητα / Επικεφαλίδα</td><td>Βραδύτερο / 20 bytes ελάχιστο</td><td>Ταχύτερο / 8 bytes</td></tr>
                            <tr><td class="font-bold">Multicast</td><td>Όχι</td><td>Ναι</td></tr>
                            <tr><td class="font-bold">Εφαρμογές</td><td>HTTP/S, FTP, SMTP, POP3, IMAP, SSH, Telnet</td><td>DNS (queries), VoIP, video streaming, online gaming, DHCP, TFTP, IGMP</td></tr>
                        </tbody>
                    </table>
                </div>
                """
            )
            ui.html(
                r"""
                <div class="overflow-x-auto w-full">
                    <table class="dark-table">
                        <thead><tr><th>Θύρα</th><th>Υπηρεσία</th><th>Θύρα</th><th>Υπηρεσία</th></tr></thead>
                        <tbody>
                            <tr><td><code>20/21</code></td><td>FTP (δεδομένα/έλεγχος)</td><td><code>53</code></td><td>DNS</td></tr>
                            <tr><td><code>22</code></td><td>SSH</td><td><code>80</code></td><td>HTTP</td></tr>
                            <tr><td><code>23</code></td><td>Telnet</td><td><code>110</code></td><td>POP3</td></tr>
                            <tr><td><code>25</code></td><td>SMTP</td><td><code>143 / 443</code></td><td>IMAP / HTTPS</td></tr>
                        </tbody>
                    </table>
                </div>
                """
            )
            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full"):
                _miniCard(
                    "fa-solid fa-handshake text-blue-500", "border-blue-500",
                    "Χειραψία Τριών Βημάτων",
                    "1) Client &rarr; SYN (δικό του ISN). 2) Server &rarr; SYN+ACK (ACK = ISN_client + 1, δικό του ISN). "
                    "3) Client &rarr; ACK (ACK = ISN_server + 1). Τα SYN και FIN <strong>καταναλώνουν 1 αριθμό "
                    "ακολουθίας</strong> το καθένα.",
                )
                _miniCard(
                    "fa-solid fa-hashtag text-emerald-500", "border-emerald-500",
                    "Αριθμοί Ακολουθίας & ACK",
                    "SEQ = πρώτο byte των δεδομένων του segment. ACK = <strong>επόμενο αναμενόμενο byte</strong> "
                    "(συσσωρευτικές επιβεβαιώσεις). Π.χ. αποστολή 500 bytes από SEQ 3001 &rarr; απάντηση ACK 3501.",
                )
                _miniCard(
                    "fa-solid fa-window-restore text-amber-500", "border-amber-500",
                    "Συρόμενο Παράθυρο & Έλεγχος Ροής",
                    "Ο παραλήπτης ανακοινώνει το rwnd (διαθέσιμο buffer) στο πεδίο Window· ο αποστολέας "
                    "κρατά unACKed bytes &le; rwnd. Σε buffer πληρότητας ανακοινώνεται παράθυρο 0 (zero window) "
                    "και ο αποστολέας σταματά (periodic zero-window probe). 3 διπλότυπα ACK &rarr; Fast Retransmit.",
                )
                _miniCard(
                    "fa-solid fa-chart-line text-purple-500", "border-purple-500",
                    "Έλεγχος Συμφόρησης: Slow Start &harr; Avoidance",
                    r"cwnd ξεκινά από 1 MSS: κάτω από το ssthresh διπλασιάζεται ανά RTT (εκθετικά), πάνω ή ίσο "
                    r"αυξάνεται κατά +1 MSS ανά RTT (γραμμικά, AIMD). Απώλεια με 3 dup ACK: Tahoe &rarr; "
                    r"\(ssthresh = \lfloor cwnd/2 \rfloor,\; cwnd = 1\). Reno (Fast Recovery) &rarr; "
                    r"\(cwnd = ssthresh + 3\).",
                )
            ui.html(
                r"""
                <div class="katex-target p-5 rounded-xl bg-[var(--card-bg-subtle)] border border-[var(--border)]">
                    <p class="text-xs font-bold text-[var(--text-1)] m-0 mb-1">Ρυθμοαπόδοση & Γινόμενο Εύρους-Καθυστέρησης</p>
                    <p class="text-xs text-[var(--text-2)] m-0">Με παράθυρο W και RTT δεδομένο:</p>
                    \[ \text{Throughput}_{max} = \frac{W}{\text{RTT}}, \qquad W_{\text{απαιτούμενο}} = R \times \text{RTT} = \text{BDP} \]
                    <p class="text-xs text-[var(--text-2)] m-0">Παράδειγμα: W = 64 KB, RTT = 100 ms &rarr; 5.24 Mbps. Για R = 100 Mbps με ίδιο RTT χρειάζεται W = 1.25 MB (BDP) — μεγαλύτερο από το μέγιστο 16-bit πεδίο παραθύρου (64 KB), άρα απαιτείται window scaling.</p>
                </div>
                """
            )

        # SECTION 9: Routing
        with ui.column().classes("w-full glass-panel p-6 md:p-8 rounded-2xl gap-5"):
            _panelHeader(
                "fa-route", "9. Δρομολόγηση: Πίνακες, Link-State vs Distance-Vector, Dijkstra",
                "Forwarding με longest prefix match, πλήρης εκτέλεση Dijkstra, και count-to-infinity.",
                "text-rose-500",
            )
            _miniCard(
                "fa-solid fa-table-columns text-blue-500", "border-blue-500",
                "Πίνακες Δρομολόγησης & Longest Prefix Match",
                "Κάθε γραμμή: Destination / Netmask / Gateway / Interface / Metric. Για κάθε προορισμό "
                "επιλέγεται η <strong>πιο εξειδικευμένη</strong> αντιστοίχιση (μακρύτερο πρόθεμα). Η γραμμή "
                "0.0.0.0/0 είναι η προεπιλεγμένη διαδρομή (default gateway) και εφαρμόζεται μόνο αν καμία "
                "άλληρη δεν ταιριάζει. Gateway 0.0.0.0 = άμεσα συνδεδεμένο δίκτυο.",
            )
            with ui.column().classes("w-full p-5 rounded-xl bg-[var(--card-bg-subtle)] border border-[var(--border)] gap-2"):
                ui.label("Εκτέλεση Dijkstra (Link-State / OSPF) — ο Πίνακας Βημάτων").classes("font-bold text-sm text-[var(--text-1)]")
                ui.html(
                    r"""
                    <div class="katex-target">
                        <p class="text-xs text-[var(--text-2)] m-0">Σε κάθε βήμα προστίθεται ο κόμβος με το ελάχιστο D() και χαλαρώνουν οι ακμές του:</p>
                        \[ D(v) = \min\left(D(v),\; D(u) + c(u,v)\right) \]
                        <p class="text-xs text-[var(--text-2)] m-0">
                        Παράδειγμα (u-v:2, u-w:5, u-x:1, x-v:2, x-w:3, x-y:1, v-w:3, y-w:1): Β0: N'={u}, D(x)=1 ελάχιστο &rarr;
                        Β1: D(v)=2, D(w)=4, D(y)=2 &rarr; Β2 (y): D(w)=3 &rarr; Β3 (v): D(w)=3 &rarr; Β4 (w).
                        Πίνακας u: v=2 απευθείας, x=1 απευθείας, y=2 μέσω x, w=3 μέσω x.
                        </p>
                    </div>
                    """
                )
            ui.html(
                r"""
                <div class="overflow-x-auto w-full">
                    <table class="dark-table">
                        <thead><tr><th>Κριτήριο</th><th>Link-State (OSPF)</th><th>Distance-Vector (RIP)</th></tr></thead>
                        <tbody>
                            <tr><td class="font-bold">Ανταλλαγή πληροφορίας</td><td>Πλημυρικό (flooding) LSA σε <strong>όλα</strong> τα δρομολογητές· καθένας υπολογίζει Dijkstra τοπικά με πλήρη τοπολογία</td><td>Ανταλλαγή διανυσμάτων απόστασης μόνο με τους <strong>γειτόνες</strong> (περιοδικά, 30 s στο RIP)</td></tr>
                            <tr><td class="font-bold">Ταχύτητα σύγκλισης</td><td>Γρήγορη (δευτερόλεπτα), event-triggered ενημερώσεις</td><td>Αργή (λεπτά) — η γνώση διαδίδεται hop-by-hop</td></tr>
                            <tr><td class="font-bold">Βρόχοι δρομολόγησης</td><td>Ουσιαστικά απαλλαγμένη (καθολική εικόνα + δένδρο SPF)</td><td>Ευάλωη: <strong>count-to-infinity</strong>· μετριασμός με split horizon, poison reverse, triggered updates· RIP max 15 hops (16 = &infin;)</td></tr>
                            <tr><td class="font-bold">Μετρική / Κλίμακα</td><td>Κόστος (εύρος ζώνης), ιεραρχικές περιοχές (areas), VLSM</td><td>Αριθμός αλμάτων· μικρά δίκτυα</td></tr>
                        </tbody>
                    </table>
                </div>
                """
            )
            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full"):
                _miniCard(
                    "fa-solid fa-infinity text-amber-500", "border-amber-500",
                    "Count-to-Infinity (Παράδειγμα)",
                    "Αν η ζεύξη A-B κοπεί, το B ακούει από το C (που περνά μέσω B) κόστος B-A = κόστος C-A + 1 "
                    "και το αυξάνει βήμα-βήμα προς το άπειρο (3, 4, 5, ...) μέχρι το μέγιστο 16 του RIP.",
                )
                _miniCard(
                    "fa-solid fa-earth-europe text-emerald-500", "border-emerald-500",
                    "BGP (Exterior Gateway Protocol)",
                    "Δρομολόγηση μεταξύ Αυτόνομων Συστημάτων (AS) βάσει πολιτικών· eBGP εξωτερικά / iBGP "
                    "εσωτερικά· αυξητικές ενημερώσεις· το πρωτόκολλο κορμού του διαδικτύου.",
                )

        # SECTION 10: Formula reference
        with ui.column().classes("w-full glass-panel p-6 md:p-8 rounded-2xl gap-5"):
            _panelHeader(
                "fa-square-root-variable", "10. Πίνακας Τύπων για Γρήγορη Αναφορά",
                "Όλοι οι τύποι των εξετάσεων συγκεντρωμένοι σε έναν πίνακα.",
                "text-blue-500",
            )
            ui.html(
                r"""
                <div class="overflow-x-auto w-full">
                    <table class="dark-table">
                        <thead><tr><th>Πεδίο</th><th>Τύπος</th><th>Σημειώσεις</th></tr></thead>
                        <tbody>
                            <tr><td>Χρησιμοποιήσιμοι hosts</td><td>\(2^h - 2 \ge H \Rightarrow h = \lceil \log_2(H+2) \rceil\)</td><td>-2: δίκτυο + broadcast</td></tr>
                            <tr><td>Διαθέσιμα υποδίκτυα</td><td>\(2^s\)</td><td>s = νέα bits υποδικτύου</td></tr>
                            <tr><td>Βήμα block</td><td>\(256 - \text{τελευταίο οκτάδιο μάσκας}\)</td><td>π.χ. 192 &rarr; 64</td></tr>
                            <tr><td>Network Address</td><td>\(\text{IP} \;\text{AND}\; \text{Μάσκα}\)</td><td>byte-προς-byte</td></tr>
                            <tr><td>Broadcast</td><td>Host bits &rarr; όλα 1</td><td>= last usable + 1</td></tr>
                            <tr><td>Ωφέλιμα δεδομένα τμήματος</td><td>\(\lfloor (\text{MTU} - 20)/8 \rfloor \times 8\)</td><td>πολλαπλάσιο του 8</td></tr>
                            <tr><td>Fragment offset</td><td>\(\text{θέση πρώτου byte} / 8\)</td><td>σε μονάδες 8 B</td></tr>
                            <tr><td>Throughput παραθύρου</td><td>\(T = W / \text{RTT}\)</td><td>W σε bits</td></tr>
                            <tr><td>Απαιτούμενο παράθυρο</td><td>\(W = R \times \text{RTT} = \text{BDP}\)</td><td>πλήρης αξιοποίηση R</td></tr>
                            <tr><td>SNR / Shannon</td><td>\(SNR_{dB} = 10\log_{10}(S/N)\), \(C = B\log_2(1+S/N)\)</td><td>φυσικό επίπεδο</td></tr>
                            <tr><td>Επιδοτικότητα πακέτου</td><td>\(\text{payload} / (\text{payload} + \text{headers}) \times 100\%\)</td><td>π.χ. 1000/1040 = 96.15%</td></tr>
                        </tbody>
                    </table>
                </div>
                """
            )

        # SECTION 11: Traps
        with ui.column().classes("w-full glass-panel p-6 md:p-8 rounded-2xl gap-4"):
            _panelHeader(
                "fa-triangle-exclamation", "11. Παγίδες & Λάθη που Στερούν Μονάδες",
                "Τα συχνότερα λάθη στις εξετάσεις δικτύων — και πώς αποφεύγονται.",
                "text-red-500",
            )
            traps = [
                "Το δίκτυο και το broadcast ΔΕΝ μετρώνται ως χρησιμοποιήσιμοι hosts: 2^h - 2, ποτέ 2^h.",
                "DF=1 σημαίνει ότι η κατάτμηση απαγορεύεται — αν το πακέτο υπερβαίνει το MTU, απορρίπτεται με ICMP Fragmentation Needed.",
                "Τα Fragment Offsets μετρώνται σε μονάδες των 8 bytes, όχι σε bytes· τα δεδομένα κάθε τμήματος (εκτός τελευταίου) πρέπει να είναι πολλαπλάσια του 8.",
                "Στο VLSM ταξινομούμε κατά φθίνουσα σειρά μεγέθους — αλλιώς δημιουργούνται επικαλύψεις.",
                "Τα SYN και FIN καταναλώνουν από 1 αριθμό ακολουθίας το καθένα (τα δεδομένα όχι — μετρώνται σε bytes).",
                "Οι επιβεβαιώσεις TCP είναι συσσωρευτικές: το ACK δηλώνει το επόμενο αναμενόμενο byte και διορθώνει αυτόματα τυχόν κενά.",
                "Σε πίνακες δρομολόγησης κερδίζει η πιο εξειδικευμένη αντιστοίχιση (longest prefix match), όχι η πρώτη ή αυτή με τη μικρότερη μετρική.",
                "Το ssthresh μετά από απώλεια με 3 διπλότυπα ACK είναι floor(cwnd/2) — και στο Tahoe το cwnd επανέρχεται σε 1 MSS, στο Reno σε ssthresh + 3.",
                "Το IPv6 :: επιτρέπεται μόνο μία φορά σε μια διεύθυνση — η μεγαλύτερη συνεχόμενη ακολουθία μηδενικών ομάδων.",
                "Η 169.254.x.x είναι APIPA (link-local) και ΔΕΝ ανήκει στα ιδιωτικά εύρη RFC 1918.",
                "Στη σύνοψη διαδρομών ελέγχουμε πάντα το εύρος: το 192.168.16.0/22 καλύπτει ακριβώς τα 16.0-19.255.",
                "Στο Dijkstra ισοβαθμίες λύνονται αυθαίρετα — το ζητούμενο είναι το ελάχιστο κόστος και το επόμενο άλμα, όχι η μοναδική διαδικασία.",
            ]
            with ui.column().classes("w-full gap-1.5"):
                for trap in traps:
                    ui.html(
                        f'<div class="tip-item"><i class="fa-solid fa-triangle-exclamation text-[var(--red-err)]"></i><span>{trap}</span></div>'
                    )
