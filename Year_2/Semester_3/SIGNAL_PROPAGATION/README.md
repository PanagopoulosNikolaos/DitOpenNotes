# Διάδοση Σημάτων (Course 304)

## Επισκόπηση Μαθήματος
Το μάθημα καλύπτει τις θεμελιώδεις αρχές της ηλεκτρομαγνητικής διάδοσης κυμάτων, τη θεωρία γραμμών μεταφοράς και κυματοδηγών, τη λειτουργία και σχεδίαση συστημάτων κεραιών, καθώς και τα μοντέλα ασύρματης διάδοσης σε πραγματικά τηλεπικοινωνιακά κανάλια:
- Θεμελιώδεις αρχές ηλεκτρομαγνητισμού: Εξισώσεις Maxwell, κυματική εξίσωση Helmholtz, κυματοδηγοί, επίπεδα κύματα, χαρακτηριστική εμπέδηση μέσου, ταχύτητα φάσης και πόλωση.
- Θεωρία Γραμμών Μεταφοράς: Εξισώσεις τηλεγραφητή, σταθερά διάδοσης $\gamma = \alpha + j\beta$, χαρακτηριστική εμπέδηση $Z_0$, συντελεστής ανάκλασης τάσης $\Gamma$, λόγος στασίμων κυμάτων (VSWR).
- Προσαρμογή σύνθετης αντίστασης: Χάρτης Smith (Smith Chart), μετασχηματιστές τετάρτου κύματος ($\lambda/4$) και προσαρμογή με μονό/διπλό προσαρμοστικό στέλεχος (stub matching).
- Θεμελιώδεις παράμετροι κεραιών: Διάγραμμα ακτινοβολίας, ένταση ακτινοβολίας, κατευθυντικότητα $D$, κέρδος $G$, ενεργός επιφάνεια $A_e$, αντίσταση ακτινοβολίας $R_r$, εύρος ζώνης (BW) και συντελεστής πόλωσης (PLF).
- Γραμμικές κεραίες σύρματος: Απειροελάχιστο δίπολο (Hertzian), δίπολο μισού κύματος ($\lambda/2$), κατακόρυφο μονόπολο ($\lambda/4$) και θεώρημα ειδώλων.
- Στοιχειοκεραίες (Antenna Arrays): Συντελεστής στοιχειοκεραίας ($AF$), ομοιόμορφες γραμμικές στοιχειοκεραίες (ULA), εγκάρσια (broadside) και επιμήκης (end-fire) ακτινοβολία, ηλεκτρονική διαμόρφωση δέσμης (phased arrays / beamforming).
- Κεραίες μικροκυμάτων: Κεραίες ανοίγματος (aperture), χοάνες (horn antennas) και μικροταινιακές κεραίες patch.
- Μηχανισμοί διάδοσης ραδιοκυμάτων: Εξίσωση Friis, απώλειες ελεύθερου χώρου (FSPL), προϋπολογισμός ζεύξης (Link Budget), ζώνες Fresnel, σκέδαση, ανάκλαση εδάφους και μοντέλα δύο ακτίνων.
- Πολυδιαδρομική διάδοση και διαλείψεις (Fading): Στατιστικά μοντέλα Rayleigh και Rician, διασπορά καθυστέρησης, εύρος ζώνης συνοχής, μετατόπιση Doppler και χρόνος συνοχής.

- **Κωδικός Μαθήματος:** 304 (ΔΙΑΔΟΣΗ ΣΗΜΑΤΩΝ)
- **Προαπαιτούμενα:** Ηλεκτρομαγνητισμός / Φυσική (105), Μαθηματική Ανάλυση (101)
- **Εξάμηνο:** 3ο

---

## Δομή Καταλόγου

* **[Assignments/](Assignments/)**: Επίσημες εργασίες εξαμήνου:
  - [`assignment_01_transmission_lines_and_reflection.md`](Assignments/assignment_01_transmission_lines_and_reflection.md): Εργασία 1 — Γραμμές μεταφοράς, υπολογισμοί ανάκλασης και VSWR.
  - [`assignment_02_antenna_arrays_and_path_loss.md`](Assignments/assignment_02_antenna_arrays_and_path_loss.md): Εργασία 2 — Στοιχειοκεραίες, εξίσωση Friis και προϋπολογισμός ζεύξης.
* **[Examples/](Examples/)**: Πρακτικά παραδείγματα υπολογισμών:
  - [`examples_quarter_wave_transformer_matching.md`](Examples/examples_quarter_wave_transformer_matching.md): Προσαρμογή εμπέδησης διπόλου $73 \, \Omega$ με μετασχηματιστή $\lambda/4$.
  - [`examples_friis_transmission_and_path_loss.md`](Examples/examples_friis_transmission_and_path_loss.md): Υπολογισμός λαμβανόμενης ισχύος και απωλειών διαδρομής Friis.
