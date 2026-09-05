"""Hospital Management case study scenario module.

Contains the complete parsed and modeled ER analysis for the University Hospital
Management Information System (Clinics, Doctors, Dependents, Patients, Admissions, Medications),
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


def createHospitalManagementScenario() -> Scenario:
    """Constructs and returns the Hospital Management database scenario.

    Returns:
        Scenario: Fully populated scenario instance.
    """
    # 1. Text Paragraphs with Interactive Segments
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="A large university hospital is designing a new database management system for comprehensive operational tracking, including "),
                TextSegment(
                    text="clinics",
                    is_highlight=True,
                    category="entity",
                    tag_label="ENTITY",
                    badge_class="badge-entity-strong",
                    tooltip="Strong Entity: Autonomous medical clinic unit with a unique clinic code.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="medical staff",
                    is_highlight=True,
                    category="entity",
                    tag_label="ENTITY",
                    badge_class="badge-entity-strong",
                    tooltip="Strong Entity: Natural person physician with unique Medical License Number (AMI) and Tax ID (AFM).",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="patients",
                    is_highlight=True,
                    category="entity",
                    tag_label="ENTITY",
                    badge_class="badge-entity-strong",
                    tooltip="Strong Entity: Natural person patient with unique Social Security Number (AMKA).",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="admissions / hospitalizations",
                    is_highlight=True,
                    category="entity",
                    tag_label="WEAK ENTITY",
                    badge_class="badge-entity-weak",
                    tooltip="Weak Entity: Hospitalization incident existentially dependent on the patient.",
                ),
                TextSegment(text=" and administered medical treatments."),
            ],
            accent_border_color=None,
        ),
        Paragraph(
            segments=[
                TextSegment(text="1. <strong>Clinics:</strong> Each clinic is characterized by a "),
                TextSegment(
                    text="unique clinic code (e.g., K01, K02)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Primary Key: Unique artificial clinic code.",
                ),
                TextSegment(text=", a "),
                TextSegment(
                    text="unique name (e.g., 'Cardiology', 'Neurology')",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Candidate Key: Alternative unique identifying clinic name.",
                ),
                TextSegment(text=", the "),
                TextSegment(text="floor", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=" on which it is housed and the "),
                TextSegment(text="administrative office telephone number", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=". Each clinic is "),
                TextSegment(
                    text="directed",
                    is_highlight=True,
                    category="rel",
                    tag_label="RELATIONSHIP 1:1",
                    badge_class="badge-rel",
                    tooltip="1:1 Relationship (Clinic - Physician): Total participation for clinic, partial participation for physician.",
                ),
                TextSegment(text=" mandatorily by a specific physician (Clinic Director), for whom the "),
                TextSegment(
                    text="date of taking office",
                    is_highlight=True,
                    category="attr",
                    tag_label="REL ATTRIBUTE",
                    badge_class="badge-attr-simple",
                    tooltip="Relationship Attribute: Date of taking office as director for the specific clinic.",
                ),
                TextSegment(text=". A physician can direct at most one clinic. Additionally, each clinic may have "),
                TextSegment(
                    text="specialized wings/facilities located in various buildings across the hospital complex (multiple locations)",
                    is_highlight=True,
                    category="attr",
                    tag_label="MULTIVALUED",
                    badge_class="badge-attr-multi",
                    tooltip="Multivalued Attribute: A clinic may span multiple wings across different buildings.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-blue-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="2. <strong>Medical Staff (Doctors):</strong> For each physician, the following data are recorded: "),
                TextSegment(
                    text="unique medical license number (AMI)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Primary Key: Unique professional medical license number.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="Tax Identification Number (AFM)",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Candidate Key: National unique tax identification number.",
                ),
                TextSegment(text=", "),
                TextSegment(text="first name", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="last name", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="specialty", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text="rank/title (e.g., Attending Physician A', Attending Physician B', Department Chair)", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="monthly base salary", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="hiring date", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=" and "),
                TextSegment(
                    text="residential address (composed of street, number, postal code, and city)",
                    is_highlight=True,
                    category="attr",
                    tag_label="COMPOSITE",
                    badge_class="badge-attr-composite",
                    tooltip="Composite Attribute: Decomposed into Street, Number, Postal Code, and City.",
                ),
                TextSegment(text=". A physician may have "),
                TextSegment(
                    text="more than one contact telephone number (e.g., internal extension, mobile)",
                    is_highlight=True,
                    category="attr",
                    tag_label="MULTIVALUED",
                    badge_class="badge-attr-multi",
                    tooltip="Multivalued Attribute: A physician may have multiple contact phone numbers.",
                ),
                TextSegment(text=". Each physician "),
                TextSegment(
                    text="belongs mandatorily to exactly one clinic",
                    is_highlight=True,
                    category="rel",
                    tag_label="RELATIONSHIP 1:N",
                    badge_class="badge-rel",
                    tooltip="1:N Relationship (Clinic -> Physician): Total participation for physician, a clinic employs multiple physicians.",
                ),
                TextSegment(text=", while multiple physicians serve in each clinic. Furthermore, an experienced physician may "),
                TextSegment(
                    text="supervise and guide",
                    is_highlight=True,
                    category="rel",
                    tag_label="RELATIONSHIP 1:N",
                    badge_class="badge-rel",
                    tooltip="Recursive 1:N Relationship (Supervisor Physician -> Resident Physician): Each resident has 1 direct supervisor.",
                ),
                TextSegment(text=" junior resident physicians (each resident has one direct supervisor physician, whereas a supervisor may guide multiple residents)."),
            ],
            accent_border_color="border-emerald-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="3. <strong>Dependents:</strong> For insurance and tax purposes, the institution records the "),
                TextSegment(
                    text="dependent family members",
                    is_highlight=True,
                    category="entity",
                    tag_label="WEAK ENTITY",
                    badge_class="badge-entity-weak",
                    tooltip="Weak Entity: Existentially dependent on Physician with no autonomous PK.",
                ),
                TextSegment(text=" of physicians. For each dependent member, the following are kept: "),
                TextSegment(
                    text="first name",
                    is_highlight=True,
                    category="key",
                    tag_label="PARTIAL KEY",
                    badge_class="badge-key-partial",
                    tooltip="Partial Key (Discriminator): Unique only within the physician's family context.",
                ),
                TextSegment(text=", "),
                TextSegment(text="gender", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="date of birth", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=" and "),
                TextSegment(text="family relationship (e.g., child, spouse)", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=". The name of the dependent is unique only within the context of the family of the specific physician."),
            ],
            accent_border_color="border-purple-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="4. <strong>Patients:</strong> For each patient, the following are recorded: the "),
                TextSegment(
                    text="unique Social Security Number (AMKA)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Primary Key: Unique national social security number.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="National ID Number (ADT)",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Candidate Key: National police identification card number.",
                ),
                TextSegment(text=", "),
                TextSegment(text="first name", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="last name", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="date of birth", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="gender", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="blood type", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=" and the "),
                TextSegment(
                    text="current age (which is calculated dynamically from the date of birth)",
                    is_highlight=True,
                    category="attr",
                    tag_label="DERIVED",
                    badge_class="badge-attr-derived",
                    tooltip="Derived Attribute: Computed dynamically from current date and date of birth.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-amber-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="5. <strong>Admissions / Hospitalizations:</strong> Each time a patient is admitted to the hospital, a new hospitalization incident is recorded. For each hospitalization, the following are recorded: a "),
                TextSegment(
                    text="sequential admission number for the specific patient",
                    is_highlight=True,
                    category="key",
                    tag_label="PARTIAL KEY",
                    badge_class="badge-key-partial",
                    tooltip="Partial Key: Sequentially numbers admissions for the same patient (1, 2, 3...).",
                ),
                TextSegment(text=", the "),
                TextSegment(text="admission date and time", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="discharge date and time (if completed)", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="room number", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="initial diagnosis", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=" and the "),
                TextSegment(
                    text="clinic in which the hospitalization takes place",
                    is_highlight=True,
                    category="rel",
                    tag_label="RELATIONSHIP 1:N",
                    badge_class="badge-rel",
                    tooltip="1:N Relationship (Clinic -> Hospitalization): Each hospitalization is hosted in 1 clinic.",
                ),
                TextSegment(text=". A patient may have multiple hospitalizations over time, but each hospitalization "),
                TextSegment(
                    text="pertains exclusively to one patient",
                    is_highlight=True,
                    category="rel",
                    tag_label="IDENTIFYING 1:N",
                    badge_class="badge-rel",
                    tooltip="Identifying 1:N Relationship (Patient -> Hospitalization): Total existential dependency on patient.",
                ),
                TextSegment(text=" and is conducted within a single clinic."),
            ],
            accent_border_color="border-cyan-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="6. <strong>Treatments & Medications:</strong> The hospital maintains a formulary catalog of "),
                TextSegment(
                    text="medications",
                    is_highlight=True,
                    category="entity",
                    tag_label="ENTITY",
                    badge_class="badge-entity-strong",
                    tooltip="Strong Entity: Pharmaceutical drug product with unique national EOF code.",
                ),
                TextSegment(text=". Each drug has a "),
                TextSegment(
                    text="unique national medication code (EOF)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Primary Key: Unique National Organization for Medicines code.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="commercial trade name",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Candidate Key: Unique commercial brand name.",
                ),
                TextSegment(text=", "),
                TextSegment(text="active pharmaceutical ingredient", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=" and "),
                TextSegment(text="unit of measurement (e.g., mg, ml)", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=". During a hospitalization, an attending physician "),
                TextSegment(
                    text="prescribes and administers medications",
                    is_highlight=True,
                    category="rel",
                    tag_label="RELATIONSHIP N:M",
                    badge_class="badge-rel",
                    tooltip="Associative Entity / N:M Relationship (Hospitalization <-> Medication with attending physician reference).",
                ),
                TextSegment(text=" to the admitted patient. For each drug administration during a specific hospitalization, the following are recorded: "),
                TextSegment(
                    text="dosage",
                    is_highlight=True,
                    category="attr",
                    tag_label="REL ATTRIBUTE",
                    badge_class="badge-attr-simple",
                    tooltip="Relationship Attribute / Junction Table: Administration dosage quantity.",
                ),
                TextSegment(text=", the "),
                TextSegment(
                    text="intake frequency per 24 hours",
                    is_highlight=True,
                    category="attr",
                    tag_label="REL ATTRIBUTE",
                    badge_class="badge-attr-simple",
                    tooltip="Relationship Attribute / Junction Table: Daily intake frequency.",
                ),
                TextSegment(text=", the "),
                TextSegment(
                    text="start date",
                    is_highlight=True,
                    category="attr",
                    tag_label="REL ATTRIBUTE",
                    badge_class="badge-attr-simple",
                    tooltip="Relationship Attribute / Junction Table: Regimen start date.",
                ),
                TextSegment(text=" and the "),
                TextSegment(
                    text="end date of the treatment regimen",
                    is_highlight=True,
                    category="attr",
                    tag_label="REL ATTRIBUTE",
                    badge_class="badge-attr-simple",
                    tooltip="Relationship Attribute / Junction Table: Regimen completion date.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-rose-500",
        ),
    ]

    # 2. Entities & Attributes
    entities = [
        Entity(
            name="CLINIC",
            entity_type="Strong Entity",
            is_weak=False,
            justification="Autonomous administrative and healthcare unit with clinic_code as primary key.",
            attributes=[
                Attribute(name="clinic_code", attr_type="Simple, Single-valued, Primary Key", is_pk=True),
                Attribute(name="clinic_name", attr_type="Simple, Single-valued, Candidate Key", is_candidate=True),
                Attribute(name="floor", attr_type="Simple, Single-valued"),
                Attribute(name="office_phone", attr_type="Simple, Single-valued"),
                Attribute(name="clinic_wings", attr_type="Multivalued", notes="Extracted to separate table CLINIC_WING"),
            ],
        ),
        Entity(
            name="PHYSICIAN",
            entity_type="Strong Entity",
            is_weak=False,
            justification="Natural person medical staff with ami and afm as unique identifiers.",
            attributes=[
                Attribute(name="ami", attr_type="Simple, Single-valued, Primary Key", is_pk=True),
                Attribute(name="afm", attr_type="Simple, Single-valued, Candidate Key", is_candidate=True),
                Attribute(name="first_name", attr_type="Simple, Single-valued"),
                Attribute(name="last_name", attr_type="Simple, Single-valued"),
                Attribute(name="specialty", attr_type="Simple, Single-valued"),
                Attribute(name="rank", attr_type="Simple, Single-valued"),
                Attribute(name="base_salary", attr_type="Simple, Single-valued"),
                Attribute(name="hire_date", attr_type="Simple, Single-valued"),
                Attribute(
                    name="residential_address",
                    attr_type="Composite",
                    components=["street", "number", "postal_code", "city"],
                ),
                Attribute(name="contact_phones", attr_type="Multivalued", notes="Extracted to separate table PHYSICIAN_PHONE"),
            ],
        ),
        Entity(
            name="DEPENDENT",
            entity_type="Weak Entity",
            is_weak=True,
            owner_entity="PHYSICIAN",
            justification="Existentially dependent on Physician. Identified by physician's FK combined with member_name.",
            attributes=[
                Attribute(name="member_name", attr_type="Simple, Partial Key", is_partial=True),
                Attribute(name="gender", attr_type="Simple, Single-valued"),
                Attribute(name="birth_date", attr_type="Simple, Single-valued"),
                Attribute(name="relationship", attr_type="Simple, Single-valued"),
            ],
        ),
        Entity(
            name="PATIENT",
            entity_type="Strong Entity",
            is_weak=False,
            justification="Natural person healthcare recipient with unique national identifier amka.",
            attributes=[
                Attribute(name="amka", attr_type="Simple, Single-valued, Primary Key", is_pk=True),
                Attribute(name="id_card_number", attr_type="Simple, Single-valued, Candidate Key", is_candidate=True),
                Attribute(name="first_name", attr_type="Simple, Single-valued"),
                Attribute(name="last_name", attr_type="Simple, Single-valued"),
                Attribute(name="birth_date", attr_type="Simple, Single-valued"),
                Attribute(name="gender", attr_type="Simple, Single-valued"),
                Attribute(name="blood_type", attr_type="Simple, Single-valued"),
                Attribute(name="age", attr_type="Derived", notes="Calculated dynamically from birth_date"),
            ],
        ),
        Entity(
            name="ADMISSION",
            entity_type="Weak Entity",
            is_weak=True,
            owner_entity="PATIENT",
            justification="Hospital admission incident. Identified by patient's amka and admission_number.",
            attributes=[
                Attribute(name="admission_number", attr_type="Simple, Partial Key", is_partial=True),
                Attribute(name="admission_datetime", attr_type="Simple, Single-valued"),
                Attribute(name="discharge_datetime", attr_type="Simple, Single-valued (Nullable)"),
                Attribute(name="room_number", attr_type="Simple, Single-valued"),
                Attribute(name="initial_diagnosis", attr_type="Simple, Single-valued"),
            ],
        ),
        Entity(
            name="MEDICATION",
            entity_type="Strong Entity",
            is_weak=False,
            justification="Approved therapeutic drug product with unique national EOF code.",
            attributes=[
                Attribute(name="eof_code", attr_type="Simple, Single-valued, Primary Key", is_pk=True),
                Attribute(name="brand_name", attr_type="Simple, Single-valued, Candidate Key", is_candidate=True),
                Attribute(name="active_substance", attr_type="Simple, Single-valued"),
                Attribute(name="unit_of_measurement", attr_type="Simple, Single-valued"),
            ],
        ),
    ]

    # 3. Relationship Attributes
    relationship_attributes = [
        RelationshipAttribute(
            name="appointment_date",
            relationship_name="MANAGES_CLINIC (1:1)",
            justification="Records when the physician officially took office as clinic director.",
        ),
        RelationshipAttribute(
            name="dosage",
            relationship_name="MEDICATION_ADMINISTRATION (N:M)",
            justification="Medication dose quantity per administration for the hospitalization.",
        ),
        RelationshipAttribute(
            name="frequency_24h",
            relationship_name="MEDICATION_ADMINISTRATION (N:M)",
            justification="Number of dosage administrations per day.",
        ),
        RelationshipAttribute(
            name="start_date",
            relationship_name="MEDICATION_ADMINISTRATION (N:M)",
            justification="Start date of the medication regimen.",
        ),
        RelationshipAttribute(
            name="end_date",
            relationship_name="MEDICATION_ADMINISTRATION (N:M)",
            justification="Completion date of the regimen.",
        ),
    ]

    # 4. Keys Analysis Table
    keys_analysis = [
        KeyAnalysisRow(
            entity_name="CLINIC",
            key_count="2",
            key_types="Candidate: {clinic_code}, {clinic_name}",
            final_pk_selection="clinic_code",
            justification="Short artificial fixed-length code.",
        ),
        KeyAnalysisRow(
            entity_name="PHYSICIAN",
            key_count="2",
            key_types="Candidate: {ami}, {afm}",
            final_pk_selection="ami",
            justification="Internal medical registry identifier number.",
        ),
        KeyAnalysisRow(
            entity_name="DEPENDENT",
            key_count="0 (Weak)",
            key_types="Partial Key: {member_name}",
            final_pk_selection="Composite PK: {Physician.ami, member_name}",
            justification="Weak entity with existential dependency on Physician.",
            is_weak=True,
        ),
        KeyAnalysisRow(
            entity_name="PATIENT",
            key_count="2",
            key_types="Candidate: {amka}, {id_card_number}",
            final_pk_selection="amka",
            justification="Unique national social security number for each citizen/patient.",
        ),
        KeyAnalysisRow(
            entity_name="ADMISSION",
            key_count="0 (Weak)",
            key_types="Partial Key: {admission_number}",
            final_pk_selection="Composite PK: {Patient.amka, admission_number}",
            justification="Weak entity dependent on Patient.",
            is_weak=True,
        ),
        KeyAnalysisRow(
            entity_name="MEDICATION",
            key_count="2",
            key_types="Candidate: {eof_code}, {brand_name}",
            final_pk_selection="eof_code",
            justification="Official national regulatory medicine identifier.",
        ),
    ]

    # 5. Relationships
    relationships = [
        Relationship(
            letter_id="a",
            name="MANAGES_CLINIC",
            connected_entities="Clinic <-> Physician",
            cardinality="1:1",
            participation="Total for Clinic, Partial for Physician",
            relationship_type="Regular Relationship",
            attributes=["appointment_date"],
            justification="Each clinic has exactly 1 director physician, each physician directs at most 1 clinic.",
        ),
        Relationship(
            letter_id="b",
            name="SERVES_IN",
            connected_entities="Physician <-> Clinic",
            cardinality="1:N",
            participation="Total for Physician, Partial for Clinic",
            relationship_type="Regular Relationship",
            attributes=[],
            justification="Each physician belongs mandatorily to 1 clinic, each clinic employs multiple physicians.",
        ),
        Relationship(
            letter_id="c",
            name="SUPERVISES",
            connected_entities="Physician (Supervisor) <-> Physician (Resident)",
            cardinality="1:N",
            participation="Partial for Supervisor (0,N), Total for Resident (1,1)",
            relationship_type="Recursive 1:N Relationship",
            attributes=[],
            justification="An experienced physician guides multiple residents, each resident has 1 supervisor.",
        ),
        Relationship(
            letter_id="d",
            name="HAS_DEPENDENT",
            connected_entities="Physician <-> Dependent",
            cardinality="1:N",
            participation="Total for Dependent, Partial for Physician",
            relationship_type="Identifying Relationship",
            attributes=[],
            justification="Connects weak entity Dependent to identifying owner Physician.",
        ),
        Relationship(
            letter_id="e",
            name="PATIENT_ADMISSION",
            connected_entities="Patient <-> Admission",
            cardinality="1:N",
            participation="Total for Admission, Partial for Patient",
            relationship_type="Identifying Relationship",
            attributes=[],
            justification="Each admission pertains exclusively to 1 patient, a patient may have multiple admissions.",
        ),
        Relationship(
            letter_id="f",
            name="HOSTS_ADMISSION",
            connected_entities="Clinic <-> Admission",
            cardinality="1:N",
            participation="Total for Admission, Partial for Clinic",
            relationship_type="Regular Relationship",
            attributes=[],
            justification="Each admission is conducted in 1 clinic, a clinic hosts multiple admissions.",
        ),
        Relationship(
            letter_id="g",
            name="MEDICATION_ADMINISTRATION",
            connected_entities="Admission <-> Medication (with Attending Physician)",
            cardinality="N:M",
            participation="Partial for both sides",
            relationship_type="Associative Entity / Junction",
            attributes=["dosage", "frequency_24h", "start_date", "end_date"],
            justification="Multiple medications are administered in an admission and each drug is administered across multiple admissions.",
        ),
    ]

    # 6. Assumptions
    assumptions = [
        "Residential Address: Decomposed into 4 atomic attributes (street, number, postal code, city) to guarantee 1NF.",
        "Multivalued Attributes: Physician contact phones and clinic wings are implemented as autonomous relational tables.",
        "Medication Administration: Implemented as a junction table with a Foreign Key referencing the attending physician who ordered the treatment.",
        "Admission & Dependents: As weak entities, they feature a composite primary key consisting of the owner PK and their discriminator partial key.",
    ]

    # 7. ER Table Nodes for SVG Crow's Foot Diagram
    er_tables = [
        ERTable(
            id="kliniki",
            label="CLINIC",
            x=50,
            y=80,
            attrs=[
                ERTableAttr(name="clinic_code", pk=True),
                ERTableAttr(name="clinic_name"),
                ERTableAttr(name="floor"),
                ERTableAttr(name="office_phone"),
                ERTableAttr(name="director_ami", fk=True),
                ERTableAttr(name="appointment_date"),
            ],
        ),
        ERTable(
            id="pteriga",
            label="CLINIC_WING",
            x=50,
            y=400,
            attrs=[
                ERTableAttr(name="clinic_code", pk=True, fk=True),
                ERTableAttr(name="wing_location", pk=True),
            ],
        ),
        ERTable(
            id="iatros",
            label="PHYSICIAN",
            x=450,
            y=50,
            attrs=[
                ERTableAttr(name="ami", pk=True),
                ERTableAttr(name="afm"),
                ERTableAttr(name="first_name"),
                ERTableAttr(name="last_name"),
                ERTableAttr(name="specialty"),
                ERTableAttr(name="rank"),
                ERTableAttr(name="base_salary"),
                ERTableAttr(name="hire_date"),
                ERTableAttr(name="street"),
                ERTableAttr(name="street_number"),
                ERTableAttr(name="postal_code"),
                ERTableAttr(name="city"),
                ERTableAttr(name="clinic_code", fk=True),
                ERTableAttr(name="supervisor_ami", fk=True),
            ],
        ),
        ERTable(
            id="tilefono_iatroy",
            label="PHYSICIAN_PHONE",
            x=450,
            y=540,
            attrs=[
                ERTableAttr(name="ami", pk=True, fk=True),
                ERTableAttr(name="phone_number", pk=True),
            ],
        ),
        ERTable(
            id="exartomeno",
            label="DEPENDENT",
            x=450,
            y=680,
            attrs=[
                ERTableAttr(name="physician_ami", pk=True, fk=True),
                ERTableAttr(name="member_name", pk=True),
                ERTableAttr(name="gender"),
                ERTableAttr(name="birth_date"),
                ERTableAttr(name="relationship"),
            ],
        ),
        ERTable(
            id="asthenis",
            label="PATIENT",
            x=850,
            y=50,
            attrs=[
                ERTableAttr(name="amka", pk=True),
                ERTableAttr(name="id_card_number"),
                ERTableAttr(name="first_name"),
                ERTableAttr(name="last_name"),
                ERTableAttr(name="birth_date"),
                ERTableAttr(name="gender"),
                ERTableAttr(name="blood_type"),
            ],
        ),
        ERTable(
            id="nosileia",
            label="ADMISSION",
            x=850,
            y=350,
            attrs=[
                ERTableAttr(name="amka", pk=True, fk=True),
                ERTableAttr(name="admission_number", pk=True),
                ERTableAttr(name="admission_datetime"),
                ERTableAttr(name="discharge_datetime"),
                ERTableAttr(name="room_number"),
                ERTableAttr(name="initial_diagnosis"),
                ERTableAttr(name="clinic_code", fk=True),
            ],
        ),
        ERTable(
            id="farmako",
            label="MEDICATION",
            x=50,
            y=600,
            attrs=[
                ERTableAttr(name="eof_code", pk=True),
                ERTableAttr(name="brand_name"),
                ERTableAttr(name="active_substance"),
                ERTableAttr(name="unit_of_measurement"),
            ],
        ),
        ERTable(
            id="chorigisi",
            label="MEDICATION_ADMINISTRATION",
            x=850,
            y=640,
            attrs=[
                ERTableAttr(name="amka", pk=True, fk=True),
                ERTableAttr(name="admission_number", pk=True, fk=True),
                ERTableAttr(name="eof_code", pk=True, fk=True),
                ERTableAttr(name="attending_ami", fk=True),
                ERTableAttr(name="dosage"),
                ERTableAttr(name="frequency_24h"),
                ERTableAttr(name="start_date"),
                ERTableAttr(name="end_date"),
            ],
        ),
    ]

    # 8. ER Diagram Edges
    er_edges = [
        EREdge(
            path="M 310,120 L 450,120",
            marker_start="start-one-mandatory",
            marker_end="end-one-optional",
            label="Manages (1:1)",
            lx=380,
            ly=110,
        ),
        # Doctor recursive supervisor (1:N)
        EREdge(
            path="M 710,90 C 770,30 770,170 710,150",
            marker_start="start-one-optional",
            marker_end="end-many-optional",
            label="Supervises (1:N)",
            lx=780,
            ly=100,
        ),
        EREdge(
            path="M 310,200 L 450,200",
            marker_start="start-one-mandatory",
            marker_end="end-many-mandatory",
            label="Serves In (1:N)",
            lx=380,
            ly=190,
        ),
        EREdge(
            path="M 180,240 L 180,400",
            marker_start="start-one-mandatory",
            marker_end="end-many-mandatory",
            label="Wings (1:N)",
            lx=180,
            ly=320,
        ),
        EREdge(
            path="M 580,490 L 580,540",
            marker_start="start-one-mandatory",
            marker_end="end-many-mandatory",
            label="Phones (1:N)",
            lx=580,
            ly=515,
        ),
        EREdge(
            path="M 710,350 L 750,350 L 750,720 L 710,720",
            marker_start="start-one-optional",
            marker_end="end-many-mandatory",
            label="Dependents (1:N)",
            lx=760,
            ly=535,
        ),
        EREdge(
            path="M 980,294 L 980,350",
            marker_start="start-one-optional",
            marker_end="end-many-mandatory",
            label="Admission (1:N)",
            lx=980,
            ly=322,
        ),
        EREdge(
            path="M 310,240 L 310,360 L 850,360",
            marker_start="start-one-mandatory",
            marker_end="end-many-mandatory",
            label="Hosts (1:N)",
            lx=580,
            ly=360,
        ),
        EREdge(
            path="M 980,594 L 980,640",
            marker_start="start-one-mandatory",
            marker_end="end-many-optional",
            label="Administration (1:N)",
            lx=980,
            ly=617,
        ),
        EREdge(
            path="M 310,680 L 850,680",
            marker_start="start-one-mandatory",
            marker_end="end-many-optional",
            label="Medication (1:N)",
            lx=580,
            ly=670,
        ),
    ]

    # 9. Relational Justifications
    relational_justifications = [
        RelationalJustification(
            title="1. 1:1 Clinic Management Relationship:",
            color_class="text-blue-400",
            description="CLINIC has total participation in the management relationship. Foreign key director_ami is placed in table CLINIC alongside appointment_date.",
        ),
        RelationalJustification(
            title="2. Weak Entities (Dependents & Admissions):",
            color_class="text-purple-400",
            description="DEPENDENT and ADMISSION are converted into tables with composite primary keys {physician_ami, member_name} and {amka, admission_number} respectively, with ON DELETE CASCADE.",
        ),
        RelationalJustification(
            title="3. Multivalued Attributes (1NF):",
            color_class="text-amber-400",
            description="Clinic wings and physician phones are decomposed into independent tables CLINIC_WING and PHYSICIAN_PHONE.",
        ),
        RelationalJustification(
            title="4. Associative Entity for Medication Administration:",
            color_class="text-emerald-400",
            description="The MEDICATION_ADMINISTRATION relationship is implemented as a junction table with composite PK {amka, admission_number, eof_code} and an FK referencing the attending physician.",
        ),
    ]

    # 10. SQL DDL Script
    sql_ddl = """-- SQL DDL Schema: Hospital Management Database
