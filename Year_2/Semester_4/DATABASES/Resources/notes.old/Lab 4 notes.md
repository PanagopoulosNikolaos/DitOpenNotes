# vaseis_dedomenon_ergastirio_5_notes

Οι σημειώσεις καλύπτουν τις βασικές εντολές SQL που εμφανίζονται στο εργαστήριο: δημιουργία και επιλογή βάσης δεδομένων, δημιουργία πινάκων, πρωτεύοντα και ξένα κλειδιά, μεταβολές σχήματος με `ALTER TABLE`, καθώς και βασικό χειρισμό δεδομένων με `INSERT`, `UPDATE` και `DELETE`. Το παράδειγμα του υλικού βασίζεται στη βάση `Hollywood` και στους πίνακες `ACTORS`, `MOVIES` και `STARS`.

---

## 1. Concept Overview

Η SQL χρησιμοποιείται για δύο βασικές κατηγορίες ενεργειών στο παρόν υλικό:

- Ορισμό και μεταβολή του σχήματος της βάσης δεδομένων.
- Εισαγωγή, ενημέρωση και διαγραφή δεδομένων.

Η λογική του παραδείγματος είναι ότι:

- Ο πίνακας `ACTORS` αποθηκεύει στοιχεία ηθοποιών.
- Ο πίνακας `MOVIES` αποθηκεύει στοιχεία ταινιών.
- Ο πίνακας `STARS` συνδέει ηθοποιούς με ταινίες και αποθηκεύει επιπλέον γνωρίσματα της συμμετοχής τους, όπως τον ρόλο και την αμοιβή.

> **[Key Insight]**
> Ο πίνακας `STARS` υλοποιεί σχέση πολλών-προς-πολλά μεταξύ `ACTORS` και `MOVIES`. Ένας ηθοποιός μπορεί να παίζει σε πολλές ταινίες και μία ταινία μπορεί να έχει πολλούς ηθοποιούς.

---

## 2. Βασικές εντολές βάσης δεδομένων

### Syntax Reference

```sql
CREATE DATABASE <database_name>;
CREATE SCHEMA <database_name>;
SHOW DATABASES;
SHOW SCHEMAS;
DROP DATABASE <database_name>;
DROP SCHEMA <database_name>;
USE <database_name>;
```

### Behavioral Description

- `CREATE DATABASE` / `CREATE SCHEMA`: δημιουργεί νέα βάση δεδομένων.
- `SHOW DATABASES` / `SHOW SCHEMAS`: εμφανίζει τις διαθέσιμες βάσεις.
- `DROP DATABASE` / `DROP SCHEMA`: διαγράφει ολόκληρη βάση δεδομένων.
- `USE <database_name>`: ορίζει ποια βάση είναι ενεργή για τις επόμενες εντολές.

### Parameter Reference

| Name | Type/Values | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `<database_name>` | Έγκυρο όνομα βάσης | Ναι | Κανένα | Το όνομα της βάσης που δημιουργείται, επιλέγεται ή διαγράφεται. |

### Παράδειγμα

```sql
CREATE DATABASE Hollywood;
USE Hollywood;
SHOW DATABASES;
```

```text
Δημιουργείται η βάση Hollywood, ορίζεται ως ενεργή και στη λίστα βάσεων εμφανίζεται το Hollywood.
```

---

## 3. CREATE TABLE και πρωτεύοντα κλειδιά

### Syntax Reference

```sql
CREATE TABLE <table_name> (
    <field_1> <type_1> [constraints],
    <field_2> <type_2> [constraints],
    ...,
    PRIMARY KEY (<field_or_fields>)
);
```

### Behavioral Description

Η `CREATE TABLE` δημιουργεί έναν νέο πίνακα και ορίζει:

- τα ονόματα των στηλών,
- τους τύπους δεδομένων,
- τυχόν περιορισμούς όπως `NOT NULL`,
- το πρωτεύον κλειδί με `PRIMARY KEY`.

Το πρωτεύον κλειδί:

- αναγνωρίζει μοναδικά κάθε γραμμή,
- δεν επιτρέπεται να είναι `NULL`,
- μπορεί να αποτελείται από ένα ή περισσότερα πεδία.

### Parameter Reference

