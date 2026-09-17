"""Domain data models for Course 203: Discrete Mathematics.

Defines the structure for storing exam exercises, multi-team variations,
graph visualizer topologies, Venn diagram sets, induction proof steps,
and finite state automata.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any


@dataclass
class ExamExercise:
    """Represents an isolated exam problem with multi-team variants and step-by-step derivations."""
    number: int
    title: str
    points: float
    topic: str
    statements: Dict[str, str]  # 'Group A': '...', 'Group B': '...'
    steps: Dict[str, List[str]]  # 'Group A': ['Step 1...', 'Step 2...']
    final_answers: Dict[str, str]  # 'Group A': '...'
    pitfalls: str = ""
    interactive_type: Optional[str] = None  # 'truth_table', 'graph', 'venn', 'dfa', 'induction'


@dataclass
class GraphNode:
    """Represents a vertex in an interactive graph canvas."""
    id: str
    label: str
    x: float
    y: float


@dataclass
class GraphEdge:
    """Represents an edge connecting two vertices."""
    u: str
    v: str
    label: Optional[str] = None
    is_directed: bool = False


@dataclass
class GraphModel:
    """Represents a graph topology for isomorphism, traversal, and Euler planarity."""
    id: str
    title: str
    nodes: List[GraphNode]
    edges: List[GraphEdge]
    is_planar: bool = True
    description: str = ""


@dataclass
class VennModel:
    """Represents sets for interactive Venn diagram operations and PIE."""
    title: str
    universal_set: List[str]
    set_a: List[str]
    set_b: List[str]
    set_c: List[str] = field(default_factory=list)
    description: str = ""


@dataclass
class InductionModel:
    """Represents a 4-stage mathematical induction proof."""
    title: str
    proposition: str
    base_step: str
    inductive_hypothesis: str
    inductive_step: str
    conclusion: str


@dataclass
class AutomatonModel:
    """Represents a deterministic finite automaton (DFA) or state machine."""
    states: List[str]
    alphabet: List[str]
    initial_state: str
    accepting_states: List[str]
    transitions: Dict[str, Dict[str, str]]  # state -> {char -> next_state}
    regex: str = ""
    description: str = ""


@dataclass
class Scenario:
    """Represents a complete discrete mathematics exam or practice session."""
    id: str
    title: str
    subtitle: str
    course_tag: str
    academic_year: str
    total_points: float
    duration_hours: float
    exercises: List[ExamExercise]
    graphs: List[GraphModel] = field(default_factory=list)
    venn_data: Optional[VennModel] = None
    induction_data: Optional[InductionModel] = None
    automaton_data: Optional[AutomatonModel] = None
    formula_chips: List[Dict[str, str]] = field(default_factory=list)
