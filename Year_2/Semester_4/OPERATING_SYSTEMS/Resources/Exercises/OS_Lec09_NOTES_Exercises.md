# Ασκήσεις — Δρομολόγηση Διεργασιών (CPU Scheduling)

**Βασισμένες σε:** `OS_Lec09_NOTES.md`  
**Αριθμός ασκήσεων:** 38

---

## Μέρος Α — Θεωρία

### Άσκηση 1
Ορίστε: turnaround time, waiting time, response time, throughput, CPU utilization.

---

### Άσκηση 2
Διακρίνετε long-term, medium-term, short-term scheduling.

---

### Άσκηση 3
Διακρίνετε preemptive και non-preemptive scheduling. Ποια αλγόριθμοι ανήκουν σε κάθε κατηγορία;

---

### Άσκηση 4
Τι είναι CPU-I/O burst cycle; Γιατί επηρεάζει τη δρομολόγηση;

---

### Άσκηση 5
Εξηγήστε priority scheduling και το πρόβλημα starvation. Τι είναι aging;

---

### Άσκηση 6
Συγκρίνετε FCFS, SJF, SRTF, Round Robin (preemption, starvation, use case).

---

### Άσκηση 7
Τι είναι time quantum στο RR; Ποια τα trade-offs μικρού vs μεγάλου quantum;

---

### Άσκηση 8
Γιατί το RR ευνοεί CPU-bound έναντι I/O-bound; Τι είναι Virtual Round Robin;

---

### Άσκηση 9
Γιατί το SJF είναι βέλτιστο για μέσο waiting time αλλά δύσκολο στην πράξη;

---

### Άσκηση 10
Δώστε τον τύπο εκθετικού μέσου για εκτίμηση CPU burst: $\tau_{n+1} = \alpha t_n + (1-\alpha)\tau_n$.

---

## Μέρος Β — Υπολογιστικές Ασκήσεις (Άφιξη t=0)

### Άσκηση 11
**FCFS**

Διεργασίες P1–P5, burst: P1=1, P2=3, P3=4, P4=3, P5=1 (άφιξη 0, σειρά P1..P5).

(α) Συμπληρώστε διάγραμμα Gantt.  
(β) Υπολογίστε turnaround, waiting, response για καθεμία.  
(γ) Μέσος waiting time.

---

### Άσκηση 12
**SJF (non-preemptive)** — ίδιο σύνολο διεργασιών με Άσκηση 11.

(α) Διάγραμμα Gantt.  
(β) Response times.  
(γ) Μέσος response time.

---

### Άσκηση 13
**Round Robin, q=2** — ίδιο σύνολο.

(α) Διάγραμμα Gantt (ανά ms).  
(β) Ουρά αναμονής ανά χρονική στιγμή (όπως στο 2023 exam).  
(γ) Waiting times και μέσος waiting time.

---

### Άσκηση 14
**Round Robin, q=1** — ίδιο σύνολο. Συγκρίνετε context switches με q=2.

---

### Άσκηση 15
**SRTF** — bursts P1=8, P2=4, P3=9, P4=5, άφιξη t=0.

Διάγραμμα Gantt και waiting times.

---

## Μέρος Γ — Διαφορετικοί Χρόνοι Άφιξης

### Άσκηση 16
P1 burst=8 (t=0), P2 burst=4 (t=1), P3 burst=9 (t=2), P4 burst=5 (t=3).

(α) SJF non-preemptive — Gantt.  
(β) SRTF — Gantt.  
(γ) Συγκρίνετε waiting times P1.

---

### Άσκηση 17
Με δεδομένα Άσκησης 16, RR με q=3. Υπολογίστε response time της P2.

---

### Άσκηση 18
4 διεργασίες: P1(24), P2(3), P3(3), άφιξη 0. FCFS vs SJF — πίνακας waiting times.

---

### Άσκηση 19
P1(10,t=0), P2(1,t=1), P3(2,t=2). SRTF: πόσες preemptions; Τελικός μέσος waiting;

---

