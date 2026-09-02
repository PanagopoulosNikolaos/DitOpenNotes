# Αρχιτεκτονική Υπολογιστών (Course 301)

## Επισκόπηση Μαθήματος
Το μάθημα καλύπτει τις θεμελιώδεις αρχές οργάνωσης και αρχιτεκτονικής σύγχρονων υπολογιστικών συστημάτων:
- Αρχιτεκτονική Συνόλου Εντολών (ISA), συμβολική γλώσσα MIPS και κωδικοποίηση εντολών (R, I, J formats).
- Σχεδίαση μονοκύκλου και πολυκύκλου επεξεργαστή, μονοπάτι δεδομένων (datapath) και μονάδα ελέγχου (control unit).
- Διασωλήνωση (pipelining 5 σταδίων: IF, ID, EX, MEM, WB), ανίχνευση και επίλυση κινδύνων (Hazards: RAW, WAR, WAW, Branch hazards) και μηχανισμοί προώθησης (Forwarding).
- Ιεραρχία μνήμης, κρυφή μνήμη (L1/L2 Cache), τεχνικές χαρτογράφησης (Direct, Set-Associative, Fully Associative), πρωτόκολλα εγγραφής (Write-Through, Write-Back) και AMAT.
- Εικονική μνήμη (Virtual Memory), σελιδοποίηση, πίνακες σελίδων και επιτάχυνση μετάφρασης με TLB.
- Παραλληλισμός επιπέδου εντολών (ILP), υπερβαθμωτοί επεξεργαστές (Superscalar), εκτέλεση εκτός σειράς (Out-of-Order) και πρόβλεψη διακλαδώσεων.
- Πολυπύρηνοι επεξεργαστές, συνοχή κρυφής μνήμης (Πρωτόκολλο MESI) και μοντέλα συνέπειας μνήμης.
- Συστήματα εισόδου/εξόδου (I/O), διακοπές (Interrupts), άμεση πρόσβαση στη μνήμη (DMA) και σύγχρονοι δίαυλοι (PCIe).

- **Κωδικός Μαθήματος:** 301 (ΑΡΧΙΤΕΚΤΟΝΙΚΗ ΥΠΟΛΟΓΙΣΤΩΝ)
- **Προαπαιτούμενα:** Ψηφιακά Ηλεκτρονικά (105/205), Σχεδίαση Λογικής (104)
- **Εξάμηνο:** 3ο

---

## Δομή Καταλόγου

* **[Assignments/](Assignments/)**: Επίσημες εργασίες εξαμήνου και ολοκληρωμένες λύσεις:
  - [`assignment_01.pdf`](Assignments/assignment_01.pdf): Εκφώνηση Εργασίας 1 (Μικροελεγκτής Arduino).
  - [`assignment_02.pdf`](Assignments/assignment_02.pdf): Εκφώνηση Εργασίας 2 (MIPS Assembly Calculator).
  - [`assignment_03.pdf`](Assignments/assignment_03.pdf): Εκφώνηση Εργασίας 3 (Ανάλυση Cache & Pipelining).
  - [`assignment_04_pipeline_and_cache_design.md`](Assignments/assignment_04_pipeline_and_cache_design.md): Εκφώνηση Εργασίας 4.
  - [`assignment_04_pipeline_and_cache_design_solution.md`](Assignments/assignment_04_pipeline_and_cache_design_solution.md): Πλήρης αναλυτική λύση της Εργασίας 4.
  - [`Complete_Exercise_1/`](Assignments/Complete_Exercise_1/): Ολοκληρωμένη υλοποίηση έξυπνου συστήματος Arduino (`code.ino`, τεχνική αναφορά).
  - [`Complete_Exercise_2/`](Assignments/Complete_Exercise_2/): Πλήρης αριθμομηχανή MIPS Assembly (`calculator_spec.asm`, σενάριο ελέγχων).
  - [`Complete_Exercise_3/`](Assignments/Complete_Exercise_3/): Τεχνική έκθεση μελέτης ιεραρχίας μνήμης.
* **[Examples/](Examples/)**: Πρακτικά παραδείγματα κώδικα και προσομοιώσεων:
  - [`examples_mips_assembly_routines.md`](Examples/examples_mips_assembly_routines.md): Συναρτήσεις MIPS και διαχείριση στοίβας (stack frame).
  - [`examples_cache_address_breakdown.md`](Examples/examples_cache_address_breakdown.md): Υπολογισμοί κατανομής bits (Tag, Index, Offset) σε άμεση και συσχετιστική cache.
  - [`Arduino/`](Examples/Arduino/): 4 ολοκληρωμένα προγράμματα Arduino (LED, σειριακή επικοινωνία, αισθητήρας θερμοκρασίας, αισθητήρας υπερήχων).
