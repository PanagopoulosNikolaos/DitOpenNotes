# Conceptual Modeling: Comprehensive Exercises

This lecture is dedicated to the practical application of Entity-Relationship (ER) modeling through two complex case studies: a Hospital Information System and a Supermarket Management System. These exercises consolidate concepts like specialization, weak entities, and relationship attributes.

---

## 1. Case Study 1: Hospital Information System

### 1.1. Requirements Analysis
*   **Infrastructure:** The hospital consists of **Clinics** (e.g., Cardiology) and **Laboratories** (e.g., Biochemical). 
    *   Clinics store: Name, Director, Number of Beds, and Number of Patients.
    *   Laboratories store: Name, Director, and multiple Phone Numbers.
*   **Personnel:** Staff is divided into **Doctors**, **Nurses**, and **Paramedical Staff**.
    *   Common attributes for all staff: Name, Surname, ID Number (AT).
    *   **Doctors:** Have a specialty (e.g., Internist), Employee ID (AM), and contact info (Address, City, Email, Phone). Each doctor belongs to exactly one Clinic and one Laboratory.
    *   **Nurses:** Have a specialty and contact info. Can work in multiple clinics but *not* in laboratories.
    *   **Paramedical Staff:** Have a specialty and Tax ID (AFM). Work exclusively in exactly one Laboratory.

### 1.2. Identified ER Components
| Component Type | Name | Details |
| :--- | :--- | :--- |
| **Entity** | `Clinic` | Attributes: Name (PK), Director, Beds, Patients. |
| **Entity** | `Laboratory` | Attributes: Name (PK), Director, {Phones} (Multi-valued). |
| **Entity** | `Doctor` | Attributes: **AM** (PK), Name, Surname, AT, Specialty, Address, City, Email, Phone. |
| **Entity** | `Nurse` | Attributes: Name, Surname, AT, Specialty, Address, City, Email, Phone. |
| **Entity** | `Paramedical` | Attributes: **AFM** (PK), Name, Surname, AT, Specialty. |
| **Relationship** | `Works_In` (Doctor) | Linked to Clinic (1) and Laboratory (1). |
| **Relationship** | `Employed_By` (Nurse) | Linked to Clinic (M:N). |
| **Relationship** | `Assigned_To` (Paramedical) | Linked to Laboratory (N:1). |

---

## 2. Case Study 2: Supermarket Management System

### 2.1. Requirements Analysis
*   **Supply Chain:** **Suppliers** provide **Products**. 
    *   Suppliers: Name, Address.
    *   Products: Name, Price, Code.
    *   *Constraint:* A supplier provides many products, and a product can come from many suppliers. The price is unique to each supplier-product pair.
*   **Internal Structure:** The market has **Departments**.
    *   Departments: Name, Code. Each has one Manager and many Employees.
    *   *Constraint:* A department is responsible for specific products. A product is sold by only one department.
*   **Human Resources:** **Employees** have a Name and Salary. Each works in exactly one department.
*   **Sales:** **Customers** and **Orders**.
    *   Customers: Surname, Name, ID (PK), Address, Account Balance.
    *   Orders: Code (PK), Date.
    *   *Constraint:* Customers place orders. An order consists of a list of products and their quantities.

### 2.2. Identified ER Components
| Component Type | Name | Details |
| :--- | :--- | :--- |
| **Entity** | `Supplier` | Attributes: **Name** (PK), Address. |
| **Entity** | `Product` | Attributes: **Code** (PK), Name. |
| **Entity** | `Department` | Attributes: **Code** (PK), Name. |
| **Entity** | `Employee` | Attributes: Name, Salary. |
| **Entity** | `Customer` | Attributes: **ID** (PK), Surname, Name, Address, Balance. |
| **Entity** | `Order` | Attributes: **Code** (PK), Date. |
| **Relationship** | `Provides` | Supplier (M) $\leftrightarrow$ Product (N). Attribute: `Price`. |
| **Relationship** | `Sold_By` | Product (N) $\leftrightarrow$ Department (1). |
| **Relationship** | `Works_At` | Employee (N) $\leftrightarrow$ Department (1). |
| **Relationship** | `Manages` | Employee (1) $\leftrightarrow$ Department (1). |
| **Relationship** | `Places` | Customer (1) $\leftrightarrow$ Order (N). |
| **Relationship** | `Contains` | Order (M) $\leftrightarrow$ Product (N). Attribute: `Quantity`. |

---

## Solved Exercises

### Exercise 1: Multi-valued vs. Separate Entity
**Problem:** In the Hospital case, why are Laboratory Phone Numbers multi-valued attributes rather than a separate "Phone" entity?

**Solution:**
*   **Answer:** Because the phone numbers do not have their own attributes and do not participate in relationships with other entities. They are simple descriptive values of the Laboratory.

### Exercise 2: Relationship Attributes in M:N
**Problem:** In the Supermarket case, why is "Price" an attribute of the `Provides` relationship and not the `Product` entity?

**Solution:**
*   **Answer:** Because different suppliers may sell the same product at different prices. The price is only determined when you specify *both* the product and the supplier.

### Exercise 3: Cardinality in Sales
**Problem:** What is the cardinality between `Customer` and `Order`? Why?

**Solution:**
*   **Answer:** $1:N$ (One-to-Many).
*   **Reason:** One customer can place many orders over time, but each specific order (identified by a unique order code) belongs to exactly one customer.

### Exercise 4: Specialization/Generalization
**Problem:** If we wanted to simplify the Hospital model, could we create a "Staff" superclass? What attributes would it have?

**Solution:**
*   **Answer:** Yes. 
*   **Attributes:** Name, Surname, AT, and Specialty (since all three types share these).

### Exercise 5: Total Participation in Management
**Problem:** In the Supermarket model, every Department must have a manager. How is this represented?

**Solution:**
*   **Answer:** A double line on the Department side of the `Manages` relationship.

### Exercise 6: Identifying Relationship Attributes
**Problem:** In Case 2, where is "Quantity" stored?

**Solution:**
*   **Answer:** On the `Contains` relationship between `Order` and `Product`. 
*   **Reason:** Quantity is specific to how many of a certain product are in a specific order.

### Exercise 7: Key Choice
**Problem:** For the `Customer` entity, why is `ID` a better primary key than `Surname`?

**Solution:**
*   **Answer:** Uniqueness. Multiple customers can have the same surname (e.g., "Papadopoulos"), but an ID card number is unique to one individual.

### Exercise 8: Handling Product Sales
**Problem:** Can a product be sold by two different departments in this model?

**Solution:**
*   **Answer:** No. 
*   **Reason:** The requirements state "a product can be sold by only one department," which implies a $N:1$ relationship between Product and Department.

---

## Exam Tip: Relationship Attributes vs. Entity Attributes

> **[Key Insight]**
> When deciding where to place an attribute, ask: "Does this value depend on one entity or the combination of two?"
> *   **Example:** `EmployeeSalary` depends only on the Employee (Entity attribute).
> *   **Example:** `HoursWorked` depends on both the Employee and the Project (Relationship attribute).
> In Many-to-Many relationships, descriptive attributes almost always belong to the **Relationship**.
