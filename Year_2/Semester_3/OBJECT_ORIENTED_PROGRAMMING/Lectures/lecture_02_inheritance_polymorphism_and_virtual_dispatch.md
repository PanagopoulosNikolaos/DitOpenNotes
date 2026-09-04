# Lecture 02: Inheritance, Polymorphism, and Virtual Dispatch

This lecture examines object-oriented hierarchies, public inheritance, runtime polymorphism via virtual functions, the internal mechanics of Virtual Method Tables (vtables), and abstract base classes.

---

## 1. Inheritance and the "Is-A" Relationship

Inheritance models an "Is-A" taxonomy where a derived class inherits members from a base class.

```cpp
class Shape {
protected:
    double x_;
    double y_;

public:
    Shape(double x, double y) : x_(x), y_(y) {}
    virtual ~Shape() = default; // Mandatory virtual destructor in base class
};

class Circle : public Shape {
private:
    double radius_;

public:
    Circle(double x, double y, double radius)
        : Shape(x, y), radius_(radius) {}
};
```

### Public vs. Private Inheritance
- **Public (`class B : public A`):** Models subtyping ("B is an A"). Public base members remain public; protected members remain protected.
- **Private (`class B : private A`):** Models implementation reuse ("B is implemented in terms of A"). Composition is strongly preferred over private inheritance.

---

## 2. Polymorphism and Dynamic Dispatch

Polymorphism allows code written to a base class interface to invoke methods specialized in derived classes.

### 2.1 Static vs. Dynamic Binding
- **Static Binding (Compile-Time):** Function call is bound at compile time based on the static pointer/reference type (default for non-virtual functions).
- **Dynamic Binding (Runtime):** Function call is resolved at runtime based on the actual dynamic type of the object pointed to. Enabled via the `virtual` keyword.

---

## 3. The Virtual Method Table (Vtable) Mechanism

When a class defines or inherits a `virtual` function, the compiler inserts a hidden pointer called the **vptr** into each object instance.

```
Object Instance in Memory:              Virtual Table (vtable) in Read-Only Data:
+------------------------+              +-------------------------------------+
| vptr                   | -----------> | &Circle::computeArea()              |
+------------------------+              +-------------------------------------+
| Shape::x_              |              | &Circle::render()                   |
+------------------------+              +-------------------------------------+
| Shape::y_              |              | &Circle::~Circle() [Destructor]     |
+------------------------+              +-------------------------------------+
| Circle::radius_        |
+------------------------+
```

### 3.1 Step-by-Step Dynamic Dispatch Sequence
1. The program executes `shape_ptr->computeArea()`.
2. The runtime retrieves `shape_ptr->vptr`.
3. It indexes the vtable at the fixed slot offset for `computeArea()`.
4. It calls the function pointer found at that offset, executing `Circle::computeArea()`.

---

## 4. Abstract Classes and Pure Virtual Functions

A function declared with `= 0` is a **pure virtual function**:
```cpp
class Shape {
public:
    virtual ~Shape() = default;
    [[nodiscard]] virtual double computeArea() const = 0; // Pure virtual
};
```
- A class containing at least one pure virtual function is an **Abstract Base Class**.
- Abstract classes cannot be instantiated directly; they define pure interface contracts.
- Any concrete derived class must provide an override for all pure virtual methods.

---

## 5. Critical Pitfall: Virtual Destructors and Object Slicing

### 5.1 Why Base Destructors Must Be Virtual
If an object of a derived class is deleted through a base-class pointer without a virtual destructor:
```cpp
Shape* s = new Circle(0, 0, 5.0);
delete s; // Undefined Behavior if ~Shape() is not virtual!
```
Only `~Shape()` would execute, leaking all dynamic memory and resources held by `Circle`. Declaring `virtual ~Shape() = default;` ensures the derived destructor executes before the base destructor.

### 5.2 Object Slicing
Assigning a derived object to a base object by value copies only the base slice of the object, truncating derived members and stripping polymorphic behavior:
```cpp
Circle c(0, 0, 5.0);
Shape s = c; // SLICED! s has no radius_ and vptr points to Shape's vtable.
```
*Rule:* Always pass polymorphic objects by pointer (`Shape*`) or by reference (`const Shape&`).

