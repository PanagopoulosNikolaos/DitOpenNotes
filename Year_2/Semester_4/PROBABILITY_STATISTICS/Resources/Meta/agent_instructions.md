# Agent Instructions: Study Notes & Phase Material Generation

This document defines the architectural guidelines, file path structures, formatting requirements, and quality criteria for creating or maintaining study notes and phase reference materials within the Probability & Statistics repository.

---

## 1. Output Directory Structure

All generated or consolidated study materials must strictly adhere to the following directory layout under `Resources/`:

```
Resources/
├── Probability_and_Statistics_Master.md    # Generated master document compiling all 8 phase files
├── Phases/                                 # 8 consolidated phase files
│   ├── Phase_1_Descriptive_Statistics.md
│   ├── Phase_2_Probability_Theory.md
│   ├── Phase_3_Conditional_Probability_Independence.md
│   ├── Phase_4_Discrete_Random_Variables.md
│   ├── Phase_5_Continuous_Random_Variables_Distributions.md
│   ├── Phase_5B_Multivariate_Random_Variables.md
│   ├── Phase_6_Inferential_Statistics.md
│   └── Phase_7_R_Programming_Commands.md
├── Archive/Phase_Notes/                    # Historical granular source files backup (68 files)
├── Scripts/                                # Build and verification scripts (e.g., build_master.py)
└── Meta/                                   # Metadata, mindmaps, and agent instruction prompts
```

### Key Path Rules:
- **Consolidated Phase Files:** Saved in `Resources/Phases/` using `Phase_<N>_<Phase_Name>.md`.
- **Master Compilation File:** Saved at `Resources/Probability_and_Statistics_Master.md`. It is built by running `python Resources/Scripts/build_master.py`.
- **Source Archive:** Original granular notes are maintained read-only in `Resources/Archive/Phase_Notes/`.

---

## 2. Document Structure Specification

Every phase file inside `Resources/Phases/` must follow this standard markdown structure:

```markdown
# Phase N: [Phase Name]

## Table of Contents
- [Section N.1: Topic Title](#section-n1-topic-title)
- [Section N.2: Topic Title](#section-n2-topic-title)
- ...
- [Exam Preparation Guide](#exam-preparation-guide)
- [Phase Summary](#phase-summary)

---

## Section N.1: [Topic Title]

### Core Theory & Definitions
[Theoretical foundation, mathematical definitions, concepts, and conceptual intuition.]

### Mathematical Formulas & Derivations
[All relevant mathematical formulas with consistent notation.]

> **Practical / Time-Domain Note:**
> [Real-world domain applications, system latency considerations, unit conversions, or practical gotchas.]

### Worked Exercises

#### Exercise 1: [Descriptive Title]
**Problem:** [Clear, complete problem statement]

**Solution:**
1. **Step 1:** [Initial setup and parameter mapping]
2. **Step 2:** [Work-in-Progress state showing calculations/intermediate steps]
3. **Step 3:** [Final calculation and answer]

#### Exercise 2: [Descriptive Title]
...

### R Implementation
```r
# Descriptive comment explaining the R snippet
# ... R code ...
```

---

## Exam Preparation Guide

### Formula Quick-Reference
[A condensed table of every formula a student must know for this phase, matching the style of the exam formula sheet (typologio). Include only formulas that are exam-relevant.]

### Exam Checklist
| Category | Items |
|----------|-------|
| Must Memorize | [Formulas and definitions that must be recalled without reference] |
| Must Understand | [Concepts where the student must apply reasoning, not just recall] |
| Book-Only (Professor May Test) | [Topics in the textbook but rarely/never taught in lectures -- the professor has a history of testing these] |

### Common Exam Traps
- [Specific pitfalls observed in past exams or based on professor behavior patterns]

### Exam Paper Cross-References
| Exam Paper | Relevant Questions | Difficulty |
|------------|-------------------|------------|
| [Exam filename] | [Which questions map to this phase] | [1-5] |

---

## Phase Summary
[Concise summary covering core concepts, key formulas, major distinctions, and exam/practical gotchas.]
```

---

## 3. Content & Formatting Guidelines

### 3.1 Markdown & LaTeX Standards
- **Inline Math:** Must use single dollar signs `$ equation $` (e.g., $E[X] = \mu$). Never use legacy `\(` or `\)`.
- **Block Math:** Must use double dollar signs centered on their own lines:
  $$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$$
  Never use legacy `\[` or `\]`.
