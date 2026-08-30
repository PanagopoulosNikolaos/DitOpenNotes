"""Topic 7: Basic Networking Issues (Βασικά Θέματα Δικτύωσης) theory renderer.

Covers Addressing (MAC, IP, Port), ARP, Routing Algorithms (Dijkstra Link-State,
Bellman-Ford Distance-Vector), Error Detection (CRC Modulo-2 XOR),
and Collision vs Broadcast Domains.
"""

from nicegui import ui


def renderTopic7BasicNetworkingIssues() -> None:
    """Renders the comprehensive theory module for Topic 7: Basic Networking Issues."""
    with ui.column().classes("w-full gap-6 text-[#f4f1ea]"):
        # Header Banner
        with ui.column().classes(
            "w-full glass-panel p-6 rounded-2xl border border-[rgba(224,107,58,0.35)] gap-3"
        ):
            with ui.row().classes("items-center gap-3"):
                ui.html('<i class="fa-solid fa-microchip text-[#e06b3a] text-2xl"></i>')
                with ui.column().classes("gap-0"):
                    ui.html('<h2 class="text-xl font-bold gradient-title m-0">Θέμα 7: Βασικά Θέματα Δικτύωσης</h2>')
                    ui.label("Διευθυνσιοδότηση (MAC/IP), Πρωτόκολλο ARP, Αλγόριθμοι Δρομολόγησης (Dijkstra, Distance-Vector), Έλεγχος Σφαλμάτων (CRC)").classes("text-sm text-[#b5b0a4]")

        # Section 1: Addressing Hierarchy
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-address-card text-blue-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">1. Ιεραρχία Διευθυνσιοδότησης & Πρωτόκολλο ARP</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-3 gap-3 w-full text-xs"):
                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-1"):
                    ui.label("MAC Address (Επίπεδο 2)").classes("font-bold text-amber-400")
                    ui.label("48 bits (6 bytes, π.χ. 00:1A:2B:3C:4D:5E). Επίπεδη (flat) φυσική διεύθυνση κάρτας δικτύου. Αλλάζει σε κάθε hop.").classes("text-[#b5b0a4]")

                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-1"):
                    ui.label("IP Address (Επίπεδο 3)").classes("font-bold text-blue-400")
                    ui.label("32 bits IPv4 / 128 bits IPv6. Ιεραρχική λογική διεύθυνση (Network ID + Host ID). Παραμένει σταθερή από άκρο σε άκρο.").classes("text-[#b5b0a4]")

                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-1"):
                    ui.label("Port Number (Επίπεδο 4)").classes("font-bold text-emerald-400")
                    ui.label("16 bits (0-65535, π.χ. 80 HTTP, 443 HTTPS). Ταυτοποιεί τη συγκεκριμένη διεργασία/εφαρμογή στον υπολογιστή.").classes("text-[#b5b0a4]")

            # ARP details
            with ui.column().classes("w-full p-4 rounded-xl bg-[#201f1d] border border-[rgba(79,142,201,0.25)] gap-2 text-xs"):
                ui.label("Λειτουργία Address Resolution Protocol (ARP):").classes("font-bold text-blue-300 text-sm")
                ui.label(
                    "• Σκοπός: Μετάφραση γνωστής IP διεύθυνσης σε άγνωστη MAC διεύθυνση στο ίδιο τοπικό δίκτυο (LAN).\n"
                    "• ARP Request: Αποστέλλεται ως Broadcast (MAC: FF-FF-FF-FF-FF-FF) - το λαμβάνουν όλοι οι κόμβοι στο LAN segment.\n"
                    "• ARP Reply: Ο κόμβος με την αντίστοιχη IP απαντά με Unicast απευθείας στον αιτούντα.\n"
                    "• ARP Cache: Προσωρινός πίνακας αντιστοιχήσεων στη μνήμη (TTL συνήθως 15-20 λεπτά) για αποφυγή επαναλαμβανόμενων broadcasts."
                ).classes("text-[#b5b0a4] whitespace-pre-line")

        # Section 2: Error Detection & CRC Modulo-2
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-calculator text-[#f59e0b] text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">2. Έλεγχος Σφαλμάτων: Cyclic Redundancy Check (CRC)</h3>')

            ui.label(
                "Ο κυκλικός έλεγχος πλεονασμού (CRC) βασίζεται στη διαίρεση δυαδικών πολυωνύμων με αριθμητική Modulo-2 "
                "(αποκλειστικό Ή - XOR χωρίς κρατούμενα)."
            ).classes("text-sm text-[#b5b0a4]")

            with ui.column().classes("w-full p-4 rounded-xl bg-[#201f1d] border border-[rgba(245,158,11,0.25)] font-mono text-xs text-[#fed7aa] leading-relaxed"):
                ui.html("""<pre class="m-0">
  Βήματα Υπολογισμού CRC:
  1. Δεδομένα D μεγέθους d bits, Πολυώνυμο Γεννήτορας G βαθμού k (άρα k+1 bits).
  2. Προσάρτηση k μηδενικών στο τέλος του D -> D * 2^k.
  3. Διαίρεση (D * 2^k) με το G με πράξεις XOR (1 XOR 1 = 0, 0 XOR 0 = 0, 1 XOR 0 = 1).
  4. Το υπόλοιπο R της διαίρεσης είναι το Frame Check Sequence (FCS) μεγέθους k bits.
  5. Μεταδιδόμενο Πλαίσιο T = (D * 2^k) XOR R.
  6. Στον παραλήπτη: Αν T mod G == 0 -> Δεν ανιχνεύτηκε σφάλμα!
</pre>""")

        # Section 3: Routing Algorithms (Dijkstra vs Bellman-Ford)
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-network-wired text-emerald-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">3. Αλγόριθμοι Δρομολόγησης: Link-State vs Distance-Vector</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs leading-relaxed"):
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(16,185,129,0.3)] gap-2"):
                    ui.label("Link-State (Dijkstra) - π.χ. OSPF, IS-IS").classes("font-bold text-emerald-400 text-sm")
                    ui.label(
                        "• Καθολική Γνώση: Κάθε δρομολογητής μαθαίνει την πλήρη τοπολογία του δικτύου μέσω Link-State Broadcasts.\n"
                        "• Αλγόριθμος: Εκτελεί τοπικά τον αλγόριθμο Dijkstra για εύρεση συντομότερων μονοπατιών.\n"
                        "• Χρονική Πολυπλοκότητα: O(V^2) ή O(E log V).\n"
                        "• Πλεονέκτημα: Γρήγορη σύγκλιση, μηδενικοί βρόχοι δρομολόγησης."
                    ).classes("text-[#b5b0a4] whitespace-pre-line")

                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(224,107,58,0.3)] gap-2"):
                    ui.label("Distance-Vector (Bellman-Ford) - π.χ. RIP").classes("font-bold text-[#e06b3a] text-sm")
                    ui.label(
                        "• Κατανεμημένη Γνώση: Κάθε κόμβος ανταλλάσσει διανύσματα αποστάσεων μόνο με τους άμεσους γείτονές του.\n"
                        "• Εξίσωση Bellman-Ford: d_x(y) = min_v { c(x,v) + d_v(y) }.\n"
                        "• Μειονεκτήματα: Αργή σύγκλιση, πρόβλημα μέτρησης στο άπειρο (Count-to-Infinity), βρόχοι δρομολόγησης."
                    ).classes("text-[#b5b0a4] whitespace-pre-line")

        # Section 4: Collision Domains vs Broadcast Domains
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-arrows-to-dot text-amber-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">4. Πεδία Συγκρούσεων (Collision) & Πεδία Εκπομπής (Broadcast)</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-3 gap-3 w-full text-xs"):
                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-1"):
                    ui.label("Hub / Repeater (Layer 1)").classes("font-bold text-red-400")
                    ui.label("1 Collision Domain για όλες τις θύρες. 1 Broadcast Domain. Αναπαράγει ηλεκτρικά σήματα παντού.").classes("text-[#b5b0a4]")

                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-1"):
                    ui.label("Bridge / Switch (Layer 2)").classes("font-bold text-blue-400")
                    ui.label("Κάθε φυσική θύρα είναι ξεχωριστό Collision Domain (Microsegmentation). Όλες οι θύρες στο ίδιο Broadcast Domain.").classes("text-[#b5b0a4]")

                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-1"):
                    ui.label("Router (Layer 3)").classes("font-bold text-emerald-400")
                    ui.label("Διαχωρίζει και τα Collision Domains και τα Broadcast Domains. Κάθε interface ανήκει σε διαφορετικό υποδίκτυο.").classes("text-[#b5b0a4]")
