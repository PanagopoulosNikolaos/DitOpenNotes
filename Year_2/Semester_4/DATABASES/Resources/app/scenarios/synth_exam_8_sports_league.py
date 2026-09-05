"""Sports League Management case study scenario module.

Contains the complete parsed and modeled ER analysis for the National Sports League Federation
(Teams, Athletes, Coaches, Player Contracts, Matches, Match Events & Injury Records),
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


def createSportsLeagueScenario() -> Scenario:
    """Constructs and returns the Sports League database scenario.

    Returns:
        Scenario: Fully populated scenario instance.
    """
    # 1. Text Paragraphs with Interactive Segments
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="A national professional sports league federation is designing a relational database information system to manage "),
                TextSegment(
                    text="teams / clubs",
                    is_highlight=True,
                    category="entity",
                    tag_label="ENTITY",
                    badge_class="badge-entity-strong",
                    tooltip="Strong Entity: Sports club / team with unique Team ID.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="athletes",
                    is_highlight=True,
                    category="entity",
                    tag_label="ENTITY",
                    badge_class="badge-entity-strong",
                    tooltip="Strong Entity: Professional player with unique League Athlete Registration Number.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="coaches",
                    is_highlight=True,
                    category="entity",
                    tag_label="ENTITY",
                    badge_class="badge-entity-strong",
                    tooltip="Strong Entity: Professional coach with unique Coach License Number (Coach ID).",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="league matches / fixtures",
                    is_highlight=True,
                    category="entity",
                    tag_label="ENTITY",
                    badge_class="badge-entity-strong",
                    tooltip="Strong Entity: Scheduled league match with unique Match ID contested between two teams.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="statistical match events",
                    is_highlight=True,
                    category="entity",
                    tag_label="WEAK ENTITY",
                    badge_class="badge-entity-weak",
                    tooltip="Weak Entity: Critical in-match event (goal, card, substitution) identified within the match context.",
                ),
                TextSegment(text=", and "),
                TextSegment(
                    text="injury incident records",
                    is_highlight=True,
                    category="entity",
                    tag_label="WEAK ENTITY",
                    badge_class="badge-entity-weak",
                    tooltip="Weak Entity: Medical injury history tracked for each athlete.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color=None,
        ),
        Paragraph(
            segments=[
                TextSegment(text="1. <strong>Clubs & Teams:</strong> Each team is characterized by a "),
                TextSegment(
                    text="unique Team ID",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Primary Key: Unique team identifier code.",
                ),
                TextSegment(text=", an "),
                TextSegment(
                    text="official club name (e.g., 'Athens Athletic Club')",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Candidate Key: Unique official corporate/club title.",
                ),
                TextSegment(text=", the "),
                TextSegment(text="home city", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="founding year", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="home stadium / arena", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", and the "),
                TextSegment(text="spectator seating capacity", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=". Each team maintains official "),
                TextSegment(
                    text="club colors (e.g., 'Cyan', 'White') recorded as a list of colors",
                    is_highlight=True,
                    category="attr",
                    tag_label="MULTI-VALUED",
                    badge_class="badge-attr-multi",
                    tooltip="Multi-Valued Attribute: Exported to the TEAM_COLOR relation.",
                ),
                TextSegment(text=". Each team is mandatorily guided by exactly one "),
                TextSegment(
                    text="Head Coach",
                    is_highlight=True,
                    category="rel",
                    tag_label="1:1 RELATIONSHIP",
                    badge_class="badge-rel-11",
                    tooltip="1:1 Relationship (HEAD_COACH): Total participation for Team, partial for Coach.",
                ),
                TextSegment(text=", for whom the "),
                TextSegment(
                    text="appointment start date",
                    is_highlight=True,
                    category="attr",
                    tag_label="RELATIONSHIP ATTRIBUTE",
                    badge_class="badge-attr-simple",
                    tooltip="Relationship Attribute: Stored in the TEAM table.",
                ),
                TextSegment(text=" is recorded."),
            ],
            accent_border_color="border-blue-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="2. <strong>Coaches:</strong> For each coach, the system tracks: the "),
                TextSegment(
                    text="unique Coach License Number (Coach ID)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Primary Key: Unique federation coaching license identifier.",
                ),
                TextSegment(text=", the "),
                TextSegment(
                    text="Tax ID (AFM)",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Candidate Key: National tax identification number of coach.",
                ),
                TextSegment(text=", the "),
                TextSegment(text="full name", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="date of birth", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="nationality", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="coaching certification tier (e.g., 'UEFA Pro', 'FIBA Level 1')", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", and the "),
                TextSegment(text="mobile contact telephone", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=". A coach can "),
                TextSegment(
                    text="serve as head coach for at most one team at a time",
                    is_highlight=True,
                    category="rel",
                    tag_label="1:1 CONSTRAINT",
                    badge_class="badge-rel-11",
                    tooltip="Uniqueness Constraint: Head Coach of at most one team concurrently.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-amber-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="3. <strong>Athletes & Professional Contracts:</strong> For each athlete, the database maintains: the "),
                TextSegment(
                    text="unique Athlete League Registration Number",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Primary Key: Unique federation athlete registration number.",
                ),
                TextSegment(text=", the "),
                TextSegment(
                    text="National ID Number (ADT)",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Candidate Key: National identity card number.",
                ),
                TextSegment(text=", the "),
                TextSegment(text="first name", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="last name", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="date of birth", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="height (in cm)", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="weight (in kg)", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="nationality", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", and the "),
                TextSegment(text="primary playing position (e.g., 'Goalkeeper', 'Central Defender', 'Forward')", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=". Each athlete is bound by an "),
                TextSegment(
                    text="official professional contract with a single team",
                    is_highlight=True,
                    category="rel",
                    tag_label="1:N RELATIONSHIP",
                    badge_class="badge-rel-1n",
                    tooltip="1:N Relationship (CONTRACT): Each player belongs to 1 team. A team contracts multiple players.",
                ),
                TextSegment(text=". For each active contract, the following are recorded: the "),
                TextSegment(text="player jersey squad number", is_highlight=True, category="attr", tag_label="RELATIONSHIP ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="contract start date", is_highlight=True, category="attr", tag_label="RELATIONSHIP ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="contract expiration date", is_highlight=True, category="attr", tag_label="RELATIONSHIP ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", and the "),
                TextSegment(text="annual base salary", is_highlight=True, category="attr", tag_label="RELATIONSHIP ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text="."),
            ],
            accent_border_color="border-purple-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="4. <strong>League Matches (Fixtures):</strong> Teams compete in scheduled tournament fixtures. Each match is identified by a "),
                TextSegment(
                    text="unique Match ID",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Primary Key: Unique league match identifier.",
                ),
                TextSegment(text=", the "),
                TextSegment(text="tournament round number", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="scheduled match date and kickoff time", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="venue stadium", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", and the "),
                TextSegment(text="assigned referee full name", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=". Each match is contested between two specific teams: the "),
                TextSegment(
                    text="Home Team",
                    is_highlight=True,
                    category="rel",
                    tag_label="1:N RELATIONSHIP (ROLE 1)",
                    badge_class="badge-rel-1n",
                    tooltip="Role 1 Relationship with TEAM: Home team (home_team_id).",
                ),
                TextSegment(text=" and the "),
                TextSegment(
                    text="Away Team",
                    is_highlight=True,
                    category="rel",
                    tag_label="1:N RELATIONSHIP (ROLE 2)",
                    badge_class="badge-rel-1n",
                    tooltip="Role 2 Relationship with TEAM: Away team (away_team_id).",
                ),
                TextSegment(text=". Upon completion of the match, the "),
                TextSegment(
                    text="final score (goals / points scored by home team and away team)",
                    is_highlight=True,
                    category="attr",
                    tag_label="ATTRIBUTES",
                    badge_class="badge-attr-simple",
                    tooltip="Final Score: score_home, score_away (NULL prior to match completion).",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-emerald-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="5. <strong>Match Events:</strong> During each match, critical incidents are logged in chronological detail. Each event is identified by a "),
                TextSegment(
                    text="sequential event number within the specific match",
                    is_highlight=True,
                    category="key",
                    tag_label="PARTIAL KEY",
                    badge_class="badge-key-partial",
                    tooltip="Partial Key: Sequential event sequence number (event_seq_no) within the specific match_id.",
                ),
                TextSegment(text=", the "),
                TextSegment(text="match minute (e.g., 45', 89')", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="event type ('Goal', 'Yellow Card', 'Red Card', 'Substitution', 'Penalty Kick')", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", and the "),
                TextSegment(
                    text="participating athlete who caused the event",
                    is_highlight=True,
                    category="rel",
                    tag_label="1:N RELATIONSHIP",
                    badge_class="badge-rel-1n",
                    tooltip="1:N Relationship (CAUSED_EVENT): Foreign Key athlete_id referencing ATHLETE table.",
                ),
                TextSegment(text=". An event "),
                TextSegment(
                    text="cannot exist independently without its parent match (Weak Entity)",
                    is_highlight=True,
                    category="entity",
                    tag_label="WEAK ENTITY",
                    badge_class="badge-entity-weak",
                    tooltip="Weak Entity: Composite PK (match_id, event_seq_no) with ON DELETE CASCADE.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-red-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="6. <strong>Injury & Medical History:</strong> For each athlete, medical records track injury incidents. For each incident, the system tracks a "),
                TextSegment(
                    text="sequential incident number for the specific athlete",
                    is_highlight=True,
                    category="key",
                    tag_label="PARTIAL KEY",
                    badge_class="badge-key-partial",
                    tooltip="Partial Key: Sequential incident number (incident_no) within the specific athlete.",
                ),
                TextSegment(text=", the "),
                TextSegment(text="injury incident date", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="injury diagnosis / type", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="estimated rehabilitation duration (in weeks)", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", and the "),
                TextSegment(text="confirmed medical clearance return date", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text="."),
            ],
            accent_border_color="border-cyan-500",
        ),
    ]

    # 2. Complete Entity List with Detailed Attributes
    entities = [
        Entity(
            name="TEAM",
            entity_type="Strong Entity",
            is_weak=False,
            owner_entity=None,
            justification="Autonomous sports club / team with distinct identity and unique Team ID.",
            attributes=[
                Attribute("team_id", "Simple / Single-valued", is_pk=True, notes="Unique team identifier code (PK)."),
                Attribute("team_name", "Simple / Single-valued", is_candidate=True, notes="Unique official registered club name."),
                Attribute("home_city", "Simple / Single-valued", notes="City where the club facility is located."),
                Attribute("founding_year", "Simple / Single-valued", notes="Year the sports club was founded."),
                Attribute("home_stadium", "Simple / Single-valued", notes="Name of home arena or venue."),
                Attribute("seating_capacity", "Simple / Single-valued", notes="Spectator seating capacity of stadium."),
                Attribute("team_colors", "Multi-valued", notes="Official club colors (TEAM_COLOR table)."),
            ],
        ),
        Entity(
            name="COACH",
            entity_type="Strong Entity",
            is_weak=False,
            owner_entity=None,
            justification="Professional coach with autonomous registry identity and unique coaching license number.",
            attributes=[
                Attribute("coach_id", "Simple / Single-valued", is_pk=True, notes="Unique coaching license certification number (PK)."),
                Attribute("tax_id", "Simple / Single-valued", is_candidate=True, notes="National Tax Identification Number (AFM)."),
                Attribute("full_name", "Simple / Single-valued", notes="Full legal name of coach."),
                Attribute("date_of_birth", "Simple / Single-valued", notes="Date of birth."),
                Attribute("nationality", "Simple / Single-valued", notes="Country of citizenship / nationality."),
                Attribute("license_tier", "Simple / Single-valued", notes="Coaching diploma category (e.g., 'UEFA Pro', 'FIBA Level 1')."),
                Attribute("phone_number", "Simple / Single-valued", notes="Primary telephone contact."),
            ],
        ),
        Entity(
            name="ATHLETE",
            entity_type="Strong Entity",
            is_weak=False,
            owner_entity=None,
            justification="Professional league player with unique federation license registration number.",
            attributes=[
                Attribute("athlete_id", "Simple / Single-valued", is_pk=True, notes="Unique athlete league registration number (PK)."),
                Attribute("national_id", "Simple / Single-valued", is_candidate=True, notes="Government-issued National ID Card Number."),
                Attribute("first_name", "Simple / Single-valued", notes="Player first name."),
                Attribute("last_name", "Simple / Single-valued", notes="Player last name."),
                Attribute("date_of_birth", "Simple / Single-valued", notes="Player date of birth."),
                Attribute("height_cm", "Simple / Single-valued", notes="Physical height in centimeters."),
                Attribute("weight_kg", "Simple / Single-valued", notes="Physical body weight in kilograms."),
                Attribute("nationality", "Simple / Single-valued", notes="Country of citizenship / nationality."),
                Attribute("playing_position", "Simple / Single-valued", notes="Primary tactical playing position."),
            ],
        ),
        Entity(
            name="MATCH",
            entity_type="Strong Entity",
            is_weak=False,
            owner_entity=None,
            justification="Official competitive fixture between home and away teams.",
            attributes=[
                Attribute("match_id", "Simple / Single-valued", is_pk=True, notes="Unique match fixture identifier (PK)."),
                Attribute("round_number", "Simple / Single-valued", notes="Tournament round sequence number."),
                Attribute("match_start_time", "Simple / Single-valued", notes="Scheduled match date and kickoff timestamp."),
                Attribute("stadium_venue", "Simple / Single-valued", notes="Stadium where the match takes place."),
                Attribute("referee_name", "Simple / Single-valued", notes="Full name of the designated head referee."),
                Attribute("score_home", "Simple / Single-valued", notes="Goals / points scored by the home team."),
                Attribute("score_away", "Simple / Single-valued", notes="Goals / points scored by the away team."),
            ],
        ),
        Entity(
            name="MATCH_EVENT",
            entity_type="Weak Entity",
            is_weak=True,
            owner_entity="MATCH",
            justification="Critical in-game event that exists only within the context of the parent match fixture.",
            attributes=[
                Attribute("event_seq_no", "Simple / Single-valued", is_partial=True, notes="Partial key (chronological sequence number in match)."),
                Attribute("match_minute", "Simple / Single-valued", notes="Elapsed match minute of occurrence (e.g., 45)."),
                Attribute("event_type", "Simple / Single-valued", notes="'Goal', 'Yellow Card', 'Red Card', 'Substitution', 'Penalty Kick'."),
            ],
        ),
        Entity(
            name="INJURY_RECORD",
            entity_type="Weak Entity",
            is_weak=True,
            owner_entity="ATHLETE",
            justification="Medical injury diagnosis event existentially dependent on the specific athlete.",
            attributes=[
                Attribute("incident_no", "Simple / Single-valued", is_partial=True, notes="Partial key (sequential injury incident number per athlete)."),
                Attribute("injury_date", "Simple / Single-valued", notes="Date when injury occurred."),
                Attribute("injury_type", "Simple / Single-valued", notes="Medical diagnostic label (e.g., 'Hamstring Strain', 'ACL Tear')."),
                Attribute("recovery_weeks", "Simple / Single-valued", notes="Estimated rehabilitation recovery duration in weeks."),
                Attribute("clearance_date", "Simple / Single-valued", notes="Medical clearance return date to active duty."),
            ],
        ),
    ]

    # 3. Relationship Attributes
    relationship_attributes = [
        RelationshipAttribute(
            name="coach_appointment_date",
            relationship_name="HEAD_COACH (TEAM - COACH)",
            justification="Effective start date of head coaching contract tenure.",
        ),
        RelationshipAttribute(
            name="jersey_number",
            relationship_name="PLAYER_CONTRACT (TEAM - ATHLETE)",
            justification="Assigned roster shirt number for the athlete on the team.",
        ),
        RelationshipAttribute(
            name="contract_start_date",
            relationship_name="PLAYER_CONTRACT (TEAM - ATHLETE)",
            justification="Effective commencement date of player contract.",
        ),
        RelationshipAttribute(
            name="contract_end_date",
            relationship_name="PLAYER_CONTRACT (TEAM - ATHLETE)",
            justification="Official expiration date of player contract.",
        ),
        RelationshipAttribute(
            name="annual_salary",
            relationship_name="PLAYER_CONTRACT (TEAM - ATHLETE)",
            justification="Contracted annual base monetary compensation.",
        ),
    ]

    # 4. Keys Analysis Table
    keys_analysis = [
        KeyAnalysisRow(
            entity_name="TEAM",
            key_count="2 Candidates",
            key_types="Candidates: {team_id}, {team_name}",
            final_pk_selection="team_id",
            justification="Compact alphanumeric code well-suited for foreign key associations.",
        ),
        KeyAnalysisRow(
            entity_name="COACH",
            key_count="2 Candidates",
            key_types="Candidates: {coach_id}, {tax_id}",
            final_pk_selection="coach_id",
            justification="Official coaching license number issued by the federation.",
        ),
        KeyAnalysisRow(
            entity_name="ATHLETE",
            key_count="2 Candidates",
            key_types="Candidates: {athlete_id}, {national_id}",
            final_pk_selection="athlete_id",
            justification="Official federation athlete registry number.",
        ),
        KeyAnalysisRow(
            entity_name="MATCH",
            key_count="1 Candidate",
            key_types="Candidate: {match_id}",
            final_pk_selection="match_id",
            justification="Unique league fixture code identifier.",
        ),
        KeyAnalysisRow(
            entity_name="MATCH_EVENT",
            key_count="Weak Entity (1 Partial Key)",
            key_types="Partial: {event_seq_no}",
            final_pk_selection="(match_id, event_seq_no)",
            justification="Composite primary key: Match Foreign Key (match_id) + chronological event sequence (event_seq_no).",
            is_weak=True,
        ),
        KeyAnalysisRow(
            entity_name="INJURY_RECORD",
            key_count="Weak Entity (1 Partial Key)",
            key_types="Partial: {incident_no}",
            final_pk_selection="(athlete_id, incident_no)",
            justification="Composite primary key: Athlete Foreign Key (athlete_id) + incident sequence (incident_no).",
            is_weak=True,
        ),
    ]

    # 5. Relationships List
    relationships = [
        Relationship(
            letter_id="a",
            name="HEAD_COACH (Head Coach)",
            connected_entities="TEAM <-> COACH",
            cardinality="1:1",
            participation="Total for Team (1,1), Partial for Coach (0,1)",
            relationship_type="Regular Relationship",
            attributes=["coach_appointment_date"],
            justification="Each team must have exactly one head coach. A coach leads at most one team concurrently.",
        ),
        Relationship(
            letter_id="b",
            name="PLAYER_CONTRACT (Player Contract)",
            connected_entities="TEAM <-> ATHLETE",
            cardinality="1:N",
            participation="Total for Athlete (1,1), Total for Team (1,N)",
            relationship_type="Regular Relationship",
            attributes=["jersey_number", "contract_start_date", "contract_end_date", "annual_salary"],
            justification="Each athlete is bound under contract with exactly 1 team. Each team contracts a roster of multiple players.",
        ),
        Relationship(
            letter_id="c",
            name="HOSTS_MATCH (Home Team)",
            connected_entities="TEAM <-> MATCH",
            cardinality="1:N",
            participation="Total for Match (1,1), Partial for Team (0,N)",
            relationship_type="Regular Relationship",
            attributes=[],
            justification="In every match fixture, exactly one team participates as the host / home team (home_team_id).",
        ),
        Relationship(
            letter_id="d",
            name="AWAY_TEAM_IN_MATCH (Away Team)",
            connected_entities="TEAM <-> MATCH",
            cardinality="1:N",
            participation="Total for Match (1,1), Partial for Team (0,N)",
            relationship_type="Regular Relationship",
            attributes=[],
            justification="In every match fixture, exactly one team participates as the visitor / away team (away_team_id).",
        ),
        Relationship(
            letter_id="e",
            name="CONTAINS_EVENT (Match Events)",
            connected_entities="MATCH <-> MATCH_EVENT",
            cardinality="1:N",
            participation="Total for Event (1,1), Partial for Match (0,N)",
            relationship_type="Identifying Relationship",
            attributes=[],
            justification="Identifying relationship of weak entity MATCH_EVENT from parent MATCH.",
        ),
        Relationship(
            letter_id="f",
            name="CAUSED_EVENT (Caused Event)",
            connected_entities="ATHLETE <-> MATCH_EVENT",
            cardinality="1:N",
            participation="Total for Event (1,1), Partial for Athlete (0,N)",
            relationship_type="Regular Relationship",
            attributes=[],
            justification="Each statistical in-match event is linked to the participating athlete who triggered it.",
        ),
        Relationship(
            letter_id="g",
            name="SUFFERED_INJURY (Suffered Injury)",
            connected_entities="ATHLETE <-> INJURY_RECORD",
            cardinality="1:N",
            participation="Total for Injury Record (1,1), Partial for Athlete (0,N)",
            relationship_type="Identifying Relationship",
            attributes=[],
            justification="Identifying relationship of weak entity INJURY_RECORD from parent ATHLETE.",
        ),
    ]

    # 6. Design Assumptions
    assumptions = [
        "The Head Coach is linked to the TEAM table via foreign key head_coach_id with a UNIQUE constraint (1:1).",
        "Player contracts are integrated into the ATHLETE table (1:N relationship with Team) as each athlete plays for one team at any given time.",
        "Match events constitute a weak entity with composite key (match_id, event_seq_no) referencing the triggering athlete via Foreign Key.",
        "Medical injury records are modeled as a weak entity with composite key (athlete_id, incident_no).",
    ]

    # 7. ER Diagram Tables
    er_tables = [
        ERTable(
            id="t-team",
            label="TEAM",
            x=60,
            y=50,
            attrs=[
                ERTableAttr("team_id", pk=True),
                ERTableAttr("team_name"),
                ERTableAttr("home_city"),
                ERTableAttr("founding_year"),
                ERTableAttr("home_stadium"),
                ERTableAttr("seating_capacity"),
                ERTableAttr("head_coach_id", fk=True),
                ERTableAttr("coach_appointment_date"),
            ],
        ),
        ERTable(
            id="t-coach",
            label="COACH",
            x=460,
            y=50,
            attrs=[
                ERTableAttr("coach_id", pk=True),
                ERTableAttr("tax_id"),
                ERTableAttr("full_name"),
                ERTableAttr("date_of_birth"),
                ERTableAttr("nationality"),
                ERTableAttr("license_tier"),
                ERTableAttr("phone_number"),
            ],
        ),
        ERTable(
            id="t-color",
            label="TEAM_COLOR",
            x=860,
            y=50,
            attrs=[
                ERTableAttr("team_id", pk=True, fk=True),
                ERTableAttr("color_name", pk=True),
            ],
        ),
        ERTable(
            id="t-athlete",
            label="ATHLETE",
            x=60,
            y=360,
            attrs=[
                ERTableAttr("athlete_id", pk=True),
                ERTableAttr("national_id"),
                ERTableAttr("first_name"),
                ERTableAttr("last_name"),
                ERTableAttr("date_of_birth"),
                ERTableAttr("height_cm"),
                ERTableAttr("weight_kg"),
                ERTableAttr("nationality"),
                ERTableAttr("playing_position"),
                ERTableAttr("team_id", fk=True),
                ERTableAttr("jersey_number"),
                ERTableAttr("contract_start_date"),
                ERTableAttr("contract_end_date"),
                ERTableAttr("annual_salary"),
            ],
        ),
        ERTable(
            id="t-injury",
            label="INJURY_RECORD",
            x=460,
            y=360,
            attrs=[
                ERTableAttr("athlete_id", pk=True, fk=True),
                ERTableAttr("incident_no", pk=True),
                ERTableAttr("injury_date"),
                ERTableAttr("injury_type"),
                ERTableAttr("recovery_weeks"),
                ERTableAttr("clearance_date"),
            ],
        ),
        ERTable(
            id="t-event",
            label="MATCH_EVENT",
            x=860,
            y=360,
            attrs=[
                ERTableAttr("match_id", pk=True, fk=True),
                ERTableAttr("event_seq_no", pk=True),
                ERTableAttr("match_minute"),
                ERTableAttr("event_type"),
                ERTableAttr("athlete_id", fk=True),
            ],
        ),
        ERTable(
            id="t-match",
            label="MATCH",
            x=460,
            y=630,
            attrs=[
                ERTableAttr("match_id", pk=True),
                ERTableAttr("round_number"),
                ERTableAttr("match_start_time"),
                ERTableAttr("stadium_venue"),
                ERTableAttr("referee_name"),
                ERTableAttr("home_team_id", fk=True),
                ERTableAttr("away_team_id", fk=True),
                ERTableAttr("score_home"),
                ERTableAttr("score_away"),
            ],
        ),
    ]

    # 8. ER Diagram Edges
    er_edges = [
        # Team to Head Coach (1:1)
        EREdge("M 320 80 L 460 80", "start-one-mandatory", "end-one-optional", "HEAD_COACH (1:1)", 390, 70),
        # Team to Colors (1:N)
        EREdge("M 320 120 L 860 120", "start-one-mandatory", "end-many-mandatory", "COLORS (1:N)", 590, 110),
        # Team to Athletes (1:N)
        EREdge("M 190 322 L 190 360", "start-one-mandatory", "end-many-mandatory", "CONTRACT (1:N)", 205, 341),
        # Athlete to Injuries (1:N identifying)
        EREdge("M 320 400 L 460 400", "start-one-optional", "end-many-mandatory", "INJURIES (1:N)", 390, 390),
        # Athlete to Events (1:N routed under injury table)
        EREdge("M 320 580 L 860 580 L 860 548", "start-one-optional", "end-many-mandatory", "CAUSED (1:N)", 590, 570),
        # Team to Match (Home, 1:N routed around athlete table)
        EREdge("M 320 200 L 400 200 L 400 660 L 460 660", "start-one-optional", "end-many-mandatory", "HOME_TEAM (1:N)", 390, 430),
        # Team to Match (Away, 1:N routed around athlete table)
        EREdge("M 320 230 L 420 230 L 420 700 L 460 700", "start-one-optional", "end-many-mandatory", "AWAY_TEAM (1:N)", 410, 470),
        # Match to Events (1:N identifying)
        EREdge("M 720 650 L 860 480", "start-one-optional", "end-many-mandatory", "CONTAINS (1:N)", 780, 570),
    ]

    # 9. Relational Conversion Justifications
    relational_justifications = [
        RelationalJustification(
            title="1. Conversion of 1:1 Relationship (HEAD_COACH)",
            color_class="border-blue-500",
            description="Because TEAM has total participation, head_coach_id is placed in TEAM with a UNIQUE constraint, ensuring a coach manages at most one team.",
        ),
        RelationalJustification(
            title="2. Conversion of Multi-Valued Attribute (TEAM_COLOR)",
            color_class="border-purple-500",
            description="The multi-valued colors attribute is exported to relational table TEAM_COLOR with composite Primary Key (team_id, color_name) and foreign key referencing TEAM.",
        ),
        RelationalJustification(
            title="3. Conversion of Weak Entities (MATCH_EVENT, INJURY_RECORD)",
            color_class="border-red-500",
            description="The MATCH_EVENT table has composite PK (match_id, event_seq_no) with ON DELETE CASCADE. The INJURY_RECORD table has composite PK (athlete_id, incident_no).",
        ),
        RelationalJustification(
            title="4. Dual 1:N Role Relationships (Home and Away Teams)",
            color_class="border-amber-500",
            description="The MATCH table includes two distinct Foreign Keys referencing TEAM (home_team_id, away_team_id) enforced with CHECK (home_team_id <> away_team_id).",
        ),
    ]

    # 10. Complete Production SQL DDL
    sql_ddl = """-- ==========================================================
