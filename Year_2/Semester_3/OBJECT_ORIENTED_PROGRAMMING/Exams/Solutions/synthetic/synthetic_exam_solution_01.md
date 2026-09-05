# University of Ioannina - Department of Informatics and Telecommunications
## Course: Object-Oriented Programming (Course Code: 302)
### Academic Year: 2025-2026
### Synthetic Final Examination Solutions - Paper 01

---

### Solution 1: Object-Oriented Paradigms & Language Invariants (20 Marks)

#### Part A: Diamond Inheritance & Virtual Base Classes (8 Marks)

1. **Structural Problem & Ambiguity:**
   Under non-virtual multiple inheritance, class `Copier` inherits two distinct copies of class `Device`: one via `Scanner` and another via `Printer`.
   When client code executes `copier.device_id`, the compiler encounters an ambiguity error:
   ```
   error: request for member 'device_id' is ambiguous
   ```
   The compiler cannot determine whether to resolve the path through `Scanner::device_id` or `Printer::device_id`. Furthermore, holding duplicate base subobjects wastes memory and risks data inconsistency if one subobject's state is modified while the other remains unchanged.

2. **Resolution via Virtual Base Inheritance:**
   By declaring `Device` as a virtual base class in both intermediate classes:
   ```cpp
   class Scanner : virtual public Device { /* ... */ };
   class Printer : virtual public Device { /* ... */ };
   ```
   The compiler alters the object layout such that `Scanner` and `Printer` store offset pointers (or virtual base table pointers, `vbtptr`) to a single, shared `Device` subobject located at the tail of the most-derived object `Copier`. Ambiguity is eliminated because only one instance of `device_id` exists.

3. **Constructor Responsibility in Virtual Inheritance:**
   In virtual inheritance, the **most-derived class** (`Copier`) is directly responsible for invoking the virtual base constructor:
   ```cpp
   Copier(int id, int s_val, int p_val) 
       : Device(id), Scanner(s_val), Printer(p_val) {}
   ```
   If intermediate classes (`Scanner` and `Printer`) call `Device(id)` in their member initializer lists, the compiler silently ignores those calls during the construction of `Copier`. Those intermediate calls only execute when `Scanner` or `Printer` are instantiated directly as standalone objects.

---

#### Part B: RTTI, Dynamic Casting & Slicing (6 Marks)

1. **`static_cast` vs `dynamic_cast` Downcasting:**
   - `static_cast` performs downcasting strictly at compile time based solely on type definitions without runtime verification. If the underlying object is not an instance of the target type, it executes unchecked pointer arithmetic leading to undefined behavior.
   - `dynamic_cast` queries Runtime Type Information (RTTI). It accesses the `std::type_info` structure pointed to by the virtual table (at offset `-1` relative to the vptr) to verify the inheritance path at runtime. It requires the polymorphic class to have at least one virtual function.

2. **Failure Semantics (Pointer vs Reference):**
   - **Pointer Downcasting:** If `dynamic_cast<Target*>(ptr)` fails, it safely evaluates to `nullptr`. Code can test this via `if (target_ptr != nullptr)`.
   - **Reference Downcasting:** References cannot be bound to null. Therefore, if `dynamic_cast<Target&>(ref)` fails, the runtime throws a `std::bad_cast` exception.

3. **Prevention of Object Slicing:**
   - Slicing occurs when an object of a derived class is copied into a base class variable **by value** (`Base b = derived_obj;`). The copy constructor of `Base` only copies the base subobject attributes and sets the `vptr` to `Base::vtable`, completely discarding derived attributes and virtual behavior.
   - When passing by pointer (`Base*`) or reference (`Base&`), no memory copy occurs. The pointer/reference points directly to the underlying object in memory, preserving the original `vptr` and the complete polymorphic type.

---

#### Part C: Const-Correctness & Storage Specifiers (6 Marks)

1. **Type Signature of `this` in Const Member Functions:**
   In a normal member function of `class Sample`, the implicit pointer has type `Sample* const` (a constant pointer to a mutable object).  
   In a `const` member function:
   ```cpp
   void Sample::inspect() const;
   ```
   The implicit `this` pointer has type `const Sample* const` (a constant pointer to a constant object). Consequently, any attempt to modify member variables through `this` generates a compiler error.

