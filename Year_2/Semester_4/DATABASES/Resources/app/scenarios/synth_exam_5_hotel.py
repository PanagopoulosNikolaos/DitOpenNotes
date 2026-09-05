"""Hotel Resort Management case study scenario module.

Contains the complete parsed and modeled ER analysis for the International Hotel Resorts Group
(Resort Units, Rooms, Staff, Guests, Bookings, Inspections, Extra Services),
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


def createHotelManagementScenario() -> Scenario:
    """Constructs and returns the Hotel Resort Management database scenario.

    Returns:
        Scenario: Fully populated scenario instance.
    """
    # 1. Text Paragraphs with Interactive Segments
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="An international luxury hotel resort chain is developing a unified database system to manage its "),
                TextSegment(
                    text="hotel properties / resort units",
                    is_highlight=True,
                    category="entity",
                    tag_label="ENTITY",
                    badge_class="badge-entity-strong",
                    tooltip="Strong Entity: Autonomous hotel resort property with unique Hotel ID.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="rooms",
                    is_highlight=True,
                    category="entity",
                    tag_label="WEAK ENTITY",
                    badge_class="badge-entity-weak",
                    tooltip="Weak Entity: Hotel room identified only in combination with the Hotel ID.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="hotel staff",
                    is_highlight=True,
                    category="entity",
                    tag_label="ENTITY",
                    badge_class="badge-entity-strong",
                    tooltip="Strong Entity: Hotel employee with unique Employee ID (AMY).",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="guests",
                    is_highlight=True,
                    category="entity",
                    tag_label="ENTITY",
                    badge_class="badge-entity-strong",
                    tooltip="Strong Entity: Natural person guest with passport or national ID number.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="bookings / reservations",
                    is_highlight=True,
                    category="entity",
                    tag_label="ENTITY",
                    badge_class="badge-entity-strong",
                    tooltip="Strong Entity: Stay reservation with unique Booking ID.",
                ),
                TextSegment(text=" and "),
                TextSegment(
                    text="extra guest services",
                    is_highlight=True,
                    category="entity",
                    tag_label="ENTITY",
                    badge_class="badge-entity-strong",
                    tooltip="Strong Entity: Extra resort amenity service with unique Service ID.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color=None,
        ),
        Paragraph(
            segments=[
                TextSegment(text="1. <strong>Hotel Properties (Resorts):</strong> Each hotel property has a "),
                TextSegment(
                    text="unique Hotel ID (e.g., HTL01)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Primary Key: Unique hotel property identifier.",
                ),
                TextSegment(text=", a "),
                TextSegment(
                    text="commercial property name (e.g., 'Aegean Grand Resort')",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Candidate Key: Unique resort brand name.",
                ),
                TextSegment(text=", "),
                TextSegment(text="star rating (1 to 5 stars)", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="geographic region / island", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="city", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="street address", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=" and "),
                TextSegment(text="official contact email", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=". Each resort offers a range of "),
                TextSegment(
                    text="amenities and facilities ('Infinity Pool', 'Spa', 'Tennis Court')",
                    is_highlight=True,
                    category="attr",
                    tag_label="MULTIVALUED",
                    badge_class="badge-attr-multi",
                    tooltip="Multivalued Attribute: Extracted to relational table HOTEL_AMENITY.",
                ),
                TextSegment(text=" recorded as an amenity list. Each hotel is "),
                TextSegment(
                    text="managed by a General Manager",
                    is_highlight=True,
                    category="rel",
                    tag_label="RELATIONSHIP 1:1",
                    badge_class="badge-rel-11",
                    tooltip="1:1 Relationship (MANAGES): Total participation for Hotel, partial for Employee.",
                ),
                TextSegment(text=", for whom the "),
                TextSegment(
                    text="appointment start date",
                    is_highlight=True,
                    category="attr",
                    tag_label="REL ATTRIBUTE",
                    badge_class="badge-attr-simple",
                    tooltip="Relationship Attribute: Stored in HOTEL table.",
                ),
                TextSegment(text=" is recorded."),
            ],
            accent_border_color="border-blue-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="2. <strong>Rooms:</strong> Each hotel features multiple guest rooms. Each room is identified by its "),
                TextSegment(
                    text="Room Number (e.g., 101, 204), which is unique only within the specific hotel property",
                    is_highlight=True,
                    category="key",
                    tag_label="PARTIAL KEY",
                    badge_class="badge-key-partial",
                    tooltip="Partial Key (Discriminator): Identifies the room only in combination with the Hotel ID.",
                ),
                TextSegment(text=". For each room, the following are recorded: the "),
                TextSegment(text="floor level", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="room category type ('Standard Double', 'Deluxe Suite', 'Family Villa')", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="maximum guest capacity", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="base nightly rate", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=" and the "),
                TextSegment(text="view orientation ('Sea View', 'Garden View')", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=". "),
                TextSegment(
                    text="A room cannot exist without its corresponding hotel property",
                    is_highlight=True,
                    category="entity",
                    tag_label="WEAK ENTITY",
                    badge_class="badge-entity-weak",
                    tooltip="Existential Dependency: Identifying owner entity is HOTEL.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-amber-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="3. <strong>Guests:</strong> For each guest, the following are recorded: the "),
                TextSegment(
                    text="unique Passport Number or National ID",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Primary Key: Unique travel identification document.",
                ),
                TextSegment(text=", the "),
                TextSegment(text="full name", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="nationality", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="date of birth", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="residential address", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(
                    text="primary email",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Candidate Key: Unique guest contact email.",
                ),
                TextSegment(text=" and "),
                TextSegment(text="accumulated loyalty reward points", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=". A guest may provide "),
                TextSegment(
                    text="multiple contact telephone numbers",
                    is_highlight=True,
                    category="attr",
                    tag_label="MULTIVALUED",
                    badge_class="badge-attr-multi",
                    tooltip="Multivalued Attribute: Stored in relational table GUEST_PHONE.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-purple-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="4. <strong>Bookings:</strong> A guest can make bookings for one or more rooms. Each booking receives a "),
                TextSegment(
                    text="unique Booking Reference ID",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Primary Key: Unique reservation reference code.",
                ),
                TextSegment(text=", the "),
                TextSegment(text="booking date", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="scheduled check-in date", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="scheduled check-out date", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="number of adults and children", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="booking status ('Confirmed', 'Checked-in', 'Completed', 'Cancelled')", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=" and the "),
                TextSegment(text="agreed total stay cost", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=". Each booking "),
                TextSegment(
                    text="pertains to a specific guest",
                    is_highlight=True,
                    category="rel",
                    tag_label="RELATIONSHIP 1:N",
                    badge_class="badge-rel-1n",
                    tooltip="1:N Relationship (MAKES_BOOKING): A guest has multiple bookings, each booking belongs to one guest.",
                ),
                TextSegment(text=" and "),
                TextSegment(
                    text="reserves a specific room in a hotel for the specified duration",
                    is_highlight=True,
                    category="rel",
                    tag_label="RELATIONSHIP 1:N",
                    badge_class="badge-rel-1n",
                    tooltip="1:N Relationship (RESERVES_ROOM): A room hosts multiple bookings across different date periods.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-emerald-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="5. <strong>Staff & Room Inspections:</strong> For each employee, the following are recorded: the "),
                TextSegment(
                    text="Employee ID (AMY)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Primary Key: Unique staff employee registration number.",
                ),
                TextSegment(text=", the "),
                TextSegment(text="full name", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="job role/department (Housekeeping, Maintenance, Reception, Chef)", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="monthly salary", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=" and the "),
                TextSegment(text="phone number", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=". Each employee "),
                TextSegment(
                    text="works at a specific hotel property",
                    is_highlight=True,
                    category="rel",
                    tag_label="RELATIONSHIP 1:N",
                    badge_class="badge-rel-1n",
                    tooltip="1:N Relationship (EMPLOYS): A hotel property employs multiple staff members.",
                ),
                TextSegment(text=". In addition, housekeeping and maintenance staff "),
                TextSegment(
                    text="conduct inspections and cleaning of rooms",
                    is_highlight=True,
                    category="rel",
                    tag_label="RELATIONSHIP N:M",
                    badge_class="badge-rel-nm",
                    tooltip="N:M Relationship (ROOM_INSPECTION): Implemented via junction table ROOM_INSPECTION.",
                ),
                TextSegment(text=". For each inspection task, the "),
                TextSegment(
                    text="inspection date and time",
                    is_highlight=True,
                    category="attr",
                    tag_label="REL ATTRIBUTE",
                    badge_class="badge-attr-simple",
                    tooltip="Relationship Attribute: Room inspection timestamp.",
                ),
                TextSegment(text=", the "),
                TextSegment(
                    text="room readiness status",
                    is_highlight=True,
                    category="attr",
                    tag_label="REL ATTRIBUTE",
                    badge_class="badge-attr-simple",
                    tooltip="Relationship Attribute: 'Ready', 'Under Cleaning', 'Out of Order'.",
                ),
                TextSegment(text=" and "),
                TextSegment(
                    text="maintenance/damage observations",
                    is_highlight=True,
                    category="attr",
                    tag_label="REL ATTRIBUTE",
                    badge_class="badge-attr-simple",
                    tooltip="Relationship Attribute: Documentation of technical defects.",
                ),
                TextSegment(text=" are recorded."),
            ],
            accent_border_color="border-rose-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="6. <strong>Extra Services & Charges:</strong> The resort offers extra chargeable services (e.g., 'Aromatherapy Massage', 'Day Cruise', 'A La Carte Dinner'). Each service has a "),
                TextSegment(
                    text="unique service code",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Primary Key: Unique service catalog code.",
                ),
                TextSegment(text=", a "),
                TextSegment(text="description", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=" and a "),
                TextSegment(text="fixed unit price", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=". During a booking stay, "),
                TextSegment(
                    text="guests can utilize multiple extra services",
                    is_highlight=True,
                    category="rel",
                    tag_label="RELATIONSHIP N:M",
                    badge_class="badge-rel-nm",
                    tooltip="N:M Relationship (SERVICE_CHARGE): Junction table between Booking and Extra Service.",
                ),
                TextSegment(text=". For each service charge under a booking, the "),
                TextSegment(
                    text="delivery date and time",
                    is_highlight=True,
                    category="attr",
                    tag_label="REL ATTRIBUTE",
                    badge_class="badge-attr-simple",
                    tooltip="Relationship Attribute: Timestamp of service provision.",
                ),
                TextSegment(text=", the "),
                TextSegment(
                    text="quantity",
                    is_highlight=True,
                    category="attr",
                    tag_label="REL ATTRIBUTE",
                    badge_class="badge-attr-simple",
                    tooltip="Relationship Attribute: Quantity of service units consumed.",
                ),
                TextSegment(text=" and the "),
                TextSegment(
                    text="total billed charge amount",
                    is_highlight=True,
                    category="attr",
                    tag_label="REL ATTRIBUTE",
                    badge_class="badge-attr-simple",
                    tooltip="Relationship Attribute: Final charged amount on booking folio.",
                ),
                TextSegment(text=" are recorded."),
            ],
            accent_border_color="border-cyan-500",
        ),
    ]

    # 2. Detailed Entities List
    entities = [
        Entity(
            name="HOTEL",
            entity_type="Strong Entity",
            is_weak=False,
            owner_entity=None,
            justification="Autonomous hospitality property unit with unique Hotel ID and operational independence.",
            attributes=[
                Attribute("hotel_id", "Simple / Single-valued", is_pk=True, notes="Unique hotel unit code (PK)"),
                Attribute("property_name", "Simple / Single-valued", is_candidate=True, notes="Commercial resort trade name (Candidate Key)"),
                Attribute("star_rating", "Simple / Single-valued", notes="Star rating classification (1-5)"),
                Attribute("geographic_region", "Simple / Single-valued", notes="Geographic area / island"),
                Attribute("city", "Simple / Single-valued", notes="Headquarters city"),
                Attribute("address", "Simple / Single-valued", notes="Street and number"),
                Attribute("email", "Simple / Single-valued", notes="Official contact email"),
                Attribute("amenities", "Multivalued", notes="Resort amenities list (Table HOTEL_AMENITY)"),
            ],
        ),
        Entity(
            name="ROOM",
            entity_type="Weak Entity",
            is_weak=True,
            owner_entity="HOTEL",
            justification="Weak entity. Room number repeats across different hotels and requires Hotel ID for complete identification.",
            attributes=[
                Attribute("room_number", "Simple / Single-valued", is_partial=True, notes="Partial Key (Discriminator) within the property"),
                Attribute("floor", "Simple / Single-valued", notes="Floor level number"),
                Attribute("room_type", "Simple / Single-valued", notes="Type ('Standard Double', 'Deluxe Suite', 'Family Villa')"),
                Attribute("capacity", "Simple / Single-valued", notes="Maximum guest occupancy capacity"),
                Attribute("base_price", "Simple / Single-valued", notes="Base nightly rate"),
                Attribute("view_type", "Simple / Single-valued", notes="Orientation ('Sea View', 'Garden View')"),
            ],
        ),
        Entity(
            name="GUEST",
            entity_type="Strong Entity",
            is_weak=False,
            owner_entity=None,
            justification="Natural person customer with unique passport or national identity card number.",
            attributes=[
                Attribute("passport_id", "Simple / Single-valued", is_pk=True, notes="Passport or National ID Number (PK)"),
                Attribute("full_name", "Simple / Single-valued", notes="Guest full name"),
                Attribute("nationality", "Simple / Single-valued", notes="Country of citizenship"),
                Attribute("birth_date", "Simple / Single-valued", notes="Date of birth"),
                Attribute("address", "Simple / Single-valued", notes="Permanent residential address"),
                Attribute("email", "Simple / Single-valued", is_candidate=True, notes="Primary email (Candidate Key)"),
                Attribute("loyalty_points", "Simple / Single-valued", notes="Accumulated loyalty reward points"),
                Attribute("phones", "Multivalued", notes="Multiple contact phone numbers (Table GUEST_PHONE)"),
            ],
        ),
        Entity(
            name="BOOKING",
            entity_type="Strong Entity",
            is_weak=False,
            owner_entity=None,
            justification="Autonomous stay reservation transaction with unique Booking ID.",
            attributes=[
                Attribute("booking_id", "Simple / Single-valued", is_pk=True, notes="Unique booking reference code (PK)"),
                Attribute("booking_date", "Simple / Single-valued", notes="Reservation creation date"),
                Attribute("check_in", "Simple / Single-valued", notes="Scheduled arrival date"),
                Attribute("check_out", "Simple / Single-valued", notes="Scheduled departure date"),
                Attribute("num_adults", "Simple / Single-valued", notes="Number of adults"),
                Attribute("num_children", "Simple / Single-valued", notes="Number of children"),
                Attribute("booking_status", "Simple / Single-valued", notes="Status ('Confirmed', 'Checked-in', 'Completed', 'Cancelled')"),
                Attribute("total_cost", "Simple / Single-valued", notes="Total accommodation cost"),
            ],
        ),
        Entity(
            name="EMPLOYEE",
            entity_type="Strong Entity",
            is_weak=False,
            owner_entity=None,
            justification="Hotel resort group employee with unique Employee ID (AMY).",
            attributes=[
                Attribute("amy", "Simple / Single-valued", is_pk=True, notes="Employee Registration Number (PK)"),
                Attribute("full_name", "Simple / Single-valued", notes="Employee full name"),
                Attribute("specialty", "Simple / Single-valued", notes="Role ('Housekeeping', 'Maintenance', 'Reception', 'Chef')"),
                Attribute("salary", "Simple / Single-valued", notes="Monthly gross salary"),
                Attribute("phone", "Simple / Single-valued", notes="Contact telephone number"),
            ],
        ),
        Entity(
            name="EXTRA_SERVICE",
            entity_type="Strong Entity",
            is_weak=False,
            owner_entity=None,
            justification="Catalog of extra available services (Spa, Tours, Fine Dining) with unique Service ID.",
            attributes=[
                Attribute("service_id", "Simple / Single-valued", is_pk=True, notes="Unique service catalog code (PK)"),
                Attribute("description", "Simple / Single-valued", notes="Service descriptive summary"),
                Attribute("unit_price", "Simple / Single-valued", notes="Standard unit charge price"),
            ],
        ),
    ]

    # 3. Relationship Attributes
    relationship_attributes = [
        RelationshipAttribute(
            name="appointment_date",
            relationship_name="MANAGES (HOTEL - EMPLOYEE)",
            justification="Date on which the General Manager assumed management duties at the property.",
        ),
        RelationshipAttribute(
            name="inspection_date",
            relationship_name="ROOM_INSPECTION (ROOM - EMPLOYEE)",
            justification="Timestamp of room inspection and verification.",
        ),
        RelationshipAttribute(
            name="readiness_status",
            relationship_name="ROOM_INSPECTION (ROOM - EMPLOYEE)",
            justification="Readiness status ('Ready', 'Under Cleaning', 'Out of Order', 'Repaired').",
        ),
        RelationshipAttribute(
            name="damage_observations",
            relationship_name="ROOM_INSPECTION (ROOM - EMPLOYEE)",
            justification="Technical notes and maintenance issues requiring remediation.",
        ),
        RelationshipAttribute(
            name="delivery_date",
            relationship_name="SERVICE_CHARGE (BOOKING - EXTRA_SERVICE)",
            justification="Timestamp when the extra service was rendered to the guest.",
        ),
        RelationshipAttribute(
            name="quantity",
            relationship_name="SERVICE_CHARGE (BOOKING - EXTRA_SERVICE)",
            justification="Number of units/quantity of service consumed.",
        ),
        RelationshipAttribute(
            name="total_amount",
            relationship_name="SERVICE_CHARGE (BOOKING - EXTRA_SERVICE)",
            justification="Calculated total charge amount billed to the stay folio.",
        ),
    ]

    # 4. Keys Analysis Table
    keys_analysis = [
        KeyAnalysisRow(
            entity_name="HOTEL",
            key_count="2 Candidate",
            key_types="Candidate: {hotel_id}, {property_name}",
            final_pk_selection="hotel_id",
            justification="Compact, invariant code optimal for Foreign Key references.",
        ),
        KeyAnalysisRow(
            entity_name="ROOM",
            key_count="Weak (1 Partial)",
            key_types="Partial Key: {room_number}",
            final_pk_selection="(hotel_id, room_number)",
            justification="Composite primary key: Hotel Foreign Key + room number.",
            is_weak=True,
        ),
        KeyAnalysisRow(
            entity_name="GUEST",
            key_count="2 Candidate",
            key_types="Candidate: {passport_id}, {email}",
            final_pk_selection="passport_id",
            justification="Official government travel document identifying international resort guests.",
        ),
        KeyAnalysisRow(
            entity_name="BOOKING",
            key_count="1 Candidate",
            key_types="Candidate: {booking_id}",
            final_pk_selection="booking_id",
            justification="Unique booking reference code generated by the Central Reservation System (CRS).",
        ),
        KeyAnalysisRow(
            entity_name="EMPLOYEE",
            key_count="1 Candidate",
            key_types="Candidate: {amy}",
            final_pk_selection="amy",
            justification="Internal personnel staff registration number.",
        ),
        KeyAnalysisRow(
            entity_name="EXTRA_SERVICE",
            key_count="1 Candidate",
            key_types="Candidate: {service_id}",
            final_pk_selection="service_id",
            justification="Unique service price-list catalog code.",
        ),
    ]

    # 5. Relationships List
    relationships = [
        Relationship(
            letter_id="a",
            name="MANAGES",
            connected_entities="HOTEL <-> EMPLOYEE",
            cardinality="1:1",
            participation="Total for Hotel (1,1), Partial for Employee (0,1)",
            relationship_type="Regular Relationship",
            attributes=["appointment_date"],
            justification="Each hotel is managed by one General Manager. An employee can manage at most one hotel property.",
        ),
        Relationship(
            letter_id="b",
            name="EMPLOYS",
            connected_entities="HOTEL <-> EMPLOYEE",
            cardinality="1:N",
            participation="Total for Employee (1,1), Total for Hotel (1,N)",
            relationship_type="Regular Relationship",
            attributes=[],
            justification="Each employee works at one specific hotel property. Each property employs multiple staff members.",
        ),
        Relationship(
            letter_id="c",
            name="HAS_ROOMS",
            connected_entities="HOTEL <-> ROOM",
            cardinality="1:N",
            participation="Total for Room (1,1), Total for Hotel (1,N)",
            relationship_type="Identifying Relationship",
            attributes=[],
            justification="Identifying relationship of weak entity ROOM from identifying owner HOTEL.",
        ),
        Relationship(
            letter_id="d",
            name="MAKES_BOOKING",
            connected_entities="GUEST <-> BOOKING",
            cardinality="1:N",
            participation="Total for Booking (1,1), Partial for Guest (0,N)",
            relationship_type="Regular Relationship",
            attributes=[],
            justification="Each booking belongs to one guest. A guest may make multiple bookings.",
        ),
        Relationship(
            letter_id="e",
            name="RESERVES_ROOM",
            connected_entities="ROOM <-> BOOKING",
            cardinality="1:N",
            participation="Total for Booking (1,1), Partial for Room (0,N)",
            relationship_type="Regular Relationship",
            attributes=[],
            justification="Each booking reserves a specific room. A room is reserved in multiple bookings across distinct time intervals.",
        ),
        Relationship(
            letter_id="f",
            name="ROOM_INSPECTION",
            connected_entities="ROOM <-> EMPLOYEE",
            cardinality="N:M",
            participation="Partial for Room (0,N), Partial for Employee (0,N)",
            relationship_type="Associative Entity (Junction)",
            attributes=["inspection_date", "readiness_status", "damage_observations"],
            justification="Housekeeping and maintenance staff perform inspections across multiple rooms, and each room is inspected repeatedly.",
        ),
        Relationship(
            letter_id="g",
            name="SERVICE_USAGE",
            connected_entities="BOOKING <-> EXTRA_SERVICE",
            cardinality="N:M",
            participation="Partial for Booking (0,N), Partial for Extra Service (0,N)",
            relationship_type="Associative Entity (Junction)",
            attributes=["delivery_date", "quantity", "total_amount"],
            justification="A booking may be charged with multiple extra services, and an extra service is billed to multiple bookings.",
        ),
    ]

    # 6. Design Assumptions
    assumptions = [
        "The General Manager is registered in table EMPLOYEE and linked via manager_amy in HOTEL with a UNIQUE constraint.",
        "Each booking reserves one specific room. If a guest requires multiple rooms, separate bookings are generated.",
        "Hotel amenities and guest phone numbers are stored in separate 1:N tables to maintain First Normal Form (1NF).",
        "Service charges are linked to the booking ID for unified billing settlement at check-out.",
    ]

    # 7. ER Diagram Tables
    er_tables = [
        ERTable(
            id="t-resort",
            label="HOTEL",
            x=50,
            y=50,
            attrs=[
                ERTableAttr("hotel_id", pk=True),
                ERTableAttr("property_name"),
                ERTableAttr("star_rating"),
                ERTableAttr("geographic_region"),
                ERTableAttr("city"),
                ERTableAttr("address"),
                ERTableAttr("email"),
                ERTableAttr("manager_amy", fk=True),
                ERTableAttr("appointment_date"),
            ],
        ),
        ERTable(
            id="t-amenities",
            label="HOTEL_AMENITY",
            x=50,
            y=370,
            attrs=[
                ERTableAttr("hotel_id", pk=True, fk=True),
                ERTableAttr("amenity_name", pk=True),
            ],
        ),
        ERTable(
            id="t-room",
            label="ROOM",
            x=450,
            y=50,
            attrs=[
                ERTableAttr("hotel_id", pk=True, fk=True),
                ERTableAttr("room_number", pk=True),
                ERTableAttr("floor"),
                ERTableAttr("room_type"),
                ERTableAttr("capacity"),
                ERTableAttr("base_price"),
                ERTableAttr("view_type"),
            ],
        ),
        ERTable(
            id="t-inspection",
            label="ROOM_INSPECTION",
            x=450,
            y=340,
            attrs=[
                ERTableAttr("hotel_id", pk=True, fk=True),
                ERTableAttr("room_number", pk=True, fk=True),
                ERTableAttr("amy", pk=True, fk=True),
                ERTableAttr("inspection_date", pk=True),
                ERTableAttr("readiness_status"),
                ERTableAttr("damage_observations"),
            ],
        ),
        ERTable(
            id="t-employee",
            label="EMPLOYEE",
            x=850,
            y=340,
            attrs=[
                ERTableAttr("amy", pk=True),
                ERTableAttr("full_name"),
                ERTableAttr("specialty"),
                ERTableAttr("salary"),
                ERTableAttr("phone"),
                ERTableAttr("hotel_id", fk=True),
            ],
        ),
        ERTable(
            id="t-guest",
            label="GUEST",
            x=850,
            y=50,
            attrs=[
                ERTableAttr("passport_id", pk=True),
                ERTableAttr("full_name"),
                ERTableAttr("nationality"),
                ERTableAttr("birth_date"),
                ERTableAttr("address"),
                ERTableAttr("email"),
                ERTableAttr("loyalty_points"),
            ],
        ),
        ERTable(
            id="t-guest-phone",
            label="GUEST_PHONE",
            x=850,
            y=600,
            attrs=[
                ERTableAttr("passport_id", pk=True, fk=True),
                ERTableAttr("phone_number", pk=True),
            ],
        ),
        ERTable(
            id="t-booking",
            label="BOOKING",
            x=450,
            y=600,
            attrs=[
                ERTableAttr("booking_id", pk=True),
                ERTableAttr("booking_date"),
                ERTableAttr("check_in"),
                ERTableAttr("check_out"),
                ERTableAttr("num_adults"),
                ERTableAttr("num_children"),
                ERTableAttr("booking_status"),
                ERTableAttr("total_cost"),
                ERTableAttr("passport_id", fk=True),
                ERTableAttr("hotel_id", fk=True),
                ERTableAttr("room_number", fk=True),
            ],
        ),
        ERTable(
            id="t-service",
            label="EXTRA_SERVICE",
            x=50,
            y=500,
            attrs=[
                ERTableAttr("service_id", pk=True),
                ERTableAttr("description"),
                ERTableAttr("unit_price"),
            ],
        ),
        ERTable(
            id="t-service-charge",
            label="SERVICE_CHARGE",
            x=50,
            y=660,
            attrs=[
                ERTableAttr("booking_id", pk=True, fk=True),
                ERTableAttr("service_id", pk=True, fk=True),
                ERTableAttr("delivery_date", pk=True),
                ERTableAttr("quantity"),
                ERTableAttr("total_amount"),
            ],
        ),
    ]

    # 8. ER Diagram Edges
    er_edges = [
        # Resort directs Employee (1:1)
        EREdge("M 310 80 L 850 360", "start-one-mandatory", "end-one-optional", "Manages (1:1)", 550, 240),
        # Resort employs Employees (1:N)
        EREdge("M 310 120 L 850 400", "start-one-mandatory", "end-many-mandatory", "Employs (1:N)", 550, 280),
        # Resort has Rooms (1:N identifying)
        EREdge("M 310 100 L 450 100", "start-one-mandatory", "end-many-mandatory", "Has Rooms (1:N)", 380, 90),
        # Resort has Amenities (1:N multi-value)
        EREdge("M 180 350 L 180 370", "start-one-mandatory", "end-many-mandatory", "Amenities (1:N)", 195, 360),
        # Room to Inspection (1:N)
        EREdge("M 580 294 L 580 340", "start-one-optional", "end-many-mandatory", "Inspection (1:N)", 595, 315),
        # Employee to Inspection (1:N)
        EREdge("M 850 370 L 710 370", "start-one-optional", "end-many-mandatory", "Performs (1:N)", 780, 360),
        # Room to Booking (1:N)
        EREdge("M 450 170 L 400 170 L 400 650 L 450 650", "start-one-optional", "end-many-mandatory", "Reserves (1:N)", 385, 410),
        # Guest to Booking (1:N)
        EREdge("M 850 200 L 710 650", "start-one-optional", "end-many-mandatory", "Books (1:N)", 780, 520),
        # Guest to Phone (1:N)
        EREdge("M 980 294 L 980 600", "start-one-optional", "end-many-mandatory", "Phone (1:N)", 995, 460),
        # Booking to Service Charge (1:N)
        EREdge("M 450 680 L 310 680", "start-one-optional", "end-many-mandatory", "Charges (1:N)", 380, 670),
        # Service to Service Charge (1:N)
        EREdge("M 180 632 L 180 660", "start-one-optional", "end-many-mandatory", "Provides (1:N)", 195, 645),
    ]

    # 9. Relational Conversion Justifications
    relational_justifications = [
        RelationalJustification(
            title="1. Conversion of Strong Entities (HOTEL, GUEST, BOOKING, EMPLOYEE, EXTRA_SERVICE)",
            color_class="border-blue-500",
            description="Each strong entity is converted into an independent table with its primary key selected from candidate keys (hotel_id, passport_id, booking_id, amy, service_id).",
        ),
        RelationalJustification(
            title="2. Conversion of Weak Entity (ROOM)",
            color_class="border-red-500",
            description="Table ROOM receives hotel_id from identifying owner entity HOTEL as Foreign Key. The primary key is composite: PRIMARY KEY (hotel_id, room_number) with ON DELETE CASCADE.",
        ),
        RelationalJustification(
            title="3. Conversion of 1:1 and 1:N Relationships (MANAGES, EMPLOYS, MAKES_BOOKING, RESERVES_ROOM)",
            color_class="border-emerald-500",
            description="In 1:1 relationship MANAGES, manager_amy is placed in HOTEL with a UNIQUE constraint. In 1:N relationships, referencing keys (passport_id, composite hotel_id + room_number) are placed as Foreign Keys in BOOKING.",
        ),
        RelationalJustification(
            title="4. Conversion of N:M Relationships (ROOM_INSPECTION, SERVICE_CHARGE)",
            color_class="border-amber-500",
            description="Junction tables ROOM_INSPECTION (composite PK: hotel_id, room_number, amy, inspection_date) and SERVICE_CHARGE (composite PK: booking_id, service_id, delivery_date) are created.",
        ),
        RelationalJustification(
            title="5. Conversion of Multivalued Attributes (AMENITIES, PHONES)",
            color_class="border-purple-500",
            description="Multivalued attributes are stored in tables HOTEL_AMENITY (hotel_id, amenity_name) and GUEST_PHONE (passport_id, phone_number) with Foreign Keys and ON DELETE CASCADE.",
        ),
    ]

    # 10. Complete Production SQL DDL
    sql_ddl = """-- ==========================================================
