# Πράξεις Συνόλων & Διαγράμματα Venn

## Βασικές Έννοιες

### 1. Καθολικό Σύνολο (U)
- **Ορισμός**: Περιέχει όλα τα πιθανά στοιχεία για ένα συγκεκριμένο πλαίσιο
- **Συμβολισμός**: $U$ ή Σύμπαν (Universe)
- **Παράδειγμα**: $U = \{1, 2, 3, 4, 5\}$ (θετικοί ακέραιοι ≤ 5)

### 2. Συμπλήρωμα ($A^c$ ή $\overline{A}$)
- **Ορισμός**: Όλα τα στοιχεία στο $U$ που ΔΕΝ ανήκουν στο σύνολο $A$
- **Τύπος**: $\overline{A} = \{x \in U : x \notin A\}$
- **Παράδειγμα**: Αν $U = \{1, 2, 3, 4, 5\}$ και $A = \{1, 2\}$, τότε $\overline{A} = \{3, 4, 5\}$

### 1+2:
```mermaid
graph TD
    subgraph U [" Καθολικό Σύνολο U = {1, 2, 3, 4, 5}"]
        subgraph A ["Σύνολο A = {1, 2}"]
            style A fill:#ffcccb,stroke:#ff6b6b,stroke-width:3px
            a1[1]
            a2[2]
        end
        
        c3[3]
        c4[4] 
        c5[5]
    end
    
    subgraph Legend [" "]
        L1[" Σύνολο A"]
        L2[" Συμπλήρωμα A' = {3, 4, 5}"]
    end
    
    style U fill:#f0f8ff,stroke:#4682b4,stroke-width:2px
    style c3 fill:#f,stroke:#4caf50
    style c4 fill:#f,stroke:#4caf50  
    style c5 fill:#f,stroke:#4caf50
    style L1 fill:#f,stroke:#ff6b6b
    style L2 fill:#f,stroke:#4caf50

```
### 3. Τομή ($A \cap B$)
- **Ορισμός**: Κοινά στοιχεία και στα δύο σύνολα
- **Τύπος**: $A \cap B = \{x : x \in A \text{ ΚΑΙ } x \in B\}$
- **Παράδειγμα**: $\{1, 2, 3\} \cap \{3, 4, 5\} = \{3\}$
```mermaid
graph LR
    subgraph Venn ["Διάγραμμα Venn: A ∩ B"]
        subgraph SetA ["Σύνολο A = {1, 2, 3}"]
            a1[1]
            a2[2]
        end
        
        subgraph Overlap ["A ∩ B = {3}"]
            common[3]
        end
        
        subgraph SetB ["Σύνολο B = {3, 4, 5}"]
            b4[4]
            b5[5]
        end
    end
    
    style SetA fill:#ffebee,stroke:#e91e63,stroke-width:2px
    style SetB fill:#e3f2fd,stroke:#2196f3,stroke-width:2px
    style Overlap fill:#c8e6c9,stroke:#4caf50,stroke-width:3px
    style common fill:#81c784,stroke:#2e7d32,stroke-width:2px

```
### 4. Ένωση ($A \cup B$)
- **Ορισμός**: Όλα τα στοιχεία από οποιοδήποτε σύνολο (ή και από τα δύο)
- **Τύπος**: $A \cup B = \{x : x \in A \text{ Ή } x \in B\}$
- **Παράδειγμα**: $\{1, 2, 3\} \cup \{3, 4, 5\} = \{1, 2, 3, 4, 5\}$
```mermaid
graph TD
    subgraph Result [" Ένωση: A ∪ B = {1, 2, 3, 4, 5}"]
        subgraph OnlyA ["Μόνο στο A"]
            style OnlyA fill:#ffebee,stroke:#e91e63
            ua1[1]
            ua2[2]
        end
        
        subgraph Both ["Και στα δύο A & B"]
            style Both fill:#fff3e0,stroke:#ff9800
            ub3[3]
        end
        
        subgraph OnlyB ["Μόνο στο B"]
            style OnlyB fill:#e3f2fd,stroke:#2196f3
            ub4[4]
            ub5[5]
        end
    end

```
### 5. Διαφορά ($A - B$ ή $A \setminus B$)
- **Ορισμός**: Στοιχεία στο $A$ αλλά όχι στο $B$
- **Τύπος**: $A - B = \{x : x \in A \text{ ΚΑΙ } x \notin B\}$
- **Παράδειγμα**: $\{1, 2, 3\} - \{3, 4, 5\} = \{1, 2\}$
```mermaid
graph TD
    subgraph Operation ["A - B: Αφαίρεση στοιχείων του B από το A"]
        subgraph Original ["Αρχικό Σύνολο A = {1, 2, 3}"]
            subgraph Keep [" Διατήρηση (όχι στο B)"]
                style Keep fill:#c8e6c9,stroke:#4caf50,stroke-width:2px
                k1[1]
                k2[2]
            end
            
            subgraph Remove [" Αφαίρεση (επίσης στο B)"]
                style Remove fill:#ffcdd2,stroke:#f44336,stroke-width:2px,stroke-dasharray: 5 5
                r3[3]
            end
        end
        
        subgraph Result [" Αποτέλεσμα: A - B = {1, 2}"]
            style Result fill:#e8f5e8,stroke:#2e7d32,stroke-width:3px
            res1[1]
            res2[2]
        end
    end
    
    Keep --> Result
    style Operation fill:#f,stroke:#666

```
## Οπτικές Αναπαραστάσεις

