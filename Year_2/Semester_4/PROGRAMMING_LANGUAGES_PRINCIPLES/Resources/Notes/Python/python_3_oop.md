# Python — Αντικειμενοστρεφής Προγραμματισμός

*Προαπαιτούμενο: python_1_basics.md — Συναρτήσεις, εμβέλεια και το μοντέλο μνήμης αντικειμένων δεσμευμένο στο heap.*
*Προαπαιτούμενο: python_2_intermediate.md — Διακοσμητές (decorators) και συναρτήσεις πρώτης τάξης.*

Το σύστημα αντικειμενοστρεφούς προγραμματισμού (OOP) της Python παρέχει τις κλάσεις ως τον κύριο μηχανισμό για τη θυλάκωση (encapsulation) κατάστασης και συμπεριφοράς σε επαναχρησιμοποιήσιμες αφαιρέσεις. Αυτό το αρχείο καλύπτει την κατασκευή κλάσεων και αντικειμένων, τον ρόλο του `self`, τις μαγικές μεθόδους (dunder methods), την κληρονομικότητα και τη Σειρά Επίλυσης Μεθόδων (MRO), τις συμβάσεις θυλάκωσης ονομάτων, τον διακοσμητή `@property`, τις στατικές μεθόδους και τις μεθόδους κλάσης, καθώς και τα δομικά μοτίβα της σύνθεσης (composition) και της συγκέντρωσης (aggregation).

---

## 1. Κλάσεις, Αντικείμενα και Ιδιότητες Στιγμιοτύπων

### 1.1 Ορισμός Κλάσης

Μια **κλάση (class)** είναι ένα προσχέδιο (blueprint) που περιγράφει την κατάσταση (ιδιότητες) και τη συμπεριφορά (μεθόδους) μιας οικογένειας αντικειμένων. Ένα **αντικείμενο (object / instance)** είναι μια συγκεκριμένη πραγμάτωση μιας κλάσης.

**Αφαιρετική σύνταξη:**

```
class <ClassName>:
    <class_body>
```

Κατά σύμβαση, τα ονόματα των κλάσεων χρησιμοποιούν `PascalCase`.

```python
class Point:
    """Αναπαριστά ένα διδιάστατο καρτεσιανό σημείο."""

    def __init__(self, x, y):
        """Αρχικοποιεί το Point με συντεταγμένες x και y.

        Args:
            x (float): Η οριζόντια συντεταγμένη.
            y (float): Η κατακόρυφη συντεταγμένη.
        """
        self.x = x   # Ιδιότητα στιγμιοτύπου συνδεδεμένη με αυτό το αντικείμενο.
        self.y = y

p = Point(3.0, 4.0)
print(p.x, p.y)
```

```text
3.0 4.0
```

### 1.2 Ο Ρόλος του `self`

Το `self` είναι η πρώτη παράμετρος κάθε μεθόδου στιγμιοτύπου. Όταν καλείται μια μέθοδος σε ένα αντικείμενο `obj.method(arg)`, η Python περνά αυτόματα το `obj` ως `self`. Είναι μια αναφορά στο **τρέχον αντικείμενο** — το συγκεκριμένο στιγμιότυπο στο οποίο εκτελέστηκε η μέθοδος.

Το `self` είναι μια σύμβαση ονοματοδοσίας, και όχι λέξη-κλειδί. Ωστόσο, η παρέκκλιση από αυτό αποθαρρύνεται εντόνως καθώς σπάει όλα τα πρότυπα εργαλεία και συμβάσεις.

**Προσπέλαση ιδιοτήτων μέσω του `self`:**

```python
class Counter:
    """Διατηρεί έναν ακέραιο μετρητή, αυξανόμενο κατόπιν απαιτήσεως."""

    def __init__(self):
        self.count = 0   # Κάθε στιγμιότυπο λαμβάνει τη δική του ιδιότητα `count`.

    def increment(self):
        """Αυξάνει τον μετρητή κατά ένα."""
        self.count += 1

    def reset(self):
        """Επαναφέρει τον μετρητή στο μηδέν."""
        self.count = 0

c1 = Counter()
c2 = Counter()
c1.increment()
c1.increment()
print(c1.count)   # 2
print(c2.count)   # 0 — το c2 είναι ξεχωριστό αντικείμενο με τη δική του ιδιότητα `count`.
```

```text
2
0
```

### 1.3 Ιδιότητες Κλάσης έναντι Ιδιοτήτων Στιγμιοτύπου

Μια **ιδιότητα κλάσης (class attribute)** ορίζεται στο σώμα της κλάσης και είναι κοινόχρηστη από όλα τα στιγμιότυπα. Μια **ιδιότητα στιγμιοτύπου (instance attribute)** ορίζεται μέσω του `self` σε μια μέθοδο και ανήκει αποκλειστικά σε ένα στιγμιότυπο.

