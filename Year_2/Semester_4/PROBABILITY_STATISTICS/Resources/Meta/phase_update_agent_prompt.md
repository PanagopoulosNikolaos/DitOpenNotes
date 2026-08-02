# Agent Instructions: Per-Phase File Update

## Objective

Update a single phase file in `Resources/Phases/` to meet the current quality standards defined in `Resources/Meta/agent_instructions.md`. Each agent instance handles **one phase file only**.

---

## Target Agent Runtime & Model Configuration

- **Agent Platform:** Antigravity IDE Chat Interface (`agy`)
- **Execution Capability:** Full terminal access, file system read/write, Conda Python environment (`py14`).
- **Working Directory (absolute):**
  `/home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/PROBABILITY_STATISTICS`

> All relative paths in this document are relative to the Working Directory above.
> Do NOT modify any file outside `Resources/Phases/` (except for running validation scripts).
> Use `conda run -n py14 python` for all Python executions.

---

## Step 0: Identify Your Phase

Before doing anything else, identify which phase you are updating. The user will tell you (e.g., "Update Phase 3"). Find your phase in the table below:

| Phase | Output File | Source Archive Directory | Source File Count |
|-------|------------|--------------------------|-------------------|
| 1 | `Resources/Phases/Phase_1_Descriptive_Statistics.md` | `Resources/Archive/Phase_Notes/Phase_1_Descriptive_Statistics/` | 10 files (5 pairs) |
| 2 | `Resources/Phases/Phase_2_Probability_Theory.md` | `Resources/Archive/Phase_Notes/Phase_2_Probability_Theory/` | 8 files (4 pairs) |
| 3 | `Resources/Phases/Phase_3_Conditional_Probability_Independence.md` | `Resources/Archive/Phase_Notes/Phase_3_Conditional_Probability_Independence/` | 6 files (3 pairs) |
| 4 | `Resources/Phases/Phase_4_Discrete_Random_Variables.md` | `Resources/Archive/Phase_Notes/Phase_4_Discrete_Random_Variables/` | 10 files (5 pairs) |
| 5 | `Resources/Phases/Phase_5_Continuous_Random_Variables_Distributions.md` | `Resources/Archive/Phase_Notes/Phase_5_Continuous_Random_Variables_Distributions/` | 10 files (5 pairs) |
| 5B | `Resources/Phases/Phase_5B_Multivariate_Random_Variables.md` | `Resources/Archive/Phase_Notes/Phase_5B_Multivariate_Random_Variables/` | 6 files (3 pairs) |
| 6 | `Resources/Phases/Phase_6_Inferential_Statistics.md` | `Resources/Archive/Phase_Notes/Phase_6_Inferential_Statistics/` | 10 files (5 pairs) |
| 7 | `Resources/Phases/Phase_7_R_Programming_Commands.md` | `Resources/Archive/Phase_Notes/Phase_7_R_Programming_Commands/` | 8 files (4 pairs) |

---

## Step 1: Read Required Files

Read the following files before writing anything:

1. **`Resources/Meta/agent_instructions.md`** -- the current quality standards (template, exercise rules, exam prep requirements).
2. **Your current phase file** -- the file you will be rewriting (from `Resources/Phases/`).
3. **All source archive files for your phase** -- every `.md` file in your phase's archive directory (listed above). These contain the original granular notes (both standard and time-variant versions). Read them all.
4. **At least 2 exam papers** from `Exams/Papers/` that are relevant to your phase (see the Exam Relevance Table in Step 3).
5. **At least 1 exam solution** from `Exams/Papers/solutions/` to understand the expected solution format.
6. **`Exams/Papers/difficulty.md`** -- to understand difficulty ratings for the cross-reference table.

---

## Step 2: Pre-Phase Analysis

Before writing the output file, perform the following analysis internally:

### 2a. Section Inventory
List every unique `##` and `###` heading across all source archive files. Determine the logical section structure for the consolidated file.

### 2b. Formula Audit
Catalogue all distinct formulas from the source files. Flag notation inconsistencies (e.g., $\bar{x}$ vs $\mu$, $s^2$ vs $\sigma^2$ for sample vs population). Resolve them using the notation from the exam formula sheet (see Step 4).

