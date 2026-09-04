# Lecture 04: Normalization Theory and Transaction Management

This lecture explores database normalization theory based on functional dependencies, defines the normal forms (1NF, 2NF, 3NF, BCNF), and examines transaction management principles (ACID properties, serializability, and concurrency control).

---

## 1. Functional Dependencies (FDs)

A functional dependency is a formal integrity constraint between two sets of attributes $X$ and $Y$ in relation schema $R$:

$$
X \to Y
$$

Constraint meaning: For any valid relation state $r(R)$, if two tuples $t_1, t_2 \in r$ agree on attribute set $X$, they must also agree on attribute set $Y$:

$$
t_1[X] = t_2[X] \implies t_1[Y] = t_2[Y]
$$

### 1.1 Armstrong's Axioms (Sound and Complete)
- **Reflexivity:** If $Y \subseteq X$, then $X \to Y$.
- **Augmentation:** If $X \to Y$, then $XZ \to YZ$.
- **Transitivity:** If $X \to Y$ and $Y \to Z$, then $X \to Z$.

**Derived Secondary Rules:**
- **Union:** If $X \to Y$ and $X \to Z$, then $X \to YZ$.
- **Decomposition:** If $X \to YZ$, then $X \to Y$ and $X \to Z$.
- **Pseudotransitivity:** If $X \to Y$ and $WY \to Z$, then $WX \to Z$.

### 1.2 Attribute Closure Algorithm ($X^+$)
To compute the set of all attributes functionally determined by $X$ under a set of FDs $F$:
1. Initialize $X^{(0)} = X$.
2. Repeatedly find any FD $Y \to Z \in F$ such that $Y \subseteq X^{(i)}$, and update:
   $$X^{(i+1)} = X^{(i)} \cup Z$$
3. Stop when $X^{(i+1)} = X^{(i)}$. Output $X^+ = X^{(i)}$.

**Candidate Key Test:** An attribute set $K$ is a candidate key of $R$ if and only if:
1. $K^+ = R$ (sufficiency / determination).
2. For all proper subsets $K' \subset K$, $(K')^+ \neq R$ (minimality).

---

## 2. Relational Database Normal Forms

Normalization systematically decomposes relations to eliminate update, insertion, and deletion anomalies.

| Normal Form | Formal Invariant Condition | Common Violation Anomaly |
|---|---|---|
| **1NF (First Normal Form)** | All attribute values must be atomic and scalar; no repeating groups or nested relations. | Multivalued phone numbers or composite addresses stored in a single table cell. |
| **2NF (Second Normal Form)** | In 1NF and every **non-prime attribute** is **fully functionally dependent** on every candidate key (no partial dependencies on a proper subset of a composite candidate key). | In $\text{Grade}(\underline{\text{sid}, \text{cid}}, \text{student\_name})$, $\text{sid} \to \text{student\_name}$ violates 2NF because `student_name` depends on part of the key. |
| **3NF (Third Normal Form)** | In 2NF and for every non-trivial FD $X \to A$, either $X$ is a superkey, or $A$ is a **prime attribute** (member of some candidate key). Disallows **transitive dependencies**. | In $\text{Emp}(\underline{\text{eid}}, \text{dept\_id}, \text{dept\_name})$, $\text{eid} \to \text{dept\_id} \to \text{dept\_name}$ violates 3NF because `dept_name` transitively depends on `eid`. |
| **BCNF (Boyce-Codd)** | For every non-trivial FD $X \to A$, $X$ must be a **superkey**. Stricter than 3NF (eliminates all functional redundancies). | In $\text{Schedule}(\underline{\text{student}, \text{course}}, \text{instructor})$ with $\text{instructor} \to \text{course}$, $\text{instructor}$ is not a superkey. |

---

## 3. Transaction Management and ACID Properties

A transaction is a logical unit of database processing that includes one or more database access operations.

```
       [ Read / Write Operations ]
                   |
           +---------------+
           |  ACID Engine  |
           +---------------+
          /        |        \
[ Atomicity ] [ Consistency ] [ Isolation ] [ Durability ]
```

- **Atomicity:** All-or-nothing execution. Enforced via DBMS write-ahead logging (WAL) and rollback mechanisms.
- **Consistency:** Execution preserves all database constraints (invariants, foreign keys, checks).
- **Isolation:** Each transaction executes unaware of concurrent transactions. Enforced via concurrency control (locking or timestamping).
- **Durability:** Once committed, changes survive system crashes. Enforced via non-volatile transaction logs.

### 3.1 Concurrency Control: Two-Phase Locking (2PL)
- **Growing Phase:** Transaction acquires locks; cannot release any lock.
- **Shrinking Phase:** Transaction releases locks; cannot acquire new locks.
- **Theorem:** Strict Two-Phase Locking guarantees **Conflict Serializability** and prevents cascading aborts.

