
**Context:** You will receive a document file. Read its full contents, then generate a self-contained quiz as described below.

***

### Base Code
Use **`quiz_base_code.html`** (located in `COMPUTER_NETWORKS/Resources/Quizes/`) as the structural and stylistic foundation. Do **not** rebuild the UI from scratch — keep its layout, theming, CSS, and JS architecture intact. Your job is to:
- Replace the placeholder questions array with questions derived from the provided document.
- Adjust any hardcoded topic labels or titles to match the document's subject.
- Preserve all existing interaction logic (instant feedback, report, shuffle/retake).

***

### Output Behavior & File Saving
- Save the generated quiz directly as an `.html` file inside the `COMPUTER_NETWORKS/Resources/Quizes/` directory.
- Use a descriptive filename matching the quiz topic (e.g., `quiz_X_topic_name.html`).
- **Directory Verification & Creation:**
  - Before saving the file, check if the directory `COMPUTER_NETWORKS/Resources/Quizes` exists.
  - If the directory does not exist, identify the main section path `COMPUTER_NETWORKS` in the project root and create the missing `Resources/Quizes` subdirectories.
- Write the complete, self-contained HTML/CSS/JS code directly to the file without using placeholders.

***

### Quiz Structure & Coverage
- Cover **all material** in the document — leave no topic unaddressed.
- Mix **theory questions** (definitions, concepts, properties) with **practical/exercise questions** (apply the concept, evaluate an expression, identify errors, fill-in-the-blank computations).
- Question order should feel varied, not grouped strictly by topic.
- There must be at least a minimum of 30 questions.

***

### Answer Option Ordering — Critical Rule
- **Correct answers must be distributed randomly across all option positions (A, B, C, D).**
- Never place the correct answer consistently as the first option.
- Before finalizing, verify that correct answers are spread across positions — roughly 25% each. If they cluster at position 0/A, shuffle the options for those questions.

***

### UI Specification
- **Theme:** Soft dark UI — dark neutral surfaces (no pure black), muted text hierarchy, subtle borders.
- **Dimensions:** Fully fluid layout — `clamp()`-based font sizes, `%`/`vw`/`vh`/`min()`/`max()` for all sizing. **Zero hardcoded pixel dimensions** on any container, width, height, or font size.
- **LaTeX rendering:** MathJax loaded via CDN, supporting both `$...$` (inline) and `$$...$$` (display/block) throughout question text and answer options.

***

### Interaction & Feedback
- **Answer reveal:** Clicking an answer option immediately shows:
  - Whether the selected answer is ✓ correct or ✗ wrong.
  - Which answer is the correct one (highlighted), regardless of what was selected.
  - All other options become unclickable after selection.
- No submit button per question — feedback is instant on click.

***

### End-of-Quiz Report
When all questions are answered, display a **status report** containing:
- Total score (e.g., 7 / 10).
- A list of each question with: ✓ or ✗, the question text, and the correct answer.
- Two action buttons:
  - **Shuffle** — randomizes question order and rerenders from question 1.
  - **Retake** — replays the exact same quiz in the same order, resetting all answers.

