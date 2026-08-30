"""Data models for Computer Networks learning scenarios, topology, and exams.

Defines the structure for storing and rendering networking scenarios,
interactive text highlights, multiple-choice and calculation questions,
and network topology diagrams.
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any


@dataclass
class TextSegment:
    """Represents a segment of text in the scenario description.

    Can be plain text or an interactive highlighted element with category tags.
    """
    text: str
    is_highlight: bool = False
    category: str = "all"  # 'delay', 'device', 'protocol', 'routing', 'error_check'
    tag_label: Optional[str] = None  # e.g., 'TRANSMISSION DELAY', 'ROUTER', 'CRC'
    badge_class: Optional[str] = None  # CSS class for badge styling
    tooltip: Optional[str] = None  # Detailed explanation on hover


@dataclass
class Paragraph:
    """Represents a paragraph in the problem description containing text segments."""
    segments: List[TextSegment]
    accent_border_color: Optional[str] = None


@dataclass
class QuestionOption:
    """Represents a single option in a multiple-choice question."""
    letter: str  # 'A', 'B', 'C', 'D'
    text: str
    is_correct: bool
    explanation: str


@dataclass
class CalculationStep:
    """Represents an algebraic or algorithmic derivation step."""
    step_number: int
    title: str
    formula: str
    substitution: str
    result: str
    rationale: str


@dataclass
class ExamQuestion:
    """Represents a complete exam or practice question with analysis and steps."""
    question_number: int
    title: str
    question_type: str  # 'Multiple Choice', 'Calculations', 'Algorithm Step', 'Theory Analysis'
    prompt_text: str
    options: List[QuestionOption] = field(default_factory=list)
    correct_option_letter: Optional[str] = None
    detailed_justification: str = ""
    common_pitfalls: List[str] = field(default_factory=list)
    calculation_steps: List[CalculationStep] = field(default_factory=list)
    related_theory_topic: Optional[str] = None


@dataclass
class TopologyNode:
    """Represents a network node in the SVG topology diagram."""
    id: str
    label: str
    node_type: str  # 'host', 'switch', 'router', 'server', 'cloud'
    x: int
    y: int
    ip_address: Optional[str] = None
    mac_address: Optional[str] = None
    properties: Dict[str, Any] = field(default_factory=dict)


@dataclass
class TopologyLink:
    """Represents a transmission link between two nodes."""
    source_id: str
    target_id: str
    bandwidth_mbps: float
    distance_km: float
    propagation_speed_km_s: float
    medium_type: str  # 'copper', 'fiber', 'wireless', 'satellite'
    label: str = ""


@dataclass
class NetworkScenario:
    """Complete container for a network exam paper, case study, or lab problem."""
    id: str
    title: str
    subtitle: str
    course_tag: str  # 'Past Exam', 'Synthetic Exam', 'Lab Practice'
    duration_info: str
    paragraphs: List[Paragraph]
    questions: List[ExamQuestion]
    nodes: List[TopologyNode] = field(default_factory=list)
    links: List[TopologyLink] = field(default_factory=list)
    methodology_summary: List[str] = field(default_factory=list)
    calculator_type: Optional[str] = None  # 'delay', 'crc', 'dijkstra', 'lpm'
