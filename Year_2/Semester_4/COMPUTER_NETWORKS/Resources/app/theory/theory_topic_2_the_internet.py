"""Topic 2: The Internet and Protocols theory renderer.

Covers Internet definition, RFC standardization, Protocol Layering (OSI vs TCP/IP),
Encapsulation/Decapsulation, and Service Models.
"""

from nicegui import ui


def renderTopic2TheInternet() -> None:
    """Renders the comprehensive theory module for Topic 2: The Internet & Protocols."""
    with ui.column().classes("w-full gap-6 text-[#f4f1ea]"):
        # Header Banner
        with ui.column().classes(
            "w-full glass-panel p-6 rounded-2xl border border-[rgba(224,107,58,0.35)] gap-3"
        ):
            with ui.row().classes("items-center gap-3"):
                ui.html('<i class="fa-solid fa-globe text-[#e06b3a] text-2xl"></i>')
                with ui.column().classes("gap-0"):
                    ui.html('<h2 class="text-xl font-bold gradient-title m-0">Θέμα 2: Το Διαδίκτυο & Πρωτόκολλα (The Internet & Protocols)</h2>')
                    ui.label("Πρότυπα RFC, Μοντέλο Στρωμάτωσης (OSI vs TCP/IP), Ενθυλάκωση & Μοντέλα Υπηρεσιών").classes("text-sm text-[#b5b0a4]")

        # Section 1: Protocols & RFC
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-file-contract text-blue-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">1. Τι είναι ένα Πρωτόκολλο & Πρότυπα RFC</h3>')

            ui.label(
                "Ένα πρωτόκολλο επικοινωνίας ορίζει τη μορφή (format), τη σειρά των μηνυμάτων που ανταλλάσσονται "
                "μεταξύ δύο ή περισσότερων οντοτήτων, καθώς και τις ενέργειες που εκτελούνται κατά τη λήψη ή αποστολή."
            ).classes("text-sm text-[#b5b0a4] leading-relaxed")

            with ui.grid().classes("grid-cols-1 md:grid-cols-3 gap-3 w-full text-xs"):
                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-1"):
                    ui.label("IETF (Internet Engineering Task Force)").classes("font-bold text-amber-400")
                    ui.label("Αναπτύσσει τα επίσημα πρότυπα του διαδικτύου ως RFC (Request For Comments).").classes("text-[#b5b0a4]")
                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-1"):
                    ui.label("IEEE (Institute of Electrical and Electronics Engineers)").classes("font-bold text-blue-400")
                    ui.label("Προτυποποιεί τα φυσικά και ζευκτικά επίπεδα (π.χ. IEEE 802.3 Ethernet, 802.11 Wi-Fi).").classes("text-[#b5b0a4]")
                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-1"):
                    ui.label("ISO & ITU-T").classes("font-bold text-emerald-400")
                    ui.label("Διεθνείς οργανισμοί για το μοντέλο αναφοράς OSI και τηλεπικοινωνιακά πρότυπα.").classes("text-[#b5b0a4]")

        # Section 2: Layering: OSI vs TCP/IP
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-layer-group text-[#f59e0b] text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">2. Αρχιτεκτονική Στρωμάτωσης: OSI 7-Layer vs TCP/IP 5-Layer</h3>')

            with ui.row().classes("w-full p-4 rounded-xl bg-[#201f1d] border border-[rgba(255,255,255,0.06)] font-mono text-xs text-[#fed7aa] overflow-x-auto"):
                ui.html(r"""<pre class="m-0">
  OSI 7 Επίπεδα                 TCP/IP 5 Επίπεδα        PDU             Συσκευές / Παραδείγματα
  ─────────────────────────────────────────────────────────────────────────────────────────────
  7. Application (Εφαρμογής)   \                       Μήνυμα (Message) HTTP, SMTP, DNS, SSH
  6. Presentation (Παρουσίασης) ── 5. Application                      JSON, TLS/SSL, MPEG
  5. Session (Συνόδου)         /                                       NetBIOS, RPC
  4. Transport (Μεταφοράς)     ── 4. Transport          Τμήμα (Segment) TCP, UDP (Port Numbers)
  3. Network (Δικτύου)         ── 3. Network            Πακέτο (Packet) IPv4, IPv6, ICMP, Routers
  2. Data Link (Σύνδεσης)      ── 2. Data Link          Πλαίσιο (Frame) Ethernet, Wi-Fi, Switches
  1. Physical (Φυσικό)         ── 1. Physical           Bit             Hubs, Repeaters, Cables
</pre>""")

        # Section 3: Encapsulation & Decapsulation
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-box-open text-emerald-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">3. Ενθυλάκωση (Encapsulation) & Αποενθυλάκωση</h3>')

            ui.label(
                "Κατά την αποστολή δεδομένων, κάθε επίπεδο προσθέτει τη δική του κεφαλίδα (header - και στο L2 trailer). "
                "Κατά τη λήψη, κάθε επίπεδο αφαιρεί την κεφαλίδα του και προωθεί το ωφέλιμο φορτίο (payload) στο ανώτερο επίπεδο."
            ).classes("text-sm text-[#b5b0a4]")

            with ui.column().classes("w-full p-4 rounded-xl bg-[#201f1d] border border-[rgba(224,107,58,0.2)] font-mono text-xs text-[#fed7aa]"):
                ui.html("""<pre class="m-0">
  [Application] : [                  Data / Payload                  ]
  [Transport]   : [ TH |             Data / Payload                  ]  (Segment)
  [Network]     : [ NH | TH |        Data / Payload                  ]  (Packet)
  [Data Link]   : [ DH | NH | TH |   Data / Payload             | DT ]  (Frame)
  [Physical]    :  0 1 1 0 1 0 0 1 0 1 1 1 0 1 0 0 1 0 1 1 0 1 0 0 1 0  (Bits on wire)
</pre>""")
