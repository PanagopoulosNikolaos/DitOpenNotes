# Discrete Mathematics Study Instrument & Exam Solution Suite

Educational NiceGUI web application for University of Ioannina (DIT) Course 203: Discrete Mathematics (Instructor: Tzimas). Implemented under Archetype B (Multi-Part Exam / Problem Set Study Sheet) from `scripts/make_app.md`.

---

## Key Features

1. **Exact 1-to-1 Transcription**:
   - Original exam papers and practice sets transcribed verbatim in their exact original sequence.
   - Preserves all multi-group variations (Group A, Group B, Group C, Group D) solved systematically step-by-step.

2. **Open Master Solution Sheets (Zero Collapsibles)**:
   - Full mathematical derivations, formulas, substitutions, results, and rationales rendered openly without accordions or hidden dialogs.
   - KaTeX typesetting for all mathematical expressions and truth tables.

3. **Master Theory Guide (100% Exam Scope)**:
   - Comprehensive scholarly coverage of all 8 core syllabus topics: Mathematical Induction, Propositional Logic & Boolean Algebra, Set Theory & PIE, Balls-in-Boxes Combinatorics, Probability & Bayes' Theorem, Relations & Closures, Graph Theory & Planarity (Euler's formula, Kuratowski's theorem), and Automata & Regular Expressions.
   - Section dedicated to Tzimas exam gotchas, seat parity routing matrix, and grading requirements.

4. **Verbatim Text Canvas with 3-Part Tooltips**:
   - Classification, Detection Clue, and Application Rationale on every semantic trigger.
   - Category filter chips (All, Logic, Sets, Prob, Graph, Automata, Clear) with visual color badges.

5. **Dual Themes & Scholarly Typography**:
   - Warm Orange Light default theme with high contrast and subtle borders.
   - Soft Dark theme with slate surfaces.
   - Typography powered by Outfit and JetBrains Mono.

6. **Interactive SVG Diagrams & Python Verification Scripts**:
   - Graph and automata visualizations with pan and zoom controls.
   - Embedded verification scripts asserting mathematical correctness.

---

## Directory Structure

```
Year_1/Semester_2/DISCRETE_MATHEMATICS/Resources/app/
├── config.py              # Design tokens, CSS styles, KaTeX script headers, regex math guard
├── main.py                # Application entrypoint controller and reactive view router
├── requirements.txt       # Python dependencies (nicegui, markdown2)
├── README.md              # Application documentation
├── models/
│   ├── __init__.py        # Package exports
│   ├── scenario.py        # Dataclasses (Scenario, ExamQuestion, CalculationStep, etc.)
│   └── registry.py        # ScenarioRegistry singleton and UI selector options
├── components/
│   ├── __init__.py        # Component exports
│   ├── header.py          # Sticky header with scenario switcher, theme toggle, and print menu
│   ├── methodology_card.py # 4 sequential problem-solving guidance cards
│   ├── interactive_canvas.py # Verbatim exam canvas with filter chips and 3-part tooltips
│   ├── analysis_section.py # Open stacked question solution cards with KaTeX
│   ├── methodology_table.py# Textual trigger recognition and trap prevention table
│   ├── visual_diagram.py  # Interactive SVG graph and automata canvas
│   ├── solution_code.py   # Rationale cards and Python verification script
│   └── theory_page.py     # Master 8-module theoretical guide for 100/100 score
└── scenarios/
    ├── __init__.py        # Auto-registration of all 11 scenarios
    ├── final_exam_2025_june.py      # June 2025 Final (Questions 1-9 across Groups A, B, C, D)
    ├── midterm_exam_2025_group_a.py # Midterm 2025 Group A (Questions 1-4 verbatim)
    ├── midterm_exam_2025_group_b.py # Midterm 2025 Group B (Questions 1-4 verbatim)
    ├── mock_exam_1_easier.py        # Mock Exam 1 (Sets, Truth Tables, Degrees)
    ├── mock_exam_2_standard.py      # Mock Exam 2 (Equivalence Closures, DFA, Probability)
    ├── mock_exam_3_standard.py      # Mock Exam 3 (NAND/XOR Gates, Sets, Induction)
    ├── mock_exam_4_harder.py        # Mock Exam 4 (Planar Bounds, Restricted RegEx, PIE)
    ├── mock_exam_5_gotchas.py       # Mock Exam 5 (Subsets vs Power Sets, NFA, g o f)
    ├── practice_exam_easy.py        # Practice Exam Easy (Questions 1-9)
    ├── practice_exam_medium.py      # Practice Exam Medium (Questions 1-9)
    └── practice_exam_hard.py        # Practice Exam Hard (Questions 1-9)
```

---

## Installation & Running

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python3 main.py
   ```

3. Open your browser at:
   ```
   http://localhost:8080
   ```
