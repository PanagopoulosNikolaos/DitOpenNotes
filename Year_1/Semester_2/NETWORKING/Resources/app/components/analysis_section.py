"""Open per-question solution sheet component (zero accordions, zero tabs).

Renders each exam question's worked solution in the exact order of the exam
paper: verbatim prompt, static MCQ option rows, given parameters, ordered
KaTeX derivation steps, supporting tables, final answer box, and tips.
"""

from nicegui import ui
from models.scenario import Scenario, ExamQuestion, AnalysisTable

_QUESTION_TYPE_BADGES = {
    "mcq": ("qtype-mcq", "Πολλαπλής Επιλογής", "fa-circle-question"),
    "computational": ("qtype-computational", "Υπολογιστικό Βήμα-Βήμα", "fa-calculator"),
    "theory": ("qtype-theory", "Θεωρητική Ανάλυση", "fa-book-open"),
    "comparison": ("qtype-comparison", "Συγκριτική Ανάλυση", "fa-scale-balanced"),
}


def _renderAnalysisTable(table: AnalysisTable) -> None:
    """Renders a single analysis or answer table as an open dark-table.

    Args:
        table (AnalysisTable): The table to render.

    Returns:
        None
    """
    rows_html = ""
    for row in table.rows:
        highlight_bg = "background: var(--card-bg-answer);" if row.highlight else ""
        cells_html = "".join(f"<td>{cell}</td>" for cell in row.cells)
        rows_html += f'<tr style="{highlight_bg}">{cells_html}</tr>'

    note_html = (
        f'<p class="text-xs text-[var(--text-3)] mt-1 mb-0">{table.note}</p>'
        if table.note
        else ""
    )

    ui.html(
        f"""
        <div class="overflow-x-auto w-full">
            <p class="text-xs font-bold text-[var(--text-1)] m-0 mt-2">{table.title}</p>
            <table class="dark-table">
                <thead>
                    <tr>{"".join(f"<th>{h}</th>" for h in table.headers)}</tr>
                </thead>
                <tbody>
                    {rows_html}
                </tbody>
            </table>
            {note_html}
        </div>
        """
    )


def _renderQuestionBlock(question: ExamQuestion) -> None:
    """Renders one exam question as an open, sequential solution sheet.

    Args:
        question (ExamQuestion): The question with its complete worked solution.

    Returns:
        None
    """
    badge_cls, badge_text, badge_icon = _QUESTION_TYPE_BADGES.get(
        question.question_type, ("qtype-theory", "Θεωρία", "fa-book-open")
    )

    with ui.column().classes(
        "w-full glass-panel gap-4 print-section print-solutions"
    ):
        # Question header: sub-number, title, type badge
        with ui.row().classes("items-center gap-3 flex-wrap w-full border-b border-[var(--border)] pb-3"):
            with ui.row().classes("items-center gap-2"):
                ui.html(
                    f'<span class="tag-label bg-[var(--card-bg-question)] text-[var(--accent-dark)] border border-[var(--card-border-question)]" '
                    f'style="font-size: 0.72rem; padding: 3px 8px;">{question.sub_number}</span>'
                )
                ui.html(f'<h3 class="text-base md:text-lg font-bold text-[var(--text-1)] m-0">{question.title}</h3>')
            ui.html(
                f'<span class="qtype-badge {badge_cls}"><i class="fa-solid {badge_icon} mr-1"></i>{badge_text}</span>'
            )

        # Full verbatim prompt
        ui.html(f'<div class="prompt-box">{question.prompt}</div>')

        # Static MCQ options: no click handlers anywhere
        if question.options:
            options_html = ""
            for opt in question.options:
                if opt.is_correct:
                    options_html += f"""
                    <div class="option-row option-correct">
                        <span class="option-letter">{opt.letter}</span>
                        <div class="flex-1">
                            <div class="text-sm text-[var(--text-1)]">{opt.text}</div>
                            <div class="option-why">{opt.explanation}</div>
                        </div>
                        <span class="option-correct-tag"><i class="fa-solid fa-circle-check"></i> ΣΩΣΤΟ</span>
                    </div>
                    """
                else:
                    options_html += f"""
                    <div class="option-row">
                        <span class="option-letter">{opt.letter}</span>
                        <div class="flex-1">
                            <div class="text-sm text-[var(--text-2)]">{opt.text}</div>
                            <div class="option-why"><i class="fa-solid fa-circle-xmark mr-1 text-[var(--red-err)]"></i>{opt.explanation}</div>
                        </div>
                    </div>
                    """
            with ui.column().classes("w-full gap-2"):
                ui.html(options_html)

        # Given parameters block (cross-referenced with canvas highlights)
        if question.given:
            given_html = "".join(
                f'<div class="given-row"><span class="given-label">{g.label}:</span>'
                f'<span class="given-value">{g.value}</span>'
                f'<span class="text-xs text-[var(--text-3)]">({g.source})</span></div>'
                for g in question.given
            )
            with ui.column().classes("w-full"):
                ui.html(
                    f"""
                    <div class="given-box">
                        <div class="step-chip" style="margin-bottom: 4px;"><i class="fa-solid fa-database"></i> Δεδομένα Εξέτασης (Given)</div>
                        {given_html}
                    </div>
                    """
                )

        # Ordered derivation steps (KaTeX display strings)
        if question.steps:
            with ui.column().classes("w-full gap-3"):
                for step in question.steps:
                    latex_html = (
                        f'<div class="katex-target">\\[{step.latex}\\]</div>'
                        if step.latex
                        else ""
                    )
                    result_html = (
                        f'<div class="step-result"><i class="fa-solid fa-arrow-right-long mr-1 text-[var(--amber)]"></i>{step.result}</div>'
                        if step.result
                        else ""
                    )
                    ui.html(
                        f"""
                        <div class="calc-step">
                            <span class="step-chip"><i class="fa-solid fa-shoe-prints"></i> {step.label}</span>
                            <div class="step-desc">{step.description}</div>
                            {latex_html}
                            {result_html}
                        </div>
                        """
                    )

        # Supporting answer tables
        for table in question.answer_tables:
            _renderAnalysisTable(table)

        # Final answer box
        if question.answer:
            ui.html(
                f"""
                <div class="answer-final">
                    <i class="fa-solid fa-flag-checkered"></i>
                    <div><strong>Τελική Απάντηση:</strong> {question.answer}</div>
                </div>
                """
            )

        # Exam tips and traps
        if question.tips:
            tips_html = "".join(
                f'<div class="tip-item"><i class="fa-solid fa-triangle-exclamation"></i><span>{tip}</span></div>'
                for tip in question.tips
            )
            with ui.column().classes("w-full gap-1 pt-1 border-t border-[var(--border)]"):
                ui.html(
                    f'<div class="step-chip" style="margin-bottom: 2px;"><i class="fa-solid fa-lightbulb"></i> Παγίδες & Σημεία Επαλήθευσης</div>{tips_html}'
                )