```python
class Dog:
    """Μοντελοποιεί ένα σκύλο με ιδιότητα επιπέδου είδους και ατομικού επιπέδου."""

    species = "Canis lupus familiaris"   # Ιδιότητα κλάσης· κοινόχρηστη σε όλα τα στιγμιότυπα Dog.

    def __init__(self, name, breed):
        self.name = name     # Ιδιότητα στιγμιοτύπου· μοναδική για αυτόν τον Dog.
        self.breed = breed

d1 = Dog("Rex", "Labrador")
d2 = Dog("Bella", "Poodle")

print(Dog.species)    # Προσπέλαση μέσω της κλάσης.
print(d1.species)     # Προσπέλαση μέσω στιγμιοτύπου (ανάγνωση από την ιδιότητα κλάσης).
print(d1.name)        # Ιδιότητα στιγμιοτύπου.
print(d2.name)        # Διαφορετικό στιγμιότυπο, διαφορετική τιμή.
```

```text
Canis lupus familiaris
Canis lupus familiaris
Rex
Bella
```

> **[Βασική Παρατήρηση]** Όταν μια ιδιότητα στιγμιοτύπου και μια ιδιότητα κλάσης μοιράζονται το ίδιο όνομα, η ιδιότητα στιγμιοτύπου **επισκιάζει (shadows)** την ιδιότητα κλάσης μόνο για το συγκεκριμένο στιγμιότυπο. Η ανάθεση `d1.species = "Wolf"` δημιουργεί μια νέα ιδιότητα στιγμιοτύπου στο `d1` και δεν τροποποιεί την ιδιότητα της κλάσης.

---

## 2. Μαγικές Μέθοδοι (Magic / Dunder Methods)

### 2.1 Ορισμός

Οι **μαγικές μέθοδοι** (ονομάζονται επίσης **dunder methods** λόγω του προθέματος και επιθήματος διπλής κάτω παύλας) είναι ειδικές μέθοδοι τις οποίες η Python καλεί σιωπηρά σε απόκριση σε συγκεκριμένες πράξεις ή κλήσεις ενσωματωμένων συναρτήσεων. Ενσωματώνουν τα οριζόμενα από τον χρήστη αντικείμενα στο σύστημα τελεστών και πρωτοκόλλων της Python.

| Μέθοδος Dunder | Καλείται Από | Σκοπός |
| :--- | :--- | :--- |
| `__init__(self, ...)` | `ClassName(...)` | Αρχικοποιεί ένα νέο στιγμιότυπο |
| `__repr__(self)` | `repr(obj)`, εμφάνιση REPL | Μη διφορούμενη αναπαράσταση συμβολοσειράς |
| `__str__(self)` | `str(obj)`, `print(obj)` | Φιλική προς τον άνθρωπο αναπαράσταση |
| `__len__(self)` | `len(obj)` | Επιστρέφει το ακέραιο μήκος |
| `__getitem__(self, key)` | `obj[key]` | Προσπέλαση δείκτη / υποσυμβόλου |
| `__setitem__(self, key, value)` | `obj[key] = value` | Ανάθεση σε δείκτη |
| `__contains__(self, item)` | `item in obj` | Έλεγχος συμμετοχής |
| `__iter__(self)` | `for x in obj`, `iter(obj)` | Επιστρέφει έναν επαναλήπτη |
| `__next__(self)` | `next(obj)` | Παράγει το επόμενο στοιχείο |
| `__eq__(self, other)` | `obj == other` | Σύγκριση ισότητας |
| `__lt__(self, other)` | `obj < other` | Σύγκριση μικρότερου από |
| `__add__(self, other)` | `obj + other` | Τελεστής πρόσθεσης |
| `__call__(self, ...)` | `obj(...)` | Καθιστά ένα στιγμιότυπο καλέσιμο |

### 2.2 `__repr__` έναντι `__str__`

- Η `__repr__` πρέπει να επιστρέφει μια συμβολοσειρά η οποία, όταν περαστεί στην `eval()`, ιδανικά ανακατασκευάζει το αντικείμενο. Είναι η αναπαράσταση για τον προγραμματιστή, η οποία χρησιμοποιείται στο REPL και στην `repr()`.
- Η `__str__` πρέπει να επιστρέφει μια περιγραφή αναγνώσιμη από τον άνθρωπο. Χρησιμοποιείται από την `print()` και τη `str()`.
- Εάν οριστεί μόνο η `__repr__`, η `str()` καταφεύγει σε αυτήν.