-- PostgreSQL / MySQL Relational Schema for Sports League Federation
-- Case Study: Exam Paper 8 (National Sports League Federation)
-- ==========================================================

-- 1. Entity: COACH (Coaches)
CREATE TABLE COACH (
    coach_id VARCHAR(15) PRIMARY KEY,
    tax_id VARCHAR(10) NOT NULL UNIQUE,
    full_name VARCHAR(100) NOT NULL,
    date_of_birth DATE NOT NULL,
    nationality VARCHAR(50) NOT NULL,
    license_tier VARCHAR(50) NOT NULL,
    phone_number VARCHAR(20) NOT NULL
);

-- 2. Entity: TEAM (Teams)
CREATE TABLE TEAM (
    team_id VARCHAR(10) PRIMARY KEY,
    team_name VARCHAR(100) NOT NULL UNIQUE,
    home_city VARCHAR(60) NOT NULL,
    founding_year INT NOT NULL CHECK (founding_year >= 1850),
    home_stadium VARCHAR(100) NOT NULL,
    seating_capacity INT NOT NULL CHECK (seating_capacity > 0),
    head_coach_id VARCHAR(15) NOT NULL UNIQUE,
    coach_appointment_date DATE NOT NULL,
    FOREIGN KEY (head_coach_id) REFERENCES COACH(coach_id) ON DELETE RESTRICT
);