### 2c. Exercise Inventory
Number every worked exercise found across all source files. Classify each as:
- **Non-time-domain:** Uses classic contexts (dice, cards, manufacturing, surveys, salaries, medical tests, grades, coins, urns, license plates, demographics).
- **Time-domain:** Uses systems/latency contexts (response times, server uptime, execution durations, SLA percentiles, network delays, queueing, throughput, timestamps, unit conversions).
- **Duplicate:** Same mathematical structure as another exercise, just a different context skin.

### 2d. Gotcha Extraction
List every callout, warning, "Common Mistake," or gotcha block from all source files. Deduplicate and organize by topic.

### 2e. R Code Audit
List every unique ` ```r ` block from all source files. Flag duplicates.

### 2f. Exam Mapping
Identify which exam paper questions map to your phase. Note the exam structure (multi-part questions, R command sub-questions, formula sheet usage).

---

## Step 3: Exam Relevance Table

The table below maps each phase to the exam papers that contain relevant questions. Use this to populate the Exam Paper Cross-References section and to model your exercise style.

| Phase | Exam Papers with Relevant Questions | Typical Exam Question Structure |
|-------|-------------------------------------|--------------------------------|
| 1 | All papers (Thema 4 in most); 2026_06_09_Team_B (Thema 1) | Grouped frequency table: compute mean, quartiles, SD, mode, percentage, R commands, Empirical Rule interval |
| 2 | All papers (Thema 2 in most); 2026_06_09_Team_B (Thema 2) | Set probability: P(A or B), P(neither), P(only A), P(A given B) with 2-3 events |
| 3 | Intermediate_1, Intermediate_2, Hard_1, Hard_2 | Bayes' theorem with 3 machines/tests; conditional probability proofs; independence testing |
| 4 | All papers (Thema 1 in most); 2026_06_09_Team_B (Thema 3) | Binomial: P(exactly k defective), P(2 or more), P(at most k), expected value, R command, justify distribution choice |
| 5 | All papers (Thema 3 in most); 2026_06_09_Team_B (Thema 4) | Normal: P(X > x), P(a < X < b) with given Phi values, R command, empirical rule |
| 5B | Rarely on exams (book-only) | Joint PDFs, covariance, order statistics -- warn students this is book-only |
| 6 | Rarely on exams (book-only) | CLT, confidence intervals, hypothesis testing -- warn students this is book-only |
| 7 | All papers (sub-questions within Thema 1, 3, 4); 2026_06_09_Team_B (Thema 1iv, 3e, 4iii) | R commands: `dbinom`, `pnorm`, `names(which.max(table()))`, `sd()`, `pbinom()`, `pnorm()` etc. |

### Exam Difficulty Ratings (from `Exams/Papers/difficulty.md`)

| Rating | Exam Papers |
|--------|------------|
| 1/5 (Easy) | `Exam_paper_Easy.md`, `Exam_paper_2024_09_06_Team_A.md` |
| 2/5 (Lower-Intermediate) | `Exam_paper_Intermediate_1.md`, `Exam_paper_2023_06_12_Team_null.md`, `Exam_paper_2024_06_14_Team_B.md`, `Exam_paper_2024_06_14_Team_C.md`, `Exam_paper_2025_06_03_Team_A.md`, `Exam_paper_2026_06_09_Team_A.md`, `Exam_paper_2026_06_09_Team_B.md` |
| 3/5 (Upper-Intermediate) | `Exam_paper_Intermediate_2.md` |
| 4/5 (Hard) | `Exam_paper_Hard_1.md` |
| 5/5 (Very Hard) | `Exam_paper_Hard_2.md` |

---

## Step 4: Official Exam Formula Sheet (Typologio)

The exam provides a formula sheet. Your Formula Quick-Reference section must match this style and cover these formulas (only those relevant to your phase):

**Descriptive Statistics:**
- Mean (ungrouped): $\bar{X} = \frac{1}{n} \sum_{i=1}^n X_i$
- Mean (grouped): $\bar{X} = \frac{1}{n} \sum_{i=1}^k X_i f_i$
- Variance (ungrouped): $s^2 = \frac{1}{n-1} \sum_{i=1}^n (x_i - \bar{x})^2$
- Variance (grouped): $s^2 = \frac{1}{n-1} \sum_{i=1}^k (X_i - \bar{X})^2 \cdot f_i$
- Coefficient of Variation: $CV = s / \bar{x}$
- Median (grouped): $M_e = L + \left( \frac{\frac{n}{2} - F_{i-1}}{f_i} \right) \cdot w$
- Quartiles (grouped): $Q_k = L + \left( \frac{\frac{k \cdot n}{4} - F_{i-1}}{f_i} \right) \cdot w, \quad k = 1, 2, 3$
- Mode (grouped): $M_o = L + \left( \frac{f_i - f_{i-1}}{(f_i - f_{i-1}) + (f_i - f_{i+1})} \right) \cdot w$

**Probability:**
- Classical definition: $P(A) = \frac{N(A)}{N(\Omega)}$
- Complement: $P(A') = 1 - P(A)$
- Addition rule: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
- Conditional probability: $P(A \mid B) = \frac{P(A \cap B)}{P(B)}, \quad P(B) > 0$
- Multiplication rule: $P(A \cap B) = P(A \mid B)P(B)$
- Independence: $P(A \cap B) = P(A)P(B)$
- Total probability: $P(B) = \sum_{i=1}^n P(B \cap A_i)$
- Bayes' theorem: $P(A_i \mid B) = \frac{P(B \mid A_i)P(A_i)}{\sum_{k=1}^n P(B \mid A_k)P(A_k)}$

---

## Step 5: Write the Updated Phase File

Write the output to the exact path specified in the Phase Table (Step 0). Follow the template structure from `Resources/Meta/agent_instructions.md` (Section 2).

### Critical Requirements

#### Structure
- Each topic section must follow: `### Core Theory & Definitions` -> `### Mathematical Formulas & Derivations` -> `### Worked Exercises` -> `### R Implementation`
- Exercises are distributed within each section (not in a single block at the end)
- Remove standalone "Time-Specific Gotchas" sections; integrate gotchas as callout blockquotes within relevant sections
- Include `## Exam Preparation Guide` before `## Phase Summary`

