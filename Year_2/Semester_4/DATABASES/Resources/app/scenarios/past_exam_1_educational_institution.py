"""Past Exam Paper 1 (Educational Institution) case study scenario module.

Contains the complete parsed and modeled ER analysis for the Educational Institution
(Faculties, Facilities, Educational Programs, Professors, Dependents, and Program Assignments),
including full attribute breakdowns, relationship cardinalities, keys analysis, Crow's Foot
ER diagram layout, relational schema mapping, and SQL DDL.
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


def createPastExam1Scenario() -> Scenario:
    """Constructs and returns the Past Exam 1 database scenario.

    Returns:
        Scenario: Fully populated scenario instance.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="An educational institution maintains information about the "),
                TextSegment(
                    text="faculties",
                    is_highlight=True,
                    category="entity",
                    tag_label="ENTITY",
                    badge_class="badge-entity-strong",
                    tooltip="Strong Entity: Autonomous academic faculty.",
                ),
                TextSegment(text=", the "),
                TextSegment(
                    text="educational programs",
                    is_highlight=True,
                    category="entity",
                    tag_label="ENTITY",
                    badge_class="badge-entity-strong",
                    tooltip="Strong Entity: Educational study/training program.",
                ),
                TextSegment(text=", the "),
                TextSegment(
                    text="professors",
                    is_highlight=True,
                    category="entity",
                    tag_label="ENTITY",
                    badge_class="badge-entity-strong",
                    tooltip="Strong Entity: Teaching academic staff.",
                ),
                TextSegment(text=" and the "),
                TextSegment(
                    text="dependent members",
                    is_highlight=True,
                    category="entity",
                    tag_label="WEAK ENTITY",
                    badge_class="badge-entity-weak",
                    tooltip="Weak Entity: Family members dependent on a professor.",
                ),
                TextSegment(text=" it offers."),
            ],
            accent_border_color=None,
        ),
        Paragraph(
            segments=[
                TextSegment(text="1. <strong>Faculties & Facilities:</strong> Each faculty has a "),
                TextSegment(text="unique code", is_highlight=True, category="key", tag_label="PK", badge_class="badge-key-pk"),
                TextSegment(text=", a "),
                TextSegment(text="unique name", is_highlight=True, category="key", tag_label="CANDIDATE KEY", badge_class="badge-key-candidate"),
                TextSegment(text=" and a specific "),
                TextSegment(text="professor who heads it (1:1)", is_highlight=True, category="rel", tag_label="RELATIONSHIP 1:1", badge_class="badge-rel"),
                TextSegment(text=". The date the head "),
                TextSegment(text="took office", is_highlight=True, category="attr", tag_label="REL ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=" is recorded. The faculties have "),
                TextSegment(
                    text="facilities located in various geographic areas",
                    is_highlight=True,
                    category="attr",
                    tag_label="MULTIVALUED",
                    badge_class="badge-attr-multi",
                    tooltip="Multivalued Attribute / Weak Entity: Mapped to FACULTY_LOCATION table.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color=None,
        ),
        Paragraph(
            segments=[
                TextSegment(text="2. <strong>Educational Programs:</strong> Each faculty offers many educational programs. Each program has a "),
                TextSegment(text="unique number", is_highlight=True, category="key", tag_label="PK", badge_class="badge-key-pk"),
                TextSegment(text=", a "),
                TextSegment(text="unique title", is_highlight=True, category="key", tag_label="CANDIDATE KEY", badge_class="badge-key-candidate"),
                TextSegment(text=" and takes place in a specific "),
                TextSegment(text="venue", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text="."),
            ],
            accent_border_color=None,
        ),
        Paragraph(
            segments=[
                TextSegment(text="3. <strong>Professors & Teaching:</strong> For each professor, the following data are recorded: "),
                TextSegment(text="first name", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="last name", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="ID number", is_highlight=True, category="key", tag_label="PK", badge_class="badge-key-pk"),
                TextSegment(text=", "),
                TextSegment(text="specialty", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="residential address", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="monthly salary", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="gender", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=" and "),
                TextSegment(text="date of birth", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=". Each professor "),
                TextSegment(text="belongs to a specific faculty", is_highlight=True, category="rel", tag_label="RELATIONSHIP N:1", badge_class="badge-rel"),
                TextSegment(text=" and may "),
                TextSegment(text="participate in the implementation of many educational programs", is_highlight=True, category="rel", tag_label="RELATIONSHIP N:M", badge_class="badge-rel"),
                TextSegment(text=" (with recording of "),
                TextSegment(text="weekly working hours", is_highlight=True, category="attr", tag_label="REL ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=")."),
            ],
            accent_border_color=None,
        ),
        Paragraph(
            segments=[
                TextSegment(text="4. <strong>Dependents:</strong> For each professor, the dependent members of his/her family are also recorded. The data kept are: "),
                TextSegment(text="name", is_highlight=True, category="key", tag_label="PARTIAL KEY", badge_class="badge-key-partial"),
                TextSegment(text=", "),
                TextSegment(text="gender", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="date of birth", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=" and "),
                TextSegment(text="family relationship", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=". Each dependent member "),
                TextSegment(text="is associated with a specific professor", is_highlight=True, category="rel", tag_label="IDENTIFYING 1:N", badge_class="badge-rel"),
                TextSegment(text="."),
            ],
            accent_border_color=None,
        ),
    ]

    entities = [
        Entity(
            name="FACULTY",
            entity_type="Strong Entity",
            is_weak=False,
            justification="Autonomous academic unit of the institution with a unique faculty code.",
            attributes=[
                Attribute(name="faculty_code", attr_type="Simple, Single-valued", is_pk=True),
                Attribute(name="faculty_name", attr_type="Simple, Single-valued", is_candidate=True),
            ],
        ),
        Entity(
            name="FACULTY_LOCATION",
            entity_type="Weak Entity / Multivalued Attribute",
            is_weak=True,
            owner_entity="FACULTY",
            justification="Geographic facility location of the faculty. Existence-dependent on FACULTY.",
            attributes=[
                Attribute(name="geographic_area", attr_type="Partial Key", is_partial=True, is_pk=False),
            ],
        ),
        Entity(
            name="EDUCATIONAL_PROGRAM",
            entity_type="Strong Entity",
            is_weak=False,
            justification="Autonomous curriculum program with a unique program number.",
            attributes=[
                Attribute(name="program_number", attr_type="Simple, Single-valued", is_pk=True),
                Attribute(name="program_title", attr_type="Simple, Single-valued", is_candidate=True),
                Attribute(name="venue", attr_type="Simple, Single-valued"),
            ],
        ),
        Entity(
            name="PROFESSOR",
            entity_type="Strong Entity",
            is_weak=False,
            justification="Academic teaching staff member with a unique national ID number.",
            attributes=[
                Attribute(name="id_number", attr_type="Simple, Single-valued", is_pk=True),
                Attribute(name="first_name", attr_type="Simple, Single-valued"),
                Attribute(name="last_name", attr_type="Simple, Single-valued"),
                Attribute(name="specialty", attr_type="Simple, Single-valued"),
                Attribute(name="residential_address", attr_type="Simple, Single-valued"),
                Attribute(name="monthly_salary", attr_type="Simple, Single-valued"),
                Attribute(name="gender", attr_type="Simple, Single-valued"),
                Attribute(name="birth_date", attr_type="Simple, Single-valued"),
            ],
        ),
        Entity(
            name="DEPENDENT",
            entity_type="Weak Entity",
            is_weak=True,
            owner_entity="PROFESSOR",
            justification="Family member of a professor. Existence-dependent on PROFESSOR (Owner Entity).",
            attributes=[
                Attribute(name="dependent_name", attr_type="Partial Key", is_partial=True, is_pk=False),
                Attribute(name="gender", attr_type="Simple, Single-valued"),
                Attribute(name="birth_date", attr_type="Simple, Single-valued"),
                Attribute(name="family_relationship", attr_type="Simple, Single-valued"),
            ],
        ),
    ]

    relationship_attributes = [
        RelationshipAttribute(
            name="date_appointed",
            relationship_name="MANAGES (FACULTY - PROFESSOR)",
            justification="Records the start date of the professor's appointment as faculty head.",
        ),
        RelationshipAttribute(
            name="weekly_hours",
            relationship_name="PARTICIPATES_IN (PROFESSOR - EDUCATIONAL_PROGRAM)",
            justification="Records the weekly teaching hours of the professor in the specific program.",
        ),
    ]

    keys_analysis = [
        KeyAnalysisRow(
            entity_name="FACULTY",
            key_count="2 Candidates",
            key_types="Candidates: {faculty_code}, {faculty_name}",
            final_pk_selection="faculty_code",
            justification="Compact artificial identifier for the academic unit.",
            is_weak=False,
        ),
        KeyAnalysisRow(
            entity_name="FACULTY_LOCATION",
            key_count="Weak (1 Partial)",
            key_types="Composite PK: {faculty_code, geographic_area}",
            final_pk_selection="faculty_code + geographic_area",
            justification="Weak entity / multivalued attribute dependent on faculty.",
            is_weak=True,
        ),
        KeyAnalysisRow(
            entity_name="EDUCATIONAL_PROGRAM",
            key_count="2 Candidates",
            key_types="Candidates: {program_number}, {program_title}",
            final_pk_selection="program_number",
            justification="Unique numeric identifier for the educational program.",
            is_weak=False,
        ),
        KeyAnalysisRow(
            entity_name="PROFESSOR",
            key_count="1 Unique",
            key_types="Candidate: {id_number}",
            final_pk_selection="id_number",
            justification="Unique National ID card number.",
            is_weak=False,
        ),
        KeyAnalysisRow(
            entity_name="DEPENDENT",
            key_count="Weak (1 Partial)",
            key_types="Composite PK: {professor_id, dependent_name}",
            final_pk_selection="professor_id + dependent_name",
            justification="Weak entity with dependent member name as discriminator.",
            is_weak=True,
        ),
    ]

    relationships = [
        Relationship(
            letter_id="a",
            name="MANAGES",
            connected_entities="FACULTY <-> PROFESSOR",
            cardinality="1:1",
            participation="Total for Faculty, Partial for Professor",
            relationship_type="Regular Relationship",
            justification="Each faculty is directed by 1 professor. A professor may direct at most 1 faculty.",
            attributes=["date_appointed"],
        ),
        Relationship(
            letter_id="b",
            name="HAS_LOCATION",
            connected_entities="FACULTY <-> FACULTY_LOCATION",
            cardinality="1:N",
            participation="Total for both sides",
            relationship_type="Identifying Relationship",
            justification="Each faculty maintains facilities across 1 or more geographic areas.",
        ),
        Relationship(
            letter_id="c",
            name="OFFERS",
            connected_entities="FACULTY <-> EDUCATIONAL_PROGRAM",
            cardinality="1:N",
            participation="Total for Program, Partial for Faculty",
            relationship_type="Regular Relationship",
            justification="Each program is offered by 1 faculty. A faculty offers 0 or more programs.",
        ),
        Relationship(
            letter_id="d",
            name="BELONGS_TO",
            connected_entities="PROFESSOR <-> FACULTY",
            cardinality="N:1",
            participation="Total for Professor, Partial for Faculty",
            relationship_type="Regular Relationship",
            justification="Each professor belongs mandatorily to exactly 1 specific faculty.",
        ),
        Relationship(
            letter_id="e",
            name="PARTICIPATES_IN",
            connected_entities="PROFESSOR <-> EDUCATIONAL_PROGRAM",
            cardinality="N:M",
            participation="Partial for both sides",
            relationship_type="Regular Relationship",
            justification="A professor may teach in multiple educational programs (even from other faculties).",
            attributes=["weekly_hours"],
        ),
        Relationship(
            letter_id="f",
            name="HAS_DEPENDENT",
            connected_entities="PROFESSOR <-> DEPENDENT",
            cardinality="1:N",
            participation="Total for Dependent, Partial for Professor",
            relationship_type="Identifying Relationship",
            justification="Each dependent member is existence-dependent on 1 professor.",
        ),
    ]

    er_tables = [
        ERTable(
            id="sxoli",
            label="FACULTY",
            x=50,
            y=60,
            attrs=[
                ERTableAttr(name="faculty_code", pk=True),
                ERTableAttr(name="faculty_name"),
                ERTableAttr(name="dean_id", fk=True),
                ERTableAttr(name="date_appointed"),
            ],
        ),
        ERTable(
            id="egkatastasi_scholis",
            label="FACULTY_LOCATION",
            x=50,
            y=340,
            attrs=[
                ERTableAttr(name="faculty_code", pk=True, fk=True),
                ERTableAttr(name="geographic_area", pk=True),
            ],
        ),
        ERTable(
            id="ekpaideutiko_programma",
            label="EDUCATIONAL_PROGRAM",
            x=450,
            y=60,
            attrs=[
                ERTableAttr(name="program_number", pk=True),
                ERTableAttr(name="program_title"),
                ERTableAttr(name="venue"),
                ERTableAttr(name="supervising_faculty_code", fk=True),
            ],
        ),
        ERTable(
            id="kathigitis",
            label="PROFESSOR",
            x=450,
            y=340,
            attrs=[
                ERTableAttr(name="id_number", pk=True),
                ERTableAttr(name="first_name"),
                ERTableAttr(name="last_name"),
                ERTableAttr(name="specialty"),
                ERTableAttr(name="residential_address"),
                ERTableAttr(name="monthly_salary"),
                ERTableAttr(name="gender"),
                ERTableAttr(name="birth_date"),
                ERTableAttr(name="faculty_code", fk=True),
            ],
        ),
        ERTable(
            id="exartomeno_melos",
            label="DEPENDENT",
            x=850,
            y=340,
            attrs=[
                ERTableAttr(name="professor_id", pk=True, fk=True),
                ERTableAttr(name="dependent_name", pk=True),
                ERTableAttr(name="gender"),
                ERTableAttr(name="birth_date"),
                ERTableAttr(name="family_relationship"),
            ],
        ),
        ERTable(
            id="symmetochi",
            label="PROGRAM_PARTICIPATION",
            x=850,
            y=60,
            attrs=[
                ERTableAttr(name="professor_id", pk=True, fk=True),
                ERTableAttr(name="program_number", pk=True, fk=True),
                ERTableAttr(name="weekly_hours"),
            ],
        ),
    ]

    er_edges = [
        EREdge(path="M 310,120 L 450,120", marker_start="start-one-mandatory", marker_end="end-many-mandatory", label="OFFERS", lx=380, ly=110),
        EREdge(path="M 180,240 L 180,340", marker_start="start-one-mandatory", marker_end="end-many-mandatory", label="HAS_LOCATION", lx=190, ly=290),
        EREdge(path="M 310,180 L 450,420", marker_start="start-one-mandatory", marker_end="end-one-optional", label="MANAGES", lx=380, ly=300),
        EREdge(path="M 310,140 L 450,400", marker_start="start-one-mandatory", marker_end="end-many-mandatory", label="BELONGS_TO", lx=370, ly=260),
        EREdge(path="M 710,120 L 850,120", marker_start="start-one-mandatory", marker_end="end-many-mandatory", label="PROGRAM", lx=780, ly=110),
        EREdge(path="M 710,420 L 850,160", marker_start="start-one-mandatory", marker_end="end-many-mandatory", label="PARTICIPATES", lx=780, ly=290),
        EREdge(path="M 710,480 L 850,480", marker_start="start-one-mandatory", marker_end="end-many-mandatory", label="HAS_DEPENDENT", lx=780, ly=470),
    ]

    relational_justifications = [
        RelationalJustification(
            title="1. FACULTY & DEAN (1:1 Relationship)",
            description="Total participation of Faculty mandates placing the FK dean_id in FACULTY along with the appointment date.",
            color_class="text-blue-400",
        ),
        RelationalJustification(
            title="2. FACULTY_LOCATION (Multivalued / Weak)",
            description="Created as a separate table with composite PK {faculty_code, geographic_area} and FK referencing FACULTY.",
            color_class="text-amber-400",
        ),
        RelationalJustification(
            title="3. PROGRAM_PARTICIPATION (N:M Relationship)",
            description="The N:M relationship between Professor and Program transforms into a junction table with composite PK {professor_id, program_number} and attribute weekly_hours.",
            color_class="text-rose-400",
        ),
        RelationalJustification(
            title="4. DEPENDENT (Weak Entity)",
            description="Receives owner PK professor_id as FK and combines it with discriminator dependent_name for composite PK.",
            color_class="text-purple-400",
        ),
    ]

    sql_ddl = """-- SQL DDL Schema: Educational Institution Database (Past Exam 1)

CREATE TABLE FACULTY (
    faculty_code VARCHAR(15) PRIMARY KEY,
    faculty_name VARCHAR(100) NOT NULL UNIQUE,
    dean_id VARCHAR(15),
    date_appointed DATE
);

CREATE TABLE FACULTY_LOCATION (
    faculty_code VARCHAR(15),
    geographic_area VARCHAR(100),
    PRIMARY KEY (faculty_code, geographic_area),
    FOREIGN KEY (faculty_code) REFERENCES FACULTY(faculty_code) ON DELETE CASCADE
);

CREATE TABLE EDUCATIONAL_PROGRAM (
    program_number INT PRIMARY KEY,
    program_title VARCHAR(150) NOT NULL UNIQUE,
    venue VARCHAR(100),
    supervising_faculty_code VARCHAR(15) NOT NULL,
    FOREIGN KEY (supervising_faculty_code) REFERENCES FACULTY(faculty_code)
);

CREATE TABLE PROFESSOR (
    id_number VARCHAR(15) PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    specialty VARCHAR(80),
    residential_address VARCHAR(120),
    monthly_salary DECIMAL(10, 2),
    gender CHAR(1) CHECK (gender IN ('M', 'F', 'O')),
    birth_date DATE,
    faculty_code VARCHAR(15) NOT NULL,
    FOREIGN KEY (faculty_code) REFERENCES FACULTY(faculty_code)
);

ALTER TABLE FACULTY ADD CONSTRAINT fk_faculty_dean
FOREIGN KEY (dean_id) REFERENCES PROFESSOR(id_number);

CREATE TABLE PROGRAM_PARTICIPATION (
    professor_id VARCHAR(15),
    program_number INT,
    weekly_hours INT NOT NULL DEFAULT 1,
    PRIMARY KEY (professor_id, program_number),
    FOREIGN KEY (professor_id) REFERENCES PROFESSOR(id_number) ON DELETE CASCADE,
    FOREIGN KEY (program_number) REFERENCES EDUCATIONAL_PROGRAM(program_number) ON DELETE CASCADE
);

CREATE TABLE DEPENDENT (
    professor_id VARCHAR(15),
    dependent_name VARCHAR(50),
    gender CHAR(1) CHECK (gender IN ('M', 'F', 'O')),
    birth_date DATE,
    family_relationship VARCHAR(40),
    PRIMARY KEY (professor_id, dependent_name),
    FOREIGN KEY (professor_id) REFERENCES PROFESSOR(id_number) ON DELETE CASCADE
);
"""

    return Scenario(
        id="past_exam_1",
        title="Past Exam 1",
        subtitle="Educational Institution: Faculties, Professors, Educational Programs & Dependents",
        course_tag="DATABASES (Exam 1)",
        paragraphs=paragraphs,
        entities=entities,
        relationship_attributes=relationship_attributes,
        keys_analysis=keys_analysis,
        relationships=relationships,
        assumptions=[
            "Each professor belongs mandatorily to exactly 1 faculty but may teach in educational programs of other faculties.",
            "Faculty direction is assigned to 1 professor with a recorded appointment date.",
            "Dependents form a weak entity with member name as the partial key (discriminator).",
        ],
        er_tables=er_tables,
        er_edges=er_edges,
        relational_justifications=relational_justifications,
        sql_ddl=sql_ddl,
    )