-- 3. Multi-valued Attribute: TEAM_COLOR
CREATE TABLE TEAM_COLOR (
    team_id VARCHAR(10) NOT NULL,
    color_name VARCHAR(30) NOT NULL,
    PRIMARY KEY (team_id, color_name),
    FOREIGN KEY (team_id) REFERENCES TEAM(team_id) ON DELETE CASCADE
);

-- 4. Entity: ATHLETE (Athletes & Professional Contracts)
CREATE TABLE ATHLETE (
    athlete_id VARCHAR(20) PRIMARY KEY,
    national_id VARCHAR(10) NOT NULL UNIQUE,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    height_cm INT NOT NULL CHECK (height_cm BETWEEN 120 AND 250),
    weight_kg INT NOT NULL CHECK (weight_kg BETWEEN 40 AND 200),
    nationality VARCHAR(50) NOT NULL,
    playing_position VARCHAR(50) NOT NULL,
    team_id VARCHAR(10) NOT NULL,
    jersey_number INT NOT NULL CHECK (jersey_number BETWEEN 1 AND 99),
    contract_start_date DATE NOT NULL,
    contract_end_date DATE NOT NULL,
    annual_salary DECIMAL(12, 2) NOT NULL CHECK (annual_salary >= 0),
    FOREIGN KEY (team_id) REFERENCES TEAM(team_id) ON DELETE RESTRICT,
    CHECK (contract_end_date > contract_start_date)
);

