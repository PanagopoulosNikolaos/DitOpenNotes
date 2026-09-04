# Examples: Multi-Paradigm Comparison Walkthrough

This document presents a side-by-side technical comparison of five core programming language paradigms solving the same canonical problem: **filtering even numbers from a list, squaring them, and computing their sum**.

---

## 1. Imperative Paradigm: C

Characteristics: Explicit memory allocation, mutable loop counter state, explicit sequential statement execution.

```c
#include <stdio.h>

int sumEvenSquares(const int *arr, int len) {
    int total = 0;
    for (int i = 0; i < len; i++) {
        if (arr[i] % 2 == 0) {
            total += arr[i] * arr[i];
        }
    }
    return total;
}

int main(void) {
    int data[] = {1, 2, 3, 4, 5, 6};
    int result = sumEvenSquares(data, 6);
    printf("Result (C): %d\n", result); // Output: 4 + 16 + 36 = 56
    return 0;
}
```

---

## 2. Object-Oriented Paradigm: C++ (STL & Lambdas)

Characteristics: Encapsulation, container abstractions (`std::vector`), generic algorithms, and lambda closures.

```cpp
#include <iostream>
#include <vector>
#include <numeric>

class NumberProcessor {
public:
    static int process(const std::vector<int>& numbers) {
        return std::accumulate(numbers.begin(), numbers.end(), 0,
            [](int acc, int val) {
                return (val % 2 == 0) ? acc + (val * val) : acc;
            });
    }
};

int main() {
    std::vector<int> data = {1, 2, 3, 4, 5, 6};
    std::cout << "Result (C++): " << NumberProcessor::process(data) << "\n";
    return 0;
}
```

---

## 3. Functional Paradigm: Haskell

Characteristics: Immutable values, pure functions, point-free function composition, and zero side-effects.

```haskell
-- Point-free functional pipeline:
-- 1. filter even numbers
-- 2. square each number
-- 3. sum the accumulated list
sumEvenSquares :: [Int] -> Int
sumEvenSquares = sum . map (^2) . filter even

main :: IO ()
main = putStrLn ("Result (Haskell): " ++ show (sumEvenSquares [1..6]))
```

---

## 4. Logic Paradigm: Prolog

Characteristics: Declarative Horn clauses, structural recursive list patterns, and unification.

```prolog
% Base case: empty list yields zero sum
sum_even_squares([], 0).

% Recursive case 1: Head is even -> square and add to sum
sum_even_squares([Head | Tail], Sum) :-
    0 is Head mod 2,
    !,
    sum_even_squares(Tail, TailSum),
    Square is Head * Head,
    Sum is Square + TailSum.

% Recursive case 2: Head is odd -> skip
sum_even_squares([_ | Tail], Sum) :-
    sum_even_squares(Tail, Sum).

% Query execution:
% ?- sum_even_squares([1, 2, 3, 4, 5, 6], Result).
% Result = 56.
```

---

## 5. Multi-Paradigm / Dynamic: Python

Characteristics: High-level dynamic typing, first-class list comprehensions or generator expressions.

```python
def sum_even_squares(numbers: list[int]) -> int:
    # Generator expression avoids allocating intermediate lists in memory
    return sum(x * x for x in numbers if x % 2 == 0)

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6]
    print(f"Result (Python): {sum_even_squares(data)}")
```

