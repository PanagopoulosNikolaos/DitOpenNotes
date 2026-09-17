"""Interactive Algorithmic Workbench & Visual Simulators for Discrete Mathematics.

Provides interactive tools for graph traversal & isomorphism, dynamic truth table
generation, multi-set Venn diagrams with PIE calculations, DFA string validation,
and mathematical induction step-by-step carousels.
"""

from typing import Dict, List, Optional
import itertools
from nicegui import ui
from models.scenario import Scenario, GraphModel, GraphNode, GraphEdge


class GraphSimulator:
    """Manages graph state, SVG generation, and step-by-step BFS/DFS execution."""

    def __init__(self) -> None:
        """Initializes the graph simulator with default graph models."""
        # Pre-configured Graph 1 (from 2025/2026 exams)
        self.g1_nodes = [
            GraphNode(id="A", label="A", x=70.0, y=70.0),
            GraphNode(id="B", label="B", x=210.0, y=50.0),
            GraphNode(id="C", label="C", x=330.0, y=110.0),
            GraphNode(id="D", label="D", x=290.0, y=230.0),
            GraphNode(id="E", label="E", x=150.0, y=250.0),
            GraphNode(id="F", label="F", x=60.0, y=180.0),
        ]
        self.g1_edges = [
            ("A", "B"), ("A", "D"), ("B", "C"), ("C", "D"),
            ("D", "E"), ("E", "F"), ("A", "F"), ("B", "E")
        ]

        # Pre-configured Graph 2 (for isomorphism testing)
        self.g2_nodes = [
            GraphNode(id="1", label="1", x=70.0, y=70.0),
            GraphNode(id="2", label="2", x=210.0, y=50.0),
            GraphNode(id="3", label="3", x=330.0, y=110.0),
            GraphNode(id="4", label="4", x=290.0, y=230.0),
            GraphNode(id="5", label="5", x=150.0, y=250.0),
            GraphNode(id="6", label="6", x=60.0, y=180.0),
        ]
        self.g2_edges = [
            ("1", "2"), ("2", "3"), ("2", "5"), ("3", "4"),
            ("3", "6"), ("4", "5"), ("5", "6"), ("1", "6")
        ]

        self.active_graph_id = "g1"
        self.visited_nodes: List[str] = []
        self.current_step_index = 0
        self.traversal_mode = "BFS"
        self.traversal_order: List[str] = []

    def getAdjList(self, graph_id: str) -> Dict[str, List[str]]:
        """Constructs adjacency list for specified graph.

        Args:
            graph_id (str): 'g1' or 'g2'.

        Returns:
            Dict[str, List[str]]: Mapping from vertex identifier to list of neighbors.
        """
        edges = self.g1_edges if graph_id == "g1" else self.g2_edges
        adj: Dict[str, List[str]] = {}
        for u, v in edges:
            adj.setdefault(u, []).append(v)
            adj.setdefault(v, []).append(u)
        for k in adj:
            adj[k].sort()
        return adj

    def computeBFS(self, start_node: str = "A") -> List[str]:
        """Calculates Breadth-First Search traversal order.

        Args:
            start_node (str): Origin node for traversal.

        Returns:
            List[str]: Chronological list of visited vertices.
        """
        adj = self.getAdjList(self.active_graph_id)
        if start_node not in adj:
            start_node = next(iter(adj))
        visited: List[str] = []
        queue = [start_node]
        seen = {start_node}
        while queue:
            curr = queue.pop(0)
            visited.append(curr)
            for neighbor in adj.get(curr, []):
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
        return visited

    def computeDFS(self, start_node: str = "A") -> List[str]:
        """Calculates Depth-First Search traversal order.

        Args:
            start_node (str): Origin node for traversal.

        Returns:
            List[str]: Chronological list of visited vertices.
        """
        adj = self.getAdjList(self.active_graph_id)
        if start_node not in adj:
            start_node = next(iter(adj))
        visited: List[str] = []
        seen = set()

        def _dfs(node: str) -> None:
            seen.add(node)
            visited.append(node)
            for neighbor in adj.get(node, []):
                if neighbor not in seen:
                    _dfs(neighbor)

        _dfs(start_node)
        return visited

    def generateSvg(self) -> str:
        """Generates SVG markup rendering current graph and visited highlight states.

        Returns:
            str: Raw SVG XML string.
        """
        nodes = self.g1_nodes if self.active_graph_id == "g1" else self.g2_nodes
        edges = self.g1_edges if self.active_graph_id == "g1" else self.g2_edges
        node_map = {n.id: n for n in nodes}

        svg_parts = [
            '<svg viewBox="0 0 400 300" class="w-full h-72 md:h-80 bg-[var(--svg-canvas-bg)] rounded-lg border border-[var(--border)]">'
        ]

        # Draw grid background
        svg_parts.append(
            '<defs><pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse">'
            '<circle cx="2" cy="2" r="1" fill="var(--svg-grid-dot)" /></pattern></defs>'
            '<rect width="100%" height="100%" fill="url(#grid)" />'
        )

        # Draw Edges
        for u, v in edges:
            if u in node_map and v in node_map:
                p1 = node_map[u]
                p2 = node_map[v]
                is_traversed = (u in self.visited_nodes and v in self.visited_nodes)
                color = "var(--svg-edge-active)" if is_traversed else "var(--svg-edge-stroke)"
                width = "3" if is_traversed else "1.5"
                svg_parts.append(
                    f'<line x1="{p1.x}" y1="{p1.y}" x2="{p2.x}" y2="{p2.y}" '
                    f'stroke="{color}" stroke-width="{width}" stroke-linecap="round" />'
                )

        # Draw Nodes
        for n in nodes:
            is_visited = n.id in self.visited_nodes
            is_current = self.visited_nodes and (self.visited_nodes[-1] == n.id)
            fill_color = "var(--accent)" if is_current else ("var(--green-ok)" if is_visited else "var(--svg-node-fill)")
            text_color = "#ffffff" if (is_visited or is_current) else "var(--svg-node-text)"
            stroke_color = "var(--accent-dark)" if is_current else "var(--svg-node-stroke)"
            r = "20" if is_current else "18"

            svg_parts.append(
                f'<circle cx="{n.x}" cy="{n.y}" r="{r}" fill="{fill_color}" '
                f'stroke="{stroke_color}" stroke-width="2.5" class="transition-all duration-300" />'
                f'<text x="{n.x}" y="{n.y + 5}" font-size="13" font-weight="700" '
                f'text-anchor="middle" fill="{text_color}">{n.label}</text>'
            )

        svg_parts.append("</svg>")
        return "".join(svg_parts)