-- 5. Weak Entity: INJURY_RECORD (Injury Records)
CREATE TABLE INJURY_RECORD (
    athlete_id VARCHAR(20) NOT NULL,
    incident_no INT NOT NULL CHECK (incident_no > 0),
    injury_date DATE NOT NULL,
    injury_type VARCHAR(100) NOT NULL,
    recovery_weeks INT NOT NULL CHECK (recovery_weeks >= 0),
    clearance_date DATE,
    PRIMARY KEY (athlete_id, incident_no),
    FOREIGN KEY (athlete_id) REFERENCES ATHLETE(athlete_id) ON DELETE CASCADE
);

-- 6. Entity: MATCH (League Matches)
CREATE TABLE MATCH (
    match_id VARCHAR(20) PRIMARY KEY,
    round_number INT NOT NULL CHECK (round_number > 0),
    match_start_time TIMESTAMP NOT NULL,
    stadium_venue VARCHAR(100) NOT NULL,
    referee_name VARCHAR(100) NOT NULL,
    home_team_id VARCHAR(10) NOT NULL,
    away_team_id VARCHAR(10) NOT NULL,
    score_home INT CHECK (score_home >= 0),
    score_away INT CHECK (score_away >= 0),
    FOREIGN KEY (home_team_id) REFERENCES TEAM(team_id) ON DELETE RESTRICT,
    FOREIGN KEY (away_team_id) REFERENCES TEAM(team_id) ON DELETE RESTRICT,
    CHECK (home_team_id <> away_team_id)
);