| Name | Type/Values | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `<table_name>` | Όνομα πίνακα | Ναι | Κανένα | Το όνομα του νέου πίνακα. |
| `<field_n>` | Όνομα πεδίου | Ναι | Κανένα | Στήλη του πίνακα. |
| `<type_n>` | `varchar(n)`, `int`, `date`, `real`, κ.ά. | Ναι | Κανένα | Τύπος δεδομένων της στήλης. |
| `constraints` | `NOT NULL`, κ.ά. | Όχι | Κανένα | Πρόσθετοι περιορισμοί στο πεδίο. |
| `PRIMARY KEY (...)` | Ένα ή περισσότερα πεδία | Ναι | Κανένα | Μοναδικός προσδιοριστής εγγραφών. |

### Παράδειγμα πίνακα `ACTORS`

```sql
CREATE TABLE ACTORS (
    ID varchar(10),
    NAME varchar(20) NOT NULL,
    BIRTHDATE date,
    BIRTHPLACE varchar(20),
    OSCARS int,
    PRIMARY KEY (ID)
);
```

```text
Δημιουργείται πίνακας ηθοποιών με πρωτεύον κλειδί το ID.
```

### Παράδειγμα πίνακα `MOVIES`

```sql
CREATE TABLE MOVIES (
    TITLE varchar(50),
    YEAR date,
    DIRECTOR varchar(50),
    BUDGET int,
    TICKETS int,
    PRIMARY KEY (TITLE)
);
```

```text
Δημιουργείται πίνακας ταινιών με πρωτεύον κλειδί το TITLE.
```

---

## 4. Ξένα κλειδιά και σύνδεση πινάκων

### Θεωρία

Ξένο κλειδί είναι ένα πεδίο ή συνδυασμός πεδίων ενός πίνακα, του οποίου οι τιμές πρέπει να υπάρχουν ήδη σε πεδίο άλλου πίνακα. Με αυτόν τον τρόπο εξασφαλίζεται αναφορική ακεραιότητα.

Στο παράδειγμα:

- το `ACTORS(ID)` είναι το πρωτεύον κλειδί των ηθοποιών,
- το `MOVIES(TITLE)` είναι το πρωτεύον κλειδί των ταινιών,
- ο πίνακας `STARS` περιέχει αυτά τα δύο πεδία ως ξένα κλειδιά.

### Syntax Reference

```sql
CREATE TABLE <table_name> (
    ...,
    FOREIGN KEY (<foreign_key_field>) REFERENCES <referenced_table>(<referenced_field>)
);
```

### Behavioral Description

- Το ξένο κλειδί επιτρέπει μόνο τιμές που υπάρχουν ήδη στον πίνακα αναφοράς.
- Αν μια τιμή δεν υπάρχει στον αναφερόμενο πίνακα, η εισαγωγή απορρίπτεται.
- Σε πίνακες συσχέτισης είναι συνηθισμένο να ορίζεται σύνθετο πρωτεύον κλειδί από τα ξένα κλειδιά.

### Parameter Reference

| Name | Type/Values | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `<foreign_key_field>` | Πεδίο τοπικού πίνακα | Ναι | Κανένα | Η στήλη που θα δείχνει σε άλλο πίνακα. |
| `<referenced_table>` | Όνομα πίνακα | Ναι | Κανένα | Ο πίνακας στον οποίο γίνεται αναφορά. |
| `<referenced_field>` | Πεδίο πίνακα αναφοράς | Ναι | Κανένα | Το πεδίο που πρέπει ήδη να περιέχει τις τιμές. |

### Παράδειγμα πίνακα `STARS`

```sql
CREATE TABLE STARS (
    ID VARCHAR(10),
    TITLE VARCHAR(50),
    ROLE VARCHAR(30),
    CACHE REAL,
    PRIMARY KEY (ID, TITLE),
    FOREIGN KEY (ID) REFERENCES ACTORS(ID),
    FOREIGN KEY (TITLE) REFERENCES MOVIES(TITLE)
);
```

```text
Δημιουργείται πίνακας συσχέτισης ηθοποιών-ταινιών. Κάθε γραμμή αντιστοιχεί σε μία συμμετοχή ηθοποιού σε μία ταινία.
```

> **[Key Insight]**
> Το σύνθετο πρωτεύον κλειδί `(ID, TITLE)` σημαίνει ότι ο ίδιος ηθοποιός δεν μπορεί να εμφανιστεί δύο φορές για την ίδια ταινία στον `STARS`.

---

## 5. ALTER TABLE

Η `ALTER TABLE` χρησιμοποιείται όταν ο πίνακας υπάρχει ήδη και θέλουμε να αλλάξουμε το σχήμα του.

