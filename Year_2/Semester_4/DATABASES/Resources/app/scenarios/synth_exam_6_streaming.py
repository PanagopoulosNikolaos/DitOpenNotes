"""Streaming Platform and Digital Content case study scenario module.

Contains the complete parsed and modeled ER analysis for the Global On-demand Streaming Platform
(Media Titles, Movies, TV Series, Episodes, Cast & Crew, Subscribers, Profiles, Viewing History & Ratings),
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


def createStreamingPlatformScenario() -> Scenario:
    """Constructs and returns the Streaming Platform database scenario.

    Returns:
        Scenario: Fully populated scenario instance.
    """
    # 1. Text Paragraphs with Interactive Segments
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="A global digital video streaming and cinematic media production platform (On-demand Streaming Platform) is architecting its database system to manage "),
                TextSegment(
                    text="media titles / works (movies and series)",
                    is_highlight=True,
                    category="entity",
                    tag_label="ENTITY (SUPERCLASS)",
                    badge_class="badge-entity-strong",
                    tooltip="Strong Entity (Superclass): Digital audiovisual work with unique ISAN.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="cast & crew",
                    is_highlight=True,
                    category="entity",
                    tag_label="ENTITY",
                    badge_class="badge-entity-strong",
                    tooltip="Strong Entity: Actor, director, or creator with unique contributor ID.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="subscribers",
                    is_highlight=True,
                    category="entity",
                    tag_label="ENTITY",
                    badge_class="badge-entity-strong",
                    tooltip="Strong Entity: Account holder with unique email address.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="user profiles",
                    is_highlight=True,
                    category="entity",
                    tag_label="WEAK ENTITY",
                    badge_class="badge-entity-weak",
                    tooltip="Weak Entity: User profile dependent on the parent subscriber account.",
                ),
                TextSegment(text=", and "),
                TextSegment(
                    text="viewing history and ratings",
                    is_highlight=True,
                    category="rel",
                    tag_label="N:M RELATIONSHIP",
                    badge_class="badge-rel-nm",
                    tooltip="N:M Relationship (WATCH_HISTORY): Logging playback sessions and reviews per profile.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color=None,
        ),
        Paragraph(
            segments=[
                TextSegment(text="1. <strong>Audiovisual Works (Media Titles):</strong> Each media work is identified by a "),
                TextSegment(
                    text="globally unique ISAN code (International Standard Audiovisual Number)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Primary Key: Globally unique ISAN code.",
                ),
                TextSegment(text=", the "),
                TextSegment(text="original title", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="production / release year", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="maturity age rating (e.g., 'PG-13', '18+')", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="primary genre / category ('Sci-Fi', 'Drama', 'Action')", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", and the "),
                TextSegment(text="synopsis overview", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=". Each title is available in "),
                TextSegment(
                    text="multiple audio dubbing languages (Audio Tracks)",
                    is_highlight=True,
                    category="attr",
                    tag_label="MULTI-VALUED",
                    badge_class="badge-attr-multi",
                    tooltip="Multi-Valued Attribute: Exported to the AUDIO_LANGUAGE relation.",
                ),
                TextSegment(text=" and "),
                TextSegment(
                    text="multiple subtitle languages (Subtitles)",
                    is_highlight=True,
                    category="attr",
                    tag_label="MULTI-VALUED",
                    badge_class="badge-attr-multi",
                    tooltip="Multi-Valued Attribute: Exported to the SUBTITLE_LANGUAGE relation.",
                ),
                TextSegment(text=" recorded as lists of available languages. Works are categorized into standalone "),
                TextSegment(
                    text="Movies (with a specific runtime duration in minutes)",
                    is_highlight=True,
                    category="entity",
                    tag_label="SUBCLASS",
                    badge_class="badge-entity-strong",
                    tooltip="Specialization / Subclass: MOVIE table with runtime duration in minutes.",
                ),
                TextSegment(text=" and "),
                TextSegment(
                    text="TV Series",
                    is_highlight=True,
                    category="entity",
                    tag_label="SUBCLASS",
                    badge_class="badge-entity-strong",
                    tooltip="Specialization / Subclass: TV_SERIES table containing episodes.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-blue-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="2. <strong>TV Series Episodes:</strong> For each TV series, there are distinct sequential episodes. Each episode is identified by the "),
                TextSegment(
                    text="season number and episode sequence number within the specific series",
                    is_highlight=True,
                    category="key",
                    tag_label="PARTIAL KEY",
                    badge_class="badge-key-partial",
                    tooltip="Partial Key: (season_number, episode_number) within the series ISAN.",
                ),
                TextSegment(text=". For each episode, the system records the "),
                TextSegment(text="episode title", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="duration in minutes", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", and the "),
                TextSegment(text="original premiere release date", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=". "),
                TextSegment(
                    text="An episode cannot exist independently without its parent TV series",
                    is_highlight=True,
                    category="entity",
                    tag_label="WEAK ENTITY",
                    badge_class="badge-entity-weak",
                    tooltip="Existential Dependency: Identifying owner entity is TV_SERIES.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-amber-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="3. <strong>Cast & Crew Contributors:</strong> For each creative contributor, the database maintains: a "),
                TextSegment(
                    text="unique Contributor Registry Number (Contributor ID)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Primary Key: Unique contributor registry identifier.",
                ),
                TextSegment(text=", the "),
                TextSegment(text="full name", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="stage name", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="date of birth", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="nationality", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", and the "),
                TextSegment(text="artistic biography", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=". A contributor "),
                TextSegment(
                    text="participates in the production of multiple titles in diverse roles (Director, Screenwriter, Lead Actor)",
                    is_highlight=True,
                    category="rel",
                    tag_label="N:M RELATIONSHIP",
                    badge_class="badge-rel-nm",
                    tooltip="N:M Relationship (CREW_PARTICIPATION): Junction relation between Media Title and Cast & Crew.",
                ),
                TextSegment(text=". For each participation of an actor in a work, the system records the "),
                TextSegment(
                    text="character / role name portrayed",
                    is_highlight=True,
                    category="attr",
                    tag_label="RELATIONSHIP ATTRIBUTE",
                    badge_class="badge-attr-simple",
                    tooltip="Relationship Attribute: Script character name.",
                ),
                TextSegment(text=" and the "),
                TextSegment(
                    text="contracted compensation fee",
                    is_highlight=True,
                    category="attr",
                    tag_label="RELATIONSHIP ATTRIBUTE",
                    badge_class="badge-attr-simple",
                    tooltip="Relationship Attribute: Agreed compensation fee.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-purple-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="4. <strong>Subscribers:</strong> For each subscriber, the system records: the "),
                TextSegment(
                    text="unique email address",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Primary Key: Unique account email.",
                ),
                TextSegment(text=", the "),
                TextSegment(
                    text="unique username",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Candidate Key: Unique account username handle.",
                ),
                TextSegment(text=", the "),
                TextSegment(text="cryptographic password hash", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="registration date", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="billing country", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", and the "),
                TextSegment(text="subscription plan tier ('Basic', 'Standard HD', 'Premium 4K')", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=". A subscriber maintains one or more "),
                TextSegment(
                    text="valid payment methods (Credit Card, PayPal)",
                    is_highlight=True,
                    category="attr",
                    tag_label="MULTI-VALUED",
                    badge_class="badge-attr-multi",
                    tooltip="Multi-Valued Attribute: Normalized in the PAYMENT_METHOD table.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-emerald-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="5. <strong>User Profiles:</strong> Each subscriber can create "),
                TextSegment(
                    text="multiple profiles within their account ('Parents', 'Kids', 'Personal')",
                    is_highlight=True,
                    category="rel",
                    tag_label="1:N RELATIONSHIP",
                    badge_class="badge-rel-1n",
                    tooltip="1:N Relationship (CREATES_PROFILE): Identifying relationship between subscriber and profile.",
                ),
                TextSegment(text=". Each profile is identified by the "),
                TextSegment(
                    text="profile name within the specific subscriber account",
                    is_highlight=True,
                    category="key",
                    tag_label="PARTIAL KEY",
                    badge_class="badge-key-partial",
                    tooltip="Partial Key: Identifies the profile only in conjunction with the subscriber email.",
                ),
                TextSegment(text=", the "),
                TextSegment(text="selected avatar icon", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="interface display language", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", whether it is a "),
                TextSegment(text="kids profile (Kids Profile - Boolean)", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", and the "),
                TextSegment(text="four-digit parental control PIN", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text="."),
            ],
            accent_border_color="border-rose-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="6. <strong>Watch History & Reviews:</strong> Each profile watches various media titles and episodes. For each playback session, the system records the "),
                TextSegment(
                    text="exact stream start timestamp",
                    is_highlight=True,
                    category="attr",
                    tag_label="RELATIONSHIP ATTRIBUTE",
                    badge_class="badge-attr-simple",
                    tooltip="Relationship Attribute: Timestamp when stream playback began.",
                ),
                TextSegment(text=", the "),
                TextSegment(
                    text="playback progress in seconds",
                    is_highlight=True,
                    category="attr",
                    tag_label="RELATIONSHIP ATTRIBUTE",
                    badge_class="badge-attr-simple",
                    tooltip="Relationship Attribute: Playback resume position in seconds.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="whether playback completed (Completed - Boolean)",
                    is_highlight=True,
                    category="attr",
                    tag_label="RELATIONSHIP ATTRIBUTE",
                    badge_class="badge-attr-simple",
                    tooltip="Relationship Attribute: Viewing completion indicator.",
                ),
                TextSegment(text=", and the optional "),
                TextSegment(
                    text="user review and rating (1 to 5 star rating and review submission date)",
                    is_highlight=True,
                    category="attr",
                    tag_label="RELATIONSHIP ATTRIBUTE",
                    badge_class="badge-attr-simple",
                    tooltip="Relationship Attribute: Numeric star rating and review submission date.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-cyan-500",
        ),
    ]

    # 2. Detailed Entities List
    entities = [
        Entity(
            name="MEDIA_TITLE (Audiovisual Title / Media Item)",
            entity_type="Strong Entity (Superclass)",
            is_weak=False,
            owner_entity=None,
            justification="Central content entity uniquely identified by international standard ISAN. Acts as the generalization superclass for Movies and TV Series.",
            attributes=[
                Attribute("isan", "Simple / Single-valued", is_pk=True, notes="International Standard Audiovisual Number (PK)"),
                Attribute("original_title", "Simple / Single-valued", notes="Original production title"),
                Attribute("release_year", "Simple / Single-valued", notes="Year of initial release"),
                Attribute("maturity_rating", "Simple / Single-valued", notes="Age certification ('G', 'PG', 'PG-13', '18+')"),
                Attribute("primary_genre", "Simple / Single-valued", notes="Primary genre classification ('Sci-Fi', 'Drama', 'Action')"),
                Attribute("synopsis", "Simple / Single-valued", notes="Plot summary overview"),
                Attribute("audio_language", "Multi-valued", notes="Available audio dubbing languages (AUDIO_LANGUAGE table)"),
                Attribute("subtitle_language", "Multi-valued", notes="Available subtitle languages (SUBTITLE_LANGUAGE table)"),
            ],
        ),
        Entity(
            name="MOVIE",
            entity_type="Strong Entity (Subclass)",
            is_weak=False,
            owner_entity=None,
            justification="Specialization of MEDIA_TITLE for standalone feature-length film productions.",
            attributes=[
                Attribute("isan", "Simple / Single-valued", is_pk=True, is_fk=False, notes="Movie ISAN (PK & FK referencing MEDIA_TITLE)"),
                Attribute("runtime_minutes", "Simple / Single-valued", notes="Total runtime duration in minutes"),
            ],
        ),
        Entity(
            name="TV_SERIES",
            entity_type="Strong Entity (Subclass)",
            is_weak=False,
            owner_entity=None,
            justification="Specialization of MEDIA_TITLE for serialized multi-episode productions.",
            attributes=[
                Attribute("isan", "Simple / Single-valued", is_pk=True, is_fk=False, notes="Series ISAN (PK & FK referencing MEDIA_TITLE)"),
            ],
        ),
        Entity(
            name="EPISODE",
            entity_type="Weak Entity",
            is_weak=True,
            owner_entity="TV_SERIES",
            justification="Weak entity with existential dependency on TV_SERIES. Identified by the series ISAN and composite partial key (season_number, episode_number).",
            attributes=[
                Attribute("season_number", "Simple / Single-valued", is_partial=True, notes="Season / cycle sequence number"),
                Attribute("episode_number", "Simple / Single-valued", is_partial=True, notes="Episode sequence number within season"),
                Attribute("episode_title", "Simple / Single-valued", notes="Title of the specific episode"),
                Attribute("runtime_minutes", "Simple / Single-valued", notes="Episode duration in minutes"),
                Attribute("premiere_date", "Simple / Single-valued", notes="Original air / release date"),
            ],
        ),
        Entity(
            name="CAST_CREW",
            entity_type="Strong Entity",
            is_weak=False,
            owner_entity=None,
            justification="Independent creative professional / contributor entity with a unique registry number.",
            attributes=[
                Attribute("contributor_id", "Simple / Single-valued", is_pk=True, notes="Unique Contributor Registry ID (PK)"),
                Attribute("full_name", "Simple / Single-valued", notes="Legal full name of contributor"),
                Attribute("stage_name", "Simple / Single-valued", notes="Artistic pseudonym or stage name"),
                Attribute("date_of_birth", "Simple / Single-valued", notes="Date of birth"),
                Attribute("nationality", "Simple / Single-valued", notes="Country of citizenship / nationality"),
                Attribute("biography", "Simple / Single-valued", notes="Artistic biographical background"),
            ],
        ),
        Entity(
            name="SUBSCRIBER",
            entity_type="Strong Entity",
            is_weak=False,
            owner_entity=None,
            justification="Natural person customer holding a subscription account with a unique email address.",
            attributes=[
                Attribute("email", "Simple / Single-valued", is_pk=True, notes="Unique account email address (PK)"),
                Attribute("username", "Simple / Single-valued", is_candidate=True, notes="Unique account username handle (Candidate Key)"),
                Attribute("password_hash", "Simple / Single-valued", notes="Cryptographic password hash"),
                Attribute("registration_date", "Simple / Single-valued", notes="Account registration date"),
                Attribute("billing_country", "Simple / Single-valued", notes="Country for billing / VAT purposes"),
                Attribute("subscription_tier", "Simple / Single-valued", notes="Subscription plan tier ('Basic', 'Standard HD', 'Premium 4K')"),
                Attribute("payment_method", "Multi-valued", notes="Multiple payment methods (PAYMENT_METHOD table)"),
            ],
        ),
        Entity(
            name="USER_PROFILE",
            entity_type="Weak Entity",
            is_weak=True,
            owner_entity="SUBSCRIBER",
            justification="Weak entity existing strictly within a subscriber account. Identified by subscriber email and profile name.",
            attributes=[
                Attribute("profile_name", "Simple / Single-valued", is_partial=True, notes="Partial Key: Profile name within subscriber account"),
                Attribute("avatar_icon", "Simple / Single-valued", notes="Avatar icon identifier / filename"),
                Attribute("ui_language", "Simple / Single-valued", notes="Preferred interface display language"),
                Attribute("is_kids", "Simple / Single-valued", notes="Kids-restricted content profile flag (Boolean)"),
                Attribute("parental_pin", "Simple / Single-valued", notes="Four-digit parental control PIN"),
            ],
        ),
    ]

    # 3. Relationship Attributes
    relationship_attributes = [
        RelationshipAttribute(
            name="role_title",
            relationship_name="CREW_PARTICIPATION",
            justification="Role or function on production (e.g., 'Director', 'Screenwriter', 'Lead Actor').",
        ),
        RelationshipAttribute(
            name="character_name",
            relationship_name="CREW_PARTICIPATION",
            justification="Fictional character name portrayed by an actor in the script.",
        ),
        RelationshipAttribute(
            name="contracted_fee",
            relationship_name="CREW_PARTICIPATION",
            justification="Agreed monetary compensation fee for the contributor's participation.",
        ),
        RelationshipAttribute(
            name="stream_start_timestamp",
            relationship_name="WATCH_HISTORY",
            justification="Precise timestamp when media playback session commenced.",
        ),
        RelationshipAttribute(
            name="playback_progress_sec",
            relationship_name="WATCH_HISTORY",
            justification="Playback progress in elapsed seconds for resuming playback.",
        ),
        RelationshipAttribute(
            name="is_completed",
            relationship_name="WATCH_HISTORY",
            justification="Boolean flag indicating whether content playback finished.",
        ),
        RelationshipAttribute(
            name="rating_stars",
            relationship_name="WATCH_HISTORY",
            justification="User evaluation score (1 to 5 integer rating stars).",
        ),
        RelationshipAttribute(
            name="review_date",
            relationship_name="WATCH_HISTORY",
            justification="Submission date of user rating and commentary.",
        ),
    ]

    # 4. Keys Analysis Table
    keys_analysis = [
        KeyAnalysisRow(
            entity_name="MEDIA_TITLE (Audiovisual Title / Media Item)",
            key_count="1 Candidate",
            key_types="Candidate: {isan}",
            final_pk_selection="isan",
            justification="Globally unique ISAN code for audiovisual productions.",
        ),
        KeyAnalysisRow(
            entity_name="MOVIE",
            key_count="1 Candidate (Inherited)",
            key_types="Candidate: {isan}",
            final_pk_selection="isan",
            justification="Primary key and Foreign Key referencing superclass MEDIA_TITLE.",
        ),
        KeyAnalysisRow(
            entity_name="TV_SERIES",
            key_count="1 Candidate (Inherited)",
            key_types="Candidate: {isan}",
            final_pk_selection="isan",
            justification="Primary key and Foreign Key referencing superclass MEDIA_TITLE.",
        ),
        KeyAnalysisRow(
            entity_name="EPISODE",
            key_count="Weak Entity (2 Partial Keys)",
            key_types="Partial Keys: {season_number, episode_number}",
            final_pk_selection="(isan, season_number, episode_number)",
            justification="Composite primary key: Series ISAN + Season Number + Episode Number.",
            is_weak=True,
        ),
        KeyAnalysisRow(
            entity_name="CAST_CREW",
            key_count="1 Candidate",
            key_types="Candidate: {contributor_id}",
            final_pk_selection="contributor_id",
            justification="Unique contributor registry number identifier.",
        ),
        KeyAnalysisRow(
            entity_name="SUBSCRIBER",
            key_count="2 Candidates",
            key_types="Candidates: {email}, {username}",
            final_pk_selection="email",
            justification="Email provides standard identity verification and communication endpoint.",
        ),
        KeyAnalysisRow(
            entity_name="USER_PROFILE",
            key_count="Weak Entity (1 Partial Key)",
            key_types="Partial Key: {profile_name}",
            final_pk_selection="(email, profile_name)",
            justification="Composite primary key: Subscriber email + Profile name.",
            is_weak=True,
        ),
    ]

    # 5. Relationships List
    relationships = [
        Relationship(
            letter_id="a",
            name="ISA HIERARCHY (Specialization / Generalization)",
            connected_entities="MEDIA_TITLE -> MOVIE / TV_SERIES",
            cardinality="1:1 (Disjoint / Total)",
            participation="Total (Every media title is either a Movie or a Series)",
            relationship_type="Inheritance Hierarchy",
            attributes=[],
            justification="Categorization of media titles into standalone movies or episodic TV series with attribute inheritance.",
        ),
        Relationship(
            letter_id="b",
            name="CONTAINS_EPISODES",
            connected_entities="TV_SERIES <-> EPISODE",
            cardinality="1:N",
            participation="Total for Episode (1,1), Total for Series (1,N)",
            relationship_type="Identifying Relationship",
            attributes=[],
            justification="Identifying relationship of weak entity EPISODE from parent TV_SERIES.",
        ),
        Relationship(
            letter_id="c",
            name="CREW_PARTICIPATION",
            connected_entities="MEDIA_TITLE <-> CAST_CREW",
            cardinality="N:M",
            participation="Total for Media Title (1,N), Partial for Contributor (0,N)",
            relationship_type="Regular Junction Relationship",
            attributes=["role_title", "character_name", "contracted_fee"],
            justification="Multiple contributors participate in a media title, and a contributor can participate in multiple titles.",
        ),
        Relationship(
            letter_id="d",
            name="CREATES_PROFILE",
            connected_entities="SUBSCRIBER <-> USER_PROFILE",
            cardinality="1:N",
            participation="Total for Profile (1,1), Total for Subscriber (1,N)",
            relationship_type="Identifying Relationship",
            attributes=[],
            justification="Identifying relationship of weak entity USER_PROFILE from parent SUBSCRIBER.",
        ),
        Relationship(
            letter_id="e",
            name="WATCH_HISTORY",
            connected_entities="USER_PROFILE <-> MEDIA_TITLE",
            cardinality="N:M",
            participation="Partial for Profile (0,N), Partial for Media Title (0,N)",
            relationship_type="Regular Junction Relationship",
            attributes=["stream_start_timestamp", "playback_progress_sec", "is_completed", "rating_stars", "review_date"],
            justification="A profile streams and rates multiple titles/episodes, and a title is streamed by multiple user profiles.",
        ),
    ]

    # 6. Design Assumptions
    assumptions = [
        "The specialization of MEDIA_TITLE into MOVIE and TV_SERIES is implemented using Class Table Inheritance (distinct tables sharing PK/FK isan).",
        "Audio and subtitle languages are stored in separate 1:N relational tables for full 1NF normalization.",
        "Subscriber payment methods are exported to an independent PAYMENT_METHOD table.",
        "Watch history supports both standalone movies (season_number = NULL, episode_number = NULL) and episodic TV series episodes.",
        "In the CREW_PARTICIPATION table, role_title is included in the composite primary key so a contributor can hold multiple roles (e.g., director & actor) in the same title.",
    ]

    # 7. ER Diagram Tables
    er_tables = [
        ERTable(
            id="t-title",
            label="MEDIA_TITLE",
            x=50,
            y=50,
            attrs=[
                ERTableAttr("isan", pk=True),
                ERTableAttr("original_title"),
                ERTableAttr("release_year"),
                ERTableAttr("maturity_rating"),
                ERTableAttr("primary_genre"),
                ERTableAttr("synopsis"),
            ],
        ),
        ERTable(
            id="t-movie",
            label="MOVIE",
            x=50,
            y=340,
            attrs=[
                ERTableAttr("isan", pk=True, fk=True),
                ERTableAttr("runtime_minutes"),
            ],
        ),
        ERTable(
            id="t-subscriber",
            label="SUBSCRIBER",
            x=50,
            y=520,
            attrs=[
                ERTableAttr("email", pk=True),
                ERTableAttr("username"),
                ERTableAttr("password_hash"),
                ERTableAttr("registration_date"),
                ERTableAttr("billing_country"),
                ERTableAttr("subscription_tier"),
            ],
        ),
        ERTable(
            id="t-payment-method",
            label="PAYMENT_METHOD",
            x=50,
            y=800,
            attrs=[
                ERTableAttr("email", pk=True, fk=True),
                ERTableAttr("payment_method", pk=True),
            ],
        ),
        ERTable(
            id="t-series",
            label="TV_SERIES",
            x=450,
            y=50,
            attrs=[
                ERTableAttr("isan", pk=True, fk=True),
            ],
        ),
        ERTable(
            id="t-audio-lang",
            label="AUDIO_LANGUAGE",
            x=450,
            y=180,
            attrs=[
                ERTableAttr("isan", pk=True, fk=True),
                ERTableAttr("audio_language", pk=True),
            ],
        ),
        ERTable(
            id="t-subtitle-lang",
            label="SUBTITLE_LANGUAGE",
            x=450,
            y=310,
            attrs=[
                ERTableAttr("isan", pk=True, fk=True),
                ERTableAttr("subtitle_language", pk=True),
            ],
        ),
        ERTable(
            id="t-participation",
            label="CREW_PARTICIPATION",
            x=450,
            y=440,
            attrs=[
                ERTableAttr("isan", pk=True, fk=True),
                ERTableAttr("contributor_id", pk=True, fk=True),
                ERTableAttr("role_title", pk=True),
                ERTableAttr("character_name"),
                ERTableAttr("contracted_fee"),
            ],
        ),
        ERTable(
            id="t-profile",
            label="USER_PROFILE",
            x=450,
            y=690,
            attrs=[
                ERTableAttr("email", pk=True, fk=True),
                ERTableAttr("profile_name", pk=True),
                ERTableAttr("avatar_icon"),
                ERTableAttr("ui_language"),
                ERTableAttr("is_kids"),
                ERTableAttr("parental_pin"),
            ],
        ),
        ERTable(
            id="t-episode",
            label="EPISODE",
            x=850,
            y=50,
            attrs=[
                ERTableAttr("isan", pk=True, fk=True),
                ERTableAttr("season_number", pk=True),
                ERTableAttr("episode_number", pk=True),
                ERTableAttr("episode_title"),
                ERTableAttr("runtime_minutes"),
                ERTableAttr("premiere_date"),
            ],
        ),
        ERTable(
            id="t-creator",
            label="CAST_CREW",
            x=850,
            y=440,
            attrs=[
                ERTableAttr("contributor_id", pk=True),
                ERTableAttr("full_name"),
                ERTableAttr("stage_name"),
                ERTableAttr("date_of_birth"),
                ERTableAttr("nationality"),
                ERTableAttr("biography"),
            ],
        ),
        ERTable(
            id="t-history",
            label="WATCH_HISTORY",
            x=850,
            y=710,
            attrs=[
                ERTableAttr("email", pk=True, fk=True),
                ERTableAttr("profile_name", pk=True, fk=True),
                ERTableAttr("isan", pk=True, fk=True),
                ERTableAttr("stream_start_timestamp", pk=True),
                ERTableAttr("season_number", fk=True),
                ERTableAttr("episode_number", fk=True),
                ERTableAttr("playback_progress_sec"),
                ERTableAttr("is_completed"),
                ERTableAttr("rating_stars"),
                ERTableAttr("review_date"),
            ],
        ),
    ]

    # 8. ER Diagram Edges
    er_edges = [
        # Media to Series (ISA)
        EREdge("M 310 80 L 450 80", "start-one-mandatory", "end-one-mandatory", "ISA (SERIES)", 380, 70),
        # Media to Movie (ISA)
        EREdge("M 180 266 L 180 340", "start-one-mandatory", "end-one-mandatory", "ISA (MOVIE)", 195, 300),
        # Series to Episodes (1:N identifying)
        EREdge("M 710 80 L 850 80", "start-one-mandatory", "end-many-mandatory", "CONTAINS (1:N)", 780, 70),
        # Media to Audio Languages (1:N multivalued)
        EREdge("M 310 160 L 450 200", "start-one-mandatory", "end-many-mandatory", "AUDIO_LANG (1:N)", 380, 170),
        # Media to Subtitles (1:N multivalued)
        EREdge("M 310 210 L 450 330", "start-one-mandatory", "end-many-mandatory", "SUBTITLES (1:N)", 380, 260),
        # Media to Participation (1:N)
        EREdge("M 310 240 L 450 460", "start-one-mandatory", "end-many-mandatory", "PARTICIPATION (1:N)", 380, 340),
        # Creator to Participation (1:N)
        EREdge("M 850 480 L 710 480", "start-one-optional", "end-many-mandatory", "PARTICIPATES (1:N)", 780, 470),
        # Subscriber to Profile (1:N identifying)
        EREdge("M 310 630 L 450 710", "start-one-mandatory", "end-many-mandatory", "CREATES (1:N)", 380, 660),
        # Subscriber to Payment methods (1:N multivalued)
        EREdge("M 180 736 L 180 800", "start-one-mandatory", "end-many-mandatory", "PAYMENT (1:N)", 195, 768),
        # Profile to History (1:N)
        EREdge("M 710 740 L 850 740", "start-one-optional", "end-many-mandatory", "WATCHES (1:N)", 780, 730),
        # Media to History (1:N routed around profile and subscriber)
        EREdge("M 310 250 L 390 250 L 390 980 L 850 980", "start-one-optional", "end-many-mandatory", "STREAM (1:N)", 590, 970),
    ]

    # 9. Relational Conversion Justifications
    relational_justifications = [
        RelationalJustification(
            title="1. Conversion of Generalization / Specialization Hierarchy (MEDIA_TITLE -> MOVIE, TV_SERIES)",
            color_class="border-blue-500",
            description="Class Table Inheritance pattern: Creates the base relation MEDIA_TITLE (holding common attributes) and specialized tables MOVIE and TV_SERIES with isan as both Primary Key and Foreign Key referencing MEDIA_TITLE.",
        ),
        RelationalJustification(
            title="2. Conversion of Weak Entities (EPISODE, USER_PROFILE)",
            color_class="border-red-500",
            description="The EPISODE table is assigned composite primary key (isan, season_number, episode_number). The USER_PROFILE table is assigned composite primary key (email, profile_name) referencing SUBSCRIBER with ON DELETE CASCADE.",
        ),
        RelationalJustification(
            title="3. Conversion of N:M Relationships (CREW_PARTICIPATION, WATCH_HISTORY)",
            color_class="border-amber-500",
            description="Constructs junction relations CREW_PARTICIPATION (composite PK: isan, contributor_id, role_title) and WATCH_HISTORY (composite PK: email, profile_name, isan, stream_start_timestamp).",
        ),
        RelationalJustification(
            title="4. Conversion of Multi-Valued Attributes (AUDIO_LANGUAGE, SUBTITLE_LANGUAGE, PAYMENT_METHOD)",
            color_class="border-purple-500",
            description="Multi-valued attributes are converted into 1:N relations: AUDIO_LANGUAGE (isan, audio_language), SUBTITLE_LANGUAGE (isan, subtitle_language), and PAYMENT_METHOD (email, payment_method).",
        ),
    ]

    # 10. Complete Production SQL DDL
    sql_ddl = """-- ==========================================================
