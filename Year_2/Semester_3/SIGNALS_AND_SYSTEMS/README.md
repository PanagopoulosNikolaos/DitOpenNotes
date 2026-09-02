# Σήματα και Συστήματα (Course 303)

## Επισκόπηση Μαθήματος
Το μάθημα καλύπτει τη μαθηματική μοντελοποίηση, ανάλυση και επεξεργασία σημάτων συνεχούς και διακριτού χρόνου, καθώς και τη θεωρία γραμμικών και χρονικά αμετάβλητων συστημάτων (LTI):
- Ταξινόμηση σημάτων (Συνεχούς/Διακριτού χρόνου, Αναλογικά/Ψηφιακά, Περιοδικά/Μη περιοδικά, Ενέργειας/Ισχύος, Άρτια/Περιττά).
- Βασικά σήματα: Μοναδιαία κρουστική συνάρτηση ($\delta$), μοναδιαία βηματική συνάρτηση ($u$), μιγαδικά εκθετικά και ημιτονοειδή σήματα.
- Ιδιότητες συστημάτων: Γραμμικότητα, Χρονική Αμεταβλητότητα, Αιτιατότητα, Ευστάθεια BIBO, Μνήμη και Αντιστρεψιμότητα.
- Συστήματα LTI: Κρουστική απόκριση $h(t)$ / $h[n]$, Ολοκλήρωμα και Άθροισμα Συνέλιξης, ιδιότητες συνέλιξης και σύνδεση συστημάτων (σε σειρά / παράλληλα).
- Ανάλυση στο πεδίο των συχνοτήτων: Σειρές Fourier Συνεχούς και Διακριτού Χρόνου (CTFS, DTFS), Μετασχηματισμός Fourier Συνεχούς Χρόνου (CTFT) και Διακριτού Χρόνου (DTFT).
- Μετασχηματισμός Laplace (Μονόπλευρος και Αμφίπλευρος), Περιοχή Σύγκλισης (ROC), πόλοι/μηδενικά και απόκριση συστημάτων.
- Μετασχηματισμός Z, Περιοχή Σύγκλισης (ROC), εξισώσεις διαφορών και ευστάθεια ψηφιακών φίλτρων.
- Θεώρημα Δειγματοληψίας Nyquist-Shannon, φαινόμενο ψευδωνυμίας (aliasing), φίλτρα καταπολέμησης και ιδανική ανακατασκευή sinc.
- Σχεδίαση φίλτρων (Butterworth, Chebyshev) και λογαριθμικά διαγράμματα Bode.

- **Κωδικός Μαθήματος:** 303 (ΣΗΜΑΤΑ ΚΑΙ ΣΥΣΤΗΜΑΤΑ)
- **Προαπαιτούμενα:** Μαθηματική Ανάλυση (101), Γραμμική Άλγεβρα (102)
- **Εξάμηνο:** 3ο

---

## Δομή Καταλόγου

* **[Assignments/](Assignments/)**: Επίσημες εργασίες εξαμήνου:
  - [`assignment_01_continuous_time_signals_and_lti_systems.md`](Assignments/assignment_01_continuous_time_signals_and_lti_systems.md): Εργασία 1 — Συνεχή σήματα, ενέργεια/ισχύς και ιδιότητες συστημάτων LTI.
  - [`assignment_02_convolution_and_fourier_transforms.md`](Assignments/assignment_02_convolution_and_fourier_transforms.md): Εργασία 2 — Συνέλιξη, μετασχηματισμοί Fourier και Laplace.
* **[Examples/](Examples/)**: Διαδραστικά εργαλεία και αναλυτικά παραδείγματα:
  - [`01_InteractiveLearning.html`](Examples/01_InteractiveLearning.html): Διαδραστικός προσομοιωτής σημάτων και πράξεων μετασχηματισμού.
  - [`02_InteractiveLearning.html`](Examples/02_InteractiveLearning.html): Προσομοιωτής συστημάτων LTI.
  - [`03_InteractiveLearning.html`](Examples/03_InteractiveLearning.html): Οπτικοποίηση ολοκληρώματος συνέλιξης σε πραγματικό χρόνο.
  - [`04_InteractiveLearning.html`](Examples/04_InteractiveLearning.html): Διαδραστική σύνθεση σειρών Fourier.
  - [`05_InteractiveLearning.html`](Examples/05_InteractiveLearning.html): Προσομοιωτής δειγματοληψίας και φαινομένου aliasing.
  - [`examples_convolution_step_by_step.md`](Examples/examples_convolution_step_by_step.md): Βήμα-προς-βήμα υπολογισμός συνέλιξης ορθογώνιων παλμών.
  - [`examples_fourier_series_and_spectrum.md`](Examples/examples_fourier_series_and_spectrum.md): Ανάλυση φάσματος τετραγωνικού παλμού.