-- PostgreSQL / MySQL Relational Schema for Hotel Resort System
-- Case Study: Exam Paper 5 (Hotel Resort Management & Services)
-- ==========================================================

-- 1. Entity: EMPLOYEE (Pre-created for foreign keys)
CREATE TABLE EMPLOYEE (
    amy VARCHAR(15) PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    specialty VARCHAR(50) NOT NULL CHECK (specialty IN ('Housekeeping', 'Maintenance', 'Reception', 'Chef', 'Management')),
    salary DECIMAL(10, 2) NOT NULL CHECK (salary > 0),
    phone VARCHAR(20) NOT NULL,
    hotel_id VARCHAR(10) NOT NULL
);

-- 2. Entity: HOTEL
CREATE TABLE HOTEL (
    hotel_id VARCHAR(10) PRIMARY KEY,
    property_name VARCHAR(100) NOT NULL UNIQUE,
    star_rating INT NOT NULL CHECK (star_rating BETWEEN 1 AND 5),
    geographic_region VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL,
    address VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    manager_amy VARCHAR(15) NOT NULL UNIQUE,
    appointment_date DATE NOT NULL,
    FOREIGN KEY (manager_amy) REFERENCES EMPLOYEE(amy)
);

-- Add foreign key constraint for employee's workplace
ALTER TABLE EMPLOYEE
ADD CONSTRAINT fk_emp_hotel
FOREIGN KEY (hotel_id) REFERENCES HOTEL(hotel_id);

