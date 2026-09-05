"""Topic 7: Basic Networking Issues theory renderer.

Covers Layer 2 MAC vs Layer 3 IP vs Layer 4 Port Addressing, Subnetting & CIDR,
ARP Protocol (Request broadcast, Reply unicast, ARP Cache, Default Gateway),
Error Detection & Correction (Parity bits, Internet Checksum, Hamming Codes, CRC Modulo-2),
and Network Diagnostics (Ping, Traceroute).
"""

from nicegui import ui


def renderTopic7BasicNetworkingIssues() -> None:
    """Renders the comprehensive theory module for Topic 7: Basic Networking Issues."""
    with ui.column().classes("w-full gap-6 text-[#f4f1ea] latex-target"):
        # Header Banner
        with ui.column().classes(
            "w-full glass-panel p-6 md:p-8 rounded-2xl border border-[rgba(224,107,58,0.35)] gap-3"
        ):
            with ui.row().classes("items-center gap-3"):
                ui.html('<i class="fa-solid fa-microchip text-[#e06b3a] text-3xl"></i>')
                with ui.column().classes("gap-0"):
                    ui.html('<h2 class="text-xl md:text-2xl font-bold gradient-title m-0">Topic 7: Basic Networking Issues</h2>')
                    ui.label(
                        "Addressing (MAC, IP, Ports), Subnetting (CIDR & Masks), "
                        "ARP Protocol, Error Detection & Correction (Parity, Checksum, Hamming, CRC), and Network Diagnostics."
                    ).classes("text-xs md:text-sm text-[#b5b0a4]")

        # =========================================================================
        # SECTION 1: Addressing Architecture (MAC, IP, Ports)
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-address-card text-blue-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">1. Multi-Layer Addressing: MAC vs IP vs Ports</h3>')

            ui.html("""
            <div class="overflow-x-auto">
                <table class="w-full text-left text-xs border-collapse">
                    <thead>
                        <tr class="border-b border-[rgba(255,255,255,0.1)] text-[#e06b3a]">
                            <th class="py-2 px-3">Address Type</th>
                            <th class="py-2 px-3">OSI Layer</th>
                            <th class="py-2 px-3">Size / Format</th>
                            <th class="py-2 px-3">Scope</th>
                            <th class="py-2 px-3">Router Behavior</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-[rgba(255,255,255,0.05)] text-[#b5b0a4]">
                        <tr>
                            <td class="py-2 px-3 font-bold text-stone-200">MAC (Physical Address)</td>
                            <td class="py-2 px-3 font-mono text-blue-400">Layer 2 (Data Link)</td>
                            <td class="py-2 px-3 font-mono">48 bits (6 hex bytes)</td>
                            <td class="py-2 px-3 text-amber-300">Local (within LAN / Hop-by-Hop)</td>
                            <td class="py-2 px-3 text-red-300 font-bold">Rewritten at each intermediate router hop.</td>
                        </tr>
                        <tr>
                            <td class="py-2 px-3 font-bold text-stone-200">IP (Logical Address)</td>
                            <td class="py-2 px-3 font-mono text-emerald-400">Layer 3 (Network)</td>
                            <td class="py-2 px-3 font-mono">32 bits (IPv4) / 128 (IPv6)</td>
                            <td class="py-2 px-3 text-emerald-300">Global (End-to-End)</td>
                            <td class="py-2 px-3 text-emerald-300 font-bold">Remains invariant from source host to destination.</td>
                        </tr>
                        <tr>
                            <td class="py-2 px-3 font-bold text-stone-200">Port (Process Identifier)</td>
                            <td class="py-2 px-3 font-mono text-purple-400">Layer 4 (Transport)</td>
                            <td class="py-2 px-3 font-mono">16 bits (0 - 65,535)</td>
                            <td class="py-2 px-3 text-purple-300">Host Process</td>
                            <td class="py-2 px-3">Identifies target service (e.g., HTTP 80, HTTPS 443, DNS 53).</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            """)

        # =========================================================================
        # SECTION 2: Subnetting & CIDR Calculations
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-network-wired text-emerald-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">2. IPv4 Subnetting & CIDR Notation</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs"):
                with ui.column().classes("p-4 rounded-xl bg-[#141413] border border-[rgba(16,185,129,0.3)] gap-2"):
                    ui.label("Fundamental Subnetting Formulas").classes("font-bold text-emerald-400 text-sm")
                    ui.html("""
                    <div class="formula-box text-xs mb-2">
                        $$\\text{Block Size} = 2^{32 - \\text{prefix}}, \\quad \\text{Usable Hosts} = 2^{32 - \\text{prefix}} - 2$$
                    </div>
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Network Address:</strong> First IP in the block (host bits = all '0'). Not assignable to hosts.</li>
                        <li><strong class="text-stone-200">Broadcast Address:</strong> Last IP in the block (host bits = all '1'). Not assignable to hosts.</li>
                        <li><strong class="text-stone-200">Usable IP Range:</strong> From (Network + 1) through (Broadcast - 1).</li>
                    </ul>
                    """)

                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(245,158,11,0.3)] gap-2"):
                    ui.label("Example: /26 Subnet").classes("font-bold text-amber-300 text-sm")
                    ui.html("""
                    <div class="space-y-1 font-mono text-xs text-[#b5b0a4]">
                        <div>• Mask: <span class="text-stone-200">255.255.255.192 (/26)</span></div>
                        <div>• Host bits: <span class="text-stone-200">32 - 26 = 6 bits</span></div>
                        <div>• Block Size: <span class="text-stone-200">$2^6 = 64$ addresses</span></div>
                        <div>• Usable Hosts: <span class="text-emerald-300 font-bold">$64 - 2 = 62$ hosts</span></div>
                        <div>• Subnet 1: <span class="text-blue-300">192.168.1.0 - 192.168.1.63</span> (Net: .0, Bc: .63)</div>
                        <div>• Subnet 2: <span class="text-blue-300">192.168.1.64 - 192.168.1.127</span> (Net: .64, Bc: .127)</div>
                    </div>
                    """)

        # =========================================================================
        # SECTION 3: Address Resolution Protocol (ARP)
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-magnifying-glass text-cyan-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">3. Address Resolution Protocol (ARP)</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs"):
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(6,182,212,0.3)] gap-2"):
                    ui.label("IP -> MAC Resolution in LAN").classes("font-bold text-cyan-300 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1.5 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">ARP Request:</strong> Sent as Link-Layer <strong>Broadcast</strong> (MAC: <code>FF-FF-FF-FF-FF-FF</code>). All LAN nodes receive it. Target MAC = <code>00-00-00-00-00-00</code>.</li>
                        <li><strong class="text-stone-200">ARP Reply:</strong> The owner of the queried IP replies via <strong>Unicast</strong> directly to the requester, returning its hardware MAC address.</li>
                    </ul>
                    """)

                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(6,182,212,0.3)] gap-2"):
                    ui.label("ARP Cache & Default Gateway").classes("font-bold text-cyan-300 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1.5 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">ARP Cache:</strong> Temporary lookup table (TTL 15-20 min). Outbound packets within this window bypass ARP broadcast discovery.</li>
                        <li><strong class="text-stone-200">Out-of-Subnet Routing:</strong> If the destination IP is external, the sending host queries the MAC address of its <strong>Default Gateway (Router)</strong>!</li>
                    </ul>
                    """)

        # =========================================================================
        # SECTION 4: Error Detection & Correction (Hamming & CRC)
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-shield-halved text-amber-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">4. Error Detection & Correction (Parity, Hamming, CRC)</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs"):
                # Hamming Code Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(245,158,11,0.3)] gap-2"):
                    ui.label("Hamming Code (Single Error Correction)").classes("font-bold text-amber-300 text-sm")
                    ui.html("""
                    <div class="formula-box text-xs mb-2">
                        $$2^p \\ge d + p + 1 \\quad (d=8 \\Rightarrow p=4, \\text{ positions } 1, 2, 4, 8)$$
                    </div>
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Parity Positions:</strong> Powers of 2 ($P_1, P_2, P_4, P_8$). Data bits ($D_i$) occupy the remaining bit indices (3, 5, 6, 7, 9, 10, 11, 12).</li>
                        <li><strong class="text-stone-200">Parity Coverage:</strong> Each $P_i$ verifies all indices whose binary representation contains a 1 at position $i$.</li>
                        <li><strong class="text-stone-200">Odd Parity:</strong> Parity bits are set to 0 or 1 so that the sum of ones in covered positions is odd.</li>
                    </ul>
                    """)

                # CRC Division Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(16,185,129,0.3)] gap-2"):
                    ui.label("Cyclic Redundancy Check (CRC)").classes("font-bold text-emerald-300 text-sm")
                    ui.html("""
                    <div class="formula-box text-xs mb-2">
                        $$\\text{Tx} = D \\cdot 2^r \\oplus R, \\quad R = (D \\cdot 2^r) \\bmod G$$
                    </div>
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li>Append $r$ zeros to data bits $D$ ($r = \\deg(G)$, the degree of generator polynomial $G$).</li>
                        <li>Perform Modulo-2 binary polynomial division (XOR) with generator $G$.</li>
                        <li>The remainder $R$ ($r$ bits) is appended to data $D$. The receiver divides the frame by $G$; a zero remainder indicates no bit errors.</li>
                    </ul>
                    """)
