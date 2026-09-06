"""Scenarios package auto-registering all real and synthetic exam papers."""

from models.registry import scenario_registry
from scenarios.practice_exam_01_core import createPracticeExam01Scenario
from scenarios.synth_exam_02_msi_counters_fsm import createSyntheticExam02Scenario

# Auto-instantiate and register all scenarios
sc1 = createPracticeExam01Scenario()
sc2 = createSyntheticExam02Scenario()

scenario_registry.registerScenario(sc1)
scenario_registry.registerScenario(sc2)

__all__ = [
    "createPracticeExam01Scenario",
    "createSyntheticExam02Scenario",
]

