"""Topic 4: Access Technologies (Τεχνολογίες Πρόσβασης) theory renderer.

Covers DSL, Cable HFC, FTTH (PON), Ethernet LANs, Wi-Fi (802.11),
and Cellular Networks (4G LTE / 5G NR).
"""

from nicegui import ui


def renderTopic4AccessTechnologies() -> None:
    """Renders the comprehensive theory module for Topic 4: Access Technologies."""
    with ui.column().classes("w-full gap-6 text-[#f4f1ea]"):
        # Header Banner
        with ui.column().classes(
            "w-full glass-panel p-6 rounded-2xl border border-[rgba(224,107,58,0.35)] gap-3"
        ):
            with ui.row().classes("items-center gap-3"):
                ui.html('<i class="fa-solid fa-wifi text-[#e06b3a] text-2xl"></i>')
                with ui.column().classes("gap-0"):
                    ui.html('<h2 class="text-xl font-bold gradient-title m-0">Θέμα 4: Τεχνολογίες Πρόσβασης (Access Technologies)</h2>')
                    ui.label("DSL, Cable/HFC, FTTH (PON/GPON), Ethernet LAN, Wi-Fi 802.11, Κινητή Τηλεφωνία 4G/5G").classes("text-sm text-[#b5b0a4]")

        # Section 1: Residential Access Comparison Table
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-house-signal text-amber-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">1. Σύγκριση Οικιακών Τεχνολογιών Πρόσβασης</h3>')

            with ui.row().classes("w-full p-4 rounded-xl bg-[#201f1d] border border-[rgba(255,255,255,0.06)] font-mono text-xs text-[#fed7aa] overflow-x-auto"):
                ui.html("""<pre class="m-0">
  Τεχνολογία      Φυσικό Μέσο              Μοντέλο Διαμοιρασμού      Downstream / Upstream     Χαρακτηριστικά / Περιορισμοί
  ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
  DSL / VDSL      Συνεστραμμένο Χάλκινο    Αποκλειστικό (Dedicated)  24-100 Mbps / 1-20 Mbps   Εξασθένηση με την απόσταση από το CO / DSLAM.
  Cable (HFC)     Ομοαξονικό + Ίνα         Διαμοιραζόμενο (Shared)   100-1000 Mbps / 50 Mbps   DOCSIS standard. Συμφόρηση σε ώρες αιχμής.
  FTTH (GPON)     Οπτική Ίνα               Διαμοιραζόμενο (PON Split) 100-2500 Mbps / 1 Gbps    Μηδενική ηλεκτρομαγνητική παρεμβολή, τεράστια εμβέλεια.
  Ethernet        UTP Cat6 / Οπτική        Αποκλειστικό ανά Port     100M / 1G / 10 Gbps Symm  Εταιρικά LANs, μέγιστο μήκος χαλκού 100m.
  Wi-Fi (802.11)  Ασύρματο (2.4/5/6 GHz)   Διαμοιραζόμενο (CSMA/CA)  54M - 9.6 Gbps            Επηρεάζεται από εμπόδια, παρεμβολές και απόσταση.
  5G NR           Κινητό Ασύρματο          Διαμοιραζόμενο (OFDMA)    100M - 10 Gbps            Ultra-low latency (&lt;1ms), Massive IoT.
</pre>""")

        # Section 2: Deep Dive: FTTH Architectures
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-network-wired text-emerald-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">2. Αρχιτεκτονική FTTH: PON vs AON</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs leading-relaxed"):
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-2"):
                    ui.label("PON (Passive Optical Network)").classes("font-bold text-emerald-400 text-sm")
                    ui.label(
                        "• Χρησιμοποιεί παθητικούς οπτικούς διαχωριστές (optical splitters) χωρίς τροφοδοσία ρεύματος.\n"
                        "• OLT (Optical Line Terminal) στο κεντρικό γραφείο, ONT/ONU στο σπίτι του συνδρομητή.\n"
                        "• Χαμηλό κόστος συντήρησης και εγκατάστασης, κυρίαρχο στην αγορά (GPON, XGS-PON)."
                    ).classes("text-[#b5b0a4] whitespace-pre-line")

                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-2"):
                    ui.label("AON (Active Optical Network)").classes("font-bold text-blue-400 text-sm")
                    ui.label(
                        "• Χρησιμοποιεί ενεργούς δρομολογητές/μεταγωγείς που απαιτούν ρεύμα στις ενδιάμεσες διασταυρώσεις.\n"
                        "• Προσφέρει αποκλειστικό εύρος ζώνης (dedicated bandwidth) ανά συνδρομητή.\n"
                        "• Υψηλότερο κόστος και πολυπλοκότητα λειτουργίας."
                    ).classes("text-[#b5b0a4] whitespace-pre-line")