-- 1. Entity: CLINIC
CREATE TABLE CLINIC (
    clinic_code VARCHAR(10) PRIMARY KEY,
    clinic_name VARCHAR(100) NOT NULL UNIQUE,
    floor INT NOT NULL,
    office_phone VARCHAR(20) NOT NULL,
    director_ami VARCHAR(15) NOT NULL UNIQUE,
    appointment_date DATE NOT NULL
);

-- 2. Multivalued Attribute: CLINIC_WING
CREATE TABLE CLINIC_WING (
    clinic_code VARCHAR(10) NOT NULL,
    wing_location VARCHAR(100) NOT NULL,
    PRIMARY KEY (clinic_code, wing_location),
    FOREIGN KEY (clinic_code) REFERENCES CLINIC(clinic_code) ON DELETE CASCADE
);

-- 3. Entity: PHYSICIAN
CREATE TABLE PHYSICIAN (
    ami VARCHAR(15) PRIMARY KEY,
    afm VARCHAR(10) NOT NULL UNIQUE,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    specialty VARCHAR(50) NOT NULL,
    rank VARCHAR(50) NOT NULL,
    base_salary DECIMAL(10, 2) NOT NULL,
    hire_date DATE NOT NULL,
    street VARCHAR(100) NOT NULL,
    street_number VARCHAR(10) NOT NULL,
    postal_code VARCHAR(10) NOT NULL,
    city VARCHAR(50) NOT NULL,
    clinic_code VARCHAR(10) NOT NULL,
    supervisor_ami VARCHAR(15),
    FOREIGN KEY (clinic_code) REFERENCES CLINIC(clinic_code),
    FOREIGN KEY (supervisor_ami) REFERENCES PHYSICIAN(ami)
);