2. **The `mutable` Keyword:**
   The `mutable` specifier exempts a class member variable from the bitwise-constness enforced by `const` member functions, permitting logical constness.  
   **Realistic Scenario:** In multithreaded design or performance caching:
   - A thread-safe `Matrix::get(size_t r, size_t c) const` method must acquire a mutex before reading. A `mutable std::mutex mutex_` allows locking within a `const` member function.
   - A `mutable double cached_determinant_` and `mutable bool is_cache_valid_` allow lazy evaluation and memoization inside a `double Matrix::computeDeterminant() const` function without violating the outward `const` contract of the API.

---

### Solution 2: Memory Layout, Multiple Inheritance, and Vtable Mechanics (25 Marks)

#### Part A: Memory Layout Analysis (13 Marks)

Given classes:
- `Shape`: `vptr_Shape` (8 bytes), `int origin_x` (4 bytes), `int origin_y` (4 bytes). Total = 16 bytes.
- `Drawable`: `vptr_Drawable` (8 bytes), `int render_layer` (4 bytes). Padding = 4 bytes. Total = 16 bytes.
- `RenderableBox`: inherits `Shape`, `Drawable`, adds `int width` (4 bytes), `int height` (4 bytes).

**Memory Offset Table for `RenderableBox` (64-bit System):**

| Offset (Hex) | Offset (Dec) | Size (Bytes) | Field / Component | Description |
|:-------------|:-------------|:-------------|:------------------|:------------|
| `0x00 - 0x07`| `0 - 7`      | 8            | `vptr_Shape`      | Primary vptr pointing to `RenderableBox` primary vtable |
| `0x08 - 0x0B`| `8 - 11`     | 4            | `Shape::origin_x` | Inherited from base `Shape` |
| `0x0C - 0x0F`| `12 - 15`    | 4            | `Shape::origin_y` | Inherited from base `Shape` |
| `0x10 - 0x17`| `16 - 23`    | 8            | `vptr_Drawable`   | Secondary vptr pointing to `Drawable` vtable in `RenderableBox` |
| `0x18 - 0x1B`| `24 - 27`    | 4            | `Drawable::render_layer` | Inherited from base `Drawable` |
| `0x1C - 0x1F`| `28 - 31`    | 4            | *(Padding)*       | Alignment padding to align next block to 8-byte boundary |
| `0x20 - 0x23`| `32 - 35`    | 4            | `RenderableBox::width`  | Derived class member |
| `0x24 - 0x27`| `36 - 39`    | 4            | `RenderableBox::height` | Derived class member |

- **Total `sizeof(RenderableBox)`:** $40 \text{ bytes}$ (`0x28`).
- **Presence of Two Vptrs:** Because `RenderableBox` uses multiple inheritance from two independent polymorphic classes (`Shape` and `Drawable`), it must support conversion to both `Shape*` (offset `+0`) and `Drawable*` (offset `+16`). Each base subobject must possess its own `vptr` so that calls through either base pointer correctly locate the appropriate virtual function pointers.

---

#### Part B: Vtable Construction & Dynamic Dispatch (12 Marks)

1. **Virtual Method Tables:**

**Primary Vtable for `RenderableBox` (associated with `vptr_Shape` at offset `0x00`):**
```
Offset -16: [RTTI Complete Object Locator / std::type_info for RenderableBox]
Offset  -8: [Offset to top = 0]
Index    0: &RenderableBox::~RenderableBox()
Index    1: &RenderableBox::computeArea()
Index    2: &Shape::move(int, int)
Index    3: &RenderableBox::render()  // Placed in primary table for complete object calls
```

**Secondary Vtable for `RenderableBox` (associated with `vptr_Drawable` at offset `0x10`):**
```
Offset -16: [RTTI Complete Object Locator for RenderableBox]
Offset  -8: [Offset to top = -16]
Index    0: &non-virtual thunk to RenderableBox::~RenderableBox()
Index    1: &non-virtual thunk to RenderableBox::render()
Index    2: &Drawable::setZIndex(int)
```

2. **Dynamic Dispatch & Thunk Trace:**

```cpp
RenderableBox* box_ptr = new RenderableBox(100, 200);
Drawable* draw_ptr = box_ptr;
draw_ptr->render();
delete draw_ptr;
```

- **Step 1: Pointer Conversion (`draw_ptr = box_ptr`):**  
  The compiler performs pointer adjustment:
  $$\text{draw\_ptr} = \text{reinterpret\_cast}<\text{Drawable*}>(\text{reinterpret\_cast}<\text{char*}>(\text{box\_ptr}) + 16)$$
  `draw_ptr` now points directly to the `Drawable` subobject at offset `0x10`.

