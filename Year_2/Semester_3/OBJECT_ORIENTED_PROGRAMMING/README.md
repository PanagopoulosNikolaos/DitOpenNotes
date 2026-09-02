# Αντικειμενοστραφής Προγραμματισμός (Course 302)

## Επισκόπηση Μαθήματος
Το μάθημα εισάγει τις θεμελιώδεις και προχωρημένες αρχές του Αντικειμενοστραφούς Προγραμματισμού (Object-Oriented Programming - OOP) με χρήση της σύγχρονης C++ (C++17/C++20):
- Κλάσεις και αντικείμενα, ενθυλάκωση (encapsulation), απόκρυψη πληροφορίας και τροποποιητές πρόσβασης (`private`, `protected`, `public`).
- Κύκλος ζωής αντικειμένων: Προκαθορισμένοι, παραμετρικοί και κατασκευαστές αντιγραφής/μετακίνησης, καταστροφείς και ο Κανόνας των Πέντε (Rule of Five).
- Κληρονομικότητα (μονή, πολλαπλή, εικονική), πολυμορφισμός χρόνου εκτέλεσης (runtime polymorphism), εικονικές συναρτήσεις (`virtual`), πίνακες vtable και καθαρά εικονικές συναρτήσεις (αφηρημένες κλάσεις / interfaces).
- Διαχείριση πόρων και ιδίωμα RAII (Resource Acquisition Is Initialization), έξυπνοι δείκτες (`std::unique_ptr`, `std::shared_ptr`, `std::weak_ptr`).
- Υπερφόρτωση τελεστών (αριθμητικοί, τελεστές ροής `<<` και `>>`, τελεστής δεικτοδότησης `[]`, functors `()`).
- Γενικός προγραμματισμός (Generic Programming), πρότυπα συναρτήσεων και κλάσεων (Templates) και Standard Template Library (STL containers, iterators, algorithms).
- Διαχείριση εξαιρέσεων (Exception Handling, `try-catch-throw`, ασφάλεια εξαιρέσεων).
- Αρχές αντικειμενοστραφούς σχεδίασης (SOLID) και σχεδιαστικά πρότυπα GoF (Singleton, Factory, Adapter, Decorator, Observer, Strategy).

- **Κωδικός Μαθήματος:** 302 (ΑΝΤΙΚΕΙΜΕΝΟΣΤΡΑΦΗΣ ΠΡΟΓΡΑΜΜΑΤΙΣΜΟΣ)
- **Προαπαιτούμενα:** Προγραμματισμός σε C II (204)
- **Εξάμηνο:** 3ο

---

## Δομή Καταλόγου

* **[Assignments/](Assignments/)**: Πρακτικές σειρές ασκήσεων και προγραμματιστικά projects:
  - [`Basics/`](Assignments/Basics/): 60 διαβαθμισμένες ασκήσεις εξάσκησης σε C++ (`001_exercise.cpp` έως `060_exercise_general.cpp`) έτοιμες για επίλυση από τους φοιτητές.
  - [`Exercise_1/`](Assignments/Exercise_1/): Εξαμηνιαίο Project μαθήματος (Επίλυση προβλήματος Job Shop Scheduling - JSSP).
* **[Examples/](Examples/)**: Πλήρως λειτουργικά και μεταγλωττίσιμα προγράμματα επίδειξης:
  - [`examples_modern_cpp_smart_pointers.md`](Examples/examples_modern_cpp_smart_pointers.md): Ολοκληρωμένα παραδείγματα `unique_ptr`, `shared_ptr`, `weak_ptr` και custom deleters.
  - [`examples_polymorphism_and_abstract_classes.md`](Examples/examples_polymorphism_and_abstract_classes.md): Σύστημα ηλεκτρονικών πληρωμών με πολυμορφισμό (`CreditCard`, `PayPal`, `CryptoPayment`).
* **[Exams/](Exams/)**:
  - [`practice_exam_01.md`](Exams/practice_exam_01.md): Πρότυπο επαναληπτικό διαγώνισμα προσομοίωσης με πλήρεις λύσεις (Rule of 5, vtable, STL, SOLID).