-- Add Circular Foreign Key for Clinic Director
ALTER TABLE CLINIC ADD CONSTRAINT fk_clinic_director
    FOREIGN KEY (director_ami) REFERENCES PHYSICIAN(ami);

-- 4. Multivalued Attribute: PHYSICIAN_PHONE
CREATE TABLE PHYSICIAN_PHONE (
    ami VARCHAR(15) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    PRIMARY KEY (ami, phone_number),
    FOREIGN KEY (ami) REFERENCES PHYSICIAN(ami) ON DELETE CASCADE
);

-- 5. Weak Entity: DEPENDENT
CREATE TABLE DEPENDENT (
    physician_ami VARCHAR(15) NOT NULL,
    member_name VARCHAR(50) NOT NULL,
    gender CHAR(1) CHECK (gender IN ('M', 'F', 'O')),
    birth_date DATE NOT NULL,
    relationship VARCHAR(30) NOT NULL,
    PRIMARY KEY (physician_ami, member_name),
    FOREIGN KEY (physician_ami) REFERENCES PHYSICIAN(ami) ON DELETE CASCADE
);

-- 6. Entity: PATIENT
CREATE TABLE PATIENT (
    amka VARCHAR(15) PRIMARY KEY,
    id_card_number VARCHAR(15) NOT NULL UNIQUE,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    birth_date DATE NOT NULL,
    gender CHAR(1) CHECK (gender IN ('M', 'F', 'O')),
    blood_type VARCHAR(5) NOT NULL
);

