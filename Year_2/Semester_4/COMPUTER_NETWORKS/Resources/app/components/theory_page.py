"""Master Theory and Study Guide component for Computer Networks."""

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


def renderTheoryPage(active_topic_id: str = "theory_full_prep") -> None:
    """Renders the comprehensive Computer Networks theory handbook and study guide.

    Args:
        active_topic_id (str): The ID of the specific theory topic to display initially.

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
                        "Πλήρης Θεωρητικός Οδηγός & Μεθοδολογία Δικτύων Υπολογιστών"
                        "</h1>"
                    )
                    ui.label(
                        "Ολοκληρωμένο εκπαιδευτικό εγχειρίδιο 7 θεματικών ενοτήτων, τυπολόγιο, συγκριτικοί πίνακες "
                        "και ενσωματωμένοι διαδραστικοί υπολογιστές."
                    ).classes("text-sm text-[#b5b0a4] mt-1")

        # Quick Reference Methodology Cards
        renderMethodologyCards()

        # Topic Selector Tabs
        topics = [
            ("theory_full_prep", "Πλήρης Οδηγός Εξετάσεων", "graduation-cap"),
            ("topic_1_network_edge", "1. Network Edge", "laptop-code"),
            ("topic_2_the_internet", "2. Internet & Protocols", "globe"),
            ("topic_3_network_structure", "3. Network Structure", "diagram-project"),
            ("topic_4_access_technologies", "4. Access Tech", "wifi"),
            ("topic_5_communication_media", "5. Media (UTP/Fiber)", "cable-car"),
            ("topic_6_data_switching_and_routing", "6. Switching & Routing", "route"),
            ("topic_7_basic_networking_issues", "7. Addressing & CRC", "microchip"),
            ("calculators", "Διαδραστικοί Υπολογιστές", "calculator"),
        ]

        topic_container = ui.column().classes("w-full gap-6")

        def showTopic(topic_id: str) -> None:
            """Renders the selected theory topic into the container."""
            topic_container.clear()
            with topic_container:
                if topic_id == "theory_full_prep":
                    renderTheoryExamFullPrep()
                    renderMethodologyTable()
                elif topic_id == "topic_1_network_edge":
                    renderTopic1NetworkEdge()
                elif topic_id == "topic_2_the_internet":
                    renderTopic2TheInternet()
                elif topic_id == "topic_3_network_structure":
                    renderTopic3NetworkStructure()
                elif topic_id == "topic_4_access_technologies":
                    renderTopic4AccessTechnologies()
                elif topic_id == "topic_5_communication_media":
                    renderTopic5CommunicationMedia()
                elif topic_id == "topic_6_data_switching_and_routing":
                    renderTopic6DataSwitchingAndRouting()
                elif topic_id == "topic_7_basic_networking_issues":
                    renderTopic7BasicNetworkingIssues()
                elif topic_id == "calculators":
                    renderCalculators()

        # Tabs Header
        with ui.row().classes("w-full gap-2 flex-wrap bg-[#141413] p-2.5 rounded-2xl border border-[rgba(255,255,255,0.08)]"):
            for tid, label, icon in topics:
                is_active = (tid == active_topic_id)
                btn_cls = "bg-[rgba(224,107,58,0.2)] text-[#fed7aa] border-[#e06b3a]" if is_active else "bg-[#201f1d] text-[#b5b0a4] border-transparent"
                ui.button(
                    f"{label}",
                    icon=icon,
                    on_click=lambda _, t=tid: showTopic(t),
                ).props("flat dense").classes(f"text-xs font-semibold px-3 py-1.5 rounded-xl border {btn_cls} hover:text-[#f4f1ea] transition-all")

        # Initial Topic Render
        showTopic(active_topic_id)
