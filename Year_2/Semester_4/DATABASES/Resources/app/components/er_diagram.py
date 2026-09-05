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
        with ui.row().classes("w-full justify-between items-center flex-wrap gap-4 border-b border-[var(--border)] pb-4"):
            with ui.column().classes("gap-1"):
                with ui.row().classes("items-center gap-2"):
                    ui.html('<i class="fa-solid fa-diagram-project text-[var(--accent)] text-xl no-print"></i>')
                    ui.html('<h2 class="text-xl font-bold text-[var(--text-1)] m-0">Σχεδίαση Διαγράμματος Ε-Ρ (Crow\'s Foot / Relational Schema)</h2>')
                ui.label(
                    "Πλήρης γραφική αναπαράσταση της Βάσης Δεδομένων με χρήση Crow's Foot Notation (Zoom, Pan, Dragging)."
                ).classes("text-xs text-[var(--text-2)] no-print")

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
        with ui.element("div").classes("relative w-full rounded-2xl overflow-hidden border border-[var(--border-accent)] shadow-inner bg-[var(--svg-canvas-bg)]"):
            # Top Legend Overlay
            ui.html(
                """
                <div class="absolute top-3 left-3 z-10 bg-[var(--header-bg)] backdrop-blur-md text-[var(--text-1)] p-2.5 rounded-xl border border-[var(--border)] text-xs flex flex-wrap items-center gap-3 no-print shadow-lg">
                    <span class="flex items-center gap-1.5"><i class="fa-solid fa-table text-blue-500"></i> Πίνακας</span>
                    <span class="flex items-center gap-1.5"><span class="w-3 h-3 bg-[#e06b3a] rounded-sm"></span> PK</span>
                    <span class="flex items-center gap-1.5"><span class="w-3 h-3 bg-slate-400 rounded-sm"></span> FK</span>
                    <span class="h-3 w-px bg-[var(--border)]"></span>
                    <span class="flex items-center gap-1 text-[11px] font-mono text-[#e06b3a] font-bold" title="Ακριβώς Ένα (Υποχρεωτικό 1)">|| 1..1</span>
                    <span class="flex items-center gap-1 text-[11px] font-mono text-[#e06b3a] font-bold" title="Μηδέν ή Ένα (Προαιρετικό 1)">O| 0..1</span>
                    <span class="flex items-center gap-1 text-[11px] font-mono text-[#f59e0b] font-bold" title="Ένα ή Πολλά (Υποχρεωτικά Πολλά)">&gt;| 1..N</span>
                    <span class="flex items-center gap-1 text-[11px] font-mono text-[#f59e0b] font-bold" title="Μηδέν ή Πολλά (Προαιρετικά Πολλά)">&gt;O 0..N</span>
                </div>
                <div class="absolute bottom-3 right-3 z-10 bg-[var(--header-bg)] backdrop-blur-sm text-[var(--text-3)] px-3 py-1.5 rounded-lg text-xs flex items-center gap-2 border border-[var(--border)] no-print shadow-md">
                    <i class="fa-solid fa-hand-pointer text-[var(--accent)]"></i> Drag για μετακίνηση • Scroll για Zoom
                </div>
                """
            )

            # SVG Canvas storing diagram data in data-attributes with inline event handlers
            ui.html(
                f"""
                <svg id="er-svg-canvas" class="w-full h-[670px]" viewBox="0 0 1200 1100" preserveAspectRatio="xMidYMid meet"
                     onmousedown="startERDrag(event)" onwheel="handleERWheel(event)"
                     data-tables='{tables_json}' data-edges='{edges_json}'>
                    <defs>
                        <!-- 1..1 (Mandatory One): || -->
                        <marker id="start-one-mandatory" markerWidth="20" markerHeight="16" refX="0" refY="8" orient="auto">
                            <line x1="2" y1="2" x2="2" y2="14" stroke="#e06b3a" stroke-width="2" />
                            <line x1="8" y1="2" x2="8" y2="14" stroke="#e06b3a" stroke-width="2" />
                        </marker>
                        <marker id="start-one" markerWidth="20" markerHeight="16" refX="0" refY="8" orient="auto">
                            <line x1="2" y1="2" x2="2" y2="14" stroke="#e06b3a" stroke-width="2" />
                            <line x1="8" y1="2" x2="8" y2="14" stroke="#e06b3a" stroke-width="2" />
                        </marker>
                        <marker id="end-one-mandatory" markerWidth="20" markerHeight="16" refX="20" refY="8" orient="auto">
                            <line x1="18" y1="2" x2="18" y2="14" stroke="#e06b3a" stroke-width="2" />
                            <line x1="12" y1="2" x2="12" y2="14" stroke="#e06b3a" stroke-width="2" />
                        </marker>
                        <marker id="end-one" markerWidth="20" markerHeight="16" refX="20" refY="8" orient="auto">
                            <line x1="18" y1="2" x2="18" y2="14" stroke="#e06b3a" stroke-width="2" />
                            <line x1="12" y1="2" x2="12" y2="14" stroke="#e06b3a" stroke-width="2" />
                        </marker>

                        <!-- 0..1 (Optional One): O| / |O -->
                        <marker id="start-one-optional" markerWidth="20" markerHeight="16" refX="0" refY="8" orient="auto">
                            <line x1="2" y1="2" x2="2" y2="14" stroke="#e06b3a" stroke-width="2" />
                            <circle cx="10" cy="8" r="4" class="svg-marker-circle" fill="var(--svg-canvas-bg, #ffffff)" stroke="#e06b3a" stroke-width="2" />
                        </marker>
                        <marker id="start-zero-one" markerWidth="20" markerHeight="16" refX="0" refY="8" orient="auto">
                            <line x1="2" y1="2" x2="2" y2="14" stroke="#e06b3a" stroke-width="2" />
                            <circle cx="10" cy="8" r="4" class="svg-marker-circle" fill="var(--svg-canvas-bg, #ffffff)" stroke="#e06b3a" stroke-width="2" />
                        </marker>
                        <marker id="end-one-optional" markerWidth="20" markerHeight="16" refX="20" refY="8" orient="auto">
                            <line x1="18" y1="2" x2="18" y2="14" stroke="#e06b3a" stroke-width="2" />
                            <circle cx="10" cy="8" r="4" class="svg-marker-circle" fill="var(--svg-canvas-bg, #ffffff)" stroke="#e06b3a" stroke-width="2" />
                        </marker>
                        <marker id="end-zero-one" markerWidth="20" markerHeight="16" refX="20" refY="8" orient="auto">
                            <line x1="18" y1="2" x2="18" y2="14" stroke="#e06b3a" stroke-width="2" />
                            <circle cx="10" cy="8" r="4" class="svg-marker-circle" fill="var(--svg-canvas-bg, #ffffff)" stroke="#e06b3a" stroke-width="2" />
                        </marker>

                        <!-- 1..N (Mandatory Many): |< / >| -->
                        <marker id="start-many-mandatory" markerWidth="20" markerHeight="16" refX="0" refY="8" orient="auto">
                            <path d="M0,2 L10,8 M0,14 L10,8 M0,8 L10,8" stroke="#f59e0b" stroke-width="2" fill="none" />
                            <line x1="14" y1="2" x2="14" y2="14" stroke="#f59e0b" stroke-width="2" />
                        </marker>
                        <marker id="start-many" markerWidth="20" markerHeight="16" refX="0" refY="8" orient="auto">
                            <path d="M0,2 L10,8 M0,14 L10,8 M0,8 L10,8" stroke="#f59e0b" stroke-width="2" fill="none" />
                            <line x1="14" y1="2" x2="14" y2="14" stroke="#f59e0b" stroke-width="2" />
                        </marker>
                        <marker id="end-many-mandatory" markerWidth="20" markerHeight="16" refX="20" refY="8" orient="auto">
                            <line x1="6" y1="2" x2="6" y2="14" stroke="#f59e0b" stroke-width="2" />
                            <path d="M20,2 L10,8 M20,14 L10,8 M20,8 L10,8" stroke="#f59e0b" stroke-width="2" fill="none" />
                        </marker>
                        <marker id="end-many" markerWidth="20" markerHeight="16" refX="20" refY="8" orient="auto">
                            <line x1="6" y1="2" x2="6" y2="14" stroke="#f59e0b" stroke-width="2" />
                            <path d="M20,2 L10,8 M20,14 L10,8 M20,8 L10,8" stroke="#f59e0b" stroke-width="2" fill="none" />
                        </marker>

                        <!-- 0..N (Optional Many): O< / >O -->
                        <marker id="start-many-optional" markerWidth="24" markerHeight="16" refX="0" refY="8" orient="auto">
                            <path d="M0,2 L10,8 M0,14 L10,8 M0,8 L10,8" stroke="#f59e0b" stroke-width="2" fill="none" />
                            <circle cx="17" cy="8" r="4" class="svg-marker-circle" fill="var(--svg-canvas-bg, #ffffff)" stroke="#f59e0b" stroke-width="2" />
                        </marker>
                        <marker id="start-zero-many" markerWidth="24" markerHeight="16" refX="0" refY="8" orient="auto">
                            <path d="M0,2 L10,8 M0,14 L10,8 M0,8 L10,8" stroke="#f59e0b" stroke-width="2" fill="none" />
                            <circle cx="17" cy="8" r="4" class="svg-marker-circle" fill="var(--svg-canvas-bg, #ffffff)" stroke="#f59e0b" stroke-width="2" />
                        </marker>
                        <marker id="end-many-optional" markerWidth="24" markerHeight="16" refX="24" refY="8" orient="auto">
                            <circle cx="7" cy="8" r="4" class="svg-marker-circle" fill="var(--svg-canvas-bg, #ffffff)" stroke="#f59e0b" stroke-width="2" />
                            <path d="M24,2 L14,8 M24,14 L14,8 M24,8 L14,8" stroke="#f59e0b" stroke-width="2" fill="none" />
                        </marker>
                        <marker id="end-zero-many" markerWidth="24" markerHeight="16" refX="24" refY="8" orient="auto">
                            <circle cx="7" cy="8" r="4" class="svg-marker-circle" fill="var(--svg-canvas-bg, #ffffff)" stroke="#f59e0b" stroke-width="2" />
                            <path d="M24,2 L14,8 M24,14 L14,8 M24,8 L14,8" stroke="#f59e0b" stroke-width="2" fill="none" />
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

            // Determine active theme colors
            const isDark = document.body.classList.contains('theme-dark') || document.documentElement.getAttribute('data-theme') === 'dark';

            const nodeBg = isDark ? '#1c1b1a' : '#ffffff';
            const nodeBorder = isDark ? 'rgba(255, 255, 255, 0.12)' : 'rgba(0, 0, 0, 0.14)';
            const headerBg = isDark ? '#26211e' : '#f4f4f5';
            const headerBorder = isDark ? 'rgba(224, 107, 58, 0.4)' : 'rgba(224, 107, 58, 0.5)';
            const headerTitleColor = isDark ? '#f4f1ea' : '#18181b';
            const rowAltBg = isDark ? 'rgba(255, 255, 255, 0.025)' : 'rgba(0, 0, 0, 0.025)';
            const attrTextColor = isDark ? '#f4f1ea' : '#18181b';
            const attrMutedColor = isDark ? '#b5b0a4' : '#52525b';
            const pkColor = isDark ? '#fdba74' : '#c2410c';
            const fkColor = isDark ? '#94a3b8' : '#64748b';
            const edgeStroke = isDark ? '#b5b0a4' : '#4b5563';
            const edgeLabelBg = isDark ? '#141413' : '#ffffff';
            const edgeLabelBorder = isDark ? 'rgba(224, 107, 58, 0.4)' : 'rgba(224, 107, 58, 0.5)';
            const edgeLabelText = isDark ? '#f4f1ea' : '#18181b';

            // Update SVG Marker circle fill colors
            const markerCircles = document.querySelectorAll('.svg-marker-circle');
            markerCircles.forEach(c => {
                c.setAttribute('fill', isDark ? '#121211' : '#ffffff');
            });

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
                path.setAttribute('stroke', edgeStroke);
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
                    rect.setAttribute('fill', edgeLabelBg);
                    rect.setAttribute('stroke', edgeLabelBorder);
                    rect.setAttribute('stroke-width', '1');
                    rect.setAttribute('rx', '6');
                    viewport.appendChild(rect);

                    const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
                    text.setAttribute('x', edge.lx);
                    text.setAttribute('y', edge.ly + 4);
                    text.setAttribute('fill', edgeLabelText);
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
                bgRect.setAttribute('fill', nodeBg);
                bgRect.setAttribute('stroke', nodeBorder);
                bgRect.setAttribute('stroke-width', '1.5');
                g.appendChild(bgRect);

                // Header Gradient Rect
                const headerRect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
                headerRect.setAttribute('x', '0');
                headerRect.setAttribute('y', '0');
                headerRect.setAttribute('width', TABLE_WIDTH);
                headerRect.setAttribute('height', HEADER_HEIGHT);
                headerRect.setAttribute('rx', '10');
                headerRect.setAttribute('fill', headerBg);
                headerRect.setAttribute('stroke', headerBorder);
                headerRect.setAttribute('stroke-width', '1');
                g.appendChild(headerRect);

                if (showAttributes) {
                    const headerSquare = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
                    headerSquare.setAttribute('x', '0');
                    headerSquare.setAttribute('y', HEADER_HEIGHT - 8);
                    headerSquare.setAttribute('width', TABLE_WIDTH);
                    headerSquare.setAttribute('height', '8');
                    headerSquare.setAttribute('fill', headerBg);
                    g.appendChild(headerSquare);
                }

                // Table Title
                const titleText = document.createElementNS('http://www.w3.org/2000/svg', 'text');
                titleText.setAttribute('x', TABLE_WIDTH / 2);
                titleText.setAttribute('y', HEADER_HEIGHT / 2 + 1);
                titleText.setAttribute('fill', headerTitleColor);
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
                            rowBg.setAttribute('fill', rowAltBg);
                            g.appendChild(rowBg);
                        }

                        // PK / FK Indicator
                        if (attr.pk || attr.fk) {
                            const keyTag = document.createElementNS('http://www.w3.org/2000/svg', 'text');
                            keyTag.setAttribute('x', '14');
                            keyTag.setAttribute('y', rowY + 18);
                            keyTag.setAttribute('fill', attr.pk ? pkColor : fkColor);
                            keyTag.setAttribute('font-size', '11px');
                            keyTag.setAttribute('font-weight', '800');
                            keyTag.textContent = (attr.pk && attr.fk) ? 'PK, FK' : (attr.pk ? 'PK' : 'FK');
                            g.appendChild(keyTag);
                        }

                        // Attribute Name
                        const attrText = document.createElementNS('http://www.w3.org/2000/svg', 'text');
                        attrText.setAttribute('x', '65');
                        attrText.setAttribute('y', rowY + 18);
                        attrText.setAttribute('fill', attr.pk ? (isDark ? '#fdba74' : '#9a3412') : (attr.fk ? attrTextColor : attrMutedColor));
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
            zoomScale = 1.0;
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