def renderAnalysisSection(scenario: Scenario) -> None:
    """Renders the complete open solution sheet for every exam question in paper order.

    Args:
        scenario (Scenario): The active scenario containing all questions.

    Returns:
        None
    """
    with ui.column().classes("w-full gap-6"):
        with ui.row().classes("items-center gap-3 no-print"):
            ui.html('<i class="fa-solid fa-magnifying-glass-chart text-[var(--accent)] text-xl"></i>')
            ui.html('<h2 class="text-xl md:text-2xl font-bold text-[var(--text-1)] m-0">Λυμένο Φύλλο: Λύσεις ανά Θέμα (Βήμα-Βήμα, στην Ίδια Δομή)</h2>')

        current_thema = None
        for question in scenario.questions:
            # Themata divider mirrors the exact structure of the exam paper
            if question.thema != current_thema:
                current_thema = question.thema
                ui.html(
                    f"""
                    <div class="thema-divider">
                        <i class="fa-solid fa-layer-group text-[var(--accent)]"></i>
                        <span class="thema-text">{question.thema}: {question.thema_title}</span>
                        <span class="tag-label bg-[var(--badge-bg)] text-[var(--text-2)]">2.5 μονάδες</span>
                    </div>
                    """
                )
            _renderQuestionBlock(question)

        # Scenario-level analysis tables (reference/summary tables)
        if scenario.analysis_tables:
            with ui.column().classes("w-full glass-panel gap-4 print-section print-tables"):
                with ui.row().classes("items-center gap-2 border-b border-[var(--border)] pb-3 w-full"):
                    ui.html('<i class="fa-solid fa-table text-[var(--accent)] no-print"></i>')
                    ui.html('<h3 class="text-lg font-bold text-[var(--text-1)] m-0">Πίνακες Ανάλυσης & Αναφοράς του Θέματος</h3>')
                for table in scenario.analysis_tables:
                    _renderAnalysisTable(table)

        # Protocol layer mapping (OSI <-> TCP/IP), when the scenario provides it
        if scenario.layers:
            with ui.column().classes("w-full glass-panel gap-4 print-section print-tables"):
                with ui.row().classes("items-center gap-2 border-b border-[var(--border)] pb-3 w-full"):
                    ui.html('<i class="fa-solid fa-layer-group text-blue-500 no-print"></i>')
                    ui.html('<h3 class="text-lg font-bold text-blue-600 dark:text-blue-300 m-0">Αντιστοίχιση Επιπέδων OSI &harr; TCP/IP (PDUs & Πρωτόκολλα)</h3>')
                layer_rows = "".join(
                    f"<tr><td><strong>{l.osi_position}. {l.osi_name}</strong><br>"
                    f'<span class="text-xs text-[var(--text-3)]">{l.osi_role}</span></td>'
                    f"<td><strong>{l.tcpip_name}</strong></td>"
                    f"<td><code>{l.pdu}</code></td>"
                    f"<td>{l.protocols}</td></tr>"
                    for l in scenario.layers
                )
                ui.html(
                    f"""
                    <div class="overflow-x-auto w-full">
                        <table class="dark-table">
                            <thead>
                                <tr>
                                    <th>Μοντέλο OSI (Επίπεδο & Ρόλος)</th>
                                    <th>Στοίβα TCP/IP</th>
                                    <th>PDU</th>
                                    <th>Αντιπροσωπευτικά Πρωτόκολλα</th>
                                </tr>
                            </thead>
                            <tbody>{layer_rows}</tbody>
                        </table>
                    </div>
                    """
                )
