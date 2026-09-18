"""Problem card presentation component for Discrete Mathematics exam exercises.

Renders unified, structured problem walkthroughs with multi-team variations
(Group A, B, C, D), AM 3323 defaults, KaTeX mathematical derivations, final answers,
and professor gotcha traps inside a single cohesive card container.
"""

from typing import List
from nicegui import ui
from models.scenario import ExamExercise


def renderProblemCard(exercise: ExamExercise) -> None:
    """Renders a single exam problem with team selector buttons, statement, and steps in one container.

    Args:
        exercise (ExamExercise): The exercise data model containing all team variations.

    Returns:
        None
    """
    teams = list(exercise.statements.keys())
    if not teams:
        teams = ["Ομάδα Α"]

    # Assign default group according to AM 3323 (I=2 even, J=3 odd -> Group B)
    default_team = teams[0]
    if "Ομάδα Β" in teams:
        default_team = "Ομάδα Β"
    elif "Ομάδες Β και Γ" in teams:
        default_team = "Ομάδες Β και Γ"

    active_team_state = {"team": default_team}

    with ui.column().classes("dash-card w-full p-6 gap-5"):
        # Header Row: Question number, points, topic
        with ui.row().classes("items-center justify-between w-full border-b border-[var(--border)] pb-3 flex-wrap gap-2"):
            with ui.row().classes("items-center gap-3"):
                ui.html(
                    f'<span class="w-8 h-8 rounded-full bg-[var(--accent)] text-white flex items-center justify-center font-black text-sm">{exercise.number}</span>'
                )
                with ui.column().classes("gap-0"):
                    ui.label(exercise.title).classes("text-base font-black text-[var(--text-1)]")
                    ui.label(exercise.topic).classes("text-xs font-bold text-[var(--text-3)]")

            with ui.row().classes("items-center gap-2"):
                ui.html(
                    f'<span class="kpi-badge font-bold text-[var(--accent)]"><i class="fa-solid fa-star"></i> {exercise.points} Μονάδ{"α" if exercise.points == 1 else "ες"}</span>'
                )

        # Team Selector Navigation Row (placed at the top for immediate access)
        with ui.row().classes("items-center justify-between w-full flex-wrap gap-3"):
            button_container = ui.row().classes("gap-2 items-center flex-wrap")

            # AM 3323 Target Indicator
            with ui.row().classes("items-center gap-2 px-3 py-1 rounded-lg bg-[rgba(217,83,30,0.12)] border border-[var(--border-accent)] text-xs text-[var(--accent)] font-bold"):
                ui.html('<i class="fa-solid fa-user-graduate"></i>')
                ui.label("AM: 3323 (Ομάδα Β)")

        # Unified Big Gray Container holding Statement, Questions, and Steps together
        unified_box = ui.column().classes("w-full p-5 md:p-6 rounded-xl bg-[var(--surface-2)] border border-[var(--border)] gap-5 shadow-sm")

        def renderUnifiedContent(team_name: str) -> None:
            """Renders statement, questions, steps, and answers in a single unified box.

            Args:
                team_name (str): The name of the currently selected team.

            Returns:
                None
            """
            unified_box.clear()
            with unified_box:
                # 1. Problem Statement Section
                stmt = exercise.statements.get(team_name, "Δεν υπάρχει εκφώνηση για αυτή την ομάδα.")
                with ui.column().classes("w-full gap-2"):
                    with ui.row().classes("items-center gap-2 text-xs font-bold text-[var(--text-3)]"):
                        ui.html('<i class="fa-solid fa-file-pen text-[var(--accent)]"></i>')
                        ui.label(f"Εκφώνηση Θέματος ({team_name}):")
                    ui.html(f'<div class="text-sm text-[var(--text-1)] leading-relaxed pl-1">{stmt}</div>')

                # Subtle divider separating statement from detailed solution
                ui.html('<div class="w-full border-t border-[var(--border)] my-1"></div>')

                # 2. Sub-questions and Step-by-Step Derivations
                steps = exercise.steps.get(team_name, [])
                if steps:
                    with ui.column().classes("w-full gap-3"):
                        with ui.row().classes("items-center gap-2 text-xs font-bold text-[var(--text-3)]"):
                            ui.html('<i class="fa-solid fa-list-ol text-[#3b82f6]"></i>')
                            ui.label(f"Ερωτήματα & Αναλυτική Επίλυση ({team_name}):")

                        for idx, step_text in enumerate(steps, 1):
                            with ui.column().classes("w-full p-4 rounded-lg bg-[var(--bg-card)] border border-[var(--border)] gap-2 shadow-sm"):
                                with ui.row().classes("items-center gap-2"):
                                    ui.html(f'<span class="text-[11px] font-black px-2.5 py-0.5 rounded bg-[var(--surface-2)] text-[var(--accent)] border border-[var(--border)]">Ερώτημα / Βήμα {idx}</span>')
                                ui.html(f'<div class="text-xs md:text-sm text-[var(--text-1)] leading-relaxed pl-1 pt-1 overflow-x-auto">{step_text}</div>')

                # 3. Final Answer Box
                final_ans = exercise.final_answers.get(team_name, "")
                if final_ans:
                    with ui.row().classes("items-center justify-between w-full p-4 rounded-lg bg-[var(--callout-success-bg)] border border-[var(--callout-success-border)] flex-wrap gap-2"):
                        with ui.row().classes("items-center gap-2"):
                            ui.html('<i class="fa-solid fa-square-check text-[var(--green-ok)] text-base"></i>')
                            ui.label("Τελικό Αποτέλεσμα:").classes("font-bold text-xs text-[var(--callout-success-text)]")
                        ui.html(f'<div class="font-bold text-xs md:text-sm text-[var(--callout-success-text)]">{final_ans}</div>')

                # 4. Pitfalls and Professor Traps
                if exercise.pitfalls:
                    with ui.column().classes("callout-gotcha w-full gap-1"):
                        with ui.row().classes("items-center gap-2"):
                            ui.html('<i class="fa-solid fa-triangle-exclamation text-[var(--red-err)]"></i>')
                            ui.label("Παγίδες Εξέτασης & Σημεία Προσοχής:").classes("font-bold text-xs")
                        ui.html(f'<div class="text-xs pl-5 leading-relaxed">{exercise.pitfalls}</div>')

        def renderButtons() -> None:
            """Re-renders team buttons with active state highlight.

            Returns:
                None
            """
            button_container.clear()
            with button_container:
                for t in teams:
                    is_active = (t == active_team_state["team"])
                    if is_active:
                        ui.button(
                            t,
                            on_click=lambda name=t: selectTeam(name)
                        ).props("dense unelevated").classes(
                            "text-xs font-black px-3.5 py-1.5 bg-[var(--accent)] text-white shadow-sm rounded-lg"
                        )
                    else:
                        ui.button(
                            t,
                            on_click=lambda name=t: selectTeam(name)
                        ).props("dense outline").classes(
                            "text-xs font-bold px-3.5 py-1.5 text-[var(--text-2)] hover:text-[var(--text-1)] border-[var(--border-accent)] rounded-lg"
                        )

        def selectTeam(team_name: str) -> None:
            """Switches the active team, re-renders controls, and schedules KaTeX math formatting.

            Args:
                team_name (str): Selected team identifier.

            Returns:
                None
            """
            active_team_state["team"] = team_name
            renderButtons()
            renderUnifiedContent(team_name)
            ui.run_javascript("setTimeout(() => { if (typeof renderKaTeX === 'function') renderKaTeX(); }, 50);")

        # Initial render of buttons and content
        renderButtons()
        renderUnifiedContent(active_team_state["team"])


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
