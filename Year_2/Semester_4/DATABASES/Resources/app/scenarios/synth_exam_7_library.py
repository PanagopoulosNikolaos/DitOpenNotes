"""Municipal Library Network case study scenario module.

Contains the complete parsed and modeled ER analysis for the Municipal Library Network
(Branches, Staff/Librarians, Book Titles, Authors, Physical Copies, Members, Loans & Reservations),
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


def createLibraryManagementScenario() -> Scenario:
    """Constructs and returns the Municipal Library Network database scenario.

    Returns:
        Scenario: Fully populated scenario instance.
    """
    # 1. Text Paragraphs with Interactive Segments
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="A metropolitan municipality is developing an integrated database information system for its public library branch network to manage "),
                TextSegment(
                    text="library branches",
                    is_highlight=True,
                    category="entity",
                    tag_label="ENTITY",
                    badge_class="badge-entity-strong",
                    tooltip="Strong Entity: Autonomous physical municipal library branch facility with unique Branch ID.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="bibliographic catalog titles",
                    is_highlight=True,
                    category="entity",
                    tag_label="ENTITY",
                    badge_class="badge-entity-strong",
                    tooltip="Strong Entity: Bibliographic book title / work uniquely identified by international standard ISBN.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="physical book copies",
                    is_highlight=True,
                    category="entity",
                    tag_label="WEAK ENTITY",
                    badge_class="badge-entity-weak",
                    tooltip="Weak Entity: Physical book inventory copy identified in conjunction with the title ISBN.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="reader members",
                    is_highlight=True,
                    category="entity",
                    tag_label="ENTITY",
                    badge_class="badge-entity-strong",
                    tooltip="Strong Entity: Registered library member with unique Membership Card Number.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="circulation loans",
                    is_highlight=True,
                    category="entity",
                    tag_label="ENTITY (TRANSACTION)",
                    badge_class="badge-entity-strong",
                    tooltip="Strong / Associative Entity (Transaction Entity): Physical copy checkout event by a registered member.",
                ),
                TextSegment(text=", and "),
                TextSegment(
                    text="hold reservations",
                    is_highlight=True,
                    category="entity",
                    tag_label="ENTITY (QUEUE)",
                    badge_class="badge-entity-strong",
                    tooltip="Strong / Associative Entity (Queue Entity): Title hold request placed by a member at a specified pickup branch.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color=None,
        ),
        Paragraph(
            segments=[
                TextSegment(text="1. <strong>Library Branches:</strong> Each library branch is characterized by a "),
                TextSegment(
                    text="unique Branch ID (e.g., 'LIB-01', 'LIB-02')",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Primary Key: Unique numerical or alphanumeric branch identifier.",
                ),
                TextSegment(text=", a "),
                TextSegment(
                    text="unique branch name (e.g., 'Central Municipal Library', 'Uptown Cultural Branch')",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Candidate Key: Official distinct name of the branch within the municipality.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="street address (street, number, postal code, neighborhood)",
                    is_highlight=True,
                    category="attr",
                    tag_label="COMPOSITE",
                    badge_class="badge-attr-composite",
                    tooltip="Composite Attribute: Decomposed into street, number, postal code, and neighborhood.",
                ),
                TextSegment(text=", "),
                TextSegment(text="phone number", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", and "),
                TextSegment(text="reader seating capacity", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=". Each branch operates on an established "),
                TextSegment(
                    text="weekly operating schedule (multiple operating days / hours)",
                    is_highlight=True,
                    category="attr",
                    tag_label="MULTI-VALUED",
                    badge_class="badge-attr-multi",
                    tooltip="Multi-Valued Attribute: Exported to the BRANCH_SCHEDULE relation.",
                ),
                TextSegment(text=". Each branch is "),
                TextSegment(
                    text="managed by a Chief Head Librarian",
                    is_highlight=True,
                    category="rel",
                    tag_label="1:1 RELATIONSHIP",
                    badge_class="badge-rel-11",
                    tooltip="1:1 Relationship (MANAGES): Total participation for Branch, partial for Librarian.",
                ),
                TextSegment(text=", for whom the "),
                TextSegment(
                    text="appointment start date",
                    is_highlight=True,
                    category="attr",
                    tag_label="RELATIONSHIP ATTRIBUTE",
                    badge_class="badge-attr-simple",
                    tooltip="Relationship Attribute: Stored within the LIBRARY_BRANCH relation.",
                ),
                TextSegment(text=" is recorded."),
            ],
            accent_border_color="border-blue-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="2. <strong>Book Titles & Authors:</strong> For each bibliographic title, the system records: the "),
                TextSegment(
                    text="unique international standard ISBN (International Standard Book Number)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Primary Key: Internationally unique ISBN identifier.",
                ),
                TextSegment(text=", the "),
                TextSegment(text="book title", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="publishing house", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="publication year", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="subject classification (e.g., 'Computer Science', 'European History')", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", and the "),
                TextSegment(text="total page count", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=". A book may be authored by "),
                TextSegment(
                    text="one or more authors (N:M Relationship)",
                    is_highlight=True,
                    category="rel",
                    tag_label="N:M RELATIONSHIP",
                    badge_class="badge-rel-nm",
                    tooltip="N:M Relationship (BOOK_AUTHORSHIP): A book title is authored by multiple authors and an author writes multiple titles.",
                ),
                TextSegment(text=". For each "),
                TextSegment(
                    text="author",
                    is_highlight=True,
                    category="entity",
                    tag_label="ENTITY",
                    badge_class="badge-entity-strong",
                    tooltip="Strong Entity: Individual writer / creator with unique author ID.",
                ),
                TextSegment(text=", the database tracks: the "),
                TextSegment(
                    text="unique Author ID",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Primary Key: Unique author registry identifier.",
                ),
                TextSegment(text=", the "),
                TextSegment(text="full name", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="nationality", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", and the "),
                TextSegment(text="birth year", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text="."),
            ],
            accent_border_color="border-amber-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="3. <strong>Physical Book Copies:</strong> Each branch maintains one or more physical copies of various books. Each physical copy is identified by a "),
                TextSegment(
                    text="unique barcode ID or sequential copy number within the specific ISBN",
                    is_highlight=True,
                    category="key",
                    tag_label="PARTIAL KEY",
                    badge_class="badge-key-partial",
                    tooltip="Partial Key: Sequential copy number (copy_number) that combined with ISBN forms the composite PK.",
                ),
                TextSegment(text=". For each copy, the system records: the "),
                TextSegment(text="physical shelf condition (e.g., 'Pristine', 'Good', 'Worn', 'Under Restoration')", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="current availability status ('Available', 'Checked Out', 'Reserved')", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="shelf location tag / call number", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", and the "),
                TextSegment(
                    text="branch where the copy is permanently housed",
                    is_highlight=True,
                    category="rel",
                    tag_label="1:N RELATIONSHIP",
                    badge_class="badge-rel-1n",
                    tooltip="1:N Relationship (HOUSES_COPY): Each physical copy belongs permanently to a specific branch collection.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-red-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="4. <strong>Library Members (Readers):</strong> For each registered member, the system maintains: the "),
                TextSegment(
                    text="unique Membership Card Number",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Primary Key: Unique reader card number.",
                ),
                TextSegment(text=", the "),
                TextSegment(
                    text="National Identity Card Number (ID / AFM)",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Candidate Key: Government-issued national identification number.",
                ),
                TextSegment(text=", the "),
                TextSegment(text="first name", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="last name", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="date of birth", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(
                    text="residential address (street, number, postal code, city)",
                    is_highlight=True,
                    category="attr",
                    tag_label="COMPOSITE",
                    badge_class="badge-attr-composite",
                    tooltip="Composite Attribute: Decomposed into street, street number, postal code, and city.",
                ),
                TextSegment(text=", the "),
                TextSegment(
                    text="email address",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Candidate Key: Unique email contact address.",
                ),
                TextSegment(text=", the "),
                TextSegment(text="registration date", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", and the "),
                TextSegment(text="membership status ('Active', 'Suspended')", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=". A member may provide "),
                TextSegment(
                    text="multiple contact phone numbers",
                    is_highlight=True,
                    category="attr",
                    tag_label="MULTI-VALUED",
                    badge_class="badge-attr-multi",
                    tooltip="Multi-Valued Attribute: Exported to the MEMBER_PHONE relation.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-purple-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="5. <strong>Circulation Loans:</strong> Members may borrow available physical copies of books. For each loan transaction, the system records: a "),
                TextSegment(
                    text="unique Loan Reference ID",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Primary Key: Unique circulation loan transaction identifier.",
                ),
                TextSegment(text=", the "),
                TextSegment(text="checkout date", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="scheduled due date", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="actual return date (if returned)", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", and any "),
                TextSegment(
                    text="accrued late fine (calculated dynamically based on overdue days)",
                    is_highlight=True,
                    category="attr",
                    tag_label="DERIVED",
                    badge_class="badge-attr-derived",
                    tooltip="Derived Attribute: Computed dynamically from overdue return date delta.",
                ),
                TextSegment(text=". A copy "),
                TextSegment(
                    text="may be checked out to at most one member at any given time",
                    is_highlight=True,
                    category="rel",
                    tag_label="1:1 CONSTRAINT",
                    badge_class="badge-rel-11",
                    tooltip="Business Rule Constraint: A physical copy has at most one active checkout loan transaction concurrently.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-emerald-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="6. <strong>Hold Reservations:</strong> When all copies of a desired title (ISBN) are currently checked out, a member can submit a "),
                TextSegment(
                    text="reservation hold request for that title at a selected branch",
                    is_highlight=True,
                    category="rel",
                    tag_label="N:M RELATIONSHIP / ENTITY",
                    badge_class="badge-rel-nm",
                    tooltip="Associative Entity (RESERVATION): Interconnects Member, Book Title, and pickup Branch.",
                ),
                TextSegment(text=". For each reservation, the following are tracked: the "),
                TextSegment(
                    text="unique Reservation ID",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Primary Key: Unique hold request identifier.",
                ),
                TextSegment(text=", the "),
                TextSegment(text="submission date and time", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="queue priority order sequence", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", and the "),
                TextSegment(text="hold request status ('Pending', 'Member Notified', 'Fulfilled', 'Cancelled')", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text="."),
            ],
            accent_border_color="border-cyan-500",
        ),
    ]

    # 2. Complete Entity List with Detailed Attributes
    entities = [
        Entity(
            name="LIBRARY_BRANCH",
            entity_type="Strong Entity",
            is_weak=False,
            owner_entity=None,
            justification="Autonomous physical library facility with distinct municipal identity and unique Branch ID.",
            attributes=[
                Attribute("branch_id", "Simple / Single-valued", is_pk=True, notes="Unique branch identifier code (PK)."),
                Attribute("branch_name", "Simple / Single-valued", is_candidate=True, notes="Unique official branch name."),
                Attribute(
                    "address",
                    "Composite",
                    components=["street", "street_number", "postal_code", "neighborhood"],
                    notes="Complete postal street address of the branch facility.",
                ),
                Attribute("phone_number", "Simple / Single-valued", notes="Main branch contact phone number."),
                Attribute("seating_capacity", "Simple / Single-valued", notes="Maximum seated reader capacity in reading halls."),
                Attribute("branch_schedule", "Multi-valued", notes="Multiple operating days and hours (BRANCH_SCHEDULE table)."),
            ],
        ),
        Entity(
            name="LIBRARIAN",
            entity_type="Strong Entity",
            is_weak=False,
            owner_entity=None,
            justification="Staff member employed at a library branch who may also serve as branch head director.",
            attributes=[
                Attribute("staff_id", "Simple / Single-valued", is_pk=True, notes="Unique employee registry number (PK)."),
                Attribute("national_id", "Simple / Single-valued", is_candidate=True, notes="Government-issued national identity card number."),
                Attribute("first_name", "Simple / Single-valued", notes="First name of staff member."),
                Attribute("last_name", "Simple / Single-valued", notes="Last name of staff member."),
                Attribute("specialty", "Simple / Single-valued", notes="Professional specialization (e.g., 'Archivist', 'Cataloger', 'Head Librarian')."),
                Attribute("phone_number", "Simple / Single-valued", notes="Direct contact telephone number."),
            ],
        ),
        Entity(
            name="BOOK_TITLE",
            entity_type="Strong Entity",
            is_weak=False,
            owner_entity=None,
            justification="Abstract intellectual work/book catalog entry uniquely identified worldwide by standard ISBN.",
            attributes=[
                Attribute("isbn", "Simple / Single-valued", is_pk=True, notes="International Standard Book Number (ISBN-13) (PK)."),
                Attribute("title", "Simple / Single-valued", notes="Full title of the bibliographic work."),
                Attribute("publisher", "Simple / Single-valued", notes="Publishing house name."),
                Attribute("publication_year", "Simple / Single-valued", notes="Year of publication."),
                Attribute("subject_category", "Simple / Single-valued", notes="Subject thematic classification (e.g., 'Computer Science', 'History')."),
                Attribute("page_count", "Simple / Single-valued", notes="Total numbered page count."),
            ],
        ),
        Entity(
            name="AUTHOR",
            entity_type="Strong Entity",
            is_weak=False,
            owner_entity=None,
            justification="Individual creative author with independent legal and biographical identity.",
            attributes=[
                Attribute("author_id", "Simple / Single-valued", is_pk=True, notes="Unique author identifier code (PK)."),
                Attribute("full_name", "Simple / Single-valued", notes="Full author name."),
                Attribute("nationality", "Simple / Single-valued", notes="Country of citizenship / nationality."),
                Attribute("birth_year", "Simple / Single-valued", notes="Year of author birth."),
            ],
        ),
        Entity(
            name="BOOK_COPY",
            entity_type="Weak Entity",
            is_weak=True,
            owner_entity="BOOK_TITLE",
            justification="Physical tangible book copy. Identified by sequential copy number within parent book ISBN.",
            attributes=[
                Attribute("copy_number", "Simple / Single-valued", is_partial=True, notes="Partial key (sequential copy number within ISBN)."),
                Attribute("barcode", "Simple / Single-valued", is_candidate=True, notes="Unique physical barcode inventory tracking tag."),
                Attribute("physical_condition", "Simple / Single-valued", notes="'Pristine', 'Good', 'Worn', 'Under Restoration'."),
                Attribute("availability_status", "Simple / Single-valued", notes="'Available', 'Checked Out', 'Reserved'."),
                Attribute("shelf_location", "Simple / Single-valued", notes="Call number / shelf placement code."),
            ],
        ),
        Entity(
            name="MEMBER",
            entity_type="Strong Entity",
            is_weak=False,
            owner_entity=None,
            justification="Registered patron/reader entitled to circulation checkouts and hold reservations.",
            attributes=[
                Attribute("card_number", "Simple / Single-valued", is_pk=True, notes="Unique library membership card number (PK)."),
                Attribute("national_id", "Simple / Single-valued", is_candidate=True, notes="National Identity Card / Tax ID number."),
                Attribute("first_name", "Simple / Single-valued", notes="Member first name."),
                Attribute("last_name", "Simple / Single-valued", notes="Member last name."),
                Attribute("date_of_birth", "Simple / Single-valued", notes="Member date of birth."),
                Attribute(
                    "residential_address",
                    "Composite",
                    components=["street", "street_number", "postal_code", "city"],
                    notes="Residential home address.",
                ),
                Attribute("email", "Simple / Single-valued", is_candidate=True, notes="Unique email contact address."),
                Attribute("registration_date", "Simple / Single-valued", notes="Date of library membership enrollment."),
                Attribute("membership_status", "Simple / Single-valued", notes="'Active', 'Suspended'."),
                Attribute("phone_numbers", "Multi-valued", notes="Multiple contact phone numbers (MEMBER_PHONE table)."),
            ],
        ),
        Entity(
            name="LOAN",
            entity_type="Strong Entity",
            is_weak=False,
            owner_entity=None,
            justification="Circulation loan transaction entity tracking physical copy checkout by a member.",
            attributes=[
                Attribute("loan_id", "Simple / Single-valued", is_pk=True, notes="Unique circulation checkout loan ID (PK)."),
                Attribute("loan_date", "Simple / Single-valued", notes="Date copy was checked out."),
                Attribute("due_date", "Simple / Single-valued", notes="Mandatory return deadline date."),
                Attribute("return_date", "Simple / Single-valued", notes="Actual check-in date (NULL if still checked out)."),
                Attribute("late_fine", "Derived", notes="Computed late penalty fine based on overdue calendar days."),
            ],
        ),
        Entity(
            name="RESERVATION",
            entity_type="Strong Entity",
            is_weak=False,
            owner_entity=None,
            justification="Hold reservation queue request placed on a title when copies are unavailable.",
            attributes=[
                Attribute("reservation_id", "Simple / Single-valued", is_pk=True, notes="Unique hold reservation identifier (PK)."),
                Attribute("submission_timestamp", "Simple / Single-valued", notes="Exact timestamp when hold was requested."),
                Attribute("queue_priority", "Simple / Single-valued", notes="Queue sequence number for fulfillment priority."),
                Attribute("reservation_status", "Simple / Single-valued", notes="'Pending', 'Member Notified', 'Fulfilled', 'Cancelled'."),
            ],
        ),
    ]

    # 3. Relationship Attributes
    relationship_attributes = [
        RelationshipAttribute(
            name="manager_start_date",
            relationship_name="MANAGES (LIBRARY_BRANCH - LIBRARIAN)",
            justification="Effective appointment start date when librarian assumed directorship of branch.",
        ),
    ]

    # 4. Keys Analysis Table
    keys_analysis = [
        KeyAnalysisRow(
            entity_name="LIBRARY_BRANCH",
            key_count="2 Candidates",
            key_types="Candidates: {branch_id}, {branch_name}",
            final_pk_selection="branch_id",
            justification="Compact, stable identifier well-suited for foreign key references.",
        ),
        KeyAnalysisRow(
            entity_name="LIBRARIAN",
            key_count="2 Candidates",
            key_types="Candidates: {staff_id}, {national_id}",
            final_pk_selection="staff_id",
            justification="Internal employee registry number identifier.",
        ),
        KeyAnalysisRow(
            entity_name="BOOK_TITLE",
            key_count="1 Candidate",
            key_types="Candidate: {isbn}",
            final_pk_selection="isbn",
            justification="Recognized international bibliographic standard for book editions.",
        ),
        KeyAnalysisRow(
            entity_name="AUTHOR",
            key_count="1 Candidate",
            key_types="Candidate: {author_id}",
            final_pk_selection="author_id",
            justification="Unique synthetic author registry code.",
        ),
        KeyAnalysisRow(
            entity_name="BOOK_COPY",
            key_count="Weak Entity (1 Partial + 1 Candidate Barcode)",
            key_types="Partial: {copy_number}, Candidate: {barcode}",
            final_pk_selection="(isbn, copy_number)",
            justification="Composite primary key: Book title Foreign Key (isbn) + sequential copy number (copy_number).",
            is_weak=True,
        ),
        KeyAnalysisRow(
            entity_name="MEMBER",
            key_count="3 Candidates",
            key_types="Candidates: {card_number}, {national_id}, {email}",
            final_pk_selection="card_number",
            justification="Official library circulation card barcode identifier.",
        ),
        KeyAnalysisRow(
            entity_name="LOAN",
            key_count="1 Candidate",
            key_types="Candidate: {loan_id}",
            final_pk_selection="loan_id",
            justification="Unique circulation transaction reference number.",
        ),
        KeyAnalysisRow(
            entity_name="RESERVATION",
            key_count="1 Candidate",
            key_types="Candidate: {reservation_id}",
            final_pk_selection="reservation_id",
            justification="Unique reservation hold transaction identifier.",
        ),
    ]

    # 5. Relationships List
    relationships = [
        Relationship(
            letter_id="a",
            name="MANAGES (Manages Branch)",
            connected_entities="LIBRARY_BRANCH <-> LIBRARIAN",
            cardinality="1:1",
            participation="Total for Branch (1,1), Partial for Librarian (0,1)",
            relationship_type="Regular Relationship",
            attributes=["manager_start_date"],
            justification="Each branch must have exactly one head librarian director. A librarian manages at most one branch.",
        ),
        Relationship(
            letter_id="b",
            name="EMPLOYS (Employs Staff)",
            connected_entities="LIBRARY_BRANCH <-> LIBRARIAN",
            cardinality="1:N",
            participation="Total for Librarian (1,1), Total for Branch (1,N)",
            relationship_type="Regular Relationship",
            attributes=[],
            justification="Every librarian is assigned to a specific branch. Each branch employs multiple staff librarians.",
        ),
        Relationship(
            letter_id="c",
            name="BOOK_AUTHORSHIP (Authorship)",
            connected_entities="AUTHOR <-> BOOK_TITLE",
            cardinality="N:M",
            participation="Total for Book Title (1,N), Partial for Author (0,N)",
            relationship_type="Regular Junction Relationship",
            attributes=[],
            justification="A book title can be authored by multiple authors, and an author can write multiple book titles.",
        ),
        Relationship(
            letter_id="d",
            name="HAS_PHYSICAL_COPIES (Has Copies)",
            connected_entities="BOOK_TITLE <-> BOOK_COPY",
            cardinality="1:N",
            participation="Total for Copy (1,1), Partial for Book Title (0,N)",
            relationship_type="Identifying Relationship",
            attributes=[],
            justification="Identifying relationship of weak entity BOOK_COPY from parent BOOK_TITLE.",
        ),
        Relationship(
            letter_id="e",
            name="HOUSES_COPY (Houses Copy)",
            connected_entities="LIBRARY_BRANCH <-> BOOK_COPY",
            cardinality="1:N",
            participation="Total for Copy (1,1), Partial for Branch (0,N)",
            relationship_type="Regular Relationship",
            attributes=[],
            justification="Each physical book copy belongs permanently to a designated branch collection.",
        ),
        Relationship(
            letter_id="f",
            name="BORROWS_COPY (Borrows Copy)",
            connected_entities="MEMBER <-> LOAN",
            cardinality="1:N",
            participation="Total for Loan (1,1), Partial for Member (0,N)",
            relationship_type="Regular Relationship",
            attributes=[],
            justification="Every loan transaction is conducted by a specific member. A member can conduct multiple loans over time.",
        ),
        Relationship(
            letter_id="g",
            name="LOAN_TARGET (Loan Target)",
            connected_entities="BOOK_COPY <-> LOAN",
            cardinality="1:N",
            participation="Total for Loan (1,1), Partial for Copy (0,N)",
            relationship_type="Regular Relationship",
            attributes=[],
            justification="Each loan transaction involves a specific physical copy. A copy can accumulate multiple loan records.",
        ),
        Relationship(
            letter_id="h",
            name="SUBMITS_RESERVATION (Submits Reservation)",
            connected_entities="MEMBER <-> RESERVATION",
            cardinality="1:N",
            participation="Total for Reservation (1,1), Partial for Member (0,N)",
            relationship_type="Regular Relationship",
            attributes=[],
            justification="Each hold reservation is submitted by a registered member.",
        ),
        Relationship(
            letter_id="i",
            name="RESERVED_TITLE (Reserved Title)",
            connected_entities="BOOK_TITLE <-> RESERVATION",
            cardinality="1:N",
            participation="Total for Reservation (1,1), Partial for Book Title (0,N)",
            relationship_type="Regular Relationship",
            attributes=[],
            justification="A reservation targets the general bibliographic work (ISBN), not a specific physical copy.",
        ),
        Relationship(
            letter_id="j",
            name="PICKUP_BRANCH (Pickup Branch)",
            connected_entities="LIBRARY_BRANCH <-> RESERVATION",
            cardinality="1:N",
            participation="Total for Reservation (1,1), Partial for Branch (0,N)",
            relationship_type="Regular Relationship",
            attributes=[],
            justification="The member selects their preferred branch facility for hold retrieval.",
        ),
    ]

    # 6. Design Assumptions
    assumptions = [
        "The Head Librarian director is linked to LIBRARY_BRANCH via foreign key manager_staff_id with a UNIQUE constraint (1:1).",
        "Physical copies are modeled as weak entities with composite primary key (isbn, copy_number) and an alternate UNIQUE constraint on barcode.",
        "Multi-valued attributes (branch weekly schedule and member phone numbers) are normalized into independent 1:N relations.",
        "Circulation loans reference the specific physical inventory copy, whereas hold reservations target the general book title (ISBN) and pickup branch.",
    ]

    # 7. ER Diagram Tables
    er_tables = [
        ERTable(
            id="t-branch",
            label="LIBRARY_BRANCH",
            x=60,
            y=50,
            attrs=[
                ERTableAttr("branch_id", pk=True),
                ERTableAttr("branch_name"),
                ERTableAttr("street"),
                ERTableAttr("street_number"),
                ERTableAttr("postal_code"),
                ERTableAttr("neighborhood"),
                ERTableAttr("phone_number"),
                ERTableAttr("seating_capacity"),
                ERTableAttr("manager_staff_id", fk=True),
                ERTableAttr("manager_start_date"),
            ],
        ),
        ERTable(
            id="t-staff",
            label="LIBRARIAN",
            x=460,
            y=50,
            attrs=[
                ERTableAttr("staff_id", pk=True),
                ERTableAttr("national_id"),
                ERTableAttr("first_name"),
                ERTableAttr("last_name"),
                ERTableAttr("specialty"),
                ERTableAttr("phone_number"),
                ERTableAttr("branch_id", fk=True),
            ],
        ),
        ERTable(
            id="t-author",
            label="AUTHOR",
            x=860,
            y=50,
            attrs=[
                ERTableAttr("author_id", pk=True),
                ERTableAttr("full_name"),
                ERTableAttr("nationality"),
                ERTableAttr("birth_year"),
            ],
        ),
        ERTable(
            id="t-schedule",
            label="BRANCH_SCHEDULE",
            x=60,
            y=420,
            attrs=[
                ERTableAttr("branch_id", pk=True, fk=True),
                ERTableAttr("day_of_week", pk=True),
                ERTableAttr("opening_time"),
                ERTableAttr("closing_time"),
            ],
        ),
        ERTable(
            id="t-book-author",
            label="BOOK_AUTHORSHIP",
            x=860,
            y=270,
            attrs=[
                ERTableAttr("isbn", pk=True, fk=True),
                ERTableAttr("author_id", pk=True, fk=True),
            ],
        ),
        ERTable(
            id="t-book",
            label="BOOK_TITLE",
            x=460,
            y=350,
            attrs=[
                ERTableAttr("isbn", pk=True),
                ERTableAttr("title"),
                ERTableAttr("publisher"),
                ERTableAttr("publication_year"),
                ERTableAttr("subject_category"),
                ERTableAttr("page_count"),
            ],
        ),
        ERTable(
            id="t-copy",
            label="BOOK_COPY",
            x=60,
            y=620,
            attrs=[
                ERTableAttr("isbn", pk=True, fk=True),
                ERTableAttr("copy_number", pk=True),
                ERTableAttr("barcode"),
                ERTableAttr("physical_condition"),
                ERTableAttr("availability_status"),
                ERTableAttr("shelf_location"),
                ERTableAttr("branch_id", fk=True),
            ],
        ),
        ERTable(
            id="t-loan",
            label="LOAN",
            x=460,
            y=680,
            attrs=[
                ERTableAttr("loan_id", pk=True),
                ERTableAttr("card_number", fk=True),
                ERTableAttr("isbn", fk=True),
                ERTableAttr("copy_number", fk=True),
                ERTableAttr("loan_date"),
                ERTableAttr("due_date"),
                ERTableAttr("return_date"),
                ERTableAttr("late_fine_amount"),
            ],
        ),
        ERTable(
            id="t-reservation",
            label="RESERVATION",
            x=860,
            y=680,
            attrs=[
                ERTableAttr("reservation_id", pk=True),
                ERTableAttr("card_number", fk=True),
                ERTableAttr("isbn", fk=True),
                ERTableAttr("branch_id", fk=True),
                ERTableAttr("submission_timestamp"),
                ERTableAttr("queue_priority"),
                ERTableAttr("reservation_status"),
            ],
        ),
        ERTable(
            id="t-member",
            label="MEMBER",
            x=60,
            y=910,
            attrs=[
                ERTableAttr("card_number", pk=True),
                ERTableAttr("national_id"),
                ERTableAttr("first_name"),
                ERTableAttr("last_name"),
                ERTableAttr("date_of_birth"),
                ERTableAttr("street"),
                ERTableAttr("street_number"),
                ERTableAttr("postal_code"),
                ERTableAttr("city"),
                ERTableAttr("email"),
                ERTableAttr("registration_date"),
                ERTableAttr("membership_status"),
            ],
        ),
        ERTable(
            id="t-member-phone",
            label="MEMBER_PHONE",
            x=60,
            y=1330,
            attrs=[
                ERTableAttr("card_number", pk=True, fk=True),
                ERTableAttr("phone_number", pk=True),
            ],
        ),
    ]

    # 8. ER Diagram Edges
    er_edges = [
        # Branch manages Staff (1:1)
        EREdge("M 320 80 L 460 80", "start-one-mandatory", "end-one-optional", "MANAGES (1:1)", 390, 70),
        # Branch employs Staff (1:N)
        EREdge("M 320 120 L 460 120", "start-one-mandatory", "end-many-mandatory", "EMPLOYS (1:N)", 390, 140),
        # Branch Schedule (1:N multivalued)
        EREdge("M 190 378 L 190 420", "start-one-mandatory", "end-many-mandatory", "SCHEDULE (1:N)", 205, 399),
        # Author to Book Authorship (1:N)
        EREdge("M 990 210 L 990 270", "start-one-optional", "end-many-mandatory", "AUTHORS (1:N)", 1005, 240),
        # Book Title to Book Authorship (1:N)
        EREdge("M 720 380 L 860 380", "start-one-mandatory", "end-many-mandatory", "HAS_AUTHORS (1:N)", 790, 370),
        # Book Title to Copies (1:N identifying)
        EREdge("M 460 460 L 320 660", "start-one-optional", "end-many-mandatory", "HAS_COPIES (1:N)", 390, 550),
        # Branch to Copies (1:N)
        EREdge("M 60 200 L 30 200 L 30 650 L 60 650", "start-one-optional", "end-many-mandatory", "HOUSES (1:N)", 20, 425),
        # Member to Loan (1:N)
        EREdge("M 320 950 L 460 740", "start-one-optional", "end-many-mandatory", "BORROWS (1:N)", 390, 835),
        # Copy to Loan (1:N)
        EREdge("M 320 720 L 460 720", "start-one-optional", "end-many-mandatory", "LOAN_TARGET (1:N)", 390, 710),
        # Member to Reservation (1:N routed around loan)
        EREdge("M 320 980 L 400 980 L 400 1000 L 820 1000 L 820 740 L 860 740", "start-one-optional", "end-many-mandatory", "SUBMITS (1:N)", 610, 990),
        # Member to Phone (1:N)
        EREdge("M 190 1294 L 190 1330", "start-one-optional", "end-many-mandatory", "PHONES (1:N)", 205, 1312),
        # Book Title to Reservation (1:N)
        EREdge("M 720 480 L 860 700", "start-one-optional", "end-many-mandatory", "RESERVES (1:N)", 790, 585),
        # Branch to Reservation (1:N)
        EREdge("M 320 200 L 860 720", "start-one-optional", "end-many-mandatory", "PICKUP_AT (1:N)", 590, 460),
    ]

    # 9. Relational Conversion Justifications
    relational_justifications = [
        RelationalJustification(
            title="1. Conversion of Weak Entity (BOOK_COPY)",
            color_class="border-red-500",
            description="The BOOK_COPY table receives foreign key isbn from BOOK_TITLE to form composite Primary Key (isbn, copy_number). It also contains a foreign key referencing LIBRARY_BRANCH to identify the housing facility.",
        ),
        RelationalJustification(
            title="2. Conversion of N:M Relationship (BOOK_AUTHORSHIP)",
            color_class="border-amber-500",
            description="The N:M relationship between AUTHOR and BOOK_TITLE is mapped to junction table BOOK_AUTHORSHIP with composite Primary Key (isbn, author_id).",
        ),
        RelationalJustification(
            title="3. Conversion of 1:1 Relationship (MANAGES)",
            color_class="border-blue-500",
            description="Because LIBRARY_BRANCH has total participation (every branch must have a head director), manager_staff_id is placed in LIBRARY_BRANCH with a UNIQUE constraint.",
        ),
        RelationalJustification(
            title="4. Conversion of Multi-Valued Attributes (BRANCH_SCHEDULE, MEMBER_PHONE)",
            color_class="border-purple-500",
            description="Multi-valued attributes are converted into 1:N relational tables: BRANCH_SCHEDULE (branch_id, day_of_week, opening_time, closing_time) and MEMBER_PHONE (card_number, phone_number).",
        ),
        RelationalJustification(
            title="5. Implementation of Circulation Transactions & Reservations",
            color_class="border-emerald-500",
            description="The LOAN table connects the physical copy (isbn, copy_number) to the member (card_number). The RESERVATION table connects the book title (isbn), member (card_number), and pickup branch (branch_id).",
        ),
    ]

    # 10. Complete Production SQL DDL
    sql_ddl = """-- ==========================================================
