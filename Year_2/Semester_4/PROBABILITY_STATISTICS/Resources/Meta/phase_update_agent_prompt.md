# Agent Instructions: Per-Phase File Update

## Objective

Update a single phase file in `Resources/Phases/` to meet the current quality standards defined in `Resources/Meta/agent_instructions.md`. Each agent instance handles **one phase file only**.

The **primary source of truth** for content is `Resources/Meta/mindmap.md`. The mindmap defines the complete scope of every phase, including both general statistics and time-domain concepts. Use the mindmap to determine what to cover, then supplement with your own knowledge and web searches to fill in all formulas, derivations, and worked examples.

---

## Target Agent Runtime & Model Configuration

- **Agent Platform:** Antigravity IDE Chat Interface (`agy`)
- **Execution Capability:** Full terminal access, file system read/write, Conda Python environment (`py14`), web search.
- **Working Directory (absolute):**
  `/home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/PROBABILITY_STATISTICS`

> All relative paths in this document are relative to the Working Directory above.
> Do NOT modify any file outside `Resources/Phases/` (except for running validation scripts).
> Use `conda run -n py14 python` for all Python executions.

---

## Step 0: Identify Your Phase

Before doing anything else, identify which phase you are updating. The user will tell you (e.g., "Update Phase 3"). Find your phase in the table below. The phase list follows the structure defined in `Resources/Meta/mindmap.md`:

| Phase | Output File | Mindmap Coverage |
|-------|------------|------------------|
| 1 | `Resources/Phases/Phase_1_Descriptive_Statistics.md` | Data organization, central tendency (incl. circular mean), position metrics (quartiles/deciles/percentiles), dispersion (incl. $c^2$ rule) |
| 2 | `Resources/Phases/Phase_2_Probability_Theory.md` | Set theory, Venn diagrams, axioms & rules (incl. 3-event inclusion-exclusion), combinatorics (incl. circular permutations, combinations with replacement) |
| 3 | `Resources/Phases/Phase_3_Conditional_Probability_Independence.md` | Conditional probability (incl. survival probability, right-censoring), independence, total probability & Bayes |
| 4 | `Resources/Phases/Phase_4_Discrete_Random_Variables.md` | PMF, expectation, variance, Binomial, Poisson (rate scaling), Geometric (memoryless), Hypergeometric, MGF/characteristic functions |
| 5 | `Resources/Phases/Phase_5_Continuous_Random_Variables_Distributions.md` | Normal, Empirical rule, Uniform, Exponential, Gamma, Erlang, Weibull, transformations |
| 5B | `Resources/Phases/Phase_5B_Multivariate_Random_Variables.md` | Joint distributions, covariance/correlation, Adam's/Eve's laws, convolution, order statistics |
| 6 | `Resources/Phases/Phase_6_Inferential_Statistics.md` | CLT, confidence intervals (mean/proportion/variance), hypothesis testing (incl. power), sampling distributions, inequalities, LLN |
| 7 | `Resources/Phases/Phase_7_Time_Domain_Data_Clock_Statistics.md` | Time series metrics (TIE, MTIE, fractional frequency offset), Allan/Hadamard variances, hardware timing & noise |
| 8 | `Resources/Phases/Phase_8_Probability_Network_Clock_Delays.md` | PTP/IEEE 1588, path delay, delay distribution modeling, multi-clock delay probabilities, Markov chains |
| 9 | `Resources/Phases/Phase_9_R_Programming_Commands.md` | Descriptive stats, distribution prefixes, distribution set, sampling gotchas, lower.tail, sd vs var |

> **Note:** Phases 7, 8, and 9 are defined in the mindmap but may not have existing archive files. For these, build the phase file entirely from the mindmap scope plus your own knowledge and web research.

---

## Step 1: Read Required Files

Read the following files before writing anything:

1. **`Resources/Meta/agent_instructions.md`** -- the current quality standards (template, exercise rules, formatting requirements).
2. **`Resources/Meta/mindmap.md`** -- the **primary source of truth**. This defines the complete scope of your phase, including all general statistics and time-domain concepts. Read the entire mindmap, not just your phase's section, so you understand how your phase connects to the others.
3. **Your current phase file** -- the file you will be rewriting (from `Resources/Phases/`). If it does not exist (e.g., for Phases 7, 8, 9), create it.
4. **`Resources/Probability_and_Statistics_Master.md`** -- the consolidated master notes. Use this as a secondary reference for formulas, derivations, and worked examples that already exist in the project.

