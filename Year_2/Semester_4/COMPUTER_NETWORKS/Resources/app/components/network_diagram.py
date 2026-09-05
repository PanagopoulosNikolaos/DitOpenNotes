"""Interactive SVG Network Topology visualizer component."""

from nicegui import ui
from models.scenario import NetworkScenario, TopologyNode, TopologyLink


def generateSvgTopology(scenario: NetworkScenario) -> str:
    """Generates standalone interactive SVG markup for the scenario topology.

    Args:
        scenario (NetworkScenario): The scenario containing topology nodes and links.

    Returns:
        str: Valid SVG markup string.
    """
    if not scenario.nodes:
        return ""

    # Calculate bounding box with padding
    xs = [n.x for n in scenario.nodes]
    ys = [n.y for n in scenario.nodes]
    min_x, max_x = min(xs) - 80, max(xs) + 100
    min_y, max_y = min(ys) - 60, max(ys) + 80
    width = max(800, max_x - min_x)
    height = max(400, max_y - min_y)

    svg_parts = [
        f'<svg viewBox="{min_x} {min_y} {width} {height}" class="w-full h-auto" xmlns="http://www.w3.org/2000/svg">',
        "<defs>",
        '  <filter id="node-glow" x="-20%" y="-20%" width="140%" height="140%">',
        '    <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.6"/>',
        '    <feDropShadow dx="0" dy="0" stdDeviation="8" flood-color="#e06b3a" flood-opacity="0.3"/>',
        "  </filter>",
        '  <linearGradient id="link-grad" x1="0%" y1="0%" x2="100%" y2="100%">',
        '    <stop offset="0%" stop-color="#e06b3a" stop-opacity="0.8"/>',
        '    <stop offset="100%" stop-color="#f59e0b" stop-opacity="0.8"/>',
        "  </linearGradient>",
        "</defs>",
    ]

    # Map node positions
    node_map = {n.id: n for n in scenario.nodes}

    # Render Links
    for link in scenario.links:
        src = node_map.get(link.source_id)
        tgt = node_map.get(link.target_id)
        if src and tgt:
            mid_x = (src.x + tgt.x) / 2
            mid_y = (src.y + tgt.y) / 2
            svg_parts.append(
                f'<line x1="{src.x}" y1="{src.y}" x2="{tgt.x}" y2="{tgt.y}" '
                f'stroke="url(#link-grad)" stroke-width="3" stroke-dasharray="6 3" stroke-linecap="round"/>'
            )
            # Link Label Pill
            label_text = link.label or f"{link.bandwidth_mbps:.0f}M | {link.distance_km:.0f}km"
            svg_parts.append(
                f'<rect x="{mid_x - 45}" y="{mid_y - 12}" width="90" height="24" rx="12" fill="#141413" stroke="#e06b3a" stroke-width="1"/>'
            )
            svg_parts.append(
                f'<text x="{mid_x}" y="{mid_y + 4}" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="10" font-weight="bold" fill="#fed7aa">{label_text}</text>'
            )

    # Render Nodes
    for node in scenario.nodes:
        # Determine color and icon by node type
        node_type = node.node_type.lower()
        if node_type == "router":
            border_color = "#e06b3a"
            fill_color = "#201f1d"
            type_tag = "ROUTER (L3)"
        elif node_type == "switch":
            border_color = "#4f8ec9"
            fill_color = "#201f1d"
            type_tag = "SWITCH (L2)"
        elif node_type == "server":
            border_color = "#10b981"
            fill_color = "#201f1d"
            type_tag = "SERVER"
        elif node_type == "cloud":
            border_color = "#a855f7"
            fill_color = "#201f1d"
            type_tag = "INTERNET"
        else:
            border_color = "#f59e0b"
            fill_color = "#201f1d"
            type_tag = "HOST"

        svg_parts.append(f'<g class="node-group" filter="url(#node-glow)" style="cursor: pointer;">')
        # Node container rectangle
        svg_parts.append(
            f'<rect x="{node.x - 65}" y="{node.y - 35}" width="130" height="70" rx="12" '
            f'fill="{fill_color}" stroke="{border_color}" stroke-width="2"/>'
        )
        # Type Badge
        svg_parts.append(
            f'<rect x="{node.x - 55}" y="{node.y - 30}" width="110" height="14" rx="7" fill="rgba(0,0,0,0.5)"/>'
        )
        svg_parts.append(
            f'<text x="{node.x}" y="{node.y - 20}" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="8" font-weight="bold" fill="{border_color}">{type_tag}</text>'
        )
        # Node Label
        svg_parts.append(
            f'<text x="{node.x}" y="{node.y + 3}" text-anchor="middle" font-family="Outfit, sans-serif" font-size="13" font-weight="bold" fill="#f4f1ea">{node.label}</text>'
        )
        # IP / MAC subtitle
        subtitle = node.ip_address or node.mac_address or ""
        if subtitle:
            svg_parts.append(
                f'<text x="{node.x}" y="{node.y + 22}" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="9" fill="#b5b0a4">{subtitle}</text>'
            )
        svg_parts.append("</g>")

    svg_parts.append("</svg>")
    return "\n".join(svg_parts)


def renderNetworkDiagram(scenario: NetworkScenario) -> None:
    """Renders the SVG network topology diagram container.

    Args:
        scenario (NetworkScenario): The active scenario object.

    Returns:
        None
    """
    if not scenario.nodes:
        return

    with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
        with ui.row().classes("items-center justify-between w-full border-b border-[rgba(255,255,255,0.08)] pb-3"):
            with ui.row().classes("items-center gap-2"):
                ui.html('<i class="fa-solid fa-diagram-project text-[#e06b3a] text-xl"></i>')
                with ui.column().classes("gap-0"):
                    ui.html('<h2 class="text-xl font-bold gradient-title m-0">Interactive Network Topology</h2>')
                    ui.label(f"Displaying {len(scenario.nodes)} nodes and {len(scenario.links)} transmission links").classes("text-xs text-[#b5b0a4]")

        svg_content = generateSvgTopology(scenario)
        with ui.column().classes("w-full p-4 rounded-xl bg-[#141413] border border-[rgba(255,255,255,0.06)] overflow-x-auto items-center"):
            ui.html(svg_content).classes("w-full max-w-4xl")