- **Step 2: Method Invocation (`draw_ptr->render()`):**  
  1. Dereference `draw_ptr` to obtain `vptr_Drawable` at offset `0x10`.
  2. Access index 1 of the secondary vtable.
  3. The target address is the **thunk** function: `non-virtual thunk to RenderableBox::render()`.
  4. The thunk adjusts the `this` pointer back to the start of `RenderableBox`:
     $$\text{this} = \text{this} - 16$$
  5. The thunk jumps directly to `RenderableBox::render()`, which executes with the proper complete object `this` pointer.

- **Step 3: Polymorphic Deletion (`delete draw_ptr`):**  
  1. Calls the virtual destructor through `vptr_Drawable` at index 0.
  2. The deleting destructor thunk adjusts the `this` pointer by subtracting 16 bytes.
  3. It executes `RenderableBox::~RenderableBox()`.
  4. It invokes `::operator delete(ptr, 40)` on the adjusted base pointer (`0x00`), deallocating the full 40-byte block. Without the virtual destructor and thunk, deleting through `draw_ptr` would pass an interior pointer (`+16`) to `free()`, causing catastrophic heap corruption.

---

### Solution 3: RAII, Modern Move Semantics & Operator Overloading (30 Marks)

```cpp
#include <iostream>
#include <stdexcept>
#include <utility>
#include <algorithm>

/**
 * A contiguous heap-allocated 2D dynamic numeric matrix implementing RAII
 * and the complete Rule of Five.
 */
class UniqueMatrix {
private:
    size_t row_count_;
    size_t col_count_;
    double* matrix_data_;

    /**
     * Allocates a contiguous heap buffer for matrix elements.
     *
     * Args:
     *     rows (size_t): The row dimension.
     *     cols (size_t): The column dimension.
     *
     * Returns:
     *     double*: Pointer to the allocated heap buffer.
     */
    static double* allocateBuffer(size_t rows, size_t cols) {
        return new double[rows * cols](); // Allocates and zero-initializes contiguous memory
    }

    /**
     * Deallocates the internal heap buffer safely.
     */
    void deallocateBuffer() noexcept {
        delete[] matrix_data_;            // Releases contiguous heap array
        matrix_data_ = nullptr;           // Prevents dangling pointer reference
    }

public:
    /**
     * Constructs an empty 0x0 matrix.
     */
    UniqueMatrix() noexcept
        : row_count_(0), col_count_(0), matrix_data_(nullptr) {}

    /**
     * Parameterized constructor allocating and initializing matrix storage.
     *
     * Args:
     *     rows (size_t): Number of rows.
     *     cols (size_t): Number of columns.
     *     initial_val (double): Initial value for all matrix cells.
     *
     * Raises:
     *     std::invalid_argument: If rows or cols are zero.
     */
    UniqueMatrix(size_t rows, size_t cols, double initial_val = 0.0)
        : row_count_(rows), col_count_(cols), matrix_data_(nullptr) {
        if (rows == 0 || cols == 0) {
            throw std::invalid_argument("Matrix dimensions must be strictly positive.");
        }
        matrix_data_ = allocateBuffer(row_count_, col_count_); // Allocates heap storage
        std::fill(matrix_data_, matrix_data_ + (row_count_ * col_count_), initial_val); // Initializes elements
    }

    /**
     * Destructor ensuring proper RAII deallocation.
     */
    ~UniqueMatrix() noexcept {
        deallocateBuffer(); // Frees dynamically allocated heap block
    }

    /**
     * Deep-copy constructor replicating resources from another matrix.
     *
     * Args:
     *     other (const UniqueMatrix&): The source matrix to copy.
     */
    UniqueMatrix(const UniqueMatrix& other)
        : row_count_(other.row_count_), col_count_(other.col_count_), matrix_data_(nullptr) {
        if (other.matrix_data_ != nullptr) {
            matrix_data_ = allocateBuffer(row_count_, col_count_); // Allocates distinct heap block
            std::copy(other.matrix_data_, 
                      other.matrix_data_ + (row_count_ * col_count_), 
                      matrix_data_);                               // Performs deep copy of elements
        }
    }

    /**
     * Swaps the member states of two matrix instances.
     *
     * Args:
     *     first (UniqueMatrix&): First matrix reference.
     *     second (UniqueMatrix&): Second matrix reference.
     */
    friend void swap(UniqueMatrix& first, UniqueMatrix& second) noexcept {
        using std::swap;
        swap(first.row_count_, second.row_count_);     // Exchanges row counts
        swap(first.col_count_, second.col_count_);     // Exchanges column counts
        swap(first.matrix_data_, second.matrix_data_); // Exchanges heap buffer pointers
    }

    /**
     * Copy assignment operator using the copy-and-swap idiom.
     *
     * Args:
     *     other (UniqueMatrix): Temporary copy received by value.
     *
     * Returns:
     *     UniqueMatrix&: Reference to this assigned instance.
     */
    UniqueMatrix& operator=(UniqueMatrix other) noexcept {
        swap(*this, other); // Swaps contents with value copy, ensuring strong exception safety
        return *this;
    }

    /**
     * Move constructor transferring ownership of heap buffer.
     *
     * Args:
     *     other (UniqueMatrix&&): Rvalue reference to source matrix.
     */
    UniqueMatrix(UniqueMatrix&& other) noexcept
        : row_count_(other.row_count_), 
          col_count_(other.col_count_), 
          matrix_data_(other.matrix_data_) {
        other.row_count_ = 0;          // Resets source row count
        other.col_count_ = 0;          // Resets source column count
        other.matrix_data_ = nullptr;  // Nullifies source pointer to prevent double free
    }

    /**
     * Element access operator with boundary verification.
     *
     * Args:
     *     row_idx (size_t): Zero-based row coordinate.
     *     col_idx (size_t): Zero-based column coordinate.
     *
     * Returns:
     *     double&: Reference to target element.
     *
     * Raises:
     *     std::out_of_range: If coordinates exceed matrix bounds.
     */
    double& operator()(size_t row_idx, size_t col_idx) {
        if (row_idx >= row_count_ || col_idx >= col_count_) {
            throw std::out_of_range("Matrix subscript index out of range.");
        }
        return matrix_data_[row_idx * col_count_ + col_idx]; // Computes row-major offset
    }

    /**
     * Const element access operator with boundary verification.
     *
     * Args:
     *     row_idx (size_t): Zero-based row coordinate.
     *     col_idx (size_t): Zero-based column coordinate.
     *
     * Returns:
     *     const double&: Const reference to target element.
     *
     * Raises:
     *     std::out_of_range: If coordinates exceed matrix bounds.
     */
    const double& operator()(size_t row_idx, size_t col_idx) const {
        if (row_idx >= row_count_ || col_idx >= col_count_) {
            throw std::out_of_range("Matrix subscript index out of range.");
        }
        return matrix_data_[row_idx * col_count_ + col_idx]; // Computes row-major offset
    }

    /**
     * Matrix addition operator.
     *
     * Args:
     *     rhs (const UniqueMatrix&): Right-hand operand matrix.
     *
     * Returns:
     *     UniqueMatrix: Resulting sum matrix.
     *
     * Raises:
     *     std::invalid_argument: If matrix dimensions do not match.
     */
    UniqueMatrix operator+(const UniqueMatrix& rhs) const {
        if (row_count_ != rhs.row_count_ || col_count_ != rhs.col_count_) {
            throw std::invalid_argument("Dimension mismatch for matrix addition.");
        }
        UniqueMatrix result_matrix(row_count_, col_count_); // Allocates result matrix
        size_t total_elements = row_count_ * col_count_;
        for (size_t i = 0; i < total_elements; ++i) {
            result_matrix.matrix_data_[i] = matrix_data_[i] + rhs.matrix_data_[i]; // Performs cell addition
        }
        return result_matrix;
    }

    /**
     * Matrix multiplication operator.
     *
     * Args:
     *     rhs (const UniqueMatrix&): Right-hand operand matrix.
     *
     * Returns:
     *     UniqueMatrix: Resulting product matrix.
     *
     * Raises:
     *     std::invalid_argument: If inner dimensions do not match.
     */
    UniqueMatrix operator*(const UniqueMatrix& rhs) const {
        if (col_count_ != rhs.row_count_) {
            throw std::invalid_argument("Inner dimensions must match for multiplication.");
        }
        UniqueMatrix product_matrix(row_count_, rhs.col_count_, 0.0); // Allocates M x N result matrix
        for (size_t i = 0; i < row_count_; ++i) {
            for (size_t k = 0; k < col_count_; ++k) {
                double temp_a = (*this)(i, k); // Caches row value to optimize memory access
                for (size_t j = 0; j < rhs.col_count_; ++j) {
                    product_matrix(i, j) += temp_a * rhs(k, j); // Accumulates dot product
                }
            }
        }
        return product_matrix;
    }

    size_t getRows() const noexcept { return row_count_; }
    size_t getCols() const noexcept { return col_count_; }
};
```

