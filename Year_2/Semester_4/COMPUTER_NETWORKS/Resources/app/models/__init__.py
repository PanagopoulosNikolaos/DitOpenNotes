"""Models package for Computer Networks application."""

from .scenario import (
    TextSegment,
    Paragraph,
    QuestionOption,
    CalculationStep,
    ExamQuestion,
    TopologyNode,
    TopologyLink,
    NetworkScenario,
)
from .registry import scenario_registry, ScenarioRegistry

__all__ = [
    "TextSegment",
    "Paragraph",
    "QuestionOption",
    "CalculationStep",
    "ExamQuestion",
    "TopologyNode",
    "TopologyLink",
    "NetworkScenario",
    "scenario_registry",
    "ScenarioRegistry",
]
