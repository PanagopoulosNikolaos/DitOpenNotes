# Γραμμική Άλγεβρα (Course 102)

## Επισκόπηση Μαθήματος
Το μάθημα καλύπτει τις θεμελιώδεις έννοιες και τις υπολογιστικές τεχνικές της σύγχρονης Γραμμικής Άλγεβρας:
- Διανύσματα στο $\mathbb{R}^n$, γραμμικοί συνδυασμοί, γραμμική εξάρτηση/ανεξαρτησία, εσωτερικό γινόμενο και νόρμες.
- Άλγεβρα πινάκων, αντιστροφή πινάκων, ορίζουσες και επίλυση γραμμικών συστημάτων με απαλοιφή Gauss-Jordan και κανόνα Cramer.
- Διανυσματικοί χώροι και υπόχωροι, βάση, διάσταση, χώρος στηλών, μηδενοχώρος και θεώρημα βαθμού-μηδενικότητας.
- Γραμμικοί μετασχηματισμοί, πίνακες αναπαράστασης και αλλαγή βάσης.
- Ορθογωνιότητα, διαδικασία Gram-Schmidt, προβολές, παραγοντοποίηση QR και μέθοδος ελαχίστων τετραγώνων.
- Ιδιοτιμές, ιδιοδιανύσματα, διαγωνιοποίηση πινάκων και εφαρμογές σε συστήματα διαφορικών εξισώσεων, αλυσίδες Markov και αλγόριθμο PageRank.
- Παραγοντοποιήσεις Cholesky και SVD (Ανάλυση Ιδιαζουσών Τιμών) με εφαρμογές στη μηχανική μάθηση και συμπίεση δεδομένων.

- **Κωδικός Μαθήματος:** 102 (ΓΡΑΜΜΙΚΗ ΑΛΓΕΒΡΑ)
- **Προαπαιτούμενα:** Κανένα
- **Εξάμηνο:** 1ο

---

## Δομή Καταλόγου

* **[Assignments/](Assignments/)**:
  - [`assignment_01_matrix_transformations.md`](Assignments/assignment_01_matrix_transformations.md): Εργασία γραμμικών μετασχηματισμών και πινάκων.
  - [`exercises.md`](Assignments/exercises.md): Βασικές ασκήσεις μαθήματος.
* **[Examples/](Examples/)**:
  - [`Matlab_Octave_Code/`](Examples/Matlab_Octave_Code/): 12 πλήρεις υλοποιήσεις αλγορίθμων σε MATLAB/GNU Octave (`01_vectors_and_matrices.m` έως `12_ml_normal_equation.m`).
* **[Exams/](Exams/)**:
  - [`practice_exam_01.md`](Exams/practice_exam_01.md): Πλήρες επαναληπτικό διαγώνισμα προσομοίωσης με αναλυτικές λύσεις.
* **[Exercises/](Exercises/)**:
  - [`exercises_matrix_operations_and_inverses.md`](Exercises/exercises_matrix_operations_and_inverses.md): Πράξεις πινάκων, αντιστροφή και ορίζουσες.
  - [`exercises_eigenvalues_and_quadratic_forms.md`](Exercises/exercises_eigenvalues_and_quadratic_forms.md): Ιδιοτιμές, διαγωνιοποίηση και τετραγωνικές μορφές.
* **[Lectures/](Lectures/)**:
  - [`lecture_01_linear_systems_and_matrices.md`](Lectures/lecture_01_linear_systems_and_matrices.md): Γραμμικά συστήματα και πίνακες.
  - [`lecture_02_vector_spaces_and_subspaces.md`](Lectures/lecture_02_vector_spaces_and_subspaces.md): Διανυσματικοί χώροι και υπόχωροι.
  - [`lecture_03_linear_transformations_and_orthogonality.md`](Lectures/lecture_03_linear_transformations_and_orthogonality.md): Γραμμικοί μετασχηματισμοί και ορθογωνιότητα.
  - [`lecture_04_eigenvalues_and_diagonalization.md`](Lectures/lecture_04_eigenvalues_and_diagonalization.md): Ιδιοτιμές και διαγωνιοποίηση.
* **[Projects/](Projects/)**:
  - [`project_01_image_compression_and_pagerank.md`](Projects/project_01_image_compression_and_pagerank.md): Εξαμηνιαίο project συμπίεσης εικόνας (SVD) και κατάταξης σελίδων (PageRank) σε Octave/Python.
* **[Resources/](Resources/)**:
  - [`resources.md`](Resources/resources.md): Προτεινόμενη βιβλιογραφία και πηγές.
  - [`Linear_Algebra_and_its_application.pdf`](Resources/Books/Linear_Algebra_and_its_application.pdf): Το κλασικό σύγγραμμα του Gilbert Strang.
  - [`Meta/mindmap.md`](Resources/Meta/mindmap.md): Αναλυτικός εννοιολογικός χάρτης μαθήματος (12 ενότητες).
  - [`Notes/`](Resources/Notes/): 11 αναλυτικές σημειώσεις θεωρίας με 80+ λυμένες ασκήσεις (`01_vectors_and_spaces.md` έως `11_applications.md`).
* **[Tutorials/](Tutorials/)**:
  - [`tutorial_01_octave_matrix_computations.md`](Tutorials/tutorial_01_octave_matrix_computations.md): Υπολογισμοί πινάκων στο GNU Octave.
  - [`tutorial_02_solving_systems_and_eigenvalues_octave.md`](Tutorials/tutorial_02_solving_systems_and_eigenvalues_octave.md): Επίλυση συστημάτων και εύρεση ιδιοτιμών στο Octave.

---

## Εκτέλεση Σεναρίων Octave

Για να εκτελέσετε τα σενάρια υπολογισμών στον κατάλογο `Examples/Matlab_Octave_Code/`:

```octave
% Εκκινήστε το GNU Octave και μεταβείτε στον φάκελο:
cd Examples/Matlab_Octave_Code

% Εκτελέστε οποιοδήποτε σενάριο με την εντολή run:
run("01_vectors_and_matrices.m")
run("12_ml_normal_equation.m")
```
