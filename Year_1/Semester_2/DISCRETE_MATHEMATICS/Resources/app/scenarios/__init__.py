"""Scenarios package initialization and auto-registration for Discrete Mathematics.

Registers all 11 examination scenarios into the global ScenarioRegistry singleton.
"""

from models.registry import scenario_registry
from scenarios.final_exam_2025_june import createFinalExam2025JuneScenario
from scenarios.midterm_exam_2025_group_a import createMidtermExam2025GroupAScenario
from scenarios.midterm_exam_2025_group_b import createMidtermExam2025GroupBScenario
from scenarios.mock_exam_1_easier import createMockExam1EasierScenario
from scenarios.mock_exam_2_standard import createMockExam2StandardScenario
from scenarios.mock_exam_3_standard import createMockExam3StandardScenario
from scenarios.mock_exam_4_harder import createMockExam4HarderScenario
from scenarios.mock_exam_5_gotchas import createMockExam5GotchasScenario
from scenarios.practice_exam_easy import createPracticeExamEasyScenario
from scenarios.practice_exam_medium import createPracticeExamMediumScenario
from scenarios.practice_exam_hard import createPracticeExamHardScenario


def registerAllScenarios() -> None:
    """Instantiates and registers all scenarios into the global registry.

    Returns:
        None
    """
    # 1. Official June 2025 Final Exam (Course 203)
    scenario_registry.registerScenario(createFinalExam2025JuneScenario())

    # 2. Official 2025 Midterm Group A
    scenario_registry.registerScenario(createMidtermExam2025GroupAScenario())

    # 3. Official 2025 Midterm Group B
    scenario_registry.registerScenario(createMidtermExam2025GroupBScenario())

    # 4-8. Curated Mock Exams (Easy to Hard & Gotchas)
    scenario_registry.registerScenario(createMockExam1EasierScenario())
    scenario_registry.registerScenario(createMockExam2StandardScenario())
    scenario_registry.registerScenario(createMockExam3StandardScenario())
    scenario_registry.registerScenario(createMockExam4HarderScenario())
    scenario_registry.registerScenario(createMockExam5GotchasScenario())

    # 9-11. Practice Exam Series (Easy, Medium, Hard)
    scenario_registry.registerScenario(createPracticeExamEasyScenario())
    scenario_registry.registerScenario(createPracticeExamMediumScenario())
    scenario_registry.registerScenario(createPracticeExamHardScenario())


# Auto-register on package import
registerAllScenarios()

__all__ = [
    "registerAllScenarios",
    "createFinalExam2025JuneScenario",
    "createMidtermExam2025GroupAScenario",
    "createMidtermExam2025GroupBScenario",
    "createMockExam1EasierScenario",
    "createMockExam2StandardScenario",
    "createMockExam3StandardScenario",
    "createMockExam4HarderScenario",
    "createMockExam5GotchasScenario",
    "createPracticeExamEasyScenario",
    "createPracticeExamMediumScenario",
    "createPracticeExamHardScenario",
]