```mermaid
graph TD
    subgraph Summary [" Οπτική Σύνοψη Πράξεων Συνόλων"]
        subgraph Row1 ["Βασικές Πράξεις"]
            A1[" Σύνολο A<br/>{1,2,3}"]
            B1[" Σύνολο B<br/>{3,4,5}"]
        end
        
        subgraph Row2 ["Αποτελέσματα"]
            Int["🟢 A ∩ B<br/>{3}"]
            Union["🟠 A ∪ B<br/>{1,2,3,4,5}"]
            Diff["🟡 A - B<br/>{1,2}"]
        end
    end
    
    A1 --> Int
    B1 --> Int
    A1 --> Union
    B1 --> Union
    A1 --> Diff
    
    style A1 fill:#ffebee,stroke:#e91e63
    style B1 fill:#e3f2fd,stroke:#2196f3
    style Int fill:#c8e6c9,stroke:#4caf50
    style Union fill:#fff3e0,stroke:#ff9800
    style Diff fill:#fff9c4,stroke:#f57f17

```

```mermaid
graph LR
    subgraph "Παραδείγματα Πράξεων Συνόλων"
        subgraph "A = {1, 2, 3}"
            A1[1] 
            A2[2]
            A3[3]
        end
        subgraph "B = {3, 4, 5}"
            B3[3]
            B4[4]
            B5[5]
        end
    end
    
    subgraph Αποτελέσματα
        Int["A ∩ B = {3}"]
        Union["A ∪ B = {1, 2, 3, 4, 5}"]
        Diff["A - B = {1, 2}"]
    end
```

## Ασκήσεις Εμπέδωσης

**Δίνονται:**
- $A = \{1, 3, 5, 7, 9\}$ (περιττοί αριθμοί < 10)
- $B = \{4, 8, 12, 16\}$ (πολλαπλάσια του 4)
- $C = \{1, 4, 9, 16\}$ (τέλεια τετράγωνα)
- $U = \{1, 2, 3, ..., 20\}$

**Υπολογίστε:**

1. $A \cup B$
2. $C \cap B$ 
3. $C - B$
4. $\emptyset \cap B$
5. $\overline{A}$ (συμπλήρωμα του A)
6. $(A \cup C) \cap B$
7. $A - (B \cup C)$


**Λεπτομέρειες**
1. **$A \cup B = \{1, 3, 4, 5, 7, 8, 9, 12, 16\}$**
   - Όλα τα μοναδικά στοιχεία και από τα δύο σύνολα

2. **$C \cap B = \{4, 16\}$**
   - Κοινά στοιχεία και στο C και στο B

3. **$C - B = \{1, 9\}$**
   - Στοιχεία στο C αλλά όχι στο B

4. **$\emptyset \cap B = \emptyset$**
   - Τομή κενού συνόλου με οποιοδήποτε σύνολο = κενό σύνολο

5. **$\overline{A} = \{2, 4, 6, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20\}$**
   - Όλα τα στοιχεία στο U που δεν ανήκουν στο A

6. **$(A \cup C) \cap B = \{4, 16\}$**
   - Πρώτα: $A \cup C = \{1, 3, 4, 5, 7, 9, 16\}$
   - Μετά τομή με το B

7. **$A - (B \cup C) = \{3, 5, 7\}$**
   - Πρώτα: $B \cup C = \{1, 4, 8, 9, 12, 16\}$
   - Στοιχεία στο A αλλά όχι στο $(B \cup C)$



## Βασικές Ιδιότητες

| Ιδιότητα     | Τύπος                                                | Περιγραφή                                       |
| ------------ | ------------------------------------------------------ | ------------------------------------------------- |
| Αντιμεταθετική  | $A \cup B = B \cup A$                                  | Η σειρά δεν έχει σημασία                              |
| Προσεταιριστική  | $(A \cup B) \cup C = A \cup (B \cup C)$                | Η ομαδοποίηση δεν έχει σημασία                           |
| Επιμεριστική | $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$       | Η τομή επιμερίζεται ως προς την ένωση               |
| De Morgan  | $\overline{A \cup B} = \overline{A} \cap \overline{B}$ | Συμπλήρωμα ένωσης = τομή συμπληρωμάτων |