```python
class Vector:
    """Αναπαριστά ένα 2D μαθηματικό διάνυσμα."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x!r}, {self.y!r})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        """Υλοποιεί την πρόσθεση διανυσμάτων μέσω του τελεστή +."""
        return Vector(self.x + other.x, self.y + other.y)

    def __len__(self):
        """Επιστρέφει το ακέραιο μήκος για συμβατότητα· τα διανύσματα έχουν 2 συνιστώσες."""
        return 2

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2

print(repr(v1))    # Αναπαράσταση προγραμματιστή.
print(str(v1))     # Αναγνώσιμη από άνθρωπο.
print(v3)          # __str__ μέσω της print.
print(len(v1))
```

```text
Vector(1, 2)
(1, 2)
(4, 6)
2
```

---

## 3. Κληρονομικότητα και η Σειρά Επίλυσης Μεθόδων (MRO)

### 3.1 Απλή Κληρονομικότητα

Η **κληρονομικότητα (inheritance)** επιτρέπει σε μια κλάση (**υποκλάση**) να αποκτά τις ιδιότητες και τις μεθόδους μιας άλλης κλάσης (**υπερκλάση**), επεκτείνοντας ή αντικαθιστώντας (overriding) τις ανάλογα με τις ανάγκες.

**Σύνταξη:**

```
class SubClass(SuperClass):
    ...
```

```python
class Animal:
    """Βασική κλάση που αναπαριστά ένα γενικό ζώο."""

    def __init__(self, name):
        self.name = name

    def speak(self):
        """Επιστρέφει τη φωνή του ζώου (προς αντικατάσταση)."""
        return "..."

class Dog(Animal):
    """Υποκλάση που αναπαριστά σκύλο· αντικαθιστά τη speak()."""

    def speak(self):
        return f"{self.name} says: Woof!"

class Cat(Animal):
    """Υποκλάση που αναπαριστά γάτα· αντικαθιστά τη speak()."""

    def speak(self):
        return f"{self.name} says: Meow!"

animals = [Dog("Rex"), Cat("Whiskers"), Dog("Buddy")]
for animal in animals:
    print(animal.speak())
```

```text
Rex says: Woof!
Whiskers says: Meow!
Buddy says: Woof!
```

### 3.2 `super()` — Εκχώρηση στον Γονέα

Η `super()` επιστρέφει ένα αντικείμενο πληρεξουσίου (proxy) που εκχωρεί κλήσεις μεθόδων στη γονική κλάση στο MRO. Η κύρια χρήση της είναι η κλήση της `__init__` του γονέα όταν η υποκλάση την επεκτείνει.

```python
class Employee(Animal):
    """Επεκτείνει την Animal με αναγνωριστικό υπαλλήλου."""

    def __init__(self, name, employee_id):
        super().__init__(name)          # Εκχωρεί στην Animal.__init__.
        self.employee_id = employee_id  # Επιπλέον ιδιότητα ειδική για τον Employee.

    def speak(self):
        return f"Employee {self.employee_id} ({self.name}) says: Hello."

e = Employee("Alice", "E-001")
print(e.speak())
print(e.name)         # Κληρονομημένο από την Animal.__init__ μέσω super().
print(e.employee_id)
```

```text
Employee E-001 (Alice) says: Hello.
Alice
E-001
```

### 3.3 Πολλαπλή Κληρονομικότητα και το MRO

Η Python υποστηρίζει **πολλαπλή κληρονομικότητα (multiple inheritance)**: μια κλάση μπορεί να κληρονομεί από περισσότερους από έναν γονείς. Για την επίλυση αμφισημιών στην αναζήτηση μεθόδων, η Python χρησιμοποιεί τον αλγόριθμο **C3 Linearization** για την παραγωγή της **Σειράς Επίλυσης Μεθόδων (Method Resolution Order - MRO)** — μια ντετερμινιστική, γραμμικοποιημένη ακολουθία κλάσεων προς αναζήτηση.

```
class C(A, B):
    ...
```

Το MRO υπολογίζεται έτσι ώστε:
1. Μια κλάση να προηγείται πάντα των γονέων της.
2. Η σειρά των γονέων στη δήλωση της κλάσης να διατηρείται.
3. Καμία κλάση να μην εμφανίζεται πριν από όλες τις κλάσεις που κληρονομούν από αυτήν.

```python
class X:
    def hello(self):
        return "X.hello"

class Y:
    def hello(self):
        return "Y.hello"

class Z(X, Y):
    pass

z = Z()
print(z.hello())        # Επιλύεται σε X.hello επειδή η X προηγείται της Y στο MRO.
print(Z.__mro__)        # Εμφανίζει το πλήρες MRO.
```

```text
X.hello
(<class '__main__.Z'>, <class '__main__.X'>, <class '__main__.Y'>, <class 'object'>)
```

> **[Βασική Παρατήρηση]** Όλες οι κλάσεις της Python κληρονομούν σιωπηρά από την `object`, η οποία είναι πάντα η τελευταία καταχώριση στο MRO. Η `object` παρέχει προεπιλεγμένες υλοποιήσεις των `__repr__`, `__str__`, `__eq__` και άλλων θεμελιωδών dunder μεθόδων.