---

### Solution 4: Smart Pointers, Generic Programming & Design Patterns (25 Marks)

#### Part A: Observer Pattern with Weak Pointers (15 Marks)

```cpp
#include <iostream>
#include <vector>
#include <memory>
#include <string>
#include <algorithm>

/**
 * Abstract observer interface for matrix lifecycle events.
 */
class MatrixObserver {
public:
    virtual ~MatrixObserver() = default;

    /**
     * Callback dispatched upon matrix modification.
     *
     * Args:
     *     event_name (const std::string&): Identifier of the dispatched event.
     */
    virtual void onMatrixModified(const std::string& event_name) = 0;
};

/**
 * Concrete subject managing observers without inducing cyclic ownership.
 */
class ObservableMatrixSubject {
private:
    std::vector<std::weak_ptr<MatrixObserver>> observers_list_;

public:
    /**
     * Registers a new observer reference.
     *
     * Args:
     *     observer_ptr (const std::shared_ptr<MatrixObserver>&): Observer instance to watch.
     */
    void registerObserver(const std::shared_ptr<MatrixObserver>& observer_ptr) {
        observers_list_.push_back(observer_ptr); // Stores weak_ptr to prevent cycle retain count
    }

    /**
     * Dispatches notifications to all active observers and prunes expired references.
     *
     * Args:
     *     event_name (const std::string&): The event description to propagate.
     */
    void notifyObservers(const std::string& event_name) {
        // Erase-remove idiom combined with weak_ptr lock checking
        auto it = observers_list_.begin();
        while (it != observers_list_.end()) {
            if (std::shared_ptr<MatrixObserver> active_obs = it->lock()) {
                active_obs->onMatrixModified(event_name); // Safely invokes callback on living instance
                ++it;
            } else {
                it = observers_list_.erase(it);           // Prunes expired observer to avoid leaks
            }
        }
    }
};
```

