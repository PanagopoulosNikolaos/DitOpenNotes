## 1. Δυαδική Αναζήτηση

Η δυαδική αναζήτηση εργάζεται διαιρώντας επαναληπτικά το χώρο αναζήτησης στη μέση. Συγκρίνει το στοιχείο στη μέση θέση με την τιμή-στόχο και αποφασίζει αν θα συνεχίσει την αναζήτηση στο αριστερό ή δεξί μισό του πίνακα. Σε κάθε βήμα, το μέγεθος του χώρου αναζήτησης μειώνεται κατά το ήμισυ, καταλήγοντας είτε στην εύρεση του στοιχείου είτε σε άδειο υποπίνακα.

**Προϋπόθεση:** Ο πίνακας πρέπει να είναι **ταξινομημένος**. Χωρίς ταξινόμηση, η λογική της διαίρεσης του χώρου αναζήτησης βάσει σύγκρισης με το μεσαίο στοιχείο δεν λειτουργεί.

## 2. Αναδρομή vs Επανάληψη

Η αναδρομή θεωρείται εναλλακτική της επανάληψης επειδή και οι δύο τεχνικές μπορούν να εκφράσουν τις ίδιες υπολογιστικές διαδικασίες. Η αναδρομή μπορεί να αντικατασταθεί από επανάληψη με ρητή στοίβα κλήσεων, ενώ η επανάληψη μπορεί να αντικατασταθεί με αναδρομή ουράς.


**C++:**
```cpp
#include <iostream>

// Recursive approach
int factorialRecursive(int n) {
    if (n == 0) return 1;
    return n * factorialRecursive(n - 1);
}

// Iterative approach
int factorialIterative(int n) {
    int result = 1;
    for (int i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}

int main() {
    std::cout << "Factorial of 5 (recursive): " << factorialRecursive(5) << std::endl;
    std::cout << "Factorial of 5 (iterative): " << factorialIterative(5) << std::endl;
    return 0;
}
```


## 3. Σύγκριση Ταξινόμησης

| Χαρακτηριστικό | Insertion Sort | Selection Sort | Bubble Sort |
|---|---|---|---|
| **Μέση Πολυπλοκότητα** | O(n²)  | O(n²)  | O(n²)  |
| **Καλύτερη Περίπτωση** | O(n)  | O(n²)  | O(n)  |
| **Χειρότερη Περίπτωση** | O(n²)  | O(n²)  | O(n²)  |
| **Προσαρμοστικότητα** | Ναι  | Όχι  | Όχι  |
| **Ανταλλαγές** | Λιγότερες  | Ελάχιστες  | Πολλές  |
| **Ταχύτητα** | Γρηγορότερη  | Μέτρια | Πιο αργή  |

Η insertion sort συγκρίνει κάθε στοιχείο με το ταξινομημένο τμήμα αριστερά και το τοποθετεί στη σωστή θέση. Η selection sort βρίσκει το ελάχιστο στοιχείο και το τοποθετεί στην αρχή. Η bubble sort συγκρίνει και ανταλλάσσει γειτονικά στοιχεία επαναληπτικά.

**C++:**

```cpp
#include <iostream>
#include <vector>

void insertionSort(std::vector<int>& arr) {
    for (int i = 1; i < arr.size(); i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

void selectionSort(std::vector<int>& arr) {
    for (int i = 0; i < arr.size() - 1; i++) {
        int min_idx = i;
        for (int j = i + 1; j < arr.size(); j++) {
            if (arr[j] < arr[min_idx])
                min_idx = j;
        }
        std::swap(arr[min_idx], arr[i]);
    }
}

void bubbleSort(std::vector<int>& arr) {
    int n = arr.size();
    bool swapped;
    for (int i = 0; i < n - 1; i++) {
        swapped = false;
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                std::swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
        if (!swapped) break;
    }
}

void printArray(const std::vector<int>& arr) {
    for (int val : arr)
        std::cout << val << " ";
    std::cout << std::endl;
}

int main() {
    std::vector<int> arr1 = {64, 34, 25, 12, 22, 11, 90};
    std::vector<int> arr2 = arr1;
    std::vector<int> arr3 = arr1;
    
    insertionSort(arr1);
    std::cout << "Insertion Sort: ";
    printArray(arr1);
    
    selectionSort(arr2);
    std::cout << "Selection Sort: ";
    printArray(arr2);
    
    bubbleSort(arr3);
    std::cout << "Bubble Sort: ";
    printArray(arr3);
    
    return 0;
}
```


## 4. Divide and Conquer - Merge Sort

Το **Merge Sort** εφαρμόζει τη στρατηγική Διαίρει και Βασίλευε.

**Στάδια:**
1. **Διαίρεση (Divide):** Χωρισμός του πίνακα στη μέση σε δύο υποπίνακες
2. **Κατάκτηση (Conquer):** Αναδρομική ταξινόμηση κάθε υποπίνακα μέχρι να απομείνουν μονά στοιχεία
3. **Συνδυασμός (Combine):** Συγχώνευση των ταξινομημένων υποπινάκων σε ενιαίο ταξινομημένο πίνακα

Η διαδικασία συνεχίζεται αναδρομικά μέχρι όλα τα στοιχεία να ενωθούν σε έναν πλήρως ταξινομημένο πίνακα.



**C++:**

```cpp
#include <iostream>
#include <vector>

void merge(std::vector<int>& arr, int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;
    
    std::vector<int> L(n1), R(n2);
    
    for (int i = 0; i < n1; i++)
        L[i] = arr[left + i];
    for (int j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j];
    
    int i = 0, j = 0, k = left;
    
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k++] = L[i++];
        } else {
            arr[k++] = R[j++];
        }
    }
    
    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];
}

void mergeSort(std::vector<int>& arr, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        
        mergeSort(arr, left, mid);      // Divide left
        mergeSort(arr, mid + 1, right); // Divide right
        merge(arr, left, mid, right);   // Combine
    }
}

int main() {
    std::vector<int> arr = {70, 50, 30, 10, 20, 40, 60};
    
    std::cout << "Original array: ";
    for (int val : arr) std::cout << val << " ";
    std::cout << std::endl;
    
    mergeSort(arr, 0, arr.size() - 1);
    
    std::cout << "Sorted array: ";
    for (int val : arr) std::cout << val << " ";
    std::cout << std::endl;
    
    return 0;
}
```


## 5. Πίνακας Πολυπλοκότητας

| Αλγόριθμος | Πολυπλοκότητα (Μέση) |
|---|---|
| Selection Sort | O(n²)  |
| Insertion Sort | O(n²)  |
| Merge Sort | O(n log n)  |
| Quick Sort | O(n log n)  |