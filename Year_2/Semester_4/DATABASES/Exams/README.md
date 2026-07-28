# Database Exams & Synthetic Finals Directory

Welcome to the **Databases Exam Preparation Hub**. This directory contains topic-focused practice drills, synthetic mock final exams, and automated compilation scripts.

---

## Directory Structure

```
Exams/
├── README.md                           # Master index and usage guide (this file)
├── general_exam_subjects.md            # Detailed syllabus and exam format breakdown
├── combine_notes.py                    # Build script to generate all_exams.md
├── all_exams.md                        # Master compiled markdown document
├── Practice_Exams/                     # Topic-specific practice drills
│   ├── Practice_Exam_01_Easy.md        # Level: Easy (Basic DDL & SQL)
│   ├── Practice_Exam_02_Medium.md      # Level: Medium (2NF, INNER JOINs)
│   ├── Practice_Exam_03_Intermediate.md# Level: Intermediate (ACID, Outer JOINs, FDs)
│   ├── Practice_Exam_04_Hard.md        # Level: Hard (3NF/BCNF, Correlated Subqueries)
│   ├── Practice_Exam_05_Advanced.md    # Level: Advanced (Indexes, Weak Entities, CASCADE)
│   ├── Practice_Exam_06_Image_Translation.md # Image to ER Diagram & Relational Schema
│   ├── Practice_Exam_07_Topic_8_9.md    # Natural JOINs, Security & Relational Algebra
│   └── Practice_Exam_08_Topic_all_in_one_exam.md # Full-Length All-In-One Exam
├── Synthetic_Finals/                   # Synthetic Mock Final Exams (15–20 simulated papers)
│   └── (Synthetic_Exam_01.md ... Synthetic_Exam_20.md)
└── images/                             # ER diagrams and exam paper scan references
    ├── Exam_paper_null_null_null.png   # Standard final exam paper template layout
    └── hospital-er-diagram-1.png       # Hospital ER Diagram solution asset
```

---

## Practice Drills Index

| Exam File | Difficulty Level | Core Topics Covered |
| :--- | :--- | :--- |
| [Practice_Exam_01_Easy.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/DATABASES/Exams/Practice_Exams/Practice_Exam_01_Easy.md) | Easy | DDL, Primary Keys, Foreign Keys, Simple SELECT |
| [Practice_Exam_02_Medium.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/DATABASES/Exams/Practice_Exams/Practice_Exam_02_Medium.md) | Medium | 2NF Normalization, INNER JOINs, M:N Relational Mapping |
| [Practice_Exam_03_Intermediate.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/DATABASES/Exams/Practice_Exams/Practice_Exam_03_Intermediate.md) | Intermediate | ACID Atomicity, LEFT JOINs, Functional Dependency Closures |
| [Practice_Exam_04_Hard.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/DATABASES/Exams/Practice_Exams/Practice_Exam_04_Hard.md) | Hard | TRUNCATE vs DELETE, BCNF Decomposition, Correlated Subqueries |
| [Practice_Exam_05_Advanced.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/DATABASES/Exams/Practice_Exams/Practice_Exam_05_Advanced.md) | Advanced | Indexes, Weak Entities, M:N Junction Tables, CASCADE |
| [Practice_Exam_06_Image_Translation.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/DATABASES/Exams/Practice_Exams/Practice_Exam_06_Image_Translation.md) | Extracted | Exam Paper Translation, Mermaid ER Diagrams, Relational Schema |
| [Practice_Exam_07_Topic_8_9.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/DATABASES/Exams/Practice_Exams/Practice_Exam_07_Topic_8_9.md) | Specialized | Natural JOIN, Rainbow Tables, Social Engineering, Security |
| [Practice_Exam_08_Topic_all_in_one_exam.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/DATABASES/Exams/Practice_Exams/Practice_Exam_08_Topic_all_in_one_exam.md) | Full Comprehensive | All-In-One Exam (Part A: ER & Schema, Part B: SQL & BCNF) |

---

## Synthetic Final Exams (15–20 Mock Papers)

Synthetic mock exams should be placed in `Synthetic_Finals/` following the naming convention `Synthetic_Exam_XX.md`. Each synthetic exam is styled after the standard final paper layout ([Exam_paper_null_null_null.png](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/DATABASES/Exams/images/Exam_paper_null_null_null.png)).

---

## Compiling All Exams

To merge all practice drills and synthetic mock exams into a single consolidated file (`all_exams.md`), execute `combine_notes.py`:

```bash
python combine_notes.py
```
