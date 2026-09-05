"""Comprehensive Exam Preparation Guide.

Synthesizes all essential networking theory, mathematical formulas, fast mental calculation tricks,
decision matrices, routing algorithms, Cisco IOS configurations, and common exam pitfalls.
"""

from nicegui import ui


def renderTheoryExamFullPrep() -> None:
    """Renders the master exam preparation guide with synthesized formulas and matrices."""
    with ui.column().classes("w-full gap-6 text-[#f4f1ea] latex-target"):
        # Header Banner
        with ui.column().classes(
            "w-full glass-panel p-6 md:p-8 rounded-2xl border border-[rgba(224,107,58,0.4)] gap-3"
        ):
            with ui.row().classes("items-center gap-3"):
                ui.html('<i class="fa-solid fa-graduation-cap text-[#e06b3a] text-3xl md:text-4xl"></i>')
                with ui.column().classes("gap-0"):
                    ui.html(
                        '<h2 class="text-xl md:text-2xl font-black gradient-title m-0">'
                        "Comprehensive Exam Preparation Guide (10/10 Exam Cheat Sheet)"
                        "</h2>"
                    )
                    ui.label(
                        "Master formula sheets with LaTeX math support, decision matrices, step-by-step algorithms, "
                        "Cisco IOS CLI commands, and critical exam pitfalls for top performance."
                    ).classes("text-xs md:text-sm text-[#b5b0a4]")

        # =========================================================================
        # SECTION 1: Fundamental Concepts, Architecture & Encapsulation
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-5"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-layer-group text-amber-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">1. Fundamental Concepts, Architecture & Encapsulation</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs"):
                # Transmission Modes Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(224,107,58,0.25)] gap-2"):
                    ui.label("Data Transmission Modes").classes("font-bold text-[#e06b3a] text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Simplex:</strong> Data transmits exclusively in 1 direction (e.g., Broadcast Television, FM Radio).</li>
                        <li><strong class="text-stone-200">Half-Duplex:</strong> Data transmits in both directions, but <em>only one direction at a time</em> (e.g., Walkie-Talkies).</li>
                        <li><strong class="text-stone-200">Full-Duplex:</strong> Data transmits in both directions <em>simultaneously</em> (e.g., Telephony, Switched Full-Duplex Ethernet).</li>
                    </ul>
                    <div class="mt-2 p-2 rounded bg-[#141413] text-amber-300 font-semibold">
                        Pitfall Warning: Multiplexing (FDM/TDM) is NOT a transmission mode; it is a signal sharing and channelization technique!
                    </div>
                    """)

                # OSI Layer & Devices Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(79,142,201,0.25)] gap-2"):
                    ui.label("OSI Model, Layers & Devices").classes("font-bold text-blue-400 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Layer 1 (Physical):</strong> Repeater, Hub. Transmit physical bits without inspecting addresses.</li>
                        <li><strong class="text-stone-200">Layer 2 (Data Link):</strong> Bridge, Switch. PDU: <em>Frame</em>. Hardware MAC addressing.</li>
                        <li><strong class="text-stone-200">Layer 3 (Network):</strong> Router. PDU: <em>Packet / Datagram</em>. Logical IP addressing.</li>
                        <li><strong class="text-stone-200">Layer 4 (Transport):</strong> TCP / UDP, Ports. PDU: <em>Segment</em>.</li>
                        <li><strong class="text-stone-200">Peer Processes:</strong> Protocol entities operating at the <em>same layer</em> across distinct communicating nodes.</li>
                    </ul>
                    """)

                # Encapsulation & Address Behavior Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(16,185,129,0.25)] gap-2"):
                    ui.label("Data Encapsulation & Address Mutability").classes("font-bold text-emerald-400 text-sm")
                    ui.html("""
                    <div class="formula-box text-xs mb-2">
                        $$\\text{Message} \\xrightarrow{\\text{L4}} \\text{Segment} \\xrightarrow{\\text{L3}} \\text{Packet} \\xrightarrow{\\text{L2}} \\text{Frame} \\xrightarrow{\\text{L1}} \\text{Bits}$$
                    </div>
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">IP Address (Layer 3):</strong> Remains <em>invariant</em> end-to-end between communicating hosts (unless translated by NAT).</li>
                        <li><strong class="text-stone-200">MAC Address (Layer 2):</strong> <em>Rewritten at each hop</em> (each router replaces the Source MAC with its own and sets Destination MAC to the next hop).</li>
                    </ul>
                    """)

                # Control Plane vs Data Plane & Domains Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(245,158,11,0.25)] gap-2"):
                    ui.label("Control Plane vs Data Plane & Domains").classes("font-bold text-amber-400 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Control Plane (Software):</strong> Routing path computation (OSPF, RIP, BGP) $\\rightarrow$ RIB routing table.</li>
                        <li><strong class="text-stone-200">Data Plane (Hardware/ASIC):</strong> Nanosecond packet forwarding $\\rightarrow$ FIB forwarding table.</li>
                        <li><strong class="text-stone-200">Collision Domain:</strong> Each Switch port forms a separate collision domain. Hub ports share one common domain.</li>
                        <li><strong class="text-stone-200">Broadcast Domain:</strong> Each Router interface delimits a distinct broadcast domain.</li>
                    </ul>
                    """)

        # =========================================================================
        # SECTION 2: Master Formula Sheet & Delay Calculations
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-5"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-square-root-variable text-amber-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">2. Master Formula Sheet: Delays & Channel Capacity</h3>')

            # Master Nodal Delay Formula Box
            with ui.column().classes("w-full p-4 rounded-xl bg-[#141413] border border-[rgba(224,107,58,0.35)] gap-2"):
                ui.label("Nodal Delay").classes("font-bold text-[#e06b3a] text-sm")
                ui.html("""
                <div class="formula-box text-sm">
                    $$d_{\\text{nodal}} = d_{\\text{proc}} + d_{\\text{queue}} + d_{\\text{trans}} + d_{\\text{prop}}$$
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-3 mt-2 text-xs text-[#b5b0a4]">
                    <div>
                        <strong class="text-stone-200">Transmission Delay:</strong> $$d_{\\text{trans}} = \\frac{L}{R}$$
                        <br><span class="text-[#78756d]">L: packet size (bits), R: transmission rate (bps). Depends ONLY on packet size and bandwidth.</span>
                    </div>
                    <div>
                        <strong class="text-stone-200">Propagation Delay:</strong> $$d_{\\text{prop}} = \\frac{l}{u}$$
                        <br><span class="text-[#78756d]">l: link distance (m), u: signal speed ($2\\times 10^8\\text{ m/s}$ in copper/fiber, $3\\times 10^8\\text{ m/s}$ in air).</span>
                    </div>
                </div>
                """)

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs"):
                # Multi-hop & Pipelining Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(16,185,129,0.3)] gap-2"):
                    ui.label("Store-and-Forward & Multi-Packet Pipelining").classes("font-bold text-emerald-400 text-sm")
                    ui.html("""
                    <div class="formula-box text-xs mb-2">
                        $$T_{\\text{total}} = (N + P - 1) \\cdot \\frac{L}{R} + N \\cdot \\frac{l}{u} + (N-1) \\cdot d_{\\text{proc}}$$
                    </div>
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">N:</strong> Number of link hops — <em>not router count!</em> (e.g., $A \\rightarrow R_1 \\rightarrow R_2 \\rightarrow B \\Rightarrow N=3$ hops).</li>
                        <li><strong class="text-stone-200">P:</strong> Number of pipelined packets.</li>
                        <li><strong class="text-stone-200">Single Packet:</strong> $$T_1 = N \\cdot \\left(\\frac{L}{R} + \\frac{l}{u}\\right)$$</li>
                    </ul>
                    """)

                # BDP & AM Exam Formula Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(245,158,11,0.3)] gap-2"):
                    ui.label("Bandwidth-Delay Product (BDP) & Student ID Parameter Mapping").classes("font-bold text-amber-400 text-sm")
                    ui.html("""
                    <div class="formula-box text-xs mb-2">
                        $$\\text{BDP (Max Bits)} = R \\times d_{\\text{prop}} = (8000 \\cdot N) \\times (d \\cdot 10^{-3}) = 8 \\cdot N \\cdot d \\text{ bits}$$
                    </div>
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">N (Bandwidth):</strong> Student ID in KB/s $\\rightarrow N \\times 1000 \\times 8\\text{ bps}$.</li>
                        <li><strong class="text-stone-200">d (Delay):</strong> Last digit of Student ID in ms (if $d=0 \\Rightarrow 5\\text{ ms}$ or $6\\text{ ms}$ as instructed).</li>
                        <li><strong class="text-stone-200">Sliding Window Condition:</strong> $$W \\ge R \\times \\text{RTT}$$ required for 100% channel utilization.</li>
                    </ul>
                    """)

                # Multi-hop RTT Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(79,142,201,0.3)] gap-2"):
                    ui.label("Multi-Hop RTT Computation").classes("font-bold text-blue-400 text-sm")
                    ui.html("""
                    <div class="formula-box text-xs mb-2">
                        $$\\text{RTT}_{A-C} = 2 \\cdot (d_{\\text{trans1}} + d_{\\text{prop1}} + d_{\\text{trans2}} + d_{\\text{prop2}}) + 3 \\cdot d_{\\text{proc}}$$
                    </div>
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li>Route: $A \\xrightarrow{\\text{proc B}} B \\xrightarrow{\\text{proc C}} C \\xrightarrow{\\text{proc B}} B \\rightarrow A$.</li>
                        <li>Includes 3 processing delays: at $B$ (forward), at $C$ (terminal processing/turnaround), at $B$ (reverse).</li>
                    </ul>
                    """)

                # Traffic Intensity & Bottleneck Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(239,68,68,0.3)] gap-2"):
                    ui.label("Traffic Intensity & Bottleneck Throughput").classes("font-bold text-red-400 text-sm")
                    ui.html("""
                    <div class="formula-box text-xs mb-2">
                        $$I = \\frac{L \\cdot a}{R}, \\quad \\text{Throughput} = \\min(R_1, R_2, \\dots, R_N)$$
                    </div>
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">I ~ 0:</strong> Minimal queuing delay ($d_{\\text{queue}} \\approx 0$).</li>
                        <li><strong class="text-stone-200">I $\\rightarrow$ 1:</strong> Exponential growth in queuing delay.</li>
                        <li><strong class="text-stone-200">I > 1:</strong> Infinite queue growth; packet loss is guaranteed.</li>
                    </ul>
                    """)

        # =========================================================================
        # SECTION 3: Subnetting, CIDR & Longest Prefix Match (LPM)
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-5"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-network-wired text-emerald-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">3. Subnetting, CIDR & Longest Prefix Match (LPM)</h3>')

            # CIDR Subnetting Reference Table
            with ui.column().classes("w-full p-4 rounded-xl bg-[#201f1d] border border-[rgba(255,255,255,0.08)] gap-3"):
                ui.label("Subnet Mask & Wildcard Mask Reference Table (Cisco OSPF)").classes("font-bold text-amber-300 text-sm")
                ui.html("""
                <div class="overflow-x-auto">
                    <table class="w-full text-left text-xs border-collapse">
                        <thead>
                            <tr class="border-b border-[rgba(255,255,255,0.1)] text-[#e06b3a]">
                                <th class="py-2 px-3">CIDR</th>
                                <th class="py-2 px-3">Subnet Mask</th>
                                <th class="py-2 px-3">Wildcard Mask</th>
                                <th class="py-2 px-3">Block Size ($2^{32-n}$)</th>
                                <th class="py-2 px-3">Usable Hosts ($2^{32-n}-2$)</th>
                                <th class="py-2 px-3">Typical Application</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-[rgba(255,255,255,0.05)] text-[#b5b0a4]">
                            <tr><td class="py-1.5 px-3 font-mono text-stone-200">/24</td><td class="py-1.5 px-3 font-mono">255.255.255.0</td><td class="py-1.5 px-3 font-mono text-amber-300">0.0.0.255</td><td class="py-1.5 px-3">256</td><td class="py-1.5 px-3 text-emerald-400 font-bold">254</td><td class="py-1.5 px-3">Standard LAN</td></tr>
                            <tr><td class="py-1.5 px-3 font-mono text-stone-200">/26</td><td class="py-1.5 px-3 font-mono">255.255.255.192</td><td class="py-1.5 px-3 font-mono text-amber-300">0.0.0.63</td><td class="py-1.5 px-3">64</td><td class="py-1.5 px-3 text-emerald-400 font-bold">62</td><td class="py-1.5 px-3">Department / Floor subnet</td></tr>
                            <tr><td class="py-1.5 px-3 font-mono text-stone-200">/28</td><td class="py-1.5 px-3 font-mono">255.255.255.240</td><td class="py-1.5 px-3 font-mono text-amber-300">0.0.0.15</td><td class="py-1.5 px-3">16</td><td class="py-1.5 px-3 text-emerald-400 font-bold">14</td><td class="py-1.5 px-3">Small server cluster</td></tr>
                            <tr><td class="py-1.5 px-3 font-mono text-stone-200">/29</td><td class="py-1.5 px-3 font-mono">255.255.255.248</td><td class="py-1.5 px-3 font-mono text-amber-300">0.0.0.7</td><td class="py-1.5 px-3">8</td><td class="py-1.5 px-3 text-emerald-400 font-bold">6</td><td class="py-1.5 px-3">DMZ / Switch interconnect</td></tr>
                            <tr><td class="py-1.5 px-3 font-mono text-stone-200">/30</td><td class="py-1.5 px-3 font-mono">255.255.255.252</td><td class="py-1.5 px-3 font-mono text-amber-300">0.0.0.3</td><td class="py-1.5 px-3">4</td><td class="py-1.5 px-3 text-emerald-400 font-bold">2</td><td class="py-1.5 px-3">Point-to-Point Router Link</td></tr>
                        </tbody>
                    </table>
                </div>
                """)

            # LPM Step-by-Step Box
            with ui.column().classes("w-full p-4 rounded-xl bg-[#201f1d] border border-[rgba(16,185,129,0.3)] gap-2 text-xs"):
                ui.label("Longest Prefix Match (LPM) Rule - Forwarding Decisions").classes("font-bold text-emerald-400 text-sm")
                ui.label("The router selects the table entry with the LONGEST prefix match (most '1' bits in subnet mask).").classes("text-[#b5b0a4]")
                ui.html("""
                <div class="p-3 rounded bg-[#141413] border border-[rgba(255,255,255,0.06)] font-mono space-y-1">
                    <div>1. <span class="text-blue-300">10.15.0.0/16</span> $\\rightarrow$ Eth0</div>
                    <div>2. <span class="text-amber-300">10.15.20.0/24</span> $\\rightarrow$ Eth1</div>
                    <div>3. <span class="text-emerald-300">10.15.20.128/25</span> $\\rightarrow$ Eth2</div>
                    <div>4. <span class="text-stone-400">0.0.0.0/0 (Default)</span> $\\rightarrow$ Eth3</div>
                </div>
                <ul class="m-0 pl-4 mt-2 space-y-1 text-[#b5b0a4]">
                    <li>IP <code class="text-stone-200">10.15.20.200</code>: Matches /16, /24, /25 $\\rightarrow$ <strong>Eth2 (/25 LPM)</strong></li>
                    <li>IP <code class="text-stone-200">10.15.20.50</code>: Matches /16, /24 $\\rightarrow$ <strong>Eth1 (/24 LPM)</strong></li>
                    <li>IP <code class="text-stone-200">10.15.21.5</code>: Matches only /16 $\\rightarrow$ <strong>Eth0 (/16 LPM)</strong></li>
                    <li>IP <code class="text-stone-200">192.168.1.1</code>: Matches none $\\rightarrow$ <strong>Eth3 (Default)</strong></li>
                </ul>
                """)

        # =========================================================================
        # SECTION 4: Data Link Layer & Error Control
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-5"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-shield-halved text-blue-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">4. Data Link Layer & Error Control (CSMA, Hamming, CRC)</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs"):
                # CSMA/CD vs CSMA/CA Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(79,142,201,0.3)] gap-2"):
                    ui.label("CSMA/CD (Ethernet) vs CSMA/CA (Wi-Fi)").classes("font-bold text-blue-300 text-sm")
                    ui.html("""
                    <div class="formula-box text-xs mb-2">
                        $$L_{\\text{min}} \\ge 2 \\cdot t_{\\text{prop}} \\cdot R = 2 \\cdot \\left(\\frac{l}{u}\\right) \\cdot R$$
                    </div>
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">CSMA/CD (802.3):</strong> Collision detection during active transmission. If collision occurs: Jam Signal + Exponential Backoff.</li>
                        <li><strong class="text-stone-200">CSMA/CA (802.11):</strong> Wireless cannot detect collisions (Hidden Terminal). Uses collision <em>avoidance</em> via Backoff timers and optional <strong>RTS/CTS</strong>.</li>
                    </ul>
                    """)

                # Hamming Code Calculation Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(245,158,11,0.3)] gap-2"):
                    ui.label("Hamming Code (Single Error Correction)").classes("font-bold text-amber-300 text-sm")
                    ui.html("""
                    <div class="formula-box text-xs mb-2">
                        $$2^p \\ge d + p + 1 \\quad (d=8 \\Rightarrow p=4, \\text{ positions } 1, 2, 4, 8)$$
                    </div>
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">$P_1$:</strong> Verifies positions 1, 3, 5, 7, 9, 11...</li>
                        <li><strong class="text-stone-200">$P_2$:</strong> Verifies positions 2, 3, 6, 7, 10, 11...</li>
                        <li><strong class="text-stone-200">$P_4$:</strong> Verifies positions 4, 5, 6, 7, 12...</li>
                        <li><strong class="text-stone-200">$P_8$:</strong> Verifies positions 8, 9, 10, 11, 12...</li>
                        <li><strong class="text-stone-200">Odd Parity:</strong> Total ones across checked indices must equal an odd number.</li>
                    </ul>
                    """)

                # CRC Modulo-2 Division Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(16,185,129,0.3)] gap-2"):
                    ui.label("Cyclic Redundancy Check (CRC)").classes("font-bold text-emerald-300 text-sm")
                    ui.html("""
                    <div class="formula-box text-xs mb-2">
                        $$\\text{Tx} = D \\cdot 2^r \\oplus R, \\quad R = (D \\cdot 2^r) \\bmod G$$
                    </div>
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li>Append $r$ zeros to data word $D$ (where $r = \\deg(G) = \\text{length}(G) - 1$).</li>
                        <li>Perform Modulo-2 binary polynomial division (XOR: $1\\oplus 1=0, 0\\oplus 0=0, 1\\oplus 0=1$).</li>
                        <li>Remainder $R$ ($r$ bits) replaces trailing zeros in the transmitted frame.</li>
                    </ul>
                    """)

                # Checksum & Parity Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(239,68,68,0.3)] gap-2"):
                    ui.label("Parity Bits & Internet Checksum").classes("font-bold text-red-300 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Parity Bits:</strong> Exclusively for 1-bit error <em>detection</em> (CANNOT correct errors).</li>
                        <li><strong class="text-stone-200">Internet Checksum (IP/UDP/TCP):</strong> 16-bit 1's complement addition with bitwise complement inversion at the end.</li>
                    </ul>
                    """)

        # =========================================================================
        # SECTION 5: ARP Protocol & Diagnostics
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-5"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-magnifying-glass text-cyan-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">5. ARP Protocol & Diagnostic Tools (Traceroute)</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs"):
                # ARP Exchange Structure Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(6,182,212,0.3)] gap-2"):
                    ui.label("ARP Request & Reply Message Structure").classes("font-bold text-cyan-300 text-sm")
                    ui.html("""
                    <div class="p-2.5 rounded bg-[#141413] border border-[rgba(255,255,255,0.06)] font-mono space-y-1 text-xs">
                        <div class="text-amber-300 font-bold">ARP Request (Broadcast -&gt; FF-FF-FF-FF-FF-FF):</div>
                        <div>Sender MAC: <span class="text-stone-200">71-65-F7-2B-08-53</span>, IP: <span class="text-stone-200">137.196.7.23</span></div>
                        <div>Target MAC: <span class="text-red-400">00-00-00-00-00-00</span>, IP: <span class="text-stone-200">137.196.7.14</span></div>
                        <div class="text-emerald-300 font-bold mt-2">ARP Reply (Unicast directly to A):</div>
                        <div>Sender MAC: <span class="text-emerald-400">58-23-D7-FA-20-B0</span>, IP: <span class="text-stone-200">137.196.7.14</span></div>
                        <div>Target MAC: <span class="text-stone-200">71-65-F7-2B-08-53</span>, IP: <span class="text-stone-200">137.196.7.23</span></div>
                    </div>
                    <ul class="m-0 pl-4 mt-2 space-y-1 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">ARP Cache:</strong> Caches IP-to-MAC bindings for 15-20 minutes. Subsequent transmissions within this window <em>do NOT emit new ARP requests</em>!</li>
                        <li><strong class="text-stone-200">Out-of-Subnet:</strong> If the destination IP resides outside the local subnet, an ARP request is emitted for the MAC of the <em>Default Gateway</em>.</li>
                    </ul>
                    """)

                # Traceroute Mechanism Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(6,182,212,0.3)] gap-2"):
                    ui.label("Traceroute Tool & TTL Mechanism").classes("font-bold text-cyan-300 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-2 text-[#b5b0a4]">
                        <li>1. Emits a sequence of IP probe packets with <strong class="text-stone-200">TTL = 1</strong>.</li>
                        <li>2. The 1st router decrements TTL to 0, drops the packet, and returns an <strong class="text-amber-300">ICMP Time Exceeded (Type 11)</strong> error, revealing its interface IP.</li>
                        <li>3. The sender increments to <strong class="text-stone-200">TTL = 2, 3...</strong> until reaching the destination, which returns <strong class="text-emerald-300">ICMP Port Unreachable (Type 3)</strong> or Echo Reply.</li>
                    </ul>
                    """)

        # =========================================================================
        # SECTION 6: Routing Protocols & Algorithms
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-5"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-route text-amber-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">6. Routing Protocols & Algorithms (Dijkstra, Bellman-Ford, Cisco IOS)</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs"):
                # Link-State vs Distance Vector Comparison Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(245,158,11,0.3)] gap-2"):
                    ui.label("Link State (Dijkstra) vs Distance Vector (Bellman-Ford)").classes("font-bold text-amber-300 text-sm")
                    ui.html("""
                    <div class="overflow-x-auto">
                        <table class="w-full text-left text-xs border-collapse">
                            <thead>
                                <tr class="border-b border-[rgba(255,255,255,0.1)] text-[#e06b3a]">
                                    <th class="py-1 px-2">Property</th>
                                    <th class="py-1 px-2">Link-State (LS)</th>
                                    <th class="py-1 px-2">Distance Vector (DV)</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-[rgba(255,255,255,0.05)] text-[#b5b0a4]">
                                <tr><td class="py-1 px-2 text-stone-200">Algorithm</td><td class="py-1 px-2">Dijkstra</td><td class="py-1 px-2">Bellman-Ford</td></tr>
                                <tr><td class="py-1 px-2 text-stone-200">Topology Map</td><td class="py-1 px-2">Complete global network topology</td><td class="py-1 px-2">Direct neighbors only</td></tr>
                                <tr><td class="py-1 px-2 text-stone-200">Equation</td><td class="py-1 px-2">$D(v) = \\min(D(v), D(w)+c(w,v))$</td><td class="py-1 px-2">$d_x(y) = \\min_v \\{c(x,v)+d_v(y)\\}$</td></tr>
                                <tr><td class="py-1 px-2 text-stone-200">Protocols</td><td class="py-1 px-2 text-emerald-400">OSPF, IS-IS</td><td class="py-1 px-2 text-blue-400">RIP (max 15 hops)</td></tr>
                                <tr><td class="py-1 px-2 text-stone-200">Issues</td><td class="py-1 px-2">Higher CPU/RAM load</td><td class="py-1 px-2 text-red-400">Count-to-Infinity</td></tr>
                            </tbody>
                        </table>
                    </div>
                    """)

                # DV Loop Solutions & BGP Hot-Potato Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(224,107,58,0.3)] gap-2"):
                    ui.label("DV Loop Prevention & BGP Hot-Potato").classes("font-bold text-[#e06b3a] text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Split Horizon:</strong> Do not advertise a learned route back out the same interface it was learned from.</li>
                        <li><strong class="text-stone-200">Poisoned Reverse:</strong> If node X routes to Y through Z, X advertises to Z that its cost to Y is $\\infty$.</li>
                        <li><strong class="text-stone-200">BGP Hot-Potato Routing:</strong> Select the egress gateway router that is <em>internally closest to the origin</em> (lowest IGP metric) to hand off the packet immediately.</li>
                    </ul>
                    """)

            # Cisco IOS CLI Commands Box
            with ui.column().classes("w-full p-4 rounded-xl bg-[#141413] border border-[rgba(79,142,201,0.3)] gap-2 text-xs"):
                ui.label("Cisco IOS Router Configuration Commands (Exam Topics)").classes("font-bold text-blue-400 text-sm")
                with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full"):
                    ui.html("""
                    <div class="p-3 rounded bg-[#201f1d] border border-[rgba(255,255,255,0.06)] font-mono">
                        <div class="text-amber-300 font-bold mb-1">// OSPF Single Area 0 (with Wildcard Masks)</div>
                        <div>R&gt;enable</div>
                        <div>R#configure terminal</div>
                        <div>R(config)#router ospf 1</div>
                        <div>R(config-router)#network 10.10.10.0 0.0.0.3 area 0</div>
                        <div>R(config-router)#network 10.10.23.0 0.0.0.3 area 0</div>
                        <div>R(config-router)#network 172.16.8.0 0.0.0.7 area 0</div>
                        <div>R(config-router)#network 192.168.1.0 0.0.0.255 area 0</div>
                        <div>R(config-router)#end</div>
                    </div>
                    """)
                    ui.html("""
                    <div class="p-3 rounded bg-[#201f1d] border border-[rgba(255,255,255,0.06)] font-mono">
                        <div class="text-emerald-300 font-bold mb-1">// RIP version 2</div>
                        <div>R&gt;enable</div>
                        <div>R#configure terminal</div>
                        <div>R(config)#router rip</div>
                        <div>R(config-router)#version 2</div>
                        <div>R(config-router)#no auto-summary</div>
                        <div>R(config-router)#network 10.15.2.0</div>
                        <div>R(config-router)#network 10.15.3.0</div>
                        <div>R(config-router)#network 10.15.6.0</div>
                        <div>R(config-router)#end</div>
                    </div>
                    """)

        # =========================================================================
        # SECTION 7: Transport Layer (TCP) & Network Security
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-5"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-arrows-split-up-and-left text-emerald-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">7. Transport Layer (TCP Congestion Control, BBR & Security)</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-3 gap-4 w-full text-xs"):
                # TCP Congestion Control Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(16,185,129,0.3)] gap-2"):
                    ui.label("TCP Congestion Control").classes("font-bold text-emerald-300 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Slow Start:</strong> $CWND$ doubles each RTT ($1 \\rightarrow 2 \\rightarrow 4...$) until reaching `ssthresh`.</li>
                        <li><strong class="text-stone-200">Congestion Avoidance:</strong> $CWND$ grows linearly by $+1\\text{ MSS}$ per RTT.</li>
                        <li><strong class="text-stone-200">Timeout:</strong> `ssthresh` = $CWND/2$, $CWND=1\\text{ MSS}$.</li>
                        <li><strong class="text-stone-200">3 Dup ACKs:</strong> Fast Recovery $\\rightarrow$ `ssthresh` = $CWND/2$, $CWND = \\text{ssthresh}$.</li>
                    </ul>
                    """)

                # TCP BBR Algorithm Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(79,142,201,0.3)] gap-2"):
                    ui.label("TCP BBR Algorithm").classes("font-bold text-blue-300 text-sm")
                    ui.html("""
                    <div class="formula-box text-xs mb-2">
                        $$CWND = RtProp \\times BtlBw$$
                    </div>
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">RtProp:</strong> $\\min(RTT)$ (e.g., $5\\text{ ms} = 0.005\\text{ s}$).</li>
                        <li><strong class="text-stone-200">BtlBw:</strong> Bottleneck link bandwidth ($0.125\\text{ GB/s} = 10^8\\text{ B/s} = 8\\times 10^8\\text{ bps}$).</li>
                        <li><strong class="text-emerald-400">CWND:</strong> $0.005 \\times 8\\cdot 10^8 = 4,000,000\\text{ bits} \\ (500\\text{ KB})$.</li>
                    </ul>
                    """)

                # Karn's Rule & Security Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(245,158,11,0.3)] gap-2"):
                    ui.label("Karn's Rule & Firewalls").classes("font-bold text-amber-300 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Karn's Rule:</strong> Do not sample $SampleRTT$ on retransmitted segments.</li>
                        <li><strong class="text-stone-200">RFC 7323:</strong> Timestamps Option enables unambiguous RTT calculation.</li>
                        <li><strong class="text-stone-200">Stateless Firewall:</strong> Inspects packets independently by IP/Port.</li>
                        <li><strong class="text-stone-200">Stateful Inspection:</strong> Maintains tracking state table for ongoing TCP connections.</li>
                    </ul>
                    """)

        # =========================================================================
        # SECTION 8: 10/10 Master Exam Checklist
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-list-check text-[#e06b3a] text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">8. Comprehensive Exam Preparation Checklist (10/10)</h3>')

            checklist_items = [
                "Distinguish Simplex, Half-Duplex, and Full-Duplex, and recognize that Multiplexing (FDM/TDM) is not a transmission mode.",
                "Identify device layers: Repeater/Hub is Layer 1, Switch is Layer 2, and Router is Layer 3.",
                "Understand that IP addresses remain invariant end-to-end, while MAC addresses change at each router hop.",
                "Distinguish Control Plane (Software / RIB) and Data Plane (Hardware / ASICs / FIB).",
                "Calculate total Nodal Delay (d_proc + d_queue + L/R + l/u) and recognize that N counts link hops (not router count).",
                "Apply the pipelining formula for P packets across N hops: T = (N + P - 1)(L/R) + N(l/u) + (N-1)d_proc.",
                "Compute BDP directly using student ID parameters: Max Bits = 8 * ID * delay_ms bits.",
                "Apply the Sliding Window condition W >= R * RTT for 100% channel utilization.",
                "Solve Subnetting problems (CIDR /24, /26, /28, /29, /30) and compute usable host counts (2^(32-n) - 2).",
                "Apply the Longest Prefix Match (LPM) rule to determine the correct egress router interface.",
                "Apply the minimum frame size formula L_min >= 2 * t_prop * R in CSMA/CD and contrast with CSMA/CA (Wi-Fi RTS/CTS).",
                "Construct Hamming codes (power-of-two parity bit positions, odd/even parity) and compute CRC (Modulo-2 XOR division).",
                "Recall that ARP Request is Broadcast (FF-FF-FF-FF-FF-FF) and Reply is Unicast, with an ARP cache TTL of 15-20 min.",
                "Understand Traceroute operation via incremental TTL probes and ICMP Time Exceeded responses.",
                "Differentiate Single-Mode Fiber (Laser, 8-10 um, long haul) vs Multi-Mode Fiber (LED, 50-62.5 um, short reach).",
                "Differentiate GEO satellites (36,000 km, ~250 ms propagation) vs LEO constellations (500-1,500 km, ~10-20 ms, Starlink).",
                "Execute Dijkstra's algorithm step-by-step and formulate Bellman-Ford distance vector updates.",
                "Identify Count-to-Infinity, Split Horizon, Poisoned Reverse, and the RIP 15-hop ceiling.",
                "Write Cisco IOS commands for OSPF single area 0 (router ospf 1, network ... wildcard area 0) and RIPv2.",
                "Apply BGP Hot-Potato routing rules, TCP Congestion Control phases, and the BBR formula CWND = RtProp * BtlBw.",
            ]

            with ui.column().classes("w-full gap-2 text-xs leading-relaxed"):
                for item in checklist_items:
                    with ui.row().classes("items-start gap-2 p-2 rounded-lg bg-[#201f1d] border border-[rgba(255,255,255,0.04)]"):
                        ui.html('<i class="fa-solid fa-square-check text-[#e06b3a] mt-0.5"></i>')
                        ui.label(item).classes("text-[#b5b0a4]")
