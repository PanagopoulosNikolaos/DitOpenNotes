"""Domain data models for computer networks exam scenarios (Archetype B).

Defines the dataclasses that carry the complete original exam paper (the
canvas content), the per-question worked solutions (options, given
parameters, ordered calculation steps with KaTeX strings), the protocol
stack elements, analysis tables, SVG diagram layouts, and design
justifications.
"""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class TextSegment:
    """Represents a segment of the exam paper text.

    Can be plain text or an interactive highlighted token whose tooltip
    satisfies the three-part hover contract (Classification, Detection
    Clue, Application Rationale).

    Attributes:
        text (str): The literal text content of the segment.
        is_highlight (bool): Whether the segment is highlighted.
        category (str): Highlight category: term, given, proto, or method.
        tag_label (Optional[str]): Small badge label next to the token.
        badge_class (Optional[str]): CSS badge class for styling.
        tooltip (Optional[str]): Three-part hover explanation.
    """

    text: str
    is_highlight: bool = False
    category: str = "all"
    tag_label: Optional[str] = None
    badge_class: Optional[str] = None
    tooltip: Optional[str] = None


@dataclass
class Paragraph:
    """Represents a paragraph of the exam paper with interactive segments.

    Attributes:
        segments (List[TextSegment]): Ordered text segments of the paragraph.
        accent_border_color (Optional[str]): Optional left accent border marker.
        is_heading (bool): Whether the paragraph is a Themata heading.
    """

    segments: List[TextSegment]
    accent_border_color: Optional[str] = None
    is_heading: bool = False


@dataclass
class GivenParameter:
    """An exam-given value, cross-referenced with a canvas highlight.

    Attributes:
        label (str): Human-readable parameter name.
        value (str): The literal value as given by the exam.
        source (str): Where the parameter appears in the exam paper.
    """

    label: str
    value: str
    source: str = ""


@dataclass
class QuestionOption:
    """A static multiple-choice option row.

    Attributes:
        letter (str): Option letter (A-D).
        text (str): The option text.
        is_correct (bool): Whether this option is the correct answer.
        explanation (str): Why the option is correct or why it fails.
    """

    letter: str
    text: str
    is_correct: bool = False
    explanation: str = ""


@dataclass
class CalculationStep:
    """An ordered derivation step of a worked solution.

    Attributes:
        label (str): Step label, e.g. 'Βήμα 1'.
        description (str): Rationale of the step (may include inline KaTeX).
        latex (str): KaTeX display string for the formula or substitution.
        result (str): Short result of the step, if any.
    """

    label: str
    description: str = ""
    latex: str = ""
    result: str = ""


@dataclass
class AnalysisRow:
    """A structured breakdown entry for analysis tables.

    Attributes:
        cells (List[str]): Cell values of the row (may include inline KaTeX).
        highlight (bool): Whether the row should be visually emphasized.
    """

    cells: List[str]
    highlight: bool = False


@dataclass
class AnalysisTable:
    """A complete analysis or answer table.

    Attributes:
        title (str): Table caption.
        headers (List[str]): Column headers.
        rows (List[AnalysisRow]): Ordered table rows.
        note (str): Optional footnote under the table.
    """

    title: str
    headers: List[str]
    rows: List[AnalysisRow]
    note: str = ""


@dataclass
class ProtocolLayer:
    """A reference-model layer (the SubjectElement of this course).

    Attributes:
        osi_position (int): OSI layer number (7 = Application, 1 = Physical).
        osi_name (str): OSI layer name.
        osi_role (str): Primary role of the OSI layer.
        tcpip_name (str): Corresponding TCP/IP stack layer.
        pdu (str): The PDU produced at this layer.
        protocols (str): Representative protocols of the layer.
        correspondence (str): Mapping rationale between the two models.
    """

    osi_position: int
    osi_name: str
    osi_role: str
    tcpip_name: str
    pdu: str
    protocols: str
    correspondence: str


@dataclass
class DiagramNode:
    """A pre-calculated node of the interactive SVG diagram.

    Attributes:
        id (str): Unique node identifier.
        label (str): Node header label.
        x (int): Top-left x coordinate in the SVG viewBox.
        y (int): Top-left y coordinate in the SVG viewBox.
        w (int): Node width in pixels.
        details (List[str]): Detail lines revealed by the detail toggle.
        highlight (bool): Whether the node receives the accent border.
    """

    id: str
    label: str
    x: int
    y: int
    w: int
    details: List[str] = field(default_factory=list)
    highlight: bool = False


