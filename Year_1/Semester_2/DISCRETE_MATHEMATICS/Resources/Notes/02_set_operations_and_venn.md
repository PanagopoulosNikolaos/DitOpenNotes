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
    subgraph U ["Καθολικό Σύνολο U = {1, 2, 3, 4, 5}"]
        subgraph A ["Σύνολο A = {1, 2}"]
            a1[1]
            a2[2]
        end
        
        c3[3]
        c4[4] 
        c5[5]
    end
    
    subgraph Legend ["Υπόμνημα"]
        L1["Σύνολο A"]
        L2["Συμπλήρωμα A' = {3, 4, 5}"]
    end
    
    style U fill:#1e293b,stroke:#38bdf8,stroke-width:1px,color:#f8fafc
    style A fill:#1e3a5f,stroke:#60a5fa,stroke-width:1px,color:#93c5fd
    style a1 fill:#0f172a,stroke:#60a5fa,color:#f8fafc
    style a2 fill:#0f172a,stroke:#60a5fa,color:#f8fafc
    style c3 fill:#0f172a,stroke:#34d399,color:#f8fafc
    style c4 fill:#0f172a,stroke:#34d399,color:#f8fafc  
    style c5 fill:#0f172a,stroke:#34d399,color:#f8fafc
    style Legend fill:#1e293b,stroke:#475569,stroke-width:1px,color:#f8fafc
    style L1 fill:#1e3a5f,stroke:#60a5fa,stroke-width:2px,color:#f8fafc
    style L2 fill:#064e3b,stroke:#34d399,stroke-width:2px,color:#f8fafc

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
    
    style Venn fill:#0f172a,stroke:#334155,stroke-width:2px,color:#f8fafc
    style SetA fill:#1e293b,stroke:#3b82f6,stroke-width:2px,color:#93c5fd
    style SetB fill:#1e293b,stroke:#a855f7,stroke-width:2px,color:#d8b4fe
    style Overlap fill:#064e3b,stroke:#10b981,stroke-width:2px,color:#6ee7b7
    style a1 fill:#0f172a,stroke:#3b82f6,color:#f8fafc
    style a2 fill:#0f172a,stroke:#3b82f6,color:#f8fafc
    style b4 fill:#0f172a,stroke:#a855f7,color:#f8fafc
    style b5 fill:#0f172a,stroke:#a855f7,color:#f8fafc
    style common fill:#047857,stroke:#34d399,stroke-width:2px,color:#ffffff

```
### 4. Ένωση ($A \cup B$)
- **Ορισμός**: Όλα τα στοιχεία από οποιοδήποτε σύνολο (ή και από τα δύο)
- **Τύπος**: $A \cup B = \{x : x \in A \text{ Ή } x \in B\}$
- **Παράδειγμα**: $\{1, 2, 3\} \cup \{3, 4, 5\} = \{1, 2, 3, 4, 5\}$
```mermaid
graph TD
    subgraph Result ["Ένωση: A ∪ B = {1, 2, 3, 4, 5}"]
        subgraph OnlyA ["Μόνο στο A"]
            ua1[1]
            ua2[2]
        end
        
        subgraph Both ["Και στα δύο A & B"]
            ub3[3]
        end
        
        subgraph OnlyB ["Μόνο στο B"]
            ub4[4]
            ub5[5]
        end
    end
    
    style Result fill:#0f172a,stroke:#334155,stroke-width:2px,color:#f8fafc
    style OnlyA fill:#1e293b,stroke:#3b82f6,stroke-width:2px,color:#93c5fd
    style Both fill:#451a03,stroke:#f59e0b,stroke-width:2px,color:#fde68a
    style OnlyB fill:#1e293b,stroke:#a855f7,stroke-width:2px,color:#d8b4fe
    style ua1 fill:#0f172a,stroke:#3b82f6,color:#f8fafc
    style ua2 fill:#0f172a,stroke:#3b82f6,color:#f8fafc
    style ub3 fill:#0f172a,stroke:#f59e0b,color:#f8fafc
    style ub4 fill:#0f172a,stroke:#a855f7,color:#f8fafc
    style ub5 fill:#0f172a,stroke:#a855f7,color:#f8fafc

