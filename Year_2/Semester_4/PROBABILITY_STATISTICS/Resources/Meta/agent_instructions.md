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
- **Step 1:** [Initial setup and parameter mapping]
- **Step 2:** [Work-in-Progress state showing calculations/intermediate steps]
- **Step 3:** [Final calculation and answer]

#### Exercise 2: [Descriptive Title]
...

### R Implementation
```r
# Descriptive comment explaining the R snippet
# ... R code ...
```

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
- **Time-Domain & Systems Context:** Highlight how concepts apply to physical/system metrics (e.g., execution durations, server latencies, timestamps, queueing delays).
- **Gotchas & Exam Tips:** Use callout blockquotes (`> **Note:** ...`) to highlight common pitfalls, degrees of freedom mistakes, parameterization traps (e.g., R `sd` vs variance), or shortcut techniques.

### 3.3 Worked Exercises & WIP States
- **Quantity:** Every phase file must contain a minimum of **30** comprehensive solved exercises.
- **Progressive Difficulty:** Include basic calculations, real-world application problems, edge cases, and R code verification.
- **Work-in-Progress (WIP) States:** Step-by-step solutions must show intermediate steps, unsimplified expressions, or partial tables before displaying the final numerical answer.

---

## 4. Master Document Compilation Workflow

When phase notes are updated or added in `Resources/Phases/`:

1. Verify phase file compliance (H1 heading, Table of Contents, Phase Summary, LaTeX syntax, no emojis).
2. Run the build script using the workspace Python environment:
   ```bash
   conda run -n py14 python Resources/Scripts/build_master.py
   ```
3. Confirm that `Resources/Probability_and_Statistics_Master.md` updates cleanly with all 8 phases included.