* **[Exercises/](Exercises/)**: Λυμένες θεματικές ασκήσεις με αναλυτική εξήγηση:
  - [`exercises_classes_inheritance_and_polymorphism.md`](Exercises/exercises_classes_inheritance_and_polymorphism.md): Ιεραρχίες κλάσεων, εικονικοί καταστροφείς και dynamic casting.
  - [`exercises_templates_and_stl_containers.md`](Exercises/exercises_templates_and_stl_containers.md): Πρότυπα κλάσεων και επεξεργασία συλλογών με αλγορίθμους STL.
  - [`exercises_design_patterns_in_cpp.md`](Exercises/exercises_design_patterns_in_cpp.md): Εφαρμογή σχεδιαστικών προτύπων Factory, Observer και Strategy.
* **[Lectures/](Lectures/)**: Σημειώσεις διαλέξεων για ολόκληρο το εξάμηνο:
  - [`lecture_01_classes_objects_and_encapsulation.md`](Lectures/lecture_01_classes_objects_and_encapsulation.md): Κλάσεις, αντικείμενα και ενθυλάκωση.
  - [`lecture_02_constructors_destructors_and_memory_management.md`](Lectures/lecture_02_constructors_destructors_and_memory_management.md): Κατασκευαστές, καταστροφείς και διαχείριση μνήμης.
  - [`lecture_03_inheritance_polymorphism_and_virtual_functions.md`](Lectures/lecture_03_inheritance_polymorphism_and_virtual_functions.md): Κληρονομικότητα, πολυμορφισμός και εικονικές συναρτήσεις.
  - [`lecture_04_templates_stl_and_exception_handling.md`](Lectures/lecture_04_templates_stl_and_exception_handling.md): Πρότυπα (Templates), STL και διαχείριση εξαιρέσεων.
  - [`lecture_05_move_semantics_and_smart_pointers.md`](Lectures/lecture_05_move_semantics_and_smart_pointers.md): Σημασιολογία μετακίνησης, rvalue references και έξυπνοι δείκτες.
  - [`lecture_06_operator_overloading_and_streams.md`](Lectures/lecture_06_operator_overloading_and_streams.md): Υπερφόρτωση τελεστών και ροές εισόδου/εξόδου (`<<`, `>>`).
  - [`lecture_07_object_oriented_design_principles_and_solid.md`](Lectures/lecture_07_object_oriented_design_principles_and_solid.md): Αρχές σχεδίασης λογισμικού και αρχές SOLID.
  - [`lecture_08_design_patterns_in_cpp.md`](Lectures/lecture_08_design_patterns_in_cpp.md): Σχεδιαστικά πρότυπα GoF (Singleton, Factory, Observer, Strategy).
* **[Projects/](Projects/)**:
  - [`project_01_banking_system_oop_cpp.md`](Projects/project_01_banking_system_oop_cpp.md): Εξαμηνιαίο συνθετικό project ανάπτυξης τραπεζικού συστήματος με αρχές SOLID και GoF patterns.
* **[Resources/](Resources/)**:
  - [`resources.md`](Resources/resources.md): Προτεινόμενη βιβλιογραφία (Deitel, Stroustrup, Gamma et al., Meyers).
  - [`Books/`](Resources/Books/): Ακαδημαϊκά συγγράμματα και οδηγοί C++.
  - [`Meta/mindmap_oop_cpp_overview.md`](Resources/Meta/mindmap_oop_cpp_overview.md): Εννοιολογικός χάρτης αντικειμενοστραφούς σχεδίασης σε Mermaid.
  - [`Notes/CPP_OOP_Theory_Guide.md`](Resources/Notes/CPP_OOP_Theory_Guide.md): Πλήρης θεωρητικός οδηγός C++ και OOP (114 KB).
  - [`Notes/notes_cpp_memory_management_and_raii.md`](Resources/Notes/notes_cpp_memory_management_and_raii.md): Μονογραφία διαχείρισης μνήμης και RAII.
  - [`Notes/notes_oop_principles_and_design_patterns.md`](Resources/Notes/notes_oop_principles_and_design_patterns.md): Μονογραφία αρχών σχεδίασης.
* **[Tutorials/](Tutorials/)**:
  - [`tutorial_01_raii_and_smart_pointers_in_modern_cpp.md`](Tutorials/tutorial_01_raii_and_smart_pointers_in_modern_cpp.md): Εργαστηριακός οδηγός RAII και έξυπνων δεικτών.
  - [`tutorial_02_operator_overloading_and_copy_control.md`](Tutorials/tutorial_02_operator_overloading_and_copy_control.md): Εργαστηριακός οδηγός ελέγχου αντιγραφής και υπερφόρτωσης τελεστών.