-- PostgreSQL / MySQL Relational Schema for Municipal Library Network
-- Case Study: Exam Paper 7 (Municipal Library Network)
-- ==========================================================

-- 1. Entity: LIBRARIAN (Staff / Librarians)
CREATE TABLE LIBRARIAN (
    staff_id VARCHAR(15) PRIMARY KEY,
    national_id VARCHAR(10) NOT NULL UNIQUE,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    specialty VARCHAR(60) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    branch_id VARCHAR(10) NOT NULL -- Will be referenced by FK after branch table creation
);

-- 2. Entity: LIBRARY_BRANCH (Library Branches)
CREATE TABLE LIBRARY_BRANCH (
    branch_id VARCHAR(10) PRIMARY KEY,
    branch_name VARCHAR(100) NOT NULL UNIQUE,
    street VARCHAR(60) NOT NULL,
    street_number VARCHAR(10) NOT NULL,
    postal_code VARCHAR(10) NOT NULL,
    neighborhood VARCHAR(50) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    seating_capacity INT NOT NULL CHECK (seating_capacity > 0),
    manager_staff_id VARCHAR(15) UNIQUE,
    manager_start_date DATE,
    FOREIGN KEY (manager_staff_id) REFERENCES LIBRARIAN(staff_id) ON DELETE SET NULL
);

