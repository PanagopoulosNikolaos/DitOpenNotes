"""Interactive SVG ER diagram viewer component with pan, zoom, and attribute toggling."""

import json
from nicegui import ui
from models.scenario import Scenario


def renderERDiagram(scenario: Scenario) -> None:
    """Renders the interactive SVG ER diagram for the given scenario.

    Args:
        scenario (Scenario): The active scenario containing ER tables and edges.

    Returns:
        None
    """
    tables_data = [
        {
            "id": t.id,
            "label": t.label,
            "x": t.x,
            "y": t.y,
            "attrs": [{"name": a.name, "pk": a.pk, "fk": a.fk} for a in t.attrs],
        }
        for t in scenario.er_tables
    ]

    edges_data = [
        {
            "path": e.path,
            "markerStart": e.marker_start,
            "markerEnd": e.marker_end,
            "label": e.label,
            "lx": e.lx,
            "ly": e.ly,
        }
        for e in scenario.er_edges
    ]

    tables_json = json.dumps(tables_data).replace("'", "&#39;")
    edges_json = json.dumps(edges_data).replace("'", "&#39;")

    with ui.column().classes("w-full glass-panel gap-4 print-section print-er-diagram"):
        # Header with controls
        with ui.row().classes("w-full justify-between items-center flex-wrap gap-4 border-b border-[rgba(255,255,255,0.08)] pb-4"):
            with ui.column().classes("gap-1"):
                with ui.row().classes("items-center gap-2"):
                    ui.html('<i class="fa-solid fa-diagram-project text-[#e06b3a] text-xl no-print"></i>')
                    ui.html('<h2 class="text-xl font-bold text-[#f4f1ea] m-0">Σχεδίαση Διαγράμματος Ε-Ρ (Crow\'s Foot / Relational Schema)</h2>')
                ui.label(
                    "Πλήρης γραφική αναπαράσταση της Βάσης Δεδομένων με χρήση Crow's Foot Notation (Zoom, Pan, Dragging)."
                ).classes("text-xs text-[#b5b0a4] no-print")

            # Control buttons
            with ui.row().classes("items-center gap-2 flex-wrap text-xs no-print"):
                ui.html(
                    """
                    <button onclick="zoomER(1.2)" class="btn-secondary" title="Μεγέθυνση"><i class="fa-solid fa-magnifying-glass-plus"></i></button>
                    <button onclick="zoomER(0.8)" class="btn-secondary" title="Σμίκρυνση"><i class="fa-solid fa-magnifying-glass-minus"></i></button>
                    <button onclick="resetERZoom()" class="btn-secondary"><i class="fa-solid fa-arrows-to-dot"></i> Επαναφορά</button>
                    <button onclick="toggleERAttributes()" id="toggle-attr-btn" class="btn-secondary"><i class="fa-solid fa-eye"></i> Απόκρυψη Γνωρισμάτων</button>
                    """,
                    sanitize=False,
                )

        # Diagram Container
        with ui.element("div").classes("relative w-full rounded-2xl overflow-hidden border border-[rgba(224,107,58,0.3)] shadow-inner bg-[#121211]"):
            # Top Legend Overlay
            ui.html(
                """
                <div class="absolute top-3 left-3 z-10 bg-[#171615]/85 backdrop-blur-md text-[#f4f1ea] p-2.5 rounded-xl border border-[rgba(255,255,255,0.08)] text-xs flex flex-wrap gap-3">
                    <span class="flex items-center gap-1.5"><i class="fa-solid fa-table text-blue-400"></i> Πίνακας</span>
                    <span class="flex items-center gap-1.5"><span class="w-3 h-3 bg-[#e06b3a] rounded-sm"></span> PK</span>
                    <span class="flex items-center gap-1.5"><span class="w-3 h-3 bg-slate-400 rounded-sm"></span> FK</span>
                    <span class="flex items-center gap-1.5"><i class="fa-solid fa-code-branch text-[#f59e0b]"></i> Σχέσεις</span>
                </div>
                <div class="absolute bottom-3 right-3 z-10 bg-[#171615]/85 text-[#78756d] px-3 py-1.5 rounded-lg text-xs flex items-center gap-2 border border-[rgba(255,255,255,0.06)] no-print">
                    <i class="fa-solid fa-hand-pointer text-[#e06b3a]"></i> Drag για μετακίνηση • Scroll για Zoom
                </div>
                """
            )

            # SVG Canvas storing diagram data in data-attributes with inline event handlers
            ui.html(
                f"""
                <svg id="er-svg-canvas" class="w-full h-[620px]" viewBox="0 0 1200 800" preserveAspectRatio="xMidYMid meet"
                     onmousedown="startERDrag(event)" onwheel="handleERWheel(event)"
                     data-tables='{tables_json}' data-edges='{edges_json}'>
                    <defs>
                        <!-- End One Marker -->
                        <marker id="end-one" markerWidth="16" markerHeight="16" refX="16" refY="8" orient="auto">
                            <line x1="10" y1="2" x2="10" y2="14" stroke="#e06b3a" stroke-width="2" />
                            <line x1="16" y1="2" x2="16" y2="14" stroke="#e06b3a" stroke-width="2" />
                        </marker>
                        <!-- Start One Marker -->
                        <marker id="start-one" markerWidth="16" markerHeight="16" refX="0" refY="8" orient="auto">
                            <line x1="0" y1="2" x2="0" y2="14" stroke="#e06b3a" stroke-width="2" />
                            <line x1="6" y1="2" x2="6" y2="14" stroke="#e06b3a" stroke-width="2" />
                        </marker>
                        <!-- End Many Marker -->
                        <marker id="end-many" markerWidth="16" markerHeight="16" refX="16" refY="8" orient="auto">
                            <line x1="8" y1="2" x2="8" y2="14" stroke="#f59e0b" stroke-width="2" />
                            <path d="M16,8 L6,2 M16,8 L6,14 M16,8 L6,8" stroke="#f59e0b" stroke-width="2" fill="none" />
                        </marker>
                        <!-- Start Many Marker -->
                        <marker id="start-many" markerWidth="16" markerHeight="16" refX="0" refY="8" orient="auto">
                            <line x1="8" y1="2" x2="8" y2="14" stroke="#f59e0b" stroke-width="2" />
                            <path d="M0,8 L10,2 M0,8 L10,14 M0,8 L10,8" stroke="#f59e0b" stroke-width="2" fill="none" />
                        </marker>
                    </defs>
                    <g id="er-svg-viewport"></g>
                </svg>
                """,
                sanitize=False,
            )