### Supplementing with Web Search and Own Knowledge

The mindmap is a high-level outline, not a complete reference. You **must** supplement it:

- **Web search** for any formula, definition, or concept in your phase that is not fully specified in the mindmap or master notes. Verify formulas against authoritative sources (textbooks, university course notes, official documentation).
- **Use your own knowledge** to fill in standard formulas, derivations, and worked examples that are well-established in statistics and probability.
- **Do not invent formulas.** Every formula you write must be either (a) present in the mindmap/master notes, or (b) verified via web search or your own reliable knowledge.

---

## Step 2: Pre-Phase Analysis

Before writing the output file, perform the following analysis internally:

### 2a. Section Inventory
List every topic and sub-topic in your phase's section of the mindmap. Determine the logical section structure for the consolidated file. Every bullet in the mindmap must be addressed somewhere in your phase file.

### 2b. Formula Audit
Catalogue **all** formulas relevant to your phase. For each formula:
- Write the general (non-time-domain) form.
- Determine whether the formula changes or needs adaptation for time-domain data (see Step 4 for the time-domain adaptation rules).
- Flag notation conventions (e.g., $\bar{x}$ vs $\mu$, $s^2$ vs $\sigma^2$ for sample vs population) and resolve them consistently.

### 2c. Exercise Inventory
Plan the exercise set. You must produce **30 exercises total**:
- **15 general statistics exercises** using classic contexts (dice, cards, manufacturing, surveys, salaries, medical tests, grades, coins, urns, license plates, demographics).
- **15 time-domain exercises** using systems/latency contexts (response times, server uptime, execution durations, SLA percentiles, network delays, queueing, throughput, timestamps, unit conversions).
- The **last 4 exercises** (exercises 27-30) must be **combined exercises** that integrate all formulas and concepts from your phase into a single multi-part problem each. These must **increase in difficulty** from exercise 27 to exercise 30. The **final exercise (30) must contain a "gotcha moment"** -- a deliberate trap or subtle pitfall that tests whether the reader catches a common mistake.

### 2d. Gotcha Extraction
List every callout, warning, "Common Mistake," or gotcha relevant to your phase. Include both general statistics gotchas and time-domain gotchas (e.g., unit conversion errors, circular time, right-censoring, memoryless assumptions, variance scaling). Deduplicate and organize by topic.

### 2e. R Code Audit
List every R command relevant to your phase. For each, note the correct usage and any time-domain-specific gotchas (e.g., `sd` vs `var` parameters, `lower.tail = FALSE`, geometric counting failures).

---

## Step 3: Knowledge Expansion

The mindmap is the scope, but you must expand it into complete, self-contained content. For each topic in your phase:

1. **Write the complete theory** -- definitions, intuition, and context. Do not assume the reader has the mindmap open; the phase file must stand alone.
2. **Write every formula** in LaTeX, including the time-domain adapted versions where applicable.
3. **Provide proper worked examples** -- at least one fully worked example per major formula, showing intermediate steps (WIP states), not just the final answer.
4. **Include R implementation** where relevant, with correct syntax and comments.

Use web search to verify any formula or concept you are not 100% certain about. Cite the source of any non-standard or specialized content (e.g., Allan variance, PTP delay calculations) in a comment or footnote.

---

## Step 4: Formula Requirements (Including Time-Domain Adaptations)

### 4a. All Formulas Must Be Present

Your phase file must include **every formula** relevant to your phase. Do not omit formulas because they seem "obvious" or "standard." The Formula Quick-Reference section (in the Exam Preparation Guide) must list all of them in the exam typologio style.

### 4b. Time-Domain Formula Adaptations

When a formula is applied to time-domain data, it may need adaptation. You **must** explicitly write the adapted formula and **use it** in the time-domain exercises. Key adaptations include:

- **Mode (grouped data):** The general formula is
  $$M_o = L + \left( \frac{f_i - f_{i-1}}{(f_i - f_{i-1}) + (f_i - f_{i+1})} \right) \cdot w$$
  When the dataset is full of time data (e.g., seconds), write the adapted formula with time units explicitly:
  $$M_o = L_{[s]} + \left( \frac{f_i - f_{i-1}}{(f_i - f_{i-1}) + (f_i - f_{i+1})} \right) \cdot w_{[s]}$$
  where $L_{[s]}$ is the lower boundary of the modal class in seconds and $w_{[s]}$ is the class width in seconds. State that the formula structure is identical but all quantities carry time units, and the result is reported in the same time unit.

- **Mean (grouped data):** $\bar{x} = \frac{\sum f_i \cdot x_i}{n}$ -- the class marks $x_i$ carry time units; the result is in time units.

- **Variance / Standard deviation:** When converting time units, apply the $c^2$ rule: if every value is multiplied by $c$, then $s^2$ scales by $c^2$ and $s$ scales by $c$. Write this explicitly for time conversions (e.g., seconds to milliseconds: $c = 1000$, so $s^2$ scales by $10^6$).

- **Circular mean (cyclic clock times):** For clock times (e.g., 23:00, 01:00), the naive arithmetic mean is invalid. Use the circular mean:
  $$\bar{\theta} = \text{atan2}\left( \sum \sin\theta_i, \sum \cos\theta_i \right), \quad \bar{t} = \frac{24 \cdot \bar{\theta}}{2\pi}$$
  where $\theta_i = \frac{2\pi \cdot t_i}{24}$.

- **Poisson rate scaling:** When the time window changes, scale $\lambda$ proportionally: $\lambda_t = \lambda \cdot t$.

- **Conditional survival probability:** $P(T > t+s \mid T > t) = \frac{P(T > t+s)}{P(T > t)}$ -- only equals $P(T > s)$ for memoryless distributions (Exponential/Geometric).

- **Percentiles/quantiles:** The percentile value scales with the time unit, but the percentile rank does not. Write this explicitly.

**Rule:** For every formula in your phase that has a time-domain variant, you must (1) present the general formula, (2) present the time-domain adapted formula with units, and (3) use the adapted formula in at least one time-domain exercise.

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
- **15 general statistics exercises** using classic exam-style contexts
- **15 time-domain exercises** using systems/latency contexts
- Label each exercise title with its domain (time-domain exercises get `(Time-Domain)` suffix)
- At least **5 multi-part exercises** (3+ sub-questions)
- At least **3 exercises with R command sub-questions**

#### Combined Exercises (Exercises 27-30)
The **last 4 exercises** must be **combined exercises** that integrate all formulas and concepts from your phase into a single multi-part problem each. Requirements:

- **Exercise 27 (Combined, Moderate):** Integrates the core formulas of your phase into one realistic scenario. Should be solvable by a student who has mastered the individual topics.
- **Exercise 28 (Combined, Harder):** Integrates more concepts, requires multiple steps, and may require the student to choose the correct formula from several options.
- **Exercise 29 (Combined, Hard):** Integrates nearly all concepts in the phase, requires careful setup, and may involve time-domain adaptations of multiple formulas.
- **Exercise 30 (Combined, Hardest + Gotcha):** Integrates all concepts, is the most difficult, and **must contain a deliberate "gotcha moment"** -- a subtle trap that tests whether the reader catches a common mistake (e.g., using variance instead of standard deviation, forgetting to scale $\lambda$, using naive mean on circular time, forgetting the $c^2$ rule, misapplying memorylessness, confusing sample vs population variance, etc.). The solution must explicitly call out the gotcha and explain how to avoid it.

Each combined exercise must:
- Be a single scenario with multiple sub-questions (a, b, c, d, ...)
- Require the use of **multiple distinct formulas** from your phase
- Show WIP states (intermediate steps, unsimplified expressions, partial tables)
- Include the final answer in bold or boxed format
- For Exercise 30, explicitly label the gotcha in the solution (e.g., "**Gotcha:** ...")

#### Exercise Style
- Show WIP states (intermediate steps, unsimplified expressions, partial tables)
- For multi-part exercises, label sub-questions as a, b, c, etc.
- Include the final answer in bold or boxed format
- For time-domain exercises, always use the time-domain adapted formulas (Step 4b)

