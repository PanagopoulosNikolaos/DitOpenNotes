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
        with ui.row().classes("items-center gap-3"):
            ui.html('<i class="fa-solid fa-magnifying-glass-chart text-[#e06b3a] text-xl"></i>')
            ui.html('<h2 class="text-xl md:text-2xl font-bold text-[#f4f1ea] m-0">Αναλυτική Αιτιολόγηση Αναγνώρισης Στοιχείων</h2>')

        # 1. Entities & Types
        with ui.column().classes("w-full glass-panel gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3 w-full"):
                ui.html('<i class="fa-solid fa-cubes text-blue-400"></i>')
                ui.html('<h3 class="text-lg font-bold text-[#93c5fd] m-0">1. Οντότητες & Είδος</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full"):
                for idx, ent in enumerate(scenario.entities, start=1):
                    border_color = "border-purple-500/50 bg-[#251f2d]" if ent.is_weak else "border-blue-500/30 bg-[#1c202a]"
                    text_color = "text-purple-300" if ent.is_weak else "text-blue-300"
                    with ui.column().classes(f"p-4 rounded-xl border {border_color} gap-2"):
                        with ui.row().classes("items-center gap-2"):
                            ui.label(f"{idx}. {ent.name}").classes(f"font-bold {text_color} text-sm")
                            ui.label(f"({ent.entity_type})").classes("text-xs text-[#b5b0a4]")
                        ui.html(f'<p class="text-xs text-[#b5b0a4] leading-relaxed m-0"><strong>Αιτιολογία:</strong> {ent.justification}</p>')

        # 2. Attributes & Types (Complete for all entities!)
        with ui.column().classes("w-full glass-panel gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3 w-full"):
                ui.html('<i class="fa-solid fa-list-check text-emerald-400"></i>')
                ui.html('<h3 class="text-lg font-bold text-[#86efac] m-0">2. Γνωρίσματα & Είδος</h3>')

            with ui.column().classes("space-y-4 w-full"):
                for ent in scenario.entities:
                    with ui.column().classes("p-4 rounded-xl bg-[#1e231e] border border-[rgba(16,185,129,0.25)] gap-2 w-full"):
                        with ui.row().classes("items-center gap-2"):
                            ui.html('<i class="fa-solid fa-cube text-emerald-400 text-xs"></i>')
                            ui.label(f"{ent.name}:").classes("font-bold text-[#86efac] text-sm")

                        with ui.element("ul").classes("list-disc list-inside text-xs text-[#b5b0a4] space-y-1.5 m-0 pl-1"):
                            for attr in ent.attributes:
                                pk_tag = '<span class="text-[#fdba74] font-bold"> [PK]</span>' if attr.is_pk else ""
                                cand_tag = '<span class="text-[#fde68a] font-bold"> [Candidate]</span>' if attr.is_candidate else ""
                                part_tag = '<span class="text-[#fef08a] font-bold"> [Partial Key]</span>' if attr.is_partial else ""
                                comp_str = f" (Αναλύεται σε: {', '.join(attr.components)})" if attr.components else ""
                                notes_str = f" — <em>{attr.notes}</em>" if attr.notes else ""
                                item_html = (
                                    f'<code>{attr.name}</code>{pk_tag}{cand_tag}{part_tag}: '
                                    f'{attr.attr_type}{comp_str}{notes_str}'
                                )
                                ui.html(f"<li>{item_html}</li>")

                # Relationship Attributes
                if scenario.relationship_attributes:
                    with ui.column().classes("p-4 rounded-xl bg-[#231e21] border border-[rgba(244,63,94,0.25)] gap-2 w-full"):
                        with ui.row().classes("items-center gap-2"):
                            ui.html('<i class="fa-solid fa-link text-rose-400 text-xs"></i>')
                            ui.label("Γνωρίσματα Σχέσεων (Relationship Attributes):").classes("font-bold text-[#fda4af] text-sm")

                        with ui.element("ul").classes("list-disc list-inside text-xs text-[#b5b0a4] space-y-1.5 m-0 pl-1"):
                            for rel_attr in scenario.relationship_attributes:
                                item_html = (
                                    f'<code>{rel_attr.name}</code>: Ανήκει στη σχέση '
                                    f'<strong>{rel_attr.relationship_name}</strong> ({rel_attr.justification})'
                                )
                                ui.html(f"<li>{item_html}</li>")

        # 3. Keys Analysis Table
        with ui.column().classes("w-full glass-panel gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3 w-full"):
                ui.html('<i class="fa-solid fa-key text-[#f59e0b]"></i>')
                ui.html('<h3 class="text-lg font-bold text-[#fde68a] m-0">3. Ανάλυση Κλειδιών & Τελική Επιλογή Πρωτεύοντος Κλειδιού (PK)</h3>')

            # Render Table
            table_rows_html = ""
            for row in scenario.keys_analysis:
                highlight_bg = "background: rgba(168, 85, 247, 0.08);" if row.is_weak else ""
                row_name_class = "text-purple-300 font-bold" if row.is_weak else "text-[#f4f1ea] font-bold"
                table_rows_html += f"""
                <tr style="{highlight_bg}">
                    <td class="{row_name_class}">{row.entity_name}</td>
                    <td>{row.key_count}</td>
                    <td>{row.key_types}</td>
                    <td><strong class="text-[#fdba74]">{row.final_pk_selection}</strong><br><span class="text-xs text-[#78756d]">{row.justification}</span></td>
                </tr>
                """

            ui.html(
                f"""
                <div class="overflow-x-auto w-full">
                    <table class="dark-table">
                        <thead>
                            <tr>
                                <th>Οντότητα</th>
                                <th>Πλήθος Κλειδιών</th>
                                <th>Είδος Κλειδιών</th>
                                <th>Τελική Επιλογή PK & Αιτιολογία</th>
                            </tr>
                        </thead>
                        <tbody>
                            {table_rows_html}
                        </tbody>
                    </table>
                </div>
                """
            )

        # 4. Relationships, Cardinalities & Justifications
        with ui.column().classes("w-full glass-panel gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3 w-full"):
                ui.html('<i class="fa-solid fa-code-branch text-rose-400"></i>')
                ui.html('<h3 class="text-lg font-bold text-[#fda4af] m-0">4. Σχέσεις, Λόγοι Πληθικότητας & Αιτιολογήσεις</h3>')

            with ui.column().classes("space-y-4 w-full"):
                for rel in scenario.relationships:
                    rel_bg = "bg-[#251f2d] border-purple-500/40" if "Ταυτοποιούσα" in rel.relationship_type else "bg-[#251d20] border-rose-500/30"
                    badge_color = "text-purple-300" if "Ταυτοποιούσα" in rel.relationship_type else "text-rose-300"
                    with ui.column().classes(f"p-4 rounded-xl border {rel_bg} gap-2 w-full"):
                        with ui.row().classes("items-center justify-between flex-wrap gap-2 w-full border-b border-[rgba(255,255,255,0.06)] pb-2"):
                            with ui.row().classes("items-center gap-2"):
                                ui.label(f"{rel.letter_id}) Σχέση: {rel.name}").classes(f"font-bold {badge_color} text-sm md:text-base")
                                ui.label(f"({rel.connected_entities})").classes("text-xs text-[#b5b0a4]")
                            with ui.row().classes("items-center gap-2 text-xs"):
                                ui.html(f'<span class="tag-label bg-[#e06b3a]/30 text-[#fdba74]">{rel.cardinality}</span>')
                                ui.html(f'<span class="tag-label bg-white/10 text-[#f4f1ea]">{rel.relationship_type}</span>')

                        with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-2 text-xs text-[#b5b0a4]"):
                            ui.html(f'<div><strong>Λόγος Πληθικότητας:</strong> <span class="text-[#fdba74] font-bold">{rel.cardinality}</span></div>')
                            ui.html(f'<div><strong>Συμμετοχή:</strong> {rel.participation}</div>')

                        if rel.attributes:
                            attr_list_str = ", ".join([f"<code>{a}</code>" for a in rel.attributes])
                            ui.html(f'<div class="text-xs text-[#b5b0a4]"><strong>Γνώρισμα Σχέσης:</strong> {attr_list_str}</div>')

                        ui.html(f'<p class="text-xs text-[#b5b0a4] leading-relaxed m-0"><strong>Αιτιολογία:</strong> {rel.justification}</p>')

        # 5. Assumptions
        with ui.column().classes("w-full p-5 rounded-xl bg-[#1c1b1a] border border-[rgba(255,255,255,0.08)] gap-3"):
            with ui.row().classes("items-center gap-2"):
                ui.html('<i class="fa-solid fa-clipboard-check text-[#f59e0b] text-sm"></i>')
                ui.label("Παραδοχές Σχεδιασμού (Design Assumptions)").classes("font-bold text-[#f4f1ea] text-sm")

            with ui.element("ol").classes("list-decimal list-inside text-xs text-[#b5b0a4] space-y-1.5 m-0 pl-1"):
                for assumption in scenario.assumptions:
                    ui.html(f"<li>{assumption}</li>")
