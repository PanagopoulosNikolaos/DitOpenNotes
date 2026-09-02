# Διάλεξη 4: Γλώσσα SQL — Ορισμός (DDL), Χειρισμός (DML) και Ερωτήματα (DQL)

## 1. Γλώσσα Ορισμού Δεδομένων (Data Definition Language - DDL)
Η DDL χρησιμοποιείται για τη δημιουργία, τροποποίηση και διαγραφή της δομής των πινάκων και των περιορισμών ακεραιότητας.

```sql
CREATE TABLE Tmima (
    tmima_id INT PRIMARY KEY,
    onoma_tmimatos VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE Kathigitis (
    kathigitis_id INT PRIMARY KEY,
    onoma VARCHAR(50) NOT NULL,
    eponymo VARCHAR(50) NOT NULL,
    misthos DECIMAL(10, 2) CHECK (misthos >= 800.00),
    tmima_id INT,
    CONSTRAINT fk_tmima FOREIGN KEY (tmima_id) 
        REFERENCES Tmima(tmima_id) 
        ON DELETE SET NULL 
        ON UPDATE CASCADE
);
```

---

## 2. Γλώσσα Χειρισμού Δεδομένων (Data Manipulation Language - DML)
- **Εισαγωγή (INSERT):**
  ```sql
  INSERT INTO Tmima (tmima_id, onoma_tmimatos) VALUES (1, 'Pliroforiki');
  INSERT INTO Kathigitis (kathigitis_id, onoma, eponymo, misthos, tmima_id)
  VALUES (101, 'Nikos', 'Papadopoulos', 2100.00, 1);
  ```
- **Ενημέρωση (UPDATE):**
  ```sql
  UPDATE Kathigitis SET misthos = misthos * 1.05 WHERE tmima_id = 1;
  ```
- **Διαγραφή (DELETE):**
  ```sql
  DELETE FROM Kathigitis WHERE kathigitis_id = 101;
  ```

---

## 3. Σύνταξη Ερωτημάτων Ανάκτησης (SELECT - DQL)

### Βασική Δομή Ερωτήματος:
```sql
SELECT K.eponymo, K.misthos, T.onoma_tmimatos
FROM Kathigitis K
JOIN Tmima T ON K.tmima_id = T.tmima_id
WHERE K.misthos > 1800.00
ORDER BY K.misthos DESC;
```

### Ομαδοποίηση και Συναρτήσεις Συνάθροισης (GROUP BY & HAVING)
- Συναρτήσεις: `COUNT()`, `SUM()`, `AVG()`, `MIN()`, `MAX()`.
- Ο όρος `WHERE` φιλτράρει μεμονωμένες εγγραφές πριν την ομαδοποίηση.
- Ο όρος `HAVING` φιλτράρει τις ομάδες μετά την ομαδοποίηση.

```sql
SELECT T.onoma_tmimatos, COUNT(K.kathigitis_id) AS synolo_didaskonton, AVG(K.misthos) AS mesos_misthos
FROM Tmima T
JOIN Kathigitis K ON T.tmima_id = K.tmima_id
GROUP BY T.tmima_id, T.onoma_tmimatos
HAVING COUNT(K.kathigitis_id) >= 2;
```

### Εμφωλευμένα Ερωτήματα (Subqueries)
```sql
SELECT onoma, eponymo, misthos
FROM Kathigitis
WHERE misthos > (SELECT AVG(misthos) FROM Kathigitis);
```

