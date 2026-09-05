"""University Portal case study scenario module.

Demonstrates modularity with a second complete ER analysis scenario for a
University Management Information System (Courses, Students, Professors, Departments).
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


def createUniversityPortalScenario() -> Scenario:
    """Constructs and returns the University Management database scenario.

    Returns:
        Scenario: Fully populated scenario instance.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="A university institution is designing an information system to manage "),
                TextSegment(
                    text="students",
                    is_highlight=True,
                    category="entity",
                    tag_label="ENTITY",
                    badge_class="badge-entity-strong",
                    tooltip="Strong Entity: Natural person with a unique Student Registration Number (AM).",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="professors",
                    is_highlight=True,
                    category="entity",
                    tag_label="ENTITY",
                    badge_class="badge-entity-strong",
                    tooltip="Strong Entity: Teaching academic staff with a unique Tax ID (AFM).",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="departments",
                    is_highlight=True,
                    category="entity",
                    tag_label="ENTITY",
                    badge_class="badge-entity-strong",
                    tooltip="Strong Entity: Academic unit with a unique department code.",
                ),
                TextSegment(text=" and the "),
                TextSegment(
                    text="courses",
                    is_highlight=True,
                    category="entity",
                    tag_label="ENTITY",
                    badge_class="badge-entity-strong",
                    tooltip="Strong Entity: Instructional course subject with a unique course code.",
                ),
                TextSegment(text=" offered."),
            ],
            accent_border_color=None,
        ),
        Paragraph(
            segments=[
                TextSegment(text="Each <strong>department</strong> is identified by a "),
                TextSegment(
                    text="unique department code",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Primary Key: Department Code.",
                ),
                TextSegment(text=", a "),
                TextSegment(
                    text="department name",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Candidate Key: Unique academic department name.",
                ),
                TextSegment(text=" and has a professor serving as "),
                TextSegment(
                    text="department chair",
                    is_highlight=True,
                    category="rel",
                    tag_label="RELATIONSHIP 1:1",
                    badge_class="badge-rel",
                    tooltip="1:1 Relationship (Department - Professor): Each department mandatorily has 1 chair (total), a professor can chair at most 1 department (partial).",
                ),
                TextSegment(text=" with a record of the "),
                TextSegment(
                    text="appointment start date",
                    is_highlight=True,
                    category="attr",
                    tag_label="REL ATTRIBUTE",
                    badge_class="badge-attr-simple",
                    tooltip="Relationship Attribute: Date of taking chair office.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-blue-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Each professor has a "),
                TextSegment(
                    text="Tax ID (AFM)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Primary Key: Professor Tax ID (AFM).",
                ),
                TextSegment(text=", "),
                TextSegment(text="full name", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="academic rank", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=" and "),
                TextSegment(
                    text="belongs to",
                    is_highlight=True,
                    category="rel",
                    tag_label="RELATIONSHIP 1:N",
                    badge_class="badge-rel",
                    tooltip="1:N Relationship (Department -> Professor): Each professor belongs to 1 department.",
                ),
                TextSegment(text=" a specific department. In addition, the professor "),
                TextSegment(
                    text="teaches",
                    is_highlight=True,
                    category="rel",
                    tag_label="RELATIONSHIP 1:N",
                    badge_class="badge-rel",
                    tooltip="1:N Relationship (Professor -> Course): A professor teaches multiple courses.",
                ),
                TextSegment(text=" one or more courses."),
            ],
            accent_border_color="border-emerald-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Each course has a "),
                TextSegment(
                    text="course code",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Primary Key: Course Code.",
                ),
                TextSegment(text=", "),
                TextSegment(text="title", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="ECTS credits", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=" and is "),
                TextSegment(
                    text="offered",
                    is_highlight=True,
                    category="rel",
                    tag_label="RELATIONSHIP 1:N",
                    badge_class="badge-rel",
                    tooltip="1:N Relationship (Department -> Course): Each course is offered by 1 department.",
                ),
                TextSegment(text=" by a department. Students "),
                TextSegment(
                    text="enroll",
                    is_highlight=True,
                    category="rel",
                    tag_label="RELATIONSHIP N:M",
                    badge_class="badge-rel",
                    tooltip="N:M Relationship between Student & Course (Many students take many courses).",
                ),
                TextSegment(text=" in courses, recording the "),
                TextSegment(
                    text="final grade",
                    is_highlight=True,
                    category="attr",
                    tag_label="REL ATTRIBUTE",
                    badge_class="badge-attr-simple",
                    tooltip="Relationship Attribute: Student grade in the course.",
                ),
                TextSegment(text=" and the "),
                TextSegment(
                    text="academic semester",
                    is_highlight=True,
                    category="attr",
                    tag_label="REL ATTRIBUTE",
                    badge_class="badge-attr-simple",
                    tooltip="Relationship Attribute: Semester of enrollment.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-amber-500",
        ),
    ]

    entities = [
        Entity(
            name="DEPARTMENT",
            entity_type="Strong Entity",
            is_weak=False,
            justification="Autonomous administrative and academic unit with Department_ID as primary key.",
            attributes=[
                Attribute(name="Department_ID", attr_type="Simple, Single-valued, Primary Key", is_pk=True),
                Attribute(name="Department_Name", attr_type="Simple, Single-valued, Candidate Key", is_candidate=True),
            ],
        ),
        Entity(
            name="PROFESSOR",
            entity_type="Strong Entity",
            is_weak=False,
            justification="Natural person teaching staff with Tax_ID as unique identifier.",
            attributes=[
                Attribute(name="Tax_ID", attr_type="Simple, Single-valued, Primary Key", is_pk=True),
                Attribute(name="Full_Name", attr_type="Simple, Single-valued"),
                Attribute(name="Academic_Rank", attr_type="Simple, Single-valued"),
            ],
        ),
        Entity(
            name="COURSE",
            entity_type="Strong Entity",
            is_weak=False,
            justification="Autonomous instructional subject with Course_ID as unique identifier.",
            attributes=[
                Attribute(name="Course_ID", attr_type="Simple, Single-valued, Primary Key", is_pk=True),
                Attribute(name="Title", attr_type="Simple, Single-valued"),
                Attribute(name="ECTS", attr_type="Simple, Single-valued"),
            ],
        ),
        Entity(
            name="STUDENT",
            entity_type="Strong Entity",
            is_weak=False,
            justification="Natural person enrolled student with Student_ID as unique identifier.",
            attributes=[
                Attribute(name="Student_ID", attr_type="Simple, Single-valued, Primary Key", is_pk=True),
                Attribute(name="Full_Name", attr_type="Simple, Single-valued"),
                Attribute(name="Enrollment_Year", attr_type="Simple, Single-valued"),
            ],
        ),
    ]

    relationship_attributes = [
        RelationshipAttribute(
            name="Appointment_Start_Date",
            relationship_name="CHAIR (1:1)",
            justification="Records when the professor assumed the chairmanship of the department.",
        ),
        RelationshipAttribute(
            name="Final_Grade",
            relationship_name="ENROLLMENT / ATTENDANCE (N:M)",
            justification="Depends on both the specific student and the specific course.",
        ),
        RelationshipAttribute(
            name="Academic_Semester",
            relationship_name="ENROLLMENT / ATTENDANCE (N:M)",
            justification="Specifies the academic examination/attendance semester.",
        ),
    ]

    keys_analysis = [
        KeyAnalysisRow(
            entity_name="DEPARTMENT",
            key_count="2",
            key_types="Candidate: {Department_ID}, {Department_Name}",
            final_pk_selection="Department_ID",
            justification="Short artificial code.",
        ),
        KeyAnalysisRow(
            entity_name="PROFESSOR",
            key_count="1",
            key_types="Candidate: {Tax_ID}",
            final_pk_selection="Tax_ID",
            justification="National unique tax identification number.",
        ),
        KeyAnalysisRow(
            entity_name="COURSE",
            key_count="1",
            key_types="Candidate: {Course_ID}",
            final_pk_selection="Course_ID",
            justification="Stable curriculum course code.",
        ),
        KeyAnalysisRow(
            entity_name="STUDENT",
            key_count="1",
            key_types="Candidate: {Student_ID}",
            final_pk_selection="Student_ID",
            justification="Unique university student registration number.",
        ),
    ]

    relationships = [
        Relationship(
            letter_id="a",
            name="CHAIR",
            connected_entities="Department <-> Professor",
            cardinality="1:1",
            participation="Total for Department, Partial for Professor",
            relationship_type="Regular Relationship",
            attributes=["Appointment_Start_Date"],
            justification="Each department has 1 chair, each professor chairs at most 1 department.",
        ),
        Relationship(
            letter_id="b",
            name="BELONGS_TO",
            connected_entities="Professor <-> Department",
            cardinality="1:N",
            participation="Total for Professor, Partial for Department",
            relationship_type="Regular Relationship",
            attributes=[],
            justification="Each professor belongs to 1 department, a department employs multiple professors.",
        ),
        Relationship(
            letter_id="c",
            name="OFFERS",
            connected_entities="Department <-> Course",
            cardinality="1:N",
            participation="Total for Course, Partial for Department",
            relationship_type="Regular Relationship",
            attributes=[],
            justification="Each course belongs to the curriculum of 1 department.",
        ),
        Relationship(
            letter_id="d",
            name="TEACHES",
            connected_entities="Professor <-> Course",
            cardinality="1:N",
            participation="Partial for Professor, Total for Course",
            relationship_type="Regular Relationship",
            attributes=[],
            justification="A professor teaches multiple courses, each course has 1 responsible instructor.",
        ),
        Relationship(
            letter_id="e",
            name="ENROLLMENT / ATTENDANCE",
            connected_entities="Student <-> Course",
            cardinality="N:M",
            participation="Partial for both sides",
            relationship_type="Regular Relationship (Junction)",
            attributes=["Final_Grade", "Academic_Semester"],
            justification="Multiple students enroll in multiple courses.",
        ),
    ]

    assumptions = [
        "Each course is taught by a single primary responsible professor (1:N ratio).",
        "A student can enroll in multiple courses per semester (N:M ratio).",
        "The department chair is mandatorily a faculty member of the same department.",
    ]

    er_tables = [
        ERTable(
            id="dept",
            label="DEPARTMENT",
            x=50,
            y=150,
            attrs=[
                ERTableAttr(name="Department_ID", pk=True),
                ERTableAttr(name="Department_Name"),
                ERTableAttr(name="Chair_Tax_ID", fk=True),
                ERTableAttr(name="Appointment_Start_Date"),
            ],
        ),
        ERTable(
            id="prof",
            label="PROFESSOR",
            x=450,
            y=80,
            attrs=[
                ERTableAttr(name="Tax_ID", pk=True),
                ERTableAttr(name="Full_Name"),
                ERTableAttr(name="Academic_Rank"),
                ERTableAttr(name="Department_ID", fk=True),
            ],
        ),
        ERTable(
            id="course",
            label="COURSE",
            x=850,
            y=150,
            attrs=[
                ERTableAttr(name="Course_ID", pk=True),
                ERTableAttr(name="Title"),
                ERTableAttr(name="ECTS"),
                ERTableAttr(name="Department_ID", fk=True),
                ERTableAttr(name="Instructor_Tax_ID", fk=True),
            ],
        ),
        ERTable(
            id="student",
            label="STUDENT",
            x=450,
            y=450,
            attrs=[
                ERTableAttr(name="Student_ID", pk=True),
                ERTableAttr(name="Full_Name"),
                ERTableAttr(name="Enrollment_Year"),
            ],
        ),
        ERTable(
            id="enrollment",
            label="COURSE_ENROLLMENT",
            x=850,
            y=450,
            attrs=[
                ERTableAttr(name="Student_ID", pk=True, fk=True),
                ERTableAttr(name="Course_ID", pk=True, fk=True),
                ERTableAttr(name="Final_Grade"),
                ERTableAttr(name="Academic_Semester"),
            ],
        ),
    ]

    er_edges = [
        EREdge(
            path="M 310,180 L 450,140",
            marker_start="start-one-mandatory",
            marker_end="end-one-optional",
            label="Chair (1:1)",
            lx=380,
            ly=150,
        ),
        EREdge(
            path="M 310,220 L 450,220",
            marker_start="start-one-mandatory",
            marker_end="end-many-mandatory",
            label="Belongs To (1:N)",
            lx=380,
            ly=230,
        ),
        EREdge(
            path="M 180,290 L 180,380 L 980,380 L 980,290",
            marker_start="start-one-mandatory",
            marker_end="end-many-mandatory",
            label="Offers (1:N)",
            lx=580,
            ly=380,
        ),
        EREdge(
            path="M 710,150 L 850,190",
            marker_start="start-one-mandatory",
            marker_end="end-many-mandatory",
            label="Teaches (1:N)",
            lx=780,
            ly=160,
        ),
        EREdge(
            path="M 710,480 L 850,480",
            marker_start="start-one-optional",
            marker_end="end-many-mandatory",
            label="Enrolls (1:N)",
            lx=780,
            ly=470,
        ),
        EREdge(
            path="M 980,290 L 980,450",
            marker_start="start-one-optional",
            marker_end="end-many-mandatory",
            label="Pertains To (1:N)",
            lx=980,
            ly=370,
        ),
    ]

    relational_justifications = [
        RelationalJustification(
            title="1. N:M Enrollment Relationship:",
            color_class="text-purple-400",
            description="The ENROLLMENT relationship was decomposed into the junction table COURSE_ENROLLMENT with a composite PK.",
        ),
        RelationalJustification(
            title="2. 1:1 Chair Relationship:",
            color_class="text-blue-400",
            description="The foreign key Chair_Tax_ID was placed in DEPARTMENT alongside the appointment start date.",
        ),
    ]

    sql_ddl = """-- SQL DDL Schema: University Portal Database
CREATE TABLE DEPARTMENT (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL UNIQUE,
    chair_tax_id VARCHAR(15) NOT NULL UNIQUE,
    appointment_start_date DATE NOT NULL
);

CREATE TABLE PROFESSOR (
    tax_id VARCHAR(15) PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    academic_rank VARCHAR(50) NOT NULL,
    department_id INT NOT NULL,
    FOREIGN KEY (department_id) REFERENCES DEPARTMENT(department_id)
);

ALTER TABLE DEPARTMENT ADD CONSTRAINT fk_department_chair
    FOREIGN KEY (chair_tax_id) REFERENCES PROFESSOR(tax_id);

CREATE TABLE COURSE (
    course_id VARCHAR(20) PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    ects INT NOT NULL,
    department_id INT NOT NULL,
    instructor_tax_id VARCHAR(15) NOT NULL,
    FOREIGN KEY (department_id) REFERENCES DEPARTMENT(department_id),
    FOREIGN KEY (instructor_tax_id) REFERENCES PROFESSOR(tax_id)
);

CREATE TABLE STUDENT (
    student_id VARCHAR(20) PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    enrollment_year INT NOT NULL
);

CREATE TABLE COURSE_ENROLLMENT (
    student_id VARCHAR(20) NOT NULL,
    course_id VARCHAR(20) NOT NULL,
    final_grade DECIMAL(4, 2),
    academic_semester VARCHAR(20) NOT NULL,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES STUDENT(student_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES COURSE(course_id) ON DELETE CASCADE
);"""

    return Scenario(
        id="university_portal",
        title="University Management System",
        subtitle="Entity-Relationship Modeling for Departments, Professors, Courses & Student Enrollments",
        course_tag="Databases (Course 404)",
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
