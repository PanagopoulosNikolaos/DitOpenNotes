# Εργαστηριακός Οδηγός 1: Διερευνητική Ανάλυση Δεδομένων και Περιγραφική Στατιστική σε R

## 1. Σκοπός Εργαστηρίου
Εξοικείωση με το περιβάλλον της γλώσσας στατιστικού προγραμματισμού R (ή RStudio). Εισαγωγή συνόλων δεδομένων, υπολογισμός δεικτών θέσης και διασποράς και γραφική αναπαράσταση με ιστογράμματα και διαγράμματα πλαισίου (boxplots).

---

## 2. Βασικές Εντολές Περιγραφικής Στατιστικής
```R
# Δημιουργία δείγματος χρόνων απόκρισης δικτύου (σε ms)
response_times <- c(42.5, 45.1, 38.9, 52.3, 41.0, 44.8, 65.2, 39.4, 43.1, 48.7, 50.2, 41.5)

# Δείκτες Θέσης
mean_val <- mean(response_times)
median_val <- median(response_times)
quantile_vals <- quantile(response_times, probs = c(0.25, 0.5, 0.75))

# Δείκτες Διασποράς
var_val <- var(response_times)
sd_val <- sd(response_times)
iqr_val <- IQR(response_times)

cat("Mesi Timi:", round(mean_val, 2), "\n")
cat("Diamesos:", median_val, "\n")
cat("Typiki Apoklisi:", round(sd_val, 2), "\n")
cat("Endotetartomoriako Eyros (IQR):", iqr_val, "\n")
```

---

## 3. Οπτικοποίηση Δεδομένων σε R
```R
par(mfrow = c(1, 2)) # Διάταξη γραφημάτων σε 1 γραμμή και 2 στήλες

# Ιστόγραμμα Συχνοτήτων με Καμπύλη Πυκνότητας
hist(response_times, breaks = 6, probability = TRUE, col = "lightblue",
     main = "Istogramma Xronwn Apokrisis", xlab = "Xronos (ms)")
lines(density(response_times), col = "darkblue", lwd = 2)

# Θηκόγραμμα (Boxplot) για Εντοπισμό Ακραίων Τιμών (Outliers)
boxplot(response_times, col = "salmon", horizontal = TRUE,
        main = "Boxplot Xronwn Apokrisis", xlab = "Xronos (ms)")
```