@dataclass
class DiagramEdge:
    """A connection, transition, or weighted link of the SVG diagram.

    Attributes:
        path (str): SVG path, e.g. 'M x1,y1 L x2,y2' or a bezier curve.
        label (str): Edge label (e.g. link cost or allocation range).
        lx (float): Label x coordinate.
        ly (float): Label y coordinate.
        dashed (bool): Whether the edge is dashed.
        marker (str): Optional end marker id (e.g. 'arrow').
    """

    path: str
    label: str = ""
    lx: float = 0
    ly: float = 0
    dashed: bool = False
    marker: str = ""


@dataclass
class DesignJustification:
    """A rationale card explaining a problem-solving or design decision.

    Attributes:
        title (str): Card title.
        color_class (str): Tailwind text color utility class for the title.
        description (str): Justification body.
    """

    title: str
    color_class: str
    description: str


@dataclass
class ExamQuestion:
    """A single exam question or sub-question with its worked solution.

    Attributes:
        thema (str): Themata group, e.g. 'Θέμα 1'.
        thema_title (str): Themata heading text from the exam paper.
        sub_number (str): Sub-question number as printed on the paper.
        title (str): Short internal title of the sub-question.
        question_type (str): One of: mcq, computational, theory, comparison.
        prompt (str): Full verbatim prompt text.
        options (List[QuestionOption]): Static MCQ options, if applicable.
        given (List[GivenParameter]): Given parameters of the exercise.
        steps (List[CalculationStep]): Ordered worked-solution steps.
        answer (str): Final answer summary (may include inline KaTeX).
        answer_tables (List[AnalysisTable]): Supporting answer tables.
        tips (List[str]): Exam traps and verification notes.
    """

    thema: str
    thema_title: str
    sub_number: str
    title: str
    question_type: str
    prompt: str
    options: List[QuestionOption] = field(default_factory=list)
    given: List[GivenParameter] = field(default_factory=list)
    steps: List[CalculationStep] = field(default_factory=list)
    answer: str = ""
    answer_tables: List[AnalysisTable] = field(default_factory=list)
    tips: List[str] = field(default_factory=list)


@dataclass
class ExamMeta:
    """Administrative metadata of an exam paper.

    Attributes:
        duration (str): Exam duration as printed on the paper.
        scoring (str): Scoring rule as printed on the paper.
    """

    duration: str
    scoring: str


@dataclass
class Scenario:
    """A complete parsed exam scenario container.

    Attributes:
        id (str): Unique scenario identifier.
        title (str): Exam title shown in selectors.
        subtitle (str): Descriptive subtitle of the exam coverage.
        course_tag (str): Course badge tag.
        exam_meta (ExamMeta): Duration and scoring metadata.
        paragraphs (List[Paragraph]): The full original exam paper text.
        questions (List[ExamQuestion]): Worked solutions in exam order.
        layers (List[ProtocolLayer]): OSI/TCP-IP layer mapping, if relevant.
        analysis_tables (List[AnalysisTable]): Scenario-level analysis tables.
        diagram_title (str): Title of the interactive SVG diagram.
        diagram_nodes (List[DiagramNode]): Pre-calculated diagram nodes.
        diagram_edges (List[DiagramEdge]): Pre-calculated diagram edges.
        diagram_note (str): Explanatory note under the diagram.
        justifications (List[DesignJustification]): Solution rationale cards.
        solution_code (str): Verification code of the model solutions.
        code_language (str): Language identifier of the code block.
    """

    id: str
    title: str
    subtitle: str
    course_tag: str
    exam_meta: ExamMeta
    paragraphs: List[Paragraph]
    questions: List[ExamQuestion]
    layers: List[ProtocolLayer] = field(default_factory=list)
    analysis_tables: List[AnalysisTable] = field(default_factory=list)
    diagram_title: str = ""
    diagram_nodes: List[DiagramNode] = field(default_factory=list)
    diagram_edges: List[DiagramEdge] = field(default_factory=list)
    diagram_note: str = ""
    justifications: List[DesignJustification] = field(default_factory=list)
    solution_code: str = ""
    code_language: str = "python"