-- PostgreSQL / MySQL Relational Schema for Streaming Platform
-- Case Study: Exam Paper 6 (Digital Video Streaming Platform)
-- ==========================================================

-- 1. Superclass Entity: MEDIA_TITLE
CREATE TABLE MEDIA_TITLE (
    isan VARCHAR(30) PRIMARY KEY,
    original_title VARCHAR(150) NOT NULL,
    release_year INT NOT NULL CHECK (release_year >= 1895),
    maturity_rating VARCHAR(10) NOT NULL CHECK (maturity_rating IN ('G', 'PG', 'PG-13', '16+', '18+')),
    primary_genre VARCHAR(50) NOT NULL,
    synopsis TEXT NOT NULL
);

-- 2. Multi-valued Attribute: AUDIO_LANGUAGE
CREATE TABLE AUDIO_LANGUAGE (
    isan VARCHAR(30) NOT NULL,
    audio_language VARCHAR(50) NOT NULL,
    PRIMARY KEY (isan, audio_language),
    FOREIGN KEY (isan) REFERENCES MEDIA_TITLE(isan) ON DELETE CASCADE
);

-- 3. Multi-valued Attribute: SUBTITLE_LANGUAGE
CREATE TABLE SUBTITLE_LANGUAGE (
    isan VARCHAR(30) NOT NULL,
    subtitle_language VARCHAR(50) NOT NULL,
    PRIMARY KEY (isan, subtitle_language),
    FOREIGN KEY (isan) REFERENCES MEDIA_TITLE(isan) ON DELETE CASCADE
);

