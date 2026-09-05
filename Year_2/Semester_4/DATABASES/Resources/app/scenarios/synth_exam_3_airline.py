"""Airline Management and Flight Operations case study scenario module.

Contains the complete parsed and modeled ER analysis for the International Airline
Company (Airports, Flight Schedules, Flight Instances, Aircraft, Flight Crew, Passengers, Bookings),
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


def createAirlineManagementScenario() -> Scenario:
    """Constructs and returns the Airline Management database scenario.

    Returns:
        Scenario: Fully populated scenario instance.
    """
    # 1. Text Paragraphs with Interactive Segments
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="An international commercial airline is designing a new relational database to manage its flight operations, "),
                TextSegment(
                    text="airports",
                    is_highlight=True,
                    category="entity",
                    tag_label="ENTITY",
                    badge_class="badge-entity-strong",
                    tooltip="Strong Entity: International airport with unique IATA code.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="scheduled flight routes",
                    is_highlight=True,
                    category="entity",
                    tag_label="ENTITY",
                    badge_class="badge-entity-strong",
                    tooltip="Strong Entity: Regular route with unique flight number.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="actual flight instances",
                    is_highlight=True,
                    category="entity",
                    tag_label="WEAK ENTITY",
                    badge_class="badge-entity-weak",
                    tooltip="Weak Entity: Scheduled route execution on a specific calendar date.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="aircraft fleet",
                    is_highlight=True,
                    category="entity",
                    tag_label="ENTITY",
                    badge_class="badge-entity-strong",
                    tooltip="Strong Entity: Fleet aircraft with manufacturer serial number MSN.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="flight crew",
                    is_highlight=True,
                    category="entity",
                    tag_label="ENTITY",
                    badge_class="badge-entity-strong",
                    tooltip="Strong Entity: Flight and cabin personnel with employee number AME.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="passengers",
                    is_highlight=True,
                    category="entity",
                    tag_label="ENTITY",
                    badge_class="badge-entity-strong",
                    tooltip="Strong Entity: Natural person traveler with passport number.",
                ),
                TextSegment(text=" and "),
                TextSegment(
                    text="ticket bookings",
                    is_highlight=True,
                    category="entity",
                    tag_label="ASSOCIATIVE",
                    badge_class="badge-entity-strong",
                    tooltip="Associative Entity: Electronic ticket booking with unique PNR code.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color=None,
        ),
        Paragraph(
            segments=[
                TextSegment(text="1. <strong>Airports:</strong> Each airport is characterized by a "),
                TextSegment(
                    text="unique 3-letter IATA code (e.g., ATH, LHR)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Primary Key: International 3-letter IATA code.",
                ),
                TextSegment(text=", its "),
                TextSegment(
                    text="official name",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Candidate Key: Unique airport name.",
                ),
                TextSegment(text=", the "),
                TextSegment(text="city", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=" and the "),
                TextSegment(text="country", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=" in which it is located. Each airport features one or more "),
                TextSegment(
                    text="takeoff and landing runways (Runways)",
                    is_highlight=True,
                    category="attr",
                    tag_label="MULTIVALUED",
                    badge_class="badge-attr-multi",
                    tooltip="Multivalued Attribute: Extracted to table AIRPORT_RUNWAY.",
                ),
                TextSegment(text=", for which distinct runway lengths and identifiers are recorded."),
            ],
            accent_border_color="border-blue-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="2. <strong>Scheduled Flight Routes:</strong> Each regular scheduled route has a "),
                TextSegment(
                    text="unique flight number (e.g., OA315)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Primary Key: Unique route flight number.",
                ),
                TextSegment(text=", "),
                TextSegment(text="scheduled departure time", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="scheduled arrival time", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="estimated flight duration", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=" and "),
                TextSegment(text="distance in nautical miles", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=". Each scheduled flight connects exactly two airports: a "),
                TextSegment(
                    text="departure airport (Departure Airport)",
                    is_highlight=True,
                    category="rel",
                    tag_label="RELATIONSHIP 1:N",
                    badge_class="badge-rel",
                    tooltip="1:N Relationship (Airport -> Flight): Origin airport.",
                ),
                TextSegment(text=" and an "),
                TextSegment(
                    text="arrival airport (Arrival Airport)",
                    is_highlight=True,
                    category="rel",
                    tag_label="RELATIONSHIP 1:N",
                    badge_class="badge-rel",
                    tooltip="1:N Relationship (Airport -> Flight): Destination airport.",
                ),
                TextSegment(text=". An airport can serve as departure point for multiple flights and arrival point for multiple others."),
            ],
            accent_border_color="border-emerald-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="3. <strong>Flight Instances (Actual Flights):</strong> A scheduled route is "),
                TextSegment(
                    text="executed",
                    is_highlight=True,
                    category="rel",
                    tag_label="IDENTIFYING 1:N",
                    badge_class="badge-rel",
                    tooltip="Identifying 1:N Relationship (Scheduled Flight -> Flight Instance): Total participation of flight instance.",
                ),
                TextSegment(text=" on specific calendar dates. Each specific flight instance is identified by the flight number combined with the "),
                TextSegment(
                    text="flight date (Flight Date)",
                    is_highlight=True,
                    category="key",
                    tag_label="PARTIAL KEY",
                    badge_class="badge-key-partial",
                    tooltip="Partial Key (Discriminator): Identifies the flight instance in conjunction with the flight number.",
                ),
                TextSegment(text=". For each actual flight instance, the following are recorded: "),
                TextSegment(text="actual departure time", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="actual arrival time", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="flight status (e.g., 'On Time', 'Delayed', 'Cancelled', 'Landed')", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=" and "),
                TextSegment(text="number of available seats", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text="."),
            ],
            accent_border_color="border-amber-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="4. <strong>Aircraft:</strong> The airline fleet consists of aircraft. Each aircraft has a "),
                TextSegment(
                    text="unique manufacturer serial number (MSN)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Primary Key: Manufacturer Serial Number.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="tail registration number (Tail Number)",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Candidate Key: Unique tail registration code.",
                ),
                TextSegment(text=", "),
                TextSegment(text="model (e.g., 'Airbus A320neo', 'Boeing 787-9')", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="manufacture year", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=" and "),
                TextSegment(text="maximum passenger capacity", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=". Each specific flight instance is "),
                TextSegment(
                    text="executed by exactly one aircraft",
                    is_highlight=True,
                    category="rel",
                    tag_label="RELATIONSHIP 1:N",
                    badge_class="badge-rel",
                    tooltip="1:N Relationship (Aircraft -> Flight Instance): Total participation of flight instance, 1 aircraft per flight.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-purple-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="5. <strong>Flight Crew & Pilots:</strong> For each crew member, the following are recorded: the "),
                TextSegment(
                    text="Employee Registration Number (AME)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Primary Key: Unique airline employee registration number.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="National ID Number (ADT)",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Candidate Key: National identity card number.",
                ),
                TextSegment(text=", "),
                TextSegment(text="full name", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="phone number", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="residential address", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="hire date", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=" and "),
                TextSegment(text="crew role (Captain, First Officer, Purser, Flight Attendant)", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=". For each specific flight, a crew team is designated. For each "),
                TextSegment(
                    text="assignment",
                    is_highlight=True,
                    category="rel",
                    tag_label="RELATIONSHIP N:M",
                    badge_class="badge-rel",
                    tooltip="Associative Entity / N:M (Flight Crew <-> Flight Instance).",
                ),
                TextSegment(text=" the "),
                TextSegment(
                    text="assigned role on that specific flight",
                    is_highlight=True,
                    category="attr",
                    tag_label="REL ATTRIBUTE",
                    badge_class="badge-attr-simple",
                    tooltip="Relationship Attribute: Assignment role on the specific flight.",
                ),
                TextSegment(text=" is recorded. In addition, an experienced Captain may "),
                TextSegment(
                    text="supervise and mentor",
                    is_highlight=True,
                    category="rel",
                    tag_label="RELATIONSHIP 1:N",
                    badge_class="badge-rel",
                    tooltip="Recursive 1:N Relationship (Instructor Captain -> Trainee First Officer).",
                ),
                TextSegment(text=" junior First Officers within the annual training program."),
            ],
            accent_border_color="border-cyan-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="6. <strong>Passengers & Bookings:</strong> For each passenger, the following are recorded: the "),
                TextSegment(
                    text="unique passport number",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Primary Key: Unique international passenger passport number.",
                ),
                TextSegment(text=", "),
                TextSegment(text="full name", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="nationality", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(
                    text="email",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Candidate Key: Unique email address.",
                ),
                TextSegment(text=" and "),
                TextSegment(text="phone number", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=". A passenger may book "),
                TextSegment(
                    text="electronic tickets (bookings)",
                    is_highlight=True,
                    category="rel",
                    tag_label="RELATIONSHIP N:M",
                    badge_class="badge-rel",
                    tooltip="Booking Entity / N:M (Passenger <-> Flight Instance).",
                ),
                TextSegment(text=" for specific flight instances. Each ticket booking has a "),
                TextSegment(
                    text="unique 6-character booking reference code (PNR)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Primary Key: Passenger Name Record 6-character alphanumeric code.",
                ),
                TextSegment(text=", "),
                TextSegment(text="assigned seat number (Seat Number)", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="class (Economy, Business)", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="ticket price", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=" and "),
                TextSegment(text="allowable baggage weight", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text="."),
            ],
            accent_border_color="border-rose-500",
        ),
    ]

    # 2. Entities & Attributes
    entities = [
        Entity(
            name="AIRPORT",
            entity_type="Strong Entity",
            is_weak=False,
            justification="International airport with unique IATA identification code.",
            attributes=[
                Attribute(name="iata_code", attr_type="Simple, Single-valued, Primary Key", is_pk=True),
                Attribute(name="airport_name", attr_type="Simple, Single-valued, Candidate Key", is_candidate=True),
                Attribute(name="city", attr_type="Simple, Single-valued"),
                Attribute(name="country", attr_type="Simple, Single-valued"),
                Attribute(
                    name="runways",
                    attr_type="Composite Multivalued",
                    components=["runway_name", "length_meters"],
                    notes="Extracted to table AIRPORT_RUNWAY",
                ),
            ],
        ),
        Entity(
            name="SCHEDULED_FLIGHT",
            entity_type="Strong Entity",
            is_weak=False,
            justification="Regular scheduled flight route with unique flight_number identifier.",
            attributes=[
                Attribute(name="flight_number", attr_type="Simple, Single-valued, Primary Key", is_pk=True),
                Attribute(name="scheduled_departure_time", attr_type="Simple, Single-valued"),
                Attribute(name="scheduled_arrival_time", attr_type="Simple, Single-valued"),
                Attribute(name="estimated_duration_minutes", attr_type="Simple, Single-valued"),
                Attribute(name="distance_nm", attr_type="Simple, Single-valued"),
            ],
        ),
        Entity(
            name="FLIGHT_INSTANCE",
            entity_type="Weak Entity",
            is_weak=True,
            owner_entity="SCHEDULED_FLIGHT",
            justification="Actual flight execution on a specific date. Identified in combination with flight_number.",
            attributes=[
                Attribute(name="flight_date", attr_type="Simple, Partial Key", is_partial=True),
                Attribute(name="actual_departure_time", attr_type="Simple, Single-valued (Nullable)"),
                Attribute(name="actual_arrival_time", attr_type="Simple, Single-valued (Nullable)"),
                Attribute(name="flight_status", attr_type="Simple, Single-valued"),
                Attribute(name="available_seats", attr_type="Simple, Single-valued"),
            ],
        ),
        Entity(
            name="AIRCRAFT",
            entity_type="Strong Entity",
            is_weak=False,
            justification="Physical fleet aircraft with unique manufacturer serial number MSN and Tail Number.",
            attributes=[
                Attribute(name="msn", attr_type="Simple, Single-valued, Primary Key", is_pk=True),
                Attribute(name="tail_number", attr_type="Simple, Single-valued, Candidate Key", is_candidate=True),
                Attribute(name="model", attr_type="Simple, Single-valued"),
                Attribute(name="manufacture_year", attr_type="Simple, Single-valued"),
                Attribute(name="passenger_capacity", attr_type="Simple, Single-valued"),
            ],
        ),
        Entity(
            name="FLIGHT_CREW",
            entity_type="Strong Entity",
            is_weak=False,
            justification="Flight or cabin crew employee with unique Employee Registration Number (AME).",
            attributes=[
                Attribute(name="ame", attr_type="Simple, Single-valued, Primary Key", is_pk=True),
                Attribute(name="national_id", attr_type="Simple, Single-valued, Candidate Key", is_candidate=True),
                Attribute(name="full_name", attr_type="Simple, Single-valued"),
                Attribute(name="phone_number", attr_type="Simple, Single-valued"),
                Attribute(name="address", attr_type="Simple, Single-valued"),
                Attribute(name="hire_date", attr_type="Simple, Single-valued"),
                Attribute(name="primary_role", attr_type="Simple, Single-valued"),
            ],
        ),
        Entity(
            name="PASSENGER",
            entity_type="Strong Entity",
            is_weak=False,
            justification="Natural person traveler with unique Passport Number.",
            attributes=[
                Attribute(name="passport_number", attr_type="Simple, Single-valued, Primary Key", is_pk=True),
                Attribute(name="full_name", attr_type="Simple, Single-valued"),
                Attribute(name="nationality", attr_type="Simple, Single-valued"),
                Attribute(name="email", attr_type="Simple, Single-valued, Candidate Key", is_candidate=True),
                Attribute(name="phone_number", attr_type="Simple, Single-valued"),
            ],
        ),
        Entity(
            name="TICKET_BOOKING",
            entity_type="Associative Entity",
            is_weak=False,
            justification="Passenger ticket issuance for a specific flight instance with unique PNR code.",
            attributes=[
                Attribute(name="pnr", attr_type="Simple, Single-valued, Primary Key", is_pk=True),
                Attribute(name="seat_number", attr_type="Simple, Single-valued"),
                Attribute(name="seat_class", attr_type="Simple, Single-valued"),
                Attribute(name="ticket_price_eur", attr_type="Simple, Single-valued"),
                Attribute(name="baggage_weight_kg", attr_type="Simple, Single-valued"),
            ],
        ),
    ]

    # 3. Relationship Attributes
    relationship_attributes = [
        RelationshipAttribute(
            name="flight_role",
            relationship_name="CREW_ASSIGNMENT (N:M)",
            justification="Describes the crew member's duties on the specific flight (e.g., Captain, First Officer).",
        ),
    ]

    # 4. Keys Analysis Table
    keys_analysis = [
        KeyAnalysisRow(
            entity_name="AIRPORT",
            key_count="2",
            key_types="Candidate: {iata_code}, {airport_name}",
            final_pk_selection="iata_code",
            justification="Standard 3-character alphanumeric code.",
        ),
        KeyAnalysisRow(
            entity_name="SCHEDULED_FLIGHT",
            key_count="1",
            key_types="Candidate: {flight_number}",
            final_pk_selection="flight_number",
            justification="Unique route flight code (e.g., OA315).",
        ),
        KeyAnalysisRow(
            entity_name="FLIGHT_INSTANCE",
            key_count="0 (Weak)",
            key_types="Partial Key: {flight_date}",
            final_pk_selection="Composite PK: {Scheduled_Flight.flight_number, flight_date}",
            justification="Weak entity dependent on scheduled flight route.",
            is_weak=True,
        ),
        KeyAnalysisRow(
            entity_name="AIRCRAFT",
            key_count="2",
            key_types="Candidate: {msn}, {tail_number}",
            final_pk_selection="msn",
            justification="Unique manufacturer serial number.",
        ),
        KeyAnalysisRow(
            entity_name="FLIGHT_CREW",
            key_count="2",
            key_types="Candidate: {ame}, {national_id}",
            final_pk_selection="ame",
            justification="Internal airline employee registry number.",
        ),
        KeyAnalysisRow(
            entity_name="PASSENGER",
            key_count="2",
            key_types="Candidate: {passport_number}, {email}",
            final_pk_selection="passport_number",
            justification="Official international travel document.",
        ),
        KeyAnalysisRow(
            entity_name="TICKET_BOOKING",
            key_count="1",
            key_types="Candidate: {pnr}",
            final_pk_selection="pnr",
            justification="Unique 6-character Passenger Name Record electronic booking code.",
        ),
    ]

    # 5. Relationships
    relationships = [
        Relationship(
            letter_id="a",
            name="DEPARTURE_AIRPORT",
            connected_entities="Airport <-> Scheduled Flight",
            cardinality="1:N",
            participation="Total for Flight, Partial for Airport",
            relationship_type="Regular Relationship",
            attributes=[],
            justification="Each scheduled flight departs from 1 origin airport.",
        ),
        Relationship(
            letter_id="b",
            name="ARRIVAL_AIRPORT",
            connected_entities="Airport <-> Scheduled Flight",
            cardinality="1:N",
            participation="Total for Flight, Partial for Airport",
            relationship_type="Regular Relationship",
            attributes=[],
            justification="Each scheduled flight lands at 1 destination airport.",
        ),
        Relationship(
            letter_id="c",
            name="ROUTE_EXECUTION",
            connected_entities="Scheduled Flight <-> Flight Instance",
            cardinality="1:N",
            participation="Total for Flight Instance, Partial for Scheduled Flight",
            relationship_type="Identifying Relationship",
            attributes=[],
            justification="Connects weak entity Flight Instance to scheduled route.",
        ),
        Relationship(
            letter_id="d",
            name="OPERATED_BY_AIRCRAFT",
            connected_entities="Aircraft <-> Flight Instance",
            cardinality="1:N",
            participation="Total for Flight Instance, Partial for Aircraft",
            relationship_type="Regular Relationship",
            attributes=[],
            justification="Each specific flight instance is operated by 1 physical aircraft.",
        ),
        Relationship(
            letter_id="e",
            name="TRAINS_PILOTS",
            connected_entities="Flight Crew (Captain) <-> Flight Crew (First Officer)",
            cardinality="1:N",
            participation="Partial for both sides",
            relationship_type="Recursive 1:N Relationship",
            attributes=[],
            justification="An experienced captain trains junior first officers.",
        ),
        Relationship(
            letter_id="f",
            name="CREW_ASSIGNMENT",
            connected_entities="Flight Crew <-> Flight Instance",
            cardinality="N:M",
            participation="Partial for both sides",
            relationship_type="Associative Entity (Junction)",
            attributes=["flight_role"],
            justification="Multiple crew members are assigned to each flight instance and each member flies multiple flights.",
        ),
        Relationship(
            letter_id="g",
            name="TICKET_BOOKING",
            connected_entities="Passenger <-> Flight Instance",
            cardinality="N:M",
            participation="Partial for both sides",
            relationship_type="Associative Entity / Booking",
            attributes=["pnr", "seat_number", "seat_class", "ticket_price_eur", "baggage_weight_kg"],
            justification="A passenger books tickets for multiple flights and a flight carries multiple passengers.",
        ),
    ]

    # 6. Assumptions
    assumptions = [
        "Multivalued Attributes: Airport runways are implemented in table AIRPORT_RUNWAY with composite primary key {iata_code, runway_name}.",
        "Flight Instance: Implemented as a weak entity with composite PK {flight_number, flight_date} and identifying dependency on Scheduled Flight.",
        "Ticket Booking: Has unique PNR code as primary key, with Foreign Keys to Passenger and Flight Instance.",
        "Crew Assignment: Connects crew members to specific flight instances (N:M), recording the specific assigned flight role.",
        "Pilot Mentoring: Implemented as a recursive 1:N self-referencing relationship in table FLIGHT_CREW via optional mentor_ame attribute.",
        "Departure & Arrival Airports: Each scheduled flight mandatorily connects two distinct airports (departure_iata != arrival_iata).",
    ]

    # 7. ER Table Nodes for SVG Crow's Foot Diagram
    er_tables = [
        ERTable(
            id="aerodromio",
            label="AIRPORT",
            x=50,
            y=80,
            attrs=[
                ERTableAttr(name="iata_code", pk=True),
                ERTableAttr(name="airport_name"),
                ERTableAttr(name="city"),
                ERTableAttr(name="country"),
            ],
        ),
        ERTable(
            id="diadromos",
            label="AIRPORT_RUNWAY",
            x=50,
            y=300,
            attrs=[
                ERTableAttr(name="iata_code", pk=True, fk=True),
                ERTableAttr(name="runway_name", pk=True),
                ERTableAttr(name="length_meters"),
            ],
        ),
        ERTable(
            id="programmatismeni",
            label="SCHEDULED_FLIGHT",
            x=450,
            y=50,
            attrs=[
                ERTableAttr(name="flight_number", pk=True),
                ERTableAttr(name="departure_iata", fk=True),
                ERTableAttr(name="arrival_iata", fk=True),
                ERTableAttr(name="scheduled_dept_time"),
                ERTableAttr(name="scheduled_arr_time"),
                ERTableAttr(name="duration_minutes"),
                ERTableAttr(name="distance_nm"),
            ],
        ),
        ERTable(
            id="stigmiotypo",
            label="FLIGHT_INSTANCE",
            x=450,
            y=380,
            attrs=[
                ERTableAttr(name="flight_number", pk=True, fk=True),
                ERTableAttr(name="flight_date", pk=True),
                ERTableAttr(name="msn", fk=True),
                ERTableAttr(name="actual_dept_time"),
                ERTableAttr(name="actual_arr_time"),
                ERTableAttr(name="flight_status"),
                ERTableAttr(name="available_seats"),
            ],
        ),
        ERTable(
            id="aeroskafos",
            label="AIRCRAFT",
            x=50,
            y=480,
            attrs=[
                ERTableAttr(name="msn", pk=True),
                ERTableAttr(name="tail_number"),
                ERTableAttr(name="model"),
                ERTableAttr(name="manufacture_year"),
                ERTableAttr(name="capacity"),
            ],
        ),
        ERTable(
            id="pliroma",
            label="FLIGHT_CREW",
            x=850,
            y=50,
            attrs=[
                ERTableAttr(name="ame", pk=True),
                ERTableAttr(name="national_id"),
                ERTableAttr(name="full_name"),
                ERTableAttr(name="phone_number"),
                ERTableAttr(name="address"),
                ERTableAttr(name="hire_date"),
                ERTableAttr(name="primary_role"),
                ERTableAttr(name="mentor_ame", fk=True),
            ],
        ),
        ERTable(
            id="anathesi",
            label="CREW_ASSIGNMENT",
            x=850,
            y=380,
            attrs=[
                ERTableAttr(name="flight_number", pk=True, fk=True),
                ERTableAttr(name="flight_date", pk=True, fk=True),
                ERTableAttr(name="ame", pk=True, fk=True),
                ERTableAttr(name="flight_role"),
            ],
        ),
        ERTable(
            id="epivatis",
            label="PASSENGER",
            x=50,
            y=700,
            attrs=[
                ERTableAttr(name="passport_number", pk=True),
                ERTableAttr(name="full_name"),
                ERTableAttr(name="nationality"),
                ERTableAttr(name="email"),
                ERTableAttr(name="phone_number"),
            ],
        ),
        ERTable(
            id="kratisi",
            label="TICKET_BOOKING",
            x=450,
            y=700,
            attrs=[
                ERTableAttr(name="pnr", pk=True),
                ERTableAttr(name="flight_number", fk=True),
                ERTableAttr(name="flight_date", fk=True),
                ERTableAttr(name="passport_number", fk=True),
                ERTableAttr(name="seat_number"),
                ERTableAttr(name="seat_class"),
                ERTableAttr(name="price_eur"),
                ERTableAttr(name="baggage_weight_kg"),
            ],
        ),
    ]

    # 8. ER Diagram Edges
    er_edges = [
        EREdge(
            path="M 310,100 L 450,80",
            marker_start="start-one-mandatory",
            marker_end="end-many-mandatory",
            label="Departure (1:N)",
            lx=380,
            ly=75,
        ),
        EREdge(
            path="M 310,140 L 450,120",
            marker_start="start-one-mandatory",
            marker_end="end-many-mandatory",
            label="Arrival (1:N)",
            lx=380,
            ly=135,
        ),
        EREdge(
            path="M 180,240 L 180,300",
            marker_start="start-one-mandatory",
            marker_end="end-many-mandatory",
            label="Runways (1:N)",
            lx=180,
            ly=270,
        ),
        EREdge(
            path="M 580,294 L 580,380",
            marker_start="start-one-mandatory",
            marker_end="end-many-mandatory",
            label="Execution (1:N)",
            lx=580,
            ly=337,
        ),
        EREdge(
            path="M 310,540 L 450,480",
            marker_start="start-one-mandatory",
            marker_end="end-many-mandatory",
            label="Aircraft (1:N)",
            lx=380,
            ly=510,
        ),
        EREdge(
            path="M 980,322 L 980,380",
            marker_start="start-one-mandatory",
            marker_end="end-many-mandatory",
            label="Assignment (1:N)",
            lx=980,
            ly=351,
        ),
        EREdge(
            path="M 710,480 L 850,480",
            marker_start="start-one-mandatory",
            marker_end="end-many-mandatory",
            label="Flight-Crew (1:N)",
            lx=780,
            ly=465,
        ),
        EREdge(
            path="M 310,750 L 450,750",
            marker_start="start-one-mandatory",
            marker_end="end-many-mandatory",
            label="Passenger Booking (1:N)",
            lx=380,
            ly=735,
        ),
        EREdge(
            path="M 580,624 L 580,700",
            marker_start="start-one-mandatory",
            marker_end="end-many-mandatory",
            label="Flight Booking (1:N)",
            lx=580,
            ly=662,
        ),
        # Pilot Mentor recursive relationship (1:N)
        EREdge(
            path="M 1110,100 C 1180,40 1180,200 1110,160",
            marker_start="start-one-optional",
            marker_end="end-many-optional",
            label="Mentor (1:N)",
            lx=1185,
            ly=120,
        ),
    ]

    # 9. Relational Justifications
    relational_justifications = [
        RelationalJustification(
            title="1. Dual Airport - Flight Relationship:",
            color_class="text-blue-400",
            description="SCHEDULED_FLIGHT contains two distinct Foreign Keys to AIRPORT (departure_iata and arrival_iata) specifying origin and destination airports.",
        ),
        RelationalJustification(
            title="2. Weak Entity for Flight Instances:",
            color_class="text-purple-400",
            description="FLIGHT_INSTANCE has composite PK {flight_number, flight_date} and existential/identifying dependency on the scheduled route (ON DELETE CASCADE).",
        ),
        RelationalJustification(
            title="3. Associative Entity for Bookings:",
            color_class="text-emerald-400",
            description="TICKET_BOOKING table has autonomous PK PNR and Foreign Keys to Passenger (passport_number) and Flight Instance (flight_number, flight_date).",
        ),
        RelationalJustification(
            title="4. Multivalued Attributes (1NF):",
            color_class="text-amber-400",
            description="Runways are decomposed into AIRPORT_RUNWAY with composite PK {iata_code, runway_name} and an FK to Airport.",
        ),
        RelationalJustification(
            title="5. Recursive Pilot Mentoring (1:N):",
            color_class="text-cyan-400",
            description="Table FLIGHT_CREW contains optional Foreign Key mentor_ame referencing primary key ame of the same table (Self-Referencing FK).",
        ),
        RelationalJustification(
            title="6. Associative Table for Crew Assignment (N:M):",
            color_class="text-rose-400",
            description="The N:M relationship is implemented in CREW_ASSIGNMENT with composite PK {flight_number, flight_date, ame} and descriptive attribute flight_role.",
        ),
    ]

    # 10. SQL DDL Script
    sql_ddl = """-- SQL DDL Schema: Airline Operations & Bookings Database
