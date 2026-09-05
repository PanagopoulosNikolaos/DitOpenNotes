"""Methodology quick reference cards component for Computer Networks with LaTeX support."""

from nicegui import ui


def renderMethodologyCards() -> None:
    """Renders quick reference cards for core networking formulas with LaTeX math support."""
    with ui.grid().classes("grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 w-full text-xs"):
        # Card 1: Nodal Delay
        with ui.column().classes(
            "p-5 rounded-2xl bg-[#201f1d] border border-[rgba(224,107,58,0.3)] shadow-md gap-2.5 transition-all hover:-translate-y-1 hover:border-[#e06b3a]"
        ):
            with ui.row().classes("items-center justify-between w-full"):
                ui.html('<span class="text-xs font-bold text-[#e06b3a] uppercase tracking-wider">Step 1: Delays</span>')
                ui.html('<i class="fa-solid fa-stopwatch text-[#e06b3a]"></i>')
            ui.html('<h4 class="text-sm font-bold text-[#f4f1ea] m-0">Nodal Delay</h4>')
            ui.markdown(
                "$$d_{\\text{nodal}} = d_{\\text{proc}} + d_{\\text{queue}} + d_{\\text{trans}} + d_{\\text{prop}}$$\n"
                "- $d_{\\text{trans}} = \\frac{L}{R}$ (Transmission)\n"
                "- $d_{\\text{prop}} = \\frac{d}{s}$ (Propagation)"
            ).classes("text-[#b5b0a4] leading-relaxed")

        # Card 2: Pipelining
        with ui.column().classes(
            "p-5 rounded-2xl bg-[#201f1d] border border-[rgba(245,158,11,0.3)] shadow-md gap-2.5 transition-all hover:-translate-y-1 hover:border-[#f59e0b]"
        ):
            with ui.row().classes("items-center justify-between w-full"):
                ui.html('<span class="text-xs font-bold text-amber-400 uppercase tracking-wider">Step 2: Store & Forward</span>')
                ui.html('<i class="fa-solid fa-bars-progress text-amber-400"></i>')
            ui.html('<h4 class="text-sm font-bold text-[#f4f1ea] m-0">Pipelining</h4>')
            ui.markdown(
                "$$T_{\\text{pipelined}} = (N + P - 1)\\frac{L}{R} + N\\frac{d}{s}$$\n"
                "- $N$ links / hops\n"
                "- $P$ packets of size $L$ bits"
            ).classes("text-[#b5b0a4] leading-relaxed")

        # Card 3: Subnetting & LPM
        with ui.column().classes(
            "p-5 rounded-2xl bg-[#201f1d] border border-[rgba(79,142,201,0.3)] shadow-md gap-2.5 transition-all hover:-translate-y-1 hover:border-blue-400"
        ):
            with ui.row().classes("items-center justify-between w-full"):
                ui.html('<span class="text-xs font-bold text-blue-400 uppercase tracking-wider">Step 3: Addressing</span>')
                ui.html('<i class="fa-solid fa-network-wired text-blue-400"></i>')
            ui.html('<h4 class="text-sm font-bold text-[#f4f1ea] m-0">Subnetting & LPM</h4>')
            ui.markdown(
                "- $\\text{Block Size} = 2^{32 - \\text{prefix}}$\n"
                "- $\\text{Hosts} = 2^{32 - \\text{prefix}} - 2$\n"
                "- **LPM:** Longest prefix match selection."
            ).classes("text-[#b5b0a4] leading-relaxed")

        # Card 4: CRC & Error Check
        with ui.column().classes(
            "p-5 rounded-2xl bg-[#201f1d] border border-[rgba(16,185,129,0.3)] shadow-md gap-2.5 transition-all hover:-translate-y-1 hover:border-emerald-400"
        ):
            with ui.row().classes("items-center justify-between w-full"):
                ui.html('<span class="text-xs font-bold text-emerald-400 uppercase tracking-wider">Step 4: Error Checking</span>')
                ui.html('<i class="fa-solid fa-shield-halved text-emerald-400"></i>')
            ui.html('<h4 class="text-sm font-bold text-[#f4f1ea] m-0">CRC Modulo-2 XOR</h4>')
            ui.markdown(
                "- Append $k = \\text{deg}(G)$ zeros to $D$\n"
                "- $R = (D \\cdot 2^k) \\pmod G$\n"
                "- Frame $T = (D \\cdot 2^k) \\oplus R$\n"
                "- Receiver: $T \\pmod G = 0$"
            ).classes("text-[#b5b0a4] leading-relaxed")
