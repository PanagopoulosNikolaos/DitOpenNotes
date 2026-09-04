# Exercises 01: Relational Algebra and Schema Mapping

This practice set provides worked problems with solutions on formulating formal Relational Algebra queries and applying the 7-step ER-to-Relational mapping algorithm.

---

## Problem 1: Formal Relational Algebra Expressions

### Schema Context
- $\text{Sailor}(\underline{\text{sid}}, \text{sname}, \text{rating}, \text{age})$
- $\text{Boat}(\underline{\text{bid}}, \text{bname}, \text{color})$
- $\text{Reservation}(\underline{\text{sid} \uparrow \text{Sailor}, \text{bid} \uparrow \text{Boat}, \text{day}})$

### Question 1.1
Find the names of sailors who have reserved at least one red boat.

#### Solution
1. Select red boats from $\text{Boat}$:
   $$R_1 = \sigma_{\text{color} = \text{'red'}}(\text{Boat})$$
2. Join with $\text{Reservation}$ on $\text{bid}$:
   $$R_2 = \text{Reservation} \bowtie R_1$$
3. Join with $\text{Sailor}$ on $\text{sid}$:
   $$R_3 = \text{Sailor} \bowtie R_2$$
4. Project sailor name:
   $$\pi_{\text{sname}}\left( \text{Sailor} \bowtie \left( \text{Reservation} \bowtie \sigma_{\text{color} = \text{'red'}}(\text{Boat}) \right) \right)$$

---

### Question 1.2
Find the sailor IDs of sailors who have reserved **all** boats.

#### Solution
This is universal quantification, which maps directly to the **Relational Division** operator ($\div$):

1. Project the pairs of sailor ID and boat ID from reservations:
   $$R_{\text{pairs}} = \pi_{\text{sid}, \text{bid}}(\text{Reservation})$$
2. Project all existing boat IDs:
   $$R_{\text{all\_boats}} = \pi_{\text{bid}}(\text{Boat})$$
3. Compute the quotient:
   $$R_{\text{result}} = R_{\text{pairs}} \div R_{\text{all\_boats}} = \pi_{\text{sid}, \text{bid}}(\text{Reservation}) \div \pi_{\text{bid}}(\text{Boat})$$

Equivalent formulation using fundamental operators:
$$
\pi_{\text{sid}}(\text{Sailor}) - \pi_{\text{sid}}\left( (\pi_{\text{sid}}(\text{Sailor}) \times \pi_{\text{bid}}(\text{Boat})) - \pi_{\text{sid}, \text{bid}}(\text{Reservation}) \right)
$$

---

## Problem 2: Mapping Weak Entities and 1:N Relationships

### Scenario
An organization has an entity $\text{Department}(\underline{\text{dept\_num}}, \text{dept\_name})$ and a weak entity $\text{Dependent}(\underline{\text{dep\_name}}, \text{birth\_date}, \text{relationship})$ identifying against $\text{Employee}(\underline{\text{emp\_id}}, \text{emp\_name})$.
A department has a $1:N$ relationship $\text{Works\_In}$ with employee (each employee works in exactly one department; a department has many employees).

### Solution
Applying Steps 1, 2, and 4 of the ER-to-Relational Mapping algorithm:

1. **Step 1 (Regular Entities):**
   $$\text{Department}(\underline{\text{dept\_num}}, \text{dept\_name})$$
2. **Step 4 ($1:N$ Relationship $\text{Works\_In}$):**
   The $N$-side is $\text{Employee}$. Place the primary key of $\text{Department}$ as foreign key in $\text{Employee}$:
   $$\text{Employee}(\underline{\text{emp\_id}}, \text{emp\_name}, \text{dept\_num} \uparrow \text{Department})$$
3. **Step 2 (Weak Entity $\text{Dependent}$):**
   Include identifying entity primary key (`emp_id`) plus partial key (`dep_name`):
   $$\text{Dependent}(\underline{\text{emp\_id} \uparrow \text{Employee}, \text{dep\_name}}, \text{birth\_date}, \text{relationship})$$
   Primary Key: $(\text{emp\_id}, \text{dep\_name})$. Foreign Key: $\text{emp\_id} \to \text{Employee}(\text{emp\_id})$.