-- 1. Entity: AIRPORT
CREATE TABLE AIRPORT (
    iata_code VARCHAR(3) PRIMARY KEY,
    airport_name VARCHAR(100) NOT NULL UNIQUE,
    city VARCHAR(50) NOT NULL,
    country VARCHAR(50) NOT NULL
);

-- 2. Multivalued Attribute: AIRPORT_RUNWAY
CREATE TABLE AIRPORT_RUNWAY (
    iata_code VARCHAR(3) NOT NULL,
    runway_name VARCHAR(20) NOT NULL,
    length_meters INT NOT NULL,
    PRIMARY KEY (iata_code, runway_name),
    FOREIGN KEY (iata_code) REFERENCES AIRPORT(iata_code) ON DELETE CASCADE
);

-- 3. Entity: SCHEDULED_FLIGHT
CREATE TABLE SCHEDULED_FLIGHT (
    flight_number VARCHAR(10) PRIMARY KEY,
    departure_iata VARCHAR(3) NOT NULL,
    arrival_iata VARCHAR(3) NOT NULL,
    scheduled_dept_time TIME NOT NULL,
    scheduled_arr_time TIME NOT NULL,
    duration_minutes INT NOT NULL,
    distance_nm DECIMAL(8, 2) NOT NULL,
    FOREIGN KEY (departure_iata) REFERENCES AIRPORT(iata_code),
    FOREIGN KEY (arrival_iata) REFERENCES AIRPORT(iata_code)
);

