# Agent Instructions: Database Systems Study Material Generation

Your objective is to generate comprehensive, high-quality study notes for the Database Systems course. The source material will either be a specific lecture or laboratory PDF file located in `DATABASES/Lectures/` or a section/topic from the mindmap `DATABASES/Resources/Meta/mindmap.md`. When generating notes from the mindmap, you will not have an attached source file; instead, you must rely on your web search capabilities and internal knowledge of database systems.

---

## Input Modes

### Mode A: PDF-Based Generation
When given a PDF file from `DATABASES/Lectures/` (e.g., `Lecture_1_Databases.pdf` or `Lab_1.pdf`):
1. Extract all key concepts, definitions, rules, SQL commands, and exercises from the PDF.
2. Structure the notes to follow the PDF's flow, making sure to expand on any brief or vague points.
3. Supplement with web search to provide rich examples, clear explanations of SQL syntax, or visual ASCII diagrams.

### Mode B: Mindmap-Based Generation
When asked to generate notes for a topic in `DATABASES/Resources/Meta/mindmap.md` without an attached source file:
1. Locate the topic in `mindmap.md` to identify the subtopics and structure.
2. Use web search to gather detailed information, standards (e.g., SQL standard behavior, MySQL specifics), and pedagogical examples for each subtopic.
3. Use your internal knowledge to build comprehensive, structured, and technically deep study material for that topic.

---

## Output Structure

You must produce **exactly one Markdown file** per lecture/laboratory PDF or per top-level mindmap section.

1. **Target Directory**: All files must be saved inside the `DATABASES/Resources/Notes/` directory. Create the directory if it does not exist.
2. **One File per Topic/Lecture**: Do not split subtopics or sections into separate files. Every sub-bullet or sub-section must be covered within the single parent file.
3. **File Naming**:
   - For PDF-based files: Use `lecture_<n>_<concept_name>.md` or `lab_<n>_<concept_name>.md` (all lowercase, underscores for spaces, transliterated/translated concept name).
   - For mindmap-based files: Use `topic_<n>_<concept_name>.md` where `<n>` is the topic number (1-indexed) and `<concept_name>` is a concise English translation/transliteration of the Greek topic title.

**Naming Examples:**

| Source Material | Output File |
|---|---|
| Lecture_1_Databases.pdf | `DATABASES/Resources/Notes/lecture_1_vases_dedomenon.md` |
| Lecture_3_Conceptual_Design_and_ER_Model.pdf | `DATABASES/Resources/Notes/lecture_3_ennoiologiki_schediasi.md` |
| Lab_1.pdf | `DATABASES/Resources/Notes/lab_1_notes.md` |
| Mindmap: Eisagogi & Basikes Ennoies (Topic 1) | `DATABASES/Resources/Notes/topic_1_eisagogi_kai_vasikes_ennoies.md` |
| Mindmap: Montelo Ontotiton-Sychetiseon (Topic 3) | `DATABASES/Resources/Notes/topic_3_montelo_ontotiton_sychetiseon_er.md` |

---

## File Internal Structure

Every generated file must follow this internal structure, strictly in this order:

### 1. Title
Use the Greek topic or lecture name as the `# H1` heading, followed immediately by an English subtitle in italics.

```markdown
# Introduction & Basic Concepts
*Introduction & Basic Concepts*
```

### 2. Table of Contents
A linked Markdown table of contents mapping to each subtopic section within the file.

### 3. Introduction
A paragraph (3-5 sentences) that frames the topic within the broader context of Database Management Systems (DBMS). Explain *why* these concepts matter, what problem they solve (e.g., transition from file-based systems to DBMS), and how they connect to database design or querying.

### 4. Subtopic Sections
For each sub-topic (from the PDF slides or sub-bullets of the mindmap), create an `## H2` section. For each nested item, create an `### H3` subsection. Every section must contain:

