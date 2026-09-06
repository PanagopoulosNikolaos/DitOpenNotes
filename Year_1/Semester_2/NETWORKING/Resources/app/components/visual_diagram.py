"""Interactive SVG diagram viewer with pan, zoom, reset, and detail toggle.

Renders the scenario-specific visual model (VLSM allocation map, network
topology with link costs, fragmentation path) from pre-calculated node
coordinates and connection paths, adapting seamlessly to both themes.
"""

import json
from nicegui import ui
from models.scenario import Scenario


def renderVisualDiagram(scenario: Scenario) -> None:
    """Renders the interactive SVG diagram for the given scenario.

    Args:
        scenario (Scenario): The active scenario containing diagram elements.

    Returns:
        None
    """
    nodes_data = [
        {
            "id": n.id,
            "label": n.label,
            "x": n.x,
            "y": n.y,
            "w": n.w,
            "details": n.details,
            "highlight": n.highlight,
        }
        for n in scenario.diagram_nodes
    ]
    edges_data = [
        {
            "path": e.path,
            "label": e.label,
            "lx": e.lx,
            "ly": e.ly,
            "dashed": e.dashed,
            "marker": e.marker,
        }
        for e in scenario.diagram_edges
    ]

    # Single quotes are escaped so the JSON survives inside data-attributes
    nodes_json = json.dumps(nodes_data).replace("'", "&#39;")
    edges_json = json.dumps(edges_data).replace("'", "&#39;")

    with ui.column().classes("w-full glass-panel gap-4 print-section print-diagram"):
        # Header with controls
        with ui.row().classes("w-full justify-between items-center flex-wrap gap-4 border-b border-[var(--border)] pb-4"):
            with ui.column().classes("gap-1"):
                with ui.row().classes("items-center gap-2"):
                    ui.html('<i class="fa-solid fa-sitemap text-[var(--accent)] text-xl no-print"></i>')
                    ui.html(f'<h2 class="text-xl font-bold text-[var(--text-1)] m-0">{scenario.diagram_title}</h2>')
                ui.label(scenario.diagram_note).classes("text-xs text-[var(--text-2)] no-print")

            # Diagram control buttons (whitelisted interactions)
            with ui.row().classes("items-center gap-2 flex-wrap text-xs no-print"):
                ui.html(
                    """
                    <button onclick="zoomExam(1.2)" class="btn-secondary" title="Μεγέθυνση"><i class="fa-solid fa-magnifying-glass-plus"></i></button>
                    <button onclick="zoomExam(0.8)" class="btn-secondary" title="Σμίκρυνση"><i class="fa-solid fa-magnifying-glass-minus"></i></button>
                    <button onclick="resetExamZoom()" class="btn-secondary"><i class="fa-solid fa-arrows-to-dot"></i> Επαναφορά</button>
                    <button onclick="toggleExamDetails()" id="toggle-details-btn" class="btn-secondary"><i class="fa-solid fa-eye"></i> Απόκρυψη Λεπτομερειών</button>
                    """,
                    sanitize=False,
                )

        # Diagram container with legend overlay
        with ui.element("div").classes("relative w-full rounded-2xl overflow-hidden border border-[var(--border-accent)] shadow-inner bg-[var(--svg-canvas-bg)]"):
            ui.html(
                """
                <div class="absolute top-3 left-3 z-10 bg-[var(--header-bg)] backdrop-blur-md text-[var(--text-1)] p-2.5 rounded-xl border border-[var(--border)] text-xs flex flex-wrap items-center gap-3 no-print shadow-lg">
                    <span class="flex items-center gap-1.5"><i class="fa-solid fa-cube text-blue-500"></i> Κόμβος / Δίκτυο</span>
                    <span class="flex items-center gap-1.5"><span class="w-3 h-3 rounded-sm border-2 border-[var(--accent)]"></span> Επισημασμένο (κρίσιμο)</span>
                    <span class="flex items-center gap-1.5"><i class="fa-solid fa-tag text-amber-500"></i> Ετικέτα ζεύξης / εύρους</span>
                </div>
                <div class="absolute bottom-3 right-3 z-10 bg-[var(--header-bg)] backdrop-blur-sm text-[var(--text-3)] px-3 py-1.5 rounded-lg text-xs flex items-center gap-2 border border-[var(--border)] no-print shadow-md">
                    <i class="fa-solid fa-hand-pointer text-[var(--accent)]"></i> Drag για μετακίνηση • Scroll για Zoom
                </div>
                """
            )

            # SVG canvas storing diagram data in data-attributes with inline handlers
            ui.html(
                f"""
                <svg id="exam-svg-canvas" class="w-full h-[560px]" viewBox="0 0 1200 640" preserveAspectRatio="xMidYMid meet"
                     onmousedown="startExamDrag(event)" onwheel="handleExamWheel(event)"
                     data-nodes='{nodes_json}' data-edges='{edges_json}' data-show-details="true">
                    <defs>
                        <marker id="arrow" markerWidth="12" markerHeight="10" refX="10" refY="5" orient="auto">
                            <path d="M 0,1 L 10,5 L 0,9 z" class="svg-arrow-path"/>
                        </marker>
                    </defs>
                    <g id="diagram-content" transform="translate(0,0) scale(1)"></g>
                </svg>
                """
            )