---

## 4. Θυλάκωση (Encapsulation)

### 4.1 Συμβάσεις Ελέγχου Προσπέλασης

Η Python δεν επιβάλλει έλεγχο προσπέλασης στο επίπεδο της γλώσσας (δεν υπάρχουν λέξεις-κλειδιά `private` ή `protected`). Αντίθετα, χρησιμοποιεί συμβάσεις ονοματοδοσίας:

| Σύμβαση | Σύνταξη | Σημασία |
| :--- | :--- | :--- |
| Δημόσιο (Public) | `attr` | Χωρίς περιορισμό· ελεύθερα προσπελάσιμο |
| Προστατευμένο (Protected) | `_attr` | Κατά σύμβαση, εσωτερική χρήση· δεν επιβάλλεται από τον διερμηνέα |
| Παραμορφωμένο (Name-mangled) | `__attr` | Ο διερμηνέας ξαναγράφει το όνομα σε `_ClassName__attr` |

### 4.2 Παραμόρφωση Ονομάτων (Name Mangling)

Οποιοδήποτε αναγνωριστικό με δύο αρχικές κάτω παύλες και το πολύ μία τελική κάτω παύλα εντός του σώματος μιας κλάσης υπόκειται σε **παραμόρφωση ονόματος (name mangling)**: ο διερμηνέας προτάσσει το `_ClassName` στο όνομα.

```python
class BankAccount:
    """Μοντελοποιεί έναν τραπεζικό λογαριασμό με ιδιωτικό υπόλοιπο."""

    def __init__(self, initial_balance):
        self.__balance = initial_balance   # Παραμορφώνεται σε _BankAccount__balance.

    def deposit(self, amount):
        """Προσθέτει το `amount` στο υπόλοιπο."""
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        """Επιστρέφει το τρέχον υπόλοιπο."""
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())       # 1500 — προσπέλαση μέσω δημόσιας μεθόδου.

# Άμεση προσπέλαση χρησιμοποιώντας το παραμορφωμένο όνομα (δυνατή, αλλά αποθαρρύνεται έντονα).
print(account._BankAccount__balance)
```

```text
1500
1500
```

### 4.3 Ο Διακοσμητής `@property`

Ο `@property` μετατρέπει μια μέθοδο σε **διαχειριζόμενη ιδιότητα (managed attribute)** (έναν descriptor). Εκθέτει μια καθαρή διασύνδεση σε στιλ ιδιότητας ενώ εκτελεί αυθαίρετη λογική κατά την προσπέλαση. Αυτή είναι η τυπική εναλλακτική της Python έναντι των ρητών μεθόδων getter/setter.

**Τρία στοιχεία:**

| Διακοσμητής | Ρόλος |
| :--- | :--- |
| `@property` | Ορίζει τον getter (προσπέλαση ανάγνωσης) |
| `@<attr>.setter` | Ορίζει τον setter (προσπέλαση εγγραφής) |
| `@<attr>.deleter` | Ορίζει τον deleter (`del obj.attr`) |

```python
class Temperature:
    """Αποθηκεύει θερμοκρασία σε Κελσίου· εκθέτει μια επικυρωμένη ιδιότητα celsius."""

    def __init__(self, celsius):
        self._celsius = None      # Ιδιωτική ιδιότητα αποθήκευσης.
        self.celsius = celsius    # Ενεργοποιεί τον setter για επικύρωση.

    @property
    def celsius(self):
        """Επιστρέφει την τρέχουσα θερμοκρασία σε Κελσίου."""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Ορίζει τη θερμοκρασία, προκαλώντας ValueError για φυσικά αδύνατες τιμές."""
        if value < -273.15:
            raise ValueError(f"Temperature {value} is below absolute zero.")
        self._celsius = value

    @property
    def fahrenheit(self):
        """Υπολογίζει και επιστρέφει την ισοδύναμη θερμοκρασία σε Φαρενάιτ (μόνο για ανάγνωση)."""
        return self._celsius * 9 / 5 + 32

t = Temperature(100)
print(t.celsius)      # 100
print(t.fahrenheit)   # 212.0
t.celsius = 37
print(t.celsius)      # 37
```

```text
100
212.0
37
```

---

## 5. Στατικές Μέθοδοι και Μέθοδοι Κλάσης

### 5.1 Μέθοδοι Στιγμιοτύπου, Μέθοδοι Κλάσης και Στατικές Μέθοδοι

