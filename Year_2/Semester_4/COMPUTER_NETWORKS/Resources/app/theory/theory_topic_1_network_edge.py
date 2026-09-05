"""Topic 1: Network Edge theory renderer.

Covers End Systems (Hosts), Network as a Service (NaaS), Tier 1/2/3 ISP hierarchy,
Client-Server vs Peer-to-Peer models, TCP vs UDP edge services, and Access Network provisioning.
"""

from nicegui import ui


def renderTopic1NetworkEdge() -> None:
    """Renders the comprehensive theory module for Topic 1: Network Edge."""
    with ui.column().classes("w-full gap-6 text-[#f4f1ea] latex-target"):
        # Header Banner
        with ui.column().classes(
            "w-full glass-panel p-6 md:p-8 rounded-2xl border border-[rgba(224,107,58,0.35)] gap-3"
        ):
            with ui.row().classes("items-center gap-3"):
                ui.html('<i class="fa-solid fa-laptop-code text-[#e06b3a] text-3xl"></i>')
                with ui.column().classes("gap-0"):
                    ui.html('<h2 class="text-xl md:text-2xl font-bold gradient-title m-0">Topic 1: Network Edge</h2>')
                    ui.label(
                        "End Systems (Hosts), Communication Paradigms (Client-Server & P2P), "
                        "Network as a Service (NaaS), ISP Hierarchy, and Access Networks."
                    ).classes("text-xs md:text-sm text-[#b5b0a4]")

        # =========================================================================
        # SECTION 1: End Systems & Architecture
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-server text-blue-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">1. End Systems (Hosts) & Role in Network Architecture</h3>')

            ui.label(
                "End systems (hosts) are devices residing at the network edge that execute user applications "
                "(computers, smartphones, servers, IoT sensors, network cameras). They are termed 'end' systems because they form "
                "strictly the origin or destination of communication — in contrast to intermediate nodes (routers, switches) "
                "that comprise the network core and simply forward packets."
            ).classes("text-xs md:text-sm text-[#b5b0a4] leading-relaxed")

            with ui.column().classes("w-full p-4 rounded-xl bg-[#141413] border border-[rgba(255,255,255,0.06)] font-mono text-xs text-[#fed7aa]"):
                ui.html(r"""<pre class="m-0 overflow-x-auto">
  Network Edge
  ─────────────────────────────────────────────────────────────────────────────
  [Laptop]       [Smartphone]       [Smart TV]       [IoT Sensors / Camera]
      \               |                  |                   /
       \              |                  |                  /
        ──────────────[Access Network]───────────────────────────────
                                       |
                             [Network Core]
                             (Routers, Switches, IXPs)
                                       |
                             [Other End Systems / Servers]
</pre>""")

            # NaaS & ISP Hierarchy
            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs"):
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(79,142,201,0.25)] gap-2"):
                    ui.label("Network as a Service (NaaS)").classes("font-bold text-blue-300 text-sm")
                    ui.label(
                        "• Abstract Pipe: The network provides applications with an abstract transmission channel "
                        "without requiring knowledge of physical routers or underlying topology.\n"
                        "• NaaS (Cloud Model): Cloud paradigm where enterprises lease network infrastructure, firewalling, and bandwidth "
                        "from providers rather than managing proprietary hardware."
                    ).classes("text-[#b5b0a4] whitespace-pre-line")

                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(245,158,11,0.25)] gap-2"):
                    ui.label("ISP Hierarchy & Peering").classes("font-bold text-amber-300 text-sm")
                    ui.label(
                        "• Tier-1 ISPs: Global backbone networks (AT&T, NTT, Lumen). Interconnect with one another via settlement-free peering (no transit fees).\n"
                        "• Tier-2 ISPs: Regional and national providers (e.g. Vodafone, Comcast). Purchase transit from Tier-1 backbones.\n"
                        "• Tier-3 / Local ISPs: Last-mile access providers connecting residential homes and commercial premises directly to the Internet."
                    ).classes("text-[#b5b0a4] whitespace-pre-line")

        # =========================================================================
        # SECTION 2: Communication Paradigms
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-arrows-split-up-and-left text-[#e06b3a] text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">2. Communication Models: Client-Server vs Peer-to-Peer (P2P)</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs leading-relaxed"):
                # Client-Server Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(79,142,201,0.3)] gap-2"):
                    with ui.row().classes("items-center gap-2"):
                        ui.html('<i class="fa-solid fa-desktop text-blue-400"></i>')
                        ui.label("Client-Server Model").classes("font-bold text-blue-300 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Server:</strong> Always-on host with a permanent (static) well-known IP address. Serves multiple concurrent clients.</li>
                        <li><strong class="text-stone-200">Client:</strong> Initiates communication, uses dynamic IP addressing, does not communicate directly with peer clients.</li>
                        <li><strong class="text-stone-200">Scalability:</strong> Constrained by server uplink bandwidth and computing power. Demands server clusters, load balancers, and CDNs.</li>
                        <li><strong class="text-stone-200">Examples:</strong> Web (HTTP/HTTPS), Email (SMTP/IMAP), DNS, Database servers.</li>
                    </ul>
                    """)

                # Peer-to-Peer Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(224,107,58,0.3)] gap-2"):
                    with ui.row().classes("items-center gap-2"):
                        ui.html('<i class="fa-solid fa-share-nodes text-[#e06b3a]"></i>')
                        ui.label("Peer-to-Peer (P2P) Model").classes("font-bold text-[#e06b3a] text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Symmetric Peers:</strong> Each node operates simultaneously as both a client and a server (concurrent downloading and uploading).</li>
                        <li><strong class="text-stone-200">Self-scalability:</strong> Each incoming peer contributes fresh upload capacity to the overall network.</li>
                        <li><strong class="text-stone-200">Dynamic Churn:</strong> Peers connect and disconnect arbitrarily, changing their IP addresses continuously.</li>
                        <li><strong class="text-stone-200">Examples:</strong> BitTorrent, Blockchain networks (Bitcoin, Ethereum), InterPlanetary File System (IPFS).</li>
                    </ul>
                    """)

            # Hybrid Architecture Note
            with ui.column().classes("w-full p-4 rounded-xl bg-[#201f1d] border border-[rgba(245,158,11,0.25)] gap-1 text-xs"):
                ui.label("Hybrid Architectures (Hybrid P2P / Client-Server)").classes("font-bold text-amber-300")
                ui.label(
                    "Many contemporary systems combine both paradigms: they utilize a central server for authentication and "
                    "peer discovery (Directory Service), followed by direct P2P connections for high-throughput media and data exchange "
                    "(e.g., early Skype, WebRTC protocols for real-time peer-to-peer audio/video streaming)."
                ).classes("text-[#b5b0a4]")

        # =========================================================================
        # SECTION 3: Edge Services (TCP vs UDP)
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-bolt text-emerald-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">3. Transport Layer Edge Services (TCP vs UDP)</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs"):
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(16,185,129,0.3)] gap-2"):
                    ui.label("TCP (Connection-Oriented, Reliable)").classes("font-bold text-emerald-400 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Connection Setup:</strong> 3-Way Handshake (SYN, SYN-ACK, ACK).</li>
                        <li><strong class="text-stone-200">Reliability:</strong> Guaranteed in-order, loss-free delivery (Sequence numbers, ACKs, Retransmissions).</li>
                        <li><strong class="text-stone-200">Flow Control:</strong> Ensures sender does not overwhelm receiver buffers (Receive Window rwnd).</li>
                        <li><strong class="text-stone-200">Congestion Control:</strong> Regulates transmission rate based on perceived network congestion (cwnd).</li>
                    </ul>
                    """)

                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(239,68,68,0.3)] gap-2"):
                    ui.label("UDP (Connectionless, Best-Effort)").classes("font-bold text-red-400 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Connectionless:</strong> Immediate transmission without preliminary handshake (zero connection setup delay).</li>
                        <li><strong class="text-stone-200">Best-Effort Delivery:</strong> No delivery guarantees, retransmissions, duplicate suppression, or ordered arrival.</li>
                        <li><strong class="text-stone-200">Lightweight Header:</strong> Fixed 8-byte header overhead (versus minimum 20 bytes in TCP).</li>
                        <li><strong class="text-stone-200">Ideal for:</strong> DNS queries, live media streaming, real-time gaming, VoIP (where low latency takes precedence over absolute reliability).</li>
                    </ul>
                    """)

        # =========================================================================
        # SECTION 4: Access Networks Breakdown
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-tower-broadcast text-amber-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">4. Last-Mile Access Networks</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-3 gap-3 w-full text-xs"):
                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-1.5"):
                    ui.label("Residential Access (DSL / HFC / FTTH)").classes("font-bold text-amber-300")
                    ui.label(
                        "• DSL: Copper telephone lines, central office DSLAM, asymmetric (ADSL) or VDSL. Strictly distance-limited (< 3-5 km).\n"
                        "• HFC (Cable): Fiber optic to neighborhood node, coaxial drop to premises (DOCSIS). Shared broadcast medium.\n"
                        "• FTTH: Optical fiber running directly to the home (PON architecture with passive optical splitters)."
                    ).classes("text-[#b5b0a4] leading-relaxed")

                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-1.5"):
                    ui.label("Enterprise Access").classes("font-bold text-blue-300")
                    ui.label(
                        "• Ethernet (IEEE 802.3): Twisted-pair copper cabling (UTP Cat6/6a) offering 1 Gbps, 10 Gbps, 100 Gbps speeds.\n"
                        "• Wi-Fi (IEEE 802.11): Wireless local access via Access Points (APs) using the CSMA/CA protocol."
                    ).classes("text-[#b5b0a4] leading-relaxed")

                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-1.5"):
                    ui.label("Mobile & Satellite Access").classes("font-bold text-emerald-300")
                    ui.label(
                        "• 4G LTE / 5G NR: Cellular connectivity to base stations (gNodeB). 5G provides eMBB, URLLC, and Network Slicing.\n"
                        "• LEO Satellites (Starlink): Low Earth Orbit (500-1500 km), achieving low propagation delay (~15-25 ms) for remote areas."
                    ).classes("text-[#b5b0a4] leading-relaxed")
