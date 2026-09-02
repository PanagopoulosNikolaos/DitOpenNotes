# Πλήρης Οδηγός C++: Από τα Βασικά στο Προχωρημένο ΑΠ

Αυτός ο οδηγός καλύπτει τον προγραμματισμό σε C++ από τις θεμελιώδεις έννοιες έως τις προχωρημένες αρχές του Αντικειμενοστραφούς Προγραμματισμού. Κάθε ενότητα βασίζεται στην προηγούμενη, παρέχοντας μια πλήρη πορεία μάθησης για αρχάριους έως επαγγελματικό επίπεδο προγραμματισμού σε C++.

## Πίνακας Περιεχομένων
1. [Βασική Εκτύπωση (Έξοδος/Είσοδος)](#βασική-εκτύπωση-έξοδοςείσοδος)
2. [Μεταβλητές και Τύποι Δεδομένων](#μεταβλητές-και-τύποι-δεδομένων)
3. [Έλεγχος Ροής (If/Else, Switch)](#έλεγχος-ροής-ifelse-switch)
4. [Βρόχοι (For, While)](#βρόχοι-for-while)
5. [Πίνακες (Arrays)](#πίνακες-arrays)
6. [Συναρτήσεις (Πέρασμα-κατά-τιμή έναντι Πέρασμα-κατά-αναφορά)](#συναρτήσεις-πέρασμα-κατά-τιμή-έναντι-πέρασμα-κατά-αναφορά)
7. [Δείκτες και Αναφορές](#δείκτες-και-αναφορές)
8. [Διανύσματα (Δυναμικοί Πίνακες)](#διανύσματα-δυναμικοί-πίνακες)
9. [Χάρτες (Συσχετιστικά Περιέκτες)](#χάρτες-συσχετιστικά-περιέκτες)
10. [Κλάσεις και Αντικείμενα (Τα Βασικά)](#κλάσεις-και-αντικείμενα-τα-βασικά)
11. [Κατασκευαστές και Καταστροφείς](#κατασκευαστές-και-καταστροφείς)
12. [Ο Δείκτης `this`](#ο-δείκτης-this)
13. [Αρχές Αντικειμενοστραφούς Προγραμματισμού (Ενθυλάκωση, Αφαίρεση)](#αρχές-αντικειμενοστραφούς-προγραμματισμού-ενθυλάκωση-αφαίρεση)
14. [Κληρονομικότητα και Πολυμορφισμός](#κληρονομικότητα-και-πολυμορφισμός)
15. [Προχωρημένη Διαχείριση Μνήμης (Σωρός έναντι Στοίβας, Έξυπνοι Δείκτες)](#προχωρημένη-διαχείριση-μνήμης-σωρός-έναντι-στοίβας-έξυπνοι-δείκτες)

---

## Βασική Εκτύπωση (Έξοδος/Είσοδος)

### Πρόγραμμα Hello World
```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Hello, World!" << endl;
    return 0;
}
```

### Επεξήγηση:
- `#include <iostream>`: Περιλαμβάνει τη βιβλιοθήκη ροών εισόδου/εξόδου
- `cout`: Το αντικείμενο ροής εξόδου κονσόλας
- `<<`: Ο τελεστής εισαγωγής ροής
- `endl`: Εισάγει νέα γραμμή και αδειάζει τον προσωρινό χώρο

### Πολλαπλές Εντολές Εκτύπωσης
```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "First line" << endl;
    cout << "Second line" << endl;
    cout << "Number: " << 42 << endl;
    cout << "Decimal: " << 3.14 << endl;
    return 0;
}
```

### Είσοδος από τον Χρήστη
```cpp
#include <iostream>
using namespace std;

int main() {
    int number;
    string name;
    
    cout << "Enter your name: ";
    cin >> name;
    cout << "Hello, " << name << "!" << endl;
    
    cout << "Enter a number: ";
    cin >> number;
    cout << "You entered: " << number << endl;
    
    return 0;
}
```

### Χρήση printf (Στυλ C)
```cpp
#include <cstdio>

int main() {
    printf("Hello, World!\n");
    printf("Number: %d\n", 42);
    printf("Float: %.2f\n", 3.14159);
    return 0;
}
```

---

## Μεταβλητές και Τύποι Δεδομένων

### Θεμελιώδεις Τύποι Δεδομένων
```cpp
#include <iostream>
using namespace std;

int main() {
    // Ακέραιοι τύποι
    int integer_var = 42;           // Κανονικός ακέραιος
    short short_var = 100;          // Σύντομος ακέραιος
    long long_var = 100000L;        // Μακρύς ακέραιος
    long long very_long = 1000000LL; // Πολύ μακρύς ακέραιος
    
    // Τύποι κινητής υποδιαστολής
    float float_var = 3.14f;        // Απλή ακρίβεια
    double double_var = 3.14159;    // Διπλή ακρίβεια
    long double long_double = 3.141592653589L; // Εκτεταμένη ακρίβεια
    
    // Τύποι χαρακτήρων
    char char_var = 'A';            // Μεμονωμένος χαρακτήρας
    wchar_t wide_char = L'B';       // Ευρύς χαρακτήρας
    char16_t utf16_char = u'C';     // Χαρακτήρας UTF-16
    char32_t utf32_char = U'D';     // Χαρακτήρας UTF-32
    
    // Λογικός τύπος
    bool bool_var = true;           // Λογική τιμή (true/false)
    
    // Σταθερές
    const int constant = 100;       // Σταθερή τιμή
    
    // Εκτύπωση όλων των μεταβλητών
    cout << "Integer: " << integer_var << endl;
    cout << "Short: " << short_var << endl;
    cout << "Long: " << long_var << endl;
    cout << "Very Long: " << very_long << endl;
    cout << "Float: " << float_var << endl;
    cout << "Double: " << double_var << endl;
    cout << "Long Double: " << long_double << endl;
    cout << "Char: " << char_var << endl;
    cout << "Bool: " << bool_var << endl;
    
    return 0;
}
```

### Δήλωση και Αρχικοποίηση Μεταβλητών
```cpp
#include <iostream>
using namespace std;

int main() {
    // Διαφορετικοί τρόποι αρχικοποίησης μεταβλητών
    int a = 5;              // Αρχικοποίηση αντιγραφής
    int b{10};              // Άμεση αρχικοποίηση (C++11)
    int c{};                // Αρχικοποίηση τιμής (προεπιλεγμένη τιμή)
    
    // Συμπερασμός τύπου
    auto x = 42;            // Το x συμπεραίνεται ως int
    auto y = 3.14;          // Το y συμπεραίνεται ως double
    auto z = 'A';           // Το z συμπεραίνεται ως char
    
    // Πολλαπλές δηλώσεις
    int width = 10, height = 20, area = width * height;
    
    cout << "Width: " << width << ", Height: " << height << ", Area: " << area << endl;
    cout << "Auto x: " << x << ", y: " << y << ", z: " << z << endl;
    
    return 0;
}
```

---

## Έλεγχος Ροής (If/Else, Switch)

### Εντολές If-Else
```cpp
#include <iostream>
using namespace std;

int main() {
    int score = 85;
    
    // Απλή εντολή if
    if (score >= 90) {
        cout << "Grade: A" << endl;
    }
    
    // Εντολή if-else
    if (score >= 80) {
        cout << "Grade: B" << endl;
    } else {
        cout << "Grade: Below B" << endl;
    }
    
    // Κλίμακα if-else if
    if (score >= 90) {
        cout << "Excellent!" << endl;
    } else if (score >= 80) {
        cout << "Good job!" << endl;
    } else if (score >= 70) {
        cout << "Average" << endl;
    } else {
        cout << "Needs improvement" << endl;
    }
    
    // Ένθετες εντολές if
    int age = 20;
    bool hasLicense = true;
    
    if (age >= 18) {
        if (hasLicense) {
            cout << "Eligible to drive" << endl;
        } else {
            cout << "Eligible for license" << endl;
        }
    } else {
        cout << "Not eligible to drive" << endl;
    }
    
    return 0;
}
```

### Εντολή Switch
```cpp
#include <iostream>
using namespace std;

int main() {
    int day = 3;
    
    switch (day) {
        case 1:
            cout << "Monday" << endl;
            break;
        case 2:
            cout << "Tuesday" << endl;
            break;
        case 3:
            cout << "Wednesday" << endl;
            break;
        case 4:
            cout << "Thursday" << endl;
            break;
        case 5:
            cout << "Friday" << endl;
            break;
        case 6:
            cout << "Saturday" << endl;
            break;
        case 7:
            cout << "Sunday" << endl;
            break;
        default:
            cout << "Invalid day" << endl;
    }
    
    // Switch με χαρακτήρα
    char grade = 'B';
    
    switch (grade) {
        case 'A':
        case 'B':
            cout << "Good performance" << endl;
            break;
        case 'C':
            cout << "Average performance" << endl;
            break;
        case 'D':
        case 'F':
            cout << "Poor performance" << endl;
            break;
        default:
            cout << "Invalid grade" << endl;
    }
    
    return 0;
}
```

### Τριαδικός Τελεστής (Τελεστής Συνθήκης)
```cpp
#include <iostream>
using namespace std;

int main() {
    int age = 20;
    string status;
    
    // Χρήση τριαδικού τελεστή
    status = (age >= 18) ? "Adult" : "Minor";
    cout << "Status: " << status << endl;
    
    // Ένθετοι τριαδικοί τελεστές
    int score = 85;
    string result = (score >= 90) ? "Excellent" :
                   (score >= 80) ? "Good" :
                   (score >= 70) ? "Average" : "Below Average";
    cout << "Result: " << result << endl;
    
    return 0;
}
```

---

## Βρόχοι (For, While)

### Βρόχος For
```cpp
#include <iostream>
using namespace std;

int main() {
    // Βασικός βρόχος for
    cout << "Counting from 1 to 5:" << endl;
    for (int i = 1; i <= 5; i++) {
        cout << i << " ";
    }
    cout << endl;
    
    // Βρόχος for με διαφορετική αύξηση
    cout << "Even numbers from 0 to 10:" << endl;
    for (int i = 0; i <= 10; i += 2) {
        cout << i << " ";
    }
    cout << endl;
    
    // Βρόχος for με μείωση
    cout << "Counting down from 5 to 1:" << endl;
    for (int i = 5; i >= 1; i--) {
        cout << i << " ";
    }
    cout << endl;
    
    // Βρόχος for βασισμένος σε εύρος (C++11)
    int numbers[] = {1, 2, 3, 4, 5};
    cout << "Using range-based for loop:" << endl;
    for (int num : numbers) {
        cout << num << " ";
    }
    cout << endl;
    
    return 0;
}
```

### Βρόχος While
```cpp
#include <iostream>
using namespace std;

int main() {
    int count = 1;
    
    cout << "Using while loop:" << endl;
    while (count <= 5) {
        cout << count << " ";
        count++;
    }
    cout << endl;
    
    // Βρόχος while με αλλαγή συνθήκης
    int num = 10;
    cout << "Dividing by 2 until less than 1:" << endl;
    while (num > 1) {
        cout << num << " ";
        num /= 2;
    }
    cout << endl;
    
    return 0;
}
```

### Βρόχος Do-While
```cpp
#include <iostream>
using namespace std;

int main() {
    int count = 1;
    
    cout << "Using do-while loop:" << endl;
    do {
        cout << count << " ";
        count++;
    } while (count <= 5);
    cout << endl;
    
    // Το do-while εγγυάται τουλάχιστον μία εκτέλεση
    int condition = 0;
    cout << "Do-while executes at least once:" << endl;
    do {
        cout << "This will print once even if condition is false" << endl;
    } while (condition != 0);
    
    return 0;
}
```

### Ένθετοι Βρόχοι
```cpp
#include <iostream>
using namespace std;

int main() {
    // Πίνακας πολλαπλασιασμού
    cout << "Multiplication Table (1-5):" << endl;
    for (int i = 1; i <= 5; i++) {
        for (int j = 1; j <= 5; j++) {
            cout << i * j << "\t";
        }
        cout << endl;
    }
    
    // Εκτύπωση σχήματος
    cout << "\nRight triangle pattern:" << endl;
    for (int i = 1; i <= 5; i++) {
        for (int j = 1; j <= i; j++) {
            cout << "* ";
        }
        cout << endl;
    }
    
    return 0;
}
```

### Εντολές Ελέγχου Βρόχου
```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Using continue and break:" << endl;
    
    // Παράλειψη ζυγών αριθμών με continue
    cout << "Odd numbers from 1 to 10:" << endl;
    for (int i = 1; i <= 10; i++) {
        if (i % 2 == 0) {
            continue;  // Παράλειψη ζυγών αριθμών
        }
        cout << i << " ";
    }
    cout << endl;
    
    // Σταμάτημα στο 5 με break
    cout << "Numbers from 1 to 10, stopping at 5:" << endl;
    for (int i = 1; i <= 10; i++) {
        if (i > 5) {
            break;  // Έξοδος από τον βρόχο όταν i > 5
        }
        cout << i << " ";
    }
    cout << endl;
    
    return 0;
}
```

---

## Πίνακες (Arrays)

### Βασικοί Πίνακες
```cpp
#include <iostream>
#include <array>
#include <iomanip>
using namespace std;

int main() {
    // Παραδοσιακοί πίνακες στυλ C
    int traditionalArray[5] = {10, 20, 30, 40, 50};
    
    // C++ std::array (προτιμότερο)
    array<int, 5> cppArray = {100, 200, 300, 400, 500};
    
    // Πίνακας double
    double prices[] = {19.99, 29.99, 39.99, 49.99};
    
    // Πίνακας συμβολοσειρών
    string names[3] = {"Alice", "Bob", "Charlie"};
    
    cout << "Traditional array: ";
    for (int i = 0; i < 5; i++) {
        cout << traditionalArray[i] << " ";
    }
    cout << endl;
    
    cout << "C++ array: ";
    for (size_t i = 0; i < cppArray.size(); i++) {
        cout << cppArray[i] << " ";
    }
    cout << endl;
    
    cout << "Prices array: ";
    for (int i = 0; i < sizeof(prices)/sizeof(prices[0]); i++) {
        cout << fixed << setprecision(2) << prices[i] << " ";
    }
    cout << endl;
    
    cout << "Names array: ";
    for (const string& name : names) {
        cout << name << " ";
    }
    cout << endl;
    
    // Πολυδιάστατοι πίνακες
    int matrix[3][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };
    
    cout << "\n2D Array (Matrix):" << endl;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
    
    // Παράδειγμα 3D πίνακα
    int cube[2][2][2] = {
        {{1, 2}, {3, 4}},
        {{5, 6}, {7, 8}}
    };
    
    cout << "\n3D Array (Cube):" << endl;
    for (int i = 0; i < 2; i++) {
        cout << "Layer " << i << ":" << endl;
        for (int j = 0; j < 2; j++) {
            for (int k = 0; k < 2; k++) {
                cout << cube[i][j][k] << " ";
            }
            cout << endl;
        }
        cout << endl;
    }
    
    return 0;
}
```

### Λειτουργίες και Αλγόριθμοι Πινάκων
```cpp
#include <iostream>
#include <array>
#include <algorithm>
#include <numeric>
#include <iterator>
using namespace std;

int main() {
    array<int, 10> numbers = {5, 2, 8, 1, 9, 3, 7, 4, 6, 0};
    
    cout << "Original array: ";
    for (int n : numbers) cout << n << " ";
    cout << endl;
    
    // Ταξινόμηση του πίνακα
    sort(numbers.begin(), numbers.end());
    cout << "Sorted: ";
    for (int n : numbers) cout << n << " ";
    cout << endl;
    
    // Αντιστροφή του πίνακα
    reverse(numbers.begin(), numbers.end());
    cout << "Reversed: ";
    for (int n : numbers) cout << n << " ";
    cout << endl;
    
    // Εύρεση μεγίστου και ελαχίστου
    auto minMax = minmax_element(numbers.begin(), numbers.end());
    cout << "Min: " << *(minMax.first) << ", Max: " << *(minMax.second) << endl;
    
    // Υπολογισμός αθροίσματος
    int sum = accumulate(numbers.begin(), numbers.end(), 0);
    cout << "Sum: " << sum << endl;
    
    // Μέτρηση εμφανίσεων
    int count = count(numbers.begin(), numbers.end(), 5);
    cout << "Count of 5: " << count << endl;
    
    // Γέμισμα πίνακα με τιμή
    array<int, 5> filledArray;
    fill(filledArray.begin(), filledArray.end(), 42);
    cout << "Filled with 42: ";
    for (int n : filledArray) cout << n << " ";
    cout << endl;
    
    // Μερικό γέμισμα
    array<int, 10> partialFill = {};
    fill(partialFill.begin(), partialFill.begin() + 5, 7);
    cout << "Partially filled: ";
    for (int n : partialFill) cout << n << " ";
    cout << endl;
    
    // Πίνακας αντικειμένων
    struct Point {
        int x, y;
        Point(int x = 0, int y = 0) : x(x), y(y) {}
        void display() const { cout << "(" << x << "," << y << ") "; }
    };
    
    array<Point, 3> points = {Point(1, 2), Point(3, 4), Point(5, 6)};
    
    cout << "Array of Points: ";
    for (const Point& p : points) {
        p.display();
    }
    cout << endl;
    
    // Επανάληψη πίνακα με δείκτες
    cout << "Index-value pairs: ";
    for (size_t i = 0; i < numbers.size(); i++) {
        cout << "[" << i << "]=" << numbers[i] << " ";
    }
    cout << endl;
    
    // Χρήση επαναληπτών (iterators)
    cout << "Using iterators: ";
    for (auto it = numbers.begin(); it != numbers.end(); ++it) {
        cout << *it << " ";
    }
    cout << endl;
    
    return 0;
}
```

### Δυναμικοί Πίνακες και Διαχείριση Μνήμης
```cpp
#include <iostream>
#include <vector>
#include <memory>
using namespace std;

int main() {
    // Δυναμικός πίνακας με new
    int size = 5;
    int* dynamicArray = new int[size];
    
    // Αρχικοποίηση του δυναμικού πίνακα
    for (int i = 0; i < size; i++) {
        dynamicArray[i] = (i + 1) * 10;
    }
    
    cout << "Dynamic array: ";
    for (int i = 0; i < size; i++) {
        cout << dynamicArray[i] << " ";
    }
    cout << endl;
    
    // Αλλαγή μεγέθους πίνακα (χειροκίνητη υλοποίηση)
    int newSize = 8;
    int* resizedArray = new int[newSize];
    
    // Αντιγραφή παλαιών τιμών
    for (int i = 0; i < size; i++) {
        resizedArray[i] = dynamicArray[i];
    }
    
    // Αρχικοποίηση νέων στοιχείων
    for (int i = size; i < newSize; i++) {
        resizedArray[i] = (i + 1) * 100;
    }
    
    cout << "Resized array: ";
    for (int i = 0; i < newSize; i++) {
        cout << resizedArray[i] << " ";
    }
    cout << endl;
    
    // Καθαρισμός δυναμικά δεσμευμένης μνήμης
    delete[] dynamicArray;
    delete[] resizedArray;
    
    // Καλύτερη προσέγγιση: Χρήση έξυπνων δεικτών
    unique_ptr<int[]> smartArray(new int[6]);
    for (int i = 0; i < 6; i++) {
        smartArray[i] = (i + 1) * 5;
    }
    
    cout << "Smart pointer array: ";
    for (int i = 0; i < 6; i++) {
        cout << smartArray[i] << " ";
    }
    cout << endl;
    // Δεν χρειάζεται χειροκίνητη διαγραφή - αυτόματος καθαρισμός
    
    // Χρήση vector αντί για χειροκίνητους δυναμικούς πίνακες (συνιστάται)
    cout << "\nUsing vector (recommended approach):" << endl;
    vector<int> recommendedArray = {10, 20, 30, 40, 50};
    
    cout << "Initial vector: ";
    for (int n : recommendedArray) cout << n << " ";
    cout << endl;
    
    // Προσθήκη στοιχείων
    recommendedArray.push_back(60);
    recommendedArray.push_back(70);
    
    cout << "After adding elements: ";
    for (int n : recommendedArray) cout << n << " ";
    cout << endl;
    
    // Αφαίρεση στοιχείων
    recommendedArray.pop_back();
    
    cout << "After removing last element: ";
    for (int n : recommendedArray) cout << n << " ";
    cout << endl;
    
    // Πολυδιάστατοι δυναμικοί πίνακες
    int rows = 3, cols = 4;
    int** matrix = new int*[rows];
    for (int i = 0; i < rows; i++) {
        matrix[i] = new int[cols];
    }
    
    // Αρχικοποίηση του πίνακα
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            matrix[i][j] = i * cols + j;
        }
    }
    
    cout << "\nDynamic 2D array:" << endl;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            cout << matrix[i][j] << "\t";
        }
        cout << endl;
    }
    
    // Καθαρισμός 2D πίνακα
    for (int i = 0; i < rows; i++) {
        delete[] matrix[i];
    }
    delete[] matrix;
    
    return 0;
}
```

---

## Συναρτήσεις (Πέρασμα-κατά-τιμή έναντι Πέρασμα-κατά-αναφορά)

### Βασικός Ορισμός Συνάρτησης
```cpp
#include <iostream>
using namespace std;

// Δήλωση συνάρτησης
void greet();
int add(int a, int b);
double calculateArea(double radius);

int main() {
    // Κλήσεις συναρτήσεων
    greet();
    
    int sum = add(10, 20);
    cout << "Sum: " << sum << endl;
    
    double area = calculateArea(5.0);
    cout << "Area of circle: " << area << endl;
    
    return 0;
}

// Ορισμοί συναρτήσεων
void greet() {
    cout << "Hello, welcome to C++ functions!" << endl;
}

int add(int a, int b) {
    return a + b;
}

double calculateArea(double radius) {
    const double PI = 3.14159;
    return PI * radius * radius;
}
```

### Παράμετροι Συνάρτησης και Τύποι Επιστροφής
```cpp
#include <iostream>
#include <string>
using namespace std;

// Συνάρτηση με πολλαπλές παραμέτρους
int multiply(int x, int y, int z) {
    return x * y * z;
}

// Συνάρτηση με προεπιλεγμένες παραμέτρους
int power(int base, int exp = 2) {
    int result = 1;
    for (int i = 0; i < exp; i++) {
        result *= base;
    }
    return result;
}

// Συνάρτηση που επιστρέφει πολλαπλές τιμές μέσω αναφοράς
void swapValues(int& a, int& b) {
    int temp = a;
    a = b;
    b = temp;
}

// Συνάρτηση με παράμετρο συμβολοσειράς
string repeatString(const string& str, int times) {
    string result = "";
    for (int i = 0; i < times; i++) {
        result += str;
    }
    return result;
}

int main() {
    cout << "Product: " << multiply(2, 3, 4) << endl;
    cout << "Power (default): " << power(3) << endl;  // Χρησιμοποιεί προεπιλεγμένο εκθέτη 2
    cout << "Power (custom): " << power(3, 4) << endl;  // Χρησιμοποιεί προσαρμοσμένο εκθέτη
    
    int x = 10, y = 20;
    cout << "Before swap: x = " << x << ", y = " << y << endl;
    swapValues(x, y);
    cout << "After swap: x = " << x << ", y = " << y << endl;
    
    cout << "Repeated string: " << repeatString("Hello ", 3) << endl;
    
    return 0;
}
```

### Πέρασμα-κατά-τιμή έναντι Πέρασμα-κατά-αναφορά
```cpp
#include <iostream>
using namespace std;

// Πέρασμα-κατά-τιμή: η συνάρτηση λαμβάνει αντίγραφο
void modifyByValue(int x) {
    x = 100;  // Τροποποιεί μόνο το τοπικό αντίγραφο
    cout << "Inside modifyByValue: x = " << x << endl;
}

// Πέρασμα-κατά-αναφορά: η συνάρτηση λαμβάνει αναφορά
void modifyByReference(int& x) {
    x = 200;  // Τροποποιεί την αρχική μεταβλητή
    cout << "Inside modifyByReference: x = " << x << endl;
}

// Πέρασμα-κατά-σταθερή-αναφορά: αποτρέπει την τροποποίηση
void printByConstReference(const int& x) {
    // x = 30;  // Αυτό θα προκαλούσε σφάλμα μεταγλώττισης
    cout << "Inside printByConstReference: x = " << x << endl;
}

// Πέρασμα-κατά-δείκτη
void modifyByPointer(int* x) {
    if (x != nullptr) {
        *x = 300;  // Τροποποιεί την αρχική μεταβλητή
        cout << "Inside modifyByPointer: *x = " << *x << endl;
    }
}

int main() {
    int value = 42;
    
    cout << "Original value: " << value << endl;
    
    // Πέρασμα-κατά-τιμή
    modifyByValue(value);
    cout << "After modifyByValue: " << value << endl;
    
    // Πέρασμα-κατά-αναφορά
    modifyByReference(value);
    cout << "After modifyByReference: " << value << endl;
    
    // Πέρασμα-κατά-σταθερή-αναφορά
    printByConstReference(value);
    cout << "After printByConstReference: " << value << endl;
    
    // Πέρασμα-κατά-δείκτη
    modifyByPointer(&value);
    cout << "After modifyByPointer: " << value << endl;
    
    return 0;
}
```

### Υπερφόρτωση Συναρτήσεων
```cpp
#include <iostream>
#include <string>
using namespace std;

// Υπερφόρτωση συναρτήσεων - ίδιο όνομα, διαφορετικές παράμετροι
void print(int value) {
    cout << "Integer: " << value << endl;
}

void print(double value) {
    cout << "Double: " << value << endl;
}

void print(const string& value) {
    cout << "String: " << value << endl;
}

void print(int a, int b) {
    cout << "Two integers: " << a << ", " << b << endl;
}

void print(int arr[], int size) {
    cout << "Array: ";
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    print(42);                    // Καλεί print(int)
    print(3.14);                  // Καλεί print(double)
    print("Hello");               // Καλεί print(string)
    print(10, 20);                // Καλεί print(int, int)
    
    int numbers[] = {1, 2, 3, 4, 5};
    print(numbers, 5);            // Καλεί print(array, size)
    
    return 0;
}
```

### Αναδρομικές Συναρτήσεις
```cpp
#include <iostream>
using namespace std;

// Υπολογισμός παραγοντικού με αναδρομή
long long factorial(int n) {
    if (n <= 1) {
        return 1;  // Βασική περίπτωση
    }
    return n * factorial(n - 1);  // Αναδρομική περίπτωση
}

// Ακολουθία Fibonacci με αναδρομή
long long fibonacci(int n) {
    if (n <= 1) {
        return n;  // Βασικές περιπτώσεις
    }
    return fibonacci(n - 1) + fibonacci(n - 2);  // Αναδρομική περίπτωση
}

// Υπολογισμός δύναμης με αναδρομή
int powerRecursive(int base, int exp) {
    if (exp == 0) {
        return 1;  // Βασική περίπτωση
    }
    if (exp == 1) {
        return base;  // Βασική περίπτωση
    }
    return base * powerRecursive(base, exp - 1);  // Αναδρομική περίπτωση
}

int main() {
    cout << "Factorial of 5: " << factorial(5) << endl;
    cout << "Fibonacci of 10: " << fibonacci(10) << endl;
    cout << "2^8: " << powerRecursive(2, 8) << endl;
    
    return 0;
}
```

---

## Δείκτες και Αναφορές

### Δείκτες
```cpp
#include <iostream>
using namespace std;

int main() {
    // Δήλωση και αρχικοποίηση δείκτη
    int value = 42;
    int* ptr = &value; // Ο ptr δείχνει στη διεύθυνση της value
    
    cout << "Value: " << value << endl;
    cout << "Address of value: " << &value << endl;
    cout << "Pointer value (address): " << ptr << endl;
    cout << "Value pointed to by ptr: " << *ptr << endl;
    
    // Αλλαγή τιμής μέσω δείκτη
    *ptr = 100;
    cout << "After changing through pointer, value: " << value << endl;
    
    // Αριθμητική δεικτών

    int arr[] = {10, 20, 30, 40, 50};
    int* arrPtr = arr;  // Δείχνει στο πρώτο στοιχείο
    
    cout << "\nArray elements using pointer arithmetic:" << endl;
    for (int i = 0; i < 5; i++) {
        cout << "Element " << i << ": " << *(arrPtr + i) << endl;
    }
    
    // Δείκτης σε δείκτη
    int** ptrToPtr = &ptr;
    cout << "\nValue through pointer to pointer: " << **ptrToPtr << endl;
    
    // Μηδενικός δείκτης
    int* nullPtr = nullptr;
    if (nullPtr == nullptr) {
        cout << "Pointer is null" << endl;
    }
    
    return 0;
}
```

### Αναφορές
```cpp
#include <iostream>
using namespace std;

int main() {
    int value = 42;
    
    // Δήλωση αναφοράς
    int& ref = value;  // Η ref είναι ψευδώνυμο για τη value
    
    cout << "Value: " << value << endl;
    cout << "Reference: " << ref << endl;
    
    // Τροποποίηση μέσω αναφοράς
    ref = 100;
    cout << "After modifying through reference, value: " << value << endl;
    
    // Αναφορές έναντι Δεικτών
    int x = 10;
    int y = 20;
    
    int& refX = x;  // Η αναφορά πρέπει να αρχικοποιηθεί
    cout << "refX = " << refX << endl;
    
    // refX = y;  // Αυτό αναθέτει την ΤΙΜΗ της y στο x, δεν κάνει τη refX να δείχνει στο y
    cout << "After refX = y, x = " << x << ", y = " << y << ", refX = " << refX << endl;
    
    // Παράδειγμα δείκτη για σύγκριση
    int* ptr = &x;
    ptr = &y;  // Τώρα ο ptr δείχνει στο y
    cout << "After ptr = &y, ptr points to value: " << *ptr << endl;
    
    return 0;
}
```

### Δείκτες και Συναρτήσεις
```cpp
#include <iostream>
using namespace std;

// Συνάρτηση που δέχεται δείκτη ως παράμετρο
void modifyThroughPointer(int* ptr) {
    if (ptr != nullptr) {
        *ptr = 100;
    }
}

// Συνάρτηση που επιστρέφει δείκτη
int* createInt(int value) {
    int* ptr = new int(value);
    return ptr;
}

// Συνάρτηση που δέχεται αναφορά ως παράμετρο
void modifyThroughReference(int& ref) {
    ref = 200;
}

int main() {
    int value = 42;
    
    cout << "Original value: " << value << endl;
    
    // Τροποποίηση μέσω δείκτη
    modifyThroughPointer(&value);
    cout << "After modifyThroughPointer: " << value << endl;
    
    // Τροποποίηση μέσω αναφοράς
    modifyThroughReference(value);
    cout << "After modifyThroughReference: " << value << endl;
    
    // Συνάρτηση που επιστρέφει δείκτη
    int* dynamicInt = createInt(300);
    cout << "Value from createInt: " << *dynamicInt << endl;
    
    // Μην ξεχνάτε να καθαρίσετε τη δυναμικά δεσμευμένη μνήμη
    delete dynamicInt;
    
    return 0;
}
```

---

## Διανύσματα (Δυναμικοί Πίνακες)

### Βασικές Λειτουργίες Διανυσμάτων
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int main() {
    // Δημιουργία διανυσμάτων
    vector<int> numbers;                    // Κενό διάνυσμα
    vector<int> numbers2(5, 10);           // Διάνυσμα με 5 στοιχεία, όλα 10
    vector<int> numbers3 = {1, 2, 3, 4, 5}; // Αρχικοποίηση με τιμές
    
    cout << "Empty vector size: " << numbers.size() << endl;
    cout << "Vector with 5 tens: ";
    for (int n : numbers2) cout << n << " ";
    cout << endl;
    
    cout << "Initialized vector: ";
    for (int n : numbers3) cout << n << " ";
    cout << endl;
    
    // Προσθήκη στοιχείων
    numbers.push_back(10);
    numbers.push_back(20);
    numbers.push_back(30);
    
    cout << "After adding elements: ";
    for (int n : numbers) cout << n << " ";
    cout << endl;
    
    // Πρόσβαση σε στοιχεία
    cout << "First element: " << numbers.front() << endl;
    cout << "Last element: " << numbers.back() << endl;
    cout << "Element at index 1: " << numbers[1] << endl;
    cout << "Element at index 1 (safe): " << numbers.at(1) << endl;
    
    // Επανάληψη με επαναλήπτες
    cout << "Using iterators: ";
    for (auto it = numbers.begin(); it != numbers.end(); ++it) {
        cout << *it << " ";
    }
    cout << endl;
    
    // Μέγεθος και χωρητικότητα
    cout << "Size: " << numbers.size() << ", Capacity: " << numbers.capacity() << endl;
    
    return 0;
}
```

### Μέθοδοι Χειρισμού Διανυσμάτων
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> numbers = {10, 20, 30, 40, 50};
    
    cout << "Original vector: ";
    for (int n : numbers) cout << n << " ";
    cout << endl;
    
    // Εισαγωγή στοιχείων
    numbers.insert(numbers.begin() + 2, 25);  // Εισαγωγή στη θέση 2
    cout << "After inserting 25 at pos 2: ";
    for (int n : numbers) cout << n << " ";
    cout << endl;
    
    // Εισαγωγή πολλαπλών στοιχείων
    vector<int> moreNumbers = {15, 17};
    numbers.insert(numbers.begin() + 1, moreNumbers.begin(), moreNumbers.end());
    cout << "After inserting multiple: ";
    for (int n : numbers) cout << n << " ";
    cout << endl;
    
    // Διαγραφή στοιχείων
    numbers.erase(numbers.begin() + 3);  // Αφαίρεση στοιχείου στη θέση 3
    cout << "After erasing position 3: ";
    for (int n : numbers) cout << n << " ";
    cout << endl;
    
    // Διαγραφή περιοχής
    numbers.erase(numbers.begin() + 1, numbers.begin() + 3);
    cout << "After erasing positions 1-2: ";
    for (int n : numbers) cout << n << " ";
    cout << endl;
    
    // Εκκαθάριση διανύσματος
    vector<int> temp = {1, 2, 3, 4, 5};
    cout << "Before clear: " << temp.size() << " elements" << endl;
    temp.clear();
    cout << "After clear: " << temp.size() << " elements" << endl;
    
    // Αλλαγή μεγέθους διανύσματος
    temp.resize(3, 0);  // Αλλαγή μεγέθους σε 3 στοιχεία, γέμισμα νέων με 0
    cout << "After resize to 3 with fill 0: ";
    for (int n : temp) cout << n << " ";
    cout << endl;
    
    temp.resize(6, 99);  // Αλλαγή μεγέθους σε 6 στοιχεία, γέμισμα νέων με 99
    cout << "After resize to 6 with fill 99: ";
    for (int n : temp) cout << n << " ";
    cout << endl;
    
    return 0;
}
```

### Αλγόριθμοι και Ταξινόμηση Διανυσμάτων
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
using namespace std;

int main() {
    vector<int> numbers = {5, 2, 8, 1, 9, 3, 7, 4, 6};
    
    cout << "Original vector: ";
    for (int n : numbers) cout << n << " ";
    cout << endl;
    
    // Ταξινόμηση διανύσματος
    sort(numbers.begin(), numbers.end());
    cout << "Sorted ascending: ";
    for (int n : numbers) cout << n << " ";
    cout << endl;
    
    // Ταξινόμηση σε φθίνουσα σειρά
    sort(numbers.rbegin(), numbers.rend());  // Αντίστροφοι επαναλήπτες
    cout << "Sorted descending: ";
    for (int n : numbers) cout << n << " ";
    cout << endl;
    
    // Εύρεση στοιχείου
    auto it = find(numbers.begin(), numbers.end(), 7);
    if (it != numbers.end()) {
        cout << "Found 7 at position: " << distance(numbers.begin(), it) << endl;
    } else {
        cout << "7 not found" << endl;
    }
    
    // Μέτρηση εμφανίσεων
    int count = count(numbers.begin(), numbers.end(), 5);
    cout << "Count of 5: " << count << endl;
    
    // Υπολογισμός αθροίσματος
    int sum = accumulate(numbers.begin(), numbers.end(), 0);
    cout << "Sum of all elements: " << sum << endl;
    
    // Ελάχιστο και μέγιστο
    auto minMax = minmax_element(numbers.begin(), numbers.end());
    cout << "Min: " << *(minMax.first) << ", Max: " << *(minMax.second) << endl;
    
    // Αντιστροφή διανύσματος
    reverse(numbers.begin(), numbers.end());
    cout << "Reversed: ";
    for (int n : numbers) cout << n << " ";
    cout << endl;
    
    // Μοναδικά στοιχεία (απαιτεί ταξινομημένο διάνυσμα)
    vector<int> sortedNums = {1, 1, 2, 2, 3, 4, 4, 5};
    auto last = unique(sortedNums.begin(), sortedNums.end());
    sortedNums.erase(last, sortedNums.end());
    cout << "Unique elements: ";
    for (int n : sortedNums) cout << n << " ";
    cout << endl;
    
    return 0;
}
```

### Διάνυσμα Αντικειμένων
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

class Person {
private:
    string name;
    int age;

public:
    Person(const string& n, int a) : name(n), age(a) {}
    
    const string& getName() const { return name; }
    int getAge() const { return age; }
    
    void display() const {
        cout << "Name: " << name << ", Age: " << age << endl;
    }
    
    // Τελεστής σύγκρισης για ταξινόμηση
    bool operator<(const Person& other) const {
        return age < other.age;
    }
};

int main() {
    // Διάνυσμα αντικειμένων
    vector<Person> people = {
        Person("Alice", 25),
        Person("Bob", 30),
        Person("Charlie", 20),
        Person("Diana", 35)
    };
    
    cout << "People in vector:" << endl;
    for (const Person& person : people) {
        person.display();
    }
    
    // Ταξινόμηση κατά ηλικία χρησιμοποιώντας τον υπερφορτωμένο τελεστή<
    sort(people.begin(), people.end());
    cout << "\nAfter sorting by age:" << endl;
    for (const Person& person : people) {
        person.display();
    }
    
    // Χρήση lambda για προσαρμοσμένη ταξινόμηση
    sort(people.begin(), people.end(), [](const Person& a, const Person& b) {
        return a.getName() < b.getName();  // Ταξινόμηση κατά όνομα
    });
    
    cout << "\nAfter sorting by name:" << endl;
    for (const Person& person : people) {
        person.display();
    }
    
    // Εύρεση ατόμου κατά ηλικία
    auto it = find_if(people.begin(), people.end(), [](const Person& p) {
        return p.getAge() == 30;
    });
    
    if (it != people.end()) {
        cout << "\nFound person with age 30: ";
        it->display();
    }
    
    // Προσθήκη νέου ατόμου
    people.emplace_back("Eve", 28);  // Πιο αποδοτικό από το push_back
    cout << "\nAfter adding Eve:" << endl;
    for (const Person& person : people) {
        person.display();
    }
    
    return 0;
}
```

---

## Χάρτες (Συσχετιστικοί Περιέκτες)

### Βασικές Λειτουργίες Χαρτών
```cpp
#include <iostream>
#include <map>
#include <string>
#include <utility>
using namespace std;

int main() {
    // Δημιουργία χαρτών
    map<string, int> ages;
    map<string, int> grades = {{"Alice", 85}, {"Bob", 92}, {"Charlie", 78}};
    
    // Εισαγωγή στοιχείων
    ages["John"] = 25;
    ages["Jane"] = 30;
    ages["Mike"] = 35;
    
    // Εισαγωγή με την μέθοδο insert
    ages.insert(make_pair("Sarah", 28));
    ages.insert({"Tom", 32});
    
    cout << "Ages map:" << endl;
    for (const auto& pair : ages) {
        cout << pair.first << ": " << pair.second << endl;
    }
    
    cout << "\nGrades map:" << endl;
    for (const auto& pair : grades) {
        cout << pair.first << ": " << pair.second << endl;
    }
    
    // Πρόσβαση σε στοιχεία
    cout << "\nAccessing elements:" << endl;
    cout << "John's age: " << ages["John"] << endl;
    cout << "Jane's age (using at): " << ages.at("Jane") << endl;
    
    // Ενημέρωση στοιχείων
    ages["John"] = 26;
    cout << "Updated John's age: " << ages["John"] << endl;
    
    // Έλεγχος ύπαρξης κλειδιού
    string key = "Bob";
    if (grades.find(key) != grades.end()) {
        cout << key << " exists in grades map with value: " << grades[key] << endl;
    } else {
        cout << key << " does not exist in grades map" << endl;
    }
    
    // Ασφαλής πρόσβαση με find
    auto it = ages.find("NonExistent");
    if (it != ages.end()) {
        cout << "Found: " << it->first << " -> " << it->second << endl;
    } else {
        cout << "Key not found in ages map" << endl;
    }
    
    return 0;
}
```

### Μέθοδοι και Επανάληψη Χαρτών
```cpp
#include <iostream>
#include <map>
#include <string>
using namespace std;

int main() {
    map<string, int> scores = {
        {"Math", 95},
        {"English", 87},
        {"Science", 92},
        {"History", 88}
    };
    
    cout << "Original map:" << endl;
    for (const auto& subject : scores) {
        cout << subject.first << ": " << subject.second << endl;
    }
    
    // Μέγεθος και κενότητα
    cout << "\nMap size: " << scores.size() << endl;
    cout << "Is empty: " << (scores.empty() ? "Yes" : "No") << endl;
    
    // Κάτω και άνω όρια
    auto lower = scores.lower_bound("English");
    auto upper = scores.upper_bound("Science");
    
    cout << "\nElements from 'English' inclusive to 'Science' exclusive:" << endl;
    for (auto it = lower; it != upper; ++it) {
        cout << it->first << ": " << it->second << endl;
    }
    
    // Ίσο εύρος (επιστρέφει ζεύγος επαναληπτών)
    auto range = scores.equal_range("History");
    cout << "\nEqual range for 'History':" << endl;
    for (auto it = range.first; it != range.second; ++it) {
        cout << it->first << ": " << it->second << endl;
    }
    
    // Διαγραφή στοιχείων
    scores.erase("History");
    cout << "\nAfter erasing 'History':" << endl;
    for (const auto& subject : scores) {
        cout << subject.first << ": " << subject.second << endl;
    }
    
    // Διαγραφή με επαναλήπτη
    auto eraseIt = scores.find("English");
    if (eraseIt != scores.end()) {
        scores.erase(eraseIt);
        cout << "\nAfter erasing 'English' by iterator:" << endl;
        for (const auto& subject : scores) {
            cout << subject.first << ": " << subject.second << endl;
        }
    }
    
    // Εκκαθάριση χάρτη
    map<string, int> temp = {{"A", 1}, {"B", 2}};
    cout << "\nBefore clear: " << temp.size() << " elements" << endl;
    temp.clear();
    cout << "After clear: " << temp.size() << " elements" << endl;
    
    return 0;
}
```

### Μη Διατεταγμένος Χάρτης έναντι Διατεταγμένου Χάρτη
```cpp
#include <iostream>
#include <map>
#include <unordered_map>
#include <string>
#include <chrono>
using namespace std;

int main() {
    // Διατεταγμένος χάρτης (std::map) - διατηρεί ταξινομημένη σειρά
    map<string, int> orderedMap = {
        {"zebra", 1},
        {"apple", 2},
        {"banana", 3},
        {"cherry", 4},
        {"dog", 5}
    };
    
    cout << "Ordered map (maintains alphabetical order):" << endl;
    for (const auto& pair : orderedMap) {
        cout << pair.first << ": " << pair.second << endl;
    }
    
    // Μη διατεταγμένος χάρτης (std::unordered_map) - ταχύτερη πρόσβαση, χωρίς εγγύηση σειράς
    unordered_map<string, int> unorderedMap = {
        {"zebra", 1},
        {"apple", 2},
        {"banana", 3},
        {"cherry", 4},
        {"dog", 5}
    };
    
    cout << "\nUnordered map (no guaranteed order):" << endl;
    for (const auto& pair : unorderedMap) {
        cout << pair.first << ": " << pair.second << endl;
    }
    
    // Σύγκριση απόδοσης
    cout << "\nPerformance comparison:" << endl;
    
    // Χρονομέτρηση εισαγωγής σε διατεταγμένο χάρτη
    auto start = chrono::high_resolution_clock::now();
    map<int, string> orderedTest;
    for (int i = 0; i < 10000; i++) {
        orderedTest[i] = "value" + to_string(i);
    }
    auto end = chrono::high_resolution_clock::now();
    auto orderedTime = chrono::duration_cast<chrono::microseconds>(end - start);
    
    // Χρονομέτρηση εισαγωγής σε μη διατεταγμένο χάρτη
    start = chrono::high_resolution_clock::now();
    unordered_map<int, string> unorderedTest;
    for (int i = 0; i < 10000; i++) {
        unorderedTest[i] = "value" + to_string(i);
    }
    end = chrono::high_resolution_clock::now();
    auto unorderedTime = chrono::duration_cast<chrono::microseconds>(end - start);
    
    cout << "Ordered map insertion time: " << orderedTime.count() << " microseconds" << endl;
    cout << "Unordered map insertion time: " << unorderedTime.count() << " microseconds" << endl;
    
    // Μέθοδος count
    cout << "\nUsing count method:" << endl;
    cout << "Does 'apple' exist in ordered map? " 
         << (orderedMap.count("apple") ? "Yes" : "No") << endl;
    cout << "Does 'grape' exist in ordered map? " 
         << (orderedMap.count("grape") ? "Yes" : "No") << endl;
    
    // try-emplace (C++17) - εισάγει μόνο αν το κλειδί δεν υπάρχει
    auto [it, inserted] = orderedMap.try_emplace("elderberry", 6);
    cout << "Tried to insert 'elderberry': " << (inserted ? "Success" : "Already existed") << endl;
    
    // emplace (εισάγει πάντα)
    auto [it2, inserted2] = orderedMap.emplace("fig", 7);
    cout << "Emplaced 'fig': " << (inserted2 ? "New element" : "Already existed") << endl;
    
    return 0;
}
```

### Χάρτης με Προσαρμοσμένο Συγκριτή
```cpp
#include <iostream>
#include <map>
#include <string>
#include <functional>
using namespace std;

// Κλάση προσαρμοσμένου συγκριτή
struct CaseInsensitiveCompare {
    bool operator()(const string& a, const string& b) const {
        string lowerA = a;
        string lowerB = b;
        
        // Μετατροπή σε πεζά για σύγκριση
        transform(lowerA.begin(), lowerA.end(), lowerA.begin(), ::tolower);
        transform(lowerB.begin(), lowerB.end(), lowerB.begin(), ::tolower);
        
        return lowerA < lowerB;
    }
};

int main() {
    // Χάρτης με προσαρμοσμένο συγκριτή
    map<string, int, CaseInsensitiveCompare> caseInsensitiveMap;
    
    caseInsensitiveMap["Apple"] = 1;
    caseInsensitiveMap["banana"] = 2;
    caseInsensitiveMap["Cherry"] = 3;
    caseInsensitiveMap["apPLe"] = 4;  // Αυτό θα αντικαταστήσει το πρώτο "Apple"
    
    cout << "Case-insensitive map:" << endl;
    for (const auto& pair : caseInsensitiveMap) {
        cout << pair.first << ": " << pair.second << endl;
    }
    
    // Προσαρμοσμένος συγκριτής βασισμένος σε lambda
    auto lengthComparator = [](const string& a, const string& b) {
        if (a.length() != b.length()) {
            return a.length() < b.length();  // Ταξινόμηση κατά μήκος πρώτα
        }
        return a < b;  // Μετά αλφαβητικά
    };
    
    map<string, int, decltype(lengthComparator)> lengthBasedMap(lengthComparator);
    
    lengthBasedMap["short"] = 1;
    lengthBasedMap["medium"] = 2;
    lengthBasedMap["a"] = 3;
    lengthBasedMap["verylongstring"] = 4;
    lengthBasedMap["hi"] = 5;
    
    cout << "\nLength-based sorted map:" << endl;
    for (const auto& pair : lengthBasedMap) {
        cout << pair.first << " (" << pair.first.length() << " chars): " << pair.second << endl;
    }
    
    // Χάρτης ζευγών
    map<pair<string, int>, double> complexMap;
    complexMap[make_pair("Alice", 25)] = 3.8;
    complexMap[make_pair("Bob", 30)] = 3.9;
    complexMap[make_pair("Alice", 26)] = 3.7;  // Διαφορετική ηλικία, ίδιο όνομα
    
    cout << "\nMap with pair keys:" << endl;
    for (const auto& pair : complexMap) {
        cout << "(" << pair.first.first << ", " << pair.first.second 
             << "): " << pair.second << endl;
    }
    
    return 0;
}
```

---

## Κλάσεις και Αντικείμενα (Τα Βασικά)

### Βασικός Ορισμός Κλάσης
```cpp
#include <iostream>
#include <string>
using namespace std;

class Student {
private:
    string name;
    int age;
    double gpa;

public:
    // Προεπιλεγμένος κατασκευαστής
    Student() {
        name = "Unknown";
        age = 0;
        gpa = 0.0;
        cout << "Default constructor called for " << name << endl;
    }
    
    // Παραμετροποιημένος κατασκευαστής
    Student(string n, int a, double g) : name(n), age(a), gpa(g) {
        cout << "Parameterized constructor called for " << name << endl;
    }
    
    // Κατασκευαστής αντιγραφής
    Student(const Student& other) {
        name = other.name;
        age = other.age;
        gpa = other.gpa;
        cout << "Copy constructor called for " << name << endl;
    }
    
    // Καταστροφέας
    ~Student() {
        cout << "Destructor called for " << name << endl;
    }
    
    // Μέθοδοι λήψης (getters)
    string getName() const { return name; }
    int getAge() const { return age; }
    double getGPA() const { return gpa; }
    
    // Μέθοδοι ρύθμισης (setters)
    void setName(const string& n) { name = n; }
    void setAge(int a) { age = a; }
    void setGPA(double g) { gpa = g; }
    
    // Μέθοδος εμφάνισης
    void display() const {
        cout << "Name: " << name << ", Age: " << age << ", GPA: " << gpa << endl;
    }
};

int main() {
    cout << "Creating student1 with default constructor:" << endl;
    Student student1;
    student1.display();
    
    cout << "\nCreating student2 with parameterized constructor:" << endl;
    Student student2("Alice", 20, 3.8);
    student2.display();
    
    cout << "\nCreating student3 as copy of student2:" << endl;
    Student student3(student2);
    student3.display();
    
    cout << "\nEnd of main function - destructors will be called:" << endl;
    return 0;
}
```

### Λίστες Αρχικοποίησης Κατασκευαστή
```cpp
#include <iostream>
#include <string>
using namespace std;

class Rectangle {
private:
    double length;
    double width;
    string color;
    static int count;  // Στατικό μέλος

public:
    // Κατασκευαστής με λίστα αρχικοποίησης
    Rectangle(double l, double w, string c) : 
        length(l), width(w), color(c) {
        count++;
        cout << "Rectangle created. Total rectangles: " << count << endl;
    }
    
    // Κατασκευαστής με προεπιλεγμένες τιμές
    Rectangle(double l = 1.0, double w = 1.0) : 
        length(l), width(w), color("white") {
        count++;
        cout << "Rectangle created with default color. Total: " << count << endl;
    }
    
    // Κατασκευαστής αντιγραφής
    Rectangle(const Rectangle& other) :
        length(other.length), width(other.width), color(other.color) {
        count++;
        cout << "Rectangle copied. Total: " << count << endl;
    }
    
    ~Rectangle() {
        count--;
        cout << "Rectangle destroyed. Remaining: " << count << endl;
    }
    
    // Μέθοδοι λήψης
    double getLength() const { return length; }
    double getWidth() const { return width; }
    string getColor() const { return color; }
    
    // Υπολογισμός εμβαδού
    double getArea() const {
        return length * width;
    }
    
    // Εμφάνιση πληροφοριών ορθογωνίου
    void display() const {
        cout << "Rectangle: " << length << "x" << width 
             << ", Color: " << color 
             << ", Area: " << getArea() << endl;
    }
    
    // Στατική μέθοδος για λήψη του πλήθους
    static int getCount() { return count; }
};

// Αρχικοποίηση στατικού μέλους
int Rectangle::count = 0;

int main() {
    cout << "Creating rectangles:" << endl;
    
    Rectangle rect1(5.0, 3.0, "red");
    rect1.display();
    
    Rectangle rect2(4.0, 6.0);
    rect2.display();
    
    Rectangle rect3(rect1);  // Κατασκευαστής αντιγραφής
    rect3.display();
    
    cout << "\nTotal rectangles created: " << Rectangle::getCount() << endl;
    
    return 0;
}
```

### Μέθοδοι και Προσδιοριστές Πρόσβασης
```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class BankAccount {
private:
    string accountNumber;
    double balance;
    string owner;
    vector<double> transactionHistory;
    
    // Ιδιωτική βοηθητική μέθοδος
    bool isValidAmount(double amount) const {
        return amount >= 0;
    }
    
public:
    // Κατασκευαστής
    BankAccount(const string& accNum, const string& own, double initialBalance = 0.0)
        : accountNumber(accNum), owner(own), balance(initialBalance) {
        if (initialBalance > 0) {
            transactionHistory.push_back(initialBalance);
        }
    }
    
    // Μέθοδοι δημόσιας διεπαφής
    void deposit(double amount) {
        if (isValidAmount(amount)) {
            balance += amount;
            transactionHistory.push_back(amount);
            cout << "Deposited $" << amount << ". New balance: $" << balance << endl;
        } else {
            cout << "Invalid deposit amount: $" << amount << endl;
        }
    }
    
    bool withdraw(double amount) {
        if (isValidAmount(amount) && amount <= balance) {
            balance -= amount;
            transactionHistory.push_back(-amount);  // Αρνητικό υποδηλώνει ανάληψη
            cout << "Withdrew $" << amount << ". New balance: $" << balance << endl;
            return true;
        } else {
            cout << "Invalid withdrawal amount: $" << amount 
                 << " (Balance: $" << balance << ")" << endl;
            return false;
        }
    }
    
    // Μέθοδοι λήψης (ελεγχόμενη πρόσβαση)
    double getBalance() const {
        return balance;
    }
    
    string getAccountNumber() const {
        return accountNumber;
    }
    
    string getOwner() const {
        return owner;
    }
    
    // Μέθοδος προβολής περιορισμένου ιστορικού συναλλαγών
    void showRecentTransactions(int count = 5) const {
        int start = max(0, (int)transactionHistory.size() - count);
        cout << "Recent " << count << " transactions:" << endl;
        for (int i = start; i < transactionHistory.size(); i++) {
            cout << "  " << (transactionHistory[i] >= 0 ? "Deposit: " : "Withdrawal: ")
                 << "$" << abs(transactionHistory[i]) << endl;
        }
    }
    
    // Εμφάνιση πληροφοριών λογαριασμού
    void displayInfo() const {
        cout << "Account: " << accountNumber << ", Owner: " << owner 
             << ", Balance: $" << balance << endl;
    }
};

int main() {
    BankAccount account("ACC001", "John Doe", 1000.0);
    account.displayInfo();
    
    account.deposit(500.0);
    account.withdraw(200.0);
    account.withdraw(2000.0);  // Μη έγκυρη ανάληψη
    
    account.showRecentTransactions();
    
    cout << "Final balance: $" << account.getBalance() << endl;
    
    return 0;
}
```

---

## Κατασκευαστές και Καταστροφείς

### Βασική Κλάση με Κατασκευαστή και Καταστροφέα
```cpp
#include <iostream>
#include <string>
using namespace std;

class Student {
private:
    string name;
    int age;
    double gpa;

public:
    // Προεπιλεγμένος κατασκευαστής
    Student() {
        name = "Unknown";
        age = 0;
        gpa = 0.0;
        cout << "Default constructor called for " << name << endl;
    }
    
    // Παραμετροποιημένος κατασκευαστής
    Student(string n, int a, double g) : name(n), age(a), gpa(g) {
        cout << "Parameterized constructor called for " << name << endl;
    }
    
    // Κατασκευαστής αντιγραφής
    Student(const Student& other) {
        name = other.name;
        age = other.age;
        gpa = other.gpa;
        cout << "Copy constructor called for " << name << endl;
    }
    
    // Καταστροφέας
    ~Student() {
        cout << "Destructor called for " << name << endl;
    }
    
    // Μέθοδοι λήψης (getters)
    string getName() const { return name; }
    int getAge() const { return age; }
    double getGPA() const { return gpa; }
    
    // Μέθοδοι ρύθμισης (setters)
    void setName(const string& n) { name = n; }
    void setAge(int a) { age = a; }
    void setGPA(double g) { gpa = g; }
    
    // Μέθοδος εμφάνισης
    void display() const {
        cout << "Name: " << name << ", Age: " << age << ", GPA: " << gpa << endl;
    }
};

int main() {
    cout << "Creating student1 with default constructor:" << endl;
    Student student1;
    student1.display();
    
    cout << "\nCreating student2 with parameterized constructor:" << endl;
    Student student2("Alice", 20, 3.8);
    student2.display();
    
    cout << "\nCreating student3 as copy of student2:" << endl;
    Student student3(student2);
    student3.display();
    
    cout << "\nEnd of main function - destructors will be called:" << endl;
    return 0;
}
```

### Καταστροφείς και Διαχείριση Πόρων
```cpp
#include <iostream>
#include <fstream>
#include <memory>
using namespace std;

class FileHandler {
private:
    string filename;
    ofstream file;
    int* dynamicMemory;

public:
    // Ο κατασκευαστής δεσμεύει πόρους
    FileHandler(const string& fname) : filename(fname) {
        cout << "Opening file: " << filename << endl;
        file.open(filename);
        
        // Δέσμευση δυναμικής μνήμης
        dynamicMemory = new int[100];
        cout << "Allocated dynamic memory" << endl;
    }
    
    // Ο καταστροφέας αποδεσμεύει πόρους
    ~FileHandler() {
        if (file.is_open()) {
            file.close();
            cout << "Closed file: " << filename << endl;
        }
        
        if (dynamicMemory != nullptr) {
            delete[] dynamicMemory;
            cout << "Freed dynamic memory" << endl;
        }
    }
    
    // Μέθοδος εγγραφής σε αρχείο
    void writeData(const string& data) {
        if (file.is_open()) {
            file << data << endl;
        }
    }
    
    // Μέθοδος προσομοίωσης διαχείρισης σφαλμάτων
    void processWithError() {
        cout << "Processing with potential error..." << endl;
        throw runtime_error("Simulated error");
    }
};

int main() {
    try {
        cout << "Creating FileHandler object:" << endl;
        FileHandler handler("test.txt");
        handler.writeData("Hello, World!");
        
        // Αποσχολιάστε την επόμενη γραμμή για να δοκιμάσετε τον καταστροφέα με εξαίρεση
        // handler.processWithError();
        
        cout << "Normal exit from try block" << endl;
    } catch (const exception& e) {
        cout << "Exception caught: " << e.what() << endl;
    }
    
    cout << "End of main function" << endl;
    return 0;
}
```

---

## Ο Δείκτης `this`

### Κατανόηση του Δείκτη `this`
```cpp
#include <iostream>
#include <string>
using namespace std;

class BankAccount {
private:
    string accountNumber;
    double balance;
    string owner;

public:
    // Κατασκευαστής
    BankAccount(const string& accNum, double bal, const string& own) 
        : accountNumber(accNum), balance(bal), owner(own) {}
    
    // Χρήση του 'this' για διάκριση μεταξύ μεταβλητών μελών και παραμέτρων
    void setDetails(const string& accountNumber, double balance, const string& owner) {
        this->accountNumber = accountNumber;  // Μέλος έναντι παραμέτρου
        this->balance = balance;              // Μέλος έναντι παραμέτρου
        this->owner = owner;                  // Μέλος έναντι παραμέτρου
        
        cout << "Account details updated using 'this' pointer" << endl;
    }
    
    // Αλυσιδωτή κλήση μεθόδων χρησιμοποιώντας το 'this'
    BankAccount& deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            cout << "Deposited $" << amount << ". New balance: $" << balance << endl;
        }
        return *this;  // Επιστροφή αναφοράς στο τρέχον αντικείμενο
    }
    
    BankAccount& withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            cout << "Withdrew $" << amount << ". New balance: $" << balance << endl;
        }
        return *this;  // Επιστροφή αναφοράς στο τρέχον αντικείμενο
    }
    
    // Μέθοδος σύγκρισης με άλλο αντικείμενο
    bool isEqual(const BankAccount& other) {
        return (this->accountNumber == other.accountNumber &&
                this->balance == other.balance &&
                this->owner == other.owner);
    }
    
    // Προστασία αυτο-ανάθεσης
    BankAccount& operator=(const BankAccount& other) {
        if (this != &other) {  // Έλεγχος για αυτο-ανάθεση
            accountNumber = other.accountNumber;
            balance = other.balance;
            owner = other.owner;
            cout << "Assignment performed" << endl;
        } else {
            cout << "Self-assignment detected and avoided" << endl;
        }
        return *this;
    }
    
    // Εμφάνιση πληροφοριών λογαριασμού
    void display() const {
        cout << "Account: " << accountNumber << ", Owner: " << owner 
             << ", Balance: $" << balance << endl;
    }
    
    // Μέθοδοι πρόσβασης
    const string& getAccountNumber() const { return accountNumber; }
    double getBalance() const { return balance; }
    const string& getOwner() const { return owner; }
};

int main() {
    BankAccount account("ACC001", 1000.0, "John Doe");
    account.display();
    
    // Χρήση του 'this' στην αλυσιδωτή κλήση μεθόδων
    account.deposit(50).withdraw(200).deposit(100);
    
    // Χρήση του 'this' για διάκριση παραμέτρων από μέλη
    account.setDetails("ACC002", 2000.0, "Jane Smith");
    account.display();
    
    // Σύγκριση με άλλο αντικείμενο
    BankAccount account2("ACC002", 2000.0, "Jane Smith");
    cout << "Accounts are equal: " << (account.isEqual(account2) ? "Yes" : "No") << endl;
    
    // Δοκιμή αυτο-ανάθεσης
    account = account;  // Θα πρέπει να ανιχνεύσει την αυτο-ανάθεση
    
    return 0;
}
```

### Το `this` σε Σύνθετα Σενάρια
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class NumberProcessor {
private:
    vector<int> numbers;

public:
    NumberProcessor(const vector<int>& nums) : numbers(nums) {}
    
    // Μέθοδος που επιστρέφει αναφορά στο τρέχον αντικείμενο
    NumberProcessor& addNumber(int num) {
        numbers.push_back(num);
        cout << "Added " << num << endl;
        return *this;
    }
    
    // Μέθοδος που επιστρέφει αναφορά στο τρέχον αντικείμενο
    NumberProcessor& removeNumber(int num) {
        auto it = find(numbers.begin(), numbers.end(), num);
        if (it != numbers.end()) {
            numbers.erase(it);
            cout << "Removed " << num << endl;
        }
        return *this;
    }
    
    // Μέθοδος που χρησιμοποιεί το 'this' για σύγκριση με άλλο αντικείμενο
    bool containsSameNumbers(const NumberProcessor& other) const {
        // Σύγκριση μεγεθών πρώτα
        if (this->numbers.size() != other.numbers.size()) {
            return false;
        }
        
        // Ταξινόμηση και των δύο διανυσμάτων προσωρινά για σύγκριση
        vector<int> thisSorted = this->numbers;
        vector<int> otherSorted = other.numbers;
        
        sort(thisSorted.begin(), thisSorted.end());
        sort(otherSorted.begin(), otherSorted.end());
        
        return thisSorted == otherSorted;
    }
    
    // Μέθοδος που επιστρέφει το ίδιο το αντικείμενο
    NumberProcessor& sortNumbers() {
        sort(numbers.begin(), numbers.end());
        cout << "Numbers sorted" << endl;
        return *this;
    }
    
    // Μέθοδος που επεξεργάζεται και επιστρέφει νέο αντικείμενο
    NumberProcessor getProcessedVersion() const {
        NumberProcessor processed = *this;  // Αντίγραφο του τρέχοντος αντικειμένου
        processed.sortNumbers();  // Επεξεργασία του αντιγράφου
        return processed;
    }
    
    // Μέθοδος εμφάνισης
    void display() const {
        cout << "Numbers: ";
        for (int num : numbers) {
            cout << num << " ";
        }
        cout << endl;
    }
    
    // Λήψη μεγέθους
    size_t getSize() const {
        return numbers.size();
    }
    
    // Υπερφόρτωση τελεστή που χρησιμοποιεί το 'this'
    bool operator<(const NumberProcessor& other) const {
        return this->getSize() < other.getSize();
    }
};

int main() {
    NumberProcessor processor({5, 2, 8, 1});
    processor.display();
    
    // Αλυσιδωτή κλήση μεθόδων χρησιμοποιώντας το 'this'
    processor.addNumber(10).removeNumber(2).sortNumbers();
    processor.display();
    
    // Δημιουργία άλλου επεξεργαστή για σύγκριση
    NumberProcessor processor2({8, 5, 1, 10});
    cout << "Both processors have same numbers: " 
         << (processor.containsSameNumbers(processor2) ? "Yes" : "No") << endl;
    
    // Λήψη επεξεργασμένης έκδοσης
    NumberProcessor sortedVersion = processor.getProcessedVersion();
    cout << "Original: ";
    processor.display();
    cout << "Sorted version: ";
    sortedVersion.display();
    
    return 0;
}
```

---

## Αρχές Αντικειμενοστραφούς Προγραμματισμού (Ενθυλάκωση, Αφαίρεση)

### Ενθυλάκωση
```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class BankAccount {
private:
    string accountNumber;
    double balance;
    string owner;
    vector<double> transactionHistory;
    
    // Ιδιωτική βοηθητική μέθοδος
    bool isValidAmount(double amount) const {
        return amount >= 0;
    }
    
public:
    // Κατασκευαστής
    BankAccount(const string& accNum, const string& own, double initialBalance = 0.0)
        : accountNumber(accNum), owner(own), balance(initialBalance) {
        if (initialBalance > 0) {
            transactionHistory.push_back(initialBalance);
        }
    }
    
    // Μέθοδοι δημόσιας διεπαφής
    void deposit(double amount) {
        if (isValidAmount(amount)) {
            balance += amount;
            transactionHistory.push_back(amount);
            cout << "Deposited $" << amount << ". New balance: $" << balance << endl;
        } else {
            cout << "Invalid deposit amount: $" << amount << endl;
        }
    }
    
    bool withdraw(double amount) {
        if (isValidAmount(amount) && amount <= balance) {
            balance -= amount;
            transactionHistory.push_back(-amount);  // Αρνητικό υποδηλώνει ανάληψη
            cout << "Withdrew $" << amount << ". New balance: $" << balance << endl;
            return true;
        } else {
            cout << "Invalid withdrawal amount: $" << amount 
                 << " (Balance: $" << balance << ")" << endl;
            return false;
        }
    }
    
    // Μέθοδοι λήψης (ελεγχόμενη πρόσβαση)
    double getBalance() const {
        return balance;
    }
    
    string getAccountNumber() const {
        return accountNumber;
    }
    
    string getOwner() const {
        return owner;
    }
    
    // Μέθοδος προβολής περιορισμένου ιστορικού συναλλαγών
    void showRecentTransactions(int count = 5) const {
        int start = max(0, (int)transactionHistory.size() - count);
        cout << "Recent " << count << " transactions:" << endl;
        for (int i = start; i < transactionHistory.size(); i++) {
            cout << "  " << (transactionHistory[i] >= 0 ? "Deposit: " : "Withdrawal: ")
                 << "$" << abs(transactionHistory[i]) << endl;
        }
    }
    
    // Εμφάνιση πληροφοριών λογαριασμού
    void displayInfo() const {
        cout << "Account: " << accountNumber << ", Owner: " << owner 
             << ", Balance: $" << balance << endl;
    }
};

int main() {
    BankAccount account("ACC001", "John Doe", 1000.0);
    account.displayInfo();
    
    account.deposit(500.0);
    account.withdraw(200.0);
    account.withdraw(2000.0);  // Μη έγκυρη ανάληψη
    
    account.showRecentTransactions();
    
    cout << "Final balance: $" << account.getBalance() << endl;
    
    return 0;
}
```

### Αφαίρεση
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
using namespace std;

// Αφηρημένη βασική κλάση
class Shape {
protected:
    string color;
    
public:
    Shape(const string& c) : color(c) {}
    
    // Η καθαρά εικονική συνάρτηση καθιστά αυτή την κλάση αφηρημένη
    virtual double calculateArea() const = 0;
    virtual double calculatePerimeter() const = 0;
    
    // Εικονική συνάρτηση που μπορεί να παρακαμφθεί
    virtual void display() const {
        cout << "Shape color: " << color << endl;
    }
    
    // Εικονικός καταστροφέας για σωστό καθαρισμό
    virtual ~Shape() = default;
};

// Συγκεκριμένες παράγωγες κλάσεις
class Circle : public Shape {
private:
    double radius;
    
public:
    Circle(const string& c, double r) : Shape(c), radius(r) {}
    
    double calculateArea() const override {
        const double PI = 3.14159265359;
        return PI * radius * radius;
    }
    
    double calculatePerimeter() const override {
        const double PI = 3.14159265359;
        return 2 * PI * radius;
    }
    
    void display() const override {
        cout << "Circle - Radius: " << radius << ", Color: " << color 
             << ", Area: " << calculateArea() 
             << ", Perimeter: " << calculatePerimeter() << endl;
    }
};

class Rectangle : public Shape {
private:
    double width, height;
    
public:
    Rectangle(const string& c, double w, double h) : Shape(c), width(w), height(h) {}
    
    double calculateArea() const override {
        return width * height;
    }
    
    double calculatePerimeter() const override {
        return 2 * (width + height);
    }
    
    void display() const override {
        cout << "Rectangle - Width: " << width << ", Height: " << height 
             << ", Color: " << color 
             << ", Area: " << calculateArea() 
             << ", Perimeter: " << calculatePerimeter() << endl;
    }
};

class Triangle : public Shape {
private:
    double side1, side2, side3;
    
public:
    Triangle(const string& c, double s1, double s2, double s3) 
        : Shape(c), side1(s1), side2(s2), side3(s3) {}
    
    double calculateArea() const override {
        // Χρήση του τύπου του Ήρωνα (Heron)
        double s = (side1 + side2 + side3) / 2;
        return sqrt(s * (s - side1) * (s - side2) * (s - side3));
    }
    
    double calculatePerimeter() const override {
        return side1 + side2 + side3;
    }
    
    void display() const override {
        cout << "Triangle - Sides: " << side1 << ", " << side2 << ", " << side3 
             << ", Color: " << color 
             << ", Area: " << calculateArea() 
             << ", Perimeter: " << calculatePerimeter() << endl;
    }
};

int main() {
    // Χρήση πολυμορφισμού με έξυπνους δείκτες
    vector<unique_ptr<Shape>> shapes;
    
    shapes.push_back(make_unique<Circle>("Red", 5.0));
    shapes.push_back(make_unique<Rectangle>("Blue", 4.0, 6.0));
    shapes.push_back(make_unique<Triangle>("Green", 3.0, 4.0, 5.0));
    
    cout << "Shape Information:" << endl;
    for (const auto& shape : shapes) {
        shape->display();
        cout << "Area: " << shape->calculateArea() << endl;
        cout << "Perimeter: " << shape->calculatePerimeter() << endl;
        cout << "---" << endl;
    }
    
    // Υπολογισμός συνολικού εμβαδού
    double totalArea = 0;
    for (const auto& shape : shapes) {
        totalArea += shape->calculateArea();
    }
    cout << "Total area of all shapes: " << totalArea << endl;
    
    return 0;
}
```

---

## Κληρονομικότητα και Πολυμορφισμός

### Απλή Κληρονομικότητα
```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

// Βασική κλάση
class Vehicle {
protected:
    string brand;
    string model;
    int year;
    double price;
    
public:
    Vehicle(const string& b, const string& m, int y, double p)
        : brand(b), model(m), year(y), price(p) {}
    
    virtual void displayInfo() const {
        cout << "Vehicle: " << brand << " " << model 
             << " (" << year << "), Price: $" << price << endl;
    }
    
    virtual void startEngine() const {
        cout << "Starting " << brand << " " << model << " engine..." << endl;
    }
    
    virtual void stopEngine() const {
        cout << "Stopping " << brand << " " << model << " engine..." << endl;
    }
    
    virtual ~Vehicle() = default;
    
    // Μέθοδοι λήψης
    string getBrand() const { return brand; }
    string getModel() const { return model; }
    int getYear() const { return year; }
    double getPrice() const { return price; }
};

// Παράγωγη κλάση
class Car : public Vehicle {
private:
    int doors;
    string fuelType;
    bool isElectric;
    
public:
    Car(const string& b, const string& m, int y, double p, int d, const string& fuel, bool electric = false)
        : Vehicle(b, m, y, p), doors(d), fuelType(fuel), isElectric(electric) {}
    
    void displayInfo() const override {
        cout << "Car: " << brand << " " << model << " (" << year << ")" << endl;
        cout << "  Doors: " << doors << ", Fuel: " << fuelType 
             << ", Electric: " << (isElectric ? "Yes" : "No") << endl;
        cout << "  Price: $" << price << endl;
    }
    
    void startEngine() const override {
        if (isElectric) {
            cout << "Starting electric motor for " << brand << " " << model << "..." << endl;
        } else {
            cout << "Starting internal combustion engine for " << brand << " " << model << "..." << endl;
        }
    }
    
    void openTrunk() const {
        cout << "Opening trunk of " << brand << " " << model << endl;
    }
    
    // Επιπλέον μέθοδος ειδική για αυτοκίνητο
    void honk() const {
        cout << brand << " " << model << " goes beep beep!" << endl;
    }
};

// Άλλη παράγωγη κλάση
class Motorcycle : public Vehicle {
private:
    int engineCC;
    bool hasSidecar;
    
public:
    Motorcycle(const string& b, const string& m, int y, double p, int cc, bool sidecar = false)
        : Vehicle(b, m, y, p), engineCC(cc), hasSidecar(sidecar) {}
    
    void displayInfo() const override {
        cout << "Motorcycle: " << brand << " " << model << " (" << year << ")" << endl;
        cout << "  Engine: " << engineCC << "cc, Sidecar: " << (hasSidecar ? "Yes" : "No") << endl;
        cout << "  Price: $" << price << endl;
    }
    
    void wheelie() const {
        cout << brand << " " << model << " performs a wheelie!" << endl;
    }
    
    void startEngine() const override {
        cout << "Revving up the " << engineCC << "cc engine of " << brand << " " << model << "..." << endl;
    }
};

int main() {
    cout << "Single Inheritance Example:" << endl;
    
    Car car("Toyota", "Camry", 2023, 25000, 4, "Gasoline");
    Motorcycle motorcycle("Harley-Davidson", "Street 750", 2022, 8000, 750);
    
    // Κλήσεις μεθόδων βασικής κλάσης
    car.displayInfo();
    car.startEngine();
    cout << endl;
    
    motorcycle.displayInfo();
    motorcycle.startEngine();
    cout << endl;
    
    // Μέθοδοι ειδικές για παράγωγες κλάσεις
    car.openTrunk();
    car.honk();
    cout << endl;
    
    motorcycle.wheelie();
    cout << endl;
    
    // Πολυμορφισμός με δείκτες βασικής κλάσης
    Vehicle* vehicles[] = {&car, &motorcycle};
    
    cout << "Using polymorphism:" << endl;
    for (int i = 0; i < 2; i++) {
        vehicles[i]->displayInfo();
        vehicles[i]->startEngine();
        cout << endl;
    }
    
    return 0;
}
```

### Πολυμορφισμός
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
#include <algorithm>
using namespace std;

// Βασική κλάση που επιδεικνύει πολυμορφισμό
class Animal {
protected:
    string name;
    int age;
    
public:
    Animal(const string& n, int a) : name(n), age(a) {}
    
    // Εικονικές συναρτήσεις για πολυμορφισμό εκτέλεσης
    virtual void makeSound() const {
        cout << name << " makes a sound." << endl;
    }
    
    virtual void move() const {
        cout << name << " moves." << endl;
    }
    
    virtual void eat() const {
        cout << name << " eats." << endl;
    }
    
    virtual void displayInfo() const {
        cout << "Animal: " << name << ", Age: " << age << endl;
    }
    
    virtual ~Animal() = default;
};

// Παράγωγες κλάσεις
class Dog : public Animal {
private:
    string breed;
    
public:
    Dog(const string& n, int a, const string& b) : Animal(n, a), breed(b) {}
    
    void makeSound() const override {
        cout << name << " the dog barks: Woof! Woof!" << endl;
    }
    
    void move() const override {
        cout << name << " the dog runs on four legs." << endl;
    }
    
    void eat() const override {
        cout << name << " the dog eats dog food." << endl;
    }
    
    void fetch() const {
        cout << name << " fetches the ball!" << endl;
    }
    
    void displayInfo() const override {
        cout << "Dog: " << name << ", Age: " << age << ", Breed: " << breed << endl;
    }
};

class Cat : public Animal {
private:
    bool isIndoor;
    
public:
    Cat(const string& n, int a, bool indoor) : Animal(n, a), isIndoor(indoor) {}
    
    void makeSound() const override {
        cout << name << " the cat meows: Meow!" << endl;
    }
    
    void move() const override {
        cout << name << " the cat prowls silently." << endl;
    }
    
    void eat() const override {
        cout << name << " the cat eats cat food." << endl;
    }
    
    void climb() const {
        cout << name << " climbs the tree!" << endl;
    }
    
    void displayInfo() const override {
        cout << "Cat: " << name << ", Age: " << age 
             << ", Indoor: " << (isIndoor ? "Yes" : "No") << endl;
    }
};

class Bird : public Animal {
private:
    string species;
    bool canFly;
    
public:
    Bird(const string& n, int a, const string& s, bool fly) 
        : Animal(n, a), species(s), canFly(fly) {}
    
    void makeSound() const override {
        cout << name << " the bird chirps: Chirp! Chirp!" << endl;
    }
    
    void move() const override {
        if (canFly) {
            cout << name << " the bird flies through the air." << endl;
        } else {
            cout << name << " the bird walks." << endl;
        }
    }
    
    void eat() const override {
        cout << name << " the bird eats seeds." << endl;
    }
    
    void fly() const {
        if (canFly) {
            cout << name << " soars in the sky!" << endl;
        } else {
            cout << name << " cannot fly." << endl;
        }
    }
    
    void displayInfo() const override {
        cout << "Bird: " << name << ", Age: " << age 
             << ", Species: " << species 
             << ", Can Fly: " << (canFly ? "Yes" : "No") << endl;
    }
};

// Συνάρτηση που επιδεικνύει πολυμορφισμό
void animalActivity(const Animal& animal) {
    animal.displayInfo();
    animal.makeSound();
    animal.move();
    animal.eat();
    cout << "---" << endl;
}

int main() {
    // Δημιουργία ζώων με έξυπνους δείκτες
    vector<unique_ptr<Animal>> animals;
    
    animals.push_back(make_unique<Dog>("Buddy", 3, "Golden Retriever"));
    animals.push_back(make_unique<Cat>("Whiskers", 2, true));
    animals.push_back(make_unique<Bird>("Tweety", 1, "Canary", true));
    animals.push_back(make_unique<Dog>("Rex", 5, "German Shepherd"));
    animals.push_back(make_unique<Cat>("Fluffy", 4, false));
    
    cout << "All animals performing activities:" << endl;
    for (const auto& animal : animals) {
        animalActivity(*animal);
    }
    
    // Επίδειξη συγκεκριμένων συμπεριφορών
    cout << "Specific behaviors:" << endl;
    for (const auto& animal : animals) {
        // Downcasting για πρόσβαση σε συγκεκριμένες μεθόδους (με ελέγχους ασφαλείας)
        if (Dog* dog = dynamic_cast<Dog*>(animal.get())) {
            dog->fetch();
        } else if (Cat* cat = dynamic_cast<Cat*>(animal.get())) {
            cat->climb();
        } else if (Bird* bird = dynamic_cast<Bird*>(animal.get())) {
            bird->fly();
        }
    }
    
    return 0;
}
```

### Πολλαπλή Κληρονομικότητα
```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

// Πρώτη βασική κλάση
class Flyable {
protected:
    double maxAltitude;
    double maxSpeed;
    
public:
    Flyable(double altitude, double speed) : maxAltitude(altitude), maxSpeed(speed) {}
    
    virtual void takeOff() const {
        cout << "Taking off..." << endl;
    }
    
    virtual void land() const {
        cout << "Landing..." << endl;
    }
    
    virtual void fly() const {
        cout << "Flying at up to " << maxSpeed << " mph and " << maxAltitude << " feet" << endl;
    }
    
    virtual ~Flyable() = default;
};

// Δεύτερη βασική κλάση
class Swimmable {
protected:
    double maxDepth;
    double swimSpeed;
    
public:
    Swimmable(double depth, double speed) : maxDepth(depth), swimSpeed(speed) {}
    
    virtual void dive() const {
        cout << "Diving underwater..." << endl;
    }
    
    virtual void surface() const {
        cout << "Surfacing..." << endl;
    }
    
    virtual void swim() const {
        cout << "Swimming at " << swimSpeed << " mph up to " << maxDepth << " feet deep" << endl;
    }
    
    virtual ~Swimmable() = default;
};

// Τρίτη βασική κλάση
class LandVehicle {
protected:
    double groundSpeed;
    int wheels;
    
public:
    LandVehicle(double speed, int w) : groundSpeed(speed), wheels(w) {}
    
    virtual void drive() const {
        cout << "Driving on " << wheels << " wheels at " << groundSpeed << " mph" << endl;
    }
    
    virtual void brake() const {
        cout << "Applying brakes..." << endl;
    }
    
    virtual ~LandVehicle() = default;
};

// Παράγωγη κλάση με πολλαπλή κληρονομικότητα
class AmphibiousVehicle : public Flyable, public Swimmable, public LandVehicle {
private:
    string name;
    
public:
    AmphibiousVehicle(const string& n, double alt, double fSpeed, 
                     double depth, double sSpeed, double gSpeed, int w)
        : Flyable(alt, fSpeed), Swimmable(depth, sSpeed), 
          LandVehicle(gSpeed, w), name(n) {}
    
    // Παράκαμψη μεθόδων για συμπεριφορά ειδική για αμφίβια οχήματα
    void takeOff() const override {
        cout << name << " taking off from water surface..." << endl;
    }
    
    void land() const override {
        cout << name << " landing on water surface..." << endl;
    }
    
    void fly() const override {
        cout << name << " flying: ";
        Flyable::fly();
    }
    
    void dive() const override {
        cout << name << " diving underwater..." << endl;
    }
    
    void surface() const override {
        cout << name << " surfacing from underwater..." << endl;
    }
    
    void swim() const override {
        cout << name << " swimming: ";
        Swimmable::swim();
    }
    
    void drive() const override {
        cout << name << " driving: ";
        LandVehicle::drive();
    }
    
    // Νέα μέθοδος που συνδυάζει όλες τις δυνατότητες
    void performAmphibiousSequence() const {
        cout << "\n--- " << name << " Amphibious Sequence ---" << endl;
        
        // Οδήγηση στη στεριά
        drive();
        
        // Μετάβαση στο νερό
        brake();
        cout << name << " entering water..." << endl;
        
        // Κολύμπι
        swim();
        
        // Κατάδυση
        dive();
        cout << name << " exploring underwater..." << endl;
        surface();
        
        // Απογείωση
        takeOff();
        fly();
        
        // Προσγείωση
        land();
        cout << name << " returning to shore." << endl;
        cout << "--- End of sequence ---\n" << endl;
    }
    
    void displayCapabilities() const {
        cout << name << " Capabilities:" << endl;
        cout << "  Flight: Up to " << maxAltitude << " ft at " << maxSpeed << " mph" << endl;
        cout << "  Swimming: Up to " << maxDepth << " ft at " << swimSpeed << " mph" << endl;
        cout << "  Driving: " << groundSpeed << " mph on " << wheels << " wheels" << endl;
    }
};

int main() {
    cout << "Multiple Inheritance Example:" << endl;
    
    AmphibiousVehicle duckBoat("Duck Boat", 1000, 120, 30, 5, 30, 6);
    
    duckBoat.displayCapabilities();
    cout << endl;
    
    // Πρόσβαση σε μεθόδους από όλες τις κληρονομημένες κλάσεις
    duckBoat.drive();
    duckBoat.swim();
    duckBoat.fly();
    cout << endl;
    
    // Εκτέλεση της πλήρους ακολουθίας
    duckBoat.performAmphibiousSequence();
    
    // Επίδειξη πρόσβασης σε συγκεκριμένες μεθόδους βασικής κλάσης
    cout << "Accessing specific base class methods:" << endl;
    duckBoat.Flyable::takeOff();
    duckBoat.Swimmable::dive();
    duckBoat.LandVehicle::brake();
    
    return 0;
}
```

---

## Προχωρημένη Διαχείριση Μνήμης (Σωρός έναντι Στοίβας, Έξυπνοι Δείκτες)

### Έξυπνοι Δείκτες
```cpp
#include <iostream>
#include <memory>
#include <vector>
#include <string>
using namespace std;

class Resource {
private:
    string name;
    int* data;
    size_t size;
    
public:
    // Κατασκευαστής
    Resource(const string& n, size_t s) : name(n), size(s) {
        data = new int[size];
        for (size_t i = 0; i < size; i++) {
            data[i] = i + 1;
        }
        cout << "Resource '" << name << "' allocated with " << size << " integers" << endl;
    }
    
    // Καταστροφέας
    ~Resource() {
        delete[] data;
        cout << "Resource '" << name << "' deallocated" << endl;
    }
    
    // Κατασκευαστής αντιγραφής
    Resource(const Resource& other) : name(other.name + "_copy"), size(other.size) {
        data = new int[size];
        for (size_t i = 0; i < size; i++) {
            data[i] = other.data[i];
        }
        cout << "Resource '" << name << "' copied from '" << other.name << "'" << endl;
    }
    
    // Τελεστής ανάθεσης
    Resource& operator=(const Resource& other) {
        if (this != &other) {
            delete[] data;  // Καθαρισμός υπάρχοντος πόρου
            
            name = other.name + "_assigned";
            size = other.size;
            data = new int[size];
            for (size_t i = 0; i < size; i++) {
                data[i] = other.data[i];
            }
            
            cout << "Resource '" << name << "' assigned from '" << other.name << "'" << endl;
        }
        return *this;
    }
    
    // Κατασκευαστής μετακίνησης
    Resource(Resource&& other) noexcept : name(move(other.name)), size(other.size), data(other.data) {
        other.data = nullptr;
        other.size = 0;
        cout << "Resource moved to '" << name << "'" << endl;
    }
    
    // Τελεστής ανάθεσης μετακίνησης
    Resource& operator=(Resource&& other) noexcept {
        if (this != &other) {
            delete[] data;  // Καθαρισμός υπάρχοντος πόρου
            
            name = move(other.name);
            size = other.size;
            data = other.data;
            
            other.data = nullptr;
            other.size = 0;
            
            cout << "Resource moved to '" << name << "'" << endl;
        }
        return *this;
    }
    
    void display() const {
        cout << "Resource '" << name << "': ";
        for (size_t i = 0; i < min(size, (size_t)5); i++) {  // Εμφάνιση πρώτων 5 στοιχείων
            cout << data[i] << " ";
        }
        if (size > 5) cout << "...";
        cout << endl;
    }
    
    string getName() const { return name; }
};

void demonstrateUniquePtr() {
    cout << "\n=== Unique Pointer Demo ===" << endl;
    
    // Δημιουργία unique_ptr
    unique_ptr<Resource> ptr1 = make_unique<Resource>("Resource1", 10);
    ptr1->display();
    
    // Μεταφορά ιδιοκτησίας με move
    unique_ptr<Resource> ptr2 = move(ptr1);
    // Το ptr1 είναι τώρα null
    cout << "ptr1 is " << (ptr1 ? "valid" : "null") << endl;
    cout << "ptr2 is " << (ptr2 ? "valid" : "null") << endl;
    
    ptr2->display();
    
    // Πίνακας με unique_ptr
    unique_ptr<int[]> arrayPtr = make_unique<int[]>(5);
    for (int i = 0; i < 5; i++) {
        arrayPtr[i] = (i + 1) * 10;
    }
    
    cout << "Array: ";
    for (int i = 0; i < 5; i++) {
        cout << arrayPtr[i] << " ";
    }
    cout << endl;
    
    // Το unique_ptr καθαρίζει αυτόματα όταν βγαίνει εκτός πεδίου εφαρμογής
}

void demonstrateSharedPtr() {
    cout << "\n=== Shared Pointer Demo ===" << endl;
    
    // Δημιουργία shared_ptr
    shared_ptr<Resource> ptr1 = make_shared<Resource>("SharedResource", 5);
    cout << "Reference count: " << ptr1.use_count() << endl;
    
    {
        // Δημιουργία άλλου shared_ptr που δείχνει στο ίδιο αντικείμενο
        shared_ptr<Resource> ptr2 = ptr1;
        cout << "Reference count: " << ptr1.use_count() << endl;
        cout << "Reference count (ptr2): " << ptr2.use_count() << endl;
        
        ptr2->display();
        
        // Δημιουργία τρίτου shared_ptr
        shared_ptr<Resource> ptr3 = ptr1;
        cout << "Reference count: " << ptr1.use_count() << endl;
    }
    
    // Τα ptr2 και ptr3 βγήκαν εκτός πεδίου, ο μετρητής αναφορών μειώθηκε
    cout << "Reference count after scope: " << ptr1.use_count() << endl;
    ptr1->display();
    
    // Ασθενής δείκτης για διάσπαση κυκλικών αναφορών
    weak_ptr<Resource> weakPtr = ptr1;
    cout << "Weak pointer created, shared count: " << weakPtr.use_count() << endl;
    
    if (auto lockedPtr = weakPtr.lock()) {  // Ασφαλής πρόσβαση στον πόρο
        cout << "Successfully locked weak pointer" << endl;
        lockedPtr->display();
    }
    
    // Επαναφορά του shared pointer
    ptr1.reset();
    cout << "ptr1 reset, expired: " << weakPtr.expired() << endl;
}

void demonstrateCustomDeleter() {
    cout << "\n=== Custom Deleter Demo ===" << endl;
    
    // Προσαρμοσμένη συνάρτηση διαγραφής
    auto customDeleter = [](Resource* res) {
        cout << "Custom deleter called for: " << res->getName() << endl;
        delete res;
    };
    
    unique_ptr<Resource, decltype(customDeleter)> ptr(
        new Resource("CustomDeleted", 3), 
        customDeleter
    );
    
    ptr->display();
    // Ο προσαρμοσμένος διαγράφων θα κληθεί αυτόματα
}

int main() {
    cout << "Advanced Memory Management with Smart Pointers" << endl;
    
    demonstrateUniquePtr();
    demonstrateSharedPtr();
    demonstrateCustomDeleter();
    
    cout << "\nAll smart pointers cleaned up automatically!" << endl;
    
    return 0;
}
```

### RAII (Απόκτηση Πόρων Είναι Αρχικοποίηση)
```cpp
#include <iostream>
#include <fstream>
#include <mutex>
#include <thread>
#include <chrono>
using namespace std;

// Κλάση RAII για διαχείριση αρχείων
class FileManager {
private:
    string filename;
    ofstream file;
    bool isOpen;
    
public:
    FileManager(const string& fname) : filename(fname), isOpen(false) {
        file.open(filename);
        if (file.is_open()) {
            isOpen = true;
            cout << "File '" << filename << "' opened successfully" << endl;
        } else {
            cout << "Failed to open file '" << filename << "'" << endl;
        }
    }
    
    // Ο καταστροφέας κλείνει αυτόματα το αρχείο
    ~FileManager() {
        if (isOpen) {
            file.close();
            cout << "File '" << filename << "' closed automatically" << endl;
        }
    }
    
    // Μη αντιγράψιμη για αποτροπή διπλασιασμού πόρων
    FileManager(const FileManager&) = delete;
    FileManager& operator=(const FileManager&) = delete;
    
    // Κατασκευαστής μετακίνησης
    FileManager(FileManager&& other) noexcept 
        : filename(move(other.filename)), file(move(other.file)), isOpen(other.isOpen) {
        other.isOpen = false;
        cout << "File manager moved" << endl;
    }
    
    // Εγγραφή σε αρχείο
    bool write(const string& data) {
        if (isOpen) {
            file << data << endl;
            return true;
        }
        return false;
    }
    
    bool isFileOpen() const { return isOpen; }
};

// Κλάση RAII για συγχρονισμό νημάτων
class ThreadLock {
private:
    mutex& mtx;
    bool locked;
    
public:
    ThreadLock(mutex& m) : mtx(m), locked(true) {
        mtx.lock();
        cout << "Mutex locked" << endl;
    }
    
    ~ThreadLock() {
        if (locked) {
            mtx.unlock();
            cout << "Mutex unlocked" << endl;
        }
    }
    
    // Αποτροπή αντιγραφής
    ThreadLock(const ThreadLock&) = delete;
    ThreadLock& operator=(const ThreadLock&) = delete;
    
    // Κατασκευαστής μετακίνησης
    ThreadLock(ThreadLock&& other) noexcept : mtx(other.mtx), locked(other.locked) {
        other.locked = false;
    }
    
    void unlock() {
        if (locked) {
            mtx.unlock();
            locked = false;
            cout << "Mutex unlocked early" << endl;
        }
    }
    
    void lockAgain() {
        if (!locked) {
            mtx.lock();
            locked = true;
            cout << "Mutex locked again" << endl;
        }
    }
};

// Κλάση RAII για προσομοίωση σύνδεσης βάσης δεδομένων
class DatabaseConnection {
private:
    string connectionString;
    bool isConnected;
    
public:
    DatabaseConnection(const string& connStr) : connectionString(connStr), isConnected(false) {
        // Προσομοίωση προσπάθειας σύνδεσης
        cout << "Attempting to connect to: " << connectionString << endl;
        isConnected = true;  // Προσομοίωση επιτυχούς σύνδεσης
        cout << "Database connected successfully" << endl;
    }
    
    ~DatabaseConnection() {
        if (isConnected) {
            cout << "Database connection closed" << endl;
        }
    }
    
    // Αποτροπή αντιγραφής
    DatabaseConnection(const DatabaseConnection&) = delete;
    DatabaseConnection& operator=(const DatabaseConnection&) = delete;
    
    // Κατασκευαστής μετακίνησης
    DatabaseConnection(DatabaseConnection&& other) noexcept 
        : connectionString(move(other.connectionString)), isConnected(other.isConnected) {
        other.isConnected = false;
    }
    
    void executeQuery(const string& query) {
        if (isConnected) {
            cout << "Executing query: " << query << endl;
        } else {
            cout << "Cannot execute query - not connected" << endl;
        }
    }
    
    bool connected() const { return isConnected; }
};

void demonstrateRAII() {
    cout << "=== RAII Demonstration ===" << endl;
    
    // RAII αρχείου
    {
        FileManager fm("example.txt");
        if (fm.isFileOpen()) {
            fm.write("Hello from RAII!");
            fm.write("Resource automatically managed");
        }
    }  // Το αρχείο κλείνεται αυτόματα εδώ
    
    // RAII mutex
    mutex mtx;
    {
        ThreadLock lock(mtx);
        cout << "Critical section accessed safely" << endl;
        // Το mutex ξεκλειδώνεται αυτόματα όταν το lock βγαίνει εκτός πεδίου
    }
    
    // RAII βάσης δεδομένων
    {
        DatabaseConnection db("localhost:5432/mydb");
        db.executeQuery("SELECT * FROM users;");
        // Η σύνδεση κλείνεται αυτόματα
    }
    
    cout << "All resources properly managed with RAII!" << endl;
}

void demonstrateExceptionSafety() {
    cout << "\n=== Exception Safety with RAII ===" << endl;
    
    try {
        FileManager fm("exception_test.txt");
        fm.write("Before exception");
        
        // Προσομοίωση εξαίρεσης
        throw runtime_error("Simulated exception occurred");
        
        // Αυτή η γραμμή δεν θα εκτελεστεί, αλλά το FileManager θα καθαριστεί
        fm.write("After exception - this won't execute");
    } catch (const exception& e) {
        cout << "Caught exception: " << e.what() << endl;
        cout << "Notice that file was still properly closed due to RAII!" << endl;
    }
    
    // Επίδειξη διαχείρισης πόρων σε πεδία εφαρμογής
    cout << "\nManual resource management vs RAII:" << endl;
    
    // Χωρίς RAII (κακή πρακτική):
    cout << "Without RAII - potential resource leak:" << endl;
    ofstream* badFile = new ofstream("bad_example.txt");
    *badFile << "This might not get cleaned up properly";
    // Ξεχάστηκε το κλείσιμο/διαγραφή - διαρροή πόρων!
    
    // Με RAII (καλή πρακτική):
    cout << "With RAII - guaranteed cleanup:" << endl;
    {
        FileManager goodFile("good_example.txt");
        goodFile.write("This will definitely get cleaned up");
    }  // Ο αυτόματος καθαρισμός γίνεται εδώ
}

int main() {
    demonstrateRAII();
    demonstrateExceptionSafety();
    
    return 0;
}
```

### Ομάδες Μνήμης και Προσαρμοσμένοι Κατανεμητές
```cpp
#include <iostream>
#include <vector>
#include <memory>
#include <list>
#include <chrono>
using namespace std;

// Απλή υλοποίηση ομάδας μνήμης
template<typename T, size_t PoolSize = 100>
class MemoryPool {
private:
    union Block {
        T object;
        Block* next;
        
        Block() : next(nullptr) {}
        ~Block() {}  // Πρέπει να είναι τετριμμένος για placement new
    };
    
    Block* freeList;
    vector<Block> pool;
    size_t allocatedCount;
    
public:
    MemoryPool() : freeList(nullptr), pool(PoolSize), allocatedCount(0) {
        // Αρχικοποίηση λίστας ελεύθερων
        for (size_t i = 0; i < PoolSize - 1; ++i) {
            pool[i].next = &pool[i + 1];
        }
        pool[PoolSize - 1].next = nullptr;
        freeList = &pool[0];
    }
    
    ~MemoryPool() {
        // Καταστροφή όλων των δεσμευμένων αντικειμένων
        reset();
    }
    
    // Δέσμευση αντικειμένου από την ομάδα
    T* allocate() {
        if (!freeList) {
            throw bad_alloc();
        }
        
        Block* block = freeList;
        freeList = block->next;
        ++allocatedCount;
        
        // Χρήση placement new για κατασκευή αντικειμένου σε προδεσμευμένη μνήμη
        return new(&block->object) T();
    }
    
    // Αποδέσμευση αντικειμένου πίσω στην ομάδα
    void deallocate(T* ptr) {
        if (!ptr) return;
        
        // Κλήση καταστροφέα
        ptr->~T();
        
        // Εύρεση αντίστοιχου block
        Block* block = reinterpret_cast<Block*>(ptr);
        
        // Προσθήκη πίσω στη λίστα ελεύθερων
        block->next = freeList;
        freeList = block;
        --allocatedCount;
    }
    
    // Επαναφορά ολόκληρης της ομάδας
    void reset() {
        // Καταστροφή όλων των δεσμευμένων αντικειμένων
        // Αυτή είναι απλοποιημένη έκδοση - στην πράξη, θα χρειαστείτε να παρακολουθείτε τα δεσμευμένα αντικείμενα
        pool.clear();
        pool.resize(PoolSize);
        
        // Ανακατασκευή λίστας ελεύθερων
        for (size_t i = 0; i < PoolSize - 1; ++i) {
            pool[i].next = &pool[i + 1];
        }
        pool[PoolSize - 1].next = nullptr;
        freeList = &pool[0];
        allocatedCount = 0;
    }
    
    size_t getAllocatedCount() const { return allocatedCount; }
    size_t getFreeCount() const { return PoolSize - allocatedCount; }
};

// Κλάση για επίδειξη χρήσης ομάδας μνήμης
class ExpensiveObject {
private:
    int id;
    vector<int> data;  // Προσομοίωση δαπανηρής αρχικοποίησης
    
public:
    ExpensiveObject(int objId = 0) : id(objId), data(1000, objId) {
        cout << "ExpensiveObject " << id << " created" << endl;
    }
    
    ~ExpensiveObject() {
        cout << "ExpensiveObject " << id << " destroyed" << endl;
    }
    
    int getId() const { return id; }
    size_t getDataSize() const { return data.size(); }
    
    void doWork() {
        // Προσομοίωση κάποιας εργασίας
        int sum = 0;
        for (int val : data) {
            sum += val;
        }
        cout << "Object " << id << " processed " << data.size() << " elements, sum: " << sum << endl;
    }
};

// Παράδειγμα προσαρμοσμένου κατανεμητή
template<typename T>
class TrackingAllocator {
public:
    using value_type = T;
    
    // Στατικοί μετρητές για παρακολούθηση δεσμεύσεων
    static size_t allocation_count;
    static size_t deallocation_count;
    static size_t bytes_allocated;
    static size_t bytes_deallocated;
    
    TrackingAllocator() = default;
    
    template<typename U>
    TrackingAllocator(const TrackingAllocator<U>&) {}
    
    T* allocate(size_t n) {
        T* ptr = static_cast<T*>(::operator new(n * sizeof(T)));
        allocation_count++;
        bytes_allocated += n * sizeof(T);
        cout << "Allocated " << n << " objects of size " << sizeof(T) 
             << ", total allocated: " << bytes_allocated << " bytes" << endl;
        return ptr;
    }
    
    void deallocate(T* ptr, size_t n) {
        deallocation_count++;
        bytes_deallocated += n * sizeof(T);
        cout << "Deallocated " << n << " objects of size " << sizeof(T) 
             << ", total deallocated: " << bytes_deallocated << " bytes" << endl;
        ::operator delete(ptr);
    }
    
    template<typename U>
    bool operator==(const TrackingAllocator<U>&) const { return true; }
    
    template<typename U>
    bool operator!=(const TrackingAllocator<U>&) const { return false; }
};

// Αρχικοποίηση στατικών μελών
template<typename T>
size_t TrackingAllocator<T>::allocation_count = 0;

template<typename T>
size_t TrackingAllocator<T>::deallocation_count = 0;

template<typename T>
size_t TrackingAllocator<T>::bytes_allocated = 0;

template<typename T>
size_t TrackingAllocator<T>::bytes_deallocated = 0;

void demonstrateMemoryPool() {
    cout << "=== Memory Pool Demonstration ===" << endl;
    
    MemoryPool<ExpensiveObject, 10> pool;
    
    cout << "Initial pool state - Allocated: " << pool.getAllocatedCount() 
         << ", Free: " << pool.getFreeCount() << endl;
    
    // Δέσμευση αντικειμένων από την ομάδα
    vector<ExpensiveObject*> objects;
    for (int i = 0; i < 5; ++i) {
        ExpensiveObject* obj = pool.allocate();
        obj->doWork();
        objects.push_back(obj);
        
        cout << "After allocation " << (i + 1) << " - Allocated: " << pool.getAllocatedCount() 
             << ", Free: " << pool.getFreeCount() << endl;
    }
    
    // Αποδέσμευση μερικών αντικειμένων
    cout << "\nDeallocating objects..." << endl;
    for (int i = 0; i < 2; ++i) {
        pool.deallocate(objects[i]);
        objects[i] = nullptr;
        
        cout << "After deallocation " << (i + 1) << " - Allocated: " << pool.getAllocatedCount() 
             << ", Free: " << pool.getFreeCount() << endl;
    }
    
    // Καθαρισμός υπόλοιπων αντικειμένων
    for (size_t i = 2; i < objects.size(); ++i) {
        if (objects[i]) {
            pool.deallocate(objects[i]);
        }
    }
}

void demonstrateCustomAllocator() {
    cout << "\n=== Custom Allocator Demonstration ===" << endl;
    
    // Επαναφορά μετρητών
    TrackingAllocator<int>::allocation_count = 0;
    TrackingAllocator<int>::deallocation_count = 0;
    TrackingAllocator<int>::bytes_allocated = 0;
    TrackingAllocator<int>::bytes_deallocated = 0;
    
    {
        // Χρήση προσαρμοσμένου κατανεμητή με vector
        vector<int, TrackingAllocator<int>> trackedVec;
        
        // Προσθήκη στοιχείων
        for (int i = 0; i < 100; ++i) {
            trackedVec.push_back(i);
        }
        
        cout << "Vector size: " << trackedVec.size() << endl;
    }
    
    cout << "Final stats - Allocations: " << TrackingAllocator<int>::allocation_count
         << ", Deallocations: " << TrackingAllocator<int>::deallocation_count << endl;
    cout << "Net allocated: " << (TrackingAllocator<int>::bytes_allocated - 
                                  TrackingAllocator<int>::bytes_deallocated) << " bytes" << endl;
}

void performanceComparison() {
    cout << "\n=== Performance Comparison ===" << endl;
    
    const int numObjects = 1000;
    
    // Χρονομέτρηση κανονικής δέσμευσης
    auto start = chrono::high_resolution_clock::now();
    vector<unique_ptr<ExpensiveObject>> regularObjects;
    for (int i = 0; i < numObjects; ++i) {
        regularObjects.push_back(make_unique<ExpensiveObject>(i));
    }
    auto end = chrono::high_resolution_clock::now();
    auto regularTime = chrono::duration_cast<chrono::microseconds>(end - start);
    
    cout << "Regular allocation time: " << regularTime.count() << " microseconds" << endl;
    
    // Χρονομέτρηση δέσμευσης από ομάδα μνήμης
    MemoryPool<ExpensiveObject, numObjects> pool;
    start = chrono::high_resolution_clock::now();
    vector<ExpensiveObject*> poolObjects;
    for (int i = 0; i < numObjects; ++i) {
        poolObjects.push_back(pool.allocate());
    }
    end = chrono::high_resolution_clock::now();
    auto poolTime = chrono::duration_cast<chrono::microseconds>(end - start);
    
    cout << "Pool allocation time: " << poolTime.count() << " microseconds" << endl;
    
    // Καθαρισμός αντικειμένων ομάδας
    for (auto obj : poolObjects) {
        pool.deallocate(obj);
    }
    
    cout << "Performance ratio (regular/pool): " << (double)regularTime.count() / poolTime.count() << endl;
}

int main() {
    demonstrateMemoryPool();
    demonstrateCustomAllocator();
    performanceComparison();
    
    return 0;
}
```

---

## Συμπέρασμα

Αυτός ο πλήρης οδηγός καλύπτει τον προγραμματισμό σε C++ από τις βασικές έννοιες έως τις προχωρημένες αρχές ΑΠ (Αντικειμενοστραφούς Προγραμματισμού) και τη διαχείριση μνήμης. Κάθε ενότητα βασίζεται στην προηγούμενη, παρέχοντας μια σταθερή βάση για την κατανόηση του προγραμματισμού σε C++.

Βασικές έννοιες που καλύπτονται:
- Βασική εκτύπωση και λειτουργίες μεταβλητών
- Έλεγχος ροής (if/else, switch)
- Βρόχοι (for, while, do-while)
- Πίνακες (arrays)
- Συναρτήσεις (πέρασμα-κατά-τιμή έναντι πέρασμα-κατά-αναφορά)
- Δείκτες και αναφορές
- Διανύσματα (δυναμικοί πίνακες)
- Χάρτες (συσχετιστικοί περιέκτες)
- Κλάσεις και αντικείμενα (τα βασικά)
- Κατασκευαστές και καταστροφείς
- Ο δείκτης `this`
- Αρχές αντικειμενοστραφούς προγραμματισμού (ενθυλάκωση, αφαίρεση)
- Κληρονομικότητα και πολυμορφισμός
- Προχωρημένη διαχείριση μνήμης (σωρός έναντι στοίβας, έξυπνοι δείκτες)