| Διακοσμητής | Πρώτη Παράμετρος | Προσπέλαση σε | Περίπτωση Χρήσης |
| :--- | :--- | :--- | :--- |
| Κανένας (προεπιλογή) | `self` (στιγμιότυπο) | Ιδιότητες στιγμιοτύπου και κλάση | Κανονικές πράξεις στιγμιοτύπου |
| `@classmethod` | `cls` (η ίδια η κλάση) | Ιδιότητες κλάσης μόνο | Εναλλακτικοί κατασκευαστές, μέθοδοι εργοστασίου |
| `@staticmethod` | Καμία | Ούτε στιγμιότυπο ούτε κλάση σιωπηρά | Βοηθητικές συναρτήσεις λογικά ομαδοποιημένες με την κλάση |

```python
class Circle:
    """Αναπαριστά κύκλο, με εργοστασιακές και βοηθητικές μεθόδους."""

    PI = 3.141592653589793   # Ιδιότητα κλάσης.

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Υπολογίζει το εμβαδόν αυτού του στιγμιοτύπου κύκλου."""
        return Circle.PI * self.radius ** 2

    @classmethod
    def from_diameter(cls, diameter):
        """Εναλλακτικός κατασκευαστής· δημιουργεί Circle από τιμή διαμέτρου.

        Args:
            diameter (float): Η διάμετρος του κύκλου.

        Returns:
            Circle: Ένα νέο στιγμιότυπο Circle με ακτίνα = διάμετρος / 2.
        """
        return cls(diameter / 2)   # Το cls αναφέρεται στην Circle (ή οποιαδήποτε υποκλάση).

    @staticmethod
    def is_valid_radius(value):
        """Επαληθεύει ότι μια τιμή ακτίνας είναι θετική.

        Args:
            value (float): Η υποψήφια ακτίνα.

        Returns:
            bool: True εάν το `value` είναι αυστηρά θετικό, False διαφορετικά.
        """
        return value > 0

c1 = Circle(5)
c2 = Circle.from_diameter(10)   # Δημιουργεί Circle με ακτίνα 5.

print(c1.area())
print(c2.radius)
print(Circle.is_valid_radius(-3))
```

```text
78.53981633974483
5.0
False
```

---

## 6. Σύνθεση και Συγκέντρωση

### 6.1 Σύνθεση έναντι Κληρονομικότητας

Η **κληρονομικότητα (inheritance)** μοντελοποιεί μια σχέση τύπου **είναι-ένα (is-a)**: ο `Dog` είναι ένα `Animal`.
Η **σύνθεση (composition)** μοντελοποιεί μια σχέση τύπου **έχει-ένα (has-a)**: το `Car` έχει μια `Engine`.

Η σύνθεση προτιμάται συχνά έναντι των βαθιών ιεραρχιών κληρονομικότητας επειδή παράγει πιο αρθρωτό, δοκιμάσιμο και συντηρήσιμο κώδικα.

### 6.2 Παράδειγμα Σύνθεσης: Engine → Car

```python
class Engine:
    """Αναπαριστά μηχανή εσωτερικής καύσης με καθορισμένη ισχύ ίππων."""

    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        """Προσομοιώνει την εκκίνηση της μηχανής."""
        return f"Engine ({self.horsepower} hp) started."

class Car:
    """Αναπαριστά αυτοκίνητο που συντίθεται από μια Engine και επιπλέον ιδιότητες."""

    def __init__(self, make, model, horsepower):
        self.make = make
        self.model = model
        self._engine = Engine(horsepower)   # Το Car κατέχει την Engine του.

    def start(self):
        """Εκκινεί το αυτοκίνητο εκχωρώντας στην εσωτερική μηχανή."""
        return f"{self.make} {self.model}: {self._engine.start()}"

car = Car("Toyota", "Supra", 340)
print(car.start())
```

```text
Toyota Supra: Engine (340 hp) started.
```

### 6.3 Παράδειγμα Συγκέντρωσης: Book → Library

Η **συγκέντρωση (aggregation)** είναι μια ασθενέστερη μορφή σύνθεσης: τα περιεχόμενα αντικείμενα μπορούν να υπάρχουν ανεξάρτητα από τον περιέκτη.

```python
class Book:
    """Αναπαριστά ένα βιβλίο με τίτλο και τιμή."""

    def __init__(self, title, price):
        self.title = title
        self.price = price

class Library:
    """Συγκεντρώνει μια συλλογή αντικειμένων Book."""

    def __init__(self, name):
        self.name = name
        self.books = []   # Η Library συγκεντρώνει υπάρχοντα αντικείμενα Book.

    def add_book(self, book):
        """Προσθέτει ένα Book στη συλλογή της βιβλιοθήκης.

        Args:
            book (Book): Το βιβλίο προς προσθήκη.
        """
        self.books.append(book)

    def total_value(self):
        """Υπολογίζει τη συνολική τιμή όλων των βιβλίων χρησιμοποιώντας έκφραση γεννήτριας.

        Returns:
            float: Το άθροισμα όλων των τιμών βιβλίων.
        """
        return sum(book.price for book in self.books)  # Η έκφραση γεννήτριας αποφεύγει την ενδιάμεση λίστα.

    def catalog(self):
        """Επιστρέφει μια μορφοποιημένη συμβολοσειρά που εμφανίζει όλα τα βιβλία και τις τιμές τους.

        Returns:
            str: Κατάλογος καταχωρίσεων βιβλίων διαχωρισμένος με νέες γραμμές.
        """
        return "\n".join(f"  {book.title}: ${book.price:.2f}" for book in self.books)

b1 = Book("Clean Code", 35.00)
b2 = Book("The Pragmatic Programmer", 42.00)
b3 = Book("Design Patterns", 55.00)

lib = Library("Tech Library")
lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)

print(lib.catalog())
print(f"Total value: ${lib.total_value():.2f}")
```

