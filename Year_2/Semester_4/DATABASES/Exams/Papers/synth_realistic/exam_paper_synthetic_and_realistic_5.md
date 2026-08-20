**Databases - Midterm Exam / Progress Test**
**Department of Informatics and Telecommunications**
**Academic Year 2025-2026**

---

### Scenario Description (Topic)

A global e-commerce retail platform is engineering a scalable relational database architecture to manage product categories, vendor supply chains, customer accounts, order processing, and payment fulfillment.

1. **Product Categories:**
   Each product category is characterized by a unique Category Code (e.g., `CAT_ELEC`, `CAT_AUDIO`), a unique category name (e.g., "Consumer Electronics", "Headphones & Audio"), a descriptive summary, and an optional reference to a Parent Category (hierarchical tree of categories). Each top-level category is overseen by a designated Category Product Manager, for whom the date of appointment is recorded. A manager oversees at most one primary category.

2. **Products & Inventory:**
   For each product, the catalog tracks: unique SKU / Product Code (e.g., `PRD-98234`), commercial product title, brand/manufacturer, retail unit price, current warehouse stock quantity, warranty period in months, and a list of available color finishes (e.g., "Matte Black", "Silver", "Midnight Blue", recorded as multiple colors). Each product belongs mandatorily to a single product category.

3. **Suppliers & Vendors:**
   For each supplier, the following are kept: unique Supplier ID (e.g., `SUP-101`), Tax ID (AFM), corporate business name, legal representative full name, headquarters address (street, number, postal code, city, country), email address, and multiple contact telephone numbers. Suppliers supply products to the catalog (a supplier supplies multiple products, and a product may be sourced from multiple suppliers). For each supply partnership, the wholesale supply unit cost and minimum lead time (in days) are recorded.

4. **Customers (Users):**
   For each registered customer, the system records: unique Customer ID, Tax ID (AFM), first name, last name, date of birth, account registration date, email address, mobile phone, and multiple delivery shipping addresses (each composed of street, number, postal code, city, country).

5. **Customer Orders:**
   Customers place purchase orders. Each order is identified by a unique Order Reference Number, order placement timestamp, selected delivery address, current order fulfillment status (e.g., "Payment Pending", "Processing", "Shipped", "Delivered", "Cancelled"), and total order cost (dynamically calculated from line items). Each order is placed by exactly one registered customer.

6. **Order Line Items & Payment Transactions:**
   An order contains one or more line items (Order Items). Each line item is identified by a sequential line number within that order, the ordered product SKU, quantity ordered, unit sale price at time of purchase, and applicable discount rate. Each order is settled through one or more payment transactions (each with a unique payment transaction ID, payment method such as Credit Card, PayPal, or Bank Wire, timestamp of payment, settled amount, and payment authorization code).

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
