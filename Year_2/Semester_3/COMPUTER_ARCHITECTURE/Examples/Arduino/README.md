# Αρχιτεκτονική Υπολογιστών - Έργα Arduino

## Πρόγραμμα_1: Αναβοσβήμα LED με Σειριακή Εξαγωγή

Ένα απλό σχέδιο Arduino που αναβοσβήνει το ενσωματωμένο LED σε ένα Arduino Uno αποστέλνοντας μηνύματα κατάστασης στη σειριακή οθόνη παρακολούθησης.

### Απαιτήσεις

- Μικροεπεξεργαστής Arduino Uno
- Καλώδιο USB (Τύπου A σε Τύπου B)
- Arduino CLI εγκατεστημένο
- Σύστημα Linux με κατάλληλα δικαιώματα USB

### Οδηγίες Ρύθμισης

#### 1. Εγκατάσταση Arduino CLI

```bash
curl -fsSL https://raw.githubusercontent.com/arduino/arduino-cli/master/install.sh | sh
```

Προσθήκη του καταλόγου bin στο PATH:
```bash
export PATH="$PATH:$HOME/Documents/University_Code/Semester_3/COMPUTER_ARCHITECTURE/bin"
```

#### 2. Εγκατάσταση Πλατφόρμας Arduino AVR

```bash
sudo arduino-cli core install arduino:avr
```

Αυτό εγκαθιστά τον απαραίτητο μεταγλωττιστή, τα εργαλεία και τις βιβλιοθήκες για την ανάπτυξη Arduino Uno.

#### 3. Σύνδεση του Arduino

Συνδέστε το Arduino Uno στον υπολογιστή σας μέσω καλωδίου USB. Επαληθεύστε τη σύνδεση:

```bash
arduino-cli board list
```

Θα πρέπει να δείτε έξοδο παρόμοια με:
```
Port         Protocol Type              Board Name  FQBN            Core
/dev/ttyACM0 serial   Serial Port (USB) Arduino Uno arduino:avr:uno arduino:avr
```

### Μεταγλάττεση και Μεταφόρτωση

#### Μεταγλάττεση του Σχεδίου

```bash
cd Program_1
arduino-cli compile --fqbn arduino:avr:uno Program_1.ino
```

#### Μεταφόρτωση στο Arduino

```bash
sudo arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:uno Program_1.ino
```

**Σημείωση:** Απαιτείται `sudo` για πρόσβαση στη σειριακή θύρα USB. Εναλλακτικά, μπορείτε να προσθέσετε τον χρήστη σας στην ομάδα `dialout`:
```bash
sudo usermod -a -G dialout $USER
```
Στη συνέχεια αποσυνδεθείτε και συνδεθείτε ξανά.

### Συμπεριφορά Προγράμματος

- **LED**: Αναβοσβήνει κάθε 2 δευτερόλεπτα (1 δευτερόλεπτο ΕΝΕΡΓΟ, 1 δευτερόλεπτο ΑΠΕΝΕΡΓΟ)
- **Σειριακή Εξαγωγή**: Εκτυπώνει μηνύματα "LED ON" και "LED OFF" σε 9600 baud

### Προβολή Σειριακής Εξαγωγής

Για να δείτε τα σειριακά μηνύματα σε πραγματικό χρόνο:

```bash
sudo arduino-cli monitor -p /dev/ttyACM0 --config baudrate=9600
```

### Αντιμετώπιση Προβλημάτων

**Σφάλμα: "main file missing from sketch"**
- Βεβαιωθείτε ότι το όνομα του φακέλου του σχεδίου ταιριάζει με το όνομα αρχείου `.ino` (π.χ. ο φάκελος `Program_1` περιέχει το `Program_1.ino`)

**Σφάλμα: "Platform 'arduino:avr' not found"**
- Εκτελέστε: `sudo arduino-cli core install arduino:avr`

**Σφάλμα: "Permission denied" στο `/dev/ttyACM0`**
- Εκτελέστε την εντολή μεταφόρτωσης με `sudo`, ή προσθέστε τον χρήστη σας στην ομάδα `dialout` όπως περιγράφηκε παραπάνω

**Το Arduino δεν ανιχνεύεται**
- Ελέγξτε τη σύνδεση καλωδίου USB
- Δοκιμάστε μια διαφορετική θύρα USB
- Εκτελέστε: `arduino-cli board list` για επαλήθευση ανίχνευσης
