# Digital Electronics Study Companion Web Application

Interactive NiceGUI educational application for Course: Digital Electronics (Year 1, Semester 2).

## Features

- Verbatim Exam Transcripts: Includes the complete Practice Exam 01 and Synthetic Exam 02 covering the entire course syllabus.
- Interactive Canvas: Exam text annotated with classification badges and 3-part educational tooltips (Classification, Detection Clue, Application Rationale).
- Complete Solution Sheets: Sequentially stacked solutions with KaTeX mathematical derivations, given parameter cards, and full distractor explanations for multiple-choice questions. Zero hidden content or accordions.
- Dynamic State Transition Diagram: Interactive SVG visualization of FSM and Modulo-6 counter state graphs, with pan, zoom, reset, and details toggle.
- Computational Verification: Complete Python verification scripts with hardware and synthesis justifications.
- Methodology Reference: Quick-reference cards and comprehensive problem recognition table.
- Master Theory Guide: Full 12-module theoretical handbook covering Number Systems, Boolean Algebra, K-Maps, Adders/ALU, MSI MUX/Decoders, Flip-Flops, Registers/Counters, FSMs, VHDL synthesis, and FPGA static timing analysis.
- Dual Theme: Orange Light default theme with high-contrast Soft Dark theme toggle.
- Clean Print & PDF Export: Dedicated print stylesheets for exam revision printouts.

## Installation & Execution

### Prerequisites

- Python 3.10+
- NiceGUI >= 1.4.0
- markdown2 >= 2.4.0

### Run with Python

```bash
cd Year_1/Semester_2/DIGITAL_ELECTRONICS/Resources/app
pip install -r requirements.txt
python3 main.py
```

Open your browser at `http://localhost:8080`.

