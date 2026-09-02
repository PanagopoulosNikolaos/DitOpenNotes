# Εργαστηριακός Οδηγός 2: Έλεγχοι Υποθέσεων t-test και Απλή Γραμμική Παλινδρόμηση σε R

## 1. Σκοπός Εργαστηρίου
Εφαρμογή ελέγχων υποθέσεων $t$-test ενός και δύο δειγμάτων, καθώς και εκτίμηση μοντέλου απλής γραμμικής παλινδρόμησης με ανάλυση καταλοίπων στη γλώσσα R.

---

## 2. Έλεγχος Υποθέσεων με Student's t-test

### Έλεγχος ενός δείγματος:
Ελέγχουμε εάν η μέση απόδοση ενός αλγορίθμου διαφέρει στατιστικά από την τιμή αναφοράς $\mu_0 = 100\text{ ms}$:
```R
scores <- c(98, 102, 105, 99, 108, 103, 101, 107, 104, 106)

# H0: mu = 100 vs H1: mu != 100
t_result <- t.test(scores, mu = 100, conf.level = 0.95)
print(t_result)
```

### Έλεγχος δύο ανεξάρτητων δειγμάτων (Two-Sample t-test):
```R
group_A <- c(12.1, 14.5, 13.2, 15.0, 11.8, 13.9)
group_B <- c(15.2, 16.8, 14.9, 17.1, 15.5, 16.2)

# Έλεγχος ισότητας μέσων τιμών (Welch t-test)
t_two_sample <- t.test(group_A, group_B, alternative = "two.sided")
print(t_two_sample)
```

---

## 3. Απλή Γραμμική Παλινδρόμηση (Linear Regression)
Μοντελοποίηση της σχέσης μεταξύ μεγέθους αρχείου ($X$ σε MB) και χρόνου μετάδοσης ($Y$ σε ms):
```R
file_size <- c(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
tx_time   <- c(15, 27, 39, 52, 61, 74, 83, 98, 107, 122)

# Προσαρμογή γραμμικού μοντέλου: Y = b0 + b1 * X + e
model <- lm(tx_time ~ file_size)
summary(model)

# Γραφική απεικόνιση με ευθεία παλινδρόμησης
plot(file_size, tx_time, pch = 19, col = "blue",
     main = "Grammikh Palindromisi: Xronos vs Megethos",
     xlab = "Megethos Arxeiou (MB)", ylab = "Xronos Metadosis (ms)")
abline(model, col = "red", lwd = 2)
```

