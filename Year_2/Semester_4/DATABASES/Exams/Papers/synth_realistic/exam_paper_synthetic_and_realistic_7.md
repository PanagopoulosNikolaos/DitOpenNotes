**Databases - Midterm Exam / Progress Test**
**Department of Informatics and Telecommunications**
**Academic Year 2025-2026**

---

### Scenario Description (Topic)

A metropolitan municipality is developing an integrated library database system for its public library branch network to manage branch facilities, bibliographic catalog titles, physical inventory copies, reader members, book loans, and hold reservations.

1. **Library Branches:**
   Each library branch is characterized by a unique Branch ID (e.g., `LIB-01`, `LIB-02`), a unique branch name (e.g., "Central Municipal Library", "Uptown Cultural Branch"), street address (street, number, postal code, neighborhood), phone number, and reader seating capacity. Each branch operates on an established weekly schedule with multiple daily opening hours (recorded as multiple operating hours). Each branch is managed by a Chief Head Librarian, for whom the appointment start date is recorded. A head librarian manages at most one branch.

2. **Book Titles & Authors:**
   For each bibliographic book title, the catalog tracks: unique ISBN (International Standard Book Number), title, publishing house, publication year, subject classification (e.g., "Computer Science", "European History", "Modern Literature"), and total page count. A book title may be authored by one or more authors. For each author, the system records: unique Author ID, author full name, nationality, and birth year.

3. **Physical Book Copies:**
   Individual branches hold physical copies of book titles. Each physical copy is identified by a unique Copy Barcode ID (or sequential copy number within the specific book title and branch), physical shelf condition (e.g., "Pristine", "Good", "Worn / Damaged"), acquisition date, call number shelf location tag, and current availability status (e.g., "Available on Shelf", "Checked Out", "Under Restoration").

4. **Library Members (Readers):**
   For each registered member, the following are kept: unique Membership Card Number, Tax ID (AFM), first name, last name, date of birth, membership registration date, card expiration date, email, mobile phone, and residential address (street, number, postal code, city).

5. **Circulation Loans:**
   Members borrow physical book copies. For each loan transaction, the system logs: unique Loan Reference Number, borrowing member, specific physical book copy, loan checkout timestamp, scheduled due date, actual return date, and any accrued overdue late fees (derived dynamically if returned late).

6. **Hold Reservations:**
   When all copies of a desired title are currently on loan, a member can place a reservation hold for that title at a selected branch. For each reservation, the following are recorded: unique Reservation ID, requesting member, target book title, pickup branch, request timestamp, queue priority position, and hold fulfillment status (e.g., "Active Pending", "Ready for Pickup", "Fulfilled", "Expired").

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
