"""Master Theory and Study Guide component for Computer Networks with LaTeX support."""

from typing import Callable, Optional
from nicegui import ui
from theory import (
    renderTopic1NetworkEdge,
    renderTopic2TheInternet,
    renderTopic3NetworkStructure,
    renderTopic4AccessTechnologies,
    renderTopic5CommunicationMedia,
    renderTopic6DataSwitchingAndRouting,
    renderTopic7BasicNetworkingIssues,
    renderTheoryExamFullPrep,
)
from .methodology_card import renderMethodologyCards
from .methodology_table import renderMethodologyTable
from .interactive_calculators import renderCalculators


def renderTheoryPage(
    active_sub_id: str = "theory_full_prep",
    on_sub_change: Optional[Callable[[str], None]] = None,
) -> None:
    """Renders the comprehensive Computer Networks study handbook with notes sub-modules.

    Args:
        active_sub_id (str): The ID of the specific study submodule to display initially.
        on_sub_change (Optional[Callable[[str], None]]): Callback when sub-module is switched.

    Returns:
        None
    """
    with ui.column().classes("w-full max-w-6xl mx-auto px-4 py-8 space-y-8"):
        # Header Banner
        with ui.column().classes(
            "w-full glass-panel p-6 md:p-8 rounded-2xl border border-[rgba(224,107,58,0.35)] gap-4"
        ):
            with ui.row().classes("items-center gap-3"):
                ui.html('<i class="fa-solid fa-book-open-reader text-[#e06b3a] text-2xl md:text-3xl"></i>')
                with ui.column().classes("gap-0"):
                    ui.html(
                        '<h1 class="text-2xl md:text-3xl font-black gradient-title m-0">'
                        "Study Module: Θεωρητικός Οδηγός & Σημειώσεις Μαθήματος"
                        "</h1>"
                    )
                    ui.label(
                        "Ολοκληρωμένο εκπαιδευτικό υλικό 7 θεματικών ενοτήτων με υποστήριξη LaTeX, συγκριτικούς πίνακες "
                        "και ενσωματωμένους διαδραστικούς υπολογιστές."
                    ).classes("text-sm text-[#b5b0a4] mt-1")

        # Quick Reference Methodology Cards
        renderMethodologyCards()

        # Topic Selector Tabs
        study_tabs = [
            ("theory_full_prep", "Πλήρης Οδηγός Εξετάσεων (Cheat Sheet)", "graduation-cap"),
            ("topic_1_network_edge", "1. Network Edge & P2P", "laptop-code"),
            ("topic_2_the_internet", "2. Internet & Protocols", "globe"),
            ("topic_3_network_structure", "3. Network Structure & ISPs", "diagram-project"),
            ("topic_4_access_technologies", "4. Access Tech (FTTH/5G)", "wifi"),
            ("topic_5_communication_media", "5. Media (UTP/Fiber/LEO)", "cable-car"),
            ("topic_6_data_switching_and_routing", "6. Switching & 4 Delays", "route"),
            ("topic_7_basic_networking_issues", "7. Addressing & CRC", "microchip"),
            ("study_calculators", "Διαδραστικοί Υπολογιστές", "calculator"),
        ]

        topic_container = ui.column().classes("w-full gap-6")

        def showStudyTopic(sub_id: str) -> None:
            """Renders the selected study submodule into the container."""
            topic_container.clear()
            with topic_container:
                if sub_id in ("theory_full_prep", "study_full_prep"):
                    renderTheoryExamFullPrep()
                    renderMethodologyTable()
                elif sub_id == "topic_1_network_edge":
                    renderTopic1NetworkEdge()
                elif sub_id == "topic_2_the_internet":
                    renderTopic2TheInternet()
                elif sub_id == "topic_3_network_structure":
                    renderTopic3NetworkStructure()
                elif sub_id == "topic_4_access_technologies":
                    renderTopic4AccessTechnologies()
                elif sub_id == "topic_5_communication_media":
                    renderTopic5CommunicationMedia()
                elif sub_id == "topic_6_data_switching_and_routing":
                    renderTopic6DataSwitchingAndRouting()
                elif sub_id == "topic_7_basic_networking_issues":
                    renderTopic7BasicNetworkingIssues()
                elif sub_id in ("study_calculators", "calculators"):
                    renderCalculators()

            ui.run_javascript("if (typeof renderAllLatex === 'function') setTimeout(renderAllLatex, 50);")

        # Tabs Header
        with ui.row().classes("w-full gap-2 flex-wrap bg-[#141413] p-2.5 rounded-2xl border border-[rgba(255,255,255,0.08)]"):
            for tid, label, icon in study_tabs:
                is_active = (tid == active_sub_id)
                btn_cls = "bg-[rgba(224,107,58,0.25)] text-[#fed7aa] border-[#e06b3a]" if is_active else "bg-[#201f1d] text-[#b5b0a4] border-transparent"
                ui.button(
                    f"{label}",
                    icon=icon,
                    on_click=lambda _, t=tid: (showStudyTopic(t), on_sub_change(t) if on_sub_change else None),
                ).props("flat dense").classes(f"text-xs font-semibold px-3 py-1.5 rounded-xl border {btn_cls} hover:text-[#f4f1ea] transition-all")

        # Initial Submodule Render
        showStudyTopic(active_sub_id)
