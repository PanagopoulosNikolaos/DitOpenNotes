"""Domain data models for Discrete Mathematics scenarios, questions, and derivations.

Defines dataclasses for storing verbatim exam papers, interactive annotated text
segments, multiple-choice questions, KaTeX calculation steps, and SVG diagram structures.
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
    category: str = "all"  # 'logic', 'set', 'prob', 'graph', 'automata', 'induct', 'param'
    tag_label: Optional[str] = None  # e.g., 'LOGIC-RULE', 'INCLUSION-EXCLUSION', 'BAYES'
    badge_class: Optional[str] = None  # e.g., 'badge-logic', 'badge-set', 'badge-prob'
    tooltip: Optional[str] = None  # Three-part explanation: Classification, Clue, Rationale


@dataclass
class Paragraph:
    """Represents a paragraph in the problem description containing text segments."""
    segments: List[TextSegment]
    accent_border_color: Optional[str] = None


@dataclass
class QuestionOption:
    """Represents a single option in a multiple-choice question."""
    letter: str  # 'A', 'B', 'C', 'D' or 'α', 'β', etc.
    text: str
    is_correct: bool
    explanation: str  # Distractor explanation or verification rationale


@dataclass
class CalculationStep:
    """Represents an algebraic, combinatorial, or inductive derivation step."""
    step_number: int
    title: str
    formula: str  # KaTeX formula string
    substitution: str  # KaTeX substitution string
    result: str  # KaTeX final or intermediate result
    rationale: str  # Underlying mathematical reason or law


@dataclass
class GivenParameter:
    """Represents an exam-given value cross-referenced with canvas highlights."""
    symbol: str  # e.g., '|A|', 'P(F|A)', 'n', 'v'
    value: str  # e.g., '100', '10%', '256', '5'
    description: str  # e.g., 'Πλήθος συμμετεχόντων', 'Πιθανότητα false negative'
    category: str = "param"


@dataclass
class ExamQuestion:
    """Represents a complete exam or practice question with analysis and steps."""
    question_number: int
    title: str
    question_type: str  # 'Προτασιακή Λογική', 'Θεωρία Συνόλων', 'Πιθανότητες', 'Σχέσεις', 'Γραφήματα', 'Αυτόματα', 'Επαγωγή'
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
    node_type: str  # 'vertex', 'state', 'set_element', 'leaf'
    x: int
    y: int
    properties: Dict[str, Any] = field(default_factory=dict)


@dataclass
class DiagramEdge:
    """Represents an edge, transition, or relation in the SVG diagram."""
    source_id: str
    target_id: str
    label: str
    edge_type: str = "undirected"  # 'undirected', 'directed', 'transition', 'relation'
    path_d: Optional[str] = None  # SVG path data
    color: Optional[str] = None


@dataclass
class DesignJustification:
    """Rationale card explaining discrete mathematical principles or analytical decisions."""
    title: str
    category: str  # 'Logic Law', 'Combinatorics Principle', 'Euler Relation', 'Closure'
    description: str
    rationale: str


@dataclass
class Scenario:
    """Complete container for a Discrete Mathematics exam paper or problem set."""
    id: str
    title: str
    subtitle: str
    course_tag: str  # 'Επίσημη Εξέταση', 'Εξέταση Προόδου', 'Εικονική Εξέταση', 'Πρακτική Εξέταση'
    duration_info: str
    paragraphs: List[Paragraph]
    questions: List[ExamQuestion]
    diagram_nodes: List[DiagramNode] = field(default_factory=list)
    diagram_edges: List[DiagramEdge] = field(default_factory=list)
    diagram_svg_custom: Optional[str] = None
    justifications: List[DesignJustification] = field(default_factory=list)
    solution_code: str = ""
