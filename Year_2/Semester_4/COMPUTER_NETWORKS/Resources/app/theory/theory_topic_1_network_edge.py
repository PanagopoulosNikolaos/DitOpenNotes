"""Topic 1: Network Edge (Δίκτυο στο Έπακρο) theory renderer.

Covers Hosts, End Systems, Client-Server and Peer-to-Peer models,
Access Networks, and Network as a Service.
"""

from nicegui import ui


def renderTopic1NetworkEdge() -> None:
    """Renders the comprehensive theory module for Topic 1: Network Edge."""
    with ui.column().classes("w-full gap-6 text-[#f4f1ea]"):
        # Header Banner
        with ui.column().classes(
            "w-full glass-panel p-6 rounded-2xl border border-[rgba(224,107,58,0.35)] gap-3"
        ):
            with ui.row().classes("items-center gap-3"):
                ui.html('<i class="fa-solid fa-laptop-code text-[#e06b3a] text-2xl"></i>')
                with ui.column().classes("gap-0"):
                    ui.html('<h2 class="text-xl font-bold gradient-title m-0">Θέμα 1: Δίκτυο στο Έπακρο (Network Edge)</h2>')
                    ui.label("Τελικά Συστήματα (Hosts), Μοντέλα Επικοινωνίας Client-Server & P2P, Δίκτυα Πρόσβασης").classes("text-sm text-[#b5b0a4]")

        # Section 1: End Systems & Architecture
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-server text-blue-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">1. Τελικά Συστήματα (End Systems / Hosts)</h3>')

            ui.label(
                "Τα τελικά συστήματα (hosts) είναι οι συσκευές που βρίσκονται στα άκρα του δικτύου και εκτελούν εφαρμογές "
                "(υπολογιστές, servers, smartphones, IoT αισθητήρες). Αποκαλούνται 'τελικά' γιατί αποτελούν την αφετηρία ή τον τερματισμό "
                "της επικοινωνίας, σε αντίθεση με τους ενδιάμεσους κόμβους (routers, switches) που απλώς προωθούν δεδομένα."
            ).classes("text-sm text-[#b5b0a4] leading-relaxed")

            with ui.row().classes("w-full p-4 rounded-xl bg-[#201f1d] border border-[rgba(255,255,255,0.06)] font-mono text-xs text-[#fed7aa] leading-relaxed"):
                ui.html(r"""<pre class="m-0">
  Δίκτυο στο Έπακρο (Network Edge)
  ─────────────────────────────────────────────────────
  [Laptop]   [Smartphone]   [Smart TV]   [IoT Sensor]
      \           |              |             /
       \          |              |            /
        ──────────[Δίκτυο Πρόσβασης (Access Network)]──────
                                  |
                         [Πυρήνας Δικτύου (Network Core)]
                                  |
                         [Άλλα Τελικά Συστήματα]
</pre>""")

        # Section 2: Communication Paradigms (Client-Server vs P2P)
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-network-wired text-[#f59e0b] text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">2. Μοντέλα Επικοινωνίας: Client-Server vs Peer-to-Peer</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs leading-relaxed"):
                # Client-Server Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(79,142,201,0.3)] gap-2"):
                    with ui.row().classes("items-center gap-2"):
                        ui.html('<i class="fa-solid fa-desktop text-blue-400"></i>')
                        ui.label("Client-Server Μοντέλο").classes("font-bold text-blue-300 text-sm")
                    ui.label(
                        "• Κεντρικός Εξυπηρετητής (Server): Always-on μηχάνημα με μόνιμη IP διεύθυνση.\n"
                        "• Πελάτης (Client): Ζητά υπηρεσίες από τον server, συνήθως έχει δυναμική IP.\n"
                        "• Κλιμάκωση (Scalability): Απαιτεί data centers και clusters όταν αυξάνονται οι πελάτες.\n"
                        "• Παραδείγματα: Web (HTTP), Email (SMTP/IMAP), DNS, FTP."
                    ).classes("text-[#b5b0a4] whitespace-pre-line")

                # Peer-to-Peer Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(224,107,58,0.3)] gap-2"):
                    with ui.row().classes("items-center gap-2"):
                        ui.html('<i class="fa-solid fa-arrows-split-up-and-left text-[#e06b3a]"></i>')
                        ui.label("Peer-to-Peer (P2P) Μοντέλο").classes("font-bold text-[#e06b3a] text-sm")
                    ui.label(
                        "• Ισοτιμία Κόμβων: Κάθε κόμβος (peer) δρα ταυτόχρονα ως client και server.\n"
                        "• Αυτο-κλιμάκωση (Self-scalability): Νέοι χρήστες φέρνουν και νέα χωρητικότητα εξυπηρέτησης.\n"
                        "• Δυναμική Φύση: Οι κόμβοι συνδέονται και αποσυνδέονται απροειδοποίητα (churn).\n"
                        "• Παραδείγματα: BitTorrent, Blockchain (Bitcoin, Ethereum)."
                    ).classes("text-[#b5b0a4] whitespace-pre-line")

        # Section 3: Access Networks Summary
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-tower-broadcast text-emerald-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">3. Δίκτυα Πρόσβασης (Access Networks)</h3>')

            ui.label(
                "Το δίκτυο πρόσβασης είναι η φυσική υποδομή που συνδέει ένα τελικό σύστημα με τον πρώτο δρομολογητή "
                "(edge router / default gateway) του παρόχου (ISP)."
            ).classes("text-sm text-[#b5b0a4]")

            with ui.grid().classes("grid-cols-1 md:grid-cols-3 gap-3 w-full text-xs"):
                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-1"):
                    ui.label("Οικιακή Πρόσβαση").classes("font-bold text-amber-400")
                    ui.label("DSL, Cable HFC, FTTH (Οπτική Ίνα)").classes("text-[#b5b0a4]")
                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-1"):
                    ui.label("Εταιρική Πρόσβαση").classes("font-bold text-blue-400")
                    ui.label("Ethernet (100M/1G/10G), Wi-Fi (802.11)").classes("text-[#b5b0a4]")
                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-1"):
                    ui.label("Κινητή Πρόσβαση").classes("font-bold text-emerald-400")
                    ui.label("4G LTE, 5G NR, Δορυφορικό LEO").classes("text-[#b5b0a4]")