### 5.1 Προσθήκη πεδίου

#### Syntax Reference

```sql
ALTER TABLE <table_name> ADD <field_name> <field_type>;
```

#### Example

```sql
ALTER TABLE MOVIES ADD DURATION varchar(6);
```

```text
Προστίθεται η στήλη DURATION στον πίνακα MOVIES.
```

### 5.2 Αλλαγή τύπου πεδίου

#### Syntax Reference

```sql
ALTER TABLE <table_name> MODIFY <field_name> <new_type>;
```

#### Behavioral Description

Η `MODIFY` αλλάζει μόνο τον τύπο του πεδίου και όχι το όνομά του.

#### Example

```sql
ALTER TABLE MOVIES MODIFY DURATION int;
```

```text
Η στήλη DURATION μετατρέπεται από varchar(6) σε int.
```

### 5.3 Διαγραφή πεδίου

#### Syntax Reference

```sql
ALTER TABLE <table_name> DROP COLUMN <field_name>;
```

#### Behavioral Description

Η διαγραφή στήλης συνεπάγεται απώλεια δεδομένων που βρίσκονται σε αυτήν τη στήλη.

#### Example

```sql
ALTER TABLE MOVIES DROP COLUMN DURATION;
```

```text
Η στήλη DURATION διαγράφεται από τον πίνακα MOVIES.
```

### 5.4 Μετονομασία πεδίου

#### Syntax Reference

```sql
ALTER TABLE <table_name> CHANGE <old_name> <new_name> <data_type>;
```

#### Example

```sql
ALTER TABLE ACTORS CHANGE BIRTHDATE DATE_OF_BIRTH DATE;
```

```text
Το πεδίο BIRTHDATE μετονομάζεται σε DATE_OF_BIRTH και δηλώνεται ο τύπος DATE.
```

### Parameter Reference

| Name | Type/Values | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `<table_name>` | Όνομα πίνακα | Ναι | Κανένα | Ο πίνακας που θα αλλάξει. |
| `<field_name>` | Όνομα πεδίου | Ναι | Κανένα | Το πεδίο που προστίθεται/μεταβάλλεται/διαγράφεται. |
| `<field_type>` | Τύπος SQL | Ναι στο `ADD` | Κανένα | Τύπος νέας στήλης. |
| `<new_type>` | Τύπος SQL | Ναι στο `MODIFY` | Κανένα | Νέος τύπος υπάρχουσας στήλης. |
| `<old_name>` | Παλιό όνομα | Ναι στο `CHANGE` | Κανένα | Το τρέχον όνομα της στήλης. |
| `<new_name>` | Νέο όνομα | Ναι στο `CHANGE` | Κανένα | Το νέο όνομα της στήλης. |
| `<data_type>` | Τύπος SQL | Ναι στο `CHANGE` | Κανένα | Ο τύπος που πρέπει να δηλωθεί ξανά. |

---

## 6. INSERT INTO

### Syntax Reference

```sql
INSERT INTO <table_name> VALUES (<value_1>, <value_2>, ...);
```

ή

```sql
INSERT INTO <table_name> (<field_list>) VALUES (<value_list>);
```

### Behavioral Description

- Κάθε `INSERT` εισάγει μία μόνο γραμμή σε έναν μόνο πίνακα.
- Αν χρησιμοποιηθεί η πλήρης μορφή με `VALUES (...)`, πρέπει να δοθεί τιμή για κάθε πεδίο.
- Αν δεν θέλουμε τιμή σε κάποιο πεδίο, γράφουμε `NULL`.
- Αν χρησιμοποιηθεί μορφή με λίστα πεδίων, όσα πεδία δεν δοθούν παίρνουν `NULL`.
- Τα πεδία `NOT NULL` και το πρωτεύον κλειδί πρέπει να πάρουν έγκυρη τιμή.

### Parameter Reference

| Name | Type/Values | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `<table_name>` | Όνομα πίνακα | Ναι | Κανένα | Ο πίνακας εισαγωγής. |
| `<field_list>` | Λίστα πεδίων | Όχι | Όλα τα πεδία | Ποια πεδία θα πάρουν ρητές τιμές. |
| `<value_list>` | Λίστα τιμών | Ναι | Κανένα | Οι τιμές που θα εισαχθούν. |

### Παραδείγματα

