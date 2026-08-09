# Πολυπαραδειγματικό Πρόγραμμα Σπουδών Επιστήμης Υπολογιστών (Mindmap)

* **Python**
  * Βασικές Έννοιες (Basics)
    * Μεταβλητές, βρόχοι (loops), συναρτήσεις
    * Δυναμική τυποποίηση (dynamic typing) & αριθμητικές εκφράσεις
    * Δυναμικά τυποποιημένο μοντέλο μνήμης (αντικείμενα δεσμευμένα στο heap)
    * Ροή ελέγχου: βρόχοι `for` / `while`
    * Κόστος αξιολόγησης ενδιάμεσου κώδικα (bytecode evaluation costs)
  * Ενδιάμεσο Επίπεδο (Intermediate)
    * Λίστες (lists), λεξικά (dictionaries), σύνολα (sets)
    * `dict` → πίνακες κατακερματισμού δομών C (C-struct hash tables) → μέση χρονική επιπλοκή O(1) για εισαγωγή/αναζήτηση
    * Κατασκευές λιστών (list comprehensions - συμβολισμός κατασκευής συνόλων)
    * Διακοσμητές (decorators)
    * Παραδείγματα: τετράγωνα, άρτιοι, καρτεσιανά γινόμενα
  * Αντικειμενοστρεφής Προγραμματισμός (Object-Oriented Programming)
    * Κλάσεις, αντικείμενα, ιδιότητες στιγμιοτύπου (instance attributes), `self`
    * Ειδικές / dunder μέθοδοι (`__init__`, `__repr__`)
    * Κληρονομικότητα & `super()` / MRO (Method Resolution Order)
    * Θυλάκωση (Encapsulation): `_protected`, `__name_mangling`
    * Διακοσμητής `@property` (αφαιρετικότητα getter/setter)
    * Στατικά στοιχεία έναντι στοιχείων στιγμιοτύπου, μέθοδοι κλάσης (class methods)
    * Σύνθεση (composition) & αθροιση (aggregation) (Engine→Car, Book→Library)
    * Εκφράσεις γεννητριών σε άθροιση (`sum(book.price for book in self.books)`)
  * Προηγμένη Επανάληψη & Αποδοτικότητα Μνήμης (Advanced Iteration & Memory Efficiency)
    * Γεννήτριες (generators) & οκνηρή αξιολόγηση (lazy evaluation)
    * Μονάδα `itertools`
      * Άπειροι επαναλήπτες (Infinite Iterators): `count()`, `cycle()`, `repeat()`
      * Συνδυαστικοί επαναλήπτες (Combinatoric Iterators): `product()`, `permutations()`, `combinations()`
      * Επαναλήπτες τερματισμού (Terminating Iterators): `accumulate()`, `chain()`, `islice()`, `groupby()`
    * Μετατόπιση εκτέλεσης σε αυτόχθονες βρόχους C για υψηλή απόδοση

