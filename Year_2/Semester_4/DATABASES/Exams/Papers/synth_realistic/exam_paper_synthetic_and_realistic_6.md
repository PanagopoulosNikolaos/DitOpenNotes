**Databases - Midterm Exam / Progress Test**
**Department of Informatics and Telecommunications**
**Academic Year 2025-2026**

---

### Scenario Description (Topic)

A global digital video streaming and cinematic media production platform is architecting its database system to manage audiovisual titles (movies and series), cast and crew contributors, user accounts, viewing profiles, streaming logs, and audience reviews.

1. **Media Titles (Audiovisual Works):**
   Each media work is identified by a globally unique ISAN (International Standard Audiovisual Number, e.g., `0000-0001-2345-0000`), original title, production/release year, maturity age rating (e.g., "PG-13", "18+"), primary genre category (e.g., "Sci-Fi", "Drama", "Psychological Thriller"), and synopsis overview. Each title is available in multiple audio dubbing languages and multiple subtitle languages (recorded as multi-valued language lists). Titles are categorized into standalone feature Movies (with a specific runtime duration in minutes) and episodic TV Series.

2. **TV Series Episodes:**
   For each TV series, there are distinct sequential episodes. An episode is identified by its Season Number and Episode Number within the respective TV series. For each episode, the system records: episode title, duration in minutes, and original premiere release date. An episode cannot exist independently without its parent TV series.

3. **Cast & Crew Contributors:**
   For each creative contributor (e.g., actors, directors, writers), the database maintains: unique Contributor ID, first name, last name, date of birth, nationality, and brief artistic biography. Contributors participate in media titles in designated creative roles (e.g., "Director", "Lead Actor", "Screenwriter", "Cinematographer") with their associated credit billing order and fictional character name (for actors).

4. **Subscribers & User Viewing Profiles:**
   Each subscriber customer account has: unique Subscriber ID, Tax ID (AFM), account email, registration date, subscription tier (e.g., "Basic", "Standard 1080p", "Premium 4K HDR"), and monthly subscription price. Under each subscriber account, users may create multiple Viewing Profiles (profile name is unique only within the parent subscriber account, with chosen avatar icon, maturity rating filter, and preferred interface language).

5. **Streaming Playback History:**
   When a profile watches content, a playback session event is logged with: unique stream session identifier, watching profile, target movie or episode, streaming start timestamp, total duration watched in minutes, playback device type (e.g., "Smart TV", "Mobile iOS", "Web Browser"), and whether playback completed.

6. **Ratings & User Reviews:**
   Viewing profiles can submit user reviews and ratings for media titles. For each review, the following are tracked: submission timestamp, numeric star rating (1 to 5 stars), written review commentary, and helpfulness approval score.

---

### Exam Questions

#### A (4 points): Conceptual Analysis

In the text above, identify and document:

1. The **entities** (and their type: strong or weak; for weak entities indicate the identifying entity).
2. The **attributes** of each entity (and their type: simple, composite, single-valued, multi-valued, derived).
3. The **keys** (how many each entity has, their type, and your final choice for the primary key; for weak entities the partial key).
4. The **relationships** and the **cardinality ratio** (1:1, 1:N, N:M), with full justification.

#### B (3 points): E-R Diagram

Draw the **Entity-Relationship (E-R)** diagram for this database. You are free (within the framework defined by the above specifications) to make any choices you consider appropriate, providing the rationale you consider correct.

#### C (3 points): Table Structure

Then show the structure of the tables with which the database will be implemented according to the diagram you drew. The tables must be written in tabular format, with **underlining of the primary key** and clear indication of the **foreign keys** (and the tables/columns to which they refer).

**Good luck!**
