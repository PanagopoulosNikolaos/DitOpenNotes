"""Problem card presentation component for Discrete Mathematics exam exercises.

Renders isolated, structured problem walkthroughs with multi-team variations
(Group A, B, C, D), KaTeX mathematical derivations, final answers, and professor gotcha traps.
"""

from typing import Dict, List
from nicegui import ui
from models.scenario import ExamExercise


def renderProblemCard(exercise: ExamExercise) -> None:
    """Renders a single exam problem with team selector tabs, statement, steps, and traps.

    Args:
        exercise (ExamExercise): The exercise data model containing all team variations.

    Returns:
        None
    """
    teams = list(exercise.statements.keys())
    if not teams:
        teams = ["Ομάδα Α"]

    with ui.column().classes("dash-card w-full p-6 gap-5"):
        # Header Row: Question number, points, topic
        with ui.row().classes("items-center justify-between w-full border-b border-[var(--border)] pb-3 flex-wrap gap-2"):
            with ui.row().classes("items-center gap-3"):
                ui.html(f'<span class="w-8 h-8 rounded-full bg-[var(--accent)] text-white flex items-center justify-center font-black text-sm">{exercise.number}</span>')
                with ui.column().classes("gap-0"):
                    ui.label(exercise.title).classes("text-base font-black text-[var(--text-1)]")
                    ui.label(exercise.topic).classes("text-xs font-bold text-[var(--text-3)]")

            with ui.row().classes("items-center gap-2"):
                ui.html(f'<span class="kpi-badge font-bold text-[var(--accent)]"><i class="fa-solid fa-star"></i> {exercise.points} Μονάδ{"α" if exercise.points == 1 else "ες"}</span>')

        # Team Selector Tabs
        active_team_state = {"team": teams[0]}

        content_container = ui.column().classes("w-full gap-4")

        def updateTeamView(team_name: str) -> None:
            active_team_state["team"] = team_name
            content_container.clear()
            with content_container:
                # 1. Problem Statement
                stmt = exercise.statements.get(team_name, "Δεν υπάρχει εκφώνηση για αυτή την ομάδα.")
                with ui.column().classes("w-full p-4 rounded-xl bg-[var(--surface-2)] border border-[var(--border)] gap-2"):
                    with ui.row().classes("items-center gap-2 text-xs font-bold text-[var(--text-3)]"):
                        ui.html('<i class="fa-solid fa-file-pen text-[var(--accent)]"></i>')
                        ui.label(f"Εκφώνηση Θέματος ({team_name}):")
                    ui.html(f'<div class="text-sm text-[var(--text-1)] leading-relaxed">{stmt}</div>')

                # 2. Step-by-Step Mathematical Derivation
                steps = exercise.steps.get(team_name, [])
                if steps:
                    with ui.column().classes("w-full gap-3"):
                        with ui.row().classes("items-center gap-2 text-xs font-bold text-[var(--text-3)]"):
                            ui.html('<i class="fa-solid fa-list-ol text-[#3b82f6]"></i>')
                            ui.label("Αναλυτική Βήμα-προς-Βήμα Επίλυση:")

                        for idx, step_text in enumerate(steps, 1):
                            with ui.column().classes("w-full p-3.5 rounded-lg bg-[var(--bg-card)] border border-[var(--border)] gap-1 shadow-sm"):
                                with ui.row().classes("items-center gap-2"):
                                    ui.html(f'<span class="text-[11px] font-bold px-2 py-0.5 rounded bg-[var(--surface-2)] text-[var(--accent)]">Βήμα {idx}</span>')
                                ui.html(f'<div class="text-xs text-[var(--text-1)] leading-relaxed pl-1 pt-1">{step_text}</div>')

                # 3. Final Answer Box
                final_ans = exercise.final_answers.get(team_name, "")
                if final_ans:
                    with ui.row().classes("items-center justify-between w-full p-3.5 rounded-lg bg-[var(--callout-success-bg)] border border-[var(--callout-success-border)]"):
                        with ui.row().classes("items-center gap-2"):
                            ui.html('<i class="fa-solid fa-square-check text-[var(--green-ok)] text-base"></i>')
                            ui.label("Τελικό Αποτέλεσμα:").classes("font-bold text-xs text-[var(--callout-success-text)]")
                        ui.html(f'<div class="font-bold text-xs text-[var(--callout-success-text)]">{final_ans}</div>')

                # 4. Professor Gotchas & Pitfalls Block
                if exercise.pitfalls:
                    with ui.column().classes("callout-gotcha w-full gap-1"):
                        with ui.row().classes("items-center gap-2"):
                            ui.html('<i class="fa-solid fa-triangle-exclamation text-[var(--red-err)]"></i>')
                            ui.label("Παγίδες Εξέτασης & Σημεία Προσοχής:").classes("font-bold text-xs")
                        ui.html(f'<div class="text-xs pl-5 leading-relaxed">{exercise.pitfalls}</div>')

        # Render team buttons
        with ui.row().classes("gap-2 items-center flex-wrap"):
            for t in teams:
                btn_cls = "text-xs font-bold px-3 py-1"
                ui.button(t, on_click=lambda name=t: updateTeamView(name)).props("dense outline").classes(btn_cls)

        # Initial render of first team
        updateTeamView(teams[0])


def renderAllProblemCards(exercises: List[ExamExercise]) -> None:
    """Renders all problem cards for an exam scenario sequentially.

    Args:
        exercises (List[ExamExercise]): List of all exam problems.

    Returns:
        None
    """
    with ui.column().classes("w-full gap-6"):
        with ui.row().classes("items-center gap-2 border-b border-[var(--border)] pb-2"):
            ui.html('<i class="fa-solid fa-layer-group text-[var(--accent)]"></i>')
            ui.label("Αναλυτικά Θέματα Εξέτασης & Παραλλαγές Ομάδων").classes("text-sm font-black tracking-wider text-[var(--text-1)]")

        for ex in exercises:
            renderProblemCard(ex)