```text
  Clean Code: $35.00
  The Pragmatic Programmer: $42.00
  Design Patterns: $55.00
Total value: $132.00
```

> **[Βασική Παρατήρηση]** Η έκφραση `sum(book.price for book in self.books)` χρησιμοποιεί μια **έκφραση γεννήτριας (generator expression)** (παρενθέσεις, όχι αγκύλες) αντί για κατασκευή λίστας. Παράγει κάθε `book.price` ένα προς ένα χωρίς την κατασκευή ενδιάμεσης λίστας στη μνήμη — σημαντικό όταν η `self.books` είναι πολύ μεγάλη. Η `sum()` δέχεται οποιοδήποτε προσπελάσιμο αντικείμενο, συμπεριλαμβανομένων των γεννητριών.

---

## Λυμένες Ασκήσεις

### Άσκηση 1: Βασική Κατασκευή Κλάσης

**Πρόβλημα:** Υλοποιήστε μια κλάση `Rectangle` με ιδιότητες `width` και `height`, μεθόδους `area()` και `perimeter()`, και μια μέθοδο `__repr__`.

**Λύση:**

```python
class Rectangle:
    """Αναπαριστά ορθογώνιο ορισμένο από πλάτος και ύψος."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Υπολογίζει το εμβαδόν του ορθογωνίου.

        Returns:
            float: Γινόμενο πλάτους και ύψους.
        """
        return self.width * self.height

    def perimeter(self):
        """Υπολογίζει την περίμετρο του ορθογωνίου.

        Returns:
            float: Το διπλάσιο του αθροίσματος πλάτους και ύψους.
        """
        return 2 * (self.width + self.height)

    def __repr__(self):
        return f"Rectangle(width={self.width!r}, height={self.height!r})"

r = Rectangle(4, 7)
print(repr(r))
print(r.area())
print(r.perimeter())
```

```text
Rectangle(width=4, height=7)
28
22
```

---

### Άσκηση 2: Ιδιότητες Κλάσης και Επισκίαση Στιγμιοτύπου

**Πρόβλημα:** Προβλέψτε την έξοδο του παρακάτω κώδικα.

```python
class Config:
    debug = False
    timeout = 30

c1 = Config()
c2 = Config()

c1.debug = True    # Δημιουργεί ιδιότητα στιγμιοτύπου στο c1· ΔΕΝ τροποποιεί την ιδιότητα της κλάσης.

print(Config.debug)
print(c1.debug)
print(c2.debug)
```

**Λύση:**

```text
False
True
False
```

Η εντολή `c1.debug = True` δημιουργεί μια νέα ιδιότητα στιγμιοτύπου `debug` στο `c1`. Η ιδιότητα κλάσης `Config.debug` παραμένει `False`. Το `c2.debug` διαβάζει την ιδιότητα κλάσης (δεν υπάρχει ιδιότητα στιγμιοτύπου στο `c2`), οπότε επιστρέφει `False`.

---

### Άσκηση 3: `__eq__` και `__lt__` για Προσαρμοσμένη Σύγκριση

**Πρόβλημα:** Υλοποιήστε μια κλάση `Student` με ιδιότητες `name` και `gpa`. Υλοποιήστε τις `__eq__` (ισότητα βάσει `name` και `gpa`) και `__lt__` (διάταξη βάσει `gpa`). Στη συνέχεια ταξινομήστε μια λίστα φοιτητών.

**Λύση:**

```python
class Student:
    """Αναπαριστά φοιτητή· υποστηρίζει ισότητα και διάταξη βάσει GPA."""

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __repr__(self):
        return f"Student({self.name!r}, gpa={self.gpa})"

    def __eq__(self, other):
        """Συγκρίνει φοιτητές βάσει ονόματος και GPA."""
        if not isinstance(other, Student):
            return NotImplemented
        return self.name == other.name and self.gpa == other.gpa

    def __lt__(self, other):
        """Διατάσσει φοιτητές βάσει GPA σε αύξουσα σειρά."""
        return self.gpa < other.gpa

students = [Student("Alice", 3.7), Student("Bob", 3.2), Student("Carol", 3.9)]
students.sort()   # Χρησιμοποιεί την __lt__ μέσω του Timsort.
print(students)
```

