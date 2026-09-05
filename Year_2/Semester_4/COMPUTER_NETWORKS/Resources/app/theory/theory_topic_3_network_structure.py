"""Topic 3: Network Structure theory renderer.

Covers Network of Networks, Hierarchical ISP Tiers (1, 2, 3), PoPs, IXPs,
Settlement-Free Peering vs Paid Transit, Content Provider Networks (Google/Meta),
Core vs Edge, Statistical Multiplexing, and Interconnection Topology.
"""

from nicegui import ui


def renderTopic3NetworkStructure() -> None:
    """Renders the comprehensive theory module for Topic 3: Network Structure."""
    with ui.column().classes("w-full gap-6 text-[#f4f1ea] latex-target"):
        # Header Banner
        with ui.column().classes(
            "w-full glass-panel p-6 md:p-8 rounded-2xl border border-[rgba(224,107,58,0.35)] gap-3"
        ):
            with ui.row().classes("items-center gap-3"):
                ui.html('<i class="fa-solid fa-diagram-project text-[#e06b3a] text-3xl"></i>')
                with ui.column().classes("gap-0"):
                    ui.html('<h2 class="text-xl md:text-2xl font-bold gradient-title m-0">Topic 3: Network Structure & ISPs</h2>')
                    ui.label(
                        "Network of Networks, Tier 1/2/3 ISP Hierarchy, "
                        "PoPs, IXPs, Peering vs Transit, Content Provider Networks, and Network Core."
                    ).classes("text-xs md:text-sm text-[#b5b0a4]")

        # =========================================================================
        # SECTION 1: Network of Networks Architecture
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-network-wired text-blue-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">1. The Internet as a "Network of Networks"</h3>')

            ui.label(
                "The Internet is not a single centralized entity, but rather a coordinated interconnection "
                "of tens of thousands of Autonomous Systems (AS) owned by commercial ISPs, universities, "
                "governments, and content providers. Their interconnection relies on hierarchical tiers and commercial agreements."
            ).classes("text-xs md:text-sm text-[#b5b0a4] leading-relaxed")

            with ui.column().classes("w-full p-4 rounded-xl bg-[#141413] border border-[rgba(255,255,255,0.06)] font-mono text-xs text-[#fed7aa]"):
                ui.html(r"""<pre class="m-0 overflow-x-auto">
  Hierarchical Structure of the Global Internet
  ─────────────────────────────────────────────────────────────────────────────
                [Tier-1 ISP A] <=== Settlement-Free Peering ===> [Tier-1 ISP B]
                    /       \                                         /       \
             Transit $       Transit $                         Transit $     Transit $
                  /           \                                   /             \
          [Tier-2 ISP 1] <--- IXP Peering ---> [Tier-2 ISP 2]      [Content Net]
              /       \                                      /       (Google/Meta)
       Transit $     Transit $                        Transit $            |
            /           \                                /            [Edge Caches]
      [Access ISP A] [Access ISP B]        [Access ISP C]              |
          /    \          |                      |                     |
     [Home]  [Corp]    [Home]                  [Home] ─────────── Direct Peering
</pre>""")

        # =========================================================================
        # SECTION 2: ISP Tiers & Interconnection Elements
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-sitemap text-amber-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">2. ISP Hierarchy (Tiers) & Interconnection Points (PoP / IXP)</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-3 gap-3 w-full text-xs"):
                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(224,107,58,0.25)] gap-1.5"):
                    ui.label("Tier-1 ISPs (Global Backbone)").classes("font-bold text-[#e06b3a]")
                    ui.label(
                        "• Global coverage with proprietary subsea and transcontinental optical fiber links (AT&T, NTT, Lumen, Telia).\n"
                        "• Never pay for transit. Interconnect with each other via Settlement-Free Peering (full-mesh connectivity)."
                    ).classes("text-[#b5b0a4] leading-relaxed")

                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(245,158,11,0.25)] gap-1.5"):
                    ui.label("Tier-2 ISPs (Regional)").classes("font-bold text-amber-300")
                    ui.label(
                        "• Regional or national network operators.\n"
                        "• Purchase transit bandwidth from Tier-1 providers for global reachability.\n"
                        "• Peer with each other at IXPs to reduce transit expenditure for local traffic."
                    ).classes("text-[#b5b0a4] leading-relaxed")

                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(79,142,201,0.25)] gap-1.5"):
                    ui.label("Tier-3 / Access ISPs (Local)").classes("font-bold text-blue-300")
                    ui.label(
                        "• Local last-mile service providers.\n"
                        "• Connect residential users, homes, and local enterprise offices.\n"
                        "• Purchase upstream transit from Tier-2 or Tier-1 providers."
                    ).classes("text-[#b5b0a4] leading-relaxed")

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs mt-2"):
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(16,185,129,0.25)] gap-2"):
                    ui.label("Points of Presence (PoP) & Internet Exchange Points (IXP)").classes("font-bold text-emerald-300 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1.5 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Point of Presence (PoP):</strong> A group of routers and switches at a specific physical location where customer networks can connect directly into an upstream provider's network.</li>
                        <li><strong class="text-stone-200">Internet Exchange Point (IXP):</strong> Standalone neutral infrastructure (typically a high-speed switch fabric inside a colocation data center) where multiple ISPs, CDNs, and content providers connect to peer directly without transit fees (e.g., DE-CIX, AMS-IX, LINX).</li>
                    </ul>
                    """)

                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(239,68,68,0.25)] gap-2"):
                    ui.label("Peering vs Transit (Economic Model)").classes("font-bold text-red-300 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1.5 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Transit (Paid Service):</strong> A customer ISP pays an upstream provider based on aggregate bandwidth (Gbps) to obtain universal reachability to the entire global Internet.</li>
                        <li><strong class="text-stone-200">Peering (Typically Settlement-Free):</strong> Two peer networks agree to exchange traffic destined exclusively for each other's direct customer bases without financial compensation, cutting transit costs.</li>
                    </ul>
                    """)

        # =========================================================================
        # SECTION 3: Content Provider Networks
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-server text-cyan-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">3. Private Content Provider Networks (Google, Meta, Microsoft)</h3>')

            ui.label(
                "Major hyperscale content providers do not rely solely on public commercial transit ISPs. "
                "They construct private global optical fiber backbones that interconnect their data centers and "
                "deploy edge caches and servers directly inside local access networks (Tier-3)."
            ).classes("text-xs md:text-sm text-[#b5b0a4]")

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs"):
                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(6,182,212,0.25)] gap-1"):
                    ui.label("Bypassing Upstream Tiers").classes("font-bold text-cyan-300")
                    ui.label(
                        "By peering directly with local Access ISPs at IXPs or hosting edge CDN caches near users, "
                        "content providers bypass Tier-1/2 transit fees and deliver minimal round-trip times (RTT)."
                    ).classes("text-[#b5b0a4]")

                with ui.column().classes("p-3 rounded-lg bg-[#201f1d] border border-[rgba(6,182,212,0.25)] gap-1"):
                    ui.label("Quality of Service (QoS) Control").classes("font-bold text-cyan-300")
                    ui.label(
                        "User traffic is routed almost entirely across the provider's private, controlled fiber network, "
                        "avoiding congestion, packet loss, and jitter in the public Internet."
                    ).classes("text-[#b5b0a4]")