-- 4. Subclass Entity: MOVIE
CREATE TABLE MOVIE (
    isan VARCHAR(30) PRIMARY KEY,
    runtime_minutes INT NOT NULL CHECK (runtime_minutes > 0),
    FOREIGN KEY (isan) REFERENCES MEDIA_TITLE(isan) ON DELETE CASCADE
);

-- 5. Subclass Entity: TV_SERIES
CREATE TABLE TV_SERIES (
    isan VARCHAR(30) PRIMARY KEY,
    FOREIGN KEY (isan) REFERENCES MEDIA_TITLE(isan) ON DELETE CASCADE
);

-- 6. Weak Entity: EPISODE
CREATE TABLE EPISODE (
    isan VARCHAR(30) NOT NULL,
    season_number INT NOT NULL CHECK (season_number > 0),
    episode_number INT NOT NULL CHECK (episode_number > 0),
    episode_title VARCHAR(150) NOT NULL,
    runtime_minutes INT NOT NULL CHECK (runtime_minutes > 0),
    premiere_date DATE NOT NULL,
    PRIMARY KEY (isan, season_number, episode_number),
    FOREIGN KEY (isan) REFERENCES TV_SERIES(isan) ON DELETE CASCADE
);

-- 7. Entity: CAST_CREW
CREATE TABLE CAST_CREW (
    contributor_id VARCHAR(15) PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    stage_name VARCHAR(100),
    date_of_birth DATE NOT NULL,
    nationality VARCHAR(50) NOT NULL,
    biography TEXT
);

