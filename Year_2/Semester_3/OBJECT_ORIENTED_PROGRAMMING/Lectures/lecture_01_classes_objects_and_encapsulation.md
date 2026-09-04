# Lecture 01: Classes, Objects, and Encapsulation

This lecture introduces the foundational concepts of Object-Oriented Programming (OOP) in C++, focusing on class design, information hiding through access specifiers, constructor types, destructor semantics, and member initialization lists.

---

## 1. Paradigm Shift: Procedural vs. Object-Oriented

Procedural programming models computation as a sequence of functions transforming decoupled passive data structures. In contrast, Object-Oriented Programming binds data (attributes) and operations (methods) into self-contained entities called **objects**, enforcing modularity and contracts.

### Core OOP Tenets:
1. **Encapsulation:** Packaging attributes and behaviors while restricting direct access to internal state.
2. **Abstraction:** Exposing essential interfaces while concealing implementation complexities.
3. **Inheritance:** Establishing hierarchical relationships to foster reuse and taxonomy.
4. **Polymorphism:** Enabling uniform interfaces to manipulate entities of varying underlying types.

---

## 2. Class Syntax and Access Modifiers

In C++, access specifiers dictate the visibility of class members:

| Specifier | Visibility Inside Class | Visibility in Derived Classes | Visibility from Outside / Client |
|---|---|---|---|
| `private` | Yes | No | No |
| `protected`| Yes | Yes | No |
| `public` | Yes | Yes | Yes |

```cpp
#include <string>
#include <stdexcept>

class BankAccount {
private:
    std::string account_number_;
    double balance_;

public:
    // Parameterized constructor with member initializer list
    BankAccount(std::string account_number, double initial_balance)
        : account_number_(std::move(account_number)), balance_(initial_balance) {
        if (balance_ < 0.0) {
            throw std::invalid_argument("Initial balance cannot be negative.");
        }
    }

    // Accessor (getter) marked const to guarantee state immutability
    [[nodiscard]] double getBalance() const noexcept {
        return balance_;
    }

    [[nodiscard]] const std::string& getAccountNumber() const noexcept {
        return account_number_;
    }

    // Mutator with invariant validation
    void deposit(double amount) {
        if (amount <= 0.0) {
            throw std::invalid_argument("Deposit amount must be positive.");
        }
        balance_ += amount;
    }

    bool withdraw(double amount) {
        if (amount <= 0.0 || amount > balance_) {
            return false;
        }
        balance_ -= amount;
        return true;
    }
};
```

---

## 3. Constructors and Object Lifecycle

Constructors initialize an object's invariant state upon allocation.

### 3.1 Member Initializer Lists
Constructing member fields inside the constructor body (`{ balance_ = initial_balance; }`) first default-initializes the field and then overwrites it via assignment.
The **Member Initializer List** (`: field_(val)`) constructs the object directly in-place, which is mandatory for:
- `const` member variables.
- Reference (`&`) member variables.
- Member objects that lack a default constructor.

### 3.2 Constructor Types
1. **Default Constructor:** Accepts zero parameters (`ClassName() = default;`).
2. **Parameterized Constructor:** Accepts application parameters to configure state.
3. **Copy Constructor:** Constructs a new object as a copy of an existing object of the same type (`ClassName(const ClassName& other)`).
4. **Move Constructor (C++11):** Transfers ownership of dynamic resources from a temporary rvalue without copying (`ClassName(ClassName&& other) noexcept`).

---

## 4. The `this` Pointer and `const` Member Functions

- **`this` Pointer:** An implicit pointer passed to all non-static member functions, holding the address of the invoking object (`this->attribute`).
- **`const` Correctness:** Member functions that do not modify the object's observable logical state must be marked `const`. A `const` method can be invoked on both const and non-const object instances.

---

## 5. Summary

- Encapsulation hides internal representation to protect class invariants.
- Access specifiers (`private`, `protected`, `public`) control the boundary between implementation and interface.
- Member initializer lists avoid redundant initialization and are mandatory for references and constants.
- `const` member functions enforce immutability contracts checked at compile-time.

