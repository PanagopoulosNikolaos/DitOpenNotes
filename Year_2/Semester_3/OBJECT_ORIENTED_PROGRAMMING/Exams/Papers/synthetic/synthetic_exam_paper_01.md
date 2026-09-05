# University of Ioannina - Department of Informatics and Telecommunications
## Course: Object-Oriented Programming (Course Code: 302)
### Academic Year: 2025-2026
### Synthetic Final Examination - Paper 01

**Time Allowed:** 3 Hours  
**Total Marks:** 100 Points  
**Instructions:**
- Answer all questions comprehensively with complete derivations, memory diagrams, and code implementations.
- All C++ code must strictly adhere to the project standards:
  - Classes in `PascalCase`.
  - Member functions and free functions in `camelCase`.
  - Variables and class members in `snake_case`.
  - Explicit Google-style docstrings (`Args:`, `Returns:`, `Raises:`).
  - Single-line comments explaining the rationale ("why").
- Do not use colloquialisms or non-standard syntax.

---

### Question 1: Object-Oriented Paradigms & Language Invariants (20 Marks)

#### Part A: Diamond Inheritance & Virtual Base Classes (8 Marks)
Consider the classic diamond inheritance scenario where class `Device` is inherited by both `Scanner` and `Printer`, which are subsequently inherited by `Copier`:

```cpp
class Device {
public:
    int device_id;
    Device(int id) : device_id(id) {}
};

class Scanner : public Device {
public:
    Scanner(int id) : Device(id) {}
};

class Printer : public Device {
public:
    Printer(int id) : Device(id) {}
};

class Copier : public Scanner, public Printer {
public:
    Copier(int s_id, int p_id) : Scanner(s_id), Printer(p_id) {}
};
```

1. Explain the structural problem and ambiguity that arises when an instance of `Copier` accesses `device_id`.
2. Illustrate how virtual base inheritance (`virtual public Device`) resolves this ambiguity.
3. In virtual base inheritance, which class constructor is directly responsible for initializing `Device`, and what occurs if intermediate constructors attempt to invoke it?

#### Part B: RTTI, Dynamic Casting & Slicing (6 Marks)
1. Contrast `static_cast` and `dynamic_cast` when downcasting pointers along an inheritance hierarchy. What mechanisms does the C++ runtime employ to validate `dynamic_cast`?
2. What are the operational differences when `dynamic_cast` fails on a pointer type versus when it fails on a reference type?
3. Explain why object slicing cannot occur when manipulating objects via pointers or references, but manifests during value assignment.

#### Part C: Const-Correctness & Storage Specifiers (6 Marks)
1. Explain the type signature of the implicit `this` pointer within a `const` member function of class `Sample`.
2. What is the role of the `mutable` keyword in modern C++? Provide a realistic software engineering scenario where `mutable` is necessary to preserve const-correctness.

---

### Question 2: Memory Layout, Multiple Inheritance, and Vtable Mechanics (25 Marks)

Analyze the following polymorphic class hierarchy:

```cpp
class Shape {
public:
    int origin_x;
    int origin_y;
    Shape() : origin_x(0), origin_y(0) {}
    virtual ~Shape() = default;
    virtual double computeArea() const = 0;
    virtual void move(int dx, int dy);
};

class Drawable {
public:
    int render_layer;
    Drawable() : render_layer(1) {}
    virtual ~Drawable() = default;
    virtual void render() const;
    virtual void setZIndex(int z);
};

class RenderableBox : public Shape, public Drawable {
public:
    int width;
    int height;
    RenderableBox(int w, int h) : width(w), height(h) {}
    ~RenderableBox() override = default;
    double computeArea() const override;
    void render() const override;
};
```

#### Part A: Memory Layout Analysis (13 Marks)
Assume a 64-bit Linux architecture with standard ABI rules (8-byte pointer alignment, 4-byte integers, struct padding):
1. Determine the memory layout of an instance of `RenderableBox`. Specify the exact byte offsets, member sizes, and padding bytes from offset `0x00` through the end of the object.
2. What is the total `sizeof(RenderableBox)`?
3. Why are there two separate virtual table pointers (`vptr`) inside `RenderableBox`? Identify their precise locations in memory.

