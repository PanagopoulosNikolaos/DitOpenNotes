"""Topic 6: Data Switching & Routing theory renderer.

Covers Packet vs Circuit Switching, Statistical Multiplexing, Store-and-Forward Pipelining,
the 4 Nodal Delays with LaTeX formulas, Traffic Intensity, Routing (Control Plane) vs Forwarding (Data Plane),
and Forwarding Tables with Longest Prefix Match (LPM).
"""

from nicegui import ui


def renderTopic6DataSwitchingAndRouting() -> None:
    """Renders the comprehensive theory module for Topic 6: Data Switching & Routing."""
    with ui.column().classes("w-full gap-6 text-[#f4f1ea] latex-target"):
        # Header Banner
        with ui.column().classes(
            "w-full glass-panel p-6 md:p-8 rounded-2xl border border-[rgba(224,107,58,0.35)] gap-3"
        ):
            with ui.row().classes("items-center gap-3"):
                ui.html('<i class="fa-solid fa-route text-[#e06b3a] text-3xl"></i>')
                with ui.column().classes("gap-0"):
                    ui.html('<h2 class="text-xl md:text-2xl font-bold gradient-title m-0">Topic 6: Data Switching & Routing</h2>')
                    ui.label(
                        "Packet vs Circuit Switching, Store-and-Forward, 4 Nodal Delays, "
                        "Traffic Intensity, Pipelining, Control vs Data Plane, and Longest Prefix Match (LPM)."
                    ).classes("text-xs md:text-sm text-[#b5b0a4]")

        # =========================================================================
        # SECTION 1: Packet Switching vs Circuit Switching
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-shuffle text-blue-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">1. Packet Switching vs Circuit Switching</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs leading-relaxed"):
                # Packet Switching Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(224,107,58,0.3)] gap-2"):
                    ui.label("Packet Switching").classes("font-bold text-[#e06b3a] text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1.5 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Packetization:</strong> Application data streams are segmented into discrete packets ($L$ bits).</li>
                        <li><strong class="text-stone-200">Statistical Multiplexing:</strong> Link capacity is allocated dynamically on demand, accommodating far more concurrent users than circuit capacity would suggest.</li>
                        <li><strong class="text-stone-200">Efficiency:</strong> Exceptional resource utilization for bursty network traffic.</li>
                        <li><strong class="text-amber-300">Trade-off:</strong> Susceptible to variable queuing delay and packet loss when burst rates exceed buffer capacity.</li>
                    </ul>
                    """)

                # Circuit Switching Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(79,142,201,0.3)] gap-2"):
                    ui.label("Circuit Switching").classes("font-bold text-blue-400 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1.5 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Dedicated Resources:</strong> Dedicated end-to-end transmission resources are reserved along the route prior to data transfer (Call Setup phase).</li>
                        <li><strong class="text-stone-200">Multiplexing:</strong> Channel partitioning via <strong>FDM</strong> (Frequency Division) or <strong>TDM</strong> (Time Division).</li>
                        <li><strong class="text-stone-200">Guaranteed Performance:</strong> Deterministic transmission throughput with zero queuing delay ($d_{\\text{queue}} = 0$).</li>
                        <li><strong class="text-red-400">Trade-off:</strong> Inefficient resource utilization when circuits sit idle, plus non-zero call setup signaling latency.</li>
                    </ul>
                    """)

        # =========================================================================
        # SECTION 2: The 4 Nodal Delays with LaTeX Formulas
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-stopwatch text-amber-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">2. The 4 Components of Nodal Delay</h3>')

            with ui.column().classes("w-full p-4 rounded-xl bg-[#141413] border border-[rgba(224,107,58,0.35)] gap-2"):
                ui.html("""
                <div class="formula-box text-sm">
                    $$d_{\\text{nodal}} = d_{\\text{proc}} + d_{\\text{queue}} + d_{\\text{trans}} + d_{\\text{prop}}$$
                </div>
                """)

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs"):
                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-1"):
                    ui.label("1. Processing Delay (d_proc)").classes("font-bold text-blue-400")
                    ui.label("Time to inspect packet headers, verify bit-level checksums, and look up output interfaces in the forwarding table. Typically microseconds (us).").classes("text-[#b5b0a4]")

                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-1"):
                    ui.label("2. Queuing Delay (d_queue)").classes("font-bold text-amber-400")
                    ui.label("Time a packet waits in router output buffers for the transmission link to become available. Driven by traffic intensity I = (L * a) / R.").classes("text-[#b5b0a4]")

                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-1"):
                    ui.label("3. Transmission Delay (d_trans)").classes("font-bold text-[#e06b3a]")
                    ui.html("<div>Time required to push all packet bits onto the link: $$d_{\\text{trans}} = \\frac{L}{R}$$ where $L$: packet size (bits), $R$: transmission link bandwidth (bps).</div>").classes("text-[#b5b0a4]")

                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-1"):
                    ui.label("4. Propagation Delay (d_prop)").classes("font-bold text-emerald-400")
                    ui.html("<div>Time for a bit to physically traverse the link: $$d_{\\text{prop}} = \\frac{l}{u}$$ where $l$: physical length (m), $u$: signal speed through the physical medium.</div>").classes("text-[#b5b0a4]")

        # =========================================================================
        # SECTION 3: Store-and-Forward & Multi-packet Pipelining
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-bars-progress text-emerald-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">3. Store-and-Forward & Transmission Pipelining</h3>')

            ui.label(
                "Under Store-and-Forward packet switching, an intermediate node must buffer the entire incoming packet "
                "before transmitting the first bit onto the outbound link."
            ).classes("text-xs md:text-sm text-[#b5b0a4]")

            with ui.column().classes("w-full p-4 rounded-xl bg-[#141413] border border-[rgba(16,185,129,0.3)] font-mono text-xs text-[#fed7aa] space-y-2"):
                ui.html("""
                <div class="text-stone-300 font-bold">// Transmission time for 1 packet across N identical links:</div>
                <div class="text-emerald-400 text-sm">$$T_1 = N \\cdot \\left(\\frac{L}{R}\\right) + \\sum_{i=1}^{N} d_{\\text{prop},i}$$</div>
                <div class="text-stone-300 font-bold mt-2">// Total transmission time for P packets with Store-and-Forward pipelining:</div>
                <div class="text-emerald-400 text-sm">$$T_{\\text{total}} = (N + P - 1) \\cdot \\left(\\frac{L}{R}\\right) + \\sum_{i=1}^{N} d_{\\text{prop},i} + (N-1) \\cdot d_{\\text{proc}}$$</div>
                """)

        # =========================================================================
        # SECTION 4: Routing vs Forwarding & LPM Rule
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-table-list text-amber-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">4. Routing (Control Plane) vs Forwarding (Data Plane) & Longest Prefix Match</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs"):
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(79,142,201,0.3)] gap-2"):
                    ui.label("Routing (Control Plane) vs Forwarding (Data Plane)").classes("font-bold text-blue-300 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1.5 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Routing (Control Plane):</strong> Network-wide coordinated process. Routing protocols (OSPF, BGP) execute distributed algorithms to compute end-to-end paths and populate the <strong>RIB</strong>.</li>
                        <li><strong class="text-stone-200">Forwarding (Data Plane):</strong> Local per-router hardware operation. Transfers incoming packets from an input interface to the appropriate output interface in nanoseconds using the <strong>FIB</strong> table in hardware ASICs.</li>
                    </ul>
                    """)

                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(245,158,11,0.3)] gap-2"):
                    ui.label("Longest Prefix Match (LPM) Rule").classes("font-bold text-amber-300 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1.5 text-[#b5b0a4]">
                        <li>The router examines the incoming packet's destination IP against all entries in its forwarding table.</li>
                        <li>When destination IP addresses match multiple subnet prefixes, the forwarding engine <strong>ALWAYS</strong> chooses the entry with the longest prefix match (most specific prefix, e.g., /25 takes precedence over /24 and /16).</li>
                    </ul>
                    """)
