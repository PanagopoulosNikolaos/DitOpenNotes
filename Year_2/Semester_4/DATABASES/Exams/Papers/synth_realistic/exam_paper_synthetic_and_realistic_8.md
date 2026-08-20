**Databases - Midterm Exam / Progress Test**
**Department of Informatics and Telecommunications**
**Academic Year 2025-2026**

---

### Scenario Description (Topic)

A national professional sports league federation is designing a relational database system to manage teams, coaching staff, professional athletes, tournament fixtures/matches, real-time match events, and athlete injury records.

1. **Clubs & Teams:**
   Each sports club is characterized by a unique Team ID (e.g., `TM-01`, `TM-02`), official club name (e.g., "Athens Athletic Club"), home city, founding year, home stadium/arena name (owned or leased), and spectator seating capacity. Each team has official club colors (e.g., "Cyan", "White", recorded as multiple colors). Each team is mandatorily guided by exactly one Head Coach, for whom the contract start date is recorded.

2. **Coaches:**
   For each coach, the following are kept: unique Coach License Number (Coach ID), Tax ID (AFM), full name, date of birth, nationality, professional coaching certification tier (e.g., "UEFA Pro", "FIBA Level 1"), and mobile contact telephone. A coach can serve as head coach for at most one team at a time.

3. **Athletes (Players):**
   For each athlete, the database tracks: unique Athlete League Registration Number, National ID (ADT), first name, last name, date of birth, height (in cm), weight (in kg), nationality, and primary playing position (e.g., "Goalkeeper", "Central Defender", "Forward"). Each athlete is under a professional contract with a single team. For each active contract, the following are recorded: player jersey squad number, contract start date, contract expiration date, and annual base salary.

4. **League Matches (Fixtures):**
   Teams compete in scheduled league matches. Each match is identified by a unique Match ID, tournament round number, scheduled match date and kickoff time, venue stadium, and assigned referee full name. Each match is contested between two specific teams: the Home Team and the Away Team. Upon completion of the match, the final score (goals/points scored by the home team and away team) is recorded.

5. **Match Events:**
   During a match, critical match events are logged in chronological detail. Each event is identified by a sequential event number within the specific match, match minute (e.g., `45'`, `89'`), event category type (e.g., "Goal", "Yellow Card", "Red Card", "Substitution", "Penalty Kick"), and the participating athlete who caused the event. A match event cannot exist independently without its associated match.

6. **Injury & Medical History:**
   The league maintains medical tracking for athlete injuries. For each injury occurrence, the system records: sequential medical incident number for the specific athlete, injury incident date, medical diagnosis/type, estimated rehabilitation recovery time (in weeks), and confirmed medical clearance return date.

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