```
### 5. Διαφορά ($A - B$ ή $A \setminus B$)
- **Ορισμός**: Στοιχεία στο $A$ αλλά όχι στο $B$
- **Τύπος**: $A - B = \{x : x \in A \text{ ΚΑΙ } x \notin B\}$
- **Παράδειγμα**: $\{1, 2, 3\} - \{3, 4, 5\} = \{1, 2\}$
```mermaid
graph TD
    subgraph Operation ["A - B: Αφαίρεση στοιχείων του B από το A"]
        subgraph Original ["Αρχικό Σύνολο A = {1, 2, 3}"]
            subgraph Keep ["Διατήρηση (όχι στο B)"]
                k1[1]
                k2[2]
            end
            
            subgraph Remove ["Αφαίρεση (επίσης στο B)"]
                r3[3]
            end
        end
        
        subgraph Result ["Αποτέλεσμα: A - B = {1, 2}"]
            res1[1]
            res2[2]
        end
    end
    
    Keep --> Result
    style Operation fill:#0f172a,stroke:#334155,stroke-width:2px,color:#f8fafc
    style Original fill:#1e293b,stroke:#475569,stroke-width:1px,color:#e2e8f0
    style Keep fill:#064e3b,stroke:#10b981,stroke-width:2px,color:#a7f3d0
    style Remove fill:#4c0519,stroke:#f43f5e,stroke-width:2px,stroke-dasharray: 5 5,color:#fecdd3
    style Result fill:#064e3b,stroke:#34d399,stroke-width:3px,color:#a7f3d0
    style k1 fill:#0f172a,stroke:#10b981,color:#f8fafc
    style k2 fill:#0f172a,stroke:#10b981,color:#f8fafc
    style r3 fill:#0f172a,stroke:#f43f5e,color:#f8fafc
    style res1 fill:#0f172a,stroke:#34d399,color:#f8fafc
    style res2 fill:#0f172a,stroke:#34d399,color:#f8fafc

```
## Οπτικές Αναπαραστάσεις

```mermaid
graph TD
    subgraph Summary ["Οπτική Σύνοψη Πράξεων Συνόλων"]
        subgraph Row1 ["Βασικές Πράξεις"]
            A1["Σύνολο A<br/>{1,2,3}"]
            B1["Σύνολο B<br/>{3,4,5}"]
        end
        
        subgraph Row2 ["Αποτελέσματα"]
            Int["A ∩ B<br/>{3}"]
            Union["A ∪ B<br/>{1,2,3,4,5}"]
            Diff["A - B<br/>{1,2}"]
        end
    end
    
    A1 --> Int
    B1 --> Int
    A1 --> Union
    B1 --> Union
    A1 --> Diff
    
    style Summary fill:#0f172a,stroke:#334155,stroke-width:2px,color:#f8fafc
    style Row1 fill:#1e293b,stroke:#475569,stroke-width:1px,color:#e2e8f0
    style Row2 fill:#1e293b,stroke:#475569,stroke-width:1px,color:#e2e8f0
    style A1 fill:#1e3a5f,stroke:#3b82f6,stroke-width:2px,color:#f8fafc
    style B1 fill:#3b1d4a,stroke:#a855f7,stroke-width:2px,color:#f8fafc
    style Int fill:#064e3b,stroke:#10b981,stroke-width:2px,color:#f8fafc
    style Union fill:#451a03,stroke:#f59e0b,stroke-width:2px,color:#f8fafc
    style Diff fill:#4c0519,stroke:#f43f5e,stroke-width:2px,color:#f8fafc

