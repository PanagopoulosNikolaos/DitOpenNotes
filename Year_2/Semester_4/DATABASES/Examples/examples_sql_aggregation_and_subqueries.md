# Παραδείγματα: Συναθροίσεις και Υποερωτήματα σε SQL

## Παράδειγμα 1: Σύνθετη Ανάλυση Μισθοδοσίας με Παράθυρα (Window Functions)

### Πρόβλημα:
Έστω ο πίνακας υπαλλήλων `Ypalliloi(ypallilos_id, onoma, tmima, misthos)`.
Ζητείται να γραφεί ερώτημα SQL που υπολογίζει για κάθε υπάλληλο:
1. Το όνομα και το τμήμα του.
2. Τον μισθό του.
3. Τον μέσο μισθό του τμήματός του.
4. Τη διαφορά του μισθού του από τον μέσο όρο του τμήματος.
5. Την κατάταξη του μισθού του μέσα στο τμήμα του (Rank).

### Λύση με χρήση SQL Window Functions:
```sql
SELECT 
    onoma,
    tmima,
    misthos,
    ROUND(AVG(misthos) OVER (PARTITION BY tmima), 2) AS mesos_orou_tmimatos,
    ROUND(misthos - AVG(misthos) OVER (PARTITION BY tmima), 2) AS diafora,
    DENSE_RANK() OVER (PARTITION BY tmima ORDER BY misthos DESC) AS katataksi_tmimatos
FROM Ypalliloi
ORDER BY tmima, katataksi_tmimatos;
```

---

## Παράδειγμα 2: Εύρεση του "Δεύτερου Υψηλότερου" χωρίς Window Functions

### Πρόβλημα:
Βρείτε τον 2ο υψηλότερο μισθό στον πίνακα `Ypalliloi` με χρήση κλασικού υποερωτήματος:

### Λύση:
```sql
SELECT MAX(misthos) AS second_highest_salary
FROM Ypalliloi
WHERE misthos < (SELECT MAX(misthos) FROM Ypalliloi);
```

