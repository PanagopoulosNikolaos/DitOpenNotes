"""Topic 4: Access Technologies theory renderer.

Covers Home Access (DSL/ADSL/VDSL, Cable HFC DOCSIS, FTTH PON/OLT/ONT),
Enterprise Access (Ethernet 802.3, Wi-Fi 802.11 a/b/g/n/ac/ax/be, CSMA/CA, RTS/CTS),
Mobile/Cellular (4G LTE, 5G NR eMBB/URLLC/mMTC, Network Slicing), and Satellite Networks.
"""

from nicegui import ui


def renderTopic4AccessTechnologies() -> None:
    """Renders the comprehensive theory module for Topic 4: Access Technologies."""
    with ui.column().classes("w-full gap-6 text-[#f4f1ea] latex-target"):
        # Header Banner
        with ui.column().classes(
            "w-full glass-panel p-6 md:p-8 rounded-2xl border border-[rgba(224,107,58,0.35)] gap-3"
        ):
            with ui.row().classes("items-center gap-3"):
                ui.html('<i class="fa-solid fa-wifi text-[#e06b3a] text-3xl"></i>')
                with ui.column().classes("gap-0"):
                    ui.html('<h2 class="text-xl md:text-2xl font-bold gradient-title m-0">Topic 4: Access Technologies</h2>')
                    ui.label(
                        "Residential Access (DSL, HFC Cable, FTTH PON), Enterprise Access (Ethernet, Wi-Fi 802.11), "
                        "Cellular Mobile (4G LTE, 5G NR, Network Slicing), and Satellite Networks."
                    ).classes("text-xs md:text-sm text-[#b5b0a4]")

        # =========================================================================
        # SECTION 1: Residential Access Technologies
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-house-signal text-amber-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">1. Residential Access Technologies (DSL, HFC Cable, FTTH)</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-3 gap-4 w-full text-xs"):
                # DSL Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(224,107,58,0.3)] gap-2"):
                    ui.label("DSL / VDSL (Telephone Copper Pair)").classes("font-bold text-[#e06b3a] text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1.5 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Infrastructure:</strong> Legacy twisted-pair copper wiring (traditional telephone line).</li>
                        <li><strong class="text-stone-200">Modulation:</strong> DMT (Discrete Multi-Tone) across distinct frequency bands (Voice: 0-4 kHz, Upstream: 25-138 kHz, Downstream: 138-1104 kHz).</li>
                        <li><strong class="text-stone-200">Central Office:</strong> <strong>DSLAM</strong> (DSL Access Multiplexer) located at the ISP Central Office.</li>
                        <li><strong class="text-amber-300">Limitation:</strong> Dedicated physical link, but bandwidth degrades exponentially with loop length (&gt; 3-5 km).</li>
                    </ul>
                    """)

                # HFC Cable Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(245,158,11,0.3)] gap-2"):
                    ui.label("HFC Cable (DOCSIS)").classes("font-bold text-amber-400 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1.5 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Infrastructure:</strong> Hybrid fiber-coaxial network: Optical fiber runs to neighborhood Fiber Nodes, coaxial cabling to homes.</li>
                        <li><strong class="text-stone-200">Protocol:</strong> <strong>DOCSIS</strong> (Data Over Cable Service Interface Specification).</li>
                        <li><strong class="text-stone-200">Central Headend:</strong> <strong>CMTS</strong> (Cable Modem Termination System) at the cable provider headend.</li>
                        <li><strong class="text-red-400">Limitation:</strong> Shared transmission medium — simultaneous active traffic from neighboring subscribers contends for aggregate capacity.</li>
                    </ul>
                    """)

                # FTTH Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(16,185,129,0.3)] gap-2"):
                    ui.label("FTTH (Fiber to the Home - PON)").classes("font-bold text-emerald-400 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1.5 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Infrastructure:</strong> 100% optical fiber from the distribution exchange directly to the subscriber's outlet.</li>
                        <li><strong class="text-stone-200">Architecture:</strong> <strong>PON</strong> (Passive Optical Network). Zero powered active equipment along the street run.</li>
                        <li><strong class="text-stone-200">Components:</strong> <strong>OLT</strong> (Optical Line Terminal) at the central office, passive optical splitters (1:32 / 1:64), and an <strong>ONT</strong> (Optical Network Terminal) at home.</li>
                        <li><strong class="text-emerald-300">Advantage:</strong> Symmetrical gigabit speeds (1-10 Gbps), minimal distance attenuation, immune to electromagnetic interference.</li>
                    </ul>
                    """)

        # =========================================================================
        # SECTION 2: Enterprise & Wireless Access (Ethernet & Wi-Fi)
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-building text-blue-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">2. Enterprise & Wireless Access (Ethernet & Wi-Fi)</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs"):
                # Ethernet Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(79,142,201,0.3)] gap-2"):
                    ui.label("Wired Ethernet (IEEE 802.3)").classes("font-bold text-blue-300 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1.5 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Topology:</strong> Star topology centered on high-speed Link Layer Switches.</li>
                        <li><strong class="text-stone-200">Cabling:</strong> Twisted pair UTP/STP (Cat5e: 1 Gbps, Cat6/6a: 10 Gbps) up to 100 meters per segment.</li>
                        <li><strong class="text-stone-200">Full-Duplex:</strong> Dedicated transmit (Tx) and receive (Rx) wire pairs $\\rightarrow$ Zero collisions in modern switched fabrics.</li>
                        <li><strong class="text-stone-200">CSMA/CD:</strong> Historically used on shared bus/repeater hubs ($L_{\\text{min}} \\ge 2 \\cdot t_{\\text{prop}} \\cdot R$).</li>
                    </ul>
                    """)

                # Wi-Fi Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(245,158,11,0.3)] gap-2"):
                    ui.label("Wireless Wi-Fi (IEEE 802.11)").classes("font-bold text-amber-300 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1.5 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Frequencies:</strong> 2.4 GHz (longer range, high interference), 5 GHz (higher speed, shorter range), 6 GHz (Wi-Fi 6E/7).</li>
                        <li><strong class="text-stone-200">CSMA/CA Protocol:</strong> Collision Avoidance with random exponential backoff timers before transmission.</li>
                        <li><strong class="text-stone-200">Hidden Terminal Problem:</strong> Two nodes out of range of each other transmitting simultaneously to a central Access Point (AP).</li>
                        <li><strong class="text-amber-300">Solution:</strong> Channel reservation handshake via <strong>RTS / CTS</strong> (Request to Send / Clear to Send).</li>
                    </ul>
                    """)

        # =========================================================================
        # SECTION 3: Mobile & 5G Cellular Networks
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-tower-cell text-emerald-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">3. Cellular Mobile Networks & 5G NR (New Radio)</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-3 gap-3 w-full text-xs"):
                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(16,185,129,0.25)] gap-1.5"):
                    ui.label("eMBB (Enhanced Mobile Broadband)").classes("font-bold text-emerald-400")
                    ui.label(
                        "• Massive data transfer rates (up to 10-20 Gbps peak downlink).\n"
                        "• Millimeter-wave spectrum (mmWave) and massive MIMO (Multiple Input Multiple Output).\n"
                        "• Targets 4K/8K video streaming, immersive AR/VR, and dense urban environments."
                    ).classes("text-[#b5b0a4] leading-relaxed")

                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(239,68,68,0.25)] gap-1.5"):
                    ui.label("URLLC (Ultra-Reliable Low-Latency)").classes("font-bold text-red-400")
                    ui.label(
                        "• Sub-millisecond radio latency (< 1 ms over the air).\n"
                        "• 99.999% (five-nines) transmission reliability for critical services.\n"
                        "• Targets autonomous vehicles, telesurgery, and Industry 4.0 factory automation."
                    ).classes("text-[#b5b0a4] leading-relaxed")

                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(79,142,201,0.25)] gap-1.5"):
                    ui.label("mMTC & Network Slicing").classes("font-bold text-blue-400")
                    ui.label(
                        "• mMTC: Massive Machine-Type Communications supporting up to 1,000,000 IoT nodes per km².\n"
                        "• Network Slicing: Logical partitioning of the physical infrastructure into isolated end-to-end virtual networks tailored to distinct SLA profiles."
                    ).classes("text-[#b5b0a4] leading-relaxed")