> [https://www.youtube.com/watch?v=ZDa-Z5JzLYM](https://www.youtube.com/watch?v=ZDa-Z5JzLYM)
> [https://www.youtube.com/watch?v=iLRZi0Gu8Go](https://www.youtube.com/watch?v=iLRZi0Gu8Go)
> [https://www.youtube.com/watch?v=q7gAio9OMLk](https://www.youtube.com/watch?v=q7gAio9OMLk)
> [https://www.youtube.com/watch?v=1p7xa_BHYDs](https://www.youtube.com/watch?v=1p7xa_BHYDs)
> [https://www.youtube.com/watch?v=p8FUoSIyIVY](https://www.youtube.com/watch?v=p8FUoSIyIVY)
> [https://www.youtube.com/watch?v=-duO0tuAfus](https://www.youtube.com/watch?v=-duO0tuAfus)

---

* **C++**
  * Βασικές Έννοιες & Σημασιολογία Υλικού (Basics & Hardware Semantics)
    * Κλήση κατ' τιμήν (pass-by-value: αντιγραφή → κόστος σε στοιβα/heap)
    * Κλήση κατά αναφορά (pass-by-reference: `&` → ψευδώνυμο μηδενικής αντιγραφής)
    * Κλήση μέσω δείκτη (pass-by-pointer: `*` → έμμεση προσπέλαση / explicit dereference)
    * Αναφορές `const` για ανάγνωση μεγάλων αντικειμένων χωρίς αντιγραφή
    * Παράδειγμα: `void update(int &x, int y)`
  * Διάταξη Μνήμης & Βελτιστοποίηση (Memory Layout & Optimization)
    * Πολυδιάστατοι πίνακες → 1D συνεχόμενη μνήμη
    * Διάταξη κατά γραμμές (Row-major order - C++, Java, Python): offset = `i × C + j`
    * Διάταξη κατά στήλες (Column-major order - Fortran, MATLAB, GLSL): offset = `j × R + i`
    * Χωρική εντοπιότητα (spatial locality) & κρυφή μνήμη CPU (L1/L2 cache)
    * Ποινή αποτυχίας κρυφής μνήμης (cache miss penalty) κατά την προσπέλαση κατά στήλες στη C++
    * Βελτιστοποίηση GEMM / υπολογιστικών πυρήνων
  * Αντικειμενοστρεφής Προγραμματισμός & Διαχείριση Πόρων (OOP & Resource Management)
    * Κατασκευαστές (constructors): προεπιλεγμένοι, με παραμέτρους, αντιγραφής
    * Καταστροφείς (destructors - `~ClassName()`)
    * RAII (Resource Acquisition Is Initialization): κύκλος ζωής πόρου συνδεδεμένος με την εμβέλεια του αντικειμένου
    * Κανόνας των Τριών / Κανόνας των Πέντε (Rule of Three / Rule of Five)
    * Δυναμική μνήμη: `new` / `delete`
    * Έξυπνοι δείκτες (smart pointers - περιβλήματα RAII)
    * Υπερφόρτωση τελεστών (operator overloading)
  * Πρότυπη Βιβλιοθήκη (Standard Template Library - STL)
    * `std::vector` → δυναμικοί πίνακες, `push_back()`, `pop_back()`
    * Επαναλήπτες (iterators): `begin()` / `end()` (αφαιρετικότητα αριθμητικής δεικτών)
    * `std::unordered_map` → πίνακας κατακερματισμού, O(1) εισαγωγή/αναζήτηση
    * `<algorithm>`: `count()`, `count_if()`, εκφράσεις lambda
    * Πρωτογενείς εντολές ταξινόμησης, μετασχηματισμού και αναζήτησης

> [https://archive.codewithharry.com/videos/cpp-tutorials-in-hindi-71](https://archive.codewithharry.com/videos/cpp-tutorials-in-hindi-71)
> [https://www.youtube.com/watch?v=qJHWeSAPHsw](https://www.youtube.com/watch?v=qJHWeSAPHsw)
> [https://www.youtube.com/watch?v=b5lYGvcBjy4](https://www.youtube.com/watch?v=b5lYGvcBjy4)
> [https://www.youtube.com/watch?v=J3T-8N9QK2A](https://www.youtube.com/watch?v=J3T-8N9QK2A)
> [https://www.youtube.com/watch?v=CHl6uxoiJPA](https://www.youtube.com/watch?v=CHl6uxoiJPA)

---
* **C**
* **Βασικές Έννοιες & Εγγύτητα στο Υλικό (Basics & Hardware Proximity)**
  * Διαδικαστικό παράδειγμα (procedural paradigm): διαχωρισμός συναρτήσεων και δεδομένων
  * Μεταβλητές, εμβέλεια, κλάσεις αποθήκευσης (`auto`, `static`, `extern`, `register`)
  * Πρωτογενείς τύποι και τα μεγέθη τους (εξαρτώμενα από την υλοποίηση αλλά προβλέψιμα στις περισσότερες πλατφόρμες)
  * Ροή ελέγχου: `if/else`, `switch`, `for`, `while`, `do-while`, `goto` (χρήση με φειδώ)
  * Συναρτήσεις: δήλωση, ορισμός, πέρασμα παραμέτρων (κατ' τιμήν έναντι προσομοίωσης αναφοράς μέσω δεικτών)
  * Παράδειγμα: `void swap(int *a, int *b)` για τροποποίηση επί τόπου (in-place)

* **Δείκτες, Μνήμη & Πίνακες (Pointers, Memory & Arrays)**
  * Δείκτες ως στοιχεία πρώτης τάξης (first-class citizens): αριθμητική διευθύνσεων, αποσυμβολισμός/επιτόπια προσπέλαση
  * Εκφυλισμός πινάκων σε δείκτες (array decay): `int arr[10]` → `int *`
  * Πολυδιάστατοι πίνακες ως πίνακες πινάκων (διάταξη row-major)
  * Δυναμική μνήμη: `malloc()`, `calloc()`, `realloc()`, `free()`
  * Παγίδες χειροκίνητης διαχείρισης μνήμης (διαρροές/memory leaks, διπλή αποδέσμευση/double-free, χρήση μετά την αποδέσμευση/use-after-free, μετέωροι δείκτες/dangling pointers)
  * Συμβολοσειρές ως πίνακες χαρακτήρων τερματιζόμενοι με null (`char[]`) + συναρτήσεις του `<string.h>`
  * Ορθότητα `const` (const correctness) και qualifiers όπως `volatile` για καταχωρητές υλικού

* **Δομές, Ενώσεις & Δυαδικός Χειρισμός (Structs, Unions & Bit Manipulation)**
  * Τύποι οριζόμενοι από τον χρήστη: `struct` (συγκέντρωση δεδομένων)
  * `typedef` για καθαρότερη σύνταξη
  * `union` (ένωση) για επικάλυψη μνήμης / type punning
  * Πεδία bit (bit-fields) και δυαδικές πράξεις (`&`, `|`, `^`, `~`, μετατοπίσεις/shifts)
  * Ευθυγράμμιση (alignment) και συμπλήρωση μνήμης (padding) σε δομές (απόδοση + ζητήματα ABI)

* **Προεπεξεργαστής & Διαδικασία Μεταγλώττισης (Preprocessor & Build Process)**
  * Μακροεντολές (`#define`), μεταγλώττιση υπό συνθήκη (`#ifdef`, `#ifndef`)
  * Αρχεία επικεφαλίδας (`.h`) έναντι αρχείων υλοποίησης (`.c`)
  * Μοντέλο ξεχωριστής μεταγλώττισης + σύνδεσης (linking)
  * Εισαγωγή στο `make` / συστήματα δομής λογισμικού (build systems)
  * Ενσωματωμένες συναρτήσεις (inline functions) και επιπτώσεις στην απόδοση

* **Πρότυπη Βιβλιοθήκη & Προγραμματισμός Συστημάτων (Standard Library & Systems Programming)**
  * `<stdio.h>`, `<stdlib.h>`, `<string.h>`, `<math.h>`
  * Είσοδος/Έξοδος αρχείων (File I/O): `fopen`, `fread`, `fwrite`, ενταμιευτής (buffering)
  * Έλεγχος διεργασιών, σήματα (signals), μεταβλητές περιβάλλοντος
  * Σχέση με τη C++: η C είναι αυστηρό υποσύνολο· η C++ προσθέτει RAII, πρότυπα (templates), εξαιρέσεις (exceptions), OOP κ.λπ.
  * Φορητότητα έναντι κώδικα ειδικού για πλατφόρμα (POSIX, Win32)

* **Απόδοση & Low-Level Βελτιστοποίηση (Performance & Low-Level Optimization)**
  * Άμεση προσπέλαση στο υλικό (ενσωματωμένη συμβολική γλώσσα / inline assembly όταν απαιτείται)
  * Δομές δεδομένων και μοτίβα προσπέλασης φιλικά προς την κρυφή μνήμη (cache-friendly)
  * Μηδενικό πρόσθετο κόστος εκτέλεσης (χωρίς συλλογή απορριμμάτων / GC, χωρίς κρυφές επιβαρύνσεις)
  * Κοινά ιδιώματα: χειροκίνητη ξεδίπλωση βρόχων (manual unrolling), λέξη-κλειδί `restrict` (`__restrict`)
  * Σύνδεση με το μοντέλο απόδοσης της C++ και τις επεκτάσεις C της Python (εσωτερικά του CPython)

> [Beej's Guide to C Programming](https://beej.us/guide/bgc/)
> [C Programming Language (K&R)](https://en.wikipedia.org/wiki/The_C_Programming_Language) — το κλασικό σύγγραμμα

---

* **Haskell**
  * Βασικές Έννοιες Αμιγών Συναρτήσεων (Basics of Pure Functions)
    * Αμετάβλητη κατάσταση (immutable state - χωρίς επαναθέτηση)
    * Αναφορική διαφάνεια (referential transparency)
    * Οκνηρή αξιολόγηση (lazy evaluation) → thunks (υπολογισμός μόνο όταν απαιτείται)
    * Χωρίς βρόχους → αμιγής αναδρομή & συναρτήσεις ανώτερης τάξης
  * Κατασκευές Λιστών & Ταίριασμα Μοτίβων (List Comprehensions & Pattern Matching)
    * Μορφή: `[ output | input_set, predicates ]`
    * Γεννήτριες (generators): `x <- [1..10]`
    * Κατηγορήματα (predicates) ως φίλτρα: `x \`mod\` 2 == 0`
    * Πολλαπλές / εξαρτημένες γεννήτριες → καρτεσιανά γινόμενα
    * Άπειρες λίστες + `take` (οκνηρή ασφαλής εξαγωγή)
    * Κόσκινο του Ερατοσθένη, ακολουθία Fibonacci μέσω χρυσής τομής
    * Ταίριασμα μοτίβων (pattern matching) & προτάσεις φυλάκων (guards - χωρίς if/else)
    * Σύγκριση με Python:
      * Τετράγωνα: `[x^2 | x <- [1..10]]`
      * Άρτιοι: `[x | x <- [1..20], x \`mod\` 2 == 0]`
      * Ζεύγη: `[(x,y) | x <- [1..3], y <- [1..3]]`
  * Συναρτήσεις Ανώτερης Τάξης & Σύστημα Τύπων (Higher-Order Functions & Type System)
    * Συναρτήσεις πρώτης τάξης (first-class: πέρασμα, αποθήκευση, επιστροφή)
    * Currying: κάθε συνάρτηση δέχεται ακριβώς ένα όρισμα
    * Μερική εφαρμογή (partial application) → νέα συνάρτηση από λιγότερα ορίσματα
    * Στατική εξαγωγή τύπων (static type inference)
    * Κλάσεις τύπων (Typeclasses): `Show`, `Read`, `Bounded`
    * Αλγεβρικοί τύποι δεδομένων (Algebraic Data Types - ADTs)
    * Τύπος `Maybe`: `Just value` / `Nothing` (ασφάλεια έναντι null)
  * Προηγμένες Αφαιρέσεις (Advanced Abstractions)
    * Συνάρτημα (Functor) → απεικόνιση (map) πάνω σε έναν τύπο
    * Εφαρμοστικό Συνάρτημα (Applicative Functor) → εφαρμογή τυλιγμένων συναρτήσεων σε τυλιγμένες τιμές
    * Μονάδα (Monad) → αλληλουχία υπολογισμών εξαρτώμενων από το πλαίσιο· απομόνωση παρενεργειών (I/O)
    * Μονοειδές (Monoid) → προσεταιριστικές πράξεις με ουδέτερο στοιχείο
    * Zipper → συναρτησιακή πλοήγηση σε αμετάβλητες δομές δέντρων
    * Αναφορική ισότητα (equational reasoning) & μαθηματική επαγωγή για αποδείξεις ορθότητας

> [https://www.youtube.com/watch?v=TklkNLihQ_A](https://www.youtube.com/watch?v=TklkNLihQ_A)
> [https://www.youtube.com/watch?v=Ex4FWMexQNo](https://www.youtube.com/watch?v=Ex4FWMexQNo)
> [https://www.classcentral.com/course/youtube-haskell-for-beginners-59640](https://www.classcentral.com/course/youtube-haskell-for-beginners-59640)
> [https://www.youtube.com/watch?v=bc3_yZEAC_0](https://www.youtube.com/watch?v=bc3_yZEAC_0)
> [https://www.youtube.com/c/grahamhuttonnotts](https://www.youtube.com/c/grahamhuttonnotts)

---

* **Prolog**
  * Βασικές Έννοιες Λογικού Προγραμματισμού (Basics of Logic Programming)
    * Βάση γνώσης: γεγονότα (facts) + κανόνες (rules)
    * Γεγονός: ισχυρισμός χωρίς όρους → `parent(alice, bob)`
    * Κανόνας (πρόταση Horn / Horn clause): `dating(X,Y) :- likes(X,Y), likes(Y,X)`
    * Ερωτήματα (queries) στη βάση γνώσης
    * Μηχανή λογικού συμπερασμού → αλήθειες Boolean ή ενσαρκώσεις μεταβλητών (instantiations)
  * Μηχανισμοί Εκτέλεσης (Execution Mechanisms)
    * Επίλυση (resolution) μέσω οπισθοδρομικής αλυσίδωσης (backward chaining)
    * Οπισθοδρόμηση (backtracking) σε περίπτωση αντίφασης → αναζήτηση εναλλακτικού μονοπατιού
    * Αναδρομικές σχέσεις: `ancestor(X,Y)`
      * Βασική περίπτωση (base case): το `X` είναι άμεσος γονέας του `Y`
      * Αναδρομική περίπτωση: το `X` είναι πρόγονος του `Z`, το `Z` γονέας του `Y`
    * Ενοποίηση μεταβλητών (unification) σε δέντρα καταγωγής
    * Ακαδημαϊκό παράδειγμα βάσης δεδομένων: `passed(Student, Course, PassGrade)`, `enrolled(Student, Course)`
  * Επεξεργασία Λιστών & Καταστάσεις Παραμέτρων (List Processing & Parameter Modes)
    * Δεσμευμένες παράμετροι (bound) → λειτουργούν ως είσοδος
    * Ελεύθερες παράμετροι (unbound) → λειτουργούν ως έξοδος (συμπληρώνονται από τη μηχανή)
    * Πολυκατευθυντική εκτέλεση (multidirectional execution)
    * `append(A, B, C)`: προς τα εμπρός (A+B→C) ή αντίστροφα (C→όλα τα ζεύγη A,B)
    * Δομική αναδρομή σε κεφαλή/ουρά (head/tail)
    * Αντιστροφή & διάσχιση λίστας χωρίς ρητό τύπο επιστροφής
  * Προηγμένες Εφαρμογές (Advanced Applications)
    * Προβλήματα ικανοποίησης περιορισμών (Constraint Satisfaction Problems - CSP)
    * Χρονοπρογραμματισμός, βελτιστοποίηση πόρων, Sudoku
    * Ο προγραμματιστής ορίζει περιορισμούς → η μηχανή αναζητά στον χώρο καταστάσεων
    * Τεχνητή Νοημοσύνη Παιχνιδιών (Game AI): δέντρα αποφάσεων NPC, συστήματα διαλόγου/γνώσης
    * Μοντέλα γλωσσολογίας & γνωσιακής επιστήμης

> [https://www.youtube.com/watch?v=gJOZZvYijqk](https://www.youtube.com/watch?v=gJOZZvYijqk)
> [https://www.youtube.com/watch?v=zK7J7lyl9J0](https://www.youtube.com/watch?v=zK7J7lyl9J0)
> [https://www.youtube.com/watch?v=8caRh1lZfDs](https://www.youtube.com/watch?v=8caRh1lZfDs)
