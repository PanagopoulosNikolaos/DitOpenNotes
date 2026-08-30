"""Methodology quick reference cards component for Computer Networks."""

from nicegui import ui


def renderMethodologyCards() -> None:
    """Renders quick reference cards for core networking formulas and methodologies."""
    with ui.grid().classes("grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 w-full text-xs"):
        # Card 1: Nodal Delay
        with ui.column().classes(
            "p-5 rounded-2xl bg-[#201f1d] border border-[rgba(224,107,58,0.3)] shadow-md gap-2.5 transition-all hover:-translate-y-1 hover:border-[#e06b3a]"
        ):
            with ui.row().classes("items-center justify-between w-full"):
                ui.html('<span class="text-xs font-bold text-[#e06b3a] uppercase tracking-wider">Βήμα 1: Καθυστερήσεις</span>')
                ui.html('<i class="fa-solid fa-stopwatch text-[#e06b3a]"></i>')
            ui.html('<h4 class="text-sm font-bold text-[#f4f1ea] m-0">Κομβική Καθυστέρηση</h4>')
            ui.label(
                "d_nodal = d_proc + d_queue + d_trans + d_prop\n"
                "• d_trans = L / R (Μετάδοση)\n"
                "• d_prop = d / s (Διάδοση)"
            ).classes("text-[#b5b0a4] font-mono leading-relaxed whitespace-pre-line")

        # Card 2: Pipelining
        with ui.column().classes(
            "p-5 rounded-2xl bg-[#201f1d] border border-[rgba(245,158,11,0.3)] shadow-md gap-2.5 transition-all hover:-translate-y-1 hover:border-[#f59e0b]"
        ):
            with ui.row().classes("items-center justify-between w-full"):
                ui.html('<span class="text-xs font-bold text-amber-400 uppercase tracking-wider">Βήμα 2: Store & Forward</span>')
                ui.html('<i class="fa-solid fa-bars-progress text-amber-400"></i>')
            ui.html('<h4 class="text-sm font-bold text-[#f4f1ea] m-0">Σωλήνωση (Pipelining)</h4>')
            ui.label(
                "Για P πακέτα σε N ζεύξεις:\n"
                "T = (N + P - 1) * (L / R) + Σ(d_prop)\n"
                "Χωρίς πακέτα (1 πακέτο): T = N * (L/R) + Σ(d_prop)"
            ).classes("text-[#b5b0a4] font-mono leading-relaxed whitespace-pre-line")

        # Card 3: Subnetting & LPM
        with ui.column().classes(
            "p-5 rounded-2xl bg-[#201f1d] border border-[rgba(79,142,201,0.3)] shadow-md gap-2.5 transition-all hover:-translate-y-1 hover:border-blue-400"
        ):
            with ui.row().classes("items-center justify-between w-full"):
                ui.html('<span class="text-xs font-bold text-blue-400 uppercase tracking-wider">Βήμα 3: Διευθυνσιοδότηση</span>')
                ui.html('<i class="fa-solid fa-network-wired text-blue-400"></i>')
            ui.html('<h4 class="text-sm font-bold text-[#f4f1ea] m-0">Υποδικτύωση & LPM</h4>')
            ui.label(
                "• Block Size = 2^(32 - prefix)\n"
                "• Hosts = 2^(32 - prefix) - 2\n"
                "• Longest Prefix Match: Επιλογή εξόδου με το μεγαλύτερο μήκος μάσκας."
            ).classes("text-[#b5b0a4] font-mono leading-relaxed whitespace-pre-line")

        # Card 4: CRC & Error Check
        with ui.column().classes(
            "p-5 rounded-2xl bg-[#201f1d] border border-[rgba(16,185,129,0.3)] shadow-md gap-2.5 transition-all hover:-translate-y-1 hover:border-emerald-400"
        ):
            with ui.row().classes("items-center justify-between w-full"):
                ui.html('<span class="text-xs font-bold text-emerald-400 uppercase tracking-wider">Βήμα 4: Έλεγχος Σφαλμάτων</span>')
                ui.html('<i class="fa-solid fa-shield-halved text-emerald-400"></i>')
            ui.html('<h4 class="text-sm font-bold text-[#f4f1ea] m-0">CRC Modulo-2 XOR</h4>')
            ui.label(
                "• Προσάρτηση k μηδενικών στο D\n"
                "• Διαίρεση (D * 2^k) mod G με XOR\n"
                "• Πλαίσιο T = (D * 2^k) XOR R\n"
                "• Παραλήπτης: T mod G == 0"
            ).classes("text-[#b5b0a4] font-mono leading-relaxed whitespace-pre-line")