```

```mermaid
graph LR
    subgraph Summary2 ["Παραδείγματα Πράξεων Συνόλων"]
        subgraph SetA2 ["A = {1, 2, 3}"]
            A1[1] 
            A2[2]
            A3[3]
        end
        subgraph SetB2 ["B = {3, 4, 5}"]
            B3[3]
            B4[4]
            B5[5]
        end
    end
    
    subgraph Results2 ["Αποτελέσματα"]
        Int2["A ∩ B = {3}"]
        Union2["A ∪ B = {1, 2, 3, 4, 5}"]
        Diff2["A - B = {1, 2}"]
    end
    
    style Summary2 fill:#0f172a,stroke:#334155,stroke-width:2px,color:#f8fafc
    style SetA2 fill:#1e293b,stroke:#3b82f6,stroke-width:2px,color:#93c5fd
    style SetB2 fill:#1e293b,stroke:#a855f7,stroke-width:2px,color:#d8b4fe
    style Results2 fill:#0f172a,stroke:#334155,stroke-width:2px,color:#f8fafc
    style A1 fill:#0f172a,stroke:#3b82f6,color:#f8fafc
    style A2 fill:#0f172a,stroke:#3b82f6,color:#f8fafc
    style A3 fill:#0f172a,stroke:#3b82f6,color:#f8fafc
    style B3 fill:#0f172a,stroke:#a855f7,color:#f8fafc
    style B4 fill:#0f172a,stroke:#a855f7,color:#f8fafc
    style B5 fill:#0f172a,stroke:#a855f7,color:#f8fafc
    style Int2 fill:#064e3b,stroke:#10b981,stroke-width:2px,color:#f8fafc
    style Union2 fill:#451a03,stroke:#f59e0b,stroke-width:2px,color:#f8fafc
    style Diff2 fill:#4c0519,stroke:#f43f5e,stroke-width:2px,color:#f8fafc
