# Laboratory Evaluation Rubric

All laboratory solutions submitted for **Principles of Programming Languages (Code: 401)** are evaluated based on a 100-point standardized rubric:

---

## Evaluation Criteria

| Category | Weight | Description |
|:---|:---:|:---|
| **Algorithmic Correctness** | 40% | Passes all unit test cases and edge cases (empty inputs, negative bounds, boundary conditions). Zero runtime exceptions. |
| **Code Documentation** | 20% | Adheres strictly to **Google Style Python Docstrings**. Every function must feature typed `Args:`, `Returns:`, and `Raises:` sections. |
| **Naming Conventions** | 15% | Strictly applies **PascalCase** for classes, **camelCase** for functions, and **snake_case** for variables and parameters. |
| **Logic Comments** | 15% | Includes single-line comments explaining the *why* and algorithmic rationale of non-obvious operations. Non-directive phrasing only. |
| **Efficiency & Complexity** | 10% | Avoids redundant allocations; respects targeted time and space complexity bounds ($O(N \log N)$ for sorting, $O(N)$ for linear sweeps). |

---

## Submission Checklist

- [✓] Code executes without syntax errors under Python 3.10+.
- [✓] All docstrings provide parameter type specifications in parentheses.
- [✓] No instructional language used in inline comments.
- [✓] Test runners in `Exercises/Lab/` pass with zero failures.

