"""Interactive SVG diagram canvas component for Discrete Mathematics graph & automata models."""

from nicegui import ui
from models.scenario import Scenario


def renderVisualDiagram(scenario: Scenario) -> None:
    """Renders interactive SVG canvas for graph theory, automata, and relation diagrams.

    Args:
        scenario (Scenario): Active scenario with diagram nodes, edges, or custom SVG.

    Returns:
        None
    """
    with ui.column().classes("w-full glass-panel p-6 gap-4 border border-[var(--border)]").props('id="visual-diagram-section"'):
        with ui.row().classes("w-full justify-between items-center flex-wrap gap-2 pb-2 border-b border-[var(--border)]"):
            with ui.row().classes("items-center gap-3"):
                ui.html('<i class="fa-solid fa-circle-nodes text-[var(--purple)] text-xl"></i>')
                with ui.column().classes("gap-0"):
                    ui.html('<h3 class="text-base md:text-lg font-bold text-[var(--text-1)] m-0">Διαδραστικό Διάγραμμα Δομής (Γράφημα / Αυτόματο / Σύνολα)</h3>')
                    ui.label("Οπτικοποίηση κορυφών, ακμών, καταστάσεων και μεταβάσεων με δυνατότητα πλοήγησης.").classes("text-xs text-[var(--text-3)]")

            # Diagram Controls: Zoom in, Zoom out, Reset
            with ui.row().classes("items-center gap-1.5"):
                ui.button(
                    icon="fa-solid fa-plus",
                    on_click=lambda: ui.run_javascript("if (window.zoomDiagram) window.zoomDiagram(1.2);"),
                ).props("flat dense round").classes("text-[var(--text-2)] hover:text-[var(--accent)]").tooltip("Μεγέθυνση (+)")
                ui.button(
                    icon="fa-solid fa-minus",
                    on_click=lambda: ui.run_javascript("if (window.zoomDiagram) window.zoomDiagram(0.8);"),
                ).props("flat dense round").classes("text-[var(--text-2)] hover:text-[var(--accent)]").tooltip("Σμίκρυνση (-)")
                ui.button(
                    icon="fa-solid fa-arrows-rotate",
                    on_click=lambda: ui.run_javascript("if (window.resetDiagram) window.resetDiagram();"),
                ).props("flat dense round").classes("text-[var(--text-2)] hover:text-[var(--accent)]").tooltip("Επαναφορά (Reset)")

        # SVG Container
        svg_content = scenario.diagram_svg_custom
        if not svg_content:
            # Build SVG from nodes and edges
            nodes = scenario.diagram_nodes
            edges = scenario.diagram_edges
            edge_elements = []
            for e in edges:
                if e.path_d:
                    d = e.path_d
                else:
                    s_node = next((n for n in nodes if n.id == e.source_id), None)
                    t_node = next((n for n in nodes if n.id == e.target_id), None)
                    if s_node and t_node:
                        d = f"M {s_node.x} {s_node.y} L {t_node.x} {t_node.y}"
                    else:
                        continue
                col = e.color or "var(--border-accent)"
                edge_elements.append(
                    f'<path d="{d}" stroke="{col}" stroke-width="2.5" fill="none" opacity="0.85" />'
                )
                if e.label:
                    edge_elements.append(
                        f'<text fill="var(--text-2)" font-size="11" font-weight="bold"><textPath href="#{e.source_id}-{e.target_id}" startOffset="50%">{e.label}</textPath></text>'
                    )

            node_elements = []
            for n in nodes:
                is_start = n.properties.get("is_start", False)
                is_accept = n.properties.get("is_accept", False)
                fill_color = "var(--surface)"
                stroke_color = "var(--purple)"
                if is_accept:
                    stroke_color = "var(--green-ok)"
                r = 24
                accept_ring = f'<circle cx="{n.x}" cy="{n.y}" r="{r-4}" fill="none" stroke="{stroke_color}" stroke-width="1.5" />' if is_accept else ""
                start_arrow = f'<path d="M {n.x-45} {n.y} L {n.x-r-2} {n.y}" stroke="var(--accent)" stroke-width="2" marker-end="url(#arrow)" />' if is_start else ""

                node_elements.append(
                    f'<g class="diagram-node" transform="translate(0,0)">'
                    f'{start_arrow}'
                    f'<circle cx="{n.x}" cy="{n.y}" r="{r}" fill="{fill_color}" stroke="{stroke_color}" stroke-width="2.5" />'
                    f'{accept_ring}'
                    f'<text x="{n.x}" y="{n.y+4}" text-anchor="middle" fill="var(--text-1)" font-size="12" font-weight="bold" font-family="JetBrains Mono, monospace">{n.label}</text>'
                    f'</g>'
                )

            svg_content = f"""
            <svg id="dm-svg-diagram" viewBox="0 0 800 320" class="w-full h-72 rounded-xl bg-[var(--svg-canvas-bg)] border border-[var(--border)] select-none">
                <defs>
                    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                        <path d="M 0 0 L 10 5 L 0 10 z" fill="var(--accent)"/>
                    </marker>
                </defs>
                <g id="dm-diagram-group" transform="matrix(1 0 0 1 0 0)">
                    {''.join(edge_elements)}
                    {''.join(node_elements)}
                </g>
            </svg>
            """

        ui.html(svg_content).classes("w-full overflow-hidden")

        # Diagram pan & zoom script
        ui.run_javascript("""
        (function() {
            const svg = document.getElementById('dm-svg-diagram');
            const g = document.getElementById('dm-diagram-group');
            if (!svg || !g) return;

            let scale = 1;
            let pointX = 0;
            let pointY = 0;
            let start = { x: 0, y: 0 };
            let isPanning = false;

            function setTransform() {
                g.setAttribute('transform', `translate(${pointX}, ${pointY}) scale(${scale})`);
            }

            window.zoomDiagram = function(factor) {
                scale *= factor;
                scale = Math.min(Math.max(0.5, scale), 3.0);
                setTransform();
            };

            window.resetDiagram = function() {
                scale = 1;
                pointX = 0;
                pointY = 0;
                setTransform();
            };

            svg.onmousedown = function(e) {
                e.preventDefault();
                start = { x: e.clientX - pointX, y: e.clientY - pointY };
                isPanning = true;
                svg.style.cursor = 'grabbing';
            };

            svg.onmousemove = function(e) {
                if (!isPanning) return;
                pointX = e.clientX - start.x;
                pointY = e.clientY - start.y;
                setTransform();
            };

            svg.onmouseup = function() {
                isPanning = false;
                svg.style.cursor = 'default';
            };

            svg.onmouseleave = function() {
                isPanning = false;
                svg.style.cursor = 'default';
            };

            svg.onwheel = function(e) {
                e.preventDefault();
                const xs = (e.clientX - pointX) / scale;
                const ys = (e.clientY - pointY) / scale;
                const delta = -e.deltaY;
                if (delta > 0) scale *= 1.1;
                else scale /= 1.1;
                scale = Math.min(Math.max(0.5, scale), 3.0);
                pointX = e.clientX - xs * scale;
                pointY = e.clientY - ys * scale;
                setTransform();
            };
        })();
        """)
