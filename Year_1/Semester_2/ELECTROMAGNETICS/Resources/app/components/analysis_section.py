"""Detailed question analysis and step-by-step solution sheet component.

Renders all questions sequentially as open, stacked master solution cards without
any accordions, tabs, collapsibles, or reveal controls.
"""

from nicegui import ui
from models.scenario import Scenario, ExamQuestion


def renderQuestionSolution(q: ExamQuestion) -> None:
    """Renders an individual question solution block openly per Section 8 specifications.

    Args:
        q (ExamQuestion): The exam question object with options or derivations.

    Returns:
        None
    """
    type_icon = "fa-solid fa-circle-question"
    if "Calculat" in q.question_type or "Άσκηση" in q.title or q.calculation_steps:
        type_icon = "fa-solid fa-calculator text-[var(--accent)]"
    else:
        type_icon = "fa-solid fa-lightbulb text-[var(--amber)]"

    with ui.column().classes("w-full glass-panel gap-4 p-6 border border-[var(--border)]"):
        # Header: Question Number, Title, Type Badges
        with ui.row().classes("w-full justify-between items-center flex-wrap gap-2 pb-3 border-b border-[var(--border)]"):
            with ui.row().classes("items-center gap-3"):
                ui.html(f'<i class="{type_icon} text-lg"></i>')
                ui.html(f'<h3 class="text-base md:text-lg font-bold text-[var(--text-1)] m-0">Θέμα {q.question_number}: {q.title}</h3>')

            with ui.row().classes("items-center gap-2 flex-wrap"):
                ui.html(f'<span class="px-2.5 py-1 rounded-full text-xs font-bold bg-[var(--surface-2)] text-[var(--accent)] border border-[var(--border-accent)]">{q.question_type}</span>')
                if q.related_theory_topic:
                    ui.html(f'<span class="px-2.5 py-1 rounded-full text-xs font-semibold bg-[var(--surface-2)] text-[var(--blue-action)] border border-[var(--border)]"><i class="fa-solid fa-book-bookmark mr-1"></i>{q.related_theory_topic}</span>')

        # Question Prompt Text (verbatim)
        with ui.column().classes("w-full p-4 rounded-xl bg-[var(--card-bg-subtle)] border border-[var(--border)] gap-2"):
            with ui.row().classes("items-center gap-2 text-[var(--text-3)] text-xs font-bold"):
                ui.html('<i class="fa-solid fa-file-lines"></i>')
                ui.label("Εκφώνηση Θέματος")
            ui.markdown(q.prompt_text).classes("text-sm text-[var(--text-1)] leading-relaxed latex-target")

        # Multiple-Choice Static Options (Open Solution Sheet: Section 8)
        if q.options:
            with ui.column().classes("w-full gap-2 mt-2"):
                with ui.row().classes("items-center gap-2 text-xs font-bold text-[var(--text-2)]"):
                    ui.html('<i class="fa-solid fa-list-check text-[var(--green-ok)]"></i>')
                    ui.label("Επιλογές Απάντησης & Αιτιολόγηση")

                with ui.column().classes("w-full gap-2"):
                    for opt in q.options:
                        is_corr = opt.is_correct
                        opt_class = "option-row-static correct" if is_corr else "option-row-static"
                        badge_class = "option-badge correct" if is_corr else "option-badge"
                        status_badge = (
                            '<span class="ml-auto text-xs font-bold text-[var(--green-ok)] flex items-center gap-1">'
                            '<i class="fa-solid fa-circle-check"></i> Σωστή Απάντηση</span>'
                            if is_corr
                            else ""
                        )

                        with ui.column().classes(f"w-full {opt_class} gap-1"):
                            with ui.row().classes("w-full items-center gap-2"):
                                ui.html(f'<span class="{badge_class}">{opt.letter}</span>')
                                ui.markdown(opt.text).classes("text-sm font-semibold text-[var(--text-1)] latex-target")
                                if status_badge:
                                    ui.html(status_badge)
                            # Inline distractor explanation
                            if opt.explanation:
                                ui.markdown(f"*{opt.explanation}*").classes("text-xs text-[var(--text-3)] ml-8 latex-target leading-normal")

        # Computational Exercise: Given Parameters Block
        if q.given_parameters:
            with ui.column().classes("w-full p-3.5 rounded-xl bg-[var(--surface-2)] border border-[var(--border)] gap-2 mt-1"):
                with ui.row().classes("items-center gap-2 text-xs font-bold text-[var(--accent)]"):
                    ui.html('<i class="fa-solid fa-clipboard-list"></i>')
                    ui.label("Δεδομένα & Παράμετροι Εκφώνησης")
                with ui.grid().classes("grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-2 w-full text-xs"):
                    for param in q.given_parameters:
                        with ui.row().classes("items-center gap-2 p-2 rounded-lg bg-[var(--canvas-bg)] border border-[var(--border)]"):
                            ui.html(f'<span class="font-bold text-[var(--accent)] font-mono">${param.symbol}$</span>')
                            ui.html(f'<span class="text-[var(--text-1)] font-medium">${param.value}$</span>')
                            ui.html(f'<span class="text-[var(--text-3)] text-[0.7rem]">({param.description})</span>')

        # Computational Exercise: Step-by-Step KaTeX Derivation
        if q.calculation_steps:
            with ui.column().classes("w-full gap-3 mt-2"):
                with ui.row().classes("items-center gap-2 text-xs font-bold text-[var(--text-2)]"):
                    ui.html('<i class="fa-solid fa-square-root-variable text-[var(--accent)]"></i>')
                    ui.label("Αναλυτική Βηματική Παραγωγή & Υπολογισμοί")

                for step in q.calculation_steps:
                    with ui.column().classes("w-full derivation-step-card gap-2"):
                        # Step header
                        with ui.row().classes("w-full justify-between items-center"):
                            with ui.row().classes("items-center gap-2"):
                                ui.html(f'<span class="w-6 h-6 rounded-full bg-[var(--accent)] text-white flex items-center justify-center font-bold text-xs">{step.step_number}</span>')
                                ui.label(step.title).classes("text-sm font-bold text-[var(--text-1)]")

                        # Formula & substitution in KaTeX
                        if step.formula:
                            with ui.column().classes("w-full p-2.5 rounded-lg bg-[var(--canvas-bg)] border border-[var(--border)] gap-1"):
                                ui.label("Μαθηματικός Τύπος:").classes("text-[0.65rem] font-bold text-[var(--text-3)] uppercase")
                                ui.markdown(f"$$\n{step.formula}\n$$").classes("text-sm text-[var(--text-1)] latex-target")

                        if step.substitution:
                            with ui.column().classes("w-full p-2.5 rounded-lg bg-[var(--canvas-bg)] border border-[var(--border)] gap-1"):
                                ui.label("Αριθμητική Αντικατάσταση:").classes("text-[0.65rem] font-bold text-[var(--text-3)] uppercase")
                                ui.markdown(f"$$\n{step.substitution}\n$$").classes("text-sm text-[var(--text-1)] latex-target")

                        if step.result:
                            with ui.row().classes("w-full items-center justify-between p-2.5 rounded-lg bg-[rgba(5,150,105,0.08)] border border-[var(--green-ok)]"):
                                with ui.row().classes("items-center gap-2"):
                                    ui.html('<i class="fa-solid fa-check text-[var(--green-ok)] text-xs"></i>')
                                    ui.label("Μερικό Αποτέλεσμα:").classes("text-xs font-bold text-[var(--green-ok)]")
                                ui.markdown(f"**${step.result}$**").classes("text-sm font-bold text-[var(--text-1)] latex-target")

                        if step.rationale:
                            with ui.row().classes("items-start gap-2 text-xs text-[var(--text-2)]"):
                                ui.html('<i class="fa-solid fa-circle-info text-[var(--text-3)] text-xs mt-0.5"></i>')
                                ui.markdown(step.rationale).classes("leading-relaxed latex-target")

        # Prominent Final Answer Highlight Box
        if q.final_answer:
            with ui.column().classes("w-full result-highlight-box gap-1"):
                with ui.row().classes("items-center gap-2 text-xs font-bold text-[var(--green-ok)]"):
                    ui.html('<i class="fa-solid fa-flag-checkered"></i>')
                    ui.label("Τελικό Αποτέλεσμα")
                ui.markdown(f"**{q.final_answer}**").classes("text-base font-black text-[var(--text-1)] latex-target")

        # Physics Justification & Rationale
        if q.detailed_justification:
            with ui.column().classes("w-full p-3.5 rounded-xl bg-[var(--card-bg-subtle)] border border-[var(--border)] gap-1.5"):
                with ui.row().classes("items-center gap-2 text-xs font-bold text-[var(--blue-action)]"):
                    ui.html('<i class="fa-solid fa-atom"></i>')
                    ui.label("Φυσική Ερμηνεία & Αιτιολόγηση")
                ui.markdown(q.detailed_justification).classes("text-xs text-[var(--text-2)] leading-relaxed latex-target")

        # Common Traps / Pitfalls
        if q.common_pitfalls:
            with ui.column().classes("w-full p-3.5 rounded-xl bg-[rgba(239,68,68,0.06)] border border-red-400/40 gap-1.5"):
                with ui.row().classes("items-center gap-2 text-xs font-bold text-red-500"):
                    ui.html('<i class="fa-solid fa-triangle-exclamation"></i>')
                    ui.label("Συνήθεις Παγίδες & Σημεία Προσοχής")
                for pitfall in q.common_pitfalls:
                    with ui.row().classes("items-start gap-2 text-xs text-[var(--text-2)]"):
                        ui.html('<span class="text-red-500 font-bold">•</span>')
                        ui.markdown(pitfall).classes("leading-relaxed latex-target")


def renderAnalysisSection(scenario: Scenario) -> None:
    """Renders all exam questions as an open, sequentially stacked master solution sheet.

    Args:
        scenario (Scenario): The active scenario containing questions and derivations.

    Returns:
        None
    """
    with ui.column().classes("w-full gap-6").props('id="solution-sheet-section"'):
        with ui.row().classes("w-full justify-between items-center"):
            with ui.row().classes("items-center gap-3"):
                ui.html('<i class="fa-solid fa-graduation-cap text-[var(--accent)] text-2xl"></i>')
                with ui.column().classes("gap-0"):
                    ui.html('<h2 class="text-xl md:text-2xl font-bold text-[var(--text-1)] m-0">Αναλυτικό Φύλλο Λύσεων & Υπολογισμών</h2>')
                    ui.label("Πλήρεις αναλυτικές λύσεις, KaTeX παραγωγές και αιτιολογήσεις ανοιχτά για μελέτη.").classes("text-xs text-[var(--text-2)]")

        # Stacked open question blocks sequentially
        for q in scenario.questions:
            renderQuestionSolution(q)

