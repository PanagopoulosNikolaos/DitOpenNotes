# Ασκήσεις Εμπέδωσης: Κλάσεις, Κληρονομικότητα και Πολυμορφισμός

## Άσκηση 1: Ιεραρχία Εργαζομένων και Υπολογισμός Μισθοδοσίας
### Εκφώνηση:
Σχεδιάστε μια αφηρημένη βασική κλάση `Employee` και δύο παράγωγες κλάσεις `SalariedEmployee` και `HourlyEmployee` σε C++:
1. Η `Employee` περιέχει όνομα (`std::string`) και αναγνωριστικό (`int id`), καθώς και την pure virtual μέθοδο `virtual double calculatePay() const = 0;`.
2. Η `SalariedEmployee` αμείβεται με σταθερό μηνιαίο μισθό.
3. Η `HourlyEmployee` αμείβεται με ωρομίσθιο και αριθμό ωρών εργασίας (με υπερωριακή προσαύξηση $1.5\times$ για ώρες $> 40$).
4. Γράψτε συνάρτηση `void printPayroll(const std::vector<std::unique_ptr<Employee>>& staff)` που εκτυπώνει τη μισθοδοσία πολυμορφικά.

### Λύση:
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>

class Employee {
protected:
    std::string name;
    int id;

public:
    Employee(const std::string& emp_name, int emp_id) : name(emp_name), id(emp_id) {}
    virtual ~Employee() = default;

    virtual double calculatePay() const = 0;
    virtual void printInfo() const {
        std::cout << "ID: " << id << " | Onoma: " << name << " | Misthos: " << calculatePay() << " EUR\n";
    }
};

class SalariedEmployee : public Employee {
private:
    double monthly_salary;

public:
    SalariedEmployee(const std::string& name, int id, double salary)
        : Employee(name, id), monthly_salary(salary) {}

    double calculatePay() const override {
        return monthly_salary;
    }
};

class HourlyEmployee : public Employee {
private:
    double hourly_rate;
    double hours_worked;

public:
    HourlyEmployee(const std::string& name, int id, double rate, double hours)
        : Employee(name, id), hourly_rate(rate), hours_worked(hours) {}

    double calculatePay() const override {
        if (hours_worked <= 40.0) {
            return hourly_rate * hours_worked;
        } else {
            double regular = 40.0 * hourly_rate;
            double overtime = (hours_worked - 40.0) * (hourly_rate * 1.5);
            return regular + overtime;
        }
    }
};

void printPayroll(const std::vector<std::unique_ptr<Employee>>& staff) {
    double total = 0.0;
    for (const auto& emp : staff) {
        emp->printInfo();
        total += emp->calculatePay();
    }
    std::cout << "Synoliko Kostos Misthodosias: " << total << " EUR\n";
}
```

---

## Άσκηση 2: Virtual Destructors και Αποφυγή Memory Leaks
### Εκφώνηση:
Εξηγήστε τι συμβαίνει όταν διαγράφεται ένα αντικείμενο παραγόμενης κλάσης μέσω δείκτη βασικής κλάσης (`Base* ptr = new Derived(); delete ptr;`) εάν ο destructor της `Base` **δεν** είναι δηλωμένος ως `virtual`.

### Λύση:
Εάν ο destructor της βασικής κλάσης δεν είναι `virtual`, η κλήση `delete ptr` προκαλεί **Undefined Behavior** (μη καθορισμένη συμπεριφορά). Στην πράξη, ο compiler θα εκτελέσει στατική σύνδεση (early binding) και θα καλέσει **μόνο** τον destructor της `Base`. Ο destructor της `Derived` δεν θα εκτελεστεί ποτέ, με αποτέλεσμα τυχόν δυναμικοί πόροι (μνήμη heap, αρχεία κ.λπ.) που δεσμεύτηκαν στην `Derived` να μην απελευθερωθούν, προκαλώντας διαρροή μνήμης (Memory Leak).
Γι' αυτό αποτελεί απαράβατο κανόνα: **Κάθε κλάση με τουλάχιστον μία virtual συνάρτηση πρέπει να διαθέτει public virtual destructor (`virtual ~Base() = default;`)**.