**Architectural Rationale for `std::weak_ptr`:**
- If the subject stored `std::shared_ptr<MatrixObserver>`, and observers stored a `std::shared_ptr<ObservableMatrixSubject>`, a strong circular reference would form. The reference count of both objects would never reach zero, creating an uncollectable memory leak.
- `std::weak_ptr` does not increment the strong reference count of the target object.
- By calling `it->lock()`, the subject attempts to create a temporary `std::shared_ptr`. If the observer is still alive, `lock()` succeeds, guaranteeing thread-safe execution during the callback. If the observer has been destroyed elsewhere, `lock()` returns `nullptr`, allowing the subject to prune the dead reference.

---

#### Part B: Generic Transformation Pipeline (10 Marks)

```cpp
#include <vector>
#include <functional>
#include <cmath>

/**
 * Transforms an input vector into an output vector by applying a unary callable.
 *
 * Args:
 *     input_data (const std::vector<InputType>&): Vector of source elements.
 *     transformer (TransformerFunc): Unary callable mapping InputType to OutputType.
 *
 * Returns:
 *     std::vector<OutputType>: Vector containing transformed elements.
 */
template <typename InputType, typename OutputType, typename TransformerFunc>
std::vector<OutputType> transformElements(
    const std::vector<InputType>& input_data,
    TransformerFunc transformer
) {
    std::vector<OutputType> result_vector;
    result_vector.reserve(input_data.size()); // Preallocates memory to prevent dynamic reallocations

    for (const auto& item : input_data) {
        result_vector.push_back(transformer(item)); // Appends transformed element
    }
    return result_vector;
}

/**
 * Helper calculating the Frobenius norm of a matrix.
 *
 * Args:
 *     mat (const UniqueMatrix&): Matrix to evaluate.
 *
 * Returns:
 *     double: The computed Frobenius norm.
 */
double computeFrobeniusNorm(const UniqueMatrix& mat) {
    double sum_squares = 0.0;
    for (size_t r = 0; r < mat.getRows(); ++r) {
        for (size_t c = 0; c < mat.getCols(); ++c) {
            double val = mat(r, c);
            sum_squares += val * val; // Sums squared matrix entries
        }
    }
    return std::sqrt(sum_squares);
}

// Usage Example
void exampleUsage() {
    std::vector<UniqueMatrix> matrix_list;
    matrix_list.emplace_back(2, 2, 3.0);
    matrix_list.emplace_back(3, 3, 2.0);

    // Transforms matrix list into a vector of Frobenius norm values
    std::vector<double> norm_values = transformElements<UniqueMatrix, double>(
        matrix_list,
        [](const UniqueMatrix& m) { return computeFrobeniusNorm(m); }
    );
}
```