#### Exercise Count and Split
- **30 exercises minimum** per phase file
- **15 non-time-domain** exercises using classic exam-style contexts
- **15 time-domain** exercises using systems/latency contexts
- Label each exercise title with its domain (time-domain exercises get `(Time-Domain)` suffix)
- At least **5 multi-part exercises** (3+ sub-questions, mirroring exam structure)
- At least **3 exercises with R command sub-questions**

#### Exercise Style
- Model non-time-domain exercises on actual exam question styles (read the exam papers)
- Model time-domain exercises on the source archive's time-variant files
- Show WIP states (intermediate steps, unsimplified expressions, partial tables)
- For multi-part exercises, label sub-questions as a, b, c, etc.
- Include the final answer in bold or boxed format

#### Exam Preparation Guide
Must include all 4 subsections:
1. **Formula Quick-Reference** -- matching the typologio style (Step 4)
2. **Exam Checklist** -- three-category table (Must Memorize / Must Understand / Book-Only)
3. **Common Exam Traps** -- specific pitfalls, book-only warnings, calculation errors
4. **Exam Paper Cross-References** -- table linking to relevant exam files with difficulty ratings

#### Formatting
- No emojis (zero tolerance)
- LaTeX: `$...$` for inline, `$$...$$` for block (no `\(`, `\)`, `\[`, `\]`)
- Code blocks must specify language tag (` ```r `, ` ```python `, ` ```bash `)
- Tables must be pipe-delimited with header separator rows

---

## Step 6: Validation

After writing the phase file, run this validation script:

```bash
conda run -n py14 python -c "
import re, sys

phase_file = 'RESOURCES_PHASES_PATH'  # Replace with actual path
with open(phase_file, 'r', encoding='utf-8') as f:
    content = f.read()

errors = []

# Rule 1: Must have a top-level H1 heading.
if not re.search(r'^# .+', content, re.MULTILINE):
    errors.append('Missing H1 heading.')

# Rule 2: Must have a Table of Contents section.
if '## Table of Contents' not in content:
    errors.append('Missing Table of Contents section.')

# Rule 3: Must have an Exam Preparation Guide section.
if '## Exam Preparation Guide' not in content:
    errors.append('Missing Exam Preparation Guide section.')

# Rule 4: Must have a Phase Summary section.
if '## Phase Summary' not in content and '## Phase' not in content:
    errors.append('Missing Phase Summary section.')
elif 'Summary' not in content:
    errors.append('Missing Phase Summary section.')

# Rule 5: No emojis.
emoji_pattern = re.compile(
    r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF'
    r'\U0001F680-\U0001F6FF\U0001F700-\U0001FAFF]'
)
if emoji_pattern.search(content):
    errors.append('Emoji detected.')

# Rule 6: Minimum 30 exercises.
ex_count = len(re.findall(r'^#### Exercise \d+:', content, re.MULTILINE))
if ex_count < 30:
    errors.append(f'Insufficient exercises: {ex_count} (minimum 30 required).')

# Rule 7: No legacy LaTeX delimiters.
latex_legacy = re.compile(r'\\\\[\\(\\[\\)\\]]')
if latex_legacy.search(content):
    errors.append('Legacy LaTeX delimiters detected.')

# Rule 8: At least 5 multi-part exercises (check for sub-question labels).
multi_part = len(re.findall(r'\\*\\*[a-c]\\)\\s', content))
if multi_part < 5:
    errors.append(f'Insufficient multi-part exercises: {multi_part} (minimum 5 required).')

# Rule 9: At least 3 R command exercises.
r_exercises = len(re.findall(r'[Rr] εντολή|[Rr] command|dbinom|pnorm|pbinom|dnorm|qnorm|dpois|ppois|dgeom|pgeom|dhyper|phyper|dexp|pexp|dgamma|pgamma|punif|qunif|pchisq|pt|pf|quantile|mean|median|var|sd|IQR|fivenum|table|which\\.max', content))
if r_exercises < 3:
    errors.append(f'Insufficient R command references: {r_exercises} (minimum 3 required).')

# Rule 10: Exam Preparation Guide subsections.
for subsection in ['Formula Quick-Reference', 'Exam Checklist', 'Common Exam Traps', 'Exam Paper Cross-References']:
    if subsection not in content:
        errors.append(f'Missing Exam Preparation Guide subsection: {subsection}')

if errors:
    print('PHASE VALIDATION FAILED:')
    for e in errors:
        print(f'  - {e}')
    sys.exit(1)
else:
    print(f'Phase validation passed. Exercises found: {ex_count}')
    print(f'  Multi-part exercises: {multi_part}')
    print(f'  R command references: {r_exercises}')
"
```

Replace `RESOURCES_PHASES_PATH` with the actual path to your phase file.

> If validation fails, fix the phase file and re-run the gate. Do not stop until all checks pass.

---

## Step 7: Post-Write Verification

After validation passes, verify the file is well-formed:

```bash
wc -l RESOURCES_PHASES_PATH
head -20 RESOURCES_PHASES_PATH
tail -20 RESOURCES_PHASES_PATH
```

Confirm:
- The file starts with `# Phase N: [Name]`
- The file ends with the Phase Summary
- The Table of Contents links match the actual section headings
- No content was accidentally truncated

---

## Quality Assurance Checklist

Before declaring your work complete, verify:

- [ ] Phase file has exactly one H1 heading
- [ ] Table of Contents includes all sections + Exam Preparation Guide + Phase Summary
- [ ] Each section follows the 4-part structure (Theory, Formulas, Exercises, R Implementation)
- [ ] 30+ exercises total (approximately 15 non-time-domain + 15 time-domain)
- [ ] At least 5 multi-part exercises
- [ ] At least 3 exercises with R command sub-questions
- [ ] Exam Preparation Guide has all 4 subsections
- [ ] Formula Quick-Reference matches the exam typologio style
- [ ] Exam Checklist includes "Book-Only (Professor May Test)" category
- [ ] Common Exam Traps includes warning about book-only content on exams
- [ ] Exam Paper Cross-References table links to actual exam files with difficulty ratings
- [ ] Zero emojis
- [ ] No legacy LaTeX delimiters
- [ ] All code blocks have language tags
- [ ] Validation script passes