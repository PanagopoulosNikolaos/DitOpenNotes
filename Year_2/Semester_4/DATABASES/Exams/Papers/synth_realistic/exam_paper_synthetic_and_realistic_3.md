**Databases - Midterm Exam / Progress Test**
**Department of Informatics and Telecommunications**
**Academic Year 2025-2026**

---

### Scenario Description (Topic)

An international commercial airline is developing a database management system to manage its flight routes, aircraft fleet, scheduled flight instances, crew assignments, and passenger bookings.

1. **Airports:**
   Each airport is characterized by a unique 3-letter IATA code (e.g., `ATH`, `LHR`, `JFK`), a unique airport name, host city, country, time zone offset (e.g., UTC+2), and a list of active runway identifiers (multiple runways). Each airport operations hub is directed by a designated Chief Station Manager, for whom the appointment date is recorded. A manager directs at most one airport station.

2. **Flight Routes:**
   Each flight route is identified by a unique flight number (e.g., `OA311`, `LH1750`), departure airport (Origin), arrival airport (Destination), scheduled departure time, scheduled arrival time, and standard flight duration in minutes (calculated dynamically from departure and arrival times). A route connects exactly one origin airport and one destination airport.

3. **Aircraft Fleet:**
   For each aircraft in the fleet, the following are recorded: unique aircraft registration tail number (e.g., `SX-DVG`), manufacturer serial number, aircraft model (e.g., `Airbus A320neo`, `Boeing 737-800`), manufacturer company name, total passenger seating capacity, and year of manufacture. An aircraft undergoes periodic maintenance inspections, tracked as sequential maintenance events (each with a maintenance event number within the aircraft, inspection date, inspection type, and maintenance facility).

4. **Flight Instances:**
   A scheduled flight route operates on specific calendar dates as a distinct Flight Instance. Each flight instance is identified by the flight number combined with the departure date, and records the actual departure time, actual arrival time, departure gate, assigned aircraft, and operational status (e.g., "On Time", "Delayed", "Departed", "Arrived", "Cancelled"). Each flight instance utilizes exactly one aircraft from the fleet.

5. **Flight Crew Members (Pilots & Cabin Crew):**
   For each crew member, the following are kept: unique employee ID, Tax ID (AFM), first name, last name, crew role (e.g., Captain, First Officer, Purser, Flight Attendant), aviation license number, accumulated flight hours, hire date, residential address (street, number, postal code, city), and multiple contact telephone numbers. Crew members are assigned to work on specific flight instances. Additionally, an experienced senior Captain serves as a flight instructor/supervisor to junior First Officers (each junior officer has one designated mentor Captain, while a mentor may supervise multiple junior officers).

6. **Passengers & Bookings:**
   For each passenger, the following are recorded: unique Passport Number, National ID (ADT), first name, last name, date of birth, nationality, email address, and mobile phone. Passengers book tickets on specific flight instances. For each issued ticket/booking, the system tracks: unique electronic ticket number (E-Ticket), booking confirmation code (PNR), booking date, assigned seat number (e.g., `14A`), travel class (e.g., Economy, Premium Economy, Business), ticket fare, and payment confirmation status.

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
