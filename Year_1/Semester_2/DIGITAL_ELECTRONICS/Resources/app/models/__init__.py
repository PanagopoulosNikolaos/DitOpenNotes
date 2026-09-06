"""Models package exposing dataclasses and global scenario registry."""

from models.scenario import (
    TextSegment,
    Paragraph,
    QuestionOption,
    CalculationStep,
    GivenParameter,
    ExamQuestion,
    DiagramNode,
    DiagramEdge,
    DesignJustification,
    Scenario,
)
from models.registry import scenario_registry, ScenarioRegistry

__all__ = [
    "TextSegment",
    "Paragraph",
    "QuestionOption",
    "CalculationStep",
    "GivenParameter",
    "ExamQuestion",
    "DiagramNode",
    "DiagramEdge",
    "DesignJustification",
    "Scenario",
    "scenario_registry",
    "ScenarioRegistry",
]

