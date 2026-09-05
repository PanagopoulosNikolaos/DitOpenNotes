"""Scenarios package auto-loader and registry initialization."""

from models.registry import scenario_registry
from .exam_past_2023_2024 import createScenario as createPast2023Scenario
from .exam_past_2026_team_edition import createScenario as createPast2026Scenario
from .exam_past_comprehensive_archive import createScenario as createPastArchiveScenario
from .exam_synth_1_core_edge_delays import createScenario as createSynth1Scenario
from .exam_synth_2_lpm_routing_mac import createScenario as createSynth2Scenario
from .exam_synth_3_p2p_store_forward_dijkstra import createScenario as createSynth3Scenario
from .exam_synth_4_encapsulation_crc_collision import createScenario as createSynth4Scenario
from .exam_synth_5_stat_multiplexing_throughput import createScenario as createSynth5Scenario


def registerAllScenarios() -> None:
    """Initializes and registers all past and synthetic exam scenarios."""
    # Past exams
    scenario_registry.registerScenario(createPast2023Scenario(), set_as_default=True)
    scenario_registry.registerScenario(createPast2026Scenario())
    scenario_registry.registerScenario(createPastArchiveScenario())

    # Synthetic exams
    scenario_registry.registerScenario(createSynth1Scenario())
    scenario_registry.registerScenario(createSynth2Scenario())
    scenario_registry.registerScenario(createSynth3Scenario())
    scenario_registry.registerScenario(createSynth4Scenario())
    scenario_registry.registerScenario(createSynth5Scenario())


# Auto-register upon import
registerAllScenarios()
