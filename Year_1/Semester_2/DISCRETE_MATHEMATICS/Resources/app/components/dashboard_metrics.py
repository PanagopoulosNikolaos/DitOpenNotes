"""Dashboard metrics and formula quick-reference component for Discrete Mathematics."""

from typing import List, Dict
from nicegui import ui
from models.scenario import Scenario


def renderDashboardMetrics(scenario: Scenario) -> None:
    """Renders top-level KPI metrics cards and quick-access formula chips.

    Args:
        scenario (Scenario): The currently active exam or study scenario.

    Returns:
        None
    """
    with ui.column().classes("w-full gap-4"):
        # Top KPI Metrics Row
        with ui.row().classes("w-full gap-4 items-stretch flex-wrap"):
            # Metric 1: Total Points
            with ui.column().classes("dash-card flex-1 min-w-[180px] p-4 gap-1"):
                with ui.row().classes("items-center justify-between w-full"):
                    ui.label("ΣΥΝΟΛΙΚΗ ΒΑΘΜΟΛΟΓΙΑ").classes("text-[10px] font-bold tracking-wider text-[var(--text-3)]")
                    ui.html('<i class="fa-solid fa-award text-[var(--accent)]"></i>')
                with ui.row().classes("items-baseline gap-2"):
                    ui.label(f"{scenario.total_points:.1f}").classes("text-2xl font-black text-[var(--text-1)]")
                    ui.label("μονάδες").classes("text-xs text-[var(--text-2)]")
                ui.label("Βάση επιτυχίας: 5.0 / 10.0").classes("text-[11px] text-[var(--text-3)]")

            # Metric 2: Duration
            with ui.column().classes("dash-card flex-1 min-w-[180px] p-4 gap-1"):
                with ui.row().classes("items-center justify-between w-full"):
                    ui.label("ΔΙΑΡΚΕΙΑ ΕΞΕΤΑΣΗΣ").classes("text-[10px] font-bold tracking-wider text-[var(--text-3)]")
                    ui.html('<i class="fa-solid fa-clock text-[#3b82f6]"></i>')
                with ui.row().classes("items-baseline gap-2"):
                    ui.label(f"{scenario.duration_hours}").classes("text-2xl font-black text-[var(--text-1)]")
                    ui.label("ώρες").classes("text-xs text-[var(--text-2)]")
                ui.label("100% γραπτή εξέταση").classes("text-[11px] text-[var(--text-3)]")

            # Metric 3: Exercises Count
            with ui.column().classes("dash-card flex-1 min-w-[180px] p-4 gap-1"):
                with ui.row().classes("items-center justify-between w-full"):
                    ui.label("ΑΡΙΘΜΟΣ ΘΕΜΑΤΩΝ").classes("text-[10px] font-bold tracking-wider text-[var(--text-3)]")
                    ui.html('<i class="fa-solid fa-list-check text-[#10b981]"></i>')
                with ui.row().classes("items-baseline gap-2"):
                    ui.label(f"{len(scenario.exercises)}").classes("text-2xl font-black text-[var(--text-1)]")
                    ui.label("θέματα (4 Ομάδες)").classes("text-xs text-[var(--text-2)]")
                ui.label("Διαβαθμισμένη δυσκολία").classes("text-[11px] text-[var(--text-3)]")

            # Metric 4: Academic Year
            with ui.column().classes("dash-card flex-1 min-w-[180px] p-4 gap-1"):
                with ui.row().classes("items-center justify-between w-full"):
                    ui.label("ΑΚΑΔΗΜΑΪΚΟ ΕΤΟΣ").classes("text-[10px] font-bold tracking-wider text-[var(--text-3)]")
                    ui.html('<i class="fa-solid fa-calendar-days text-[#f59e0b]"></i>')
                with ui.row().classes("items-baseline gap-2"):
                    ui.label(scenario.academic_year).classes("text-xl font-black text-[var(--text-1)]")
                ui.label("Εαρινό Εξάμηνο").classes("text-[11px] text-[var(--text-3)]")

        # Quick Reference Formula Chips Section
        with ui.expansion("Τυπολόγιο & Θεμελιώδεις Τύποι (Quick Formula Reference)", icon="functions").classes(
            "w-full dash-card px-2 py-1 text-sm font-semibold"
        ):
            with ui.column().classes("p-3 gap-3 w-full"):
                with ui.row().classes("w-full gap-3 flex-wrap"):
                    # Formula 1: Inclusion-Exclusion (PIE)
                    with ui.column().classes("callout-formula flex-1 min-w-[280px] gap-1"):
                        with ui.row().classes("items-center gap-2"):
                            ui.html('<i class="fa-solid fa-cubes text-[var(--accent)]"></i>')
                            ui.label("Αρχή Εγκλεισμού - Αποκλεισμού (PIE)").classes("font-bold text-xs")
                        ui.html(
                            r"<div>$$|A \cup B \cup C| = |A| + |B| + |C| - (|A \cap B| + |A \cap C| + |B \cap C|) + |A \cap B \cap C|$$</div>"
                        )

                    # Formula 2: Graph Handshaking & Euler
                    with ui.column().classes("callout-formula flex-1 min-w-[280px] gap-1"):
                        with ui.row().classes("items-center gap-2"):
                            ui.html('<i class="fa-solid fa-circle-nodes text-[#10b981]"></i>')
                            ui.label("Θεώρημα Χειραψιών & Τύπος Euler").classes("font-bold text-xs")
                        ui.html(
                            r"<div>$$\sum_{v \in V} \deg(v) = 2|E|, \quad V - E + R = 2 \quad (\text{Επίπεδοι Συνεκτικοί})$$</div>"
                        )

                    # Formula 3: Bayes Law
                    with ui.column().classes("callout-formula flex-1 min-w-[280px] gap-1"):
                        with ui.row().classes("items-center gap-2"):
                            ui.html('<i class="fa-solid fa-percent text-[#3b82f6]"></i>')
                            ui.label("Θεώρημα Bayes & Ολική Πιθανότητα").classes("font-bold text-xs")
                        ui.html(
                            r"<div>$$P(A_i \mid B) = \frac{P(B \mid A_i)P(A_i)}{\sum_{j} P(B \mid A_j)P(A_j)}$$</div>"
                        )

                    # Formula 4: Combinatorics
                    with ui.column().classes("callout-formula flex-1 min-w-[280px] gap-1"):
                        with ui.row().classes("items-center gap-2"):
                            ui.html('<i class="fa-solid fa-calculator text-[#f59e0b]"></i>')
                            ui.label("Συνδυασμοί & Διατάξεις").classes("font-bold text-xs")
                        ui.html(
                            r"<div>$$C(n, k) = \binom{n}{k} = \frac{n!}{k!(n-k)!}, \quad P(n, k) = \frac{n!}{(n-k)!}$$</div>"
                        )