# Register global head script
ui.add_head_html(
    """
    <script>
        let showAttributes = true;
        let zoomScale = 1;
        let panX = 0, panY = 0;
        let isDragging = false;
        let startX = 0, startY = 0;

        const TABLE_WIDTH = 260;
        const ROW_HEIGHT = 28;
        const HEADER_HEIGHT = 40;

        function startERDrag(e) {
            isDragging = true;
            startX = e.clientX - panX;
            startY = e.clientY - panY;
            const svg = document.getElementById('er-svg-canvas');
            if (svg) svg.style.cursor = 'grabbing';
        }

        function handleERWheel(e) {
            e.preventDefault();
            const zoomFactor = e.deltaY < 0 ? 1.1 : 0.9;
            zoomER(zoomFactor);
        }

        window.addEventListener('mousemove', e => {
            if (!isDragging) return;
            panX = e.clientX - startX;
            panY = e.clientY - startY;
            updateTransform();
        });

        window.addEventListener('mouseup', () => {
            if (isDragging) {
                isDragging = false;
                const svg = document.getElementById('er-svg-canvas');
                if (svg) svg.style.cursor = 'grab';
            }
        });

        function initERDiagram() {
            const svgCanvas = document.getElementById('er-svg-canvas');
            const viewport = document.getElementById('er-svg-viewport');
            if (!svgCanvas || !viewport) return;

            const tablesRaw = svgCanvas.getAttribute('data-tables');
            const edgesRaw = svgCanvas.getAttribute('data-edges');
            if (!tablesRaw || !edgesRaw) return;

            const erTables = JSON.parse(tablesRaw);
            const erEdges = JSON.parse(edgesRaw);

            viewport.innerHTML = '';

            erTables.forEach(t => {
                t.h = showAttributes ? (HEADER_HEIGHT + (t.attrs.length * ROW_HEIGHT) + 8) : HEADER_HEIGHT;
                t.cx = t.x + TABLE_WIDTH / 2;
                t.bottom = t.y + t.h;
                t.right = t.x + TABLE_WIDTH;
            });

            // Draw Edges
            erEdges.forEach(edge => {
                const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
                path.setAttribute('d', edge.path);
                path.setAttribute('fill', 'none');
                path.setAttribute('stroke', '#b5b0a4');
                path.setAttribute('stroke-width', '2');
                path.setAttribute('marker-start', `url(#${edge.markerStart})`);
                path.setAttribute('marker-end', `url(#${edge.markerEnd})`);
                viewport.appendChild(path);

                if (edge.label) {
                    const textWidth = edge.label.length * 7.5;
                    const rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
                    rect.setAttribute('x', edge.lx - textWidth / 2 - 8);
                    rect.setAttribute('y', edge.ly - 10);
                    rect.setAttribute('width', textWidth + 16);
                    rect.setAttribute('height', '20');
                    rect.setAttribute('fill', '#141413');
                    rect.setAttribute('stroke', 'rgba(224,107,58,0.4)');
                    rect.setAttribute('stroke-width', '1');
                    rect.setAttribute('rx', '6');
                    viewport.appendChild(rect);

                    const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
                    text.setAttribute('x', edge.lx);
                    text.setAttribute('y', edge.ly + 4);
                    text.setAttribute('fill', '#f4f1ea');
                    text.setAttribute('font-size', '11px');
                    text.setAttribute('font-weight', '600');
                    text.setAttribute('text-anchor', 'middle');
                    text.textContent = edge.label;
                    viewport.appendChild(text);
                }
            });

            // Draw Tables
            erTables.forEach(tbl => {
                const g = document.createElementNS('http://www.w3.org/2000/svg', 'g');
                g.setAttribute('class', 'er-node');
                g.setAttribute('transform', `translate(${tbl.x}, ${tbl.y})`);

                // Main Container Rect
                const bgRect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
                bgRect.setAttribute('x', '0');
                bgRect.setAttribute('y', '0');
                bgRect.setAttribute('width', TABLE_WIDTH);
                bgRect.setAttribute('height', tbl.h);
                bgRect.setAttribute('rx', '10');
                bgRect.setAttribute('fill', '#1c1b1a');
                bgRect.setAttribute('stroke', 'rgba(255, 255, 255, 0.12)');
                bgRect.setAttribute('stroke-width', '1.5');
                g.appendChild(bgRect);

                // Header Gradient Rect
                const headerRect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
                headerRect.setAttribute('x', '0');
                headerRect.setAttribute('y', '0');
                headerRect.setAttribute('width', TABLE_WIDTH);
                headerRect.setAttribute('height', HEADER_HEIGHT);
                headerRect.setAttribute('rx', '10');
                headerRect.setAttribute('fill', '#26211e');
                headerRect.setAttribute('stroke', 'rgba(224, 107, 58, 0.4)');
                headerRect.setAttribute('stroke-width', '1');
                g.appendChild(headerRect);

                if (showAttributes) {
                    const headerSquare = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
                    headerSquare.setAttribute('x', '0');
                    headerSquare.setAttribute('y', HEADER_HEIGHT - 8);
                    headerSquare.setAttribute('width', TABLE_WIDTH);
                    headerSquare.setAttribute('height', '8');
                    headerSquare.setAttribute('fill', '#26211e');
                    g.appendChild(headerSquare);
                }

                // Table Title
                const titleText = document.createElementNS('http://www.w3.org/2000/svg', 'text');
                titleText.setAttribute('x', TABLE_WIDTH / 2);
                titleText.setAttribute('y', HEADER_HEIGHT / 2 + 1);
                titleText.setAttribute('fill', '#f4f1ea');
                titleText.setAttribute('font-size', '13px');
                titleText.setAttribute('font-weight', '800');
                titleText.setAttribute('text-anchor', 'middle');
                titleText.setAttribute('dominant-baseline', 'middle');
                titleText.textContent = tbl.label;
                g.appendChild(titleText);

                // Table Attributes List
                if (showAttributes) {
                    tbl.attrs.forEach((attr, idx) => {
                        const rowY = HEADER_HEIGHT + (idx * ROW_HEIGHT);

                        if (idx % 2 === 0) {
                            const rowBg = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
                            rowBg.setAttribute('x', '1');
                            rowBg.setAttribute('y', rowY);
                            rowBg.setAttribute('width', TABLE_WIDTH - 2);
                            rowBg.setAttribute('height', ROW_HEIGHT);
                            rowBg.setAttribute('fill', 'rgba(255, 255, 255, 0.025)');
                            g.appendChild(rowBg);
                        }

                        // PK / FK Indicator
                        if (attr.pk || attr.fk) {
                            const keyTag = document.createElementNS('http://www.w3.org/2000/svg', 'text');
                            keyTag.setAttribute('x', '14');
                            keyTag.setAttribute('y', rowY + 18);
                            keyTag.setAttribute('fill', attr.pk ? '#e06b3a' : '#78756d');
                            keyTag.setAttribute('font-size', '11px');
                            keyTag.setAttribute('font-weight', '800');
                            keyTag.textContent = (attr.pk && attr.fk) ? 'PK, FK' : (attr.pk ? 'PK' : 'FK');
                            g.appendChild(keyTag);
                        }

                        // Attribute Name
                        const attrText = document.createElementNS('http://www.w3.org/2000/svg', 'text');
                        attrText.setAttribute('x', '65');
                        attrText.setAttribute('y', rowY + 18);
                        attrText.setAttribute('fill', attr.pk ? '#f4f1ea' : '#b5b0a4');
                        attrText.setAttribute('font-size', '12px');
                        if (attr.pk) {
                            attrText.setAttribute('font-weight', '700');
                        }
                        attrText.textContent = attr.name;
                        g.appendChild(attrText);
                    });
                }

                viewport.appendChild(g);
            });

            updateTransform();
        }

        function updateTransform() {
            const viewport = document.getElementById('er-svg-viewport');
            if (viewport) {
                viewport.setAttribute('transform', `translate(${panX}, ${panY}) scale(${zoomScale})`);
            }
        }

        function zoomER(factor) {
            zoomScale = Math.min(Math.max(0.4, zoomScale * factor), 2.5);
            updateTransform();
        }

        function resetERZoom() {
            zoomScale = 1;
            panX = 0;
            panY = 0;
            updateTransform();
        }

        function toggleERAttributes() {
            showAttributes = !showAttributes;
            const btn = document.getElementById('toggle-attr-btn');
            if (btn) {
                btn.innerHTML = showAttributes ?
                    '<i class="fa-solid fa-eye"></i> Απόκρυψη Γνωρισμάτων' :
                    '<i class="fa-solid fa-eye-slash"></i> Εμφάνιση Γνωρισμάτων';
            }
            initERDiagram();
        }

        document.addEventListener('DOMContentLoaded', initERDiagram);
        setTimeout(initERDiagram, 100);
    </script>
    """,
    shared=True,
)
