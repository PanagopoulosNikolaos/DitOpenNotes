"""Domain data models for Digital Electronics scenarios, questions, and derivations.

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
    category: str = "all"  # 'binary', 'boolean', 'fsm', 'vhdl', 'param'
    tag_label: Optional[str] = None  # e.g., 'C2', 'K-MAP', 'FSM', 'MUX'
    badge_class: Optional[str] = None  # e.g., 'badge-binary', 'badge-boolean'
    tooltip: Optional[str] = None  # Three-part explanation: Classification, Clue, Rationale


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
    explanation: str  # Distractor explanation or verification rationale


@dataclass
class CalculationStep:
    """Represents an algebraic, truth-table, or minimization step."""
    step_number: int
    title: str
    formula: str  # KaTeX formula string
    substitution: str  # KaTeX substitution or truth table snippet
    result: str  # KaTeX final or intermediate result
    rationale: str  # Underlying engineering or mathematical rationale


@dataclass
class GivenParameter:
    """Represents an exam-given value cross-referenced with canvas highlights."""
    symbol: str  # e.g., 'A', 'B', 'f_clk'
    value: str  # e.g., '+43', '-27', '100 MHz'
    description: str  # e.g., 'First operand in decimal', 'Second operand in decimal'
    category: str = "param"


@dataclass
class ExamQuestion:
    """Represents a complete exam or practice question with analysis and steps."""
    question_number: int
    title: str
    question_type: str  # 'Binary Arithmetic', 'K-Map Minimization', 'FSM Sequential Design', 'VHDL Hardware Synthesis'
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
    """Represents a node or state in the interactive SVG diagram."""
    id: str
    label: str
    node_type: str  # 'state', 'gate', 'port', 'mux_block', 'ff_block'
    x: int
    y: int
    properties: Dict[str, Any] = field(default_factory=dict)


@dataclass
class DiagramEdge:
    """Represents a transition or wire in the SVG diagram."""
    source_id: str
    target_id: str
    label: str
    edge_type: str  # 'transition', 'wire', 'bus', 'clock'
    path_d: Optional[str] = None
    color: Optional[str] = None


@dataclass
class DesignJustification:
    """Rationale card explaining hardware principles or synthesis decisions."""
    title: str
    category: str  # 'Boolean Theorem', 'FSM Timing', 'VHDL Idiom', 'Hardware Efficiency'
    description: str
    rationale: str


@dataclass
class Scenario:
    """Complete container for a Digital Electronics exam paper or problem set."""
    id: str
    title: str
    subtitle: str
    course_tag: str  # 'Practice Exam', 'Synthetic Exam', 'Official Exam'
    duration_info: str
    paragraphs: List[Paragraph]
    questions: List[ExamQuestion]
    diagram_nodes: List[DiagramNode] = field(default_factory=list)
    diagram_edges: List[DiagramEdge] = field(default_factory=list)
    diagram_svg_custom: Optional[str] = None
    justifications: List[DesignJustification] = field(default_factory=list)
    solution_code: str = ""

