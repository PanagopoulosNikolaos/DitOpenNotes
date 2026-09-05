"""Data models for ER Analysis scenarios, entities, attributes, keys, and diagrams.

Defines the structure for storing and rendering database design case studies,
including Chen and Crow's Foot notations and relational schema mapping.
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any


@dataclass
class TextSegment:
    """Represents a segment of text in the problem description.

    Can be plain text or an interactive highlighted element.
    """
    text: str
    is_highlight: bool = False
    category: str = "all"  # entity, key, attr, rel
    tag_label: Optional[str] = None  # e.g., 'ENTITY', 'PK', 'RELATIONSHIP 1:N'
    badge_class: Optional[str] = None  # CSS class for badge styling
    tooltip: Optional[str] = None  # Detailed explanation on hover


@dataclass
class Paragraph:
    """Represents a paragraph in the requirements text with interactive segments."""
    segments: List[TextSegment]
    accent_border_color: Optional[str] = None  # Left border accent class or color


@dataclass
class Attribute:
    """Represents an entity or relationship attribute."""
    name: str
    attr_type: str  # 'Simple / Single-valued', 'Composite', 'Multivalued', 'Derived'
    is_pk: bool = False
    is_candidate: bool = False
    is_partial: bool = False
    is_fk: bool = False
    components: List[str] = field(default_factory=list)  # Sub-attributes for composite
    notes: Optional[str] = None


@dataclass
class Entity:
    """Represents an ER entity definition with justifications."""
    name: str
    entity_type: str  # 'Strong Entity' or 'Weak Entity'
    is_weak: bool = False
    owner_entity: Optional[str] = None
    justification: str = ""
    attributes: List[Attribute] = field(default_factory=list)


@dataclass
class RelationshipAttribute:
    """Represents an attribute attached directly to a relationship."""
    name: str
    relationship_name: str
    justification: str


@dataclass
class KeyAnalysisRow:
    """Represents an entry in the key analysis table."""
    entity_name: str
    key_count: str
    key_types: str
    final_pk_selection: str
    justification: str
    is_weak: bool = False


@dataclass
class Relationship:
    """Represents a relationship between entities."""
    letter_id: str  # e.g. 'a', 'b', 'c' or '1', '2', '3'
    name: str
    connected_entities: str  # e.g. 'Researcher <-> Research Unit'
    cardinality: str  # e.g. '1:1', '1:N', 'N:M'
    participation: str  # e.g. 'Total for Unit, Partial for Researcher'
    relationship_type: str = "Regular Relationship"  # or 'Identifying Relationship'
    attributes: List[str] = field(default_factory=list)
    justification: str = ""


@dataclass
class ERTableAttr:
    """Attribute representation inside an SVG table node."""
    name: str
    pk: bool = False
    fk: bool = False


@dataclass
class ERTable:
    """Table node in the relational/Crow's Foot diagram."""
    id: str
    label: str
    x: int
    y: int
    attrs: List[ERTableAttr] = field(default_factory=list)


@dataclass
class EREdge:
    """Relationship edge connecting tables in the ER diagram."""
    path: str
    marker_start: str
    marker_end: str
    label: str
    lx: float
    ly: float


@dataclass
class RelationalJustification:
    """Design rationale for relational mapping decisions."""
    title: str
    color_class: str
    description: str


@dataclass
class Scenario:
    """Complete case study scenario container."""
    id: str
    title: str
    subtitle: str
    course_tag: str
    paragraphs: List[Paragraph]
    entities: List[Entity]
    relationship_attributes: List[RelationshipAttribute]
    keys_analysis: List[KeyAnalysisRow]
    relationships: List[Relationship]
    assumptions: List[str]
    er_tables: List[ERTable]
    er_edges: List[EREdge]
    relational_justifications: List[RelationalJustification]
    sql_ddl: str = ""