```sql
INSERT INTO ACTORS VALUES ('A02', 'Angelina Jolie', '1975-06-04', 'California', NULL);
INSERT INTO ACTORS VALUES ('A03', 'Leonardo DiCaprio', '1974-11-11', 'Los Angeles', NULL);
INSERT INTO ACTORS VALUES ('A04', 'Morgan Freeman', '1937-06-01', 'Tennessee', NULL);
INSERT INTO ACTORS VALUES ('A05', 'Meryl Streep', '1949-06-22', 'New Jersey', NULL);
```

```text
Εισάγονται τέσσερις διαφορετικές γραμμές στον πίνακα ACTORS, μία ανά εντολή INSERT.
```

```sql
INSERT INTO ACTORS (ID, NAME) VALUES ('A06', 'George Clooney');
```

```text
Εισάγεται νέα γραμμή όπου τα υπόλοιπα πεδία παίρνουν την τιμή NULL.
```

---

## 7. UPDATE και DELETE

### 7.1 UPDATE

#### Syntax Reference

```sql
UPDATE <table_name>
SET <field_name> = <new_value>
WHERE <condition>;
```

#### Behavioral Description

- Το `SET` δηλώνει ποια αλλαγή θέλουμε.
- Το `WHERE` δηλώνει σε ποιες γραμμές θα εφαρμοστεί.
- Αν παραλειφθεί το `WHERE`, η αλλαγή εφαρμόζεται σε όλες τις γραμμές του πίνακα.

#### Example

```sql
UPDATE ACTORS
SET BIRTHDATE = '1968-08-15'
WHERE ID = 'A01';
```

```text
Ενημερώνεται η ημερομηνία γέννησης μόνο του ηθοποιού με ID A01.
```

### 7.2 DELETE

#### Syntax Reference

```sql
DELETE FROM <table_name>
WHERE <condition>;
```

#### Behavioral Description

- Διαγράφει όσες γραμμές ικανοποιούν τη συνθήκη.
- Αν παραλειφθεί το `WHERE`, διαγράφονται όλες οι γραμμές.
- Ο πίνακας συνεχίζει να υπάρχει, αλλά μένει κενός.

#### Example

```sql
DELETE FROM ACTORS
WHERE ID = 'A01';
```

```text
Διαγράφεται μόνο η γραμμή του ηθοποιού με ID A01.
```

```sql
DELETE FROM ACTORS;
```

```text
Διαγράφονται όλες οι γραμμές του πίνακα ACTORS, αλλά ο πίνακας παραμένει στη βάση.
```

---

## 8. Common Errors and Gotchas

### 8.1 Παράλειψη `WHERE` σε `UPDATE`

**Σφάλμα:**

```sql
UPDATE ACTORS
SET BIRTHDATE = '1968-08-15';
```

**Τι συμβαίνει:** αλλάζει η ημερομηνία γέννησης σε όλες τις εγγραφές.

**Αντιμετώπιση:** πάντα έλεγχος ότι υπάρχει σωστή συνθήκη `WHERE` πριν την εκτέλεση.

### 8.2 Παράλειψη `WHERE` σε `DELETE`

**Σφάλμα:**

```sql
DELETE FROM ACTORS;
```

**Τι συμβαίνει:** σβήνονται όλα τα δεδομένα του πίνακα.

**Αντιμετώπιση:** πρώτα δοκιμή της συνθήκης με `SELECT`, μετά `DELETE`.

### 8.3 Εισαγωγή άκυρου ξένου κλειδιού

**Σφάλμα:** εισαγωγή εγγραφής σε `STARS` με `ID` ή `TITLE` που δεν υπάρχει ήδη.

**Τι συμβαίνει:** η εισαγωγή απορρίπτεται λόγω παραβίασης αναφορικής ακεραιότητας.

**Αντιμετώπιση:** πρώτα εισαγωγή στον γονικό πίνακα (`ACTORS` ή `MOVIES`), μετά στον `STARS`.

### 8.4 Μη παροχή τιμής σε `NOT NULL` πεδίο

**Σφάλμα:** εισαγωγή γραμμής χωρίς τιμή στο `NAME` του `ACTORS`.

**Τι συμβαίνει:** η εντολή αποτυγχάνει επειδή το πεδίο έχει περιορισμό `NOT NULL`.

**Αντιμετώπιση:** πάντα έλεγχος των περιορισμών πριν το `INSERT`.

---

## Solved Exercises

