"""Research Institute case study scenario module.

Contains the complete parsed and corrected ER analysis for the Research Institute
problem (Course 404), including all entities, full attribute breakdowns,
relationship cardinalities, keys analysis, and Crow's Foot ER diagram layout.
"""

from models.scenario import (
    Scenario,
    Paragraph,
    TextSegment,
    Entity,
    Attribute,
    RelationshipAttribute,
    KeyAnalysisRow,
    Relationship,
    ERTable,
    ERTableAttr,
    EREdge,
    RelationalJustification,
)


def createResearchInstituteScenario() -> Scenario:
    """Constructs and returns the Research Institute database scenario.

    Returns:
        Scenario: Fully populated scenario instance with corrected data.
    """
    # 1. Text Paragraphs with Interactive Segments
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="A research institute maintains information about the "),
                TextSegment(
                    text="researchers",
                    is_highlight=True,
                    category="entity",
                    tag_label="ENTITY",
                    badge_class="badge-entity-strong",
                    tooltip="Strong Entity: Natural person with autonomous existence and ID number.",
                ),
                TextSegment(text=", the "),
                TextSegment(
                    text="research units",
                    is_highlight=True,
                    category="entity",
                    tag_label="ENTITY",
                    badge_class="badge-entity-strong",
                    tooltip="Strong Entity: Autonomous administrative department with a unique code.",
                ),
                TextSegment(text=" and the "),
                TextSegment(
                    text="research projects",
                    is_highlight=True,
                    category="entity",
                    tag_label="ENTITY",
                    badge_class="badge-entity-strong",
                    tooltip="Strong Entity: Autonomous project with a unique number.",
                ),
                TextSegment(text=" it implements."),
            ],
            accent_border_color=None,
        ),
        Paragraph(
            segments=[
                TextSegment(text="Each <strong>research unit</strong> has a "),
                TextSegment(
                    text="unique code",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Primary Key: Unique artificial identifier code.",
                ),
                TextSegment(text=", a "),
                TextSegment(
                    text="unique name",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Candidate Key: Alternative unique alphanumeric name.",
                ),
                TextSegment(text=" and a specific researcher who is "),
                TextSegment(
                    text="scientifically responsible",
                    is_highlight=True,
                    category="rel",
                    tag_label="RELATIONSHIP 1:1",
                    badge_class="badge-rel",
                    tooltip="1:1 Relationship between Researcher & Unit (Total participation for unit, partial for researcher).",
                ),
                TextSegment(text=" for it. For each person in charge, the "),
                TextSegment(
                    text="date of taking office",
                    is_highlight=True,
                    category="attr",
                    tag_label="REL ATTRIBUTE",
                    badge_class="badge-attr-simple",
                    tooltip="Relationship Attribute: Describes when the supervisor took office in the specific unit.",
                ),
                TextSegment(text=" is recorded. The research units have "),
                TextSegment(
                    text="facilities located in various geographic areas",
                    is_highlight=True,
                    category="attr",
                    tag_label="MULTIVALUED",
                    badge_class="badge-attr-multi",
                    tooltip="Multivalued Attribute: A unit can have multiple facility locations.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-blue-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Each research unit "),
                TextSegment(
                    text="implements",
                    is_highlight=True,
                    category="rel",
                    tag_label="RELATIONSHIP 1:N",
                    badge_class="badge-rel",
                    tooltip="1:N Relationship between Unit & Projects (A unit implements many projects, each project belongs to 1 unit).",
                ),
                TextSegment(text=" many research projects. Each project has a "),
                TextSegment(
                    text="unique number",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Primary Key: Unique numeric identifier for the project.",
                ),
                TextSegment(text=", a "),
                TextSegment(
                    text="unique title",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Candidate Key: Alternative unique project title.",
                ),
                TextSegment(text=" and takes place in a "),
                TextSegment(
                    text="specific venue",
                    is_highlight=True,
                    category="attr",
                    tag_label="ATTRIBUTE",
                    badge_class="badge-attr-simple",
                    tooltip="Simple Single-valued Attribute: Describes the location/facility where the project is conducted.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-amber-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="For each researcher, the following data are recorded: "),
                TextSegment(text="first name", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="last name", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(
                    text="ID number",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Primary Key: Unique national identification card number.",
                ),
                TextSegment(text=", "),
                TextSegment(text="scientific field", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(
                    text="residential address",
                    is_highlight=True,
                    category="attr",
                    tag_label="COMPOSITE",
                    badge_class="badge-attr-composite",
                    tooltip="Composite Attribute: Decomposed into Street, Number, Postal Code, City.",
                ),
                TextSegment(text=", "),
                TextSegment(text="monthly salary", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="gender", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=" and "),
                TextSegment(text="date of birth", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=". Each researcher "),
                TextSegment(
                    text="belongs",
                    is_highlight=True,
                    category="rel",
                    tag_label="RELATIONSHIP 1:N",
                    badge_class="badge-rel",
                    tooltip="1:N Relationship (Unit -> Researcher): Each researcher belongs to 1 unit; the unit employs many.",
                ),
                TextSegment(text=" to a specific research unit, but may "),
                TextSegment(
                    text="participate",
                    is_highlight=True,
                    category="rel",
                    tag_label="RELATIONSHIP N:M",
                    badge_class="badge-rel",
                    tooltip="N:M Relationship between Researcher & Project: Multiple researchers work on multiple projects.",
                ),
                TextSegment(
                    text=" in the implementation of many research projects, even if those are implemented by other units. For each participation, the "
                ),
                TextSegment(
                    text="number of working hours per week",
                    is_highlight=True,
                    category="attr",
                    tag_label="REL ATTRIBUTE",
                    badge_class="badge-attr-simple",
                    tooltip="Relationship Attribute: Depends jointly on the researcher and the project.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-emerald-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="For each researcher, the "),
                TextSegment(
                    text="dependent members",
                    is_highlight=True,
                    category="entity",
                    tag_label="WEAK ENTITY",
                    badge_class="badge-entity-weak",
                    tooltip="Weak Entity: Existence-dependent on the Researcher, without an independent PK.",
                ),
                TextSegment(text=" of his/her family are also recorded. The data kept are: "),
                TextSegment(
                    text="name",
                    is_highlight=True,
                    category="key",
                    tag_label="PARTIAL KEY",
                    badge_class="badge-key-partial",
                    tooltip="Partial Key (Discriminator): Distinguishes members of the same family.",
                ),
                TextSegment(text=", "),
                TextSegment(text="gender", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="date of birth", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=" and "),
                TextSegment(text="family relationship", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text="."),
            ],
            accent_border_color="border-purple-500",
        ),
    ]

    # 2. Entity Definitions with Justifications & Full Attributes Breakdown
    entities = [
        Entity(
            name="RESEARCH_UNIT",
            entity_type="Strong Entity",
            is_weak=False,
            justification=(
                "Describes an autonomous administrative/organizational department of the institute. "
                "It is strong because it possesses its own unique identifier (unit_code) "
                "and is not existence-dependent on another entity."
            ),
            attributes=[
                Attribute(name="unit_code", attr_type="Simple, Single-valued (Primary Key)", is_pk=True),
                Attribute(name="unit_name", attr_type="Simple, Single-valued (Candidate Key)", is_candidate=True),
                Attribute(
                    name="facilities",
                    attr_type="Multivalued Attribute",
                    notes="The problem text notes 'facilities located in various geographic areas', thus a unit has multiple facility locations.",
                ),
            ],
        ),
        Entity(
            name="RESEARCH_PROJECT",
            entity_type="Strong Entity",
            is_weak=False,
            justification=(
                "Autonomous entity describing a research project with its own unique "
                "identifier (project_number) and independent existence."
            ),
            attributes=[
                Attribute(name="project_number", attr_type="Simple, Single-valued (Primary Key)", is_pk=True),
                Attribute(name="project_title", attr_type="Simple, Single-valued (Candidate Key)", is_candidate=True),
                Attribute(name="venue", attr_type="Simple, Single-valued", notes="Specifies the implementation location/laboratory."),
            ],
        ),
        Entity(
            name="RESEARCHER",
            entity_type="Strong Entity",
            is_weak=False,
            justification=(
                "Natural person working at the institute with autonomous existence and a globally "
                "unique national ID number (id_number)."
            ),
            attributes=[
                Attribute(name="id_number", attr_type="Simple, Single-valued (Primary Key)", is_pk=True),
                Attribute(name="first_name", attr_type="Simple, Single-valued"),
                Attribute(name="last_name", attr_type="Simple, Single-valued"),
                Attribute(name="scientific_field", attr_type="Simple, Single-valued"),
                Attribute(name="monthly_salary", attr_type="Simple, Single-valued"),
                Attribute(name="gender", attr_type="Simple, Single-valued"),
                Attribute(name="birth_date", attr_type="Simple, Single-valued"),
                Attribute(
                    name="residential_address",
                    attr_type="Composite Attribute",
                    components=["street", "number", "postal_code", "city"],
                    notes="Decomposed into atomic attributes during relational schema design.",
                ),
            ],
        ),
        Entity(
            name="DEPENDENT",
            entity_type="Weak Entity",
            is_weak=True,
            owner_entity="RESEARCHER",
            justification=(
                "Weak entity lacking a complete independent key "
                "(name alone is not globally unique) and existence-dependent "
                "on RESEARCHER (deleting the researcher cascades to dependents)."
            ),
            attributes=[
                Attribute(name="dependent_name", attr_type="Partial Key (Discriminator)", is_partial=True),
                Attribute(name="gender", attr_type="Simple, Single-valued"),
                Attribute(name="birth_date", attr_type="Simple, Single-valued"),
                Attribute(name="family_relationship", attr_type="Simple, Single-valued"),
            ],
        ),
    ]

    # 3. Relationship Attributes
    relationship_attributes = [
        RelationshipAttribute(
            name="date_appointed",
            relationship_name="HEADED_BY (1:1)",
            justification="Records the timestamp when the specific researcher was appointed head of the unit.",
        ),
        RelationshipAttribute(
            name="weekly_hours",
            relationship_name="PARTICIPATES_IN (N:M)",
            justification="Jointly depends on the pair (Researcher, Project), as a researcher commits different hours to each project.",
        ),
    ]

    # 4. Keys Analysis Table
    keys_analysis = [
        KeyAnalysisRow(
            entity_name="RESEARCH_UNIT",
            key_count="2",
            key_types="Candidates: {unit_code}, {unit_name}",
            final_pk_selection="unit_code",
            justification="Compact, stable artificial numeric/alphanumeric code preferred over mutable name.",
            is_weak=False,
        ),
        KeyAnalysisRow(
            entity_name="RESEARCH_PROJECT",
            key_count="2",
            key_types="Candidates: {project_number}, {project_title}",
            final_pk_selection="project_number",
            justification="Short, unique identifier unchanged throughout the project lifecycle.",
            is_weak=False,
        ),
        KeyAnalysisRow(
            entity_name="RESEARCHER",
            key_count="1",
            key_types="Candidate: {id_number}",
            final_pk_selection="id_number",
            justification="Official government-issued unique person identification number.",
            is_weak=False,
        ),
        KeyAnalysisRow(
            entity_name="DEPENDENT",
            key_count="0 (Weak Entity / Partial Key)",
            key_types="Partial Key: {dependent_name}",
            final_pk_selection="{researcher_id, dependent_name}",
            justification="Composite Primary Key in relational mapping (combines Owner PK + Partial Key).",
            is_weak=True,
        ),
    ]

    # 5. Relationships & Cardinalities
    relationships = [
        Relationship(
            letter_id="a",
            name="HEADED_BY",
            connected_entities="Researcher <-> Research Unit",
            cardinality="1:1",
            participation="Total for Unit, Partial for Researcher",
            relationship_type="Regular Relationship",
            attributes=["date_appointed"],
            justification=(
                "• Unit -> Researcher (1): 'a specific researcher who is scientifically responsible for it'. "
                "• Researcher -> Unit (1): Design assumption that a researcher heads at most 1 unit."
            ),
        ),
        Relationship(
            letter_id="b",
            name="IMPLEMENTS",
            connected_entities="Research Unit <-> Research Project",
            cardinality="1:N",
            participation="Total for Project",
            relationship_type="Regular Relationship",
            attributes=[],
            justification=(
                "• Unit -> Project (N): 'Each research unit implements many research projects'. "
                "• Project -> Unit (1): Each project is administered by 1 managing research unit."
            ),
        ),
        Relationship(
            letter_id="c",
            name="BELONGS_TO",
            connected_entities="Researcher <-> Research Unit",
            cardinality="1:N",
            participation="Total for Researcher",
            relationship_type="Regular Relationship",
            attributes=[],
            justification=(
                "• Researcher -> Unit (1): 'Each researcher belongs to a specific research unit'. "
                "• Unit -> Researcher (N): A unit employs multiple researchers."
            ),
        ),
        Relationship(
            letter_id="d",
            name="PARTICIPATES_IN",
            connected_entities="Researcher <-> Research Project",
            cardinality="N:M",
            participation="Partial for both sides",
            relationship_type="Regular Relationship (Junction)",
            attributes=["weekly_hours"],
            justification=(
                "• Researcher -> Project (M): 'may participate in the implementation of many research projects'. "
                "• Project -> Researcher (N): A project is implemented by a team of multiple researchers."
            ),
        ),
        Relationship(
            letter_id="e",
            name="HAS_DEPENDENT",
            connected_entities="Researcher <-> Dependent",
            cardinality="1:N",
            participation="Total for Dependent",
            relationship_type="Identifying Relationship",
            attributes=[],
            justification=(
                "A researcher may have 0, 1, or N dependents. "
                "Each dependent belongs mandatorily to 1 specific researcher-guardian."
            ),
        ),
    ]

    # 6. Design Assumptions
    assumptions = [
        "Residential Address: Assumed to be decomposed into atomic attributes (Street, Number, Postal Code, City), hence modeled as composite.",
        "Scientific Field: Assumed that each researcher declares one primary scientific field (single-valued).",
        "Scientific Supervisor: Assumed that a researcher cannot be head of more than one unit simultaneously (1:1 ratio).",
        "Unit Facilities: Extracted into a separate table (UNIT_FACILITY) to satisfy First Normal Form (1NF).",
    ]

    # 7. ER Diagram Tables
    er_tables = [
        ERTable(
            id="unit",
            label="RESEARCH_UNIT",
            x=50,
            y=150,
            attrs=[
                ERTableAttr(name="unit_code", pk=True),
                ERTableAttr(name="unit_name"),
                ERTableAttr(name="head_id", fk=True),
                ERTableAttr(name="date_appointed"),
            ],
        ),
        ERTable(
            id="facility",
            label="UNIT_FACILITY",
            x=50,
            y=450,
            attrs=[
                ERTableAttr(name="unit_code", pk=True, fk=True),
                ERTableAttr(name="facility_location", pk=True),
            ],
        ),
        ERTable(
            id="researcher",
            label="RESEARCHER",
            x=430,
            y=50,
            attrs=[
                ERTableAttr(name="id_number", pk=True),
                ERTableAttr(name="first_name"),
                ERTableAttr(name="last_name"),
                ERTableAttr(name="scientific_field"),
                ERTableAttr(name="monthly_salary"),
                ERTableAttr(name="gender"),
                ERTableAttr(name="birth_date"),
                ERTableAttr(name="street"),
                ERTableAttr(name="street_number"),
                ERTableAttr(name="postal_code"),
                ERTableAttr(name="city"),
                ERTableAttr(name="unit_code", fk=True),
            ],
        ),
        ERTable(
            id="dependent",
            label="DEPENDENT",
            x=430,
            y=530,
            attrs=[
                ERTableAttr(name="researcher_id", pk=True, fk=True),
                ERTableAttr(name="dependent_name", pk=True),
                ERTableAttr(name="gender"),
                ERTableAttr(name="birth_date"),
                ERTableAttr(name="family_relationship"),
            ],
        ),
        ERTable(
            id="project",
            label="RESEARCH_PROJECT",
            x=810,
            y=150,
            attrs=[
                ERTableAttr(name="project_number", pk=True),
                ERTableAttr(name="project_title"),
                ERTableAttr(name="venue"),
                ERTableAttr(name="managing_unit_code", fk=True),
            ],
        ),
        ERTable(
            id="participation",
            label="PROJECT_PARTICIPATION",
            x=810,
            y=420,
            attrs=[
                ERTableAttr(name="researcher_id", pk=True, fk=True),
                ERTableAttr(name="project_number", pk=True, fk=True),
                ERTableAttr(name="weekly_hours"),
            ],
        ),
    ]

    # 8. ER Diagram Edges
    er_edges = [
        EREdge(
            path="M 180,150 L 180,25 L 940,25 L 940,150",
            marker_start="start-one-mandatory",
            marker_end="end-many-mandatory",
            label="Implements (1:N)",
            lx=560,
            ly=25,
        ),
        EREdge(
            path="M 310,200 L 430,200",
            marker_start="start-one-mandatory",
            marker_end="end-one-optional",
            label="Headed by (1:1)",
            lx=370,
            ly=190,
        ),
        EREdge(
            path="M 310,270 L 430,270",
            marker_start="start-one-mandatory",
            marker_end="end-many-mandatory",
            label="Belongs to (1:N)",
            lx=370,
            ly=260,
        ),
        EREdge(
            path="M 180,310 L 180,450",
            marker_start="start-one-mandatory",
            marker_end="end-many-mandatory",
            label="Facilities (1:N)",
            lx=180,
            ly=380,
        ),
        EREdge(
            path="M 560,434 L 560,530",
            marker_start="start-one-optional",
            marker_end="end-many-mandatory",
            label="Maintains (1:N)",
            lx=560,
            ly=482,
        ),
        EREdge(
            path="M 690,430 L 750,430 L 750,440 L 810,440",
            marker_start="start-one-optional",
            marker_end="end-many-mandatory",
            label="Participates (1:N)",
            lx=750,
            ly=415,
        ),
        EREdge(
            path="M 940,310 L 940,420",
            marker_start="start-one-optional",
            marker_end="end-many-mandatory",
            label="Concerns (1:N)",
            lx=940,
            ly=365,
        ),
    ]

    # 9. Relational Justifications
    relational_justifications = [
        RelationalJustification(
            title="1. Crow's Foot Notation Selection:",
            color_class="text-blue-400",
            description=(
                "Directly represents the relational table schema. Entities appear with their attributes "
                "as columns, providing a clear distinction between Primary Keys (PK) and Foreign Keys (FK)."
            ),
        ),
        RelationalJustification(
            title="2. N:M Relationships Resolution (Junction Tables):",
            color_class="text-purple-400",
            description=(
                "The PARTICIPATES_IN relationship between Researcher and Project is decomposed into the intermediate "
                "PROJECT_PARTICIPATION table with a composite Primary Key composed of both Foreign Keys, "
                "also hosting the weekly_hours attribute."
            ),
        ),
        RelationalJustification(
            title="3. Multivalued Attributes Handling:",
            color_class="text-emerald-400",
            description=(
                "The multivalued attribute facilities is extracted into a separate table UNIT_FACILITY, "
                "ensuring First Normal Form (1NF). It connects to RESEARCH_UNIT via a 1:N relationship."
            ),
        ),
        RelationalJustification(
            title="4. Foreign Keys (FK) Placement:",
            color_class="text-rose-400",
            description=(
                "In 1:N relationships (such as Belongs to and Maintains), the FK is placed on the 'N' side. "
                "In the 1:1 relationship (Headed by), the FK is placed in RESEARCH_UNIT together with date_appointed."
            ),
        ),
    ]

    # 10. SQL DDL Schema
    sql_ddl = """-- ==========================================================
-- SQL DDL Schema: Research Institute Database (Chen -> Relational)
-- ==========================================================

-- 1. Table: RESEARCH_UNIT
CREATE TABLE RESEARCH_UNIT (
    unit_code INT PRIMARY KEY,
    unit_name VARCHAR(120) NOT NULL UNIQUE,
    head_id VARCHAR(20) NOT NULL UNIQUE,
    date_appointed DATE NOT NULL
);

-- 2. Table: UNIT_FACILITY (Multivalued Attribute Extraction)
CREATE TABLE UNIT_FACILITY (
    unit_code INT NOT NULL,
    facility_location VARCHAR(150) NOT NULL,
    PRIMARY KEY (unit_code, facility_location),
    FOREIGN KEY (unit_code) REFERENCES RESEARCH_UNIT(unit_code) 
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- 3. Table: RESEARCHER
CREATE TABLE RESEARCHER (
    id_number VARCHAR(20) PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    scientific_field VARCHAR(100) NOT NULL,
    monthly_salary DECIMAL(10, 2) NOT NULL,
    gender CHAR(1) CHECK (gender IN ('M', 'F', 'O')),
    birth_date DATE NOT NULL,
    street VARCHAR(80),
    street_number VARCHAR(10),
    postal_code VARCHAR(10),
    city VARCHAR(50),
    unit_code INT NOT NULL,
    FOREIGN KEY (unit_code) REFERENCES RESEARCH_UNIT(unit_code)
        ON UPDATE CASCADE
);

-- Add Circular Foreign Key for Headed by 1:1
ALTER TABLE RESEARCH_UNIT
    ADD CONSTRAINT fk_unit_head
    FOREIGN KEY (head_id) REFERENCES RESEARCHER(id_number)
        ON UPDATE CASCADE;

-- 4. Table: DEPENDENT (Weak Entity)
CREATE TABLE DEPENDENT (
    researcher_id VARCHAR(20) NOT NULL,
    dependent_name VARCHAR(50) NOT NULL,
    gender CHAR(1) CHECK (gender IN ('M', 'F', 'O')),
    birth_date DATE NOT NULL,
    family_relationship VARCHAR(50) NOT NULL,
    PRIMARY KEY (researcher_id, dependent_name),
    FOREIGN KEY (researcher_id) REFERENCES RESEARCHER(id_number)
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- 5. Table: RESEARCH_PROJECT
CREATE TABLE RESEARCH_PROJECT (
    project_number INT PRIMARY KEY,
    project_title VARCHAR(150) NOT NULL UNIQUE,
    venue VARCHAR(100) NOT NULL,
    managing_unit_code INT NOT NULL,
    FOREIGN KEY (managing_unit_code) REFERENCES RESEARCH_UNIT(unit_code)
        ON UPDATE CASCADE
);

-- 6. Table: PROJECT_PARTICIPATION (N:M Junction Table)
CREATE TABLE PROJECT_PARTICIPATION (
    researcher_id VARCHAR(20) NOT NULL,
    project_number INT NOT NULL,
    weekly_hours DECIMAL(5, 2) NOT NULL DEFAULT 0.0,
    PRIMARY KEY (researcher_id, project_number),
    FOREIGN KEY (researcher_id) REFERENCES RESEARCHER(id_number)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (project_number) REFERENCES RESEARCH_PROJECT(project_number)
        ON DELETE CASCADE ON UPDATE CASCADE
);"""

    return Scenario(
        id="research_institute",
        title="Research Institute & Projects",
        subtitle="Interactive Requirements Canvas, Methodology & Complete E-R Diagram",
        course_tag="Database Systems (Course 404)",
        paragraphs=paragraphs,
        entities=entities,
        relationship_attributes=relationship_attributes,
        keys_analysis=keys_analysis,
        relationships=relationships,
        assumptions=assumptions,
        er_tables=er_tables,
        er_edges=er_edges,
        relational_justifications=relational_justifications,
        sql_ddl=sql_ddl,
    )
