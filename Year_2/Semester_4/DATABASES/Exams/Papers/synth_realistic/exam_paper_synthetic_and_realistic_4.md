**Databases - Midterm Exam / Progress Test**
**Department of Informatics and Telecommunications**
**Academic Year 2025-2026**

---

### Scenario Description (Topic)

A international luxury hotel resort chain is designing a unified relational database management system to manage its properties, room inventory, employee staffing, customer reservations, and on-premise guest services.

1. **Hotel Properties:**
   Each hotel property is identified by a unique Hotel Code (e.g., `HTL01`, `HTL02`), a unique property name (e.g., "Grand Palace Resort", "Seaside Luxury Hotel"), star category rating (e.g., 4-star, 5-star), geographic address (street, number, postal code, city, country), central phone number, and a list of resort amenities (e.g., "Infinity Pool", "Spa & Wellness", "Tennis Court", "Conference Center", recorded as multiple amenities). Each hotel is mandatorily managed by a designated General Manager (Employee), for whom the start date of management is recorded. A manager manages at most one hotel property.

2. **Hotel Rooms:**
   Within each hotel property, individual rooms are identified by their Room Number (e.g., `101`, `408`). A room number is unique only within the context of a specific hotel. For each room, the system records: floor level, room category type (e.g., Standard Single, Deluxe Double, Executive Suite, Presidential Suite), base nightly rate, and maximum guest occupancy capacity.

3. **Hotel Staff (Employees):**
   For each employee, the following are kept: unique Employee ID, Tax ID (AFM), first name, last name, job role/department (e.g., Front Desk Receptionist, Executive Chef, Housekeeping Supervisor, Concierge), monthly salary, hire date, residential address (street, number, postal code, city), and multiple contact telephone numbers. Each employee is assigned to work at exactly one hotel property. Furthermore, senior department supervisors oversee and guide junior staff members (each employee has one direct supervisor, while a supervisor oversees multiple employees).

4. **Guests (Customers):**
   For each guest, the following are recorded: unique Passport Number or National ID (ADT), Tax ID (AFM), first name, last name, date of birth, nationality, contact email address, and mobile telephone number.

5. **Bookings (Reservations):**
   Guests place reservations for hotel stays. Each reservation is characterized by a unique Booking Reference Code (Booking ID), reservation date, scheduled check-in date, scheduled check-out date, total duration in nights (derived dynamically), total calculated booking cost, and reservation status (e.g., "Confirmed", "Checked-In", "Completed", "Cancelled"). A booking is placed by a single primary guest and reserves one or more specific rooms.

6. **Guest Services & Charges:**
   Hotels offer various chargeable services (e.g., Airport Transfer, Spa Massage, Laundry Service, Fine Dining Room Service). Each service has a unique Service Code, service name, description, and standard unit price. When a service is provided to a guest during their stay, the service charge is logged with: sequential charge transaction number, associated booking, service rendered, timestamp of service delivery, quantity consumed, and total billed amount.

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
