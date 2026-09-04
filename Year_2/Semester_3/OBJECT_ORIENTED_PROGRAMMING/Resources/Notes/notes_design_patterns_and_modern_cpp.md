# Deep-Dive Study Notes: Object-Oriented Design Patterns and Modern C++

This study guide examines software architectural design patterns (SOLID principles, GoF patterns) and their modern implementations in C++17/C++20.

---

## 1. The SOLID Principles

| Principle | Core Directive | Practical C++ Application |
|---|---|---|
| **Single Responsibility (SRP)** | A class should have one, and only one, reason to change. | Decouple business logic from persistence and network serialization. |
| **Open/Closed (OCP)** | Software entities should be open for extension, but closed for modification. | Use abstract base classes and virtual dispatch to add new behaviors without editing existing code. |
| **Liskov Substitution (LSP)** | Subtypes must be substitutable for their base types without altering correctness. | Derived classes must honor base preconditions and postconditions (avoid throwing unexpected exceptions). |
| **Interface Segregation (ISP)** | Clients should not be forced to depend on interfaces they do not use. | Favor many fine-grained interfaces over one monolithic general-purpose interface. |
| **Dependency Inversion (DIP)** | High-level modules should not depend on low-level modules; both should depend on abstractions. | Inject abstract dependencies (via smart pointers or references) rather than hardcoding concrete instances. |

---

## 2. Observer Pattern in C++

Enables one-to-many publish-subscribe communication:

```cpp
#include <iostream>
#include <vector>
#include <memory>
#include <algorithm>

class IObserver {
public:
    virtual ~IObserver() = default;
    virtual void update(int temperature) = 0;
};

class WeatherStation {
private:
    std::vector<IObserver*> observers_;
    int temperature_{0};

public:
    void attach(IObserver* obs) {
        observers_.push_back(obs);
    }

    void detach(IObserver* obs) {
        observers_.erase(std::remove(observers_.begin(), observers_.end(), obs), observers_.end());
    }

    void setTemperature(int temp) {
        temperature_ = temp;
        notify();
    }

    void notify() {
        for (auto* obs : observers_) {
            obs->update(temperature_);
        }
    }
};

class PhoneDisplay : public IObserver {
public:
    void update(int temp) override {
        std::cout << "PhoneDisplay updated: Temperature is " << temp << " C\n";
    }
};
```