# Global head script: builds the diagram from data attributes and manages
# pan, zoom, reset, and the detail toggle. Re-rendered on theme switches.
ui.add_head_html(
    """
    <script>
        let examView = { x: 0, y: 0, scale: 1 };
        let examDragging = false;
        let examLastMouse = { x: 0, y: 0 };

        function svgPoint(svg, clientX, clientY) {
            const pt = svg.createSVGPoint();
            pt.x = clientX;
            pt.y = clientY;
            return pt.matrixTransform(svg.getScreenCTM().inverse());
        }

        function applyExamTransform() {
            const g = document.getElementById('diagram-content');
            if (g) {
                g.setAttribute('transform', `translate(${examView.x},${examView.y}) scale(${examView.scale})`);
            }
        }

        function initExamDiagram() {
            const svg = document.getElementById('exam-svg-canvas');
            if (!svg) return;
            const nodes = JSON.parse(svg.getAttribute('data-nodes') || '[]');
            const edges = JSON.parse(svg.getAttribute('data-edges') || '[]');
            const showDetails = svg.getAttribute('data-show-details') !== 'false';
            const g = svg.querySelector('#diagram-content');
            if (!g) return;
            g.innerHTML = '';
            const NS = 'http://www.w3.org/2000/svg';

            // Edges render below nodes so lines never cover node content
            edges.forEach(e => {
                const pathEl = document.createElementNS(NS, 'path');
                pathEl.setAttribute('d', e.path);
                pathEl.setAttribute('class', 'svg-edge-line' + (e.dashed ? ' svg-edge-dashed' : ''));
                if (e.marker) {
                    pathEl.setAttribute('marker-end', 'url(#' + e.marker + ')');
                }
                g.appendChild(pathEl);
                if (e.label) {
                    const w = e.label.length * 7.2 + 12;
                    const rect = document.createElementNS(NS, 'rect');
                    rect.setAttribute('x', e.lx - w / 2);
                    rect.setAttribute('y', e.ly - 10);
                    rect.setAttribute('width', w);
                    rect.setAttribute('height', 20);
                    rect.setAttribute('rx', 5);
                    rect.setAttribute('class', 'svg-edge-label-bg');
                    g.appendChild(rect);
                    const text = document.createElementNS(NS, 'text');
                    text.setAttribute('x', e.lx);
                    text.setAttribute('y', e.ly + 4);
                    text.setAttribute('text-anchor', 'middle');
                    text.setAttribute('class', 'svg-edge-label');
                    text.textContent = e.label;
                    g.appendChild(text);
                }
            });

            // Nodes: header bar + optional detail lines
            nodes.forEach(n => {
                const grp = document.createElementNS(NS, 'g');
                grp.setAttribute('class', 'svg-node');
                const headerH = 26;
                const lineH = 15;
                const pad = 7;
                const details = (showDetails && n.details) ? n.details : [];
                const h = headerH + details.length * lineH + pad;

                const rect = document.createElementNS(NS, 'rect');
                rect.setAttribute('x', n.x);
                rect.setAttribute('y', n.y);
                rect.setAttribute('width', n.w);
                rect.setAttribute('height', h);
                rect.setAttribute('rx', 8);
                rect.setAttribute('class', 'svg-node-rect' + (n.highlight ? ' svg-node-hl' : ''));
                grp.appendChild(rect);

                const header = document.createElementNS(NS, 'rect');
                header.setAttribute('x', n.x);
                header.setAttribute('y', n.y);
                header.setAttribute('width', n.w);
                header.setAttribute('height', headerH);
                header.setAttribute('rx', 8);
                header.setAttribute('class', 'svg-node-header');
                grp.appendChild(header);

                const title = document.createElementNS(NS, 'text');
                title.setAttribute('x', n.x + n.w / 2);
                title.setAttribute('y', n.y + 17);
                title.setAttribute('text-anchor', 'middle');
                title.setAttribute('class', 'svg-node-title');
                title.textContent = n.label;
                grp.appendChild(title);

                details.forEach((d, i) => {
                    const line = document.createElementNS(NS, 'text');
                    line.setAttribute('x', n.x + 9);
                    line.setAttribute('y', n.y + headerH + 13 + i * lineH);
                    line.setAttribute('class', 'svg-node-detail');
                    line.textContent = d;
                    grp.appendChild(line);
                });

                g.appendChild(grp);
            });
            applyExamTransform();
        }

        function startExamDrag(evt) {
            examDragging = true;
            const svg = document.getElementById('exam-svg-canvas');
            examLastMouse = svgPoint(svg, evt.clientX, evt.clientY);
            const stop = () => { examDragging = false; };
            const move = (evt2) => {
                if (!examDragging) return;
                const svg = document.getElementById('exam-svg-canvas');
                const pt = svgPoint(svg, evt2.clientX, evt2.clientY);
                examView.x += (pt.x - examLastMouse.x) * examView.scale;
                examView.y += (pt.y - examLastMouse.y) * examView.scale;
                examLastMouse = pt;
                applyExamTransform();
            };
            window.addEventListener('mousemove', move);
            window.addEventListener('mouseup', () => { examDragging = false; window.removeEventListener('mousemove', move); }, { once: true });
            evt.preventDefault();
        }

        function handleExamWheel(evt) {
            zoomExam(evt.deltaY < 0 ? 1.12 : 0.89);
            evt.preventDefault();
        }

        function zoomExam(factor) {
            const svg = document.getElementById('exam-svg-canvas');
            if (!svg) return;
            const centerX = 600, centerY = 320;
            const newScale = Math.min(3.2, Math.max(0.35, examView.scale * factor));
            const ratio = newScale / examView.scale;
            examView.x = centerX - (centerX - examView.x) * ratio;
            examView.y = centerY - (centerY - examView.y) * ratio;
            examView.scale = newScale;
            applyExamTransform();
        }

        function resetExamZoom() {
            examView = { x: 0, y: 0, scale: 1 };
            applyExamTransform();
        }

        function toggleExamDetails() {
            const svg = document.getElementById('exam-svg-canvas');
            const btn = document.getElementById('toggle-details-btn');
            if (!svg) return;
            const show = svg.getAttribute('data-show-details') !== 'false';
            svg.setAttribute('data-show-details', show ? 'false' : 'true');
            if (btn) {
                btn.innerHTML = show
                    ? '<i class="fa-solid fa-eye-slash"></i> Εμφάνιση Λεπτομερειών'
                    : '<i class="fa-solid fa-eye"></i> Απόκρυψη Λεπτομερειών';
            }
            initExamDiagram();
        }

        document.addEventListener('DOMContentLoaded', () => {
            initExamDiagram();
        });
        setTimeout(initExamDiagram, 100);
    </script>
    """,
    shared=True,
)
