"""Maritime Shipping and Fleet Management case study scenario module.

Contains the complete parsed and modeled ER analysis for the International Maritime
Shipping Company (Vessels, Ports, Voyages, Seafarers, Embarkation Contracts, Statutory Inspections),
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


def createMaritimeShippingScenario() -> Scenario:
    """Constructs and returns the Maritime Fleet Management database scenario.

    Returns:
        Scenario: Fully populated scenario instance.
    """
    # 1. Text Paragraphs with Interactive Segments
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="An international commercial shipping company managing cargo vessels (ocean-going bulk carriers and tankers) decided to replace its disparate file systems with a centralized Database Management System (DBMS) to efficiently manage its "),
                TextSegment(
                    text="fleet (vessels)",
                    is_highlight=True,
                    category="entity",
                    tag_label="ENTITY",
                    badge_class="badge-entity-strong",
                    tooltip="Strong Entity: Ocean-going vessel with unique IMO number and Call Sign.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="ports of call",
                    is_highlight=True,
                    category="entity",
                    tag_label="ENTITY",
                    badge_class="badge-entity-strong",
                    tooltip="Strong Entity: Port with unique UN/LOCODE.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="voyages / commercial routes",
                    is_highlight=True,
                    category="entity",
                    tag_label="ENTITY",
                    badge_class="badge-entity-strong",
                    tooltip="Strong Entity: Commercial voyage with unique Voyage Code.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="crew embarkations",
                    is_highlight=True,
                    category="entity",
                    tag_label="ASSOCIATIVE",
                    badge_class="badge-entity-strong",
                    tooltip="Associative Entity: Employment contract for a seafarer on a vessel.",
                ),
                TextSegment(text=" and "),
                TextSegment(
                    text="periodic safety inspections",
                    is_highlight=True,
                    category="entity",
                    tag_label="WEAK ENTITY",
                    badge_class="badge-entity-weak",
                    tooltip="Weak Entity: Seaworthiness inspection existentially dependent on the vessel.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color=None,
        ),
        Paragraph(
            segments=[
                TextSegment(text="1. <strong>Fleet Vessels:</strong> For each vessel, the following are recorded: the "),
                TextSegment(
                    text="unique international 7-digit IMO number (International Maritime Organization number)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Primary Key: Unique global IMO vessel identification number.",
                ),
                TextSegment(text=", the "),
                TextSegment(text="vessel name", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(
                    text="call sign (also unique)",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Candidate Key: Unique international maritime radiotelephony call sign.",
                ),
                TextSegment(text=", the "),
                TextSegment(text="build year", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="flag (country of registry)", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="deadweight tonnage (DWT)", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=" and the "),
                TextSegment(text="vessel type (e.g., 'Bulk Carrier', 'Crude Oil Tanker')", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=". Each vessel "),
                TextSegment(
                    text="mandatorily has one unique Captain / Master",
                    is_highlight=True,
                    category="rel",
                    tag_label="RELATIONSHIP 1:1",
                    badge_class="badge-rel",
                    tooltip="1:1 Relationship (Vessel - Seafarer/Captain): Total participation for vessel, partial participation for seafarer.",
                ),
                TextSegment(text=" who holds overall command of the ship."),
            ],
            accent_border_color="border-blue-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="2. <strong>Ports:</strong> Each port is uniquely identified by its "),
                TextSegment(
                    text="5-character UN/LOCODE (e.g., GRPIR for Piraeus, NLRTM for Rotterdam)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Primary Key: United Nations Code for Trade and Transport Locations.",
                ),
                TextSegment(text=", its "),
                TextSegment(
                    text="official name",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Candidate Key: Unique geographical port name.",
                ),
                TextSegment(text=", the "),
                TextSegment(text="country", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=" and the "),
                TextSegment(text="maximum allowable draft", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=". A port possesses "),
                TextSegment(
                    text="multiple terminals/piers",
                    is_highlight=True,
                    category="attr",
                    tag_label="MULTIVALUED",
                    badge_class="badge-attr-multi",
                    tooltip="Multivalued Attribute: Extracted to separate table PORT_TERMINAL.",
                ),
                TextSegment(text=" recorded as a list of available facilities."),
            ],
            accent_border_color="border-emerald-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="3. <strong>Voyages / Commercial Routes:</strong> Each vessel performs scheduled commercial voyages. For each voyage, the system tracks a "),
                TextSegment(
                    text="unique Voyage Code",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Primary Key: Unique commercial voyage code.",
                ),
                TextSegment(text=", the "),
                TextSegment(
                    text="vessel executing it",
                    is_highlight=True,
                    category="rel",
                    tag_label="RELATIONSHIP 1:N",
                    badge_class="badge-rel",
                    tooltip="1:N Relationship (Vessel -> Voyage): Each voyage belongs to 1 vessel, a vessel performs multiple voyages.",
                ),
                TextSegment(text=", the "),
                TextSegment(
                    text="port of origin",
                    is_highlight=True,
                    category="rel",
                    tag_label="RELATIONSHIP 1:N",
                    badge_class="badge-rel",
                    tooltip="1:N Relationship (Port -> Voyage): Port of departure.",
                ),
                TextSegment(text=", the "),
                TextSegment(
                    text="port of destination",
                    is_highlight=True,
                    category="rel",
                    tag_label="RELATIONSHIP 1:N",
                    badge_class="badge-rel",
                    tooltip="1:N Relationship (Port -> Voyage): Port of final arrival.",
                ),
                TextSegment(text=", the "),
                TextSegment(text="estimated time of departure (ETD)", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="estimated time of arrival (ETA)", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="actual arrival timestamp", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="cargo type", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=" and the "),
                TextSegment(text="total cargo weight in metric tons", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text="."),
            ],
            accent_border_color="border-amber-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="4. <strong>Seafarers & Crew:</strong> For each seafarer, the following are recorded: the "),
                TextSegment(
                    text="unique Discharge Book Number (Seaman's Book Number)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Primary Key: Unique professional seafarer registration number.",
                ),
                TextSegment(text=", the "),
                TextSegment(
                    text="Passport Number",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Candidate Key: Unique international travel passport number.",
                ),
                TextSegment(text=", the "),
                TextSegment(text="first name", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="last name", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="date of birth", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="nationality", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(
                    text="permanent residential address (street, number, city, country)",
                    is_highlight=True,
                    category="attr",
                    tag_label="COMPOSITE",
                    badge_class="badge-attr-composite",
                    tooltip="Composite Attribute: Decomposed into Street, Number, City, and Country.",
                ),
                TextSegment(text=" and the "),
                TextSegment(text="primary rank/specialty (e.g., Captain, Chief Engineer, Able Seaman)", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=". Each seafarer holds "),
                TextSegment(
                    text="one or more international STCW certifications of competency (e.g., 'Medical First Aid', 'BRM')",
                    is_highlight=True,
                    category="attr",
                    tag_label="MULTIVALUED",
                    badge_class="badge-attr-multi",
                    tooltip="Multivalued Attribute: Extracted to separate table STCW_CERTIFICATION.",
                ),
                TextSegment(text=", which are documented in detail."),
            ],
            accent_border_color="border-purple-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="5. <strong>Crew Contracts / Embarkations:</strong> Seafarers "),
                TextSegment(
                    text="embark on vessels via formal fixed-term employment contracts",
                    is_highlight=True,
                    category="rel",
                    tag_label="RELATIONSHIP N:M",
                    badge_class="badge-rel",
                    tooltip="Associative Entity / N:M (Seafarer <-> Vessel): Many seafarers serve on many vessels successively.",
                ),
                TextSegment(text=". For each embarkation, the system records the vessel, the seafarer, the "),
                TextSegment(
                    text="sign-on date",
                    is_highlight=True,
                    category="key",
                    tag_label="PK COMPONENT",
                    badge_class="badge-key-pk",
                    tooltip="Primary Key Component: Allows multiple successive embarkations of the same seafarer on the same vessel.",
                ),
                TextSegment(text=", the "),
                TextSegment(text="sign-off date", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="duty rank/position on the voyage", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=" and the "),
                TextSegment(text="monthly net salary in US dollars", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=". In addition, for mentoring and training purposes, each cadet or junior officer has a designated senior officer serving as an "),
                TextSegment(
                    text="onboard mentor / instructor",
                    is_highlight=True,
                    category="rel",
                    tag_label="RELATIONSHIP 1:N",
                    badge_class="badge-rel",
                    tooltip="Recursive 1:N Relationship (Mentor Seafarer -> Mentee Seafarer).",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-cyan-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="6. <strong>Safety Inspections & Certificates:</strong> Each vessel periodically undergoes statutory inspections by classification societies and port state control authorities. For each inspection, the system records a "),
                TextSegment(
                    text="sequential inspection number for the specific vessel",
                    is_highlight=True,
                    category="key",
                    tag_label="PARTIAL KEY",
                    badge_class="badge-key-partial",
                    tooltip="Partial Key (Discriminator): Sequentially numbers inspections for each vessel (1, 2, 3...).",
                ),
                TextSegment(text=", the "),
                TextSegment(text="inspection date", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="inspection organization (e.g., Lloyd's Register, DNV)", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="result (Passed, Conditional/Observations, Rejected)", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=" and the "),
                TextSegment(text="expiration date of the issued seaworthiness certificate", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=". An inspection "),
                TextSegment(
                    text="cannot exist autonomously without its corresponding vessel",
                    is_highlight=True,
                    category="rel",
                    tag_label="IDENTIFYING 1:N",
                    badge_class="badge-rel",
                    tooltip="Identifying 1:N Relationship (Vessel -> Inspection): Total existential dependency of the weak entity.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-rose-500",
        ),
    ]

    # 2. Entities & Attributes
    entities = [
        Entity(
            name="VESSEL",
            entity_type="Strong Entity",
            is_weak=False,
            justification="Autonomous commercial fleet vessel with unique international IMO number and Call Sign.",
            attributes=[
                Attribute(name="imo_number", attr_type="Simple, Single-valued, Primary Key", is_pk=True),
                Attribute(name="call_sign", attr_type="Simple, Single-valued, Candidate Key", is_candidate=True),
                Attribute(name="vessel_name", attr_type="Simple, Single-valued"),
                Attribute(name="build_year", attr_type="Simple, Single-valued"),
                Attribute(name="flag", attr_type="Simple, Single-valued"),
                Attribute(name="dwt", attr_type="Simple, Single-valued"),
                Attribute(name="vessel_type", attr_type="Simple, Single-valued"),
            ],
        ),
        Entity(
            name="PORT",
            entity_type="Strong Entity",
            is_weak=False,
            justification="International port of call with unique UN/LOCODE.",
            attributes=[
                Attribute(name="un_locode", attr_type="Simple, Single-valued, Primary Key", is_pk=True),
                Attribute(name="port_name", attr_type="Simple, Single-valued, Candidate Key", is_candidate=True),
                Attribute(name="country", attr_type="Simple, Single-valued"),
                Attribute(name="max_draft", attr_type="Simple, Single-valued"),
                Attribute(name="terminals", attr_type="Multivalued", notes="Extracted to table PORT_TERMINAL"),
            ],
        ),
        Entity(
            name="VOYAGE",
            entity_type="Strong Entity",
            is_weak=False,
            justification="Scheduled commercial route with unique Voyage Code.",
            attributes=[
                Attribute(name="voyage_code", attr_type="Simple, Single-valued, Primary Key", is_pk=True),
                Attribute(name="etd", attr_type="Simple, Single-valued"),
                Attribute(name="eta", attr_type="Simple, Single-valued"),
                Attribute(name="actual_arrival", attr_type="Simple, Single-valued (Nullable)"),
                Attribute(name="cargo_type", attr_type="Simple, Single-valued"),
                Attribute(name="cargo_weight_tons", attr_type="Simple, Single-valued"),
            ],
        ),
        Entity(
            name="SEAFARER",
            entity_type="Strong Entity",
            is_weak=False,
            justification="Natural person professional seafarer with unique Discharge Book Number.",
            attributes=[
                Attribute(name="discharge_book_number", attr_type="Simple, Single-valued, Primary Key", is_pk=True),
                Attribute(name="passport_number", attr_type="Simple, Single-valued, Candidate Key", is_candidate=True),
                Attribute(name="first_name", attr_type="Simple, Single-valued"),
                Attribute(name="last_name", attr_type="Simple, Single-valued"),
                Attribute(name="birth_date", attr_type="Simple, Single-valued"),
                Attribute(name="nationality", attr_type="Simple, Single-valued"),
                Attribute(name="rank_specialty", attr_type="Simple, Single-valued"),
                Attribute(
                    name="residential_address",
                    attr_type="Composite",
                    components=["street", "number", "city", "country"],
                ),
                Attribute(name="stcw_certifications", attr_type="Multivalued", notes="Extracted to table STCW_CERTIFICATION"),
            ],
        ),
        Entity(
            name="EMBARKATION_CONTRACT",
            entity_type="Associative Entity",
            is_weak=False,
            justification="Employment contract of a seafarer on a specific vessel with sign-on date and compensation.",
            attributes=[
                Attribute(name="sign_on_date", attr_type="Simple, PK Component", is_pk=True),
                Attribute(name="sign_off_date", attr_type="Simple, Single-valued (Nullable)"),
                Attribute(name="duty_rank", attr_type="Simple, Single-valued"),
                Attribute(name="monthly_salary_usd", attr_type="Simple, Single-valued"),
            ],
        ),
        Entity(
            name="SAFETY_INSPECTION",
            entity_type="Weak Entity",
            is_weak=True,
            owner_entity="VESSEL",
            justification="Seaworthiness inspection. Existentially dependent on Vessel and numbered sequentially.",
            attributes=[
                Attribute(name="inspection_number", attr_type="Simple, Partial Key", is_partial=True),
                Attribute(name="inspection_date", attr_type="Simple, Single-valued"),
                Attribute(name="organization", attr_type="Simple, Single-valued"),
                Attribute(name="result", attr_type="Simple, Single-valued"),
                Attribute(name="certificate_expiry_date", attr_type="Simple, Single-valued"),
            ],
        ),
    ]

    # 3. Relationship Attributes
    relationship_attributes = [
        RelationshipAttribute(
            name="sign_on_date",
            relationship_name="EMBARKATION (N:M)",
            justification="Specifies the start date of embarkation on the specific vessel.",
        ),
        RelationshipAttribute(
            name="sign_off_date",
            relationship_name="EMBARKATION (N:M)",
            justification="Specifies the end date of embarkation on the specific vessel.",
        ),
        RelationshipAttribute(
            name="duty_rank",
            relationship_name="EMBARKATION (N:M)",
            justification="Describes the seafarer's role in the specific embarkation contract.",
        ),
        RelationshipAttribute(
            name="monthly_salary_usd",
            relationship_name="EMBARKATION (N:M)",
            justification="Agreed net monthly compensation for the contract duration.",
        ),
    ]

    # 4. Keys Analysis Table
    keys_analysis = [
        KeyAnalysisRow(
            entity_name="VESSEL",
            key_count="2",
            key_types="Candidate: {imo_number}, {call_sign}",
            final_pk_selection="imo_number",
            justification="Unique global 7-digit code remaining immutable throughout vessel lifetime.",
        ),
        KeyAnalysisRow(
            entity_name="PORT",
            key_count="2",
            key_types="Candidate: {un_locode}, {port_name}",
            final_pk_selection="un_locode",
            justification="Standard 5-character international code.",
        ),
        KeyAnalysisRow(
            entity_name="VOYAGE",
            key_count="1",
            key_types="Candidate: {voyage_code}",
            final_pk_selection="voyage_code",
            justification="Unique operational voyage code.",
        ),
        KeyAnalysisRow(
            entity_name="SEAFARER",
            key_count="2",
            key_types="Candidate: {discharge_book_number}, {passport_number}",
            final_pk_selection="discharge_book_number",
            justification="Official maritime identity discharge book document.",
        ),
        KeyAnalysisRow(
            entity_name="EMBARKATION_CONTRACT",
            key_count="1 (Composite)",
            key_types="Composite: {discharge_book_number, imo_number, sign_on_date}",
            final_pk_selection="{discharge_book_number, imo_number, sign_on_date}",
            justification="Allows the same seafarer to embark repeatedly on the same vessel on different dates.",
        ),
        KeyAnalysisRow(
            entity_name="SAFETY_INSPECTION",
            key_count="0 (Weak)",
            key_types="Partial Key: {inspection_number}",
            final_pk_selection="Composite PK: {Vessel.imo_number, inspection_number}",
            justification="Weak entity with existential dependency on Vessel.",
            is_weak=True,
        ),
    ]

    # 5. Relationships
    relationships = [
        Relationship(
            letter_id="a",
            name="CAPTAIN_COMMANDS",
            connected_entities="Vessel <-> Seafarer (Captain)",
            cardinality="1:1",
            participation="Total for Vessel, Partial for Seafarer",
            relationship_type="Regular Relationship",
            attributes=[],
            justification="Each vessel mandatorily has 1 captain who commands it, each seafarer is captain of at most 1 vessel.",
        ),
        Relationship(
            letter_id="b",
            name="EXECUTES_VOYAGE",
            connected_entities="Vessel <-> Voyage",
            cardinality="1:N",
            participation="Total for Voyage, Partial for Vessel",
            relationship_type="Regular Relationship",
            attributes=[],
            justification="Each voyage belongs to and is executed by 1 vessel, a vessel performs many voyages.",
        ),
        Relationship(
            letter_id="c",
            name="DEPARTS_FROM",
            connected_entities="Port (Origin) <-> Voyage",
            cardinality="1:N",
            participation="Total for Voyage, Partial for Port",
            relationship_type="Regular Relationship",
            attributes=[],
            justification="Each voyage originates from 1 specific port of departure.",
        ),
        Relationship(
            letter_id="d",
            name="DESTINATION_TO",
            connected_entities="Port (Destination) <-> Voyage",
            cardinality="1:N",
            participation="Total for Voyage, Partial for Port",
            relationship_type="Regular Relationship",
            attributes=[],
            justification="Each voyage terminates at 1 specific destination port.",
        ),
        Relationship(
            letter_id="e",
            name="EMBARKATION",
            connected_entities="Seafarer <-> Vessel",
            cardinality="N:M",
            participation="Partial for both sides",
            relationship_type="Associative Entity (Junction Table)",
            attributes=["sign_on_date", "sign_off_date", "duty_rank", "monthly_salary_usd"],
            justification="Many seafarers embark on many vessels over the course of their careers.",
        ),
        Relationship(
            letter_id="f",
            name="MENTORS",
            connected_entities="Seafarer (Mentor) <-> Seafarer (Mentee)",
            cardinality="1:N",
            participation="Partial for Mentor, Partial for Mentee",
            relationship_type="Recursive 1:N Relationship",
            attributes=[],
            justification="A senior officer guides cadets or junior officers onboard.",
        ),
        Relationship(
            letter_id="g",
            name="UNDERGOES_INSPECTION",
            connected_entities="Vessel <-> Safety Inspection",
            cardinality="1:N",
            participation="Total for Inspection, Partial for Vessel",
            relationship_type="Identifying Relationship",
            attributes=[],
            justification="Connects weak entity Safety Inspection to identifying owner Vessel.",
        ),
    ]

    # 6. Assumptions
    assumptions = [
        "Residential Address: Decomposed into Street, Number, City, and Country to guarantee First Normal Form (1NF).",
        "Multivalued Attributes: Port terminals and seafarer STCW certifications are implemented as separate relational tables.",
        "Embarkation Contract: Primary key includes sign_on_date, allowing repeated contracts for the same seafarer on the same ship.",
        "Safety Inspection: As a weak entity, it features a composite PK {imo_number, inspection_number} with ON DELETE CASCADE.",
    ]

    # 7. ER Table Nodes for SVG Crow's Foot Diagram
    er_tables = [
        ERTable(
            id="ploio",
            label="VESSEL",
            x=50,
            y=80,
            attrs=[
                ERTableAttr(name="imo_number", pk=True),
                ERTableAttr(name="call_sign"),
                ERTableAttr(name="vessel_name"),
                ERTableAttr(name="build_year"),
                ERTableAttr(name="flag"),
                ERTableAttr(name="dwt"),
                ERTableAttr(name="vessel_type"),
                ERTableAttr(name="captain_discharge_book", fk=True),
            ],
        ),
        ERTable(
            id="limani",
            label="PORT",
            x=50,
            y=450,
            attrs=[
                ERTableAttr(name="un_locode", pk=True),
                ERTableAttr(name="port_name"),
                ERTableAttr(name="country"),
                ERTableAttr(name="max_draft"),
            ],
        ),
        ERTable(
            id="terminal",
            label="PORT_TERMINAL",
            x=50,
            y=680,
            attrs=[
                ERTableAttr(name="un_locode", pk=True, fk=True),
                ERTableAttr(name="terminal_name", pk=True),
            ],
        ),
        ERTable(
            id="taxidi",
            label="VOYAGE",
            x=450,
            y=80,
            attrs=[
                ERTableAttr(name="voyage_code", pk=True),
                ERTableAttr(name="imo_number", fk=True),
                ERTableAttr(name="origin_port_code", fk=True),
                ERTableAttr(name="dest_port_code", fk=True),
                ERTableAttr(name="etd"),
                ERTableAttr(name="eta"),
                ERTableAttr(name="actual_arrival"),
                ERTableAttr(name="cargo_type"),
                ERTableAttr(name="cargo_weight_tons"),
            ],
        ),
        ERTable(
            id="naytikos",
            label="SEAFARER",
            x=850,
            y=50,
            attrs=[
                ERTableAttr(name="discharge_book_number", pk=True),
                ERTableAttr(name="passport_number"),
                ERTableAttr(name="first_name"),
                ERTableAttr(name="last_name"),
                ERTableAttr(name="birth_date"),
                ERTableAttr(name="nationality"),
                ERTableAttr(name="rank_specialty"),
                ERTableAttr(name="street"),
                ERTableAttr(name="street_number"),
                ERTableAttr(name="city"),
                ERTableAttr(name="country"),
                ERTableAttr(name="mentor_discharge_book", fk=True),
            ],
        ),
        ERTable(
            id="pistopoiisi_stcw",
            label="STCW_CERTIFICATION",
            x=850,
            y=480,
            attrs=[
                ERTableAttr(name="discharge_book_number", pk=True, fk=True),
                ERTableAttr(name="certification_name", pk=True),
            ],
        ),
        ERTable(
            id="symvasi",
            label="EMBARKATION_CONTRACT",
            x=450,
            y=450,
            attrs=[
                ERTableAttr(name="discharge_book_number", pk=True, fk=True),
                ERTableAttr(name="imo_number", pk=True, fk=True),
                ERTableAttr(name="sign_on_date", pk=True),
                ERTableAttr(name="sign_off_date"),
                ERTableAttr(name="duty_rank"),
                ERTableAttr(name="monthly_salary_usd"),
            ],
        ),
        ERTable(
            id="epitheorisi",
            label="SAFETY_INSPECTION",
            x=450,
            y=680,
            attrs=[
                ERTableAttr(name="imo_number", pk=True, fk=True),
                ERTableAttr(name="inspection_number", pk=True),
                ERTableAttr(name="inspection_date"),
                ERTableAttr(name="organization"),
                ERTableAttr(name="result"),
                ERTableAttr(name="certificate_expiry_date"),
            ],
        ),
    ]

    # 8. ER Diagram Edges
    er_edges = [
        EREdge(
            path="M 310,120 L 450,120",
            marker_start="start-one-mandatory",
            marker_end="end-many-mandatory",
            label="Executes (1:N)",
            lx=380,
            ly=110,
        ),
        EREdge(
            path="M 310,480 L 450,220",
            marker_start="start-one-optional",
            marker_end="end-many-mandatory",
            label="Origin (1:N)",
            lx=360,
            ly=340,
        ),
        EREdge(
            path="M 310,540 L 450,260",
            marker_start="start-one-optional",
            marker_end="end-many-mandatory",
            label="Destination (1:N)",
            lx=400,
            ly=400,
        ),
        EREdge(
            path="M 180,600 L 180,680",
            marker_start="start-one-mandatory",
            marker_end="end-many-mandatory",
            label="Terminals (1:N)",
            lx=180,
            ly=640,
        ),
        EREdge(
            path="M 980,440 L 980,480",
            marker_start="start-one-mandatory",
            marker_end="end-many-mandatory",
            label="STCW (1:N)",
            lx=980,
            ly=460,
        ),
        EREdge(
            path="M 310,240 L 310,500 L 450,500",
            marker_start="start-one-optional",
            marker_end="end-many-mandatory",
            label="Vessel Embarkation (1:N)",
            lx=360,
            ly=500,
        ),
        EREdge(
            path="M 850,250 L 710,480",
            marker_start="start-one-optional",
            marker_end="end-many-mandatory",
            label="Seafarer Embarkation (1:N)",
            lx=770,
            ly=370,
        ),
        EREdge(
            path="M 180,320 L 180,720 L 450,720",
            marker_start="start-one-optional",
            marker_end="end-many-mandatory",
            label="Inspection (1:N)",
            lx=300,
            ly=720,
        ),
        EREdge(
            path="M 310,80 L 850,80",
            marker_start="start-one-mandatory",
            marker_end="end-one-optional",
            label="Captain (1:1)",
            lx=580,
            ly=70,
        ),
        # Sailor Mentor recursive relationship (1:N)
        EREdge(
            path="M 1110,100 C 1170,40 1170,180 1110,140",
            marker_start="start-one-optional",
            marker_end="end-many-optional",
            label="Mentor (1:N)",
            lx=1180,
            ly=110,
        ),
    ]

    # 9. Relational Justifications
    relational_justifications = [
        RelationalJustification(
            title="1. 1:1 Captain Command Relationship:",
            color_class="text-blue-400",
            description="VESSEL has total participation in the command relationship. The Foreign Key captain_discharge_book is placed in table VESSEL.",
        ),
        RelationalJustification(
            title="2. Associative Entity EMBARKATION_CONTRACT:",
            color_class="text-emerald-400",
            description="The N:M relationship is implemented with composite PK {discharge_book_number, imo_number, sign_on_date} allowing multiple contracts per seafarer.",
        ),
        RelationalJustification(
            title="3. Multivalued Attributes (1NF):",
            color_class="text-amber-400",
            description="Port terminals and seafarer STCW certifications are decomposed into independent tables PORT_TERMINAL and STCW_CERTIFICATION.",
        ),
        RelationalJustification(
            title="4. Weak Entity for Inspections:",
            color_class="text-purple-400",
            description="SAFETY_INSPECTION has composite PK {imo_number, inspection_number} and foreign key rule ON DELETE CASCADE.",
        ),
    ]

    # 10. SQL DDL Script
    sql_ddl = """-- SQL DDL Schema: Maritime Fleet Management Database