-- 4. Entity: AIRCRAFT
CREATE TABLE AIRCRAFT (
    msn VARCHAR(20) PRIMARY KEY,
    tail_number VARCHAR(15) NOT NULL UNIQUE,
    model VARCHAR(50) NOT NULL,
    manufacture_year INT NOT NULL,
    capacity INT NOT NULL
);

-- 5. Weak Entity: FLIGHT_INSTANCE
CREATE TABLE FLIGHT_INSTANCE (
    flight_number VARCHAR(10) NOT NULL,
    flight_date DATE NOT NULL,
    msn VARCHAR(20) NOT NULL,
    actual_dept_time TIMESTAMP,
    actual_arr_time TIMESTAMP,
    flight_status VARCHAR(30) NOT NULL CHECK (flight_status IN ('On Time', 'Delayed', 'Cancelled', 'Landed', 'Boarding')),
    available_seats INT NOT NULL,
    PRIMARY KEY (flight_number, flight_date),
    FOREIGN KEY (flight_number) REFERENCES SCHEDULED_FLIGHT(flight_number) ON DELETE CASCADE,
    FOREIGN KEY (msn) REFERENCES AIRCRAFT(msn)
);

-- 6. Entity: FLIGHT_CREW
CREATE TABLE FLIGHT_CREW (
    ame VARCHAR(15) PRIMARY KEY,
    national_id VARCHAR(15) NOT NULL UNIQUE,
    full_name VARCHAR(100) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    address VARCHAR(100) NOT NULL,
    hire_date DATE NOT NULL,
    primary_role VARCHAR(50) NOT NULL,
    mentor_ame VARCHAR(15),
    FOREIGN KEY (mentor_ame) REFERENCES FLIGHT_CREW(ame)
);

