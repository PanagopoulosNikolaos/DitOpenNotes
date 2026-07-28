# Πρακτική Εφαρμογή & Περιβάλλοντα Ανάπτυξης
*Practical Application & Development Environments*

---

## Πίνακας Περιεχομένων
*Table of Contents*

1. [Εισαγωγή](#εισαγωγή)
2. [Εργαλεία, Συστήματα & Αρχιτεκτονική](#εργαλεία-συστήματα--αρχιτεκτονική)
   - [MySQL Server](#mysql-server)
   - [MySQL Workbench](#mysql-workbench)
   - [XAMPP & phpMyAdmin](#xampp--phpmyadmin)
   - [Συγκριτικός Πίνακας: Εργαλεία Διαχείρισης](#συγκριτικός-πίνακας-εργαλεία-διαχείρισης)
3. [Υλοποίηση σε Πραγματικές Συνθήκες](#υλοποίηση-σε-πραγματικές-συνθήκες)
   - [Προσδιορισμός Κατάλληλων Τύπων Δεδομένων](#προσδιορισμός-κατάλληλων-τύπων-δεδομένων)
   - [Υλοποίηση Περιορισμών (NOT NULL, UNIQUE, DEFAULT)](#υλοποίηση-περιορισμών-not-null-unique-default)
   - [Σύνδεση Πινάκων μέσω Ξένων Κλειδιών (FOREIGN KEY ... REFERENCES)](#σύνδεση-πινάκων-μέσω-ξένων-κλειδιών-foreign-key--references)
   - [Διαχείριση Σχέσεων "Πολλά-προς-Πολλά" (Ενδιάμεσος Πίνακας)](#διαχείριση-σχέσεων-πολλά-προς-πολλά-ενδιάμεσος-πίνακας)
4. [Πίνακας Βασικών Εννοιών](#πίνακας-βασικών-εννοιών)
5. [Βασικά Συμπεράσματα](#βασικά-συμπεράσματα)

---

## Εισαγωγή

Η θεωρητική γνώση των μοντέλων δεδομένων, της Σχεσιακής Άλγεβρας και της SQL αποκτά πλήρη αξία μόνο όταν εφαρμοστεί σε πραγματικό λογισμικό. Στο πλαίσιο του μαθήματος, το κυρίαρχο σύστημα υλοποίησης είναι το **MySQL** — ένα από τα πιο διαδεδομένα ανοιχτού κώδικα **Relational Database Management Systems (RDBMS)** παγκοσμίως. Η πρακτική αυτή ενότητα καλύπτει τόσο τα **εργαλεία** (MySQL Server, MySQL Workbench, XAMPP, phpMyAdmin) όσο και τις **αποφάσεις σχεδιασμού** που λαμβάνει ο διαχειριστής ΒΔ κατά την υλοποίηση: επιλογή τύπων δεδομένων, ορισμό περιορισμών, δήλωση Ξένων Κλειδιών και χειρισμό σχέσεων N:M μέσω ενδιάμεσων πινάκων. Η ικανότητα να μεταφράζεται ένα ER διάγραμμα ή ένα Σχεσιακό Σχήμα σε λειτουργική MySQL βάση δεδομένων αποτελεί θεμελιώδη δεξιότητα κάθε μηχανικού λογισμικού.

---

## Εργαλεία, Συστήματα & Αρχιτεκτονική
*Tools, Systems & Architecture*

Η αρχιτεκτονική ενός συστήματος MySQL βασίζεται στο μοντέλο **client-server**: ο **MySQL Server** εκτελείται στο παρασκήνιο ως υπηρεσία (service/daemon) που διαχειρίζεται τα δεδομένα, ενώ διάφορα **client εργαλεία** συνδέονται σε αυτόν για να εκτελέσουν ερωτήματα και διαχειριστικές εργασίες.

```text
  Αρχιτεκτονική Client-Server MySQL:

  +---------------------+        TCP/IP ή Socket        +---------------------+
  |     CLIENT TOOLS    |  <-------------------------->  |    MySQL Server     |
  +---------------------+                               +---------------------+
  |  mysql CLI          |                               |  - Query Engine     |
  |  MySQL Workbench    |                               |  - Storage Engine   |
  |  phpMyAdmin         |                               |    (InnoDB)         |
  |  Εφαρμογή (PHP/     |                               |  - Buffer Pool      |
  |  Python/Java)       |                               |  - Log Files        |
  +---------------------+                               +---------------------+
                                                               |
                                                        +------+------+
                                                        |  Δεδομένα  |
                                                        |  (Αρχεία   |
                                                        |  Δίσκου)   |
                                                        +------------+
```

---

### MySQL Server
*The Backend Database Management System*

Ο **MySQL Server** είναι ο πυρήνας (backend) του συστήματος — η διεργασία που **αποθηκεύει, οργανώνει και εξυπηρετεί** τα δεδομένα. Εκτελείται συνεχώς ως **υπηρεσία** του λειτουργικού συστήματος και ακούει για εισερχόμενες συνδέσεις από clients (από προεπιλογή στη θύρα **3306**). Δεν έχει γραφικό περιβάλλον — η αλληλεπίδραση γίνεται μέσω SQL εντολών που αποστέλλονται από ένα client.

**Κύρια χαρακτηριστικά:**
- Υποστηρίζει πολλαπλούς ταυτόχρονους χρήστες (**Concurrency**) μέσω transaction management.
- Χρησιμοποιεί κατά κύριο λόγο τη **Storage Engine InnoDB**, η οποία υποστηρίζει Foreign Keys, Transactions και ACID εγγυήσεις.
- Διαχειρίζεται δικαιώματα πρόσβασης (**privileges**) ανά χρήστη και ανά βάση δεδομένων.

**Σύνδεση μέσω γραμμής εντολών (mysql CLI):**

```sql
-- Σύνδεση ως root χρήστης στον τοπικό MySQL Server
mysql -u root -p

-- Αφού συνδεθεί, εμφάνιση διαθέσιμων βάσεων
SHOW DATABASES;
```

```text
  mysql> SHOW DATABASES;
  +--------------------+
  | Database           |
  +--------------------+
  | information_schema |
  | mysql              |
  | performance_schema |
  | sys                |
  | university_db      |
  +--------------------+
  5 rows in set (0.00 sec)
```

**Exam Note:** Οι βάσεις `information_schema`, `mysql`, `performance_schema` και `sys` είναι **συστημικές βάσεις** που δημιουργούνται αυτόματα από τον MySQL Server. Δεν πρέπει ποτέ να τροποποιηθούν χειροκίνητα.

---

### MySQL Workbench
*Graphical Database Management Environment / GUI Client*

Το **MySQL Workbench** είναι το επίσημο **γραφικό περιβάλλον (GUI)** που παρέχει η Oracle για τη διαχείριση MySQL Server. Συνδυάζει σε ένα εργαλείο:
- **SQL Editor**: Σύνταξη και εκτέλεση SQL ερωτημάτων με syntax highlighting και αυτόματη συμπλήρωση.
- **Visual Schema Designer (EER Diagram)**: Οπτική σχεδίαση και τροποποίηση σχημάτων βάσεων δεδομένων — δημιουργία πινάκων, ορισμός σχέσεων με drag-and-drop.
- **Server Administration**: Διαχείριση χρηστών, δικαιωμάτων, status του server και log files.
- **Data Export / Import**: Εισαγωγή και εξαγωγή δεδομένων σε μορφές SQL dump, CSV κ.ά.

```text
  MySQL Workbench — Περιοχές Εργασίας:

  +-----------------------------------------------------------+
  |                    MySQL Workbench                        |
  +------------------+----------------------------------------+
  |  Navigator       |                                        |
  |  +------------+  |   +--------------------------------+  |
  |  | Schemas    |  |   |       SQL Editor               |  |
  |  | - uni_db   |  |   |  SELECT * FROM Foititis;       |  |
  |  |   Tables   |  |   |  > Execute (Ctrl+Enter)        |  |
  |  |   Views    |  |   +--------------------------------+  |
  |  |   Procs    |  |   |       Result Grid              |  |
  |  +------------+  |   |  am | onoma | eponymo | ...    |  |
  |                  |   +--------------------------------+  |
  +------------------+----------------------------------------+
```

**Αναλογία**: Το MySQL Workbench είναι σαν ένα **cockpit αεροπλάνου** — παρέχει όλες τις πληροφορίες και τα χειριστήρια σε ένα γραφικό περιβάλλον, ενώ ο MySQL Server είναι οι κινητήρες που πραγματικά εκτελούν τη δουλειά.

---

### XAMPP & phpMyAdmin
*Web-Based Management Package and Services*

Το **XAMPP** (X = Cross-platform, A = Apache, M = MariaDB/MySQL, P = PHP, P = Perl) είναι ένα **πακέτο εγκατάστασης** που ενσωματώνει σε ένα installer:
- **Apache HTTP Server**: Web server για εξυπηρέτηση PHP εφαρμογών.
- **MySQL / MariaDB**: Relational database server.
- **PHP**: Server-side scripting language.
- **phpMyAdmin**: Web-based εργαλείο διαχείρισης MySQL μέσω browser.

Το **phpMyAdmin** είναι μια PHP εφαρμογή που εκτελείται στον Apache και παρέχει **πλήρη διαχείριση MySQL μέσω web browser**, χωρίς εγκατάσταση επιπλέον λογισμικού. Είναι ιδανικό για web hosting περιβάλλοντα όπου δεν υπάρχει άμεση πρόσβαση CLI.

```text
  XAMPP Stack — Αρχιτεκτονική:

  Browser (Client)
       |
       | HTTP Request (π.χ. http://localhost/phpmyadmin)
       v
  +--------------------+
  |   Apache Server    |  <-- Εκτελεί PHP scripts
  +--------------------+
       |
       | MySQL Protocol (θύρα 3306)
       v
  +--------------------+
  |  MySQL / MariaDB   |  <-- Αποθηκεύει τα δεδομένα
  +--------------------+

  Η phpMyAdmin είναι ένα σύνολο PHP αρχείων στον Apache
  που δρουν ως web-based MySQL client.
```

**Key Distinction:** Το XAMPP χρησιμοποιείται συχνά για **τοπική ανάπτυξη (localhost)** web εφαρμογών, ενώ σε περιβάλλον παραγωγής (production) τα στοιχεία (Apache, MySQL, PHP) εγκαθίστανται και διαμορφώνονται χωριστά για λόγους ασφάλειας και απόδοσης.

---

### Συγκριτικός Πίνακας: Εργαλεία Διαχείρισης
*Comparative Table: Management Tools*

| Χαρακτηριστικό | MySQL Server (CLI) | MySQL Workbench | phpMyAdmin |
|---|---|---|---|
| **Τύπος** | CLI / Backend Service | Desktop GUI Client | Web-based GUI Client |
| **Διεπαφή** | Γραμμή εντολών | Γραφική (Desktop App) | Browser |
| **Εγκατάσταση** | Μόνο | Χωριστά (requires Server) | Μέρος XAMPP ή standalone |
| **Σχεδίαση ER** | Όχι | Ναι (Visual EER Designer) | Περιορισμένα |
| **Κατάλληλο για** | Scripting, automation | Ανάπτυξη, σχεδίαση | Web hosting, γρήγορη πρόσβαση |
| **Απαιτεί PHP/Apache** | Όχι | Όχι | Ναι |
| **Import/Export** | mysqldump CLI | Ναι (GUI) | Ναι (GUI) |

---

## Υλοποίηση σε Πραγματικές Συνθήκες
*Implementation in Real-World Conditions*

Η υλοποίηση ενός Σχεσιακού Σχήματος σε MySQL απαιτεί πέρα από τη γνώση σύνταξης SQL και μια σειρά από **αποφάσεις σχεδιασμού** που επηρεάζουν την ακεραιότητα, την απόδοση και τη συντηρησιμότητα της βάσης. Οι κρίσιμες αποφάσεις αφορούν: ποιος **τύπος δεδομένων** ταιριάζει σε κάθε πεδίο, ποιοι **περιορισμοί** (constraints) διασφαλίζουν την ποιότητα των δεδομένων, και πώς υλοποιούνται οι **σχέσεις** μεταξύ πινάκων.

---

### Προσδιορισμός Κατάλληλων Τύπων Δεδομένων
*Determining Appropriate Data Types*

Ο **τύπος δεδομένων** (data type) κάθε στήλης ορίζει το **είδος και το εύρος των τιμών** που μπορεί να αποθηκεύσει. Η επιλογή του σωστού τύπου είναι κρίσιμη: ένας τύπος πολύ μεγάλος σπαταλά αποθηκευτικό χώρο, ενώ ένας πολύ μικρός μπορεί να μην χωρέσει τα δεδομένα και να προκαλέσει σφάλμα ή απώλεια πληροφορίας.

**Κύριες κατηγορίες τύπων δεδομένων MySQL:**

| Κατηγορία | Τύπος | Αποθήκευση / Εύρος | Τυπική Χρήση |
|---|---|---|---|
| **Ακέραιοι** | `TINYINT` | 1 byte, -128 έως 127 (ή 0-255 UNSIGNED) | Boolean flags, μικρές κατηγορίες |
| | `SMALLINT` | 2 bytes, -32,768 έως 32,767 | Μικροί αριθμοί |
| | `INT` / `INTEGER` | 4 bytes, ~-2.1 δισ. έως 2.1 δισ. | IDs, ποσότητες, counts |
| | `BIGINT` | 8 bytes, ~-9.2 · 10¹⁸ έως 9.2 · 10¹⁸ | Πολύ μεγάλοι αριθμοί, timestamps |
| **Δεκαδικοί** | `FLOAT` | 4 bytes | Κατά προσέγγιση δεκαδικά |
| | `DOUBLE` | 8 bytes | Επιστημονικοί υπολογισμοί |
| | `DECIMAL(M,D)` | Μεταβλητό | Χρηματικά ποσά (ακριβής αναπαράσταση) |
| **Κείμενο** | `CHAR(N)` | Σταθερό N bytes (1-255) | Κωδικοί σταθερού μήκους (π.χ. ISO χώρας) |
| | `VARCHAR(N)` | Μεταβλητό, έως N bytes (1-65535) | Ονόματα, emails, τίτλοι |
| | `TEXT` | Έως 65,535 bytes | Μεγάλα κείμενα (περιγραφές, σχόλια) |
| **Ημερομηνία/Ώρα** | `DATE` | 3 bytes, `YYYY-MM-DD` | Ημερομηνία γέννησης, έναρξης |
| | `DATETIME` | 8 bytes, `YYYY-MM-DD HH:MM:SS` | Χρονοσφραγίδα γεγονότος |
| | `TIMESTAMP` | 4 bytes, αυτόματη ενημέρωση UTC | Τελευταία τροποποίηση εγγραφής |
| | `TIME` | 3 bytes, `HH:MM:SS` | Διάρκεια, ωράριο |
| **Λογικός** | `BOOLEAN` / `TINYINT(1)` | 1 byte (0 = FALSE, 1 = TRUE) | Σημαίες κατάστασης |

**Παράδειγμα — Δημιουργία πίνακα `Foititis` με επιλεγμένους τύπους:**

```sql
CREATE TABLE Foititis (
    -- INT: ακέραιος αριθμητικός Αριθμός Μητρώου, μέχρι ~2 δισ.
    am           INT            NOT NULL,
    -- VARCHAR(50): μεταβλητού μήκους κείμενο, έως 50 χαρακτήρες
    onoma        VARCHAR(50)    NOT NULL,
    eponymo      VARCHAR(50)    NOT NULL,
    -- VARCHAR(100): email μπορεί να είναι μεγαλύτερο
    email        VARCHAR(100),
    -- DATE: αποθηκεύει μόνο ημερομηνία χωρίς ώρα
    hmerominia   DATE,
    -- INT: Foreign Key προς dept_id του πίνακα Tmima
    dept_id      INT            NOT NULL,
    PRIMARY KEY (am)
);
```

**Σύγκριση `CHAR` vs `VARCHAR`:**

| Χαρακτηριστικό | `CHAR(N)` | `VARCHAR(N)` |
|---|---|---|
| **Μήκος αποθήκευσης** | Πάντα N bytes (συμπληρώνεται με κενά) | Πραγματικό μήκος + 1-2 bytes overhead |
| **Απόδοση** | Ταχύτερο για σταθερό μήκος | Αποδοτικότερο για μεταβλητό μήκος |
| **Κατάλληλο για** | Κωδικοί χώρας (`GR`, `US`), ΑΦΜ | Ονόματα, emails, διευθύνσεις |

**Exam Note:** Για χρηματικά ποσά, **ποτέ** δεν χρησιμοποιείται `FLOAT` ή `DOUBLE` λόγω αποσφαλμάτωσης κινητής υποδιαστολής (floating-point rounding errors). Χρησιμοποιείται `DECIMAL(10, 2)` (π.χ. 10 ψηφία συνολικά, 2 δεκαδικά) για ακριβή αναπαράσταση.

---

### Υλοποίηση Περιορισμών (NOT NULL, UNIQUE, DEFAULT)
*Implementing Constraints*

Οι **περιορισμοί (Constraints)** είναι κανόνες που επιβάλλει η MySQL αυτόματα σε κάθε `INSERT` ή `UPDATE`, διασφαλίζοντας την **ακεραιότητα των δεδομένων** (data integrity). Ορίζονται κατά τη δημιουργία (`CREATE TABLE`) ή προστίθενται αργότερα (`ALTER TABLE`).

**Κύριοι περιορισμοί:**

| Περιορισμός | Σκοπός | Παραβίαση |
|---|---|---|
| `NOT NULL` | Απαγορεύει NULL τιμές σε μια στήλη | `ERROR 1048: Column cannot be null` |
| `UNIQUE` | Διασφαλίζει μοναδικότητα τιμών (NULL επιτρέπεται) | `ERROR 1062: Duplicate entry` |
| `DEFAULT value` | Ορίζει προεπιλεγμένη τιμή αν δεν δοθεί | — (δεν προκαλεί σφάλμα) |
| `PRIMARY KEY` | `NOT NULL` + `UNIQUE` + index | `ERROR 1062` ή `ERROR 1048` |
| `CHECK (expr)` | Επαληθεύει λογική συνθήκη (MySQL 8.0.16+) | `ERROR 3819: Check constraint violated` |

**Παράδειγμα — Πίνακας `Mathima` με πολλαπλούς περιορισμούς:**

```sql
CREATE TABLE Mathima (
    -- PRIMARY KEY: NOT NULL + UNIQUE αυτόματα
    mathima_id   INT           NOT NULL AUTO_INCREMENT,
    -- NOT NULL: ο τίτλος είναι υποχρεωτικός
    titlos       VARCHAR(100)  NOT NULL,
    -- UNIQUE: ο κωδικός μαθήματος πρέπει να είναι μοναδικός
    kodikos      VARCHAR(10)   NOT NULL UNIQUE,
    -- DEFAULT: αν δεν δοθούν μονάδες ECTS, θεωρούνται 5
    ects         TINYINT       NOT NULL DEFAULT 5,
    -- NULL επιτρέπεται: η περιγραφή είναι προαιρετική
    perigrafi    TEXT,
    -- CHECK: οι μονάδες ECTS πρέπει να είναι μεταξύ 1 και 30
    CONSTRAINT chk_ects CHECK (ects BETWEEN 1 AND 30),
    PRIMARY KEY (mathima_id)
);
```

**Επίδειξη συμπεριφοράς περιορισμών:**

**Κατάσταση πριν:**
```text
  mysql> SELECT * FROM Mathima;
  Empty set (0.00 sec)
```

**Επιτυχής εισαγωγή (με DEFAULT):**
```sql
-- Δεν δίνεται τιμή για ects — λαμβάνει DEFAULT 5
INSERT INTO Mathima (titlos, kodikos)
VALUES ('Βάσεις Δεδομένων', 'CS301');
```

**Κατάσταση μετά:**
```text
  mysql> SELECT * FROM Mathima;
  +------------+------------------+---------+------+-----------+
  | mathima_id | titlos           | kodikos | ects | perigrafi |
  +------------+------------------+---------+------+-----------+
  |          1 | Βάσεις Δεδομένων | CS301   |    5 | NULL      |
  +------------+------------------+---------+------+-----------+
```

**Παραβίαση NOT NULL:**
```sql
-- Δεν δίνεται τιμή για titlos (NOT NULL) — σφάλμα
INSERT INTO Mathima (kodikos) VALUES ('CS302');
-- ERROR 1364 (HY000): Field 'titlos' doesn't have a default value
```

**Παραβίαση UNIQUE:**
```sql
-- Ο κωδικός 'CS301' υπάρχει ήδη — παραβίαση UNIQUE
INSERT INTO Mathima (titlos, kodikos)
VALUES ('Άλλο Μάθημα', 'CS301');
-- ERROR 1062 (23000): Duplicate entry 'CS301' for key 'mathima.kodikos'
```

**Παραβίαση CHECK:**
```sql
-- ects = 50 υπερβαίνει το CHECK constraint (1-30)
INSERT INTO Mathima (titlos, kodikos, ects)
VALUES ('Μάθημα Τεστ', 'CS399', 50);
-- ERROR 3819 (HY000): Check constraint 'chk_ects' is violated.
```

**Key Distinction:** Η `UNIQUE` constraint επιτρέπει **πολλαπλές NULL τιμές** στην ίδια στήλη (η NULL δεν θεωρείται ίση με καμία τιμή, ούτε με άλλη NULL). Αντίθετα, η `PRIMARY KEY` **δεν επιτρέπει** καμία NULL τιμή.

---

### Σύνδεση Πινάκων μέσω Ξένων Κλειδιών (FOREIGN KEY ... REFERENCES)
*Connecting Tables via Foreign Keys*

Το **Ξένο Κλειδί (Foreign Key)** είναι ο μηχανισμός με τον οποίο η MySQL επιβάλλει **Αναφορική Ακεραιότητα (Referential Integrity)** μεταξύ δύο πινάκων. Διασφαλίζει ότι κάθε τιμή στη στήλη-FK του **θυγατρικού πίνακα (child table)** αντιστοιχεί σε μια υπάρχουσα τιμή στον **γονικό πίνακα (parent table)**.

**Κανόνες Αναφορικής Ακεραιότητας:**
- Δεν μπορεί να εισαχθεί εγγραφή στο child με τιμή FK που δεν υπάρχει στον parent.
- Δεν μπορεί να διαγραφεί εγγραφή από τον parent αν υπάρχουν child εγγραφές που την αναφέρουν.

**Σύνταξη δήλωσης FOREIGN KEY:**

```sql
-- Inline ορισμός (για απλές FK)
CREATE TABLE child_table (
    fk_column   INT,
    FOREIGN KEY (fk_column) REFERENCES parent_table (pk_column)
);

-- Ορισμός με όνομα constraint (προτεινόμενος — πιο αναγνώσιμος)
CREATE TABLE child_table (
    fk_column   INT,
    CONSTRAINT fk_child_parent
        FOREIGN KEY (fk_column)
        REFERENCES parent_table (pk_column)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);
```

**Παράδειγμα — Σχέση `Foititis` → `Tmima` (N:1):**

```text
  Σχεσιακό Σχήμα:
  Tmima(<u>dept_id</u>, onoma_tmimatos, sxoli)
  Foititis(<u>am</u>, onoma, eponymo, email, hmerominia, #dept_id)

  ER Αναπαράσταση:
  +-------------+            1:N           +------------+
  |    TMIMA    |  <>---( Ανήκει σε )---<  |  FOITITIS  |
  +-------------+                          +------------+
  | dept_id(PK) |                          | am (PK)    |
  | onoma_tmim. |                          | onoma      |
  | sxoli       |                          | eponymo    |
  +-------------+                          | dept_id(FK)|
                                           +------------+
```

**Δημιουργία πινάκων με FOREIGN KEY:**

```sql
-- Βήμα 1: Πρώτα ο γονικός πίνακας (parent)
CREATE TABLE Tmima (
    dept_id        INT          NOT NULL AUTO_INCREMENT,
    onoma_tmimatos VARCHAR(100) NOT NULL,
    sxoli          VARCHAR(100) NOT NULL,
    PRIMARY KEY (dept_id)
);

-- Βήμα 2: Μετά ο θυγατρικός πίνακας (child) με FK
CREATE TABLE Foititis (
    am           INT          NOT NULL,
    onoma        VARCHAR(50)  NOT NULL,
    eponymo      VARCHAR(50)  NOT NULL,
    email        VARCHAR(100) UNIQUE,
    hmerominia   DATE,
    dept_id      INT          NOT NULL,
    PRIMARY KEY (am),
    -- Ορισμός Foreign Key με ρητό όνομα constraint
    CONSTRAINT fk_foititis_tmima
        FOREIGN KEY (dept_id)
        REFERENCES Tmima (dept_id)
        ON DELETE RESTRICT   -- Αποτρέπει διαγραφή τμήματος με φοιτητές
        ON UPDATE CASCADE    -- Αν αλλάξει το dept_id στο Tmima, ενημερώνεται αυτόματα
);
```

**Επίδειξη Αναφορικής Ακεραιότητας:**

**Εισαγωγή δεδομένων:**
```sql
-- Εισαγωγή τμημάτων στον parent
INSERT INTO Tmima (onoma_tmimatos, sxoli)
VALUES ('Πληροφορική', 'Θετικών Επιστημών'),
       ('Μαθηματικά',  'Θετικών Επιστημών');
```

```text
  Tmima:
  +---------+-------------------+-------------------+
  | dept_id | onoma_tmimatos    | sxoli             |
  +---------+-------------------+-------------------+
  |       1 | Πληροφορική       | Θετικών Επιστημών |
  |       2 | Μαθηματικά        | Θετικών Επιστημών |
  +---------+-------------------+-------------------+
```

```sql
-- Επιτυχής εισαγωγή: dept_id=1 υπάρχει στο Tmima
INSERT INTO Foititis (am, onoma, eponymo, dept_id)
VALUES (10001, 'Αλέξης', 'Νικολόπουλος', 1);
```

**Παραβίαση FK — εισαγωγή με ανύπαρκτο dept_id:**
```sql
-- ΑΠΟΤΥΧΙΑ: dept_id=99 δεν υπάρχει στον πίνακα Tmima
INSERT INTO Foititis (am, onoma, eponymo, dept_id)
VALUES (10002, 'Ελένη', 'Παπαδοπούλου', 99);
-- ERROR 1452 (23000): Cannot add or update a child row:
-- a foreign key constraint fails (`university_db`.`Foititis`,
-- CONSTRAINT `fk_foititis_tmima` FOREIGN KEY (`dept_id`)
-- REFERENCES `Tmima` (`dept_id`))
```

**Παραβίαση FK — διαγραφή parent με εξαρτώμενα children:**
```sql
-- ΑΠΟΤΥΧΙΑ: το τμήμα 1 έχει φοιτητές — ON DELETE RESTRICT
DELETE FROM Tmima WHERE dept_id = 1;
-- ERROR 1451 (23000): Cannot delete or update a parent row:
-- a foreign key constraint fails
```

**Επιλογές ON DELETE / ON UPDATE:**

| Επιλογή | Συμπεριφορά κατά διαγραφή/ενημέρωση γονικής εγγραφής |
|---|---|
| `RESTRICT` (default) | Αποτρέπει την ενέργεια — επιστρέφει σφάλμα |
| `CASCADE` | Διαδίδει την αλλαγή αυτόματα στα children |
| `SET NULL` | Θέτει την FK στήλη σε NULL (η στήλη πρέπει να επιτρέπει NULL) |
| `NO ACTION` | Παρόμοιο με RESTRICT (ελέγχεται στο τέλος transaction) |
| `SET DEFAULT` | Θέτει DEFAULT τιμή (σπάνια υποστηρίζεται από InnoDB) |

**Exam Note:** Η σειρά δημιουργίας πινάκων έχει σημασία: **πρώτα ο γονικός (parent), μετά ο θυγατρικός (child)**. Αντίστροφα, κατά τη **διαγραφή**: **πρώτα ο child, μετά ο parent**. Επίσης, η MySQL απαιτεί το Storage Engine **InnoDB** (και όχι MyISAM) για την υποστήριξη Foreign Keys.

---

### Διαχείριση Σχέσεων "Πολλά-προς-Πολλά" (Ενδιάμεσος Πίνακας)
*Managing Many-to-Many Relationships via Junction Table*

Οι σχέσεις **N:M (Πολλά-προς-Πολλά)** δεν μπορούν να υλοποιηθούν άμεσα στο Σχεσιακό Μοντέλο. Η λύση είναι η **ανάλυσή τους σε δύο σχέσεις 1:N** μέσω ενός **ενδιάμεσου πίνακα (junction table / associative table / bridge table)**, που περιέχει τα Foreign Keys και των δύο πινάκων.

**Το πρόβλημα της N:M σχέσης:**

Έστω ότι ένας φοιτητής εγγράφεται σε πολλά μαθήματα, και κάθε μάθημα έχει πολλούς φοιτητές.

```text
  ER Διάγραμμα (N:M):
  +------------+     N:M          +------------+
  |  FOITITIS  |<>--( Εγγράφεται )--<>|  MATHIMA   |
  +------------+    σε            +------------+
  | am (PK)    |                  | mathima_id |
  | onoma      |                  | titlos     |
  +------------+                  +------------+

  ΠΡΟΒΛΗΜΑ: Δεν μπορεί να υλοποιηθεί με μία μόνο FK στήλη —
  ούτε ο Foititis μπορεί να έχει πολλές τιμές dept_id,
  ούτε το Mathima μπορεί να έχει πολλές τιμές am σε μία στήλη.
```

**Λύση — Ανάλυση σε δύο 1:N μέσω ενδιάμεσου πίνακα:**

```text
  Μετά ανάλυση:

  +------------+   1:N   +-------------------+   N:1   +------------+
  |  FOITITIS  |<--------| EGGRAFI (Junction) |-------->|  MATHIMA   |
  +------------+         +-------------------+         +------------+
  | am (PK)    |         | am (FK, PK)       |         | mathima_id |
  | onoma      |         | mathima_id (FK,PK)|         | titlos     |
  +------------+         | hmerominia_eggraf |         +------------+
                          | vathmos           |
                          +-------------------+

  Σχεσιακό Σχήμα:
  Foititis(<u>am</u>, onoma, eponymo, dept_id)
  Mathima(<u>mathima_id</u>, titlos, kodikos, ects)
  Eggrafi(<u>am</u>, <u>mathima_id</u>, hmerominia_eggrafis, vathmos)
           ^FK→Foititis  ^FK→Mathima
```

**Δημιουργία ενδιάμεσου πίνακα `Eggrafi`:**

```sql
-- Βήμα 1: Γονικοί πίνακες (Foititis και Mathima υπάρχουν ήδη)

-- Βήμα 2: Ο ενδιάμεσος πίνακας με Σύνθετο Primary Key
CREATE TABLE Eggrafi (
    -- FK προς Foititis
    am                  INT  NOT NULL,
    -- FK προς Mathima
    mathima_id          INT  NOT NULL,
    -- Επιπλέον γνωρίσματα της σχέσης (relationship attributes)
    hmerominia_eggrafis DATE,
    vathmos             DECIMAL(4, 2),
    -- Σύνθετο Primary Key: ο συνδυασμός am+mathima_id είναι μοναδικός
    PRIMARY KEY (am, mathima_id),
    -- FK προς Foititis
    CONSTRAINT fk_eggrafi_foititis
        FOREIGN KEY (am)
        REFERENCES Foititis (am)
        ON DELETE CASCADE,   -- Αν διαγραφεί φοιτητής, διαγράφονται οι εγγραφές του
    -- FK προς Mathima
    CONSTRAINT fk_eggrafi_mathima
        FOREIGN KEY (mathima_id)
        REFERENCES Mathima (mathima_id)
        ON DELETE RESTRICT   -- Δεν μπορεί να διαγραφεί μάθημα με εγγεγραμμένους φοιτητές
);
```

**Εισαγωγή δεδομένων στον ενδιάμεσο πίνακα:**

```sql
-- Φοιτητής am=10001 εγγράφεται στο μάθημα mathima_id=1
INSERT INTO Eggrafi (am, mathima_id, hmerominia_eggrafis)
VALUES (10001, 1, '2024-10-01');

-- Ο ίδιος φοιτητής εγγράφεται και σε δεύτερο μάθημα
INSERT INTO Eggrafi (am, mathima_id, hmerominia_eggrafis)
VALUES (10001, 2, '2024-10-01');

-- Άλλος φοιτητής στο ίδιο μάθημα
INSERT INTO Eggrafi (am, mathima_id, hmerominia_eggrafis)
VALUES (10002, 1, '2024-10-02');
```

```text
  Eggrafi:
  +-------+------------+--------------------+---------+
  | am    | mathima_id | hmerominia_eggraf. | vathmos |
  +-------+------------+--------------------+---------+
  | 10001 |          1 | 2024-10-01         |    NULL |
  | 10001 |          2 | 2024-10-01         |    NULL |
  | 10002 |          1 | 2024-10-02         |    NULL |
  +-------+------------+--------------------+---------+
```

**Ανάκτηση δεδομένων μέσω JOIN:**

```sql
-- Ποια μαθήματα παρακολουθεί ο φοιτητής am=10001;
SELECT f.onoma, f.eponymo, m.titlos, m.kodikos, e.hmerominia_eggrafis
FROM   Eggrafi e
JOIN   Foititis f  ON e.am         = f.am
JOIN   Mathima  m  ON e.mathima_id = m.mathima_id
WHERE  e.am = 10001;
```

```text
  +--------+--------------+------------------+---------+--------------------+
  | onoma  | eponymo      | titlos           | kodikos | hmerominia_eggraf. |
  +--------+--------------+------------------+---------+--------------------+
  | Αλέξης | Νικολόπουλος | Βάσεις Δεδομένων | CS301   | 2024-10-01         |
  | Αλέξης | Νικολόπουλος | Αλγόριθμοι       | CS201   | 2024-10-01         |
  +--------+--------------+------------------+---------+--------------------+
```

**Αποτροπή διπλής εγγραφής (ο ίδιος φοιτητής στο ίδιο μάθημα):**

```sql
-- Προσπάθεια διπλής εγγραφής: am=10001, mathima_id=1 υπάρχει ήδη
INSERT INTO Eggrafi (am, mathima_id)
VALUES (10001, 1);
-- ERROR 1062 (23000): Duplicate entry '10001-1' for key 'Eggrafi.PRIMARY'
-- Το Σύνθετο PK αποτρέπει την διπλή εγγραφή αυτόματα.
```

**Key Distinction:** Στον ενδιάμεσο πίνακα, το **Σύνθετο Primary Key** `(am, mathima_id)` εκτελεί διπλό ρόλο: (1) εγγυάται ότι κάθε συνδυασμός φοιτητή-μαθήματος εμφανίζεται **το πολύ μία φορά**, και (2) αποτελεί αυτόματα **index** για ταχύτερες αναζητήσεις βάσει και των δύο πεδίων.

---

## Πίνακας Βασικών Εννοιών
*Summary Table of Key Concepts*

| Έννοια | Ορισμός | Κύριο Χαρακτηριστικό / Κανόνας |
|---|---|---|
| **MySQL Server** | Το backend RDBMS που αποθηκεύει και εξυπηρετεί δεδομένα | Εκτελείται ως service, ακούει στη θύρα 3306 |
| **MySQL Workbench** | Επίσημο desktop GUI client για MySQL | Περιλαμβάνει SQL editor, Visual EER designer, server admin |
| **XAMPP** | Cross-platform πακέτο (Apache + MySQL/MariaDB + PHP) | Για τοπική ανάπτυξη web εφαρμογών (localhost) |
| **phpMyAdmin** | Web-based GUI για MySQL μέσω browser | Τρέχει ως PHP εφαρμογή στον Apache |
| **InnoDB** | Storage engine της MySQL | Υποστηρίζει Foreign Keys, Transactions, ACID |
| **Τύπος Δεδομένων** | Ορίζει το είδος και εύρος τιμών μιας στήλης | Λανθασμένος τύπος → σπατάλη χώρου ή απώλεια δεδομένων |
| **NOT NULL** | Constraint που απαγορεύει NULL τιμές | Παραβίαση → `ERROR 1048` |
| **UNIQUE** | Constraint μοναδικότητας τιμών (NULL επιτρέπεται) | Παραβίαση → `ERROR 1062` |
| **DEFAULT** | Ορίζει αυτόματη τιμή αν δεν παρασχεθεί | Δεν προκαλεί σφάλμα — εφαρμόζεται σιωπηλά |
| **FOREIGN KEY** | Στήλη που αναφέρεται σε Primary Key άλλου πίνακα | Επιβάλλει Αναφορική Ακεραιότητα |
| **ON DELETE CASCADE** | Διαδίδει τη διαγραφή στα child records | Προσοχή: μαζική αυτόματη διαγραφή |
| **ON DELETE RESTRICT** | Αποτρέπει διαγραφή parent αν υπάρχουν children | Προεπιλογή — ασφαλέστερη επιλογή |
| **Junction Table** | Ενδιάμεσος πίνακας για υλοποίηση N:M σχέσης | Φέρει Σύνθετο PK από τα δύο FK |
| **Σύνθετο Primary Key** | PK αποτελούμενο από δύο ή περισσότερες στήλες | Χρησιμοποιείται στον ενδιάμεσο πίνακα N:M |
| **AUTO_INCREMENT** | Αυτόματη αύξηση ακέραιου PK | Η MySQL αναθέτει την επόμενη διαθέσιμη τιμή |

---

## Βασικά Συμπεράσματα
*Key Takeaways*

- Ο **MySQL Server** είναι το backend σύστημα που εκτελείται ως service· τα εργαλεία (Workbench, phpMyAdmin, CLI) είναι απλώς **clients** που συνδέονται σε αυτόν.
- Το **MySQL Workbench** προσφέρει οπτικό σχεδιασμό σχημάτων (EER Diagrams) και είναι το κύριο εργαλείο ανάπτυξης· το **XAMPP/phpMyAdmin** στοχεύει σε web περιβάλλοντα και γρήγορη πρόσβαση μέσω browser.
- Η σωστή επιλογή **τύπου δεδομένων** είναι κρίσιμη: `INT` για IDs, `VARCHAR` για μεταβλητού μήκους κείμενα, `DATE` για ημερομηνίες, `DECIMAL` (όχι `FLOAT`) για χρηματικά ποσά.
- Ο συνδυασμός `NOT NULL`, `UNIQUE` και `DEFAULT` ορίζει τους κανόνες ποιότητας δεδομένων σε επίπεδο στήλης και επιβάλλεται αυτόματα από τη μηχανή κατά κάθε εγγραφή.
- Η δήλωση `FOREIGN KEY ... REFERENCES` με **ρητό όνομα constraint** είναι βέλτιστη πρακτική — διευκολύνει την αποσφαλμάτωση όταν εμφανίζεται σφάλμα παραβίασης FK.
- Η **Αναφορική Ακεραιότητα** απαιτεί αυστηρή σειρά δημιουργίας πινάκων: **πρώτα ο parent, μετά ο child**· και αντίστροφα για τη διαγραφή.
- Η `ON DELETE CASCADE` είναι ισχυρή αλλά επικίνδυνη — μια διαγραφή γονικής εγγραφής μπορεί να διαγράψει αυτόματα **δεκάδες ή χιλιάδες** child εγγραφές. Η `ON DELETE RESTRICT` είναι ο ασφαλέστερος προεπιλεγμένος κανόνας.
- Οι σχέσεις **N:M δεν υλοποιούνται ποτέ άμεσα** — αναλύονται πάντα σε δύο 1:N μέσω **ενδιάμεσου πίνακα** με **Σύνθετο Primary Key**.
- Ο ενδιάμεσος πίνακας μπορεί να φέρει **επιπλέον γνωρίσματα** της ίδιας της σχέσης (π.χ. ημερομηνία εγγραφής, βαθμός) που δεν ανήκουν στους αρχικούς πίνακες.
- Η MySQL απαιτεί **InnoDB** storage engine (όχι MyISAM) για την υποστήριξη Foreign Keys· ο έλεγχος γίνεται με `SHOW CREATE TABLE table_name;`.
