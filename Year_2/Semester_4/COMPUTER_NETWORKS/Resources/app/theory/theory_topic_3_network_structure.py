"""Topic 3: Network Structure (Δομή του Δικτύου) theory renderer.

Covers Network of Networks, Tier-1 ISPs, IXPs, PoPs, Peering vs Transit,
and Content Provider Networks (CDNs).
"""

from nicegui import ui


def renderTopic3NetworkStructure() -> None:
    """Renders the comprehensive theory module for Topic 3: Network Structure."""
    with ui.column().classes("w-full gap-6 text-[#f4f1ea]"):
        # Header Banner
        with ui.column().classes(
            "w-full glass-panel p-6 rounded-2xl border border-[rgba(224,107,58,0.35)] gap-3"
        ):
            with ui.row().classes("items-center gap-3"):
                ui.html('<i class="fa-solid fa-diagram-project text-[#e06b3a] text-2xl"></i>')
                with ui.column().classes("gap-0"):
                    ui.html('<h2 class="text-xl font-bold gradient-title m-0">Θέμα 3: Δομή του Δικτύου (Network Structure)</h2>')
                    ui.label("Δίκτυο Δικτύων (Network of Networks), Tier-1/2/Access ISPs, IXPs, PoPs, Peering & Transit").classes("text-sm text-[#b5b0a4]")

        # Section 1: Network of Networks Hierarchy
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-sitemap text-blue-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">1. Ιεραρχία Παρόχων (ISP Hierarchy)</h3>')

            ui.label(
                "Το διαδίκτυο δεν είναι ένα ενιαίο κεντρικό δίκτυο, αλλά ένα ιεραρχικό σύμπλεγμα αυτόνομων συστημάτων (AS). "
                "Χωρίζεται σε επίπεδα (Tiers) ανάλογα με την παγκόσμια εμβέλεια και τη συνδεσιμότητά τους."
            ).classes("text-sm text-[#b5b0a4] leading-relaxed")

            with ui.grid().classes("grid-cols-1 md:grid-cols-3 gap-3 w-full text-xs"):
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(224,107,58,0.3)] gap-2"):
                    ui.label("Tier-1 ISPs (Παγκόσμιοι)").classes("font-bold text-[#e06b3a] text-sm")
                    ui.label(
                        "• Παγκόσμια κάλυψη με υπερατλαντικές οπτικές ίνες.\n"
                        "• Δεν πληρώνουν κανέναν για transit (settlement-free peering μεταξύ τους).\n"
                        "• Παραδείγματα: AT&T, Lumen/CenturyLink, NTT, Telia, Verizon."
                    ).classes("text-[#b5b0a4] whitespace-pre-line")

                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(245,158,11,0.3)] gap-2"):
                    ui.label("Tier-2 / Regional ISPs").classes("font-bold text-amber-400 text-sm")
                    ui.label(
                        "• Περιφερειακοί / Εθνικοί πάροχοι (π.χ. Cosmote, Vodafone GR).\n"
                        "• Αγοράζουν transit από Tier-1 και συνδέονται μεταξύ τους μέσω IXPs.\n"
                        "• Εξυπηρετούν τοπικούς παρόχους πρόσβασης."
                    ).classes("text-[#b5b0a4] whitespace-pre-line")

                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(79,142,201,0.3)] gap-2"):
                    ui.label("Access ISPs (Πρόσβασης)").classes("font-bold text-blue-400 text-sm")
                    ui.label(
                        "• Το 'τελευταίο μίλι' (last mile) προς τους οικιακούς και εταιρικούς χρήστες.\n"
                        "• Συνδέονται σε Tier-2 ή απευθείας σε περιφερειακά PoPs."
                    ).classes("text-[#b5b0a4] whitespace-pre-line")

        # Section 2: IXPs, PoPs & Peering vs Transit
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-handshake text-emerald-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">2. Σημεία Διασύνδεσης: PoP, IXP, Peering & Transit</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs"):
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-2"):
                    ui.label("PoP (Point of Presence) & Multi-homing").classes("font-bold text-[#f4f1ea]")
                    ui.label(
                        "• PoP: Ομάδα δρομολογητών σε ένα φυσικό σημείο όπου πελάτες/ISP μπορούν να συνδεθούν.\n"
                        "• Multi-homing: Σύνδεση ενός οργανισμού σε 2 ή περισσότερους παρόχους για εφεδρεία και εξισορρόπηση φορτίου."
                    ).classes("text-[#b5b0a4] whitespace-pre-line")

                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-2"):
                    ui.label("IXP (Internet Exchange Point) & Peering").classes("font-bold text-[#f4f1ea]")
                    ui.label(
                        "• IXP: Αυτόνομο κέντρο διασύνδεσης (π.χ. GR-IX στην Ελλάδα, DE-CIX στη Γερμανία) όπου πολλοί ISPs συνδέουν τα δίκτυά τους.\n"
                        "• Peering: Απευθείας ανταλλαγή κίνησης μεταξύ δύο ISPs χωρίς χρέωση transit."
                    ).classes("text-[#b5b0a4] whitespace-pre-line")
