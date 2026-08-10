Department of Informatics and Telecommunications
University of Ioannina
Spyridon Tzimas
Spring Semester 2025

# 203: Discrete Mathematics
## Mock Exam 5 (Gotchas)

Your seat in this exam is uniquely identified by a label of the form $X - I J$ where $X$ is the name of the room and $I$ and $J$ are the row and column respectively to which the particular seat belongs. Your group is:

| $I \setminus J$ | even | odd |
| :--- | :--- | :--- |
| even | Group A | Group B |
| odd | Group C | Group D |

The grading value of the exam is 10 points. The duration of the exam is three hours. Only blue and black pens are allowed. Pencil is allowed only for writing on scrap paper.

Good Luck!

---

**Topic 1. (3 points)** Determine whether the following statements are True or False and justify your answer.
a. (1.5 points) If $A \subseteq B \cup C$, then necessarily $(A \subseteq B)$ or $(A \subseteq C)$.
b. (1.5 points) The empty set $\emptyset$ is an element of the power set $P((?))$.

- **Group A:** (?) = $\emptyset$
- **Group B:** (?) = $\{\emptyset\}$
- **Group C:** (?) = $\{1, 2\}$
- **Group D:** (?) = $\{\{\emptyset\}\}$

(Trap: Correctly distinguish "belongs" ($\in$) from "subset" ($\subseteq$)).

---

**Topic 2. (4 points)** Consider the Non-deterministic Finite Automaton (NFA) $N$ that recognizes the language $L = (0 \cup 1)^*(?)(0 \cup 1)^*$. Convert it to an equivalent DFA using the subset construction algorithm.

- **Group A:** (?) = $00$
- **Group B:** (?) = $11$
- **Group C:** (?) = $01$
- **Group D:** (?) = $10$

How many states does the resulting minimal DFA have? (Trap: Are there any unreachable or equivalent states?)

---

**Topic 3. (3 points)** We have a function $f: A \to B$ and a $g: B \to C$. If the composition $g \circ f$ is (?), what can we conclude with certainty about $f$ and $g$?

- **Group A:** (?) = injective (1-1)
- **Group B:** (?) = surjective (onto)
- **Group C:** (?) = injective AND $f$ is surjective
- **Group D:** (?) = surjective AND $g$ is injective

Give a counterexample for the property that is NOT necessarily inherited. (Trap: Which function is forced to have the property and which is not?)