* **[Exams/](Exams/)**:
  - [`practice_exam_01.md`](Exams/practice_exam_01.md): Πρότυπο επαναληπτικό διαγώνισμα προσομοίωσης με αναλυτικές λύσεις (MIPS, Hazards, Cache, AMAT).
* **[Exercises/](Exercises/)**: Λυμένες θεματικές ασκήσεις με βήμα-προς-βήμα υπολογισμούς:
  - [`exercises_mips_assembly_and_instruction_encoding.md`](Exercises/exercises_mips_assembly_and_instruction_encoding.md): Συμβολική γλώσσα MIPS και κωδικοποίηση δυαδικών εντολών.
  - [`exercises_pipelining_hazards_and_branch_prediction.md`](Exercises/exercises_pipelining_hazards_and_branch_prediction.md): Κίνδυνοι διασωλήνωσης, διαγράμματα χρονισμού και πρόβλεψη διακλαδώσεων.
  - [`exercises_cache_mapping_and_performance.md`](Exercises/exercises_cache_mapping_and_performance.md): Χαρτογράφηση cache, πολιτικές αντικατάστασης και επιδόσεις AMAT.
* **[Lectures/](Lectures/)**: Σημειώσεις διαλέξεων για ολόκληρο το εξάμηνο:
  - [`lecture_01_instruction_set_architecture_and_mips.md`](Lectures/lecture_01_instruction_set_architecture_and_mips.md): Αρχιτεκτονική συνόλου εντολών και MIPS ISA.
  - [`lecture_02_processor_datapath_and_control_unit.md`](Lectures/lecture_02_processor_datapath_and_control_unit.md): Μονοπάτι δεδομένων και μονάδα ελέγχου επεξεργαστή.
  - [`lecture_03_pipelining_and_hazards.md`](Lectures/lecture_03_pipelining_and_hazards.md): Διασωλήνωση, κίνδυνοι και τεχνικές forwarding.
  - [`lecture_04_memory_hierarchy_and_cache.md`](Lectures/lecture_04_memory_hierarchy_and_cache.md): Ιεραρχία μνήμης και σχεδίαση κρυφής μνήμης.
  - [`lecture_05_virtual_memory_and_tlb.md`](Lectures/lecture_05_virtual_memory_and_tlb.md): Εικονική μνήμη, σελιδοποίηση και επιτάχυνση TLB.
  - [`lecture_06_instruction_level_parallelism_and_superscalar.md`](Lectures/lecture_06_instruction_level_parallelism_and_superscalar.md): ILP, υπερβαθμωτοί επεξεργαστές και εκτέλεση εκτός σειράς.
  - [`lecture_07_multicore_processors_and_cache_coherence.md`](Lectures/lecture_07_multicore_processors_and_cache_coherence.md): Πολυπύρηνα συστήματα και πρωτόκολλα συνοχής MESI.
  - [`lecture_08_storage_io_and_system_buses.md`](Lectures/lecture_08_storage_io_and_system_buses.md): Αποθήκευση, μηχανισμοί I/O, DMA και δίαυλοι PCIe.
* **[Projects/](Projects/)**:
  - [`project_01_mips_single_cycle_datapath_simulator.md`](Projects/project_01_mips_single_cycle_datapath_simulator.md): Εξαμηνιαίο συνθετικό project ανάπτυξης προσομοιωτή MIPS datapath.
* **[Resources/](Resources/)**:
  - [`resources.md`](Resources/resources.md): Προτεινόμενα συγγράμματα (Patterson & Hennessy, Stallings, Harris & Harris).
  - [`Meta/mindmap_computer_architecture_overview.md`](Resources/Meta/mindmap_computer_architecture_overview.md): Εννοιολογικός χάρτης μαθήματος σε Mermaid.
  - [`Notes/`](Resources/Notes/): Εκτενείς σημειώσεις προχωρημένων κεφαλαίων (επεξεργαστές superscalar, παράλληλη επεξεργασία, πολυπύρηνα).
* **[Tutorials/](Tutorials/)**:
  - [`tutorial_01_assembly_programming_mips_mars.md`](Tutorials/tutorial_01_assembly_programming_mips_mars.md): Εργαστηριακός οδηγός προσομοιωτή MARS MIPS.
  - [`tutorial_02_cache_memory_and_pipeline_simulation.md`](Tutorials/tutorial_02_cache_memory_and_pipeline_simulation.md): Οδηγός προσομοίωσης cache και pipeline.