### Exercise 1: Δημιουργία και επιλογή βάσης

**Problem:** Να δημιουργηθεί η βάση `Hollywood` και να οριστεί ως ενεργή.

**Solution:**

1. Δημιουργούμε τη βάση με `CREATE DATABASE`.
2. Την ενεργοποιούμε με `USE`.

```sql
CREATE DATABASE Hollywood;
USE Hollywood;
```

```text
Η βάση Hollywood δημιουργείται και επιλέγεται ως ενεργή βάση εργασίας.
```

### Exercise 2: Δημιουργία πίνακα ηθοποιών

**Problem:** Να δημιουργηθεί ο πίνακας `ACTORS` με πρωτεύον κλειδί το `ID` και υποχρεωτικό το `NAME`.

**Solution:**

1. Ορίζουμε τα πεδία του πίνακα.
2. Βάζουμε `NOT NULL` στο `NAME`.
3. Ορίζουμε `PRIMARY KEY (ID)`.

```sql
CREATE TABLE ACTORS (
    ID varchar(10),
    NAME varchar(20) NOT NULL,
    BIRTHDATE date,
    BIRTHPLACE varchar(20),
    OSCARS int,
    PRIMARY KEY (ID)
);
```

```text
Ο πίνακας δημιουργείται και κάθε ηθοποιός ταυτοποιείται μοναδικά από το ID.
```

### Exercise 3: Δημιουργία πίνακα ταινιών

**Problem:** Να δημιουργηθεί ο πίνακας `MOVIES` με πρωτεύον κλειδί το `TITLE`.

**Solution:**

1. Ορίζουμε τα πέντε πεδία του πίνακα.
2. Θέτουμε πρωτεύον κλειδί στο `TITLE`.

```sql
CREATE TABLE MOVIES (
    TITLE varchar(50),
    YEAR date,
    DIRECTOR varchar(50),
    BUDGET int,
    TICKETS int,
    PRIMARY KEY (TITLE)
);
```

```text
Ο πίνακας MOVIES δημιουργείται με μοναδικό αναγνωριστικό τον τίτλο.
```

### Exercise 4: Δημιουργία πίνακα συσχέτισης

**Problem:** Να δημιουργηθεί πίνακας `STARS` που να συνδέει ηθοποιούς και ταινίες και να αποθηκεύει τον ρόλο και την αμοιβή.

**Solution:**

1. Χρειαζόμαστε πεδία `ID`, `TITLE`, `ROLE`, `CACHE`.
2. Το `ID` θα αναφέρεται στο `ACTORS(ID)`.
3. Το `TITLE` θα αναφέρεται στο `MOVIES(TITLE)`.
4. Για να μην υπάρχουν διπλές συμμετοχές για το ίδιο ζεύγος, ορίζουμε σύνθετο πρωτεύον κλειδί `(ID, TITLE)`.

```sql
CREATE TABLE STARS (
    ID VARCHAR(10),
    TITLE VARCHAR(50),
    ROLE VARCHAR(30),
    CACHE REAL,
    PRIMARY KEY (ID, TITLE),
    FOREIGN KEY (ID) REFERENCES ACTORS(ID),
    FOREIGN KEY (TITLE) REFERENCES MOVIES(TITLE)
);
```

```text
Ο πίνακας STARS δημιουργείται ως πίνακας συσχέτισης πολλών-προς-πολλά.
```

### Exercise 5: Προσθήκη και αλλαγή τύπου πεδίου

**Problem:** Να προστεθεί η στήλη `DURATION` στον πίνακα `MOVIES` και στη συνέχεια να αλλάξει ο τύπος της σε `int`.

**Solution:**

1. Αρχικά προσθέτουμε τη στήλη ως `varchar(6)`.
2. Μετά τη μετατρέπουμε σε `int`.
3. Ενδιάμεση κατάσταση: ο πίνακας έχει πλέον τη στήλη `DURATION`, αλλά αρχικά είναι συμβολοσειρά.
4. Τελική κατάσταση: η `DURATION` αποθηκεύει ακέραια λεπτά.

```sql
ALTER TABLE MOVIES ADD DURATION varchar(6);
ALTER TABLE MOVIES MODIFY DURATION int;
```

```text
Πρώτα προστίθεται η στήλη DURATION και στη συνέχεια αλλάζει ο τύπος της σε int.
```

### Exercise 6: Εισαγωγή πλήρους εγγραφής

