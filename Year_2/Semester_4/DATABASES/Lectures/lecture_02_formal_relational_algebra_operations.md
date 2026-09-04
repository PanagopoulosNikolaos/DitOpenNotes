# Lecture 02: Formal Relational Algebra Operations

This lecture presents the formal procedural query language of the Relational Model: Relational Algebra. It covers the fundamental unary and binary operators, derived operators, and expression formulation for query processing.

---

## 1. Mathematical Foundations of the Relational Model

A relation $R$ of degree $n$ is defined over attributes $A_1, A_2, \dots, A_n$ with domains $\text{dom}(A_i)$:

$$
R \subseteq \text{dom}(A_1) \times \text{dom}(A_2) \times \dots \times \text{dom}(A_n)
$$

Relational algebra operators take one or two relations as input and produce a new relation as output (**property of closure**), enabling operator composition into complex algebraic expressions.

---

## 2. Fundamental Relational Algebra Operators

### 2.1 Selection ($\sigma$)
Selects a horizontal subset of tuples from relation $R$ that satisfy a specified boolean condition condition $p$:

$$
\sigma_p(R) = \{ t \in R \mid p(t) = \text{true} \}
$$

- Degree: Equal to degree of $R$.
- Cardinality: $0 \le |\sigma_p(R)| \le |R|$.
- Example: Retrieve all employees earning more than 50,000:
  $$\sigma_{\text{salary} > 50000}(\text{Employee})$$

### 2.2 Projection ($\pi$)
Selects a vertical subset of columns from relation $R$, discarding unmentioned attributes and eliminating duplicate rows:

$$
\pi_{A_1, A_2, \dots, A_k}(R) = \{ t[A_1, A_2, \dots, A_k] \mid t \in R \}
$$

- Degree: Exactly $k$.
- Cardinality: $1 \le |\pi_L(R)| \le |R|$ (due to mathematical set duplicate elimination).
- Example: Retrieve distinct department names:
  $$\pi_{\text{dept\_name}}(\text{Department})$$

### 2.3 Cartesian (Cross) Product ($\times$)
Combines all tuples from relation $R$ with all tuples from relation $S$:

$$
R \times S = \{ t \cdot s \mid t \in R \land s \in S \}
$$

- If $R$ has degree $n_1$ and cardinality $m_1$, and $S$ has degree $n_2$ and cardinality $m_2$:
  $$\text{Degree}(R \times S) = n_1 + n_2, \quad \text{Cardinality}(R \times S) = m_1 \cdot m_2$$

### 2.4 Set Theoretic Operators ($\cup$, $-$, $\cap$)
Two relations $R$ and $S$ must be **union-compatible** (have identical degree and matching attribute domains):
- **Union ($\cup$):** $R \cup S = \{ t \mid t \in R \lor t \in S \}$.
- **Set Difference ($-_-$):** $R - S = \{ t \mid t \in R \land t \notin S \}$.
- **Intersection ($\cap$):** Derived operator: $R \cap S = R - (R - S)$.

### 2.5 Rename ($\rho$)
Renames a relation or its attributes:
$$\rho_{S(B_1, B_2, \dots, B_n)}(R)$$

---

## 3. Derived Operators

### 3.1 Theta Join ($\bowtie_\theta$)
Combines Cartesian product with a selection predicate $\theta$:

$$
R \bowtie_\theta S = \sigma_\theta(R \times S)
$$

### 3.2 Equijoin and Natural Join ($\bowtie$)
- **Equijoin:** A theta join where the condition consists strictly of equality comparisons ($R.A = S.B$).
- **Natural Join ($R \bowtie S$):** Automatically equates attributes having identical names in both relations, projecting out redundant duplicate attribute columns.

### 3.3 Division ($\div$)
Useful for queries expressing "for all" or universal quantification (e.g., "Find students who have taken ALL courses offered by the CS department"):

$$
R(Z) \div S(Y) = \{ t \in \pi_{Z - Y}(R) \mid \forall s \in S, \ (t \cdot s) \in R \}
$$

Algebraic formulation using fundamental operators:

$$
R \div S = \pi_X(R) - \pi_X\left( (\pi_X(R) \times S) - R \right) \quad \text{where } X = Z - Y
$$

---

## 4. Query Formulation Examples

Given schemas:
- $\text{Student}(\underline{\text{sid}}, \text{name}, \text{gpa})$
- $\text{Enrollment}(\underline{\text{sid}, \text{cid}}, \text{grade})$
- $\text{Course}(\underline{\text{cid}}, \text{title}, \text{dept})$

### Query 1: Find names of students enrolled in 'Databases'
$$
\pi_{\text{name}}\left( \text{Student} \bowtie \text{Enrollment} \bowtie \sigma_{\text{title} = \text{'Databases'}}(\text{Course}) \right)
$$

### Query 2: Find students who have NOT enrolled in any course
$$
\pi_{\text{sid}, \text{name}}(\text{Student}) - \pi_{\text{sid}, \text{name}}(\text{Student} \bowtie \text{Enrollment})
$$

