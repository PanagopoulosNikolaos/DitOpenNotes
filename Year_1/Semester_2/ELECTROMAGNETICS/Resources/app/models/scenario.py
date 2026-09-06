"""Domain data models for Electromagnetics scenarios, questions, and derivations.

Defines dataclasses for storing and rendering exam papers verbatim, interactive
annotated text segments, multiple-choice questions, KaTeX calculation steps,
and SVG diagram structures.
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any


@dataclass
class TextSegment:
    """Represents a segment of text in the exam description.

    Can be plain text or an interactive highlighted element with category tags
    and hover-to-explain tooltips satisfying the three-part contract.
    """
    text: str
    is_highlight: bool = False
    category: str = "all"  # 'field', 'param', 'calc', 'law', 'geom'
    tag_label: Optional[str] = None  # e.g., 'E-FIELD', 'POYNTING', 'GAUSS'
    badge_class: Optional[str] = None  # e.g., 'badge-field', 'badge-param'
    tooltip: Optional[str] = None  # Three-part explanation: Classification, Clue, Rationale


@dataclass
class Paragraph:
    """Represents a paragraph in the problem description containing text segments."""
    segments: List[TextSegment]
    accent_border_color: Optional[str] = None


@dataclass
class QuestionOption:
    """Represents a single option in a multiple-choice question."""
    letter: str  # 'A', 'B', 'Γ', 'Δ' or 'A', 'B', 'C', 'D'
    text: str
    is_correct: bool
    explanation: str  # Distractor explanation or verification rationale


@dataclass
class CalculationStep:
    """Represents an algebraic or vector calculus derivation step."""
    step_number: int
    title: str
    formula: str  # KaTeX formula string
    substitution: str  # KaTeX substitution string
    result: str  # KaTeX final or intermediate result
    rationale: str  # Underlying physical or mathematical reason


@dataclass
class GivenParameter:
    """Represents an exam-given value cross-referenced with canvas highlights."""
    symbol: str  # e.g., 'c', 'E_0', 'omega'
    value: str  # e.g., '3 * 10^8 m/s', '1.5 V/m'
    description: str  # e.g., 'Speed of light in vacuum', 'Electric field amplitude'
    category: str = "param"


@dataclass
class ExamQuestion:
    """Represents a complete exam or practice question with analysis and steps."""
    question_number: int
    title: str
    question_type: str  # 'Multiple Choice', 'Calculations', 'Theory Analysis', 'Proof'
    prompt_text: str
    options: List[QuestionOption] = field(default_factory=list)
    correct_option_letter: Optional[str] = None
    given_parameters: List[GivenParameter] = field(default_factory=list)
    calculation_steps: List[CalculationStep] = field(default_factory=list)
    final_answer: str = ""
    detailed_justification: str = ""
    common_pitfalls: List[str] = field(default_factory=list)
    related_theory_topic: Optional[str] = None


@dataclass
class DiagramNode:
    """Represents a node or element in the interactive SVG diagram."""
    id: str
    label: str
    node_type: str  # 'vector_e', 'vector_b', 'vector_k', 'source', 'boundary', 'charge'
    x: int
    y: int
    properties: Dict[str, Any] = field(default_factory=dict)


@dataclass
class DiagramEdge:
    """Represents a vector, field line, or ray in the SVG diagram."""
    source_id: str
    target_id: str
    label: str
    edge_type: str  # 'wave_e', 'wave_b', 'ray', 'flux_line', 'normal'
    path_d: Optional[str] = None  # SVG path data
    color: Optional[str] = None


@dataclass
class DesignJustification:
    """Rationale card explaining physical principles or analytical decisions."""
    title: str
    category: str  # 'Maxwell Law', 'Wave Property', 'Boundary Condition', 'Conservation'
    description: str
    rationale: str


@dataclass
class Scenario:
    """Complete container for an Electromagnetics exam paper or problem set."""
    id: str
    title: str
    subtitle: str
    course_tag: str  # 'Past Exam', 'Practice Exam', 'Laboratory'
    duration_info: str
    paragraphs: List[Paragraph]
    questions: List[ExamQuestion]
    diagram_nodes: List[DiagramNode] = field(default_factory=list)
    diagram_edges: List[DiagramEdge] = field(default_factory=list)
    diagram_svg_custom: Optional[str] = None
    justifications: List[DesignJustification] = field(default_factory=list)
    solution_code: str = ""

