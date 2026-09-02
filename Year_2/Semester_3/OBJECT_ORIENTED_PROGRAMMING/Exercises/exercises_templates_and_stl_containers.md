# Ασκήσεις Εμπέδωσης: Πρότυπα (Templates) και Περιέκτες STL

## Άσκηση 1: Υλοποίηση Generic Κυκλικού Buffer (Circular Queue Template)
### Εκφώνηση:
Υλοποιήστε μια γενική κλάση προτύπου `CircularBuffer<T, Capacity>` σε C++ που υποστηρίζει:
- `push(const T& item)`: Εισαγωγή στοιχείου (πετάει `std::overflow_error` αν είναι γεμάτος).
- `pop()`: Αφαίρεση στοιχείου (πετάει `std::underflow_error` αν είναι κενός).
- `size() const`, `empty() const`, `full() const`.

### Λύση:
```cpp
#include <iostream>
#include <stdexcept>
#include <array>

template <typename T, size_t Capacity>
class CircularBuffer {
private:
    std::array<T, Capacity> buffer;
    size_t head = 0;
    size_t tail = 0;
    size_t count = 0;

public:
    bool empty() const { return count == 0; }
    bool full() const { return count == Capacity; }
    size_t size() const { return count; }

    void push(const T& item) {
        if (full()) {
            throw std::overflow_error("Buffer is full");
        }
        buffer[tail] = item;
        tail = (tail + 1) % Capacity;
        ++count;
    }

    T pop() {
        if (empty()) {
            throw std::underflow_error("Buffer is empty");
        }
        T val = buffer[head];
        head = (head + 1) % Capacity;
        --count;
        return val;
    }
};
```

---

## Άσκηση 2: Επεξεργασία Συλλογών με STL Algorithms και Lambdas
### Εκφώνηση:
Δίνεται ένα διάνυσμα `std::vector<int> numbers = {12, 5, 8, 19, 24, 7, 30, 3, 16};`.
Χρησιμοποιώντας αποκλειστικά αλγορίθμους της `<algorithm>` και εκφράσεις λάμδα (lambdas):
1. Φιλτράρετε και κρατήστε μόνο τους άρτιους αριθμούς.
2. Ταξινομήστε τους κατά φθίνουσα σειρά.
3. Υπολογίστε το άθροισμά τους με `std::accumulate`.

### Λύση:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

int main() {
    std::vector<int> numbers = {12, 5, 8, 19, 24, 7, 30, 3, 16};

    // 1. Αφαίρεση περιττών αριθμών (Erase-Remove idiom)
    numbers.erase(
        std::remove_if(numbers.begin(), numbers.end(), [](int n) { return n % 2 != 0; }),
        numbers.end()
    );

    // 2. Ταξινόμηση κατά φθίνουσα σειρά
    std::sort(numbers.begin(), numbers.end(), [](int a, int b) { return a > b; });

    // 3. Άθροισμα
    int sum = std::accumulate(numbers.begin(), numbers.end(), 0);

    std::cout << "Artioi taxinomimenoi kata fthinousa: ";
    for (int n : numbers) std::cout << n << " ";
    std::cout << "\nAthroisma: " << sum << "\n";

    return 0;
}
```

