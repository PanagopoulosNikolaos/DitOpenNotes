"""Detailed question analysis and step-by-step justifications component with LaTeX support."""

from nicegui import ui
from models.scenario import NetworkScenario, ExamQuestion


def renderQuestionBlock(q: ExamQuestion) -> None:
    """Renders an individual question analysis block with interactive option testing and LaTeX.

    Args:
        q (ExamQuestion): The exam question object.

    Returns:
        None
    """
    # Determine icon and accent color by question type for visual distinction
    type_icon = "fa-solid fa-circle-question"
    if "Calculat" in q.question_type or "Άσκηση" in q.title or q.calculation_steps:
        type_icon = "fa-solid fa-calculator"
    elif "Algorithm" in q.question_type or "Dijkstra" in q.title:
        type_icon = "fa-solid fa-diagram-project"

    # Collapsible accordion panel with full width click header
    with ui.expansion(
        text=f"Ερώτηση {q.question_number}: {q.title}",
        icon=type_icon,
    ).classes(
        "w-full rounded-2xl bg-[#201f1d] border border-[rgba(255,255,255,0.08)] "
        "text-[#f4f1ea] font-semibold text-sm transition-all "
        "hover:border-[rgba(224,107,58,0.4)]"
    ).props("dense header-class='p-3'"):
        with ui.column().classes("w-full gap-4 px-3 pb-3 pt-1 latex-target"):
            # Question type + theory topic tags
            with ui.row().classes("items-center gap-2 flex-wrap"):
                ui.label(q.question_type).classes(
                    "px-3 py-1 rounded-full text-xs font-semibold bg-[#141413] border border-[rgba(224,107,58,0.35)] text-[#fed7aa]"
                )
                if q.related_theory_topic:
                    ui.label(f"Θεωρία: {q.related_theory_topic}").classes(
                        "px-3 py-1 rounded-full text-xs bg-[rgba(79,142,201,0.15)] text-blue-300 border border-[rgba(79,142,201,0.3)]"
                    )

            # Question prompt with LaTeX support
            with ui.column().classes("w-full p-4 rounded-xl bg-[#141413] border border-[rgba(255,255,255,0.06)] gap-1.5"):
                with ui.row().classes("items-center gap-2 text-[#78756d] text-xs font-bold mb-1"):
                    ui.html('<i class="fa-solid fa-question"></i>')
                    ui.label("Εκφώνηση")
                ui.markdown(q.prompt_text).classes("text-sm text-[#f4f1ea] leading-relaxed")

            # Multiple-choice interactive options
            if q.options:
                feedback_container = ui.column().classes("w-full gap-2 mt-1")

                def handleOptionClick(opt_letter: str, is_corr: bool, exp: str) -> None:
                    """Handles option selection click and renders feedback with LaTeX math."""
                    feedback_container.clear()
                    with feedback_container:
                        border_color = "rgba(16,185,129,0.4)" if is_corr else "rgba(239,68,68,0.4)"
                        bg_color = "rgba(16,185,129,0.08)" if is_corr else "rgba(239,68,68,0.08)"
                        text_color = "text-emerald-300" if is_corr else "text-red-300"
                        status_text = "Σωστή Επιλογή" if is_corr else "Εσφαλμένη Επιλογή"

                        with ui.column().classes(f"w-full p-4 rounded-xl border {text_color} gap-1.5").style(
                            f"background: {bg_color}; border-color: {border_color};"
                        ):
                            with ui.row().classes("items-center gap-2 font-bold text-xs"):
                                icon_name = "check" if is_corr else "xmark"
                                ui.html(f'<i class="fa-solid fa-{icon_name}"></i>')
                                ui.label(f"Επιλογή {opt_letter}: {status_text}")
                            ui.markdown(exp).classes("text-xs text-[#f4f1ea] leading-relaxed")
                    
                    ui.run_javascript("if (typeof renderAllLatex === 'function') renderAllLatex();")

                with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-3 w-full text-xs mt-1"):
                    for opt in q.options:
                        is_correct = opt.is_correct
                        opt_letter = opt.letter
                        opt_text = opt.text
                        opt_exp = opt.explanation

                        with ui.card().classes(
                            "option-card p-3.5 rounded-xl bg-[#141413] border border-[rgba(255,255,255,0.06)] "
                            "hover:border-[#e06b3a] hover:bg-[#1c1b1a] cursor-pointer transition-all gap-1"
                        ).on("click", lambda _, l=opt_letter, c=is_correct, e=opt_exp: handleOptionClick(l, c, e)):
                            with ui.row().classes("items-center gap-2 w-full"):
                                ui.label(f"[{opt_letter}]").classes(
                                    "font-bold font-mono " + ("text-emerald-400" if is_correct else "text-stone-400")
                                )
                                ui.markdown(opt_text).classes("text-stone-200 font-medium")

            # Step-by-step calculation steps — rendered as numbered step cards
            if q.calculation_steps:
                with ui.column().classes("w-full mt-2 gap-0 border-t border-[rgba(255,255,255,0.06)] pt-4"):
                    with ui.row().classes("items-center gap-2 mb-3"):
                        ui.html('<i class="fa-solid fa-list-ol text-blue-400 text-sm"></i>')
                        ui.label("Αναλυτική Βηματική Επίλυση").classes("text-sm font-bold text-[#fed7aa]")

                    for step in q.calculation_steps:
                        with ui.row().classes("w-full gap-3 items-start mb-4"):
                            # Step number pill
                            ui.html(
                                f'<div class="flex-shrink-0 w-8 h-8 rounded-full bg-[#e06b3a] text-white '
                                f'flex items-center justify-center font-bold text-xs shadow-md '
                                f'shadow-orange-900/40 mt-0.5">{step.step_number}</div>'
                            )
                            # Step content card
                            with ui.column().classes(
                                "flex-1 p-4 rounded-xl bg-[#141413] border border-[rgba(255,255,255,0.07)] gap-2.5"
                            ):
                                # Step title
                                ui.label(step.title).classes("text-sm font-bold text-[#f4f1ea]")

                                # Formula row
                                if step.formula:
                                    with ui.column().classes("w-full formula-box gap-0.5"):
                                        ui.label("Τύπος:").classes("text-[0.65rem] font-bold text-[#78756d] uppercase tracking-wider")
                                        ui.markdown(f"$$${step.formula}$$$").classes("text-[#fed7aa]")

                                # Substitution row
                                if step.substitution:
                                    with ui.column().classes("w-full formula-box gap-0.5"):
                                        ui.label("Αντικατάσταση:").classes("text-[0.65rem] font-bold text-[#78756d] uppercase tracking-wider")
                                        ui.markdown(f"$$${step.substitution}$$$").classes("text-[#fed7aa]")

                                # Result highlight
                                if step.result:
                                    with ui.row().classes(
                                        "w-full items-center gap-2 p-2.5 rounded-lg "
                                        "bg-[rgba(16,185,129,0.08)] border border-[rgba(16,185,129,0.25)]"
                                    ):
                                        ui.html('<i class="fa-solid fa-circle-check text-emerald-400 text-xs"></i>')
                                        ui.label("Αποτέλεσμα:").classes("text-xs font-bold text-emerald-400")
                                        ui.markdown(f"**$$${step.result}$$$**").classes("text-emerald-300 font-bold text-sm")

                                # Rationale note
                                if step.rationale:
                                    with ui.row().classes("items-start gap-1.5 mt-0.5"):
                                        ui.html('<i class="fa-solid fa-circle-info text-[#78756d] text-xs mt-0.5"></i>')
                                        ui.markdown(step.rationale).classes("text-xs text-[#b5b0a4] leading-relaxed")

            # Detailed Justification Block with LaTeX
            if q.detailed_justification:
                with ui.column().classes("w-full p-4 rounded-xl bg-[#141413] border border-[rgba(224,107,58,0.2)] gap-2 text-xs"):
                    with ui.row().classes("items-center gap-2 text-[#e06b3a] font-bold"):
                        ui.html('<i class="fa-solid fa-lightbulb"></i>')
                        ui.label("Αιτιολόγηση & Θεωρητική Τεκμηρίωση")
                    ui.markdown(q.detailed_justification).classes("text-stone-300 leading-relaxed")

            # Common Pitfalls Callout
            if q.common_pitfalls:
                with ui.column().classes("w-full p-3.5 rounded-xl bg-[rgba(239,68,68,0.08)] border border-[rgba(239,68,68,0.25)] gap-1 text-xs"):
                    with ui.row().classes("items-center gap-2 text-red-400 font-bold"):
                        ui.html('<i class="fa-solid fa-triangle-exclamation"></i>')
                        ui.label("Συχνές Παγίδες Εξετάσεων:")
                    for pit in q.common_pitfalls:
                        ui.markdown(f"- {pit}").classes("text-stone-300")


