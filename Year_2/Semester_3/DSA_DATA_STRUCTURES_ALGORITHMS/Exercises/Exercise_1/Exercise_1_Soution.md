## 1. Best, Average, Worst Case

**Best case:** Minimum operations required

**Average case:** Expected operations for typical input

**Worst case:** Maximum operations required

### Python
```python
# Linear Search example
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Best case: O(1) - element at index 0
arr_best = [5, 2, 8, 1, 9]
print(linear_search(arr_best, 5))  # Found immediately


# Average case: O(n/2) ≈ O(n) - element in middle
arr_avg = [1, 2, 8, 5, 9]
print(linear_search(arr_avg, 5))  # Found at middle


# Worst case: O(n) - element at end or not found
arr_worst = [1, 2, 8, 9, 5]
print(linear_search(arr_worst, 5))  # Found at last position
```


## 2. Growth Rate Order

$$\log n < n \log n < n^2 < 2^n < n!$$

### Python
```python
import math


n = 10
functions = {
    'log n': math.log2(n),
    'n log n': n * math.log2(n),
    'n^2': n**2,
    '2^n': 2**n,
    'n!': math.factorial(n)
}


for name, value in sorted(functions.items(), key=lambda item: item[1]):
    print(f"{name}: {value}")
```


## 3. Time Estimation

For $$O(n^2)$$: $$\frac{T_2}{T_1} = \frac{n_2^2}{n_1^2}$$

$$\frac{T_2}{1} = \frac{5000^2}{1000^2} = \frac{25000000}{1000000} = 25$$

**Time = 25 seconds**

### Python
```python
# O(n^2) scaling calculation
n1 = 1000
t1 = 1  # seconds
n2 = 5000


t2 = t1 * (n2 / n1) ** 2
print(f"Time for {n2} elements: {t2} seconds")
```


## 4. Time Complexity vs Space Complexity

**Time complexity:** Counting operations
**Space complexity:** Memory usage

Example of tradeoff: Memoization increases space but reduces time

### Python
```python
# Without memoization - O(2^n) time, O(n) space
def fib_slow(n):
    if n <= 1:
        return n
    return fib_slow(n-1) + fib_slow(n-2)


# With memoization - O(n) time, O(n) space
def fib_fast(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_fast(n-1, memo) + fib_fast(n-2, memo)
    return memo[n]


print(fib_fast(30))  # Faster, more memory
```


## 5. Optimization Approaches

**Memoization:** Storing computed results to avoid redundant calculations

**Better data structures:** Using hash tables instead of arrays for lookups


### C++
```cpp
#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <algorithm>


int function_count = 0;


int expensive_computation(int n, std::unordered_map<int, int>& cache) {
    function_count++;
    
    if (cache.find(n) != cache.end()) {
        return cache[n];
    }
    
    int result = (n > 0) ? n * n + expensive_computation(n - 1, cache) : 0;
    cache[n] = result;
    return result;
}


int main() {
    // Slow: O(n) lookup
    std::vector<int> slow_list = {1, 2, 3, 4, 5};
    bool found_in_list = std::find(slow_list.begin(), slow_list.end(), 3) != slow_list.end();
    std::cout << std::boolalpha << found_in_list << std::endl;  // O(n)
    
    // Fast: O(1) lookup
    std::unordered_set<int> fast_set = {1, 2, 3, 4, 5};
    bool found_in_set = fast_set.find(3) != fast_set.end();
    std::cout << std::boolalpha << found_in_set << std::endl;  // O(1)
    
    // Cache and computation
    std::unordered_map<int, int> cache_for_run;
    function_count = 0;
    std::cout << expensive_computation(100, cache_for_run) << std::endl;
    std::cout << "Function called: " << function_count << " times" << std::endl;
    
    return 0;
}


```
