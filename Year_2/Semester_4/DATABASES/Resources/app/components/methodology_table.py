"""General methodology table component summarizing ER modeling extraction rules."""

from nicegui import ui


def renderMethodologyTable() -> None:
    """Renders the comprehensive reference guide table for text-to-ER extraction.

    Returns:
        None
    """
    with ui.column().classes("w-full glass-panel gap-4 no-print"):
        with ui.row().classes("items-center gap-3"):
            ui.html('<i class="fa-solid fa-table text-[var(--accent)] text-xl"></i>')
            ui.html('<h2 class="text-xl md:text-2xl font-bold text-[var(--text-1)] m-0">General Identification Guide (Methodology Matrix)</h2>')

        ui.label(
            "Use the following rules to systematically extract ER model constructs from any requirements text:"
        ).classes("text-xs text-[var(--text-2)]")

        table_content = """
        <div class="overflow-x-auto w-full">
            <table class="dark-table shadow-sm">
                <thead>
                    <tr>
                        <th style="width: 25%;">Modeling Element</th>
                        <th style="width: 35%;">Textual Indicators & Clues</th>
                        <th style="width: 40%;">Classification & Extraction Rules</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td class="font-bold text-blue-600 dark:text-blue-300">
                            <i class="fa-solid fa-cube mr-1 text-blue-500"></i> Entities
                        </td>
                        <td>
                            Typically <strong>nouns</strong> describing autonomous objects, persons, organizations, or concepts with independent existence.
                        </td>
                        <td>
                            • <strong>Strong:</strong> Possesses its own unique identifier (primary key).<br>
                            • <strong>Weak:</strong> Lacks a complete primary key; existence-dependent on an owner entity.
                        </td>
                    </tr>
                    <tr>
                        <td class="font-bold text-emerald-600 dark:text-emerald-300">
                            <i class="fa-solid fa-tag mr-1 text-emerald-500"></i> Attributes
                        </td>
                        <td>
                            <strong>Characteristics, properties, or data points</strong> recorded or maintained for an entity or relationship.
                        </td>
                        <td>
                            • <strong>Simple (Atomic):</strong> Cannot be further subdivided (e.g., Gender).<br>
                            • <strong>Composite:</strong> Can be divided into smaller sub-components (e.g., Address).<br>
                            • <strong>Single-valued:</strong> Exactly one value per entity instance.<br>
                            • <strong>Multivalued:</strong> Multiple values per entity instance (e.g., Phone Numbers, Facility Locations).<br>
                            • <strong>Derived:</strong> Computable from other stored attributes (e.g., Age from BirthDate).
                        </td>
                    </tr>
                    <tr>
                        <td class="font-bold text-amber-600 dark:text-amber-300">
                            <i class="fa-solid fa-key mr-1 text-amber-500"></i> Keys
                        </td>
                        <td>
                            Phrases such as <em>"unique code"</em>, <em>"ID number"</em>, <em>"unique name"</em>, <em>"SSN"</em>, <em>"tax number"</em>.
                        </td>
                        <td>
                            • <strong>Candidate Keys:</strong> All minimal superkeys capable of uniquely identifying tuples.<br>
                            • <strong>Primary Key (PK):</strong> The designated candidate key chosen for entity identification.<br>
                            • <strong>Partial Key (Discriminator):</strong> Uniquely identifies weak entity instances sharing the same owner.
                        </td>
                    </tr>
                    <tr>
                        <td class="font-bold text-rose-600 dark:text-rose-300">
                            <i class="fa-solid fa-code-branch mr-1 text-rose-500"></i> Relationships & Cardinality
                        </td>
                        <td>
                            <strong>Verbs or verbal phrases</strong> connecting entities (e.g., "belongs to", "manages", "enrolled in", "participates in").
                        </td>
                        <td>
                            • <strong>Cardinality Ratios:</strong> 1:1, 1:N, N:M (evaluate both directions: <em>1 A associates with how many B? / 1 B associates with how many A?</em>).<br>
                            • <strong>Participation:</strong> Total (mandatory — double line) or Partial (optional — single line).
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
        """
        ui.html(table_content)