-- 7. Associative Entity / Junction: CREW_ASSIGNMENT
CREATE TABLE CREW_ASSIGNMENT (
    flight_number VARCHAR(10) NOT NULL,
    flight_date DATE NOT NULL,
    ame VARCHAR(15) NOT NULL,
    flight_role VARCHAR(50) NOT NULL,
    PRIMARY KEY (flight_number, flight_date, ame),
    FOREIGN KEY (flight_number, flight_date) REFERENCES FLIGHT_INSTANCE(flight_number, flight_date) ON DELETE CASCADE,
    FOREIGN KEY (ame) REFERENCES FLIGHT_CREW(ame) ON DELETE CASCADE
);

-- 8. Entity: PASSENGER
CREATE TABLE PASSENGER (
    passport_number VARCHAR(20) PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    nationality VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone_number VARCHAR(20) NOT NULL
);

-- 9. Associative Entity / Booking: TICKET_BOOKING
CREATE TABLE TICKET_BOOKING (
    pnr VARCHAR(6) PRIMARY KEY,
    flight_number VARCHAR(10) NOT NULL,
    flight_date DATE NOT NULL,
    passport_number VARCHAR(20) NOT NULL,
    seat_number VARCHAR(10) NOT NULL,
    seat_class VARCHAR(20) NOT NULL CHECK (seat_class IN ('Economy', 'Premium Economy', 'Business', 'First')),
    price_eur DECIMAL(8, 2) NOT NULL,
    baggage_weight_kg DECIMAL(5, 2) NOT NULL,
    FOREIGN KEY (flight_number, flight_date) REFERENCES FLIGHT_INSTANCE(flight_number, flight_date) ON DELETE CASCADE,
    FOREIGN KEY (passport_number) REFERENCES PASSENGER(passport_number) ON DELETE CASCADE
);"""

    return Scenario(
        id="airline_management",
        title="Airline Management & Flight Operations System",
        subtitle="Entity-Relationship Modeling for Airports, Routes, Flight Instances, Aircraft, Crew & Bookings",
        course_tag="Databases (Progress Test 2025-2026 - Topic 3)",
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