-- 1. Entity: PORT
CREATE TABLE PORT (
    un_locode VARCHAR(5) PRIMARY KEY,
    port_name VARCHAR(100) NOT NULL UNIQUE,
    country VARCHAR(50) NOT NULL,
    max_draft DECIMAL(5, 2) NOT NULL
);

-- 2. Multivalued Attribute: PORT_TERMINAL
CREATE TABLE PORT_TERMINAL (
    un_locode VARCHAR(5) NOT NULL,
    terminal_name VARCHAR(100) NOT NULL,
    PRIMARY KEY (un_locode, terminal_name),
    FOREIGN KEY (un_locode) REFERENCES PORT(un_locode) ON DELETE CASCADE
);

-- 3. Entity: SEAFARER
CREATE TABLE SEAFARER (
    discharge_book_number VARCHAR(20) PRIMARY KEY,
    passport_number VARCHAR(20) NOT NULL UNIQUE,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    birth_date DATE NOT NULL,
    nationality VARCHAR(50) NOT NULL,
    rank_specialty VARCHAR(50) NOT NULL,
    street VARCHAR(100) NOT NULL,
    street_number VARCHAR(10) NOT NULL,
    city VARCHAR(50) NOT NULL,
    country VARCHAR(50) NOT NULL,
    mentor_discharge_book VARCHAR(20),
    FOREIGN KEY (mentor_discharge_book) REFERENCES SEAFARER(discharge_book_number)
);