-- 7. Weak Entity: MATCH_EVENT (Match Events)
CREATE TABLE MATCH_EVENT (
    match_id VARCHAR(20) NOT NULL,
    event_seq_no INT NOT NULL CHECK (event_seq_no > 0),
    match_minute INT NOT NULL CHECK (match_minute BETWEEN 1 AND 130),
    event_type VARCHAR(40) NOT NULL CHECK (
        event_type IN ('Goal', 'Yellow Card', 'Red Card', 'Substitution', 'Penalty Kick', 'Own Goal')
    ),
    athlete_id VARCHAR(20) NOT NULL,
    PRIMARY KEY (match_id, event_seq_no),
    FOREIGN KEY (match_id) REFERENCES MATCH(match_id) ON DELETE CASCADE,
    FOREIGN KEY (athlete_id) REFERENCES ATHLETE(athlete_id) ON DELETE RESTRICT
);

-- Performance Indexes
CREATE INDEX idx_athlete_team ON ATHLETE(team_id);
CREATE INDEX idx_match_teams ON MATCH(home_team_id, away_team_id, round_number);
CREATE INDEX idx_events_match ON MATCH_EVENT(match_id, match_minute);
CREATE INDEX idx_injuries_athlete ON INJURY_RECORD(athlete_id);
"""

    return Scenario(
        id="sports_league",
        title="Professional Sports League Federation Management System",
        subtitle="Teams, Athletes, Coaches, Professional Contracts, League Fixtures, Match Events & Injury Medical History",
        course_tag="Databases (Progress Test 2025-2026 - Problem 8)",
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