-- 8. Junction Table: CREW_PARTICIPATION (N:M)
CREATE TABLE CREW_PARTICIPATION (
    isan VARCHAR(30) NOT NULL,
    contributor_id VARCHAR(15) NOT NULL,
    role_title VARCHAR(50) NOT NULL CHECK (role_title IN ('Director', 'Screenwriter', 'Lead Actor', 'Supporting Actor', 'Producer')),
    character_name VARCHAR(100),
    contracted_fee DECIMAL(12, 2) CHECK (contracted_fee >= 0),
    PRIMARY KEY (isan, contributor_id, role_title),
    FOREIGN KEY (isan) REFERENCES MEDIA_TITLE(isan) ON DELETE CASCADE,
    FOREIGN KEY (contributor_id) REFERENCES CAST_CREW(contributor_id) ON DELETE CASCADE
);

-- 9. Entity: SUBSCRIBER
CREATE TABLE SUBSCRIBER (
    email VARCHAR(100) PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    registration_date DATE NOT NULL,
    billing_country VARCHAR(50) NOT NULL,
    subscription_tier VARCHAR(30) NOT NULL CHECK (subscription_tier IN ('Basic', 'Standard HD', 'Premium 4K'))
);

-- 10. Multi-valued Attribute: PAYMENT_METHOD
CREATE TABLE PAYMENT_METHOD (
    email VARCHAR(100) NOT NULL,
    payment_method VARCHAR(50) NOT NULL,
    PRIMARY KEY (email, payment_method),
    FOREIGN KEY (email) REFERENCES SUBSCRIBER(email) ON DELETE CASCADE
);

