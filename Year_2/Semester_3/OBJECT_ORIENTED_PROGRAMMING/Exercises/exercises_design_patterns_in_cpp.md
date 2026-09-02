# Ασκήσεις Εμπέδωσης: Σχεδιαστικά Πρότυπα (Design Patterns) σε C++

## Άσκηση 1: Υλοποίηση Thread-Safe Singleton (Meyers' Singleton)
### Εκφώνηση:
Υλοποιήστε το σχεδιαστικό πρότυπο Singleton για μια κλάση διαχείρισης ρυθμίσεων συστήματος `ConfigurationManager` στη σύγχρονη C++ (Meyers' Singleton), εξασφαλίζοντας thread-safety χωρίς χειροκίνητα mutex locks.

### Λύση:
```cpp
#include <iostream>
#include <string>
#include <unordered_map>

class ConfigurationManager {
private:
    std::unordered_map<std::string, std::string> settings;

    // Private Constructor
    ConfigurationManager() {
        std::cout << "[Config] Arxikopoiisi Configuration Manager (Meyers Singleton).\n";
        settings["app_name"] = "DitOpenNotes";
        settings["version"] = "2.0.0";
    }

    // Απαγόρευση αντιγραφής και ανάθεσης
    ConfigurationManager(const ConfigurationManager&) = delete;
    ConfigurationManager& operator=(const ConfigurationManager&) = delete;

public:
    // Στατική μέθοδος ανάκτησης του μοναδικού instance (C++11 thread-safe static initialization)
    static ConfigurationManager& getInstance() {
        static ConfigurationManager instance;
        return instance;
    }

    std::string getSetting(const std::string& key) const {
        auto it = settings.find(key);
        if (it != settings.end()) {
            return it->second;
        }
        return "";
    }

    void setSetting(const std::string& key, const std::string& val) {
        settings[key] = val;
    }
};

int main() {
    auto& config1 = ConfigurationManager::getInstance();
    std::cout << "App Name: " << config1.getSetting("app_name") << "\n";

    auto& config2 = ConfigurationManager::getInstance();
    config2.setSetting("theme", "dark");

    std::cout << "Theme meso config1: " << config1.getSetting("theme") << "\n";
    return 0;
}
```

---

## Άσκηση 2: Σχεδιαστικό Πρότυπο Εργοστασίου (Factory Pattern)
### Εκφώνηση:
Υλοποιήστε ένα `LoggerFactory` που παράγει αντικείμενα τύπου `ConsoleLogger` ή `FileLogger` που κληρονομούν από τη διεπαφή `ILogger`.

### Λύση:
```cpp
#include <iostream>
#include <memory>
#include <string>

class ILogger {
public:
    virtual ~ILogger() = default;
    virtual void log(const std::string& message) = 0;
};

class ConsoleLogger : public ILogger {
public:
    void log(const std::string& message) override {
        std::cout << "[CONSOLE LOG]: " << message << "\n";
    }
};

class FileLogger : public ILogger {
private:
    std::string filename;
public:
    FileLogger(const std::string& file) : filename(file) {}
    void log(const std::string& message) override {
        std::cout << "[FILE LOG to " << filename << "]: " << message << "\n";
    }
};

enum class LoggerType { CONSOLE, FILE };

class LoggerFactory {
public:
    static std::unique_ptr<ILogger> createLogger(LoggerType type, const std::string& param = "") {
        switch (type) {
            case LoggerType::CONSOLE:
                return std::make_unique<ConsoleLogger>();
            case LoggerType::FILE:
                return std::make_unique<FileLogger>(param.empty() ? "app.log" : param);
            default:
                return nullptr;
        }
    }
};
```