- **Code Blocks:** Must always specify the language syntax tag (` ```r `, ` ```python `, ` ```bash `).
- **No Emojis:** Emojis are strictly prohibited throughout all notes, headers, and code comments.

### 3.2 Theoretical Depth & Practical Context
- **No Skipping Theory:** Provide mathematical foundations (PDFs, PMFs, CDFs, expectations, variances) before introducing examples.
- **Dual-Domain Coverage:** Every phase must cover both non-time-domain (classic) and time-domain (systems/latency) contexts with equal weight. Neither domain should displace the other.
- **Gotchas & Exam Tips:** Use callout blockquotes (`> **Note:** ...`) to highlight common pitfalls, degrees of freedom mistakes, parameterization traps (e.g., R `sd` vs variance), or shortcut techniques.

### 3.3 Worked Exercises & WIP States

#### Quantity and Split
- **Total:** Every phase file must contain a minimum of **30** comprehensive solved exercises.
- **Split:** Exercises must be evenly divided between two domains:
  - **15 Non-Time-Domain Exercises:** Classic probability and statistics contexts that mirror actual university exam question styles. Examples: dice rolls, card hands, manufacturing defect rates, newspaper survey data, salary tables, medical diagnostic tests, student grades, coin flips, balls in urns, license plates, demographic data.
  - **15 Time-Domain Exercises:** Systems, latency, and performance-engineering contexts that cover book material the professor may test without having taught in lectures. Examples: response times, server uptime, execution durations, SLA percentiles (p50/p90/p95/p99), network delays, queueing delays, throughput, timestamp handling, cyclic time, unit conversions (ns/ms/s).
- **Labeling:** Each exercise title must indicate its domain:
  - Non-time-domain: `#### Exercise 5: Grouped Mean from Salary Data`
  - Time-domain: `#### Exercise 6: Grouped Mean from Latency Data (Time-Domain)`

#### Progressive Difficulty
- Include basic calculations, real-world application problems, edge cases, and R code verification.
- Exercises should progress from simple formula application to multi-step exam-style problems.

#### Work-in-Progress (WIP) States
- Step-by-step solutions must show intermediate steps, unsimplified expressions, or partial tables before displaying the final numerical answer.
- Multi-part exercises (mirroring exam structure) should label sub-questions as a, b, c, etc.

#### Exam-Style Multi-Part Exercises
- At least 5 of the 30 exercises per phase must be multi-part (3+ sub-questions) mirroring real exam structure.
- At least 3 of the 30 exercises per phase must include an R command sub-question (e.g., "What R command computes the probability in part a?").

---

## 4. Exam Preparation Guide Requirements

Every phase file must include an `## Exam Preparation Guide` section before the `## Phase Summary`. This section must contain:

### 4.1 Formula Quick-Reference
- A condensed table or list of every exam-relevant formula in the phase.
- Must match the notation and style of the official exam formula sheet (typologio).
- Exclude formulas that are book-only and never appear on exams unless explicitly noted.

### 4.2 Exam Checklist
- A three-category table: "Must Memorize," "Must Understand," and "Book-Only (Professor May Test)."
- The "Book-Only" category is critical: the professor has a documented history of testing material from the textbook that was never covered in lectures. Students must be warned about these topics explicitly.

### 4.3 Common Exam Traps
- List specific pitfalls observed in past exam papers or based on known professor behavior.
- Include warnings about book-only content appearing on exams.
- Include warnings about common calculation errors (e.g., using $n$ instead of $n-1$ for sample variance, confusing `sd` with variance in R).

### 4.4 Exam Paper Cross-References
- A table linking the phase's topics to specific exam papers in `Exams/Papers/`.
- Include the exam filename, which questions map to this phase, and the difficulty rating from `Exams/Papers/difficulty.md`.

---

## 5. Master Document Compilation Workflow

When phase notes are updated or added in `Resources/Phases/`:

1. Verify phase file compliance (H1 heading, Table of Contents, Exam Preparation Guide, Phase Summary, LaTeX syntax, no emojis).
2. Run the build script using the workspace Python environment:
   ```bash
   conda run -n py14 python Resources/Scripts/build_master.py
   ```
3. Confirm that `Resources/Probability_and_Statistics_Master.md` updates cleanly with all 8 phases included.

---

## 6. Validation Criteria

### Per-Phase Validation
| Criterion | Requirement |
|-----------|-------------|
| H1 heading | Exactly one: `# Phase N: [Name]` |
| Table of Contents | Must include all section links + Exam Preparation Guide + Phase Summary |
| Exercise count | Minimum 30 total |
| Exercise split | Approximately 15 non-time-domain + 15 time-domain |
| Multi-part exercises | At least 5 per phase |
| R command exercises | At least 3 per phase |
| Exam Preparation Guide | Must include all 4 subsections (Formula Quick-Reference, Exam Checklist, Common Exam Traps, Exam Paper Cross-References) |
| Phase Summary | Concise summary at the end |
| Emojis | Zero tolerance |
| LaTeX delimiters | `$...$` and `$$...$$` only; no `\(`, `\)`, `\[`, `\]` |
| Code blocks | Must specify language tag |

### Full Repository Validation
| Criterion | Requirement |
|-----------|-------------|
| Phase files | Exactly 8 in `Resources/Phases/` |
| Total exercises | Minimum 240 (30 × 8) |
| Master file | `Resources/Probability_and_Statistics_Master.md` exists and is non-empty |
| Archive | `Resources/Archive/Phase_Notes/` contains all original 68 `.md` files |