* **[Exams/](Exams/)**:
  - [`practice_exam_01.md`](Exams/practice_exam_01.md): Πρότυπο επαναληπτικό διαγώνισμα προσομοίωσης με λύσεις (Συνέλιξη, LTI, Laplace, Ευστάθεια).
* **[Exercises/](Exercises/)**: Λυμένες θεματικές ασκήσεις:
  - [`exercises_signal_classification_and_transformations.md`](Exercises/exercises_signal_classification_and_transformations.md): Ταξινόμηση σημάτων, χρονική ολίσθηση/κλιμάκωση και ενέργεια.
  - [`exercises_lti_systems_and_convolution.md`](Exercises/exercises_lti_systems_and_convolution.md): Ιδιότητες LTI, γραμμικότητα, χρονική αμεταβλητότητα και συνέλιξη.
  - [`exercises_fourier_laplace_z_transforms.md`](Exercises/exercises_fourier_laplace_z_transforms.md): Υπολογισμοί μετασχηματισμών Fourier, Laplace και Z.
* **[Lectures/](Lectures/)**: Σημειώσεις διαλέξεων για ολόκληρο το εξάμηνο και επίσημες διαφάνειες:
  - [`lecture_01_introduction_and_signal_classification.md`](Lectures/lecture_01_introduction_and_signal_classification.md): Εισαγωγή και ταξινόμηση σημάτων.
  - [`lecture_02_continuous_and_discrete_time_signals.md`](Lectures/lecture_02_continuous_and_discrete_time_signals.md): Σήματα συνεχούς και διακριτού χρόνου.
  - [`lecture_03_lti_systems_and_convolution.md`](Lectures/lecture_03_lti_systems_and_convolution.md): Συστήματα LTI και συνέλιξη.
  - [`lecture_04_fourier_analysis_and_laplace_transform.md`](Lectures/lecture_04_fourier_analysis_and_laplace_transform.md): Ανάλυση Fourier και μετασχηματισμός Laplace.
  - [`lecture_05_fourier_series_and_frequency_response.md`](Lectures/lecture_05_fourier_series_and_frequency_response.md): Σειρές Fourier και απόκριση συχνότητας LTI.
  - [`lecture_06_z_transform_and_discrete_lti_systems.md`](Lectures/lecture_06_z_transform_and_discrete_lti_systems.md): Μετασχηματισμός Z και διακριτά συστήματα.
  - [`lecture_07_sampling_theorem_and_aliasing.md`](Lectures/lecture_07_sampling_theorem_and_aliasing.md): Θεώρημα δειγματοληψίας και aliasing.
  - [`lecture_08_filter_design_and_bode_plots.md`](Lectures/lecture_08_filter_design_and_bode_plots.md): Σχεδίαση φίλτρων και διαγράμματα Bode.
* **[Projects/](Projects/)**:
  - [`project_01_audio_signal_filtering_and_spectral_analysis.md`](Projects/project_01_audio_signal_filtering_and_spectral_analysis.md): Εξαμηνιαίο συνθετικό project επεξεργασίας και φιλτραρίσματος ηχητικών σημάτων σε Python.
* **[Resources/](Resources/)**:
  - [`resources.md`](Resources/resources.md): Προτεινόμενη βιβλιογραφία (Oppenheim & Willsky, Lathi, Haykin & Van Veen, Downey).
  - [`Books/`](Resources/Books/): Ακαδημαϊκά συγγράμματα (Think DSP, Vural).
  - [`Meta/mindmap_signals_and_systems.md`](Resources/Meta/mindmap_signals_and_systems.md): Εννοιολογικός χάρτης μαθήματος σε Mermaid.
  - [`Notes/`](Resources/Notes/): Εκτενείς σημειώσεις διαλέξεων 01-06 (Εισαγωγή, Σήματα, Συστήματα, LTI, Συνέλιξη).
* **[Tutorials/](Tutorials/)**:
  - [`tutorial_01_signal_operations_and_convolution_python.md`](Tutorials/tutorial_01_signal_operations_and_convolution_python.md): Εργαστηριακός οδηγός πράξεων σημάτων και συνέλιξης σε Python/NumPy.
  - [`tutorial_02_frequency_response_and_bode_plots_scipy.md`](Tutorials/tutorial_02_frequency_response_and_bode_plots_scipy.md): Οδηγός απόκρισης συχνότητας και Bode plots με SciPy.