def renderAnalysisSection(scenario: NetworkScenario) -> None:
    """Renders the comprehensive question analysis section for the active scenario.

    Args:
        scenario (NetworkScenario): The active scenario object.

    Returns:
        None
    """
    part_a = [q for q in scenario.questions if q.options and not q.calculation_steps]
    part_b = [q for q in scenario.questions if q.calculation_steps or not q.options]

    with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-6"):
        with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
            ui.html('<i class="fa-solid fa-list-check text-[#e06b3a] text-xl"></i>')
            with ui.column().classes("gap-0"):
                ui.html('<h2 class="text-xl font-bold gradient-title m-0">Αναλυτική Επίλυση Θεμάτων & Ασκήσεων</h2>')
                ui.label(
                    f"Περιλαμβάνει {len(scenario.questions)} θέματα με πλήρη αιτιολόγηση, μαθηματική επίλυση και LaTeX τύπους. "
                    "Κλικ σε κάθε θέμα για ανάπτυξη."
                ).classes("text-xs text-[#b5b0a4]")

        # Part A: Theory & Multiple Choice
        if part_a:
            with ui.column().classes("w-full gap-3"):
                with ui.row().classes("items-center gap-2.5 py-2 px-4 rounded-xl bg-[rgba(224,107,58,0.1)] border border-[rgba(224,107,58,0.25)]"):
                    ui.html('<i class="fa-solid fa-circle-question text-[#e06b3a]"></i>')
                    ui.html('<h3 class="text-sm font-bold text-[#fed7aa] m-0">Μέρος Α: Ερωτήσεις Θεωρίας & Πολλαπλής Επιλογής</h3>')
                for q in part_a:
                    renderQuestionBlock(q)

        # Section divider between Part A and Part B
        if part_a and part_b:
            with ui.row().classes("w-full items-center gap-3 my-2"):
                ui.html('<div class="flex-1 h-px bg-[rgba(255,255,255,0.07)]"></div>', tag="div")
                ui.html(
                    '<span class="text-xs text-[#78756d] font-mono uppercase tracking-widest px-2">Μέρος Β</span>',
                    tag="div",
                )
                ui.html('<div class="flex-1 h-px bg-[rgba(255,255,255,0.07)]"></div>', tag="div")

        # Part B: Exercises & Calculations
        if part_b:
            with ui.column().classes("w-full gap-3"):
                with ui.row().classes("items-center gap-2.5 py-2 px-4 rounded-xl bg-[rgba(79,142,201,0.1)] border border-[rgba(79,142,201,0.25)]"):
                    ui.html('<i class="fa-solid fa-calculator text-blue-400"></i>')
                    ui.html('<h3 class="text-sm font-bold text-blue-300 m-0">Μέρος Β: Ασκήσεις & Αναλυτική Επίλυση</h3>')
                for q in part_b:
                    renderQuestionBlock(q)

        # Fallback: if grouping logic puts all in one bucket
        if not part_a and not part_b:
            for q in scenario.questions:
                renderQuestionBlock(q)