```text
[Student('Bob', gpa=3.2), Student('Alice', gpa=3.7), Student('Carol', gpa=3.9)]
```

---

### Άσκηση 4: Κληρονομικότητα και Αντικατάσταση Μεθόδου

**Πρόβλημα:** Δημιουργήστε μια ιεραρχία κλάσεων: `Shape` (βασική) → `Circle` και `Square` (υποκλάσεις). Η `Shape` διαθέτει αφαιρετική μέθοδο `area()`. Επιδείξτε πολυμορφική κλήση.

**Λύση:**

```python
class Shape:
    """Βασική κλάση για γεωμετρικά σχήματα· οι υποκλάσεις πρέπει να υλοποιήσουν την area()."""

    def area(self):
        """Επιστρέφει το εμβαδόν του σχήματος (αντικατάσταση στις υποκλάσεις)."""
        raise NotImplementedError(f"{type(self).__name__} must implement area()")

class Circle(Shape):
    """Κύκλος ορισμένος από την ακτίνα του."""

    PI = 3.141592653589793

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.PI * self.radius ** 2

class Square(Shape):
    """Τετράγωνο ορισμένο από το μήκος της πλευράς του."""

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

shapes = [Circle(5), Square(4), Circle(3), Square(7)]
for shape in shapes:
    print(f"{type(shape).__name__}: area = {shape.area():.4f}")
```

```text
Circle: area = 78.5398
Square: area = 16.0000
Circle: area = 28.2743
Square: area = 49.0000
```

---

### Άσκηση 5: `super()` σε Πολλαπλή Κληρονομικότητα

**Πρόβλημα:** Ιχνηλατήστε την κλήση στην `super().__init__()` μέσω του παρακάτω MRO και προβλέψτε την έξοδο.

```python
class A:
    def __init__(self):
        print("A.__init__")
        super().__init__()

class B(A):
    def __init__(self):
        print("B.__init__")
        super().__init__()

class C(A):
    def __init__(self):
        print("C.__init__")
        super().__init__()

class D(B, C):
    def __init__(self):
        print("D.__init__")
        super().__init__()

d = D()
print(D.__mro__)
```

**Λύση:**

Το MRO της `D` είναι `[D, B, C, A, object]`. Κάθε κλήση `super().__init__()` ακολουθεί αυτή τη γραμμική αλυσίδα:

```text
D.__init__
B.__init__
C.__init__
A.__init__
(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
```

Η `super()` στην `B.__init__` δεν καλεί την `A.__init__` άμεσα — καλεί την επόμενη κλάση στο MRO της `D`, η οποία είναι η `C`. Αυτός είναι ο μηχανισμός συνεργατικής πολλαπλής κληρονομικότητας που αποτρέπει την κλήση της `A.__init__` δύο φορές.

---

### Άσκηση 6: `@property` με Επικύρωση

**Πρόβλημα:** Υλοποιήστε μια κλάση `PositiveCounter` της οποίας η ιδιότητα `value` δέχεται μόνο θετικούς ακεραίους, προκαλώντας `ValueError` διαφορετικά.

**Λύση:**

```python
class PositiveCounter:
    """Ένας μετρητής που επιβάλλει μια αυστηρά θετική ακέραια τιμή."""

    def __init__(self, initial):
        self.value = initial   # Χρησιμοποιεί τον setter για επικύρωση.

    @property
    def value(self):
        """Επιστρέφει την τρέχουσα τιμή του μετρητή."""
        return self._value

    @value.setter
    def value(self, v):
        """Ορίζει την τιμή του μετρητή, προκαλώντας ValueError εάν το v δεν είναι θετικός ακέραιος."""
        if not isinstance(v, int) or v <= 0:
            raise ValueError(f"Value must be a positive integer, got {v!r}.")
        self._value = v

c = PositiveCounter(10)
print(c.value)
c.value = 5
print(c.value)

try:
    c.value = -3
except ValueError as e:
    print(e)
```

```text
10
5
Value must be a positive integer, got -3.
```

---

### Άσκηση 7: Σύνθεση — Στοιβάδα (Stack) με Χρήση Λίστας

**Πρόβλημα:** Υλοποιήστε μια κλάση `Stack` χρησιμοποιώντας σύνθεση (μια εσωτερική `list`) αντί να κληρονομείτε από τη `list`. Υλοποιήστε τις `push()`, `pop()`, `peek()`, `is_empty()` και `__len__`.

**Λύση:**