-- 7. Weak Entity: ADMISSION
CREATE TABLE ADMISSION (
    amka VARCHAR(15) NOT NULL,
    admission_number INT NOT NULL,
    admission_datetime TIMESTAMP NOT NULL,
    discharge_datetime TIMESTAMP,
    room_number VARCHAR(10) NOT NULL,
    initial_diagnosis TEXT NOT NULL,
    clinic_code VARCHAR(10) NOT NULL,
    PRIMARY KEY (amka, admission_number),
    FOREIGN KEY (amka) REFERENCES PATIENT(amka) ON DELETE CASCADE,
    FOREIGN KEY (clinic_code) REFERENCES CLINIC(clinic_code)
);

-- 8. Entity: MEDICATION
CREATE TABLE MEDICATION (
    eof_code VARCHAR(20) PRIMARY KEY,
    brand_name VARCHAR(100) NOT NULL UNIQUE,
    active_substance VARCHAR(100) NOT NULL,
    unit_of_measurement VARCHAR(20) NOT NULL
);

-- 9. Relationship / Junction Table: MEDICATION_ADMINISTRATION
CREATE TABLE MEDICATION_ADMINISTRATION (
    amka VARCHAR(15) NOT NULL,
    admission_number INT NOT NULL,
    eof_code VARCHAR(20) NOT NULL,
    attending_ami VARCHAR(15) NOT NULL,
    dosage VARCHAR(50) NOT NULL,
    frequency_24h INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    PRIMARY KEY (amka, admission_number, eof_code),
    FOREIGN KEY (amka, admission_number) REFERENCES ADMISSION(amka, admission_number) ON DELETE CASCADE,
    FOREIGN KEY (eof_code) REFERENCES MEDICATION(eof_code),
    FOREIGN KEY (attending_ami) REFERENCES PHYSICIAN(ami)
);"""

    return Scenario(
        id="hospital_management",
        title="Hospital Management System",
        subtitle="Entity-Relationship Modeling for Clinics, Physicians, Patients, Admissions & Treatments",
        course_tag="Databases (Progress Test 2025-2026 - Topic 1)",
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
