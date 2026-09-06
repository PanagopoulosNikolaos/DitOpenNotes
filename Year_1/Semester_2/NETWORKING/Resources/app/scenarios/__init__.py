"""Scenarios package initialization and auto-registration."""

from models.registry import scenario_registry
from .past_exam_1_review_theme import createPastExam1Scenario
from .synth_exam_1_ip_addressing import createSynthExam1Scenario
from .synth_exam_2_internet_layer import createSynthExam2Scenario
from .synth_exam_3_transport_routing import createSynthExam3Scenario


def initializeScenarios() -> None:
    """Instantiates and registers all available scenarios into the registry."""
    # Register the real (discovered) practice exam as the default scenario
    past_exam_1 = createPastExam1Scenario()
    scenario_registry.registerScenario(past_exam_1, set_as_default=True)

    # Register Synthetic Exam 1: IP addressing, VLSM & CIDR
    synth_exam_1 = createSynthExam1Scenario()
    scenario_registry.registerScenario(synth_exam_1, set_as_default=False)

    # Register Synthetic Exam 2: Internet layer, fragmentation, TTL & NAT
    synth_exam_2 = createSynthExam2Scenario()
    scenario_registry.registerScenario(synth_exam_2, set_as_default=False)

    # Register Synthetic Exam 3: Transport layer & routing algorithms
    synth_exam_3 = createSynthExam3Scenario()
    scenario_registry.registerScenario(synth_exam_3, set_as_default=False)


# Auto-initialize on import
initializeScenarios()

__all__ = [
    "createPastExam1Scenario",
    "createSynthExam1Scenario",
    "createSynthExam2Scenario",
    "createSynthExam3Scenario",
    "initializeScenarios",
]
