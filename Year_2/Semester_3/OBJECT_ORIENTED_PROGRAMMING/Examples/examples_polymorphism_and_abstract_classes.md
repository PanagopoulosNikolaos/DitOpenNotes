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
        std::cout << "[CreditCard] Χρέωση " << amount << " EUR στην κάρτα ****" 
                  << card_number.substr(card_number.length() - 4) << "\n";
        return true;
    }

    void printReceipt(double amount) const override {
        std::cout << "Απόδειξη [CreditCard] TxID: " << transaction_id 
                  << " | Ποσό: " << amount << " EUR\n";
    }
};

class PayPalPayment : public PaymentMethod {
private:
    std::string email;

public:
    PayPalPayment(const std::string& id, const std::string& mail)
        : PaymentMethod(id), email(mail) {}

    bool processPayment(double amount) override {
        std::cout << "[PayPal] Πληρωμή " << amount << " EUR μέσω λογαριασμού: " << email << "\n";
        return true;
    }

    void printReceipt(double amount) const override {
        std::cout << "Απόδειξη [PayPal] TxID: " << transaction_id 
                  << " | Email: " << email << " | Ποσό: " << amount << " EUR\n";
    }
};

class CryptoPayment : public PaymentMethod {
private:
    std::string wallet_address;

public:
    CryptoPayment(const std::string& id, const std::string& wallet)
        : PaymentMethod(id), wallet_address(wallet) {}

    bool processPayment(double amount) override {
        std::cout << "[Crypto] Μεταφορά ισότιμου ποσού " << amount 
                  << " EUR στο πορτοφόλι " << wallet_address.substr(0, 6) << "..." << "\n";
        return true;
    }

    void printReceipt(double amount) const override {
        std::cout << "Απόδειξη [Crypto] TxID: " << transaction_id 
                  << " | Διεύθυνση: " << wallet_address << " | Ποσό: " << amount << " EUR\n";
    }
};

int main() {
    std::vector<std::unique_ptr<PaymentMethod>> payments;
    payments.push_back(std::make_unique<CreditCardPayment>("TX1001", "1234567890123456"));
    payments.push_back(std::make_unique<PayPalPayment>("TX1002", "student@dit.gr"));
    payments.push_back(std::make_unique<CryptoPayment>("TX1003", "0x71C...B29"));

    double amounts[] = {49.99, 120.00, 350.50};

    for (size_t i = 0; i < payments.size(); ++i) {
        if (payments[i]->processPayment(amounts[i])) {
            payments[i]->printReceipt(amounts[i]);
        }
        std::cout << "-------------------------------------\n";
    }

    return 0;
}
```