-- 11. Weak Entity: USER_PROFILE
CREATE TABLE USER_PROFILE (
    email VARCHAR(100) NOT NULL,
    profile_name VARCHAR(50) NOT NULL,
    avatar_icon VARCHAR(100) DEFAULT 'default_avatar.png',
    ui_language VARCHAR(20) DEFAULT 'en',
    is_kids BOOLEAN NOT NULL DEFAULT FALSE,
    parental_pin VARCHAR(4),
    PRIMARY KEY (email, profile_name),
    FOREIGN KEY (email) REFERENCES SUBSCRIBER(email) ON DELETE CASCADE
);

-- 12. Junction Table: WATCH_HISTORY (N:M Viewing & Ratings)
CREATE TABLE WATCH_HISTORY (
    email VARCHAR(100) NOT NULL,
    profile_name VARCHAR(50) NOT NULL,
    isan VARCHAR(30) NOT NULL,
    stream_start_timestamp TIMESTAMP NOT NULL,
    season_number INT,
    episode_number INT,
    playback_progress_sec INT NOT NULL DEFAULT 0 CHECK (playback_progress_sec >= 0),
    is_completed BOOLEAN NOT NULL DEFAULT FALSE,
    rating_stars INT CHECK (rating_stars BETWEEN 1 AND 5),
    review_date DATE,
    PRIMARY KEY (email, profile_name, isan, stream_start_timestamp),
    FOREIGN KEY (email, profile_name) REFERENCES USER_PROFILE(email, profile_name) ON DELETE CASCADE,
    FOREIGN KEY (isan) REFERENCES MEDIA_TITLE(isan) ON DELETE CASCADE,
    FOREIGN KEY (isan, season_number, episode_number) REFERENCES EPISODE(isan, season_number, episode_number) ON DELETE CASCADE
);"""

    return Scenario(
        id="streaming_platform",
        title="Digital Video Streaming Platform System",
        subtitle="Data Modeling for Media Titles (Movies/Series), Episodes, Cast & Crew, Subscribers, Profiles & Watch History",
        course_tag="Databases (Progress Test 2025-2026 - Problem 6)",
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