- A clear conceptual explanation (what it is, how it works, why it exists).
- A real-world database analogy (e.g., comparing database indexes to index cards in a library, or comparing transaction ACID properties to a banking transfer).
- Key terminology in **bold** with an inline definition on first use.
- ASCII diagrams or structured text layouts representing schemas, ER diagrams, query execution paths, or architecture (e.g., 3-schema architecture, client-server DB).
- Comparative tables where contrasting concepts are discussed (e.g., DBMS vs. File Systems, Strong vs. Weak entities, DDL vs. DML, Primary Key vs. Candidate Key vs. Foreign Key, Clustered vs. Non-clustered indexes).

### 5. Summary Table
A Markdown table at the end of the file consolidating the key terms, their one-line definitions, and critical characteristics.

| Concept | Definition | Key Characteristic / Rule |
|---|---|---|
| ... | ... | ... |

### 6. Key Takeaways
A short bulleted list (5-10 bullets) of the most important facts, rules, design practices, or SQL syntax tips.

---

## Content and Formatting Guidelines

### 1. Markdown and SQL Styling
- Use standard, clean Markdown.
- All SQL code must be formatted inside ` ```sql ` fenced code blocks, adhering to professional formatting standards (keywords like `SELECT`, `INSERT`, `CREATE TABLE` in uppercase).
- Use inline backticks for SQL function names, data types (e.g., `VARCHAR`, `INT`), table/column names, and commands.

### 2. LaTeX and Math
- Use LaTeX for Relational Algebra operators and equations (e.g., selection $\sigma$, projection $\pi$, join $\bowtie$).
  - **Inline math:** `$ \sigma_{age > 20}(Employees) $`.
  - **Block math:** Double dollar signs on their own line.
- Never write raw Unicode math symbols. Always use LaTeX.

### 3. Clarity and Flow
- Write explanations in English, using standard technical terms (e.g., "Primary Key", "Foreign Key", "Join", "Query", "Transaction", "ACID", "Index", "Normal Form") as-is.
- Highlight exam-critical points using a **bold label** such as **"Exam Note:"** or **"Key Distinction:"**.

### 4. Diagrams and Schema Layouts
- For ER modeling, include ASCII/text diagrams representing entities, attributes, and relationships.
- For relational schemas, show the table name followed by attributes list, underlining Primary Keys and using dashed underlines or footnotes for Foreign Keys:
  `Employee(<u>emp_id</u>, first_name, last_name, #dept_id)`

**Example of an ER ASCII diagram:**
```text
  +--------------+               +--------------+
  |   EMPLOYEE   |               |  DEPARTMENT  |
  +--------------+     1:N       +--------------+
  |  emp_id (PK) |<>---( Works )---| dept_id (PK) |
  |  name        |     In        | dept_name    |
  +--------------+               +--------------+
```

**Example of a comparative table:**
| Feature | DBMS | File Processing System |
|---|---|---|
| Data Redundancy | Minimized via normalization | High (multiple duplicate files) |
| Concurrency Control | Built-in transaction management | Difficult or unsupported |
| Data Independence | High (logical & physical separation) | Low (data structure tied to code) |

---

## Database-Specific Requirements

- **SQL Examples with Visual Tables**: When documenting DDL/DML/DQL, always provide the input table state, the SQL query block, and the resulting table state.
- **Relational Algebra Equivalence**: For relational algebra sections, show the query in both algebraic notation and its SQL equivalent.
- **Normalization Walks**: For normalization topics, show step-by-step how a relation is decomposed, listing all functional dependencies (FDs), identifying candidate keys, and showing why a relation violates a normal form (1NF, 2NF, 3NF, BCNF) and how it is resolved.
- **English subtopic headers are required**: Use the English topic names from `mindmap.md` or the PDF lecture names as your `## H2` section headings.

---

## General Rules
- Emojis are not allowed and may not be used in any way.
- If you spot any emojis, ask whether they are needed; if the answer is no, remove them.
- Do not fabricate SQL standards or database engine features.
- All file content must be in English, with technical terms, SQL commands, and diagrams in standard form.