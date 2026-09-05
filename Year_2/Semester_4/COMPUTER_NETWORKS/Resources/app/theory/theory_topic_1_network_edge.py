"""Topic 1: Network Edge (Δίκτυο στο Έπακρο) theory renderer.

Covers End Systems (Hosts), Network as a Service (NaaS), Tier 1/2/3 ISP hierarchy,
Client-Server vs Peer-to-Peer models, TCP vs UDP edge services, and Access Network provisioning.
"""

from nicegui import ui


def renderTopic1NetworkEdge() -> None:
    """Renders the comprehensive theory module for Topic 1: Network Edge."""
    with ui.column().classes("w-full gap-6 text-[#f4f1ea] latex-target"):
        # Header Banner
        with ui.column().classes(
            "w-full glass-panel p-6 md:p-8 rounded-2xl border border-[rgba(224,107,58,0.35)] gap-3"
        ):
            with ui.row().classes("items-center gap-3"):
                ui.html('<i class="fa-solid fa-laptop-code text-[#e06b3a] text-3xl"></i>')
                with ui.column().classes("gap-0"):
                    ui.html('<h2 class="text-xl md:text-2xl font-bold gradient-title m-0">Θέμα 1: Δίκτυο στο Έπακρο (Network Edge)</h2>')
                    ui.label(
                        "Τελικά Συστήματα (Hosts), Μοντέλα Επικοινωνίας (Client-Server & P2P), "
                        "Το Δίκτυο ως Υπηρεσία (NaaS), Ιεραρχία Παρόχων (ISPs) και Δίκτυα Πρόσβασης."
                    ).classes("text-xs md:text-sm text-[#b5b0a4]")

        # =========================================================================
        # SECTION 1: End Systems & Architecture
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-server text-blue-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">1. Τελικά Συστήματα (End Systems / Hosts) & Ρόλος στην Αρχιτεκτονική</h3>')

            ui.label(
                "Τα τελικά συστήματα (hosts) είναι οι συσκευές που βρίσκονται στα άκρα του δικτύου και εκτελούν τις εφαρμογές "
                "(υπολογιστές, smartphones, servers, αισθητήρες IoT, δικτυακές κάμερες). Αποκαλούνται 'τελικά' γιατί αποτελούν "
                "αποκλειστικά την αφετηρία ή τον τερματισμό της επικοινωνίας — σε αντίθεση με τους ενδιάμεσους κόμβους (routers, switches) "
                "που ανήκουν στον πυρήνα του δικτύου (network core) και απλώς προωθούν πακέτα."
            ).classes("text-xs md:text-sm text-[#b5b0a4] leading-relaxed")

            with ui.column().classes("w-full p-4 rounded-xl bg-[#141413] border border-[rgba(255,255,255,0.06)] font-mono text-xs text-[#fed7aa]"):
                ui.html(r"""<pre class="m-0 overflow-x-auto">
  Δίκτυο στο Έπακρο (Network Edge)
  ─────────────────────────────────────────────────────────────────────────────
  [Laptop]       [Smartphone]       [Smart TV]       [IoT Sensors / Camera]
      \               |                  |                   /
       \              |                  |                  /
        ──────────────[Δίκτυο Πρόσβασης (Access Network)]─────────────
                                       |
                            [Πυρήνας Δικτύου (Core)]
                            (Routers, Switches, IXPs)
                                       |
                            [Άλλα Τελικά Συστήματα / Servers]
</pre>""")

            # NaaS & ISP Hierarchy
            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs"):
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(79,142,201,0.25)] gap-2"):
                    ui.label("Το Δίκτυο ως Υπηρεσία (Network as a Service - NaaS)").classes("font-bold text-blue-300 text-sm")
                    ui.label(
                        "• Αφηρημένος Αγωγός (Abstract Pipe): Το δίκτυο προσφέρει στις εφαρμογές έναν αγωγό μεταφοράς δεδομένων "
                        "χωρίς να απαιτείται γνώση των φυσικών δρομολογητών ή της υποκείμενης τοπολογίας.\n"
                        "• NaaS (Cloud Model): Μοντέλο όπου επιχειρήσεις 'νοικιάζουν' δικτυακές υποδομές, firewalling και bandwidth "
                        "από παρόχους αντί να συντηρούν ιδιόκτητο εξοπλισμό."
                    ).classes("text-[#b5b0a4] whitespace-pre-line")

                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(245,158,11,0.25)] gap-2"):
                    ui.label("Ιεραρχία Παρόχων ISP & Peering").classes("font-bold text-amber-300 text-sm")
                    ui.label(
                        "• Tier-1 ISPs: Παγκόσμιο backbone (AT&T, NTT, Lumen). Συνδέονται μεταξύ τους με settlement-free peering (χωρίς χρέωση).\n"
                        "• Tier-2 ISPs: Περιφερειακοί πάροχοι (Vodafone, Cosmote). Αγοράζουν transit από Tier-1.\n"
                        "• Tier-3 / Local ISPs: Τοπικοί πάροχοι πρόσβασης 'τελευταίου μιλίου' (last-mile) προς σπίτια και επιχειρήσεις."
                    ).classes("text-[#b5b0a4] whitespace-pre-line")

        # =========================================================================
        # SECTION 2: Communication Paradigms
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-arrows-split-up-and-left text-[#e06b3a] text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">2. Μοντέλα Επικοινωνίας: Client-Server vs Peer-to-Peer (P2P)</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs leading-relaxed"):
                # Client-Server Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(79,142,201,0.3)] gap-2"):
                    with ui.row().classes("items-center gap-2"):
                        ui.html('<i class="fa-solid fa-desktop text-blue-400"></i>')
                        ui.label("Μοντέλο Client-Server").classes("font-bold text-blue-300 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Server:</strong> Always-on μηχάνημα με μόνιμη (στατική) γνωστή IP διεύθυνση. Εξυπηρετεί πολλαπλούς πελάτες ταυτόχρονα.</li>
                        <li><strong class="text-stone-200">Client:</strong> Εκκινεί την επικοινωνία, έχει δυναμική IP, δεν επικοινωνεί απευθείας με άλλους clients.</li>
                        <li><strong class="text-stone-200">Κλιμάκωση:</strong> Περιορίζεται από το bandwidth και την επεξεργαστική ισχύ του server. Απαιτεί server farms, load balancers και CDNs.</li>
                        <li><strong class="text-stone-200">Παραδείγματα:</strong> Web (HTTP/HTTPS), Email (SMTP/IMAP), DNS, Βάσεις Δεδομένων.</li>
                    </ul>
                    """)

                # Peer-to-Peer Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(224,107,58,0.3)] gap-2"):
                    with ui.row().classes("items-center gap-2"):
                        ui.html('<i class="fa-solid fa-share-nodes text-[#e06b3a]"></i>')
                        ui.label("Μοντέλο Peer-to-Peer (P2P)").classes("font-bold text-[#e06b3a] text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Ισοτιμία (Peers):</strong> Κάθε κόμβος λειτουργεί ταυτόχρονα ως client και server (κατεβάζει και ανεβάζει ταυτόχρονα).</li>
                        <li><strong class="text-stone-200">Αυτο-κλιμακωσιμότητα (Self-scalability):</strong> Κάθε νέος χρήστης φέρνει νέα χωρητικότητα εξυπηρέτησης (uplink bandwidth) στο δίκτυο.</li>
                        <li><strong class="text-stone-200">Δυναμικό Churn:</strong> Οι κόμβοι συνδέονται και αποσυνδέονται απροειδοποίητα, αλλάζοντας συνεχώς διευθύνσεις IP.</li>
                        <li><strong class="text-stone-200">Παραδείγματα:</strong> BitTorrent, Blockchain (Bitcoin, Ethereum), InterPlanetary File System (IPFS).</li>
                    </ul>
                    """)

            # Hybrid Architecture Note
            with ui.column().classes("w-full p-4 rounded-xl bg-[#201f1d] border border-[rgba(245,158,11,0.25)] gap-1 text-xs"):
                ui.label("Υβριδικά Μοντέλα (Hybrid P2P / Client-Server)").classes("font-bold text-amber-300")
                ui.label(
                    "Πολλά σύγχρονα συστήματα συνδυάζουν και τα δύο: Χρησιμοποιούν κεντρικό server για αυθεντικοποίηση και "
                    "ανακάλυψη κόμβων (Node Discovery / Directory Service), και κατόπιν απευθείας P2P συνδέσεις για τη μεταφορά δεδομένων "
                    "(π.χ. παλαιότερο Skype, πρωτόκολλα WebRTC για peer-to-peer audio/video streaming)."
                ).classes("text-[#b5b0a4]")

        # =========================================================================
        # SECTION 3: Edge Services (TCP vs UDP)
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-bolt text-emerald-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">3. Υπηρεσίες Επίπεδου Μεταφοράς στο Έπακρο (TCP vs UDP)</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs"):
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(16,185,129,0.3)] gap-2"):
                    ui.label("TCP (Connection-Oriented, Reliable)").classes("font-bold text-emerald-400 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Εγκατάσταση Σύνδεσης:</strong> 3-Way Handshake (SYN, SYN-ACK, ACK).</li>
                        <li><strong class="text-stone-200">Αξιοπιστία:</strong> Εγγυημένη παράδοση χωρίς απώλειες και στη σωστή σειρά (Sequence numbers, ACKs, Retransmissions).</li>
                        <li><strong class="text-stone-200">Έλεγχος Ροής (Flow Control):</strong> Ο παραλήπτης δεν κατακλύζεται από δεδομένα (Receive Window `rwnd`).</li>
                        <li><strong class="text-stone-200">Έλεγχος Συμφόρησης (Congestion Control):</strong> Προσαρμογή ρυθμού βάσει κατάστασης του δικτύου (`cwnd`).</li>
                    </ul>
                    """)

                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(239,68,68,0.3)] gap-2"):
                    ui.label("UDP (Connectionless, Best-Effort)").classes("font-bold text-red-400 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Χωρίς Σύνδεση:</strong> Άμεση αποστολή δεδομένων χωρίς χειραψία (μηδενική καθυστέρηση έναρξης).</li>
                        <li><strong class="text-stone-200">Αναξιόπιστη Παράδοση:</strong> Δεν εγγυάται παράδοση, σειρά ή αποφυγή διπλοτύπων.</li>
                        <li><strong class="text-stone-200">Ελαφριά Επικεφαλίδα:</strong> Μόλις 8 bytes (έναντι τουλάχιστον 20 bytes του TCP).</li>
                        <li><strong class="text-stone-200">Ιδανικό για:</strong> DNS queries, live streaming, real-time gaming, VoIP (όπου η χαμηλή καθυστέρηση προέχει της απόλυτης αξιοπιστίας).</li>
                    </ul>
                    """)

        # =========================================================================
        # SECTION 4: Access Networks Breakdown
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-tower-broadcast text-amber-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">4. Δίκτυα Πρόσβασης "Τελευταίου Μιλίου" (Last-Mile Access)</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-3 gap-3 w-full text-xs"):
                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-1.5"):
                    ui.label("Οικιακή Πρόσβαση (DSL / HFC / FTTH)").classes("font-bold text-amber-300")
                    ui.label(
                        "• DSL: Χαλκός τηλεφωνίας, DSLAM στο αστικό κέντρο, ασύμμετρο (ADSL) ή VDSL. Περιορίζεται αυστηρά από την απόσταση (< 3-5 km).\n"
                        "• HFC (Cable): Οπτική ίνα μέχρι τον τοπικό κόμβο γειτονιάς και ομοαξονικό στο σπίτι (DOCSIS). Κοινόχρηστο μέσο.\n"
                        "• FTTH: Οπτική ίνα απευθείας στο σπίτι (PON αρχιτεκτονική με παθητικούς διαχωριστές)."
                    ).classes("text-[#b5b0a4] leading-relaxed")

                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-1.5"):
                    ui.label("Εταιρική Πρόσβαση (Enterprise)").classes("font-bold text-blue-300")
                    ui.label(
                        "• Ethernet (IEEE 802.3): Καλωδίωση συνεστραμμένου ζεύγους (UTP Cat6/6a) με ταχύτητες 1 Gbps, 10 Gbps, 100 Gbps.\n"
                        "• Wi-Fi (IEEE 802.11): Ασύρματη πρόσβαση μέσω Access Points (AP), πρωτόκολλο CSMA/CA."
                    ).classes("text-[#b5b0a4] leading-relaxed")

                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-1.5"):
                    ui.label("Κινητή & Δορυφορική Πρόσβαση").classes("font-bold text-emerald-300")
                    ui.label(
                        "• 4G LTE / 5G NR: Σύνδεση με σταθμούς βάσης κυψελών (gNodeB). Το 5G προσφέρει eMBB, URLLC και Network Slicing.\n"
                        "• LEO Satellites (Starlink): Χαμηλή τροχιά (500-1500 km), χαμηλή καθυστέρηση (~15-25 ms) για απομακρυσμένες περιοχές."
                    ).classes("text-[#b5b0a4] leading-relaxed")
