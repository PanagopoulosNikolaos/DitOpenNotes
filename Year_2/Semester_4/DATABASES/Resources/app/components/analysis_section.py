"""Detailed analysis section component covering Entities, Attributes, Keys, and Relationships."""

from nicegui import ui
from models.scenario import Scenario


def renderAnalysisSection(scenario: Scenario) -> None:
    """Renders the comprehensive ER analysis justifications and breakdown.

    Args:
        scenario (Scenario): The active scenario containing detailed model analysis.

    Returns:
        None
    """
    with ui.column().classes("w-full gap-6"):
        with ui.row().classes("items-center gap-3 no-print"):
            ui.html('<i class="fa-solid fa-magnifying-glass-chart text-[var(--accent)] text-xl"></i>')
            ui.html('<h2 class="text-xl md:text-2xl font-bold text-[var(--text-1)] m-0">Detailed Element Identification & Rationale</h2>')

        # 1. Entities & Types (Excluded from Print)
        with ui.column().classes("w-full glass-panel gap-4 no-print"):
            with ui.row().classes("items-center gap-2 border-b border-[var(--border)] pb-3 w-full"):
                ui.html('<i class="fa-solid fa-cubes text-blue-500"></i>')
                ui.html('<h3 class="text-lg font-bold text-blue-600 dark:text-[#93c5fd] m-0">1. Entities & Types</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full"):
                for idx, ent in enumerate(scenario.entities, start=1):
                    border_color = (
                        "border-purple-300 dark:border-purple-500/50 bg-[var(--card-bg-ent-weak)]"
                        if ent.is_weak
                        else "border-blue-300 dark:border-blue-500/30 bg-[var(--card-bg-ent-strong)]"
                    )
                    text_color = "text-purple-700 dark:text-purple-300" if ent.is_weak else "text-blue-700 dark:text-blue-300"
                    with ui.column().classes(f"p-4 rounded-xl border {border_color} gap-2 shadow-sm"):
                        with ui.row().classes("items-center gap-2"):
                            ui.label(f"{idx}. {ent.name}").classes(f"font-bold {text_color} text-sm")
                            ui.label(f"({ent.entity_type})").classes("text-xs text-[var(--text-2)]")
                        ui.html(f'<p class="text-xs text-[var(--text-2)] leading-relaxed m-0"><strong>Rationale:</strong> {ent.justification}</p>')

        # 2. Attributes & Types (Included in Print)
        with ui.column().classes("w-full glass-panel gap-4 print-section print-attributes"):
            with ui.row().classes("items-center gap-2 border-b border-[var(--border)] pb-3 w-full"):
                ui.html('<i class="fa-solid fa-list-check text-emerald-500 no-print"></i>')
                ui.html('<h3 class="text-lg font-bold text-emerald-600 dark:text-[#86efac] m-0">2. Attributes & Classification</h3>')

            with ui.column().classes("space-y-4 w-full attr-card-container"):
                for ent in scenario.entities:
                    with ui.column().classes("p-4 rounded-xl bg-[var(--card-bg-attr)] border border-[var(--card-border-attr)] gap-2 w-full attr-card print-avoid-break shadow-sm"):
                        with ui.row().classes("items-center gap-2"):
                            ui.html('<i class="fa-solid fa-cube text-emerald-500 text-xs no-print"></i>')
                            ui.label(f"{ent.name}:").classes("font-bold text-emerald-700 dark:text-[#86efac] text-sm")

                        with ui.element("ul").classes("list-disc list-inside text-xs text-[var(--text-2)] space-y-1.5 m-0 pl-1"):
                            for attr in ent.attributes:
                                pk_tag = '<span class="text-orange-600 dark:text-[#fdba74] font-bold"> [PK]</span>' if attr.is_pk else ""
                                cand_tag = '<span class="text-amber-600 dark:text-[#fde68a] font-bold"> [Candidate]</span>' if attr.is_candidate else ""
                                part_tag = '<span class="text-yellow-600 dark:text-[#fef08a] font-bold"> [Partial Key]</span>' if attr.is_partial else ""
                                comp_str = f" (Decomposed into: {', '.join(attr.components)})" if attr.components else ""
                                notes_str = f" — <em>{attr.notes}</em>" if attr.notes else ""
                                item_html = (
                                    f'<code>{attr.name}</code>{pk_tag}{cand_tag}{part_tag}: '
                                    f'{attr.attr_type}{comp_str}{notes_str}'
                                )
                                ui.html(f"<li>{item_html}</li>")

                # Relationship Attributes
                if scenario.relationship_attributes:
                    with ui.column().classes("p-4 rounded-xl bg-[var(--card-bg-rel-attr)] border border-[var(--card-border-rel-attr)] gap-2 w-full attr-card-rel print-avoid-break shadow-sm"):
                        with ui.row().classes("items-center gap-2"):
                            ui.html('<i class="fa-solid fa-link text-rose-500 text-xs no-print"></i>')
                            ui.label("Relationship Attributes:").classes("font-bold text-rose-700 dark:text-[#fda4af] text-sm")

                        with ui.element("ul").classes("list-disc list-inside text-xs text-[var(--text-2)] space-y-1.5 m-0 pl-1"):
                            for rel_attr in scenario.relationship_attributes:
                                item_html = (
                                    f'<code>{rel_attr.name}</code>: Belongs to relationship '
                                    f'<strong>{rel_attr.relationship_name}</strong> ({rel_attr.justification})'
                                )
                                ui.html(f"<li>{item_html}</li>")

        # 3. Keys Analysis Table (Included in Print)
        with ui.column().classes("w-full glass-panel gap-4 print-section print-keys"):
            with ui.row().classes("items-center gap-2 border-b border-[var(--border)] pb-3 w-full"):
                ui.html('<i class="fa-solid fa-key text-[#f59e0b] no-print"></i>')
                ui.html('<h3 class="text-lg font-bold text-amber-600 dark:text-[#fde68a] m-0">3. Key Analysis & Primary Key (PK) Selection</h3>')

            # Render Table
            table_rows_html = ""
            for row in scenario.keys_analysis:
                highlight_bg = "background: rgba(168, 85, 247, 0.08);" if row.is_weak else ""
                row_name_class = "text-purple-700 dark:text-purple-300 font-bold" if row.is_weak else "text-[var(--text-1)] font-bold"
                table_rows_html += f"""
                <tr style="{highlight_bg}">
                    <td class="{row_name_class}">{row.entity_name}</td>
                    <td>{row.key_count}</td>
                    <td>{row.key_types}</td>
                    <td><strong class="text-orange-600 dark:text-[#fdba74]">{row.final_pk_selection}</strong><br><span class="text-xs text-[var(--text-3)]">{row.justification}</span></td>
                </tr>
                """

            ui.html(
                f"""
                <div class="overflow-x-auto w-full">
                    <table class="dark-table">
                        <thead>
                            <tr>
                                <th>Entity</th>
                                <th>Key Count</th>
                                <th>Key Types</th>
                                <th>Selected PK & Rationale</th>
                            </tr>
                        </thead>
                        <tbody>
                            {table_rows_html}
                        </tbody>
                    </table>
                </div>
                """
            )

        # 4. Relationships, Cardinalities & Justifications (Included in Print)
        with ui.column().classes("w-full glass-panel gap-4 print-section print-relationships"):
            with ui.row().classes("items-center gap-2 border-b border-[var(--border)] pb-3 w-full"):
                ui.html('<i class="fa-solid fa-code-branch text-rose-500 no-print"></i>')
                ui.html('<h3 class="text-lg font-bold text-rose-600 dark:text-[#fda4af] m-0">4. Relationships, Cardinality Ratios & Rationale</h3>')

            with ui.column().classes("space-y-4 w-full rel-card-container"):
                for rel in scenario.relationships:
                    is_identifying = "identifying" in rel.relationship_type.lower()
                    rel_bg = (
                        "bg-[var(--card-bg-rel-ident)] border-purple-300 dark:border-purple-500/40"
                        if is_identifying
                        else "bg-[var(--card-bg-rel)] border-rose-300 dark:border-rose-500/30"
                    )
                    badge_color = "text-purple-700 dark:text-purple-300" if is_identifying else "text-rose-700 dark:text-rose-300"
                    with ui.column().classes(f"p-4 rounded-xl border {rel_bg} gap-2 w-full rel-card print-avoid-break shadow-sm"):
                        with ui.row().classes("items-center justify-between flex-wrap gap-2 w-full border-b border-[var(--border)] pb-2"):
                            with ui.row().classes("items-center gap-2"):
                                ui.label(f"{rel.letter_id}) Relationship: {rel.name}").classes(f"font-bold {badge_color} text-sm md:text-base")
                                ui.label(f"({rel.connected_entities})").classes("text-xs text-[var(--text-2)]")
                            with ui.row().classes("items-center gap-2 text-xs"):
                                ui.html(f'<span class="tag-label bg-orange-100 dark:bg-[#e06b3a]/30 text-orange-700 dark:text-[#fdba74]">{rel.cardinality}</span>')
                                ui.html(f'<span class="tag-label bg-gray-200 dark:bg-white/10 text-[var(--text-1)]">{rel.relationship_type}</span>')

                        with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-2 text-xs text-[var(--text-2)]"):
                            ui.html(f'<div><strong>Cardinality Ratio:</strong> <span class="text-orange-600 dark:text-[#fdba74] font-bold">{rel.cardinality}</span></div>')
                            ui.html(f'<div><strong>Participation:</strong> {rel.participation}</div>')

                        if rel.attributes:
                            attr_list_str = ", ".join([f"<code>{a}</code>" for a in rel.attributes])
                            ui.html(f'<div class="text-xs text-[var(--text-2)]"><strong>Relationship Attribute:</strong> {attr_list_str}</div>')

                        ui.html(f'<p class="text-xs text-[var(--text-2)] leading-relaxed m-0"><strong>Rationale:</strong> {rel.justification}</p>')

        # 5. Assumptions (Excluded from Print)
        with ui.column().classes("w-full p-5 rounded-xl bg-[var(--card-bg-subtle)] border border-[var(--border)] gap-3 no-print shadow-sm"):
            with ui.row().classes("items-center gap-2"):
                ui.html('<i class="fa-solid fa-clipboard-check text-[#f59e0b] text-sm"></i>')
                ui.label("Design Assumptions").classes("font-bold text-[var(--text-1)] text-sm")

            with ui.element("ol").classes("list-decimal list-inside text-xs text-[var(--text-2)] space-y-1.5 m-0 pl-1"):
                for assumption in scenario.assumptions:
                    ui.html(f"<li>{assumption}</li>")