class AutomatonSimulator:
    """Simulates DFA execution on input strings."""

    def __init__(self) -> None:
        """Initializes DFA for accepting strings with at least two '0's."""
        self.states = ["q0", "q1", "q2"]
        self.initial_state = "q0"
        self.accepting_states = ["q2"]
        self.transitions = {
            "q0": {"0": "q1", "1": "q0"},
            "q1": {"0": "q2", "1": "q1"},
            "q2": {"0": "q2", "1": "q2"},
        }
        self.current_state = "q0"
        self.trace: List[str] = ["q0"]

    def runString(self, input_str: str) -> bool:
        """Runs the entire string and updates the execution trace.

        Args:
            input_str (str): Input string containing binary characters '0' and '1'.

        Returns:
            bool: True if final state is accepting, False otherwise.
        """
        self.current_state = self.initial_state
        self.trace = [self.initial_state]
        for char in input_str:
            if char in self.transitions.get(self.current_state, {}):
                self.current_state = self.transitions[self.current_state][char]
                self.trace.append(self.current_state)
            else:
                return False
        return self.current_state in self.accepting_states

    def generateSvg(self) -> str:
        """Generates SVG state transition diagram for DFA.

        Returns:
            str: SVG string.
        """
        # Node positions: q0=(80, 100), q1=(200, 100), q2=(320, 100)
        coords = {"q0": (80, 100), "q1": (200, 100), "q2": (320, 100)}
        svg = [
            '<svg viewBox="0 0 400 200" class="w-full h-48 bg-[var(--svg-canvas-bg)] rounded-lg border border-[var(--border)]">'
        ]

        # Initial arrow
        svg.append('<path d="M 30 100 L 60 100" stroke="var(--accent)" stroke-width="2" marker-end="url(#arrow)" />')

        # Self-loops & Transitions
        # q0 -> q1 (0)
        svg.append('<path d="M 100 100 L 180 100" stroke="var(--text-3)" stroke-width="2" />')
        svg.append('<text x="140" y="90" font-size="12" font-weight="bold" fill="var(--accent)">0</text>')
        # q1 -> q2 (0)
        svg.append('<path d="M 220 100 L 300 100" stroke="var(--text-3)" stroke-width="2" />')
        svg.append('<text x="260" y="90" font-size="12" font-weight="bold" fill="var(--accent)">0</text>')

        # Self loop on q0 (1)
        svg.append('<path d="M 75 80 A 15 15 0 1 1 90 80" fill="none" stroke="var(--text-3)" stroke-width="2" />')
        svg.append('<text x="80" y="55" font-size="12" font-weight="bold" fill="var(--text-2)">1</text>')
        # Self loop on q1 (1)
        svg.append('<path d="M 195 80 A 15 15 0 1 1 210 80" fill="none" stroke="var(--text-3)" stroke-width="2" />')
        svg.append('<text x="200" y="55" font-size="12" font-weight="bold" fill="var(--text-2)">1</text>')
        # Self loop on q2 (0, 1)
        svg.append('<path d="M 315 80 A 15 15 0 1 1 330 80" fill="none" stroke="var(--text-3)" stroke-width="2" />')
        svg.append('<text x="315" y="55" font-size="12" font-weight="bold" fill="var(--text-2)">0, 1</text>')

        # Draw State circles
        for state, (x, y) in coords.items():
            is_active = (state == self.current_state)
            fill_color = "var(--accent)" if is_active else "var(--svg-node-fill)"
            text_color = "#ffffff" if is_active else "var(--svg-node-text)"
            stroke = "var(--accent-dark)" if is_active else "var(--svg-node-stroke)"

            # Double circle for accepting state q2
            if state in self.accepting_states:
                svg.append(f'<circle cx="{x}" cy="{y}" r="26" fill="none" stroke="{stroke}" stroke-width="1.8" />')

            svg.append(f'<circle cx="{x}" cy="{y}" r="22" fill="{fill_color}" stroke="{stroke}" stroke-width="2" />')
            svg.append(f'<text x="{x}" y="{y + 4}" font-size="12" font-weight="bold" text-anchor="middle" fill="{text_color}">{state}</text>')

        svg.append("</svg>")
        return "".join(svg)


