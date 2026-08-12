# Hashing

## Contents
1. [Introduction](#introduction)
2. [Hash Functions](#hash-functions)
3. [Collisions and Resolution](#collisions-and-resolution)
4. [Open Addressing](#open-addressing)
5. [Closed Addressing](#closed-addressing)
6. [Complexity](#complexity)
7. [Examples](#examples)

---

## Introduction

**Hashing** is a technique for storing and retrieving data in constant time O(1) on average.

### Basic Concepts

- **Hash Table**: Data structure that stores key-value pairs
- **Hash Function**: Converts keys to table indices
- **Collision**: When two keys map to the same index
- **Load Factor**: alpha = n/m where n = number of elements, m = table size

### Hash Table Visualization

```mermaid
graph LR
    A[Key: 'apple'] --> B[Hash Function]
    B --> C[Index: 3]
    C --> D[Hash Table]
    
    E[Key: 'banana'] --> F[Hash Function]
    F --> G[Index: 7]
    G --> D
    
    D --> H[0: null]
    D --> I[1: null]
    D --> J[2: null]
    D --> K[3: 'apple']
    D --> L[4: null]
    D --> M[5: null]
    D --> N[6: null]
    D --> O[7: 'banana']
```

---

## Hash Functions

### 1. Division Method

**Formula**: `h(k) = k mod m`

Where:
- `k` = key
- `m` = table size (usually a prime number)

**Example**:
```
m = 11 (table size)

h(25) = 25 mod 11 = 3
h(37) = 37 mod 11 = 4
h(42) = 42 mod 11 = 9
h(58) = 58 mod 11 = 3  ← Collision with 25!
```

### 2. Multiplication Method

**Formula**: `h(k) = ⌊m × (k × A mod 1)⌋`

Where:
- `A` = constant (0 < A < 1), often A ≈ 0.6180339887 (golden ratio)
- `k × A mod 1` = fractional part of k × A

**Example**:
```
m = 8, A = 0.618

h(123) = ⌊8 × (123 × 0.618 mod 1)⌋
       = ⌊8 × (76.014 mod 1)⌋
       = ⌊8 × 0.014⌋
       = ⌊0.112⌋ = 0
```

### 3. Universal Hashing

**Formula**: `h(k) = ((a × k + b) mod p) mod m`

Where:
- `p` = large prime number
- `a`, `b` = random constants

**Example**:
```
m = 10, p = 17, a = 3, b = 5

h(8) = ((3 × 8 + 5) mod 17) mod 10
     = ((24 + 5) mod 17) mod 10
     = (29 mod 17) mod 10
     = 12 mod 10 = 2
```

### 4. Hashing for Strings

**Polynomial Method**:

`h(s) = (s[0] × p^(n-1) + s[1] × p^(n-2) + ... + s[n-1]) mod m`

**Example**:
```cpp
#include <string>

long long hashString(std::string s, int m = 101, int p = 31) {
    long long hash_value = 0;
    for (char c : s) {
        hash_value = (hash_value * p + c) % m;
    }
    return hash_value;
}

// Example
// h("cat") = (99×31² + 97×31 + 116) mod 101
//          = (95019 + 3007 + 116) mod 101
//          = 98142 mod 101 = 40
```

---

## Collisions and Resolution

### What is a Collision?

When `h(k₁) = h(k₂)` but `k₁ ≠ k₂`

### Resolution Methods

```mermaid
graph TD
    A[Collision Resolution Methods] --> B[Closed Addressing<br/>Closed Addressing]
    A --> C[Open Addressing<br/>Open Addressing]
    
    B --> D[Chaining<br/>Chaining]
    
    C --> E[Linear Probing<br/>Linear Probing]
    C --> F[Quadratic Probing<br/>Quadratic Probing]
    C --> G[Double Hashing<br/>Double Hashing]
```

---

## Closed Addressing (Chaining)

### Operating Principle

Each position in the table contains a linked list with all elements that hash to that position.

### Visualization

```mermaid
graph TD
    subgraph "Hash Table with Chaining"
    H0[0: ] --> L0[null]
    H1[1: ] --> L1[21] --> L1B[43] --> L1C[null]
    H2[2: ] --> L2[14] --> L2B[null]
    H3[3: ] --> L3[25] --> L3B[58] --> L3C[null]
    H4[4: ] --> L4[37] --> L4B[null]
    H5[5: ] --> L5[null]
    H6[6: ] --> L6[null]
    H7[7: ] --> L7[null]
    H8[8: ] --> L8[null]
    H9[9: ] --> L9[42] --> L9B[null]
    H10[10: ] --> L10[null]
    end
```

### Example 1: Inserting Elements

**Data**: Insert the numbers [25, 37, 42, 58, 14, 21, 43] into a table of size m=11

```
Step 1: h(25) = 25 mod 11 = 3
┌───┬────┐
│ 0 │    │
│ 1 │    │
│ 2 │    │
│ 3 │ 25 │
│ 4 │    │
└───┴────┘

Step 2: h(37) = 37 mod 11 = 4
┌───┬────┐
│ 3 │ 25 │
│ 4 │ 37 │
└───┴────┘

Step 3: h(42) = 42 mod 11 = 9
┌───┬────┐
│ 3 │ 25 │
│ 4 │ 37 │
│ 9 │ 42 │
└───┴────┘

Step 4: h(58) = 58 mod 11 = 3 ← Collision!
┌───┬─────────┐
│ 3 │ 25 → 58 │
│ 4 │ 37      │
│ 9 │ 42      │
└───┴─────────┘

Step 5-7: Continuing...
┌────┬──────────────┐
│ 1  │ 21 → 43      │
│ 2  │ 14           │
│ 3  │ 25 → 58      │
│ 4  │ 37           │
│ 9  │ 42           │
└────┴──────────────┘
```

### C++ Implementation

```cpp
#include <iostream>
#include <vector>
#include <list>
#include <string>

template <typename K, typename V>
class HashTableChaining {
private:
    struct Node {
        K key;
        V value;
        Node(K k, V v) : key(k), value(v) {}
    };

    int size;
    std::vector<std::list<Node>> table;
    int count;

    int hashFunction(K key) {
        return (int)(key % size);
    }

public:
    HashTableChaining(int s = 11) : size(s), table(s), count(0) {}

    void insert(K key, V value) {
        int index = hashFunction(key);
        for (auto& node : table[index]) {
            if (node.key == key) {
                node.value = value;
                return;
            }
        }
        table[index].emplace_back(key, value);
        count++;
    }

    V* search(K key) {
        int index = hashFunction(key);
        for (auto& node : table[index]) {
            if (node.key == key) return &node.value;
        }
        return nullptr;
    }

    bool remove(K key) {
        int index = hashFunction(key);
        auto& chain = table[index];
        for (auto it = chain.begin(); it != chain.end(); ++it) {
            if (it->key == key) {
                chain.erase(it);
                count--;
                return true;
            }
        }
        return false;
    }

    void display() {
        for (int i = 0; i < size; ++i) {
            std::cout << i << ": ";
            for (const auto& node : table[i]) {
                std::cout << "(" << node.key << ", " << node.value << ") -> ";
            }
            std::cout << "nullptr" << std::endl;
        }
    }
};
```

### Usage Example

```cpp
int main() {
    // Create hash table
    HashTableChaining<int, std::string> ht(11);

    // Insert elements
    std::vector<int> elements = {25, 37, 42, 58, 14, 21, 43};
    for (int num : elements) {
        ht.insert(num, "Value_" + std::to_string(num));
    }

    // Display
    ht.display();

    // Search
    std::string* val = ht.search(58);
    if (val) std::cout << "\nSearch 58: " << *val << std::endl;
    else std::cout << "\nSearch 58: Not found" << std::endl;

    // Delete
    ht.remove(42);
    std::cout << "\nAfter deleting 42:" << std::endl;
    ht.display();
    
    return 0;
}
```

**Output**:
```
0: None
1: (43, Value_43) -> (21, Value_21) -> None
2: (14, Value_14) -> None
3: (58, Value_58) -> (25, Value_25) -> None
4: (37, Value_37) -> None
5: None
6: None
7: None
8: None
9: (42, Value_42) -> None
10: None

Search 58: Value_58
Search 100: None

After deleting 42:
9: None
```

---

## Open Addressing

### Operating Principle

All elements are stored **inside the table**. In case of a collision, we search for the next available position.

### 1. Linear Probing

**Formula**: `h(k, i) = (h'(k) + i) mod m`

Where:
- `h'(k)` = initial hash function
- `i` = probe number (0, 1, 2, ...)

### Linear Probing Example

**Data**: Insert [25, 37, 42, 58, 14, 26] into a table of size m=11

```
Step 1: h(25, 0) = 25 mod 11 = 3
┌───┬────┐
│ 3 │ 25 │
└───┴────┘

Step 2: h(37, 0) = 37 mod 11 = 4
┌───┬────┐
│ 3 │ 25 │
│ 4 │ 37 │
└───┴────┘

Step 3: h(42, 0) = 42 mod 11 = 9
┌───┬────┐
│ 3 │ 25 │
│ 4 │ 37 │
│ 9 │ 42 │
└───┴────┘

Step 4: h(58, 0) = 58 mod 11 = 3 ← Occupied!
        h(58, 1) = (3 + 1) mod 11 = 4 ← Occupied!
        h(58, 2) = (3 + 2) mod 11 = 5 ← Free!
┌───┬────┐
│ 3 │ 25 │
│ 4 │ 37 │
│ 5 │ 58 │
│ 9 │ 42 │
└───┴────┘

Step 5: h(14, 0) = 14 mod 11 = 3 ← Occupied!
        h(14, 1) = 4 ← Occupied!
        h(14, 2) = 5 ← Occupied!
        h(14, 3) = 6 ← Free!
┌───┬────┐
│ 3 │ 25 │
│ 4 │ 37 │
│ 5 │ 58 │
│ 6 │ 14 │
│ 9 │ 42 │
└───┴────┘

Step 6: h(26, 0) = 26 mod 11 = 4 ← Occupied!
        Continuing: 5, 6, 7 (Free!)
┌───┬────┐
│ 3 │ 25 │
│ 4 │ 37 │
│ 5 │ 58 │
│ 6 │ 14 │
│ 7 │ 26 │
│ 9 │ 42 │
└───┴────┘
```

### Problem: Primary Clustering

Large contiguous regions of occupied positions are created.

```mermaid
graph LR
    A[Clustering] --> B[Long chains of<br/>occupied positions]
    B --> C[Increased<br/>search time]
    C --> D[Degraded<br/>performance]
```

### Linear Probing Implementation

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <optional>

template <typename K, typename V>
class HashTableLinearProbing {
private:
    struct Entry {
        K key;
        V value;
        bool occupied = false;
    };

    int size;
    std::vector<Entry> table;
    int count;

    int hashFunction(K key) {
        return (int)(key % size);
    }

public:
    HashTableLinearProbing(int s = 11) : size(s), table(s), count(0) {}

    void insert(K key, V value) {
        if (count >= size) throw std::runtime_error("The table is full!");

        int index = hashFunction(key);
        int i = 0;

        while (table[(index + i) % size].occupied) {
            if (table[(index + i) % size].key == key) {
                table[(index + i) % size].value = value;
                return;
            }
            i++;
            if (i >= size) break;
        }

        table[(index + i) % size] = {key, value, true};
        count++;
    }

    V* search(K key) {
        int index = hashFunction(key);
        int i = 0;

        while (table[(index + i) % size].occupied) {
            if (table[(index + i) % size].key == key) {
                return &table[(index + i) % size].value;
            }
            i++;
            if (i >= size) break;
        }
        return nullptr;
    }

    void display() {
        for (int i = 0; i < size; ++i) {
            if (table[i].occupied)
                std::cout << i << ": (" << table[i].key << ", " << table[i].value << ")" << std::endl;
            else
                std::cout << i << ": nullptr" << std::endl;
        }
    }
};
```

### 2. Quadratic Probing

**Formula**: `h(k, i) = (h'(k) + c₁×i + c₂×i²) mod m`

Often we use: `h(k, i) = (h'(k) + i²) mod m`

### Quadratic Probing Example

**Data**: Insert [25, 37, 58, 14] into a table of size m=11

```
h(25, 0) = (25 + 0²) mod 11 = 3
h(37, 0) = (37 + 0²) mod 11 = 4
h(58, 0) = (58 + 0²) mod 11 = 3 ← Collision
h(58, 1) = (3 + 1²) mod 11 = 4 ← Collision
h(58, 2) = (3 + 2²) mod 11 = 7 ← Free!
h(14, 0) = (14 + 0²) mod 11 = 3 ← Collision
h(14, 1) = (3 + 1²) mod 11 = 4 ← Collision
h(14, 2) = (3 + 2²) mod 11 = 7 ← Collision
h(14, 3) = (3 + 3²) mod 11 = 1 ← Free!

Final Table:
┌───┬────┐
│ 1 │ 14 │
│ 3 │ 25 │
│ 4 │ 37 │
│ 7 │ 58 │
└───┴────┘
```

### 3. Double Hashing

**Formula**: `h(k, i) = (h₁(k) + i × h₂(k)) mod m`

Where:
- `h₁(k) = k mod m` (primary function)
- `h₂(k) = 1 + (k mod (m-1))` (secondary function)

### Double Hashing Example

**Data**: m=11, Insert [25, 37, 58]

```
h₁(25) = 25 mod 11 = 3
h₂(25) = 1 + (25 mod 10) = 1 + 5 = 6
→ Position 3

h₁(37) = 37 mod 11 = 4
h₂(37) = 1 + (37 mod 10) = 1 + 7 = 8
→ Position 4

h₁(58) = 58 mod 11 = 3 ← Collision
h₂(58) = 1 + (58 mod 10) = 1 + 8 = 9
h(58, 0) = 3
h(58, 1) = (3 + 1×9) mod 11 = 12 mod 11 = 1 ← Free!

Final Table:
┌───┬────┐
│ 1 │ 58 │
│ 3 │ 25 │
│ 4 │ 37 │
└───┴────┘
```

### Method Comparison

```mermaid
graph TD
    A[Probing Methods] --> B[Linear Probing]
    A --> C[Quadratic Probing]
    A --> D[Double Hashing]
    
    B --> E[+ Simple<br/>- Primary Clustering]
    C --> F[+ Reduces Clustering<br/>- Secondary Clustering]
    D --> G[+ Better distribution<br/>- More complex]
```

---

## Complexity

### Chaining

| Operation | Average Case | Worst Case |
|-----------|--------------|------------|
| Insertion | O(1)         | O(n)       |
| Search    | O(1 + alpha) | O(n)       |
| Deletion  | O(1 + alpha) | O(n)       |

Where alpha = n/m (load factor)

### Open Addressing

| Operation | Average Case | Worst Case |
|-----------|--------------|------------|
| Insertion | O(1/(1-alpha))| O(n)       |
| Search    | O(1/(1-alpha))| O(n)       |
| Deletion  | O(1/(1-alpha))| O(n)       |

**Note**: For alpha < 0.7, performance remains good.

### Load Factor Analysis

```
alpha = 0.5:  Average number of probes ≈ 1.5
alpha = 0.75: Average number of probes ≈ 4
alpha = 0.9:  Average number of probes ≈ 10
alpha ≥ 1:    Rehashing required
```

---

## Application Examples

### Example 1: Word Frequency Dictionary

```cpp
#include <iostream>
#include <string>
#include <unordered_map>
#include <sstream>
#include <algorithm>

std::unordered_map<std::string, int> wordFrequency(std::string text) {
    std::unordered_map<std::string, int> freq;
    std::stringstream ss(text);
    std::string word;
    
    while (ss >> word) {
        // Convert to lowercase
        std::transform(word.begin(), word.end(), word.begin(), ::tolower);
        freq[word]++;
    }
    
    return freq;
}

// Usage
int main() {
    std::string text = "the book is good the book has many pages";
    auto result = wordFrequency(text);
    
    for (const auto& pair : result) {
        std::cout << pair.first << ": " << pair.second << std::endl;
    }
    return 0;
}
```

### Example 2: Duplicate Detection

```cpp
#include <iostream>
#include <vector>
#include <unordered_set>

std::vector<int> findDuplicates(const std::vector<int>& arr) {
    std::unordered_set<int> seen;
    std::unordered_set<int> duplicates;
    
    for (int num : arr) {
        if (seen.count(num)) {
            duplicates.insert(num);
        } else {
            seen.insert(num);
        }
    }
    
    return std::vector<int>(duplicates.begin(), duplicates.end());
}

// Usage
int main() {
    std::vector<int> numbers = {1, 2, 3, 2, 4, 5, 3, 6, 7, 5};
    auto dups = findDuplicates(numbers);
    
    for (int n : dups) std::cout << n << " ";
    return 0;
}
```

### Example 3: Two Sum Problem

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

std::vector<int> twoSum(std::vector<int>& nums, int target) {
    std::unordered_map<int, int> seen;
    
    for (int i = 0; i < nums.size(); i++) {
        int complement = target - nums[i];
        if (seen.count(complement)) {
            return {seen[complement], i};
        }
        seen[nums[i]] = i;
    }
    return {};
}

// Usage
int main() {
    std::vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    auto result = twoSum(nums, target);
    if (!result.empty())
        std::cout << "[" << result[0] << ", " << result[1] << "]" << std::endl;
    return 0;
}
```

**Step by Step**:
```
nums = [2, 7, 11, 15], target = 9

Step 1: num=2, complement=7
  seen = {2: 0}

Step 2: num=7, complement=2
  2 exists in seen!
  Return: [0, 1]
```

### Example 4: Anagram Detection

```cpp
#include <iostream>
#include <string>
#include <unordered_map>

bool areAnagrams(std::string s1, std::string s2) {
    if (s1.length() != s2.length()) return false;
    
    std::unordered_map<char, int> char_count;
    
    for (char c : s1) char_count[c]++;
    
    for (char c : s2) {
        if (!char_count.count(c)) return false;
        char_count[c]--;
        if (char_count[c] < 0) return false;
    }
    
    for (auto const& [key, val] : char_count) {
        if (val != 0) return false;
    }
    return true;
}

// Usage
int main() {
    std::cout << std::boolalpha << areAnagrams("listen", "silent") << std::endl; // true
    std::cout << std::boolalpha << areAnagrams("hello", "world") << std::endl;  // false
    return 0;
}
```

---

## Practical Exercise 1: Cache Implementation

Implement a cache system with LRU (Least Recently Used) eviction policy.

### Solution

```cpp
#include <iostream>
#include <unordered_map>
#include <list>

class LRUCache {
private:
    struct Node {
        int key, value;
        Node(int k, int v) : key(k), value(v) {}
    };

    int capacity;
    std::list<Node> cacheList;
    std::unordered_map<int, std::list<Node>::iterator> cacheMap;

public:
    LRUCache(int cap) : capacity(cap) {}

    int get(int key) {
        if (cacheMap.find(key) == cacheMap.end()) return -1;
        
        // Move to front (recently used)
        cacheList.splice(cacheList.begin(), cacheList, cacheMap[key]);
        return cacheMap[key]->value;
    }

    void put(int key, int value) {
        if (cacheMap.find(key) != cacheMap.end()) {
            cacheList.splice(cacheList.begin(), cacheList, cacheMap[key]);
            cacheMap[key]->value = value;
            return;
        }

        if (cacheList.size() == capacity) {
            int lastKey = cacheList.back().key;
            cacheList.pop_back();
            cacheMap.erase(lastKey);
        }

        cacheList.emplace_front(key, value);
        cacheMap[key] = cacheList.begin();
    }
};

// Usage
int main() {
    LRUCache cache(2);
    cache.put(1, 1);
    cache.put(2, 2);
    std::cout << cache.get(1) << std::endl;    // 1
    cache.put(3, 3);                           // Removes 2
    std::cout << cache.get(2) << std::endl;    // -1
    return 0;
}
```

**Visualization**:
```
Capacity = 2

put(1, 1): [1]
put(2, 2): [2, 1]
get(1):    [1, 2] (1 moved to front)
put(3, 3): [3, 1] (2 removed - LRU)
```

---

## Practical Exercise 2: Group Anagrams

Given a list of words. Group the anagrams together.

### Solution

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>

std::vector<std::vector<std::string>> groupAnagrams(std::vector<std::string>& words) {
    std::unordered_map<std::string, std::vector<std::string>> groups;
    
    for (const std::string& word : words) {
        std::string sorted_word = word;
        std::sort(sorted_word.begin(), sorted_word.end());
        groups[sorted_word].push_back(word);
    }
    
    std::vector<std::vector<std::string>> result;
    for (auto const& [key, group] : groups) {
        result.push_back(group);
    }
    return result;
}

// Usage
int main() {
    std::vector<std::string> words = {"eat", "tea", "tan", "ate", "nat", "bat"};
    auto result = groupAnagrams(words);
    // Print results...
    return 0;
}
```

**Step by Step**:
```
words = ["eat", "tea", "tan", "ate", "nat", "bat"]

"eat" → sorted: "aet" → {"aet": ["eat"]}
"tea" → sorted: "aet" → {"aet": ["eat", "tea"]}
"tan" → sorted: "ant" → {"aet": [...], "ant": ["tan"]}
"ate" → sorted: "aet" → {"aet": ["eat", "tea", "ate"], ...}
"nat" → sorted: "ant" → {..., "ant": ["tan", "nat"]}
"bat" → sorted: "abt" → {..., "abt": ["bat"]}

Result: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```

---

## Practical Exercise 3: Longest Consecutive Sequence

Find the length of the longest consecutive sequence of numbers.

### Solution

```cpp
#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>

int longestConsecutive(std::vector<int>& nums) {
    std::unordered_set<int> num_set(nums.begin(), nums.end());
    int max_length = 0;
    
    for (int num : num_set) {
        if (!num_set.count(num - 1)) {
            int current_num = num;
            int current_length = 1;
            
            while (num_set.count(current_num + 1)) {
                current_num++;
                current_length++;
            }
            max_length = std::max(max_length, current_length);
        }
    }
    return max_length;
}

// Usage
int main() {
    std::vector<int> nums = {100, 4, 200, 1, 3, 2};
    std::cout << longestConsecutive(nums) << std::endl; // 4
    return 0;
}
```

**Analysis**:
```
nums = [100, 4, 200, 1, 3, 2]
num_set = {100, 4, 200, 1, 3, 2}

Check 100: 99 does not exist → Start of sequence
  100 → 101 does not exist → Length: 1

Check 1: 0 does not exist → Start of sequence
  1 → 2 → 3 → 4 → 5 does not exist → Length: 4 

Check 2, 3, 4: 1, 2, 3 exist → Not a start

Maximum: 4
```

---

## Summary

### Advantages of Hash Tables

- O(1) average time complexity for insert, search, delete
- Flexible and easy to use
- Ideal for fast searching

### Disadvantages

- Worst case: O(n)
- Do not maintain element order
- Require extra memory
- Collisions reduce performance

### When to Use

- Fast element search
- Existence checking
- Frequency counting
- Cache implementations
- Data grouping

### Key Points

1. **Good hash function**: Uniform distribution
2. **Load factor**: Maintain alpha < 0.75
3. **Method selection**: Chaining vs Open Addressing
4. **Rehashing**: When the table is full
