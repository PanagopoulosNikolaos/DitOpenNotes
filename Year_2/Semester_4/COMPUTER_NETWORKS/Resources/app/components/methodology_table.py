"""Methodology and protocol comparison tables component for Computer Networks."""

from nicegui import ui


def renderMethodologyTable() -> None:
    """Renders comprehensive reference and comparison tables for networking."""
    with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-6"):
        with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
            ui.html('<i class="fa-solid fa-table-list text-[#f59e0b] text-xl"></i>')
            with ui.column().classes("gap-0"):
                ui.html('<h2 class="text-xl font-bold gradient-title m-0">Comparative Tables & Methodology</h2>')
                ui.label("Summary reference tables distinguishing networking technologies, devices, and protocols.").classes("text-xs text-[#b5b0a4]")

        # Table 1: Device vs Domains Matrix
        with ui.column().classes("w-full gap-2"):
            ui.html('<h3 class="text-sm font-bold text-[#fed7aa] m-0">1. Device, OSI Layer & Collision/Broadcast Domains Matrix</h3>')
            with ui.row().classes("w-full p-4 rounded-xl bg-[#201f1d] border border-[rgba(255,255,255,0.06)] font-mono text-xs text-[#fed7aa] overflow-x-auto"):
                ui.html("""<pre class="m-0">
  Device                OSI Layer       PDU             Collision Domains                   Broadcast Domains               Functions & Characteristics
  ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
  Repeater / Hub        Layer 1 (Phys)  Bit             1 Shared across all ports           1 Single domain                 Regenerates physical signal without inspection.
  Bridge / Switch       Layer 2 (Link)  Frame           1 per physical port (Microsegment)  1 Single domain                 Filters based on MAC addresses (MAC Table).
  Router                Layer 3 (Net)   Packet          1 per physical interface            1 per physical interface        Isolates broadcast domains, routes via IP.
  Gateway               Layer 4-7       Segment/Message 1 per connection                    1 per connection                Translates higher-layer protocols.
</pre>""")

        # Table 2: Routing Protocols Comparison
        with ui.column().classes("w-full gap-2"):
            ui.html('<h3 class="text-sm font-bold text-[#fed7aa] m-0">2. Interior & Exterior Routing Protocols Comparison</h3>')
            with ui.row().classes("w-full p-4 rounded-xl bg-[#201f1d] border border-[rgba(255,255,255,0.06)] font-mono text-xs text-[#fed7aa] overflow-x-auto"):
                ui.html("""<pre class="m-0">
  Protocol        Algorithm Type            Metric                      Convergence                 Usage & Limitations
  ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
  RIPv1 / RIPv2   Distance-Vector (Bellman) Hop Count (Max 15 hops)     Slow (Count to Infinity)    Small LAN/Campus networks.
  OSPF            Link-State (Dijkstra)     Cost (Inverse Bandwidth)    Very Fast (LSA Flooding)    Large Enterprise & ISP networks.
  BGP (Border)    Path-Vector (Policy-based)AS-Path + BGP Attributes    Stable (Policy Routing)     Inter-Autonomous System (Internet).
</pre>""")
