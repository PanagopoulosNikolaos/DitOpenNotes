"""Topic 2: The Internet and Protocols theory renderer.

Covers Internet Hardware (Routers, Switches, Modems, Repeaters), TCP/IP & OSI stacks,
IPv4 vs IPv6, TCP vs UDP, DNS architecture & queries, Traceroute, Optical Submarine Cables vs Satellites,
Packet Segmentation, 4 Delays with numerical LaTeX examples, and Encapsulation.
"""

from nicegui import ui


def renderTopic2TheInternet() -> None:
    """Renders the comprehensive theory module for Topic 2: The Internet & Protocols."""
    with ui.column().classes("w-full gap-6 text-[#f4f1ea] latex-target"):
        # Header Banner
        with ui.column().classes(
            "w-full glass-panel p-6 md:p-8 rounded-2xl border border-[rgba(224,107,58,0.35)] gap-3"
        ):
            with ui.row().classes("items-center gap-3"):
                ui.html('<i class="fa-solid fa-globe text-[#e06b3a] text-3xl"></i>')
                with ui.column().classes("gap-0"):
                    ui.html('<h2 class="text-xl md:text-2xl font-bold gradient-title m-0">Topic 2: The Internet & Protocols</h2>')
                    ui.label(
                        "Network Hardware, TCP/IP Protocol Stack, IP/MAC Addressing, DNS, Traceroute, "
                        "Undersea Fiber Cables, GEO/LEO Satellites, Delay Calculations, and Encapsulation."
                    ).classes("text-xs md:text-sm text-[#b5b0a4]")

        # =========================================================================
        # SECTION 1: Hardware & Network Interconnection Devices
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-microchip text-blue-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">1. Hardware: Interconnection Equipment & Devices</h3>')

            ui.html("""
            <div class="overflow-x-auto">
                <table class="w-full text-left text-xs border-collapse">
                    <thead>
                        <tr class="border-b border-[rgba(255,255,255,0.1)] text-[#e06b3a]">
                            <th class="py-2 px-3">Device</th>
                            <th class="py-2 px-3">OSI Layer</th>
                            <th class="py-2 px-3">PDU</th>
                            <th class="py-2 px-3">Addressing</th>
                            <th class="py-2 px-3">Key Function & Characteristics</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-[rgba(255,255,255,0.05)] text-[#b5b0a4]">
                        <tr>
                            <td class="py-2 px-3 font-bold text-stone-200">Repeater / Hub</td>
                            <td class="py-2 px-3 font-mono text-amber-300">Layer 1 (Physical)</td>
                            <td class="py-2 px-3">Bits</td>
                            <td class="py-2 px-3 text-[#78756d]">None</td>
                            <td class="py-2 px-3">Electrical/optical signal regeneration and amplification. Single shared collision domain (Shared Medium).</td>
                        </tr>
                        <tr>
                            <td class="py-2 px-3 font-bold text-stone-200">Bridge / Switch</td>
                            <td class="py-2 px-3 font-mono text-blue-400">Layer 2 (Data Link)</td>
                            <td class="py-2 px-3 font-mono text-blue-300">Frame</td>
                            <td class="py-2 px-3 font-mono text-stone-200">MAC (48-bit)</td>
                            <td class="py-2 px-3">Frame filtering and forwarding based on MAC table. Each port = isolated Collision Domain. Preserves Broadcast Domain.</td>
                        </tr>
                        <tr>
                            <td class="py-2 px-3 font-bold text-stone-200">Router</td>
                            <td class="py-2 px-3 font-mono text-emerald-400">Layer 3 (Network)</td>
                            <td class="py-2 px-3 font-mono text-emerald-300">Packet / Datagram</td>
                            <td class="py-2 px-3 font-mono text-stone-200">IP (32/128-bit)</td>
                            <td class="py-2 px-3">Interconnects distinct subnets, computes optimal paths (RIB/FIB). Each interface = isolated Broadcast Domain.</td>
                        </tr>
                        <tr>
                            <td class="py-2 px-3 font-bold text-stone-200">Modem</td>
                            <td class="py-2 px-3 font-mono text-amber-300">Layer 1 / 2</td>
                            <td class="py-2 px-3">Signals / Bits</td>
                            <td class="py-2 px-3 text-[#78756d]">Physical</td>
                            <td class="py-2 px-3">Modulation and Demodulation of digital signals onto analog carriers (DSL, Cable, Fiber ONT).</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            """)

        # =========================================================================
        # SECTION 2: The TCP/IP Protocol Stack & Architecture
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-layer-group text-amber-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">2. The TCP/IP Protocol Stack & OSI Model</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs"):
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(245,158,11,0.25)] gap-2"):
                    ui.label("TCP/IP Layers & Protocol Data Units (PDUs)").classes("font-bold text-amber-300 text-sm")
                    ui.html("""
                    <div class="space-y-1.5 font-mono text-xs">
                        <div class="p-2 rounded bg-[#141413] border border-[rgba(255,255,255,0.06)] flex justify-between">
                            <span class="text-purple-300 font-bold">5. Application</span>
                            <span class="text-[#b5b0a4]">Message (HTTP, DNS, SMTP, FTP)</span>
                        </div>
                        <div class="p-2 rounded bg-[#141413] border border-[rgba(255,255,255,0.06)] flex justify-between">
                            <span class="text-blue-300 font-bold">4. Transport</span>
                            <span class="text-[#b5b0a4]">Segment (TCP, UDP, Ports)</span>
                        </div>
                        <div class="p-2 rounded bg-[#141413] border border-[rgba(255,255,255,0.06)] flex justify-between">
                            <span class="text-emerald-300 font-bold">3. Network</span>
                            <span class="text-[#b5b0a4]">Datagram / Packet (IP, ICMP, OSPF, BGP)</span>
                        </div>
                        <div class="p-2 rounded bg-[#141413] border border-[rgba(255,255,255,0.06)] flex justify-between">
                            <span class="text-amber-300 font-bold">2. Data Link</span>
                            <span class="text-[#b5b0a4]">Frame (Ethernet 802.3, Wi-Fi 802.11, ARP)</span>
                        </div>
                        <div class="p-2 rounded bg-[#141413] border border-[rgba(255,255,255,0.06)] flex justify-between">
                            <span class="text-stone-300 font-bold">1. Physical</span>
                            <span class="text-[#b5b0a4]">Bits (UTP, Fiber, Wireless signals)</span>
                        </div>
                    </div>
                    """)

                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(79,142,201,0.25)] gap-2"):
                    ui.label("IPv4 vs IPv6 & Protocol Definition").classes("font-bold text-blue-300 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1.5 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Protocol Definition:</strong> A formalized set of rules governing message format (syntax), semantic meaning (semantics), and transmission/reception sequencing between two or more communicating entities.</li>
                        <li><strong class="text-stone-200">IPv4 (32-bit):</strong> $2^{32} \\approx 4.3$ billion addresses (e.g. `192.168.1.1`). Exhausted $\\rightarrow$ requires NAT.</li>
                        <li><strong class="text-stone-200">IPv6 (128-bit):</strong> $2^{128} \\approx 3.4 \\times 10^{38}$ addresses (hexadecimal notation, e.g. `2001:db8::1`). Eliminates NAT, natively supports SLAAC and IPsec.</li>
                    </ul>
                    """)

        # =========================================================================
        # SECTION 3: DNS Architecture & Query Sequence
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-sitemap text-emerald-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">3. Domain Name System (DNS)</h3>')

            ui.label(
                "DNS is a distributed, hierarchical database mapping human-readable hostnames "
                "(e.g., dit.uoi.gr) to numerical IP addresses (e.g., 195.130.8.25). Operates on UDP port 53."
            ).classes("text-xs md:text-sm text-[#b5b0a4]")

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs"):
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(16,185,129,0.3)] gap-2"):
                    ui.label("DNS Server Hierarchy").classes("font-bold text-emerald-300 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Root DNS Servers:</strong> 13 logical root authorities (A-M) instantiated via hundreds of anycast nodes globally. Direct queries to TLD servers.</li>
                        <li><strong class="text-stone-200">Top-Level Domain (TLD) Servers:</strong> Responsible for top-level extensions such as `.com`, `.org`, `.gr`, `.edu`.</li>
                        <li><strong class="text-stone-200">Authoritative DNS Servers:</strong> Official organizational servers holding actual resource records (A, AAAA, MX, CNAME).</li>
                        <li><strong class="text-stone-200">Local DNS Server (Resolver):</strong> The local ISP or campus resolver performing lookups on behalf of querying clients.</li>
                    </ul>
                    """)

                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(245,158,11,0.3)] gap-2"):
                    ui.label("Resolution Workflow & Caching").classes("font-bold text-amber-300 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">1. Local Cache Check:</strong> Browser cache $\\rightarrow$ OS Hosts file $\\rightarrow$ Local DNS Server cache.</li>
                        <li><strong class="text-stone-200">2. Iterative Lookup:</strong> Local DNS queries Root DNS $\\rightarrow$ TLD (`.gr`) $\\rightarrow$ Authoritative (`uoi.gr`).</li>
                        <li><strong class="text-stone-200">3. Recursive Lookup:</strong> Client delegates complete lookup to the Local DNS resolver and awaits the final response.</li>
                        <li><strong class="text-stone-200">DNS Caching (TTL):</strong> Records are cached for a Time-To-Live (TTL) duration, dramatically reducing global backbone traffic.</li>
                    </ul>
                    """)

        # =========================================================================
        # SECTION 4: Optical Submarine Cables vs Satellites (GEO vs LEO)
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-satellite-dish text-cyan-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">4. Optical Fiber (Submarine Cables) vs Satellites (GEO & LEO)</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-3 gap-3 w-full text-xs"):
                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(79,142,201,0.3)] gap-1.5"):
                    ui.label("Submarine Optical Fibers").classes("font-bold text-blue-300")
                    ui.label(
                        "• Carry over 99% of global intercontinental data traffic.\n"
                        "• Single-Mode Fiber (Laser) utilizing DWDM (Dense Wavelength Division Multiplexing).\n"
                        "• Massive bandwidth (hundreds of Tbps per fiber pair) with minimal propagation latency."
                    ).classes("text-[#b5b0a4] leading-relaxed")

                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(239,68,68,0.3)] gap-1.5"):
                    ui.label("Geostationary Satellites (GEO)").classes("font-bold text-red-300")
                    ui.label(
                        "• Orbital altitude: 35,786 km (~36,000 km).\n"
                        "• Stationary relative to Earth's surface (orbital period = 24 hours).\n"
                        "• Significant propagation delay: d_prop ≈ 36,000 km / (3*10^5 km/s) ≈ 120 ms (RTT ≥ 480-500 ms)."
                    ).classes("text-[#b5b0a4] leading-relaxed")

                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(16,185,129,0.3)] gap-1.5"):
                    ui.label("Low Earth Orbit Satellites (LEO)").classes("font-bold text-emerald-300")
                    ui.label(
                        "• Orbital altitude: 500 – 1,500 km (e.g. Starlink, Kuiper).\n"
                        "• Ultra-low propagation latency: d_prop ≈ 10 – 20 ms (competitive with terrestrial fiber networks).\n"
                        "• Require large constellations of thousands of satellites and continuous inter-satellite handovers."
                    ).classes("text-[#b5b0a4] leading-relaxed")

        # =========================================================================
        # SECTION 5: Comprehensive 4 Delays with Numerical LaTeX Example
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-calculator text-amber-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">5. Comprehensive Delay Breakdown & Numerical Example</h3>')

            ui.html("""
            <div class="p-4 rounded-xl bg-[#141413] border border-[rgba(224,107,58,0.35)] font-mono text-xs space-y-2">
                <div class="text-amber-300 font-bold text-sm">// Problem Parameters:</div>
                <div class="text-[#b5b0a4]">
                    • Packet Size: $L = 1{,}000\\text{ Bytes} = 8{,}000\\text{ bits}$<br>
                    • Transmission Rate: $R = 10\\text{ Mbps} = 10^7\\text{ bps}$<br>
                    • Link Distance: $l = 2{,}000\\text{ km} = 2 \\times 10^6\\text{ m}$<br>
                    • Propagation Speed: $u = 2 \\times 10^8\\text{ m/s}$ (Optical Fiber)<br>
                    • Processing Delay: $d_{\\text{proc}} = 1\\text{ ms} = 0.001\\text{ s}$, Queuing Delay: $d_{\\text{queue}} = 2\\text{ ms} = 0.002\\text{ s}$
                </div>
                <div class="text-emerald-300 font-bold mt-3">// Step 1: Transmission & Propagation Calculations:</div>
                <div class="text-stone-200">
                    $$d_{\\text{trans}} = \\frac{L}{R} = \\frac{8{,}000\\text{ bits}}{10^7\\text{ bps}} = 0.0008\\text{ s} = 0.8\\text{ ms}$$
                    $$d_{\\text{prop}} = \\frac{l}{u} = \\frac{2 \\times 10^6\\text{ m}}{2 \\times 10^8\\text{ m/s}} = 0.01\\text{ s} = 10\\text{ ms}$$
                </div>
                <div class="text-emerald-300 font-bold mt-3">// Step 2: Total Nodal Delay:</div>
                <div class="text-stone-200">
                    $$d_{\\text{nodal}} = d_{\\text{proc}} + d_{\\text{queue}} + d_{\\text{trans}} + d_{\\text{prop}} = 1 + 2 + 0.8 + 10 = 13.8\\text{ ms}$$
                </div>
            </div>
            """)
