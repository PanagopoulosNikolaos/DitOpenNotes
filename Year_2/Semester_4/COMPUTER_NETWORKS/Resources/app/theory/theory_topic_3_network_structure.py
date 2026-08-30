"""Topic 3: Network Structure (Δομή του Δικτύου) theory renderer.

Covers Network of Networks, Hierarchical ISP Tiers (1, 2, 3), PoPs, IXPs,
Settlement-Free Peering vs Paid Transit, Content Provider Networks (Google/Meta),
Core vs Edge, Statistical Multiplexing, and Traceroute across Autonomous Systems.
"""

from nicegui import ui


def renderTopic3NetworkStructure() -> None:
    """Renders the comprehensive theory module for Topic 3: Network Structure."""
    with ui.column().classes("w-full gap-6 text-[#f4f1ea] latex-target"):
        # Header Banner
        with ui.column().classes(
            "w-full glass-panel p-6 md:p-8 rounded-2xl border border-[rgba(224,107,58,0.35)] gap-3"
        ):
            with ui.row().classes("items-center gap-3"):
                ui.html('<i class="fa-solid fa-diagram-project text-[#e06b3a] text-3xl"></i>')
                with ui.column().classes("gap-0"):
                    ui.html('<h2 class="text-xl md:text-2xl font-bold gradient-title m-0">Θέμα 3: Δομή του Δικτύου (Network Structure & ISPs)</h2>')
                    ui.label(
                        "Δίκτυο Δικτύων (Network of Networks), Ιεραρχία Παρόχων Tier 1/2/3, "
                        "PoPs, IXPs, Peering vs Transit, Δίκτυα Παρόχων Περιεχομένου και Πυρήνας Δικτύου."
                    ).classes("text-xs md:text-sm text-[#b5b0a4]")

        # =========================================================================
        # SECTION 1: Network of Networks Architecture
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-network-wired text-blue-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">1. Το Διαδίκτυο ως "Δίκτυο Δικτύων" (Network of Networks)</h3>')

            ui.label(
                "Το Διαδίκτυο δεν είναι μια ενιαία κεντρική οντότητα, αλλά μια χαοτική αλλά άριστα οργανωμένη διασύνδεση "
                "δεκάδων χιλιάδων Αυτόνομων Συστημάτων (Autonomous Systems - AS) που ανήκουν σε εμπορικούς ISPs, πανεπιστήμια, "
                "κυβερνήσεις και παρόχους περιεχομένου. Η διασύνδεσή τους στηρίζεται σε ιεραρχική δομή και οικονομικές συμφωνίες."
            ).classes("text-xs md:text-sm text-[#b5b0a4] leading-relaxed")

            with ui.column().classes("w-full p-4 rounded-xl bg-[#141413] border border-[rgba(255,255,255,0.06)] font-mono text-xs text-[#fed7aa]"):
                ui.html(r"""<pre class="m-0 overflow-x-auto">
  Ιεραρχική Δομή Παγκόσμιου Διαδικτύου
  ─────────────────────────────────────────────────────────────────────────────
                [Tier-1 ISP A] <=== Peering (Δωρεάν) ===> [Tier-1 ISP B]
                    /       \                                  /       \
             Transit $       Transit $                  Transit $     Transit $
                  /           \                            /             \
          [Tier-2 ISP 1] <--- IXP Peering ---> [Tier-2 ISP 2]      [Content Net]
              /       \                               /          (Google/Meta)
       Transit $     Transit $                 Transit $               |
            /           \                         /               [Edge Caches]
      [Access ISP A] [Access ISP B]        [Access ISP C]              |
          /    \          |                      |                     |
     [Home]  [Corp]    [Home]                  [Home] ─────────── Direct Peering
</pre>""")

        # =========================================================================
        # SECTION 2: ISP Tiers & Interconnection Elements
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-sitemap text-amber-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">2. Ιεραρχία Παρόχων (Tiers) & Σημεία Διασύνδεσης (PoP / IXP)</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-3 gap-3 w-full text-xs"):
                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(224,107,58,0.25)] gap-1.5"):
                    ui.label("Tier-1 ISPs (Global Backbone)").classes("font-bold text-[#e06b3a]")
                    ui.label(
                        "• Παγκόσμια κάλυψη με ιδιόκτητες υποβρύχιες και διηπειρωτικές οπτικές ίνες (AT&T, NTT, Lumen, Telia).\n"
                        "• Δεν πληρώνουν κανέναν για transit. Συνδέονται μεταξύ τους με Settlement-Free Peering (πλήρης διασύνδεση full-mesh)."
                    ).classes("text-[#b5b0a4] leading-relaxed")

                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(245,158,11,0.25)] gap-1.5"):
                    ui.label("Tier-2 ISPs (Regional)").classes("font-bold text-amber-300")
                    ui.label(
                        "• Περιφερειακοί ή εθνικοί πάροχοι (π.χ. Vodafone, Cosmote).\n"
                        "• Αγοράζουν transit από Tier-1 παρόχους για πρόσβαση στον υπόλοιπο κόσμο.\n"
                        "• Κάνουν Peering μεταξύ τους σε IXPs για μείωση κόστους διακίνησης τοπικής κίνησης."
                    ).classes("text-[#b5b0a4] leading-relaxed")

                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(79,142,201,0.25)] gap-1.5"):
                    ui.label("Tier-3 / Access ISPs (Local)").classes("font-bold text-blue-300")
                    ui.label(
                        "• Τοπικοί πάροχοι τελευταίου μιλίου (last-mile).\n"
                        "• Συνδέουν τελικούς χρήστες, κατοικίες και τοπικές επιχειρήσεις.\n"
                        "• Πληρώνουν transit στους ανώτερους Tier-2 ή Tier-1 παρόχους."
                    ).classes("text-[#b5b0a4] leading-relaxed")

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs mt-2"):
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(16,185,129,0.25)] gap-2"):
                    ui.label("Σημεία Παρουσίας (PoP) & Σημεία Ανταλλαγής (IXP)").classes("font-bold text-emerald-300 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1.5 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Point of Presence (PoP):</strong> Ομάδα από routers και switches σε μια τοποθεσία όπου ένας πελάτης ISP μπορεί να συνδεθεί φυσικά στον πάροχο.</li>
                        <li><strong class="text-stone-200">Internet Exchange Point (IXP):</strong> Ανεξάρτητη υποδομή (συνήθως μεγάλο switch fabric σε data center) όπου πολλαπλοί ISPs και CDNs συνδέονται για απευθείας ανταλλαγή κίνησης (peering) χωρίς χρέωση transit (π.χ. GR-IX στην Ελλάδα, DE-CIX στη Φρανκφούρτη).</li>
                    </ul>
                    """)

                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(239,68,68,0.25)] gap-2"):
                    ui.label("Peering vs Transit (Οικονομικό Μοντέλο)").classes("font-bold text-red-300 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1.5 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Transit (Επί πληρωμή):</strong> Ο πελάτης-ISP πληρώνει τον ανώτερο ISP ανάλογα με το εύρος ζώνης (Gbps) για να αποκτήσει πρόσβαση σε <em>ολόκληρο το παγκόσμιο Διαδίκτυο</em>.</li>
                        <li><strong class="text-stone-200">Peering (Συνήθως Δωρεάν):</strong> Δύο ISPs συμφωνούν να ανταλλάσσουν κίνηση <em>αποκλειστικά μεταξύ των δικών τους πελατών</em> χωρίς οικονομική συναλλαγή, εξοικονομώντας έξοδα transit.</li>
                    </ul>
                    """)

        # =========================================================================
        # SECTION 3: Content Provider Networks
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-server text-cyan-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">3. Ιδιωτικά Δίκτυα Παρόχων Περιεχομένου (Google, Meta, Microsoft)</h3>')

            ui.label(
                "Οι μεγάλοι κολοσσοί περιεχομένου (Content Providers) δεν βασίζονται αποκλειστικά στους εμπορικούς ISPs. "
                "Κατασκευάζουν δικά τους ιδιωτικά παγκόσμια δίκτυα οπτικών ινών, διασυνδέοντας τα Data Centers τους και "
                "τοποθετώντας Edge Servers / Caches μέσα στα δίκτυα των τοπικών παρόχων πρόσβασης (Tier-3)."
            ).classes("text-xs md:text-sm text-[#b5b0a4]")

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs"):
                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(6,182,212,0.25)] gap-1"):
                    ui.label("Παράκαμψη Ανώτερων Tiers (Bypass)").classes("font-bold text-cyan-300")
                    ui.label(
                        "Με το να συνδέονται απευθείας με τοπικούς Access ISPs στα IXPs ή να τοποθετούν CDN caches στα άκρα, "
                        "παρακάμπτουν τα κόστη transit των Tier-1/2 παρόχων και προσφέρουν ελάχιστο RTT στους χρήστες."
                    ).classes("text-[#b5b0a4]")

                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(6,182,212,0.25)] gap-1"):
                    ui.label("Έλεγχος Ποιότητας Υπηρεσίας (QoS)").classes("font-bold text-cyan-300")
                    ui.label(
                        "Η κίνηση μεταφέρεται σχεδόν μέχρι το σπίτι του χρήστη μέσα από το ιδιωτικό, ελεγχόμενο backbone του παρόχου "
                        "περιεχομένου, αποφεύγοντας τη συμφόρηση του δημόσιου Ίντερνετ."
                    ).classes("text-[#b5b0a4]")