-- 4. Multivalued Attribute: STCW_CERTIFICATION
CREATE TABLE STCW_CERTIFICATION (
    discharge_book_number VARCHAR(20) NOT NULL,
    certification_name VARCHAR(100) NOT NULL,
    PRIMARY KEY (discharge_book_number, certification_name),
    FOREIGN KEY (discharge_book_number) REFERENCES SEAFARER(discharge_book_number) ON DELETE CASCADE
);

-- 5. Entity: VESSEL
CREATE TABLE VESSEL (
    imo_number VARCHAR(10) PRIMARY KEY,
    call_sign VARCHAR(15) NOT NULL UNIQUE,
    vessel_name VARCHAR(100) NOT NULL,
    build_year INT NOT NULL,
    flag VARCHAR(50) NOT NULL,
    dwt DECIMAL(12, 2) NOT NULL,
    vessel_type VARCHAR(50) NOT NULL,
    captain_discharge_book VARCHAR(20) NOT NULL UNIQUE,
    FOREIGN KEY (captain_discharge_book) REFERENCES SEAFARER(discharge_book_number)
);

-- 6. Entity: VOYAGE
CREATE TABLE VOYAGE (
    voyage_code VARCHAR(30) PRIMARY KEY,
    imo_number VARCHAR(10) NOT NULL,
    origin_port_code VARCHAR(5) NOT NULL,
    dest_port_code VARCHAR(5) NOT NULL,
    etd TIMESTAMP NOT NULL,
    eta TIMESTAMP NOT NULL,
    actual_arrival TIMESTAMP,
    cargo_type VARCHAR(100) NOT NULL,
    cargo_weight_tons DECIMAL(12, 2) NOT NULL,
    FOREIGN KEY (imo_number) REFERENCES VESSEL(imo_number),
    FOREIGN KEY (origin_port_code) REFERENCES PORT(un_locode),
    FOREIGN KEY (dest_port_code) REFERENCES PORT(un_locode)
);