-- Add Foreign Key for Staff Branch employment
ALTER TABLE LIBRARIAN
ADD CONSTRAINT fk_staff_branch
FOREIGN KEY (branch_id) REFERENCES LIBRARY_BRANCH(branch_id) ON DELETE RESTRICT;

-- 3. Multi-valued Attribute: BRANCH_SCHEDULE
CREATE TABLE BRANCH_SCHEDULE (
    branch_id VARCHAR(10) NOT NULL,
    day_of_week VARCHAR(20) NOT NULL CHECK (day_of_week IN ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')),
    opening_time TIME NOT NULL,
    closing_time TIME NOT NULL,
    PRIMARY KEY (branch_id, day_of_week, opening_time),
    FOREIGN KEY (branch_id) REFERENCES LIBRARY_BRANCH(branch_id) ON DELETE CASCADE,
    CHECK (closing_time > opening_time)
);

-- 4. Entity: BOOK_TITLE (Book Titles / Catalog)
CREATE TABLE BOOK_TITLE (
    isbn VARCHAR(20) PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    publisher VARCHAR(100) NOT NULL,
    publication_year INT NOT NULL CHECK (publication_year >= 1450),
    subject_category VARCHAR(60) NOT NULL,
    page_count INT NOT NULL CHECK (page_count > 0)
);

-- 5. Entity: AUTHOR (Authors)
CREATE TABLE AUTHOR (
    author_id VARCHAR(15) PRIMARY KEY,
    full_name VARCHAR(120) NOT NULL,
    nationality VARCHAR(50) NOT NULL,
    birth_year INT CHECK (birth_year >= 1000)
);

-- 6. Junction Table: BOOK_AUTHORSHIP (N:M Book Authorship)
CREATE TABLE BOOK_AUTHORSHIP (
    isbn VARCHAR(20) NOT NULL,
    author_id VARCHAR(15) NOT NULL,
    PRIMARY KEY (isbn, author_id),
    FOREIGN KEY (isbn) REFERENCES BOOK_TITLE(isbn) ON DELETE CASCADE,
    FOREIGN KEY (author_id) REFERENCES AUTHOR(author_id) ON DELETE CASCADE
);

-- 7. Weak Entity: BOOK_COPY (Physical Copies)
CREATE TABLE BOOK_COPY (
    isbn VARCHAR(20) NOT NULL,
    copy_number INT NOT NULL CHECK (copy_number > 0),
    barcode VARCHAR(40) NOT NULL UNIQUE,
    physical_condition VARCHAR(30) NOT NULL CHECK (physical_condition IN ('Pristine', 'Good', 'Worn', 'Under Restoration')),
    availability_status VARCHAR(30) NOT NULL DEFAULT 'Available' CHECK (availability_status IN ('Available', 'Checked Out', 'Reserved')),
    shelf_location VARCHAR(30) NOT NULL,
    branch_id VARCHAR(10) NOT NULL,
    PRIMARY KEY (isbn, copy_number),
    FOREIGN KEY (isbn) REFERENCES BOOK_TITLE(isbn) ON DELETE CASCADE,
    FOREIGN KEY (branch_id) REFERENCES LIBRARY_BRANCH(branch_id) ON DELETE RESTRICT
);

-- 8. Entity: MEMBER (Library Members)
CREATE TABLE MEMBER (
    card_number VARCHAR(20) PRIMARY KEY,
    national_id VARCHAR(10) NOT NULL UNIQUE,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    street VARCHAR(60) NOT NULL,
    street_number VARCHAR(10) NOT NULL,
    postal_code VARCHAR(10) NOT NULL,
    city VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    registration_date DATE NOT NULL,
    membership_status VARCHAR(20) NOT NULL DEFAULT 'Active' CHECK (membership_status IN ('Active', 'Suspended'))
);

-- 9. Multi-valued Attribute: MEMBER_PHONE
CREATE TABLE MEMBER_PHONE (
    card_number VARCHAR(20) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    PRIMARY KEY (card_number, phone_number),
    FOREIGN KEY (card_number) REFERENCES MEMBER(card_number) ON DELETE CASCADE
);

-- 10. Entity: LOAN (Circulation Transactions)
CREATE TABLE LOAN (
    loan_id VARCHAR(20) PRIMARY KEY,
    card_number VARCHAR(20) NOT NULL,
    isbn VARCHAR(20) NOT NULL,
    copy_number INT NOT NULL,
    loan_date DATE NOT NULL,
    due_date DATE NOT NULL,
    return_date DATE,
    late_fine_amount DECIMAL(8, 2) DEFAULT 0.00 CHECK (late_fine_amount >= 0),
    FOREIGN KEY (card_number) REFERENCES MEMBER(card_number) ON DELETE RESTRICT,
    FOREIGN KEY (isbn, copy_number) REFERENCES BOOK_COPY(isbn, copy_number) ON DELETE RESTRICT,
    CHECK (due_date >= loan_date)
);

-- 11. Entity: RESERVATION (Hold Queue)
CREATE TABLE RESERVATION (
    reservation_id VARCHAR(20) PRIMARY KEY,
    card_number VARCHAR(20) NOT NULL,
    isbn VARCHAR(20) NOT NULL,
    branch_id VARCHAR(10) NOT NULL,
    submission_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    queue_priority INT NOT NULL CHECK (queue_priority > 0),
    reservation_status VARCHAR(30) NOT NULL DEFAULT 'Pending' CHECK (
        reservation_status IN ('Pending', 'Member Notified', 'Fulfilled', 'Cancelled')
    ),
    FOREIGN KEY (card_number) REFERENCES MEMBER(card_number) ON DELETE CASCADE,
    FOREIGN KEY (isbn) REFERENCES BOOK_TITLE(isbn) ON DELETE CASCADE,
    FOREIGN KEY (branch_id) REFERENCES LIBRARY_BRANCH(branch_id) ON DELETE RESTRICT
);

-- Indexes for Query Performance
CREATE INDEX idx_copy_branch ON BOOK_COPY(branch_id);
CREATE INDEX idx_loan_active ON LOAN(card_number, return_date);
CREATE INDEX idx_reservation_queue ON RESERVATION(isbn, branch_id, queue_priority);
"""

    return Scenario(
        id="library_management",
        title="Municipal Library Network Management System",
        subtitle="Public Library Branches, Bibliographic Titles, Physical Copies, Members, Circulation Loans & Reservations",
        course_tag="Databases (Progress Test 2025-2026 - Problem 7)",
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
