"""Scenarios package initialization and auto-registration for Discrete Mathematics."""

from models.registry import scenario_registry
from .past_exam_1_june_2025 import createPastExamJune2025
from .past_exam_2_june_2026 import createPastExamJune2026
from .mock_exam_1_foundations import createMockExam1Foundations
from .mock_exam_2_automata import createMockExam2Automata


def initScenarios() -> None:
    """Initializes and registers all course scenarios in the singleton registry.

    Returns:
        None
    """
    # 1. Official Exam June 2025 (Default)
    scenario_registry.registerScenario(createPastExamJune2025(), set_as_default=True)

    # 2. Official Exam June 2026
    scenario_registry.registerScenario(createPastExamJune2026())

    # 3. Practice Mock Exam 1
    scenario_registry.registerScenario(createMockExam1Foundations())

    # 4. Practice Mock Exam 2
    scenario_registry.registerScenario(createMockExam2Automata())


# Auto-execute registration on package import
initScenarios()