```

## Ασκήσεις Εμπέδωσης & Αναλυτικές Λύσεις

**Δεδομένα Συνόλων:**
- $U = \{1, 2, 3, \dots, 20\}$ (Καθολικό σύνολο θετικών ακεραίων $\leq 20$)
- $A = \{1, 3, 5, 7, 9\}$ (Περιττοί αριθμοί $< 10$)
- $B = \{4, 8, 12, 16\}$ (Πολλαπλάσια του 4 στο $U$)
- $C = \{1, 4, 9, 16\}$ (Τέλεια τετράγωνα στο $U$)

---

### **1. Υπολογισμός $A \cup B$**
- **Ερώτημα**: Βρείτε την ένωση των συνόλων $A$ και $B$.
- **Βήμα 1 (Ορισμός)**: Η ένωση περιλαμβάνει όλα τα στοιχεία που ανήκουν είτε στο $A$ είτε στο $B$ (ή και στα δύο), χωρίς επαναλήψεις.
- **Βήμα 2 (Συνδυασμός στοιχείων)**:
  - Στοιχεία του $A$: $\{1, 3, 5, 7, 9\}$
  - Στοιχεία του $B$: $\{4, 8, 12, 16\}$
  - Δεν υπάρχουν κοινά στοιχεία ($A \cap B = \emptyset$).
- **Τελική Λύση**:
  $$A \cup B = \{1, 3, 4, 5, 7, 8, 9, 12, 16\}$$

---

### **2. Υπολογισμός $C \cap B$**
- **Ερώτημα**: Βρείτε την τομή των συνόλων $C$ και $B$.
- **Βήμα 1 (Ορισμός)**: Η τομή περιέχει μόνο τα κοινά στοιχεία που ανήκουν ταυτόχρονα και στο $C$ και στο $B$.
- **Βήμα 2 (Έλεγχος στοιχείων)**:
  - $C = \{1, \mathbf{4}, 9, \mathbf{16}\}$
  - $B = \{\mathbf{4}, 8, 12, \mathbf{16}\}$
  - Τα κοινά στοιχεία είναι το 4 και το 16.
- **Τελική Λύση**:
  $$C \cap B = \{4, 16\}$$

---

### **3. Υπολογισμός $C - B$ (ή $C \setminus B$)**
- **Ερώτημα**: Βρείτε τη διαφορά του συνόλου $B$ από το σύνολο $C$.
- **Βήμα 1 (Ορισμός)**: Η διαφορά $C - B$ περιέχει τα στοιχεία που ανήκουν στο $C$ αλλά ΔΕΝ ανήκουν στο $B$.
- **Βήμα 2 (Αφαίρεση κοινών στοιχείων)**:
  - Ξεκινάμε με το $C = \{1, 4, 9, 16\}$.
  - Αφαιρούμε τα στοιχεία που υπάρχουν και στο $B$: αφαιρούμε το 4 και το 16.
  - Απομένουν τα στοιχεία 1 και 9.
- **Τελική Λύση**:
  $$C - B = \{1, 9\}$$

---

### **4. Υπολογισμός $\emptyset \cap B$**
- **Ερώτημα**: Βρείτε την τομή του κενού συνόλου με το $B$.
- **Βήμα 1 (Ορισμός)**: Η τομή απαιτεί στοιχεία που ανήκουν ταυτόχρονα στο $\emptyset$ και στο $B$.
- **Βήμα 2 (Ιδιότητα)**: Επειδή το κενό σύνολο $\emptyset$ δεν περιέχει κανένα στοιχείο, δεν υπάρχει κανένα κοινό στοιχείο με οποιοδήποτε σύνολο.
- **Τελική Λύση**:
  $$\emptyset \cap B = \emptyset$$

---

### **5. Υπολογισμός $\overline{A}$ (Συμπλήρωμα του $A$)**
- **Ερώτημα**: Βρείτε το συμπλήρωμα του συνόλου $A$ ως προς το καθολικό σύνολο $U$.
- **Βήμα 1 (Ορισμός)**: $\overline{A} = U - A = \{x \in U : x \notin A\}$.
- **Βήμα 2 (Αφαίρεση στοιχείων του $A$ από το $U$)**:
  - $U = \{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20\}$
  - Αφαιρούμε τα στοιχεία $A = \{1, 3, 5, 7, 9\}$.
- **Τελική Λύση**:
  $$\overline{A} = \{2, 4, 6, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20\}$$

---

### **6. Υπολογισμός $(A \cup C) \cap B$**
- **Ερώτημα**: Υπολογίστε την έκφραση $(A \cup C) \cap B$.
- **Βήμα 1 (Υπολογισμός παρένθεσης $A \cup C$)**:
  - $A = \{1, 3, 5, 7, 9\}$, $C = \{1, 4, 9, 16\}$
  - $A \cup C = \{1, 3, 4, 5, 7, 9, 16\}$
- **Βήμα 2 (Τομή με το $B$)**:
  - $B = \{4, 8, 12, 16\}$
  - Εξετάζουμε ποια στοιχεία του $\{1, 3, \mathbf{4}, 5, 7, 9, \mathbf{16}\}$ ανήκουν και στο $\{\mathbf{4}, 8, 12, \mathbf{16}\}$.
  - Κοινά στοιχεία: 4 και 16.
- **Τελική Λύση**:
  $$(A \cup C) \cap B = \{4, 16\}$$

---

### **7. Υπολογισμός $A - (B \cup C)$**
- **Ερώτημα**: Υπολογίστε την έκφραση $A - (B \cup C)$.
- **Βήμα 1 (Υπολογισμός παρένθεσης $B \cup C$)**:
  - $B = \{4, 8, 12, 16\}$, $C = \{1, 4, 9, 16\}$
  - $B \cup C = \{1, 4, 8, 9, 12, 16\}$
- **Βήμα 2 (Αφαίρεση από το $A$)**:
  - $A = \{1, 3, 5, 7, 9\}$
  - Αφαιρούμε όσα στοιχεία του $A$ εμφανίζονται στο $\{1, 4, 8, 9, 12, 16\}$:
    - Το 1 αφαιρείται (υπάρχει στο $B \cup C$)
    - Το 3 διατηρείται
    - Το 5 διατηρείται
    - Το 7 διατηρείται
    - Το 9 αφαιρείται (υπάρχει στο $B \cup C$)
- **Τελική Λύση**:
  $$A - (B \cup C) = \{3, 5, 7\}$$



## Βασικές Ιδιότητες

| Ιδιότητα     | Τύπος                                                | Περιγραφή                                       |
| ------------ | ------------------------------------------------------ | ------------------------------------------------- |
| Αντιμεταθετική  | $A \cup B = B \cup A$                                  | Η σειρά δεν έχει σημασία                              |
| Προσεταιριστική  | $(A \cup B) \cup C = A \cup (B \cup C)$                | Η ομαδοποίηση δεν έχει σημασία                           |
| Επιμεριστική | $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$       | Η τομή επιμερίζεται ως προς την ένωση               |
| De Morgan  | $\overline{A \cup B} = \overline{A} \cap \overline{B}$ | Συμπλήρωμα ένωσης = τομή συμπληρωμάτων |