## Μέρος Δ — Σύγκριση και Ανάλυση

### Άσκηση 20
Σημειώστε **Σ** ή **Λ**:

1. Το FCFS είναι preemptive.
2. Το SJF δίνει ελάχιστο μέσο waiting time για δεδομένο σύνολο.
3. Το RR δεν προκαλεί starvation.
4. Όταν όλες οι διεργασίες φτάνουν ταυτόχρονα, SRTF = SJF.
5. Μεγάλο quantum στο RR το καθιστά παρόμοιο με FCFS.

---

### Άσκηση 21
Κυκλώστε τη σωστή απάντηση: Ποιος αλγόριθμος είναι κατάλληλος για interactive time-sharing;

- α) FCFS  
- β) SJF  
- γ) Round Robin  
- δ) Batch priority

---

### Άσκηση 22
Γιατί το context switch overhead αυξάνεται με μικρό quantum στο RR;

---

### Άσκηση 23
**Βελτιστοποίηση:** RR με q=100ms, bursts 5ms. Τι πρόβλημα παρατηρείτε;

---

### Άσκηση 24
Υπολογίστε $\tau_3$ αν $\alpha=0.5$, $t_1=10$, $t_2=6$, $\tau_1=\tau_2=8$.

---

### Άσκηση 25
Συμπληρώστε πίνακα:

| Algorithm | Preemptive | Starvation | Min avg waiting |
| :--- | :--- | :--- | :--- |
| FCFS | | | |
| SJF | | | |
| SRTF | | | |
| RR | | | |

---

### Άσκηση 26
**Σενάριο 2023 exam:** P1=1, P2=3, P3=4, P4=3, P5=1, SJF. Επαληθεύστε: response times 0,2,8,5,1 και μέσος 3.2 ms.

---

### Άσκηση 27
**Σενάριο 2023 exam:** ίδιες διεργασίες, RR q=2. Επαληθεύστε waiting times και μέσο 5.8 ms.

---

### Άσκηση 28
Waiting time = Completion - Arrival - Burst. Δείξτε τον υπολογισμό για P2 στο RR q=2 (Άσκηση 13).

---

### Άσκηση 29
Response time = χρόνος πρώτης εκτέλεσης - arrival. Διαφορά από waiting time;

---

### Άσκηση 30
5 διεργασίες, bursts 10,1,2,1,1. SJF. Ποια διεργασία παθαίνει starvation αν συνεχώς φτάνουν νέες με burst 1;

---

### Άσκηση 31
Priority: P1(prio 3, burst 10), P2(prio 1, burst 1), P3(prio 2, burst 2), non-preemptive. Gantt;

---

### Άσκηση 32
Πώς το aging αντιμετωπίζει starvation σε priority scheduling;

---

### Άσκηση 33
**Exam tip:** Συνηθισμένα λάθη — (α) ξεχνούν preemption στο SRTF, (β) λάθος ουρά στο RR. Δώστε παράδειγμα για καθένα.

---

### Άσκηση 34
8 διεργασίες, burst 6,8,7,3, μόνο αυτές 4. FCFS vs SJF — ποια έχει μικρότερο $\sum$ waiting;

---

### Άσκηση 35
RR q=4, bursts 24,3,3. Πόσες φορές η P2 μπαίνει στην ουρά; Συγκρίνετε με FCFS για response της P2.

---

### Άσκηση 36
Επιλέξτε κατάλληλο αλγόριθμο: (α) batch overnight jobs, (β) web server, (γ) real-time hard deadlines, (δ) known burst times batch.

---

### Άσκηση 37
Σχεδιάστε Gantt για 3 διεργασίες RR q=2 χειροκίνητα και ελέγξτε waiting: P1(5), P2(3), P3(1).

---

### Άσκηση 38
Συνδυαστική εξέτασης: 5 διεργασίες, bursts 2,1,8,4,5, άφιξη 0.

Υπολογίστε μέσο waiting για FCFS, SJF, RR(q=2) και συγκρίνετε ποιος αλγόριθμος προτιμάται για batch vs interactive.