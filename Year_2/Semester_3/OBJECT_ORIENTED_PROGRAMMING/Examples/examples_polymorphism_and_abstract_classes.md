# Παραδείγματα: Πολυμορφισμός, Αφηρημένες Κλάσεις και Διεπαφές

## Παράδειγμα 1: Σύστημα Επεξεργασίας Πληρωμών (Payment Gateway)

### Περιγραφή
Σχεδιασμός συστήματος επεξεργασίας ηλεκτρονικών πληρωμών με χρήση αφηρημένης βασικής κλάσης `PaymentMethod` και υλοποιήσεων `CreditCardPayment`, `PayPalPayment`, και `CryptoPayment`.

### Πλήρης Κώδικας C++
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>

class PaymentMethod {
protected:
    std::string transaction_id;

public:
    PaymentMethod(const std::string& id) : transaction_id(id) {}
    virtual ~PaymentMethod() = default;

    virtual bool processPayment(double amount) = 0;
    virtual void printReceipt(double amount) const = 0;
};

class CreditCardPayment : public PaymentMethod {
private:
    std::string card_number;

public:
    CreditCardPayment(const std::string& id, const std::string& card)
        : PaymentMethod(id), card_number(card) {}

    bool processPayment(double amount) override {
        std::cout << "[CreditCard] Xrewsi " << amount << " EUR stin karta ****" 
                  << card_number.substr(card_number.length() - 4) << "\n";
        return true;
    }

    void printReceipt(double amount) const override {
        std::cout << "Apodeixi [CreditCard] TxID: " << transaction_id 
                  << " | Poso: " << amount << " EUR\n";
    }
};

class PayPalPayment : public PaymentMethod {
private:
    std::string email;

public:
    PayPalPayment(const std::string& id, const std::string& mail)
        : PaymentMethod(id), email(mail) {}

    bool processPayment(double amount) override {
        std::cout << "[PayPal] Plirwmi " << amount << " EUR meso logariasmou: " << email << "\n";
        return true;
    }

    void printReceipt(double amount) const override {
        std::cout << "Apodeixi [PayPal] TxID: " << transaction_id 
                  << " | Email: " << email << " | Poso: " << amount << " EUR\n";
    }
};

int main() {
    std::vector<std::unique_ptr<PaymentMethod>> payments;
    payments.push_back(std::make_unique<CreditCardPayment>("TX1001", "1234567890123456"));
    payments.push_back(std::make_unique<PayPalPayment>("TX1002", "student@dit.gr"));

    double amounts[] = {49.99, 120.00};

    for (size_t i = 0; i < payments.size(); ++i) {
        if (payments[i]->processPayment(amounts[i])) {
            payments[i]->printReceipt(amounts[i]);
        }
        std::cout << "-------------------------------------\n";
    }

    return 0;
}
```