-- 3. Multi-valued Attribute: HOTEL_AMENITY
CREATE TABLE HOTEL_AMENITY (
    hotel_id VARCHAR(10) NOT NULL,
    amenity_name VARCHAR(100) NOT NULL,
    PRIMARY KEY (hotel_id, amenity_name),
    FOREIGN KEY (hotel_id) REFERENCES HOTEL(hotel_id) ON DELETE CASCADE
);

-- 4. Weak Entity: ROOM
CREATE TABLE ROOM (
    hotel_id VARCHAR(10) NOT NULL,
    room_number VARCHAR(10) NOT NULL,
    floor INT NOT NULL,
    room_type VARCHAR(50) NOT NULL CHECK (room_type IN ('Standard Double', 'Deluxe Suite', 'Family Villa', 'Superior Room')),
    capacity INT NOT NULL CHECK (capacity > 0),
    base_price DECIMAL(10, 2) NOT NULL CHECK (base_price > 0),
    view_type VARCHAR(50) NOT NULL CHECK (view_type IN ('Sea View', 'Garden View', 'Mountain View', 'Pool View')),
    PRIMARY KEY (hotel_id, room_number),
    FOREIGN KEY (hotel_id) REFERENCES HOTEL(hotel_id) ON DELETE CASCADE
);