* **[Exams/](Exams/)**:
  - [`practice_exam_01.md`](Exams/practice_exam_01.md): Πρότυπο επαναληπτικό διαγώνισμα προσομοίωσης με λύσεις (Smith Chart, Friis, Δίπολο, ULA).
* **[Exercises/](Exercises/)**: Λυμένες θεματικές ασκήσεις με πλήρη μαθηματική τεκμηρίωση:
  - [`exercises_transmission_lines_and_standing_waves.md`](Exercises/exercises_transmission_lines_and_standing_waves.md): Γραμμές μεταφοράς, στάσιμα κύματα και προσαρμογή stub.
  - [`exercises_antenna_radiation_patterns_and_gain.md`](Exercises/exercises_antenna_radiation_patterns_and_gain.md): Διαγράμματα ακτινοβολίας, απολαβή και κατευθυντικότητα.
  - [`exercises_free_space_path_loss_and_link_budget.md`](Exercises/exercises_free_space_path_loss_and_link_budget.md): Απώλειες ελεύθερου χώρου και σχεδιασμός ασύρματων ζεύξεων.
* **[Lectures/](Lectures/)**: Σημειώσεις διαλέξεων για ολόκληρο το εξάμηνο:
  - [`lecture_01_electromagnetic_wave_propagation_fundamentals.md`](Lectures/lecture_01_electromagnetic_wave_propagation_fundamentals.md): Ηλεκτρομαγνητικά κύματα και εξισώσεις Maxwell.
  - [`lecture_02_transmission_lines_and_impedance_matching.md`](Lectures/lecture_02_transmission_lines_and_impedance_matching.md): Γραμμές μεταφοράς και προσαρμογή εμπέδησης.
  - [`lecture_03_antenna_parameters_and_radiation_mechanisms.md`](Lectures/lecture_03_antenna_parameters_and_radiation_mechanisms.md): Θεμελιώδεις παράμετροι κεραιών.
  - [`lecture_04_radio_wave_propagation_mechanisms_and_link_budget.md`](Lectures/lecture_04_radio_wave_propagation_mechanisms_and_link_budget.md): Μηχανισμοί ραδιοδιάδοσης και Link Budget.
  - [`lecture_05_wire_antennas_dipoles_and_monopoles.md`](Lectures/lecture_05_wire_antennas_dipoles_and_monopoles.md): Γραμμικές κεραίες σύρματος, δίπολα και μονόπολα.
  - [`lecture_06_antenna_arrays_and_beamforming.md`](Lectures/lecture_06_antenna_arrays_and_beamforming.md): Στοιχειοκεραίες και ηλεκτρονική διαμόρφωση δέσμης.
  - [`lecture_07_aperture_microstrip_and_horn_antennas.md`](Lectures/lecture_07_aperture_microstrip_and_horn_antennas.md): Κεραίες ανοίγματος, χοάνες και μικροταινιακά patches.
  - [`lecture_08_multipath_propagation_and_fading_channels.md`](Lectures/lecture_08_multipath_propagation_and_fading_channels.md): Πολυδιαδρομική διάδοση και διαλείψεις Rayleigh/Rician.
* **[Projects/](Projects/)**:
  - [`project_01_wireless_link_budget_calculator_and_coverage_planner.md`](Projects/project_01_wireless_link_budget_calculator_and_coverage_planner.md): Εξαμηνιαίο συνθετικό project ανάπτυξης λογισμικού υπολογισμού Link Budget και σχεδιασμού κάλυψης.
* **[Resources/](Resources/)**:
  - [`resources.md`](Resources/resources.md): Προτεινόμενη βιβλιογραφία (Balanis, Pozar, Rappaport).
  - [`Books/Antenna Theory Analysis and Design 3rd ed.pdf`](Resources/Books/Antenna%20Theory%20Analysis%20and%20Design%203rd%20ed.pdf): Κλασικό σύγγραμμα C. A. Balanis.
  - [`Meta/mindmap_signal_propagation.md`](Resources/Meta/mindmap_signal_propagation.md): Εννοιολογικός χάρτης μαθήματος σε Mermaid.
  - [`Notes/`](Resources/Notes/): 17 πλήρεις μονογραφίες θεωρίας κεραιών (`section_01_antennas.md` έως `section_17_antenna_measurements.md`).
* **[Tutorials/](Tutorials/)**:
  - [`tutorial_01_smith_chart_and_impedance_matching.md`](Tutorials/tutorial_01_smith_chart_and_impedance_matching.md): Εργαστηριακός οδηγός επίλυσης προβλημάτων γραμμών με Smith Chart.
  - [`tutorial_02_link_budget_calculation_and_friis_formula.md`](Tutorials/tutorial_02_link_budget_calculation_and_friis_formula.md): Οδηγός υπολογισμού προϋπολογισμού ζεύξης και εξίσωσης Friis.