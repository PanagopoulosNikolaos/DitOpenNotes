# Ηλεκτρομαγνητισμός και Τηλεπικοινωνίες (Course 201)

## Επισκόπηση Μαθήματος
Το μάθημα καλύπτει τις θεμελιώδεις αρχές της κλασικής ηλεκτροδυναμικής, του διανυσματικού λογισμού πεδίων, της ηλεκτροστατικής και μαγνητοστατικής, των εξισώσεων του Maxwell σε ολοκληρωτική και διαφορική μορφή, καθώς και τη διάδοση ηλεκτρομαγνητικών κυμάτων και γραμμών μεταφοράς.

- **Κωδικός Μαθήματος:** 201 (ΑΡΧΕΣ ΗΛΕΚΤΡΟΜΑΓΝΗΤΙΣΜΟΥ & ΤΗΛΕΠΙΚΟΙΝΩΝΙΩΝ)
- **Προαπαιτούμενα:** Μαθηματική Ανάλυση (Course 101), Γραμμική Άλγεβρα (Course 102)
- **Εξάμηνο:** 2ο
- **ECTS:** 6

---

## Δομή Καταλόγου

* **[Assignments/](Assignments/)**: Εργασίες θεωρίας και ασκήσεων:
  - [`assignment_01_electrostatics_and_dielectrics.md`](Assignments/assignment_01_electrostatics_and_dielectrics.md): Νόμος του Gauss, δυναμικό, εξίσωση Poisson και σύνθετα διηλεκτρικά.
  - [`assignment_02_magnetostatics_and_induction.md`](Assignments/assignment_02_magnetostatics_and_induction.md): Νόμος του Ampère, ομοαξονικά καλώδια, μαγνητική ροπή και επαγωγή Faraday.
* **[Examples/](Examples/)**: Υπολογιστικά εργαλεία και συμβολικός διανυσματικός λογισμός:
  - [`electromagnetics_vector_calculus_sympy.ipynb`](Examples/electromagnetics_vector_calculus_sympy.ipynb): Διαδραστικό Jupyter Notebook συμβολικών υπολογισμών πεδίων με SymPy.
  - [`examples_vector_calculus.py`](Examples/examples_vector_calculus.py): Αυτόνομο script υπολογισμού κλίσης (gradient), απόκλισης (divergence) και στροβιλισμού (curl).
* **[Exams/](Exams/)**: Υλικό εξετάσεων και επαναληπτικά τεστ:
  - [`practice_exam_01.md`](Exams/practice_exam_01.md): Πλήρες διαγώνισμα θεωρίας και ασκήσεων (επίπεδα κύματα, αγωγοί, πυκνωτές).
  - [`practice_exam_02.md`](Exams/practice_exam_02.md): Επαναληπτικό τεστ ηλεκτροστατικής και μαγνητοστατικής.
  - [`practice_exam_03.md`](Exams/practice_exam_03.md): Διαγώνισμα προσομοίωσης με κανόνες Kirchhoff και δυνάμεις Coulomb/Lorentz.
  - [`theory_answers.pdf`](Exams/theory_answers.pdf): Απαντήσεις θεμάτων θεωρίας.
  - **`Papers/`**: Παλαιότερα θέματα εξετάσεων με σαρωμένα πρωτότυπα και μεταγραφές:
    - [`Exam_paper_2024_09_23_Team_B.md`](Exams/Papers/Exam_paper_2024_09_23_Team_B.md)
    - [`Exam_paper_2026_06_Team_A.md`](Exams/Papers/Exam_paper_2026_06_Team_A.md) έως [`Team_D.md`](Exams/Papers/Exam_paper_2026_06_Team_D.md)
* **[Exercises/](Exercises/)**: Θεματικές σειρές ασκήσεων με αναλυτικές λύσεις:
  - [`exercises_electrostatics_and_gauss_law.md`](Exercises/exercises_electrostatics_and_gauss_law.md): Ηλεκτροστατική και νόμος του Gauss.
  - [`exercises_maxwell_equations_and_plane_waves.md`](Exercises/exercises_maxwell_equations_and_plane_waves.md): Εξισώσεις Maxwell, επίπεδα κύματα και διάνυσμα Poynting.
* **[Lectures/](Lectures/)**: Επίσημες διαλέξεις μαθήματος σε PDF (`01_ΗΜ.pdf` έως `09_ΗΜ.pdf`).
* **[Projects/](Projects/)**:
  - [`project_01_electromagnetic_field_simulation_python.md`](Projects/project_01_electromagnetic_field_simulation_python.md): Εξαμηνιαίο συνθετικό project αριθμητικής επίλυσης της εξίσωσης Laplace/Poisson με FDM σε Python.
* **[Resources/](Resources/)**:
  - [`resources.md`](Resources/resources.md): Προτεινόμενη διεθνής και ελληνική βιβλιογραφία (Cheng, Hayt κ.ά.).
  - [`Meta/mindmap_electromagnetics_and_transmission_lines.md`](Resources/Meta/mindmap_electromagnetics_and_transmission_lines.md): Εννοιολογικός χάρτης μαθήματος.
  - `Notes/`: Αναλυτικές σημειώσεις θεωρίας και συνοπτικό τυπολόγιο (`notes_electromagnetics_summary.md`, `notes_electrostatics...`, `notes_maxwell...`).
* **[Tutorials/](Tutorials/)**:
  - [`tutorial_01_vector_calculus_for_electromagnetics.md`](Tutorials/tutorial_01_vector_calculus_for_electromagnetics.md): Μαθηματικό υπόβαθρο διανυσματικού λογισμού.
  - [`tutorial_02_transmission_line_calculations_smith_chart.md`](Tutorials/tutorial_02_transmission_line_calculations_smith_chart.md): Γραμμές μεταφοράς και υπολογισμοί με χάρτη Smith.

---

## Εκτέλεση Παραδειγμάτων

```bash
cd Examples

# Εκτέλεση του script διανυσματικού λογισμού
python3 examples_vector_calculus.py
```
