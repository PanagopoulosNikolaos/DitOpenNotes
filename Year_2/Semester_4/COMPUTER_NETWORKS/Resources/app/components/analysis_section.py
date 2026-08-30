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
    with ui.column().classes("w-full p-6 rounded-2xl bg-[#201f1d] border border-[rgba(255,255,255,0.08)] gap-4"):
        # Question Title and Metadata Header
        with ui.row().classes("items-center justify-between w-full flex-wrap gap-2 border-b border-[rgba(255,255,255,0.06)] pb-3"):
            with ui.row().classes("items-center gap-3"):
                ui.html(
                    f'<span class="w-8 h-8 rounded-full bg-[#e06b3a] text-white flex items-center justify-center font-bold text-sm shadow-md">'
                    f'{q.question_number}</span>'
                )
                ui.html(f'<h3 class="text-base md:text-lg font-bold text-[#f4f1ea] m-0">{q.title}</h3>')

            with ui.row().classes("gap-2 items-center"):
                ui.label(q.question_type).classes(
                    "px-2.5 py-1 rounded-full text-xs font-semibold bg-[#141413] border border-[rgba(224,107,58,0.3)] text-[#fed7aa]"
                )
                if q.related_theory_topic:
                    ui.label(f"Θεωρία: {q.related_theory_topic}").classes(
                        "px-2.5 py-1 rounded-full text-xs bg-[rgba(79,142,201,0.15)] text-blue-300 border border-[rgba(79,142,201,0.3)]"
                    )

        # Question Prompt with LaTeX Support
        ui.markdown(q.prompt_text).classes("text-sm text-[#f4f1ea] leading-relaxed")

        # Multiple-choice interactive options
        if q.options:
            feedback_container = ui.column().classes("w-full gap-2 mt-1")

            def handleOptionClick(opt_letter: str, is_corr: bool, exp: str) -> None:
                """Handles option selection click and renders feedback with LaTeX math."""
                feedback_container.clear()
                with feedback_container:
                    border_color = "rgba(16,185,129,0.4)" if is_corr else "rgba(239,68,68,0.4)"
                    bg_color = "rgba(16,185,129,0.1)" if is_corr else "rgba(239,68,68,0.1)"
                    text_color = "text-emerald-300" if is_corr else "text-red-300"
                    status_text = "Σωστή Επιλογή" if is_corr else "Εσφαλμένη Επιλογή"

                    with ui.column().classes(f"w-full p-4 rounded-xl border {text_color} gap-1.5").style(f"background: {bg_color}; border-color: {border_color};"):
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
                        "p-3.5 rounded-xl bg-[#141413] border border-[rgba(255,255,255,0.06)] "
                        "hover:border-[#e06b3a] hover:bg-[#1c1b1a] cursor-pointer transition-all gap-1"
                    ).on("click", lambda _, l=opt_letter, c=is_correct, e=opt_exp: handleOptionClick(l, c, e)):
                        with ui.row().classes("items-center gap-2"):
                            ui.label(f"[{opt_letter}]").classes(
                                "font-bold font-mono " + ("text-emerald-400" if is_correct else "text-stone-400")
                            )
                            ui.markdown(opt_text).classes("text-stone-200 font-medium")

        # Step-by-step calculation steps with LaTeX Math
        if q.calculation_steps:
            with ui.column().classes("w-full mt-3 gap-3 border-t border-[rgba(255,255,255,0.06)] pt-3"):
                ui.label("Αναλυτική Βήμα-προς-Βήμα Επίλυση (Detailed LaTeX Derivations):").classes("text-xs font-bold text-[#fed7aa]")
                for step in q.calculation_steps:
                    with ui.column().classes("w-full step-node text-xs"):
                        ui.html(f'<div class="step-bullet">{step.step_number}</div>')
                        with ui.column().classes("gap-1.5"):
                            ui.label(step.title).classes("font-bold text-[#f4f1ea]")
                            if step.formula:
                                with ui.row().classes("w-full formula-box"):
                                    ui.markdown(f"**Μαθηματικός Τύπος:** $${step.formula}$$")
                            if step.substitution:
                                with ui.row().classes("w-full formula-box"):
                                    ui.markdown(f"**Αριθμητική Αντικατάσταση:** $${step.substitution}$$")
                            if step.result:
                                with ui.row().classes("items-center gap-2 mt-1"):
                                    ui.label("Τελικό Αποτέλεσμα:").classes("text-stone-400 font-medium")
                                    ui.markdown(f"**$${step.result}$$**").classes("font-bold text-emerald-400")
                            if step.rationale:
                                ui.markdown(f"*{step.rationale}*").classes("text-xs text-[#b5b0a4] mt-0.5")

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
    with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-6"):
        with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
            ui.html('<i class="fa-solid fa-list-check text-[#e06b3a] text-xl"></i>')
            with ui.column().classes("gap-0"):
                ui.html('<h2 class="text-xl font-bold gradient-title m-0">Αναλυτική Επίλυση Θεμάτων & Ασκήσεων</h2>')
                ui.label(f"Περιλαμβάνει {len(scenario.questions)} θέματα με πλήρη αιτιολόγηση, μαθηματική επίλυση και LaTeX τύπους").classes("text-xs text-[#b5b0a4]")

        for q in scenario.questions:
            renderQuestionBlock(q)
