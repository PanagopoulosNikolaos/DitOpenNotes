"""Methodology quick-guide 4-step cards component."""

from nicegui import ui


def renderMethodologyCards() -> None:
    """Renders the 4-step methodology cards explaining how to analyze any ER problem.

    Returns:
        None
    """
    with ui.column().classes("w-full glass-panel gap-4 no-print"):
        with ui.row().classes("items-center gap-3"):
            ui.html('<i class="fa-solid fa-compass text-[var(--accent)] text-xl"></i>')
            ui.html('<h2 class="text-xl font-bold text-[var(--text-1)] m-0">How to Analyze Any Requirements Text (Step-by-Step)</h2>')

        with ui.grid().classes("grid-cols-1 md:grid-cols-4 gap-4 w-full"):
            # Step 1: Entities
            with ui.column().classes(
                "p-4 rounded-xl bg-[var(--card-bg-subtle)] border-l-4 border-blue-500 border border-[var(--border)] gap-1 shadow-sm"
            ):
                with ui.row().classes("items-center gap-2"):
                    ui.html('<i class="fa-solid fa-cube text-blue-500 text-sm"></i>')
                    ui.label("1. Entities").classes("font-bold text-blue-600 dark:text-blue-300 text-sm")
                ui.label(
                    "Identify major nouns (people, objects, concepts) that have autonomous "
                    "existence and about which data is maintained."
                ).classes("text-xs text-[var(--text-2)] leading-relaxed")

            # Step 2: Attributes
            with ui.column().classes(
                "p-4 rounded-xl bg-[var(--card-bg-subtle)] border-l-4 border-emerald-500 border border-[var(--border)] gap-1 shadow-sm"
            ):
                with ui.row().classes("items-center gap-2"):
                    ui.html('<i class="fa-solid fa-tag text-emerald-500 text-sm"></i>')
                    ui.label("2. Attributes").classes("font-bold text-emerald-600 dark:text-emerald-300 text-sm")
                ui.label(
                    "Identify properties and characteristics of entities. Classify them into "
                    "Simple, Composite, Multivalued, or Derived."
                ).classes("text-xs text-[var(--text-2)] leading-relaxed")

            # Step 3: Keys
            with ui.column().classes(
                "p-4 rounded-xl bg-[var(--card-bg-subtle)] border-l-4 border-amber-500 border border-[var(--border)] gap-1 shadow-sm"
            ):
                with ui.row().classes("items-center gap-2"):
                    ui.html('<i class="fa-solid fa-key text-amber-500 text-sm"></i>')
                    ui.label("3. Keys").classes("font-bold text-amber-600 dark:text-amber-300 text-sm")
                ui.label(
                    "Look for terms like 'unique code', 'ID', 'SSN'. Select Primary Keys (PK) "
                    "and identify Partial Keys for weak entities."
                ).classes("text-xs text-[var(--text-2)] leading-relaxed")

            # Step 4: Relationships
            with ui.column().classes(
                "p-4 rounded-xl bg-[var(--card-bg-subtle)] border-l-4 border-rose-500 border border-[var(--border)] gap-1 shadow-sm"
            ):
                with ui.row().classes("items-center gap-2"):
                    ui.html('<i class="fa-solid fa-code-branch text-rose-500 text-sm"></i>')
                    ui.label("4. Relationships & Cardinalities").classes("font-bold text-rose-600 dark:text-rose-300 text-sm")
                ui.label(
                    "Identify verbs linking entities. Analyze both directions to determine "
                    "cardinality ratios (1:1, 1:N, N:M) and participation constraints."
                ).classes("text-xs text-[var(--text-2)] leading-relaxed")