**Problem:** Να εισαχθεί ο ηθοποιός Angelina Jolie με πλήρη στοιχεία, εκτός από τα Oscar που θα είναι άγνωστα.

**Solution:**

1. Χρησιμοποιούμε πλήρη μορφή `INSERT INTO ... VALUES (...)`.
2. Δίνουμε τιμή σε όλα τα πεδία με τη σωστή σειρά.
3. Για άγνωστο πλήθος Oscar, βάζουμε `NULL`.

```sql
INSERT INTO ACTORS VALUES ('A02', 'Angelina Jolie', '1975-06-04', 'California', NULL);
```

```text
Η εγγραφή της Angelina Jolie προστίθεται στον πίνακα ACTORS.
```

### Exercise 7: Εισαγωγή μερικών πεδίων

**Problem:** Να εισαχθεί ο George Clooney δίνοντας μόνο `ID` και `NAME`.

**Solution:**

1. Χρησιμοποιούμε τη μορφή `INSERT INTO <table> (<fields>) VALUES (...)`.
2. Δηλώνουμε μόνο τα πεδία που έχουν διαθέσιμες τιμές.
3. Τα υπόλοιπα πεδία παίρνουν `NULL`.

```sql
INSERT INTO ACTORS (ID, NAME) VALUES ('A06', 'George Clooney');
```

```text
Η εγγραφή προστίθεται και τα BIRTHDATE, BIRTHPLACE, OSCARS γίνονται NULL.
```

### Exercise 8: Ενημέρωση συγκεκριμένης εγγραφής

**Problem:** Να αλλάξει η ημερομηνία γέννησης του ηθοποιού με `ID = 'A01'` σε `1968-08-15`.

**Solution:**

1. Επιλέγουμε τον πίνακα `ACTORS`.
2. Με `SET` ορίζουμε τη νέα τιμή.
3. Με `WHERE ID = 'A01'` περιορίζουμε την αλλαγή σε μία μόνο γραμμή.

```sql
UPDATE ACTORS
SET BIRTHDATE = '1968-08-15'
WHERE ID = 'A01';
```

```text
Ενημερώνεται μόνο η εγγραφή με πρωτεύον κλειδί A01.
```

### Exercise 9: Διαγραφή συγκεκριμένης εγγραφής

**Problem:** Να διαγραφεί ο ηθοποιός με `ID = 'A01'`.

**Solution:**

1. Χρησιμοποιούμε `DELETE FROM ACTORS`.
2. Περιορίζουμε τη διαγραφή με `WHERE ID = 'A01'`.
3. Άρα επηρεάζεται μία μόνο εγγραφή.

```sql
DELETE FROM ACTORS
WHERE ID = 'A01';
```

```text
Η γραμμή του ηθοποιού A01 αφαιρείται από τον πίνακα ACTORS.
```

### Exercise 10: Επικίνδυνη καθολική διαγραφή

**Problem:** Τι συμβαίνει αν εκτελεστεί η εντολή `DELETE FROM ACTORS;` χωρίς `WHERE`;

**Solution:**

1. Η εντολή δεν περιέχει συνθήκη φιλτραρίσματος.
2. Άρα η διαγραφή εφαρμόζεται σε όλες τις γραμμές.
3. Ενδιάμεση λογική: ο πίνακας παραμένει ορισμένος στο σχήμα της βάσης, αλλά το περιεχόμενό του μηδενίζεται.
4. Τελικό αποτέλεσμα: δεν υπάρχει καμία εγγραφή στον `ACTORS`.

```sql
DELETE FROM ACTORS;
```

```text
Όλες οι εγγραφές του ACTORS διαγράφονται, αλλά ο πίνακας συνεχίζει να υπάρχει.
```

---

## Exam Tip: Αναγνώριση τύπου εντολής

- Αν αλλάζει το σχήμα της βάσης ή ενός πίνακα, σκέψου `CREATE`, `DROP`, `ALTER`.
- Αν αλλάζουν τα ίδια τα δεδομένα, σκέψου `INSERT`, `UPDATE`, `DELETE`.
- Σε `UPDATE` και `DELETE`, η πιο συχνή παγίδα εξετάσεων είναι η παράλειψη του `WHERE`.
- Σε σχέσεις πολλών-προς-πολλά, συνήθως χρειάζεται ενδιάμεσος πίνακας με δύο ξένα κλειδιά και συχνά σύνθετο πρωτεύον κλειδί.
