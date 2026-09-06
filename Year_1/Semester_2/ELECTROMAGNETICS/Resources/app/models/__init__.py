"""Data models package initialization for Electromagnetics app."""

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
from models.registry import ScenarioRegistry, scenario_registry

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
    "ScenarioRegistry",
    "scenario_registry",
]