#### Exam Preparation Guide
Must include all 4 subsections:
1. **Formula Quick-Reference** -- matching the typologio style, including time-domain adapted formulas
2. **Exam Checklist** -- three-category table (Must Memorize / Must Understand / Book-Only)
3. **Common Exam Traps** -- specific pitfalls, book-only warnings, calculation errors, time-domain gotchas
4. **Exam Paper Cross-References** -- if exam papers exist for your phase, link to them with difficulty ratings. If no exam papers exist (e.g., Phases 7, 8), note this and instead reference the relevant mindmap sections.

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
r_exercises = len(re.findall(r'[Rr] command|dbinom|pnorm|pbinom|dnorm|qnorm|dpois|ppois|dgeom|pgeom|dhyper|phyper|dexp|pexp|dgamma|pgamma|punif|qunif|pchisq|pt|pf|quantile|mean|median|var|sd|IQR|fivenum|table|which\\.max', content))
if r_exercises < 3:
    errors.append(f'Insufficient R command references: {r_exercises} (minimum 3 required).')

# Rule 10: Exam Preparation Guide subsections.
for subsection in ['Formula Quick-Reference', 'Exam Checklist', 'Common Exam Traps', 'Exam Paper Cross-References']:
    if subsection not in content:
        errors.append(f'Missing Exam Preparation Guide subsection: {subsection}')

# Rule 11: At least 15 time-domain exercises (check for Time-Domain suffix).
time_domain = len(re.findall(r'\(Time-Domain\)', content))
if time_domain < 15:
    errors.append(f'Insufficient time-domain exercises: {time_domain} (minimum 15 required).')

# Rule 12: Last 4 exercises are combined (check for Combined label in exercises 27-30).
combined = len(re.findall(r'\(Combined', content))
if combined < 4:
    errors.append(f'Insufficient combined exercises: {combined} (minimum 4 required).')

# Rule 13: Exercise 30 has a gotcha moment.
if 'Gotcha' not in content:
    errors.append('Missing gotcha moment (required in Exercise 30).')

if errors:
    print('PHASE VALIDATION FAILED:')
    for e in errors:
        print(f'  - {e}')
    sys.exit(1)
else:
    print(f'Phase validation passed. Exercises found: {ex_count}')
    print(f'  Multi-part exercises: {multi_part}')
    print(f'  R command references: {r_exercises}')
    print(f'  Time-domain exercises: {time_domain}')
    print(f'  Combined exercises: {combined}')
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
- Every topic from the mindmap's phase section is addressed somewhere in the file

---

## Quality Assurance Checklist

Before declaring your work complete, verify:

- [ ] Phase file has exactly one H1 heading
- [ ] Table of Contents includes all sections + Exam Preparation Guide + Phase Summary
- [ ] Each section follows the 4-part structure (Theory, Formulas, Exercises, R Implementation)
- [ ] 30+ exercises total (15 general statistics + 15 time-domain)
- [ ] At least 5 multi-part exercises
- [ ] At least 3 exercises with R command sub-questions
- [ ] Last 4 exercises (27-30) are combined exercises integrating all phase concepts
- [ ] Combined exercises increase in difficulty (27 < 28 < 29 < 30)
- [ ] Exercise 30 contains a deliberate gotcha moment, explicitly labeled in the solution
- [ ] All formulas from the mindmap phase section are present
- [ ] Time-domain adapted formulas are written explicitly (with units) and used in time-domain exercises
- [ ] Mode formula for time data is written with time units and used
- [ ] Exam Preparation Guide has all 4 subsections
- [ ] Formula Quick-Reference matches the exam typologio style and includes time-domain variants
- [ ] Exam Checklist includes "Book-Only (Professor May Test)" category
- [ ] Common Exam Traps includes time-domain gotchas (unit conversion, circular time, memorylessness, $c^2$ rule)
- [ ] Exam Paper Cross-References table links to actual exam files with difficulty ratings (or notes absence for Phases 7, 8)
- [ ] Zero emojis
- [ ] No legacy LaTeX delimiters
- [ ] All code blocks have language tags
- [ ] Validation script passes