-- 5. Entity: GUEST
CREATE TABLE GUEST (
    passport_id VARCHAR(20) PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    nationality VARCHAR(50) NOT NULL,
    birth_date DATE NOT NULL,
    address VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    loyalty_points INT DEFAULT 0 CHECK (loyalty_points >= 0)
);

-- 6. Multi-valued Attribute: GUEST_PHONE
CREATE TABLE GUEST_PHONE (
    passport_id VARCHAR(20) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    PRIMARY KEY (passport_id, phone_number),
    FOREIGN KEY (passport_id) REFERENCES GUEST(passport_id) ON DELETE CASCADE
);

-- 7. Entity: BOOKING
CREATE TABLE BOOKING (
    booking_id VARCHAR(20) PRIMARY KEY,
    booking_date DATE NOT NULL,
    check_in DATE NOT NULL,
    check_out DATE NOT NULL,
    num_adults INT NOT NULL CHECK (num_adults > 0),
    num_children INT DEFAULT 0 CHECK (num_children >= 0),
    booking_status VARCHAR(30) NOT NULL CHECK (booking_status IN ('Confirmed', 'Checked-in', 'Completed', 'Cancelled')),
    total_cost DECIMAL(10, 2) NOT NULL CHECK (total_cost >= 0),
    passport_id VARCHAR(20) NOT NULL,
    hotel_id VARCHAR(10) NOT NULL,
    room_number VARCHAR(10) NOT NULL,
    CHECK (check_out > check_in),
    FOREIGN KEY (passport_id) REFERENCES GUEST(passport_id) ON DELETE CASCADE,
    FOREIGN KEY (hotel_id, room_number) REFERENCES ROOM(hotel_id, room_number) ON DELETE RESTRICT
);

