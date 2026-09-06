"""Scenarios package initialization and auto-registration of all exam papers."""

from models.registry import scenario_registry
from scenarios.past_exam_2024_09_team_b import createPastExam202409TeamB
from scenarios.past_exam_2026_06_team_a import createPastExam202606TeamA
from scenarios.past_exam_2026_06_team_b import createPastExam202606TeamB
from scenarios.past_exam_2026_06_team_c import createPastExam202606TeamC
from scenarios.past_exam_2026_06_team_d import createPastExam202606TeamD
from scenarios.synth_exam_1_comprehensive import createSynthExam1Comprehensive
from scenarios.synth_exam_2_fields_waves import createSynthExam2FieldsWaves
from scenarios.synth_exam_3_full_spectrum import createSynthExam3FullSpectrum

# Auto-instantiate and register all scenarios in chronological and pedagogical order
scenario_registry.registerScenario(createPastExam202409TeamB())
scenario_registry.registerScenario(createPastExam202606TeamA())
scenario_registry.registerScenario(createPastExam202606TeamB())
scenario_registry.registerScenario(createPastExam202606TeamC())
scenario_registry.registerScenario(createPastExam202606TeamD())
scenario_registry.registerScenario(createSynthExam1Comprehensive())
scenario_registry.registerScenario(createSynthExam2FieldsWaves())
scenario_registry.registerScenario(createSynthExam3FullSpectrum())

__all__ = [
    "createPastExam202409TeamB",
    "createPastExam202606TeamA",
    "createPastExam202606TeamB",
    "createPastExam202606TeamC",
    "createPastExam202606TeamD",
    "createSynthExam1Comprehensive",
    "createSynthExam2FieldsWaves",
    "createSynthExam3FullSpectrum",
]