def renderVisualSimulator(scenario: Scenario) -> None:
    """Renders the top interactive visualizer and algorithmic workbench.

    Args:
        scenario (Scenario): Active scenario.

    Returns:
        None
    """
    graph_sim = GraphSimulator()
    automaton_sim = AutomatonSimulator()

    with ui.column().classes("w-full dash-card p-6 gap-6"):
        with ui.row().classes("items-center justify-between w-full border-b border-[var(--border)] pb-3"):
            with ui.row().classes("items-center gap-3"):
                ui.html('<i class="fa-solid fa-flask-vial text-[var(--accent)] text-xl"></i>')
                with ui.column().classes("gap-0"):
                    ui.label("Διαδραστικό Αλγοριθμικό Εργαστήριο (Interactive Workbench)").classes("text-base font-black")
                    ui.label("Προσομοιωτές Γράφων, Πινάκων Αληθείας, Διαγραμμάτων Venn, DFA & Επαγωγής").classes("text-xs text-[var(--text-2)]")

        # Tab Navigation
        with ui.tabs().props("dense mobile-arrows outside-arrows").classes("w-full text-xs font-bold border-b border-[var(--border)]") as tabs:
            tab_graph = ui.tab("1. Γράφοι & Euler", icon="hub")
            tab_truth = ui.tab("2. Πίνακες Αληθείας", icon="table_chart")
            tab_venn = ui.tab("3. Venn & PIE", icon="pie_chart")
            tab_dfa = ui.tab("4. Αυτόματα DFA", icon="settings")
            tab_induction = ui.tab("5. Μαθηματική Επαγωγή", icon="view_carousel")

        with ui.tab_panels(tabs, value=tab_graph).classes("w-full bg-transparent p-0 pt-4"):

            # PANEL 1: GRAPH & ISOMORPHISM WORKBENCH
            with ui.tab_panel(tab_graph):
                with ui.row().classes("w-full gap-6 flex-col xl:flex-row items-stretch"):
                    # Left: Interactive SVG Canvas
                    with ui.column().classes("w-full xl:flex-1 min-w-0 max-w-2xl gap-3"):
                        svg_container = ui.html(graph_sim.generateSvg())

                        # Graph details chip
                        with ui.row().classes("gap-2 items-center text-xs text-[var(--text-2)]"):
                            ui.html('<i class="fa-solid fa-circle-info text-[var(--accent)]"></i>')
                            info_label = ui.label("Κορυφές: |V| = 6, Ακμές: |E| = 8, Βαθμοί: A:3, B:3, C:2, D:3, E:3, F:2")

                    # Right: Controls & Stepper
                    with ui.column().classes("w-full xl:flex-1 min-w-0 max-w-2xl gap-4 p-4 rounded-xl bg-[var(--surface-2)] border border-[var(--border)]"):
                        ui.label("Έλεγχος & Αλγόριθμοι Διάσχισης").classes("text-xs font-bold tracking-wider text-[var(--text-3)]")

                        # Graph Selector
                        def onGraphChange(e):
                            graph_sim.active_graph_id = e.value
                            graph_sim.visited_nodes = []
                            svg_container.set_content(graph_sim.generateSvg())
                            if e.value == "g1":
                                info_label.set_text("Γράφημα G1: |V|=6, |E|=8. Βαθμοί: 3, 3, 3, 3, 2, 2. Επίπεδο (Kuratowski: χωρίς K5/K3,3).")
                            else:
                                info_label.set_text("Γράφημα G2: |V|=6, |E|=8. Βαθμοί: 3, 3, 3, 3, 2, 2. Ισόμορφο με G1.")

                        ui.select(
                            options={"g1": "Γράφημα G1 (Εξετάσεις 2025/2026)", "g2": "Γράφημα G2 (Ισόμορφο προς έλεγχο)"},
                            value="g1",
                            on_change=onGraphChange,
                        ).props('outlined dense popup-content-class="app-select-popup"').classes("w-full text-xs bg-[var(--input-bg)]")

                        # Traversal Actions
                        with ui.row().classes("w-full gap-2"):
                            def runBFS():
                                graph_sim.visited_nodes = graph_sim.computeBFS("A" if graph_sim.active_graph_id == "g1" else "1")
                                svg_container.set_content(graph_sim.generateSvg())
                                log_label.set_text(f"Σειρά BFS: {' -> '.join(graph_sim.visited_nodes)}")

                            def runDFS():
                                graph_sim.visited_nodes = graph_sim.computeDFS("A" if graph_sim.active_graph_id == "g1" else "1")
                                svg_container.set_content(graph_sim.generateSvg())
                                log_label.set_text(f"Σειρά DFS: {' -> '.join(graph_sim.visited_nodes)}")

                            def resetGraph():
                                graph_sim.visited_nodes = []
                                svg_container.set_content(graph_sim.generateSvg())
                                log_label.set_text("Αναμονή εκτέλεσης αλγορίθμου...")

                            ui.button("Εκτέλεση BFS", on_click=runBFS).props("dense unelevated").classes(
                                "flex-1 text-xs bg-[var(--blue-action)] text-white font-bold"
                            )
                            ui.button("Εκτέλεση DFS", on_click=runDFS).props("dense unelevated").classes(
                                "flex-1 text-xs bg-[var(--accent)] text-white font-bold"
                            )
                            ui.button("Επαναφορά", on_click=resetGraph).props("dense outline").classes(
                                "text-xs text-[var(--text-2)]"
                            )

                        # Traversal Log Output
                        with ui.column().classes("w-full p-2.5 rounded-lg bg-[var(--bg-card)] border border-[var(--border)] gap-1"):
                            ui.label("Καταγραφή Διάσχισης (Traversal Log):").classes("text-[10px] font-bold text-[var(--text-3)]")
                            log_label = ui.label("Αναμονή εκτέλεσης αλγορίθμου...").classes("text-xs font-mono font-bold text-[var(--text-1)]")

                        # Invariants & Euler Verification
                        with ui.expansion("Επαλήθευση Τύπου Euler & Θεωρήματος Χειραψιών", icon="calculate", value=True).classes(
                            "w-full callout-formula text-xs font-semibold rounded-lg p-0 overflow-hidden"
                        ):
                            with ui.column().classes("w-full p-2 gap-1 text-xs overflow-x-auto"):
                                ui.label("Επαλήθευση Τύπου Euler (Επίπεδοι Γράφοι):").classes("font-bold text-xs")
                                ui.html(r'<div class="katex-scroll">$$V - E + R = 2 \implies 6 - 8 + R = 2 \implies R = 4 \text{ περιοχές}$$</div>')
                                ui.html(r'<div class="katex-scroll">$$\sum_{v \in V} \deg(v) = 16 = 2|E| \quad (3+3+3+3+2+2 = 16)$$</div>')

            # PANEL 2: TRUTH TABLE GENERATOR
            with ui.tab_panel(tab_truth):
                with ui.column().classes("w-full gap-4"):
                    with ui.row().classes("w-full justify-between items-center flex-wrap gap-3"):
                        ui.label("Αυτόματη Κατασκευή & Επαλήθευση Πινάκων Αληθείας").classes("text-sm font-bold")

                        # Formula selector
                        formula_select = ui.select(
                            options={
                                "syllogism": "Υποθετικός Συλλογισμός: ((p -> q) & (q -> r)) -> (p -> r)",
                                "demorgan": "Νόμος De Morgan: !(p & q) <-> (!p | !q)",
                                "modus_ponens": "Modus Ponens: ((p -> q) & p) -> q",
                                "resolution": "Κανόνας Επίλυσης: ((p | q) & !p) -> q",
                                "custom_2025": "Θέμα 1 (2025): ((p -> q) & (!p -> q)) -> q",
                            },
                            value="syllogism",
                        ).props('outlined dense popup-content-class="app-select-popup"').classes("w-96 max-w-full text-xs bg-[var(--input-bg)]")

                    table_container = ui.column().classes("w-full overflow-x-auto")

                    def renderTruthTable(formula_key: str) -> None:
                        table_container.clear()
                        with table_container:
                            if formula_key == "syllogism":
                                # 3 variables: p, q, r
                                vars = ["p", "q", "r"]
                                rows = []
                                all_true = True
                                for p, q, r in itertools.product([True, False], repeat=3):
                                    p_imp_q = (not p) or q
                                    q_imp_r = (not q) or r
                                    p_imp_r = (not p) or r
                                    hyp = p_imp_q and q_imp_r
                                    res = (not hyp) or p_imp_r
                                    if not res:
                                        all_true = False
                                    rows.append((p, q, r, p_imp_q, q_imp_r, hyp, p_imp_r, res))

                                html_table = [
                                    '<table class="truth-table">',
                                    '<thead><tr>',
                                    '<th>p</th><th>q</th><th>r</th><th>p &rarr; q</th><th>q &rarr; r</th>',
                                    '<th>(p &rarr; q) &and; (q &rarr; r)</th><th>p &rarr; r</th>',
                                    '<th class="bg-[var(--accent)] text-white">Αποτέλεσμα</th>',
                                    '</tr></thead><tbody>'
                                ]
                                for row in rows:
                                    html_table.append("<tr>")
                                    for idx, val in enumerate(row):
                                        val_str = "T" if val else "F"
                                        cls = "val-true" if val else "val-false"
                                        if idx == len(row) - 1:
                                            cls += " font-bold bg-[var(--card-bg-subtle)]"
                                        html_table.append(f'<td class="{cls}">{val_str}</td>')
                                    html_table.append("</tr>")
                                html_table.append("</tbody></table>")

                                ui.html("".join(html_table))
                                with ui.row().classes("items-center gap-2 mt-2"):
                                    ui.html('<span class="kpi-badge text-[var(--green-ok)] border-[var(--green-ok)]"><i class="fa-solid fa-circle-check"></i> ΤΑΥΤΟΛΟΓΙΑ (Όλες οι γραμμές T)</span>')
                                    ui.label("Ο τύπος είναι έγκυρος και αποτελεί βασικό κανόνα συμπερασμού.").classes("text-xs text-[var(--text-2)]")

                            elif formula_key == "custom_2025":
                                vars = ["p", "q"]
                                rows = []
                                for p, q in itertools.product([True, False], repeat=2):
                                    p_imp_q = (not p) or q
                                    np_imp_q = p or q
                                    hyp = p_imp_q and np_imp_q
                                    res = (not hyp) or q
                                    rows.append((p, q, not p, p_imp_q, np_imp_q, hyp, res))

                                html_table = [
                                    '<table class="truth-table">',
                                    '<thead><tr>',
                                    '<th>p</th><th>q</th><th>&not;p</th><th>p &rarr; q</th><th>&not;p &rarr; q</th>',
                                    '<th>(p &rarr; q) &and; (&not;p &rarr; q)</th>',
                                    '<th class="bg-[var(--accent)] text-white">Αποτέλεσμα &rarr; q</th>',
                                    '</tr></thead><tbody>'
                                ]
                                for row in rows:
                                    html_table.append("<tr>")
                                    for idx, val in enumerate(row):
                                        val_str = "T" if val else "F"
                                        cls = "val-true" if val else "val-false"
                                        html_table.append(f'<td class="{cls}">{val_str}</td>')
                                    html_table.append("</tr>")
                                html_table.append("</tbody></table>")
                                ui.html("".join(html_table))
                                with ui.row().classes("items-center gap-2 mt-2"):
                                    ui.html('<span class="kpi-badge text-[var(--green-ok)] border-[var(--green-ok)]"><i class="fa-solid fa-circle-check"></i> ΤΑΥΤΟΛΟΓΙΑ</span>')
                                    ui.label("Επαλήθευση Θέματος 1 Ιουνίου 2025 (Ομάδα Α)").classes("text-xs text-[var(--text-2)]")

                            else:
                                # Standard 2-var formulas
                                vars = ["p", "q"]
                                rows = []
                                for p, q in itertools.product([True, False], repeat=2):
                                    if formula_key == "demorgan":
                                        lhs = not (p and q)
                                        rhs = (not p) or (not q)
                                        res = lhs == rhs
                                        rows.append((p, q, not p, not q, p and q, lhs, rhs, res))
                                    elif formula_key == "modus_ponens":
                                        p_imp_q = (not p) or q
                                        hyp = p_imp_q and p
                                        res = (not hyp) or q
                                        rows.append((p, q, p_imp_q, hyp, res))
                                    else:
                                        p_or_q = p or q
                                        hyp = p_or_q and (not p)
                                        res = (not hyp) or q
                                        rows.append((p, q, not p, p_or_q, hyp, res))

                                html_table = ['<table class="truth-table"><thead><tr>']
                                for v in vars:
                                    html_table.append(f"<th>{v}</th>")
                                html_table.append('<th class="bg-[var(--accent)] text-white">Αποτέλεσμα</th></tr></thead><tbody>')
                                for row in rows:
                                    html_table.append("<tr>")
                                    for idx, val in enumerate(row):
                                        val_str = "T" if val else "F"
                                        cls = "val-true" if val else "val-false"
                                        html_table.append(f'<td class="{cls}">{val_str}</td>')
                                    html_table.append("</tr>")
                                html_table.append("</tbody></table>")
                                ui.html("".join(html_table))

                    formula_select.on_value_change(lambda e: renderTruthTable(e.value))
                    renderTruthTable("syllogism")

            # PANEL 3: VENN & SET OPERATIONS (PIE)
            with ui.tab_panel(tab_venn):
                with ui.row().classes("w-full gap-6 flex-col lg:flex-row items-center"):
                    # Venn SVG Visualizer
                    venn_svg = ui.html("""
                    <svg viewBox="0 0 400 250" class="w-full h-64 bg-[var(--svg-canvas-bg)] rounded-lg border border-[var(--border)]">
                        <!-- Universal Set Ω -->
                        <rect x="20" y="20" width="360" height="210" rx="12" fill="none" stroke="var(--border-accent)" stroke-width="2" stroke-dasharray="4 4"/>
                        <text x="35" y="45" font-size="14" font-weight="bold" fill="var(--text-3)">&Omega; = {1, ..., 8}</text>

                        <!-- Set A (left circle) -->
                        <circle id="circle-a" cx="160" cy="130" r="70" fill="rgba(217, 83, 30, 0.2)" stroke="var(--accent)" stroke-width="2.5"/>
                        <text x="120" y="90" font-size="14" font-weight="bold" fill="var(--accent)">A = {1, 2, 3, 4}</text>

                        <!-- Set B (right circle) -->
                        <circle id="circle-b" cx="240" cy="130" r="70" fill="rgba(59, 130, 246, 0.2)" stroke="var(--blue-action)" stroke-width="2.5"/>
                        <text x="260" y="90" font-size="14" font-weight="bold" fill="var(--blue-action)">B = {3, 4, 5, 6}</text>

                        <!-- Region Labels -->
                        <text x="135" y="135" font-size="12" font-weight="bold" fill="var(--text-1)">1, 2</text>
                        <text x="195" y="135" font-size="12" font-weight="bold" fill="var(--text-1)">3, 4</text>
                        <text x="255" y="135" font-size="12" font-weight="bold" fill="var(--text-1)">5, 6</text>
                        <text x="50" y="190" font-size="12" font-weight="bold" fill="var(--text-3)">7, 8</text>
                    </svg>
                    """)

                    # Set Controls & Live Math
                    with ui.column().classes("flex-1 gap-4 p-4 rounded-xl bg-[var(--surface-2)] border border-[var(--border)]"):
                        ui.label("Επιλογή Πράξης Συνόλων & Υπολογισμός").classes("text-xs font-bold tracking-wider text-[var(--text-3)]")

                        result_box = ui.column().classes("callout-formula w-full gap-1 text-xs")

                        def setVennOp(op_name: str, elements: str, formula: str):
                            result_box.clear()
                            with result_box:
                                ui.label(f"Πράξη: {op_name}").classes("font-bold text-sm")
                                ui.label(f"Στοιχεία: {elements}").classes("font-mono font-bold")
                                ui.html(f"<div>$${formula}$$</div>")

                        with ui.row().classes("gap-2 flex-wrap"):
                            ui.button("A ∪ B", on_click=lambda: setVennOp("Ένωση (A ∪ B)", "{1, 2, 3, 4, 5, 6}", "|A \\cup B| = |A| + |B| - |A \\cap B| = 4 + 4 - 2 = 6")).props("dense outline").classes("text-xs font-bold")
                            ui.button("A ∩ B", on_click=lambda: setVennOp("Τομή (A ∩ B)", "{3, 4}", "|A \\cap B| = 2")).props("dense outline").classes("text-xs font-bold")
                            ui.button("A \\ B", on_click=lambda: setVennOp("Διαφορά (A \\ B)", "{1, 2}", "|A \\setminus B| = |A| - |A \\cap B| = 4 - 2 = 2")).props("dense outline").classes("text-xs font-bold")
                            ui.button("A ⊕ B", on_click=lambda: setVennOp("Συμμετρική Διαφορά (A ⊕ B)", "{1, 2, 5, 6}", "|A \\oplus B| = |A \\cup B| - |A \\cap B| = 6 - 2 = 4")).props("dense outline").classes("text-xs font-bold")
                            ui.button("(A ∪ B)^c", on_click=lambda: setVennOp("Συμπλήρωμα (A ∪ B)^c", "{7, 8}", "|(A \\cup B)^c| = |\\Omega| - |A \\cup B| = 8 - 6 = 2")).props("dense outline").classes("text-xs font-bold")

                        setVennOp("Ένωση (A ∪ B)", "{1, 2, 3, 4, 5, 6}", "|A \\cup B| = |A| + |B| - |A \\cap B| = 4 + 4 - 2 = 6")

            # PANEL 4: DFA STRING VALIDATOR
            with ui.tab_panel(tab_dfa):
                with ui.row().classes("w-full gap-6 flex-col lg:flex-row items-center"):
                    dfa_svg_container = ui.html(automaton_sim.generateSvg())

                    with ui.column().classes("flex-1 gap-3 p-4 rounded-xl bg-[var(--surface-2)] border border-[var(--border)]"):
                        ui.label("DFA: Αναγνώριση Συμβολοσειρών με τουλάχιστον 2 μηδενικά").classes("text-xs font-bold text-[var(--text-3)]")
                        ui.label("Κανονική Έκφραση: 1* 0 1* 0 (0 | 1)*").classes("text-xs font-mono font-bold text-[var(--accent)]")

                        test_input = ui.input(
                            label="Συμβολοσειρά Εισόδου (0 & 1)",
                            value="10101",
                        ).props("outlined dense").classes("w-full bg-[var(--input-bg)] text-xs")

                        status_badge = ui.html('<span class="kpi-badge"><i class="fa-solid fa-clock"></i> Αναμονή ελέγχου</span>')
                        trace_label = ui.label("Διαδρομή: q0").classes("text-xs font-mono text-[var(--text-2)]")

                        def testDFA():
                            val = test_input.value.strip()
                            accepted = automaton_sim.runString(val)
                            dfa_svg_container.set_content(automaton_sim.generateSvg())
                            trace_str = " -> ".join(automaton_sim.trace)
                            trace_label.set_text(f"Διαδρομή καταστάσεων: {trace_str}")
                            if accepted:
                                status_badge.set_content('<span class="kpi-badge text-[var(--green-ok)] border-[var(--green-ok)]"><i class="fa-solid fa-check"></i> ΑΠΟΔΕΚΤΗ (Τουλάχιστον 2 μηδενικά)</span>')
                            else:
                                status_badge.set_content('<span class="kpi-badge text-[var(--red-err)] border-[var(--red-err)]"><i class="fa-solid fa-xmark"></i> ΑΠΟΡΡΙΨΗ (Λιγότερα από 2 μηδενικά)</span>')

                        with ui.row().classes("gap-2 items-center"):
                            ui.button("Έλεγχος Συμβολοσειράς", on_click=testDFA).props("dense unelevated").classes(
                                "text-xs bg-[var(--accent)] text-white font-bold"
                            )
                            ui.button("Καθαρισμός", on_click=lambda: [test_input.set_value(""), automaton_sim.runString(""), dfa_svg_container.set_content(automaton_sim.generateSvg()), trace_label.set_text("Διαδρομή: q0")]).props("dense outline").classes(
                                "text-xs text-[var(--text-2)]"
                            )

            # PANEL 5: MATHEMATICAL INDUCTION CAROUSEL
            with ui.tab_panel(tab_induction):
                induction_step = {"curr": 1}
                total_steps = 4

                step_card = ui.column().classes("dash-card w-full p-5 gap-3")

                def updateInductionView():
                    step_card.clear()
                    step_num = induction_step["curr"]
                    with step_card:
                        with ui.row().classes("items-center justify-between w-full border-b border-[var(--border)] pb-2"):
                            ui.label(f"Βήμα {step_num} από {total_steps}:").classes("text-xs font-bold text-[var(--text-3)]")
                            if step_num == 1:
                                ui.html('<span class="kpi-badge text-[var(--blue-action)]">ΒΑΣΙΚΟ ΒΗΜΑ (Base Step)</span>')
                            elif step_num == 2:
                                ui.html('<span class="kpi-badge text-[#f59e0b]">ΕΠΑΓΩΓΙΚΗ ΥΠΟΘΕΣΗ (Hypothesis)</span>')
                            elif step_num == 3:
                                ui.html('<span class="kpi-badge text-[var(--accent)]">ΕΠΑΓΩΓΙΚΟ ΒΗΜΑ (Inductive Step)</span>')
                            else:
                                ui.html('<span class="kpi-badge text-[var(--green-ok)]">ΣΥΜΠΕΡΑΣΜΑ & Q.E.D.</span>')

                        if step_num == 1:
                            ui.label("Πρόταση P(n): 1 + 3 + 3^2 + ... + 3^n = (3^(n+1) - 1) / 2  για κάθε n >= 0").classes("text-sm font-bold")
                            ui.html("""
                            <div class="callout-formula">
                                <b>Έλεγχος για n = 0:</b><br/>
                                Αριστερό Μέλος: $$LHS = 3^0 = 1$$<br/>
                                Δεξί Μέλος: $$RHS = \\frac{3^{0+1} - 1}{2} = \\frac{3 - 1}{2} = \\frac{2}{2} = 1$$<br/>
                                Εφόσον LHS = RHS = 1, η βάση της επαγωγής ισχύει για n = 0.
                            </div>
                            """)
                        elif step_num == 2:
                            ui.label("Διατύπωση Επαγωγικής Υπόθεσης").classes("text-sm font-bold")
                            ui.html("""
                            <div class="callout-formula">
                                Υποθέτουμε ότι η πρόταση P(k) ισχύει για κάποιο αυθαίρετο ακέραιο k &ge; 0:<br/>
                                $$1 + 3 + 3^2 + \\cdots + 3^k = \\frac{3^{k+1} - 1}{2}$$
                            </div>
                            """)
                        elif step_num == 3:
                            ui.label("Απόδειξη για n = k + 1").classes("text-sm font-bold")
                            ui.html("""
                            <div class="callout-formula">
                                Ζητούμε να αποδείξουμε ότι P(k+1) είναι αληθής, δηλαδή:<br/>
                                $$1 + 3 + 3^2 + \\cdots + 3^k + 3^{k+1} = \\frac{3^{(k+1)+1} - 1}{2} = \\frac{3^{k+2} - 1}{2}$$<br/>
                                <b>Αντικατάσταση της Επαγωγικής Υπόθεσης:</b><br/>
                                $$LHS = \\left(1 + 3 + \\cdots + 3^k\\right) + 3^{k+1} = \\frac{3^{k+1} - 1}{2} + 3^{k+1}$$<br/>
                                $$= \\frac{3^{k+1} - 1 + 2 \\cdot 3^{k+1}}{2} = \\frac{3 \\cdot 3^{k+1} - 1}{2} = \\frac{3^{k+2} - 1}{2} = RHS$$
                            </div>
                            """)
                        else:
                            ui.label("Τελικό Συμπέρασμα").classes("text-sm font-bold")
                            ui.html("""
                            <div class="callout-gotcha" style="border-color: var(--green-ok); background: var(--callout-success-bg); color: var(--callout-success-text);">
                                <b>Ολοκλήρωση της Απόδειξης:</b><br/>
                                Εφόσον ισχύει η βάση P(0) και αποδείχθηκε ότι P(k) &implies; P(k+1) για κάθε k &ge; 0,
                                από την Αρχή της Μαθηματικής Επαγωγής η ισότητα ισχύει για κάθε φυσικό αριθμό n &ge; 0. (Q.E.D.)
                            </div>
                            """)

                def nextInduction():
                    if induction_step["curr"] < total_steps:
                        induction_step["curr"] += 1
                        updateInductionView()

                def prevInduction():
                    if induction_step["curr"] > 1:
                        induction_step["curr"] -= 1
                        updateInductionView()

                def resetInduction():
                    induction_step["curr"] = 1
                    updateInductionView()

                with ui.row().classes("w-full justify-between items-center mt-3"):
                    ui.button("Προηγούμενο Βήμα", on_click=prevInduction).props("dense outline").classes("text-xs")
                    ui.button("Επαναφορά", on_click=resetInduction).props("dense outline").classes("text-xs text-[var(--text-3)]")
                    ui.button("Επόμενο Βήμα", on_click=nextInduction).props("dense unelevated").classes("text-xs bg-[var(--accent)] text-white font-bold")

                updateInductionView()
