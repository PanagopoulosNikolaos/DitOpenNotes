# Assignment 02: Generic Matrix Arithmetic Class with Operator Overloading

## Objective
Implement an efficient, exception-safe 2D Matrix mathematics class (`Matrix<T>`) in C++, adhering to RAII, the Rule of Five, operator overloading conventions, and mathematical exception safety.

---

## Technical Specifications

### 1. Class Design
```cpp
template <typename T>
class Matrix {
private:
    size_t rows_;
    size_t cols_;
    T* data_; // Contiguous row-major storage

public:
    Matrix(size_t rows, size_t cols, const T& initial_val = T{});
    ~Matrix();
    Matrix(const Matrix& other);
    Matrix(Matrix&& other) noexcept;
    Matrix& operator=(Matrix other) noexcept; // Copy-and-swap
    
    // Element access with bounds checking
    T& at(size_t r, size_t c);
    const T& at(size_t r, size_t c) const;

    // Fast unchecked subscript operator
    T* operator[](size_t r);
    const T* operator[](size_t r) const;

    // Algebraic operators
    Matrix& operator+=(const Matrix& rhs);
    Matrix& operator-=(const Matrix& rhs);
    Matrix& operator*=(const Matrix& rhs);
    
    friend Matrix operator+(Matrix lhs, const Matrix& rhs) { return lhs += rhs; }
    friend Matrix operator-(Matrix lhs, const Matrix& rhs) { return lhs -= rhs; }
    friend Matrix operator*(const Matrix& lhs, const Matrix& rhs);

    friend std::ostream& operator<<(std::ostream& os, const Matrix& mat);
};
```

### 2. Constraints and Edge Cases
1. Out-of-bounds access in `at(r, c)` must throw `std::out_of_range`.
2. Mismatched dimensions in addition/subtraction must throw `std::invalid_argument`.
3. Matrix multiplication requires `lhs.cols() == rhs.rows()`.
4. Must maintain contiguous 1D row-major heap layout for optimal cache locality.

---

## Deliverables
1. `Matrix.hpp`: Complete header-only template class.
2. `matrix_test.cpp`: Automated unit tests verifying Rule of Five correctness, arithmetic operations, and exception throwing.
3. Clean Valgrind log showing zero memory leaks and zero invalid reads/writes.

