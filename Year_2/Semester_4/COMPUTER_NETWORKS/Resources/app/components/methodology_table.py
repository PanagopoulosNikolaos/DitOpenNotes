"""Methodology and protocol comparison tables component for Computer Networks."""

from nicegui import ui


def renderMethodologyTable() -> None:
    """Renders comprehensive reference and comparison tables for networking."""
    with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-6"):
        with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
            ui.html('<i class="fa-solid fa-table-list text-[#f59e0b] text-xl"></i>')
            with ui.column().classes("gap-0"):
                ui.html('<h2 class="text-xl font-bold gradient-title m-0">Συγκριτικοί Πίνακες & Μεθοδολογία</h2>')
                ui.label("Συνοπτικοί πίνακες διάκρισης τεχνολογιών, συσκευών και πρωτοκόλλων").classes("text-xs text-[#b5b0a4]")

        # Table 1: Device vs Domains Matrix
        with ui.column().classes("w-full gap-2"):
            ui.html('<h3 class="text-sm font-bold text-[#fed7aa] m-0">1. Πίνακας Συσκευών, Επιπέδων OSI & Πεδίων Συγκρούσεων/Εκπομπής</h3>')
            with ui.row().classes("w-full p-4 rounded-xl bg-[#201f1d] border border-[rgba(255,255,255,0.06)] font-mono text-xs text-[#fed7aa] overflow-x-auto"):
                ui.html("""<pre class="m-0">
  Συσκευή               Επίπεδο OSI     PDU             Collision Domains (Συγκρούσεων)     Broadcast Domains (Εκπομπής)    Λειτουργία & Χαρακτηριστικά
  ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
  Repeater / Hub        Layer 1 (Phys)  Bit             1 Ενιαίο για όλες τις θύρες         1 Ενιαίο                        Αναπαράγει ηλεκτρικό/οπτικό σήμα χωρίς έλεγχο.
  Bridge / Switch       Layer 2 (Link)  Frame (Πλαίσιο) 1 ανά φυσική θύρα (Microsegment)    1 Ενιαίο                        Φιλτράρισμα βάσει MAC διευθύνσεων (MAC Table).
  Router (Δρομολογητής) Layer 3 (Net)   Packet (Πακέτο) 1 ανά φυσικό interface              1 ανά φυσικό interface          Διαχωρίζει broadcast domains, δρομολογεί με IP.
  Gateway (Πύλη)        Layer 4-7       Segment/Message 1 ανά σύνδεση                       1 ανά σύνδεση                   Μετάφραση πρωτοκόλλων ανώτερων επιπέδων.
</pre>""")

        # Table 2: Routing Protocols Comparison
        with ui.column().classes("w-full gap-2"):
            ui.html('<h3 class="text-sm font-bold text-[#fed7aa] m-0">2. Σύγκριση Πρωτοκόλλων Εσωτερικής & Εξωτερικής Δρομολόγησης</h3>')
            with ui.row().classes("w-full p-4 rounded-xl bg-[#201f1d] border border-[rgba(255,255,255,0.06)] font-mono text-xs text-[#fed7aa] overflow-x-auto"):
                ui.html("""<pre class="m-0">
  Πρωτόκολλο      Τύπος Αλγορίθμου          Metric (Μετρικό)            Σύγκλιση (Convergence)      Χρήση & Περιορισμοί
  ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
  RIPv1 / RIPv2   Distance-Vector (Bellman) Hop Count (Μέγιστο 15 hops) Αργή (Count to Infinity)    Μικρά δίκτυα LAN/Campus.
  OSPF            Link-State (Dijkstra)     Cost (Αντίστροφο Bandwidth) Πολύ Γρήγορη (LSA Flooding) Μεγάλα εταιρικά δίκτυα & ISPs.
  BGP (Border)    Path-Vector (Policy-based)AS-Path + BGP Attributes    Σταθερή (Policy Routing)    Διασύνδεση Αυτόνομων Συστημάτων (Internet).
</pre>""")
