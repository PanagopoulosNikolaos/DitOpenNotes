# Assignment Notebook Guide: Interactive Python Exercises

This guide explains how to complete, verify, and document Python assignments using Jupyter Notebooks in **Principles of Programming Languages (Code: 401)**.

---

## 1. Setup & Execution

1. **Environment Initialization**:
   Ensure a modern Python 3.10+ virtual environment is active:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install jupyter
   ```

2. **Opening the Notebook**:
   ```bash
   jupyter notebook
   ```
   Navigate to `Exercises/Python/Notebooks/General_Exercises/General_Exercises.ipynb` or `Exam_Style/Exam_Style.ipynb`.

---

## 2. Best Practices for Coding in Cells

- **Pure Functions**: Write self-contained functions where possible. Avoid mutating global variables between cells.
- **Documentation**: Write full Google Style docstrings for every function implemented in code cells.
- **Edge Case Tests**: Include test invocations in cells covering zero, empty list, negative numbers, and boundary values.
- **Output Cleanliness**: Clear cell outputs (`Cell -> All Output -> Clear`) prior to final submission.