-- 8. Entity: EXTRA_SERVICE
CREATE TABLE EXTRA_SERVICE (
    service_id VARCHAR(15) PRIMARY KEY,
    description VARCHAR(150) NOT NULL,
    unit_price DECIMAL(8, 2) NOT NULL CHECK (unit_price >= 0)
);

-- 9. Junction Table: ROOM_INSPECTION (N:M)
CREATE TABLE ROOM_INSPECTION (
    hotel_id VARCHAR(10) NOT NULL,
    room_number VARCHAR(10) NOT NULL,
    amy VARCHAR(15) NOT NULL,
    inspection_date TIMESTAMP NOT NULL,
    readiness_status VARCHAR(30) NOT NULL CHECK (readiness_status IN ('Ready', 'Under Cleaning', 'Out of Order', 'Repaired')),
    damage_observations TEXT,
    PRIMARY KEY (hotel_id, room_number, amy, inspection_date),
    FOREIGN KEY (hotel_id, room_number) REFERENCES ROOM(hotel_id, room_number) ON DELETE CASCADE,
    FOREIGN KEY (amy) REFERENCES EMPLOYEE(amy) ON DELETE CASCADE
);

-- 10. Junction Table: SERVICE_CHARGE (N:M)
CREATE TABLE SERVICE_CHARGE (
    booking_id VARCHAR(20) NOT NULL,
    service_id VARCHAR(15) NOT NULL,
    delivery_date TIMESTAMP NOT NULL,
    quantity INT NOT NULL DEFAULT 1 CHECK (quantity > 0),
    total_amount DECIMAL(10, 2) NOT NULL CHECK (total_amount >= 0),
    PRIMARY KEY (booking_id, service_id, delivery_date),
    FOREIGN KEY (booking_id) REFERENCES BOOKING(booking_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES EXTRA_SERVICE(service_id)
);"""

    return Scenario(
        id="hotel_management",
        title="Hotel Resort Management System",
        subtitle="Entity-Relationship Modeling for Resort Units, Rooms, Guests, Bookings, Staff & Extra Services",
        course_tag="Databases (Progress Test 2025-2026 - Topic 5)",
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