-- 7. Associative Entity / Junction: EMBARKATION_CONTRACT
CREATE TABLE EMBARKATION_CONTRACT (
    discharge_book_number VARCHAR(20) NOT NULL,
    imo_number VARCHAR(10) NOT NULL,
    sign_on_date DATE NOT NULL,
    sign_off_date DATE,
    duty_rank VARCHAR(50) NOT NULL,
    monthly_salary_usd DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (discharge_book_number, imo_number, sign_on_date),
    FOREIGN KEY (discharge_book_number) REFERENCES SEAFARER(discharge_book_number) ON DELETE CASCADE,
    FOREIGN KEY (imo_number) REFERENCES VESSEL(imo_number) ON DELETE CASCADE
);

-- 8. Weak Entity: SAFETY_INSPECTION
CREATE TABLE SAFETY_INSPECTION (
    imo_number VARCHAR(10) NOT NULL,
    inspection_number INT NOT NULL,
    inspection_date DATE NOT NULL,
    organization VARCHAR(100) NOT NULL,
    result VARCHAR(50) NOT NULL CHECK (result IN ('Passed', 'Conditional/Observations', 'Rejected')),
    certificate_expiry_date DATE NOT NULL,
    PRIMARY KEY (imo_number, inspection_number),
    FOREIGN KEY (imo_number) REFERENCES VESSEL(imo_number) ON DELETE CASCADE
);"""

    return Scenario(
        id="maritime_shipping",
        title="Maritime Fleet & Crew Management System",
        subtitle="Entity-Relationship Modeling for Vessels, Ports, Voyages, Seafarers, Contracts & Inspections",
        course_tag="Databases (Progress Test 2025-2026 - Topic 2)",
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