```python
class Stack:
    """Δομή δεδομένων LIFO υλοποιημένη μέσω σύνθεσης με μια λίστα Python."""

    def __init__(self):
        self._data = []   # Εσωτερική λίστα· δεν εκτίθεται άμεσα.

    def push(self, item):
        """Ωθεί ένα στοιχείο στην κορυφή της στοιβάδας.

        Args:
            item: Το στοιχείο προς ώθηση.
        """
        self._data.append(item)

    def pop(self):
        """Αφαιρεί και επιστρέφει το κορυφαίο στοιχείο.

        Returns:
            Το κορυφαίο στοιχείο.

        Raises:
            IndexError: Εάν η στοιβάδα είναι άδεια.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self):
        """Επιστρέφει το κορυφαίο στοιχείο χωρίς να το αφαιρέσει.

        Returns:
            Το κορυφαίο στοιχείο.

        Raises:
            IndexError: Εάν η στοιβάδα είναι άδεια.
        """
        if self.is_empty():
            raise IndexError("peek at empty stack")
        return self._data[-1]

    def is_empty(self):
        """Επιστρέφει True εάν η στοιβάδα δεν περιέχει στοιχεία."""
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f"Stack({self._data!r})"

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s)
print(s.peek())
print(s.pop())
print(len(s))
```

```text
Stack([1, 2, 3])
3
3
2
```

---

### Άσκηση 8: Συγκέντρωση με Εκφράσεις Γεννήτριας

**Πρόβλημα:** Επεκτείνετε το μοντέλο `Library` / `Book`. Δοθείσης μιας λίστας βιβλίων, υπολογίστε: τη συνολική τιμή, τη μέση τιμή, το ακριβότερο βιβλίο και μια λίστα με όλα τα βιβλία που κοστίζουν πάνω από $40.

**Λύση:**

```python
class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price
    def __repr__(self):
        return f"Book({self.title!r}, ${self.price:.2f})"

class Library:
    def __init__(self, books):
        self.books = books   # Συγκεντρώνει ανεξάρτητα υπάρχοντα αντικείμενα Book.

    def total_value(self):
        return sum(b.price for b in self.books)

    def average_price(self):
        return self.total_value() / len(self.books)

    def most_expensive(self):
        return max(self.books, key=lambda b: b.price)

    def books_above(self, threshold):
        return [b for b in self.books if b.price > threshold]

catalog = [
    Book("SICP", 55.00),
    Book("CLRS", 75.00),
    Book("Python Cookbook", 38.00),
    Book("Fluent Python", 48.00),
    Book("Learning Python", 30.00),
]
lib = Library(catalog)

print(f"Total: ${lib.total_value():.2f}")
print(f"Average: ${lib.average_price():.2f}")
print(f"Most expensive: {lib.most_expensive()}")
print(f"Above $40: {lib.books_above(40)}")
```

```text
Total: $246.00
Average: $49.20
Most expensive: Book('CLRS', $75.00)
Above $40: [Book('SICP', $55.00), Book('CLRS', $75.00), Book('Fluent Python', $48.00)]
```

---

## Συμβουλή Εξετάσεων: MRO, `super()` και Παραμόρφωση Ονομάτων

**Μοτίβο εξετάσεων MRO:** Δοθείσης μιας ιεραρχίας κλάσεων με πολλαπλή κληρονομικότητα, για τον προσδιορισμό της σειράς επίλυσης μεθόδων, εφαρμόστε τον κανόνα C3 linearization: ξεκινήστε από την πλέον παραγόμενη κλάση, και προτιμάτε πάντα τον αριστερότερο γονέα. Η ιδιότητα `ClassName.__mro__` εμφανίζει την πλήρη ακολουθία.

**`super()` σε απλή κληρονομικότητα:** Η `super().__init__(args)` πρέπει να καλείται ρητά στην `__init__` της υποκλάσης εάν η `__init__` του γονέα ορίζει ιδιότητες από τις οποίες εξαρτάται η υποκλάση. Η παράλειψη αυτής της κλήσης αποτελεί το συχνότερο σφάλμα κληρονομικότητας.

**Διακριτότητα παραμόρφωσης ονομάτων:** Το `__attr` (δύο αρχικές κάτω παύλες, το πολύ μία τελική) υφίσταται παραμόρφωση. Το `__attr__` (δύο αρχικές και δύο τελικές κάτω παύλες — dunder) **δεν** παραμορφώνεται· είναι θέση μαγικής μεθόδου. Η διαφορά έγκειται στις τελικές κάτω παύλες.

**`@property` έναντι άμεσης ιδιότητας:** Ο ορισμός της `@property` δεν εμποδίζει την άμεση προσπέλαση στην υποκείμενη ιδιότητα αποθήκευσης (π.χ. `self._celsius`). Η σύμβαση μιας μεμονωμένης αρχικής κάτω παύλας σηματοδοτεί ότι η άμεση προσπέλαση αποθαρρύνεται, αλλά ο διερμηνέας δεν την επιβάλλει.
