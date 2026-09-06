# Electromagnetics Study Companion Web Application

Interactive NiceGUI educational application for Course 201: Principles of Electromagnetics & Telecommunications (Year 1, Semester 2).

## Features

- Verbatim Exam Transcripts: Includes all official past exam papers (September 2024 Team B, June 2026 Teams A, B, C, D) and practice exams (01, 02, 03).
- Interactive Canvas: Exam text annotated with classification badges and 3-part educational tooltips (Classification, Detection Clue, Application Rationale).
- Complete Solution Sheets: Sequentially stacked solutions with KaTeX mathematical derivations, given parameter cards, and full distractor explanations for multiple-choice questions.
- Dynamic 3D Plane Wave Diagram: Interactive SVG visualization showing orthogonal electric (E) and magnetic (H) field vectors with wave propagation vector (k), with pan, zoom, reset, and field layer toggle.
- Computational Verification: Complete SymPy/Python verification scripts with physical justifications.
- Methodology Reference: Quick-reference cards and comprehensive problem recognition table.
- Master Theory Guide: Full theoretical overview covering Vector Calculus, Maxwell's Equations, Plane Waves, Poynting Vector, Transmission Lines, and fundamental physical constants.
- Dual Theme: Orange Light default theme with high-contrast Soft Dark theme toggle.
- Clean Print & PDF Export: Dedicated print stylesheets for exam revision printouts.

## Installation & Execution

### Prerequisites

- Python 3.10+ (tested with Python 3.14)
- NiceGUI >= 3.12.0

### Run with Conda

```bash
conda run -n py14 python main.py
```

### Run with Python Virtual Environment

```bash
pip install -r requirements.txt
python main.py
```

Open your browser at `http://localhost:8080`.

