# Relational Algebra, JOINs & Security Policies
*Relational Algebra, JOINs & Security Policies*

---

## Table of Contents
*Table of Contents*

1. [Introduction](#introduction)
2. [Cartesian Product](#cartesian-product)
3. [Natural Join](#natural-join)
4. [The Join Operation (JOIN)](#the-join-operation-join)
   - [Theta Join ($\theta$-Join)](#theta-join--join)
   - [Equality Join (Equi-Join)](#equality-join-equi-join)
   - [Inner Join](#inner-join)
   - [Outer Join](#outer-join)
5. [Nested Queries](#nested-queries)
6. [Security Threats & Cybersecurity](#security-threats--cybersecurity)
   - [Password Cracking](#password-cracking)
   - [Social Engineering](#social-engineering)
7. [Information Security Policies](#information-security-policies)
   - [Software Security](#software-security)
   - [Data Security](#data-security)
   - [Security Policy for Passwords](#security-policy-for-passwords)
8. [Summary Table of Key Concepts](#summary-table-of-key-concepts)
9. [Key Takeaways](#key-takeaways)
10. [Solved Exercises](#solved-exercises)
11. [Exam Tip: JOIN Mechanics & Safety Policies](#exam-tip-join-mechanics--safety-policies)

---

## Introduction

This document covers the advanced operations of **Relational Algebra**, focusing on the **Cartesian Product**, the **Natural Join**, and the various forms of **JOINs** in SQL. Furthermore, it examines the fundamental concepts of **Information Systems Security**, the methods of **Password Cracking**, the threat of **Social Engineering**, and the importance of **Security Policies** for safeguarding data. These concepts link the mathematical theory of databases with practical query design and security in real-world environments.

---

## Cartesian Product
*Cartesian Product*

The **Cartesian Product**, denoted by $R \times S$, is a binary operation of relational algebra that combines every tuple of a relation $R$ with every tuple of a relation $S$. The schema of the output relation includes all the attributes of both relations.

**Analogy**: It is similar to a restaurant menu that includes $3$ appetizers and $4$ main courses. The "everything-with-everything" combination produces $12$ possible meal choices, regardless of whether they match well in taste.

**Basic rules**:
- If relation $R$ has cardinality $|R| = m$ and relation $S$ has cardinality $|S| = n$, the result $R \times S$ will have $m \times n$ tuples.
- If an attribute-name conflict arises (e.g., the column `cust_name` in both tables), it is resolved by using the full relation name as a prefix: `Customer.cust_name` and `Deposit.cust_name`.

```text
Cartesian Product Schema:
Customer(cust_name, street, cust_city)   X   Deposit(br_name, acc_number, cust_name, balance)
  |
  v
Result(Customer.cust_name, street, cust_city, br_name, acc_number, Deposit.cust_name, balance)
```

| Characteristic | Cartesian Product |
|:---|:---|
| **Symbol** | $\times$ |
| **SQL Implementation** | `CROSS JOIN` or `FROM Table1, Table2` |
| **Cardinality** | $|R| \times \|S\|$ |
| **Duplicate Columns** | Both are retained with a table prefix |

---

## Natural Join
*Natural Join*

The **Natural Join**, denoted by $R \bowtie S$, joins two relations by automatically using equality on all common attributes (columns with the same name). In the result, the common column appears only once, avoiding duplication.

**Analogy**: It is like matching puzzle pieces. If we have a card with book details and a card with author details, we connect them only if the author's name matches exactly, discarding the unrelated cards.

**Mathematical Definition**:
$$
R \bowtie S = \sigma_{R.A_1 = S.A_1 \land \dots \land R.A_k = S.A_k}(R \times S)
$$
where $A_1, \dots, A_k$ are the common attributes of relations $R$ and $S$.

```text
Natural Join Schema:
R(A, B)   bowtie   S(B, C)
  |
  v
Result(A, B, C)  <-- The common attribute B appears only once
```

```sql
-- Natural Join in SQL
SELECT * 
FROM Customer 
NATURAL JOIN Deposit;
```

---

## The Join Operation (JOIN)
*The Join Operation*

The **Join** is the most frequently used table-combining operation. It allows specifying explicit join conditions, which may be based on equality or other comparison operators.

---

### Theta Join ($\theta$-Join)
*Theta Join*

The **Theta Join**, denoted by $R \bowtie_{\theta} S$, is the most general form of join. It combines tuples from $R$ and $S$ for which a general condition $\theta$ holds. This condition can involve operators such as $=, >, <, \neq, \geq, \leq$.

**Mathematical Definition**:
$$
R \bowtie_{\theta} S = \sigma_{\theta}(R \times S)
$$

---

### Equality Join (Equi-Join)
*Equi-Join*

The **Equi-Join** is a special case of the Theta Join where the condition $\theta$ involves exclusively equality operators ($=$). Unlike the natural join, the equi-join retains both join columns in the final result.

```sql
-- Equi-Join in SQL
SELECT * 
FROM Customer 
JOIN Deposit ON Customer.cust_name = Deposit.cust_name;
```

---

### Inner Join
*Inner Join*

The term `JOIN` in SQL is shorthand for the **Inner Join**. It returns only the records that have a matching value in both tables based on the `ON` condition.

**Analogy**: Given a list of students and a list of lab registrations, an Inner Join will return only the students who are registered in at least one lab.

```sql
-- Inner Join in SQL with ON
SELECT Customer.cust_name, Borrow.amount
FROM Customer
INNER JOIN Borrow ON Customer.cust_name = Borrow.cust_name;
```

---

### Outer Join
*Outer Join*

The **Outer Join** allows keeping the tuples that have no match in the joined relation, filling the empty fields with the value `NULL`.

#### Left Outer Join ($\⟕$)
It retains all the tuples of the left relation. If there is no match on the right, the right-side columns are filled with `NULL`.

```sql
SELECT * 
FROM Customer 
LEFT OUTER JOIN Deposit ON Customer.cust_name = Deposit.cust_name;
```

#### Right Outer Join ($\⟖$)
It retains all the tuples of the right relation. If there is no match on the left, the left-side columns are filled with `NULL`.

```sql
SELECT Borrow.loan_number, Borrow.amount, Customer.cust_name 
FROM Borrow 
RIGHT OUTER JOIN Customer ON Borrow.cust_name = Customer.cust_name;
```

---

### Comparative Table of JOIN Types

| JOIN Type | Join Condition | Common Column Retention | Unmatched Rows |
|:---|:---|:---|:---|
| **Theta Join ($\bowtie_{\theta}$)** | Any ($=, >, <, \dots$) | Yes (Duplicate columns) | No |
| **Equi-Join** | Only equality ($=$) | Yes (Duplicate columns) | No |
| **Natural Join ($\bowtie$)** | Automatic equality of common columns | No (Column merging) | No |
| **Left Outer Join ($\⟕$)** | Any equality condition | Yes (Duplicate columns) | Yes (From the left table) |
| **Right Outer Join ($\⟖$)** | Any equality condition | Yes (Duplicate columns) | Yes (From the right table) |

---

## Nested Queries
*Nested Queries*

Often, using a table join is not necessary, as the information can be retrieved with **Nested Queries (Subqueries)**. A subquery executes internally and returns a list of values used by the outer query (usually with the `IN` operator).

**Analogy**: It is like searching for books by specific authors. First, we run the inner search to find the IDs of authors born in Athens, and then we use that list to retrieve their books.

```sql
-- Nested query in SQL
SELECT acc_no 
FROM Deposit
WHERE br_name IN (
    SELECT br_name 
    FROM branch 
    WHERE Br_city = 'Athens'
);
```

---

## Security Threats & Cybersecurity
*Security Threats & Cybersecurity*

A **Threat** is defined as any event or action that can lead to loss, data destruction, or physical damage to the infrastructure of an Information System (IS).

**Categories of Threats**:
1. **Natural Disasters**: Fires, floods, earthquakes.
2. **Accidental Threats**: Human errors, hardware failure.
3. **Deliberate (Non-Physical) Threats**: Malicious software (Malware), DoS attacks, Phishing, etc.

---

### Password Cracking
*Password Cracking*

**Password Cracking** is the process of gaining unauthorized access by finding or decrypting passwords.

**Cracking techniques**:
- **Dictionary Attack**: Use of a predefined list of common words to compare against the hashes of the passwords.
- **Brute Force Attack**: Trying all possible combinations of characters and symbols using algorithms.
- **Rainbow Table Attack**: Use of pre-computed mapping tables (pre-computed hashes) to find the original value of a hash (e.g., MD5).
- **Guess**: Trying obvious passwords (e.g., `admin`, `123456`, `password`).
- **Spidering**: Collecting information from the company's websites and social networks to build targeted word lists.

| Technique | Mechanism | Advantage | Disadvantage |
|:---|:---|:---|:---|
| **Dictionary** | Testing ready-made words | Fast execution | Fails on random passwords |
| **Brute Force** | Testing all combinations | Guaranteed result | Requires enormous time |
| **Rainbow Table** | Search in pre-computed hashes | Almost instantaneous discovery | Requires enormous storage space |

---

### Social Engineering
*Social Engineering*

**Social Engineering** is the art of manipulating and deceiving the users of a system in order to extract confidential information (e.g., passwords).

**Analogy**: It is like a con artist pretending to be a technician from the water company to get into your house, instead of trying to break the door lock.

**The Social Engineering Cycle**:
```text
  +--------------------------------+
  |  1. Information Gathering      | (Gather Info)
  +--------------------------------+
                  |
                  v
  +--------------------------------+
  |    2. Plan Attack              | (Plan Attack)
  +--------------------------------+
                  |
                  v
  +--------------------------------+
  |    3. Acquire Tools            | (Acquire Tools)
  +--------------------------------+
                  |
                  v
  +--------------------------------+
  |          4. Attack             | (Attack)
  +--------------------------------+
                  |
                  v
  +--------------------------------+
  |  5. Use Acquired Knowledge     | (Use Knowledge)
  +--------------------------------+
```

**Common techniques**:
- **Phishing**: Sending fake emails that mimic trusted organizations to steal credentials.
- **Tailgating**: Physical entry into a secured area by closely following an authorized employee.
- **Familiarity Exploit**: Developing friendly relations with the victim before the attack.
- **Intimidating Circumstances**: Using threats or intimidation to coerce the user into providing information.
- **Exploiting Human Curiosity/Greed**: Luring users with promises of money or deliberately leaving infected USB flash drives in common areas.

---

## Information Security Policies
*Information Security Policies*

A **Security Policy** is a formal document that includes rules, guidelines, procedures, and roles for protecting an organization's Information Systems.

---

### Software Security
- Prohibition of installing software without a license or the security officer's approval.
- Software modifications must first be performed in a staging environment and then in production.
- Mandatory installation of anti-malware software on servers and workstations.
- Immediate isolation and cleaning of workstations in case of infection.

---

### Data Security
- Prohibition of sending unencrypted data over the internet.
- Maintaining regular backups and storing them in a safe, physically protected location.
- Protecting the physical storage media that contain confidential data.

---

### Security Policy for Passwords
- **Characteristics of a strong password**:
  - Length of at least $15$ characters.
  - Use of uppercase, lowercase, numbers, and symbols.
  - Must not be a dictionary word in any language and must not be based on personal information.
  - Must not be stored online or in plain-text files.
- **Management rules**:
  - Change of user passwords at least every $6$ months.
  - Prohibition of sharing passwords for accounts with high privileges.
  - Prohibition of disclosing a password by phone, email, to supervisors, colleagues, or security forms.

---

## Summary Table of Key Concepts
*Summary Table of Key Concepts*

| Concept | Definition | Critical Rule / Characteristic |
|:---|:---|:---|
| **Cartesian Product ($R \times S$)** | Combination of all tuples of $R$ with those of $S$ | Produces $\|R\| \times \|S\|$ records |
| **Natural Join ($R \bowtie S$)** | Join based on equality of common attributes | Merges the common columns into one |
| **Theta Join ($R \bowtie_{\theta} S$)** | Join based on a general condition $\theta$ | Implemented as $\sigma_{\theta}(R \times S)$ |
| **Left Outer Join ($\⟕$)** | Join that retains all left-side elements | Fills unmatched right-side entries with `NULL` |
| **Right Outer Join ($\⟖$)** | Join that retains all right-side elements | Fills unmatched left-side entries with `NULL` |
| **Threat** | Event that causes loss/damage to the IS | Can be natural, accidental, or deliberate |
| **Dictionary Attack** | Cracking attack with predefined words | Based on ready-made password dictionaries |
| **Social Engineering** | Manipulation of users to extract passwords | Exploits human trust/ignorance |
| **Security Policy** | Set of rules for protecting the IS | Constitutes a legal and operational obligation |

---

## Key Takeaways
*Key Takeaways*

- The **Cartesian Product** combines all elements of two tables, producing a large relation with duplicate columns.
- The **Natural Join** automatically performs an equality check on the common fields and retains the common column only once.
- **Outer Joins** prevent information loss for records without a match by introducing `NULL` values.
- **Nested Queries** offer an alternative method of data retrieval without using explicit joins.
- **Information Security** is threatened both by technical methods (Password Cracking) and by human weaknesses (Social Engineering).
- **Security Policies** must be strictly enforced at the software, data, and password-management levels (minimum 15 characters, change every 6 months).

---

## Solved Exercises

### Exercise 1: Cartesian Product Calculation
**Problem:**
The relations $R$ (Customers) and $S$ (Deposits) are given:
$$
R = \{ (\text{'Petrou'}, \text{'Athens'}), (\text{'Pavlou'}, \text{'Larisa'}) \}
$$
$$
S = \{ (1100, \text{'Petrou'}), (756, \text{'Pavlou'}) \}
$$
Compute the Cartesian Product $R \times S$ and draw the output table.

**Solution:**
1. We determine the schemas of the relations:
   - $R(\text{cust\_name}, \text{cust\_city})$
   - $S(\text{acc\_no}, \text{cust\_name})$
2. The schema of the result will be:
   - $Result(R.\text{cust\_name}, \text{cust\_city}, \text{acc\_no}, S.\text{cust\_name})$
3. We combine each row of $R$ with each row of $S$ (in total $2 \times 2 = 4$ rows):
   - Row 1: $(\text{'Petrou'}, \text{'Athens'})$ with $(1100, \text{'Petrou'})$
   - Row 2: $(\text{'Petrou'}, \text{'Athens'})$ with $(756, \text{'Pavlou'})$
   - Row 3: $(\text{'Pavlou'}, \text{'Larisa'})$ with $(1100, \text{'Petrou'})$
   - Row 4: $(\text{'Pavlou'}, \text{'Larisa'})$ with $(756, \text{'Pavlou'})$

*Result table:*
| R.cust_name | cust_city | acc_no | S.cust_name |
|:---|:---|:---|:---|
| Petrou | Athens | 1100 | Petrou |
| Petrou | Athens | 756 | Pavlou |
| Pavlou | Larisa | 1100 | Petrou |
| Pavlou | Larisa | 756 | Pavlou |

---

### Exercise 2: Natural Join Application
**Problem:**
Using the relations $R$ and $S$ from Exercise 1, compute the Natural Join $R \bowtie S$.

**Solution:**
1. We identify the common attribute of the two tables, which is `cust_name`.
2. From the Cartesian Product of Exercise 1, we keep only the rows where $R.\text{cust\_name} = S.\text{cust\_name}$:
   - Line 1: $\text{'Petrou'} = \text{'Petrou'}$ (Accepted)
   - Line 2: $\text{'Petrou'} \neq \text{'Pavlou'}$ (Rejected)
   - Line 3: $\text{'Pavlou'} \neq \text{'Petrou'}$ (Rejected)
   - Line 4: $\text{'Pavlou'} = \text{'Pavlou'}$ (Accepted)
3. We merge the common column `cust_name` into one.

*Result table:*
| cust_name | cust_city | acc_no |
|:---|:---|:---|
| Petrou | Athens | 1100 |
| Pavlou | Larisa | 756 |

---

### Exercise 3: Equi-Join SQL Translation
**Problem:**
Write the SQL query that performs the equi-join of the tables `Customer(cust_name, cust_city)` and `Deposit(acc_no, cust_name)` on the column `cust_name`, and show the structure of the result.

**Solution:**
1. The SQL query uses the `JOIN ... ON ...` syntax:
```sql
SELECT * 
FROM Customer 
JOIN Deposit ON Customer.cust_name = Deposit.cust_name;
```
2. The output retains both `cust_name` columns of the tables.

*Result table:*
| Customer.cust_name | cust_city | acc_no | Deposit.cust_name |
|:---|:---|:---|:---|
| Petrou | Athens | 1100 | Petrou |
| Pavlou | Larisa | 756 | Pavlou |

---

### Exercise 4: Left Outer Join Computation
**Problem:**
The following tables are given:
- `Customer(cust_name, cust_city)` with records: `('Petrou', 'Athens')`, `('Pavlou', 'Larisa')`, `('Antonis', 'Thessaloniki')`
- `Deposit(acc_no, cust_name)` with records: `(1100, 'Petrou')`, `(756, 'Pavlou')`

Compute the Left Outer Join of the tables `Customer` and `Deposit` on the column `cust_name`.

**Solution:**
1. The Left Outer Join retains all the records of the left table (`Customer`).
2. For the records `Petrou` and `Pavlou` there is a match in the `Deposit` table, so they are filled in normally.
3. For the record `Antonis` there is no corresponding record in `Deposit`. Consequently, the `Deposit` fields (`acc_no`, `Deposit.cust_name`) take the value `NULL`.

*Result table:*
| Customer.cust_name | cust_city | acc_no | Deposit.cust_name |
|:---|:---|:---|:---|
| Petrou | Athens | 1100 | Petrou |
| Pavlou | Larisa | 756 | Pavlou |
| Antonis | Thessaloniki | NULL | NULL |

---

### Exercise 5: Multiple Table Join Query
**Problem:**
The following tables are given:
- `Customer(cust_name, cust_city)`
- `Deposit(acc_no, br_name, cust_name, balance)`
- `Branch(br_name, br_city)`

Write an SQL query to find the names of customers and their balances who have a deposit in a branch located in a **different** city from their city of residence.

**Solution:**
1. We must join the `Customer` table with `Deposit` (via `cust_name`) and the `Deposit` table with `Branch` (via `br_name`).
2. We add the filtering condition `Customer.cust_city <> Branch.br_city`.

```sql
SELECT Customer.cust_name, Deposit.balance
FROM Customer
JOIN Deposit ON Customer.cust_name = Deposit.cust_name
JOIN Branch ON Deposit.br_name = Branch.br_name
WHERE Customer.cust_city <> Branch.br_city;
```

---

### Exercise 6: Right Outer Join Analysis
**Problem:**
The tables `Borrow(loan_number, amount, cust_name)` with record `(L-101, 1000, 'Giorgos')` and `Customer(cust_name, street, cust_city)` with records `('Giorgos', 'Patision 10', 'Athens')`, `('Maria', 'Trikoupi 12', 'Patra')` are given.

Compute the result of the Right Outer Join of `Borrow` with `Customer` on the column `cust_name`.

**Solution:**
1. The Right Outer Join retains all the records of the right table (`Customer`).
2. For `Giorgos` there is a match, so it is linked to the loan `L-101`.
3. For `Maria` there is no loan in the `Borrow` table. The `loan_number` and `amount` fields are filled with `NULL`.

*Result table:*
| loan_number | amount | cust_name | street | cust_city |
|:---|:---|:---|:---|:---|
| L-101 | 1000 | Giorgos | Patision 10 | Athens |
| NULL | NULL | Maria | Trikoupi 12 | Patra |

---

### Exercise 7: Nested Subquery Translation
**Problem:**
Convert the following join (JOIN) query into an equivalent query using a nested subquery:
```sql
SELECT DISTINCT Deposit.cust_name
FROM Deposit
JOIN Branch ON Deposit.br_name = Branch.br_name
WHERE Branch.br_city = 'Athens';
```

**Solution:**
1. The inner query (subquery) must retrieve the names of the branches (`br_name`) located in the city 'Athens'.
2. The outer query will select the names of customers from the `Deposit` table whose branch is included in the subquery's list.

```sql
SELECT DISTINCT cust_name
FROM Deposit
WHERE br_name IN (
    SELECT br_name
    FROM Branch
    WHERE br_city = 'Athens'
);
```

---

### Exercise 8: Natural Join vs. Theta Join Equivalence
**Problem:**
Prove mathematically using relational algebra that the Natural Join $R \bowtie S$ for the relations $R(A, B)$ and $S(B, C)$ is equivalent to a projection operation over a Theta Join.

**Solution:**
1. The Theta Join with an equality condition on the common attribute $B$ is defined as:
   $$ R \bowtie_{R.B = S.B} S = \sigma_{R.B = S.B}(R \times S) $$
   This relation has the attributes $(A, R.B, S.B, C)$.
2. The Natural Join $R \bowtie S$ has the attributes $(A, B, C)$, where the duplicate $B$ column has been merged.
3. To make the two expressions identical, we apply projection ($\pi$) to the result of the Theta Join to discard one of the two $B$ columns (e.g., $S.B$) and rename the other to $B$:
   $$ R \bowtie S = \pi_{A, R.B \text{ AS } B, C}(\sigma_{R.B = S.B}(R \times S)) $$
   Therefore, the Natural Join is a specialized form of Theta Join followed by a projection.

---

## Exam Tip: JOIN Mechanics & Safety Policies

> **[Key Insight]**
> **Exam Tip - JOINs**: In exams, when the difference between `NATURAL JOIN` and `JOIN ... ON` (Equi-join) is asked:
> 1. `NATURAL JOIN` automatically merges columns with the same name and returns the common column **only once**.
> 2. `JOIN ... ON` retains **both columns** in the result, adding the table name as a prefix. If the conversion of a natural join into a general join is requested, an explicit projection (`SELECT`) of the individual columns must be used to avoid duplication.
> 
> **Exam Tip - Security Policies**: In theory questions about password security, remember the following "golden rules":
> - Minimum password length: **15 characters** (not 8 or 10).
> - Change frequency: **Every 6 months** (at least).
> - **Entity Integrity** concerns exclusively the Primary Key (not NULL), while **Referential Integrity** concerns the Foreign Key (it must point to an existing record). Do not confuse them!
