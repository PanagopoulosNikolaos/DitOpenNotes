# Agent Instructions: Study Guide Material Generation

Your objective is to read the `Lectures/study_guide.md` file and generate comprehensive, high-quality study notes for each topic covered in the guide. You are strongly encouraged to use your web search capabilities to gather additional information, clarify complex theoretical concepts, or find insightful real-world examples.

## Output Structure

For each Phase in the study guide, you must:
1. **Target Directory**: All folders and files generated must be saved inside the `Lectures/` directory. If the specific phase directory does not exist, you must create it explicitly.
2. **Phase Directories**: Create a directory inside `Lectures/` named after the phase (e.g., `Lectures/Phase_1_Descriptive_Statistics`).
3. **Markdown Files**: Create individual Markdown files inside the corresponding phase directory for every individual bullet point and sub-bullet point.
4. **File Naming**: Name the files using the format: `phase_<n>_<bullet_num>_<concept_covered>.md` (e.g., `phase_1_1_frequency_tables.md`). Keep the names concise, descriptive, and use underscores for spaces.

## Content & Formatting Guidelines

When generating the content for each file, strictly adhere to the following rules:

### 1. Markdown & LaTeX Styling
- Use standard, clean Markdown structure (Headings, lists, bold text for emphasis).
- Use LaTeX for all mathematical notation:
  - **Inline math:** Use single dollar signs `$ equation $` (no indentation).
  - **Block math:** Use double dollar signs `$$ equation $$` to center and indent equations on their own line.

### 2. Clarity & Flow
- Follow a clear, logical progression from top to bottom.
- Explain concepts concisely but **do not leave out any important information or edge cases**. 
- Always highlight the easiest and most practical way of solving problems.
- If there is a pattern, shortcut, or specific technique that can save a lot of time during exams, make sure to explicitly mention and emphasize it.

### 3. Theoretical Depth & Web Search
- **Do not skip theory.** You must provide the mathematical foundation before jumping into examples.
- For example, when explaining frequency tables for ungrouped and grouped data, you must clearly dictate the exact formula and logic used to calculate *each* specific column (absolute, relative, cumulative).
- **Use Web Search:** Use web search whenever necessary to research and confirm facts, supplement your theoretical explanations, or find better analogies and examples for the concepts.

### 4. Interactive & Progressive Examples
- Provide detailed, step-by-step examples. **You must include at least 8 solved examples or exercises in every file you generate.**
- When demonstrating a computational process (like filling out a frequency table or applying a formula), do not just provide the final answer.
- **Provide "Work-in-Progress" states:** Show a half-finished column or equation, explicitly explain the calculation required to find the next value, and *then* display the fully completed table or solved equation.

## General Rules
- Emojis are not allowed and may not be used in any way.
- If you spot any emojis you are to ask if these are needed if the response is no you may remove them.