#### Part B: Vtable Construction & Dynamic Dispatch (12 Marks)
1. Draw the detailed Virtual Method Tables (Vtables) for `Shape`, `Drawable`, and `RenderableBox`.
2. Trace the step-by-step execution and pointer arithmetic performed by the compiler for the following instructions:
   ```cpp
   RenderableBox* box_ptr = new RenderableBox(100, 200);
   Drawable* draw_ptr = box_ptr; // Implicit base pointer conversion
   draw_ptr->render();
   delete draw_ptr;
   ```
   Explain the concept of a **thunk** (or `this`-pointer adjustment) during the invocation of `render()` and the virtual destructor through `draw_ptr`.

---

### Question 3: RAII, Modern Move Semantics & Operator Overloading (30 Marks)

Design and implement a robust, production-grade 2D dynamic numeric matrix class named `UniqueMatrix`. The class encapsulates a single contiguous block of heap-allocated memory of type `double*` for optimal cache locality.

```cpp
class UniqueMatrix {
private:
    size_t row_count_;
    size_t col_count_;
    double* matrix_data_;

public:
    // Required implementations
};
```

You must implement the complete class declaration and method definitions adhering to the Rule of Five and RAII idioms:

1. **Default & Parameterized Constructors:**
   - Default constructor initializing a matrix of dimensions $0 \times 0$ with `nullptr`.
   - Parameterized constructor `UniqueMatrix(size_t rows, size_t cols, double initial_val = 0.0)` allocating a contiguous block of `rows * cols` doubles, zero-initialized or filled with `initial_val`. Throws `std::invalid_argument` if rows or cols are 0.
2. **Destructor:**
   - Safely deallocates heap resources and resets pointers.
3. **Copy Semantics:**
   - Deep-copy constructor allocating new heap storage and replicating contents.
   - Copy assignment operator implementing the **Copy-and-Swap** idiom with a `swap` helper function.
4. **Move Semantics (C++11):**
   - Move constructor decorated with `noexcept` that pilfers heap resources and nullifies the source object.
   - Move assignment operator decorated with `noexcept` using resource exchange.
5. **Element Access Operators:**
   - Overload `operator()(size_t row_idx, size_t col_idx)` for both `const` and non-`const` instances with row-major offset calculation (`row_idx * col_count_ + col_idx`) and strict bounds checking throwing `std::out_of_range`.
6. **Arithmetic Operators:**
   - Overload `operator+` for matrix addition (dimensions must match; throws `std::invalid_argument` on mismatch).
   - Overload `operator*` for matrix multiplication ($M \times K$ multiplied by $K \times N$ yielding $M \times N$; throws `std::invalid_argument` on dimension mismatch).

All code must include Google-style docstrings and descriptive inline comments.

---

### Question 4: Smart Pointers, Generic Programming & Design Patterns (25 Marks)

#### Part A: Observer Pattern with Cycle-Safe Smart Pointers (15 Marks)
Cyclic references between subjects and observers lead to severe memory leaks when using `std::shared_ptr`.

1. Design an abstract `MatrixObserver` class with a pure virtual method `void onMatrixModified(const std::string& event_name)`.
2. Design a concrete `ObservableMatrixSubject` class that maintains a collection of registered observers.
3. Explain why the observer list must store `std::weak_ptr<MatrixObserver>` rather than `std::shared_ptr<MatrixObserver>`.
4. Implement `void registerObserver(const std::shared_ptr<MatrixObserver>& observer_ptr)` and `void notifyObservers(const std::string& event_name)`. In `notifyObservers`, explain how `lock()` is used to acquire a temporary `std::shared_ptr`, and how expired observers are cleanly pruned from the container.

#### Part B: Generic Transformation Pipeline (10 Marks)
Implement a generic, templated C++ utility function `transformElements` that applies an arbitrary transformation function or lambda to an input vector and returns a transformed vector:

- Template parameters: Input element type `InputType`, Output element type `OutputType`, and Functor/Callable type `TransformerFunc`.
- Signature:
  ```cpp
  template <typename InputType, typename OutputType, typename TransformerFunc>
  std::vector<OutputType> transformElements(
      const std::vector<InputType>& input_data,
      TransformerFunc transformer
  );
  ```
- Use `std::vector::reserve` to eliminate redundant memory reallocations.
- Provide a brief usage example demonstrating mapping a vector of `UniqueMatrix` instances to a vector of their computed determinants (or Frobenius norms).

