"""Topic 7: Basic Networking Issues (Βασικά Θέματα Δικτύωσης) theory renderer.

Covers Layer 2 MAC vs Layer 3 IP vs Layer 4 Port Addressing, Subnetting & CIDR,
ARP Protocol (Request broadcast, Reply unicast, ARP Cache, Default Gateway),
Error Detection & Correction (Parity bits, Internet Checksum, Hamming Codes, CRC Modulo-2),
and Network Diagnostics (Ping, Traceroute).
"""

from nicegui import ui


def renderTopic7BasicNetworkingIssues() -> None:
    """Renders the comprehensive theory module for Topic 7: Basic Networking Issues."""
    with ui.column().classes("w-full gap-6 text-[#f4f1ea] latex-target"):
        # Header Banner
        with ui.column().classes(
            "w-full glass-panel p-6 md:p-8 rounded-2xl border border-[rgba(224,107,58,0.35)] gap-3"
        ):
            with ui.row().classes("items-center gap-3"):
                ui.html('<i class="fa-solid fa-microchip text-[#e06b3a] text-3xl"></i>')
                with ui.column().classes("gap-0"):
                    ui.html('<h2 class="text-xl md:text-2xl font-bold gradient-title m-0">Θέμα 7: Βασικά Θέματα Δικτύωσης (Basic Networking Issues)</h2>')
                    ui.label(
                        "Διευθυνσιοδότηση (MAC, IP, Ports), Υποδικτύωση (Subnetting & CIDR), "
                        "Πρωτόκολλο ARP, Ανίχνευση/Διόρθωση Σφαλμάτων (Parity, Checksum, Hamming, CRC) και Traceroute."
                    ).classes("text-xs md:text-sm text-[#b5b0a4]")

        # =========================================================================
        # SECTION 1: Addressing Architecture (MAC, IP, Ports)
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-address-card text-blue-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">1. Πολυεπίπεδη Διευθυνσιοδότηση: MAC vs IP vs Ports</h3>')

            ui.html("""
            <div class="overflow-x-auto">
                <table class="w-full text-left text-xs border-collapse">
                    <thead>
                        <tr class="border-b border-[rgba(255,255,255,0.1)] text-[#e06b3a]">
                            <th class="py-2 px-3">Τύπος Διεύθυνσης</th>
                            <th class="py-2 px-3">Επίπεδο OSI</th>
                            <th class="py-2 px-3">Μέγεθος / Μορφή</th>
                            <th class="py-2 px-3">Εμβέλεια (Scope)</th>
                            <th class="py-2 px-3">Συμπεριφορά σε Δρομολογητές</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-[rgba(255,255,255,0.05)] text-[#b5b0a4]">
                        <tr>
                            <td class="py-2 px-3 font-bold text-stone-200">MAC (Physical Address)</td>
                            <td class="py-2 px-3 font-mono text-blue-400">Layer 2 (Data Link)</td>
                            <td class="py-2 px-3 font-mono">48 bits (6 hex bytes)</td>
                            <td class="py-2 px-3 text-amber-300">Τοπική (εντός LAN / Hop)</td>
                            <td class="py-2 px-3 text-red-300 font-bold">Αλλάζει σε κάθε router hop (επανεγγράφεται).</td>
                        </tr>
                        <tr>
                            <td class="py-2 px-3 font-bold text-stone-200">IP (Logical Address)</td>
                            <td class="py-2 px-3 font-mono text-emerald-400">Layer 3 (Network)</td>
                            <td class="py-2 px-3 font-mono">32 bits (IPv4) / 128 (IPv6)</td>
                            <td class="py-2 px-3 text-emerald-300">Παγκόσμια (End-to-End)</td>
                            <td class="py-2 px-3 text-emerald-300 font-bold">Παραμένει σταθερή από πηγή σε προορισμό.</td>
                        </tr>
                        <tr>
                            <td class="py-2 px-3 font-bold text-stone-200">Port (Θύρα Διαδικασίας)</td>
                            <td class="py-2 px-3 font-mono text-purple-400">Layer 4 (Transport)</td>
                            <td class="py-2 px-3 font-mono">16 bits (0 - 65.535)</td>
                            <td class="py-2 px-3 text-purple-300">Διαδικασία Host (Process)</td>
                            <td class="py-2 px-3">Προσδιορίζει την εφαρμογή (π.χ. HTTP 80, HTTPS 443, DNS 53).</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            """)

        # =========================================================================
        # SECTION 2: Subnetting & CIDR Calculations
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-network-wired text-emerald-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">2. Υποδικτύωση IPv4 & Νοτασία CIDR</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs"):
                with ui.column().classes("p-4 rounded-xl bg-[#141413] border border-[rgba(16,185,129,0.3)] gap-2"):
                    ui.label("Βασικοί Τύποι Υποδικτύωσης").classes("font-bold text-emerald-400 text-sm")
                    ui.html("""
                    <div class="formula-box text-xs mb-2">
                        $$\\text{Block Size} = 2^{32 - \\text{prefix}}, \\quad \\text{Hosts} = 2^{32 - \\text{prefix}} - 2$$
                    </div>
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Διεύθυνση Δικτύου:</strong> Πρώτη IP του block (host bits = all '0'). Δεν αποδίδεται σε host.</li>
                        <li><strong class="text-stone-200">Διεύθυνση Εκπομπής:</strong> Τελευταία IP του block (host bits = all '1'). Δεν αποδίδεται σε host.</li>
                        <li><strong class="text-stone-200">Ωφέλιμο Εύρος IPs:</strong> Από (Network + 1) έως (Broadcast - 1).</li>
                    </ul>
                    """)

                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(245,158,11,0.3)] gap-2"):
                    ui.label("Παράδειγμα: Υποδίκτυο /26").classes("font-bold text-amber-300 text-sm")
                    ui.html("""
                    <div class="space-y-1 font-mono text-xs text-[#b5b0a4]">
                        <div>• Μάσκα: <span class="text-stone-200">255.255.255.192 (/26)</span></div>
                        <div>• Host bits: <span class="text-stone-200">32 - 26 = 6 bits</span></div>
                        <div>• Block Size: <span class="text-stone-200">$2^6 = 64$ διευθύνσεις</span></div>
                        <div>• Ωφέλιμοι Hosts: <span class="text-emerald-300 font-bold">$64 - 2 = 62$ hosts</span></div>
                        <div>• Subnet 1: <span class="text-blue-300">192.168.1.0 - 192.168.1.63</span> (Net: .0, Bc: .63)</div>
                        <div>• Subnet 2: <span class="text-blue-300">192.168.1.64 - 192.168.1.127</span> (Net: .64, Bc: .127)</div>
                    </div>
                    """)

        # =========================================================================
        # SECTION 3: Address Resolution Protocol (ARP)
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-magnifying-glass text-cyan-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">3. Πρωτόκολλο ARP (Address Resolution Protocol)</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs"):
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(6,182,212,0.3)] gap-2"):
                    ui.label("Αντιστοίχιση IP -> MAC στο LAN").classes("font-bold text-cyan-300 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1.5 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">ARP Request:</strong> Εκπέμπεται ως <strong>Broadcast</strong> (MAC: <code>FF-FF-FF-FF-FF-FF</code>). Όλοι οι κόμβοι στο LAN το λαμβάνουν. Target MAC = <code>00-00-00-00-00-00</code>.</li>
                        <li><strong class="text-stone-200">ARP Reply:</strong> Ο κόμβος που κατέχει την IP απαντά ως <strong>Unicast</strong> απευθείας στον αιτούντα, περιέχοντας την πραγματική MAC του.</li>
                    </ul>
                    """)

                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(6,182,212,0.3)] gap-2"):
                    ui.label("ARP Cache & Default Gateway").classes("font-bold text-cyan-300 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1.5 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">ARP Cache:</strong> Προσωρινή μνήμη αντιστοιχίσεων (15-20 min). Αν σταλεί νέο πακέτο εντός του χρόνου, <em>δεν επαναλαμβάνεται το ARP request</em>.</li>
                        <li><strong class="text-stone-200">Επικοινωνία εκτός LAN:</strong> Αν η IP ανήκει σε άλλο subnet, ο host στέλνει ARP request για τη MAC της <strong>Default Gateway (Router)</strong>!</li>
                    </ul>
                    """)

        # =========================================================================
        # SECTION 4: Error Detection & Correction (Hamming & CRC)
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-shield-halved text-amber-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">4. Ανίχνευση & Διόρθωση Σφαλμάτων (Parity, Hamming, CRC)</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs"):
                # Hamming Code Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(245,158,11,0.3)] gap-2"):
                    ui.label("Κώδικας Hamming (Single Error Correction)").classes("font-bold text-amber-300 text-sm")
                    ui.html("""
                    <div class="formula-box text-xs mb-2">
                        $$2^p \\ge d + p + 1 \\quad (d=8 \\Rightarrow p=4, \\text{ θέσεις } 1, 2, 4, 8)$$
                    </div>
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Θέσεις Parity:</strong> Δυνάμεις του 2 ($P_1, P_2, P_4, P_8$). Τα δεδομένα ($D_i$) μπαίνουν στις υπόλοιπες θέσεις (3, 5, 6, 7, 9, 10, 11, 12).</li>
                        <li><strong class="text-stone-200">Κάλυψη Parity:</strong> Κάθε $P_i$ ελέγχει τις θέσεις των οποίων η δυαδική αναπαράσταση έχει άσο στη θέση $i$.</li>
                        <li><strong class="text-stone-200">Περιττή Ισοτιμία:</strong> Προσθέτουμε 0 ή 1 ώστε το σύνολο των άσων να είναι περιττός αριθμός.</li>
                    </ul>
                    """)

                # CRC Division Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(16,185,129,0.3)] gap-2"):
                    ui.label("Κυκλικός Έλεγχος Πλεονασμού (CRC)").classes("font-bold text-emerald-300 text-sm")
                    ui.html("""
                    <div class="formula-box text-xs mb-2">
                        $$\\text{Tx} = D \\cdot 2^r \\oplus R, \\quad R = (D \\cdot 2^r) \\bmod G$$
                    </div>
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li>Προσθέτουμε $r$ μηδενικά στο τέλος του $D$ ($r = \\text{βαθμός πολυωνύμου } G$).</li>
                        <li>Εκτελούμε διαίρεση Modulo-2 (XOR) με τον γεννήτορα $G$.</li>
                        <li>Το υπόλοιπο $R$ ($r$ bits) προστίθεται στο τέλος του $D$. Ο παραλήπτης διαιρεί με το $G$ και αν το υπόλοιπο είναι 0, δεν υπάρχει σφάλμα.</li>
                    </ul>
                    """)
