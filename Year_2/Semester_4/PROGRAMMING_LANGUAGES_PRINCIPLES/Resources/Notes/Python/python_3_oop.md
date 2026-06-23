# Python — Object-Oriented Programming

*Prerequisite: python_1_basics.md — Functions, scope, and the heap-bound object model.*
*Prerequisite: python_2_intermediate.md — Decorators and first-class functions.*

Python's object-oriented programming (OOP) system provides classes as the primary mechanism for encapsulating state and behavior into reusable abstractions. This file covers class and instance construction, the role of `self`, magic (dunder) methods, inheritance and the Method Resolution Order (MRO), name encapsulation conventions, the `@property` descriptor, static and class methods, and the structural patterns of composition and aggregation.

---

## 1. Classes, Objects, and Instance Attributes

### 1.1 Class Definition

A **class** is a blueprint that describes the state (attributes) and behavior (methods) of a family of objects. An **object** (instance) is a concrete realization of a class.

**Abstract syntax:**

```
class <ClassName>:
    <class_body>
```

By convention, class names use `PascalCase`.

```python
class Point:
    """Represents a two-dimensional Cartesian point."""

    def __init__(self, x, y):
        """Initializes the Point with x and y coordinates.

        Args:
            x (float): The horizontal coordinate.
            y (float): The vertical coordinate.
        """
        self.x = x   # Instance attribute bound to this object.
        self.y = y

p = Point(3.0, 4.0)
print(p.x, p.y)
```

```text
3.0 4.0
```

### 1.2 The Role of `self`

`self` is the first parameter of every instance method. When a method is called on an object `obj.method(arg)`, Python automatically passes `obj` as `self`. It is a reference to the **current object** — the specific instance on which the method was invoked.

`self` is a naming convention, not a keyword. However, deviating from it is strongly discouraged as it breaks all standard tools and conventions.

**Attribute access via `self`:**

```python
class Counter:
    """Maintains an integer count, incrementing on demand."""

    def __init__(self):
        self.count = 0   # Each instance gets its own `count` attribute.

    def increment(self):
        """Increments the counter by one."""
        self.count += 1

    def reset(self):
        """Resets the counter to zero."""
        self.count = 0

c1 = Counter()
c2 = Counter()
c1.increment()
c1.increment()
print(c1.count)   # 2
print(c2.count)   # 0 — c2 is a separate object with its own `count`.
```

```text
2
0
```

### 1.3 Class Attributes vs. Instance Attributes

A **class attribute** is defined in the class body and is shared by all instances. An **instance attribute** is defined via `self` in a method and belongs exclusively to one instance.

```python
class Dog:
    """Models a dog with a species-level and individual-level attribute."""

    species = "Canis lupus familiaris"   # Class attribute; shared by all Dog instances.

    def __init__(self, name, breed):
        self.name = name     # Instance attribute; unique to this Dog.
        self.breed = breed

d1 = Dog("Rex", "Labrador")
d2 = Dog("Bella", "Poodle")

print(Dog.species)    # Accessed through the class.
print(d1.species)     # Accessed through an instance (read from class attribute).
print(d1.name)        # Instance attribute.
print(d2.name)        # Different instance, different value.
```

```text
Canis lupus familiaris
Canis lupus familiaris
Rex
Bella
```

> **[Key Insight]** When an instance attribute and a class attribute share the same name, the instance attribute **shadows** the class attribute for that specific instance only. Assigning `d1.species = "Wolf"` creates a new instance attribute on `d1` and does not modify the class attribute.

---

## 2. Magic (Dunder) Methods

### 2.1 Definition

**Magic methods** (also called **dunder methods** for their double-underscore prefix and suffix) are special methods that Python calls implicitly in response to specific operations or built-in function calls. They integrate user-defined objects into Python's operator and protocol system.

| Dunder Method | Invoked By | Purpose |
| :--- | :--- | :--- |
| `__init__(self, ...)` | `ClassName(...)` | Initializes a new instance |
| `__repr__(self)` | `repr(obj)`, REPL display | Unambiguous string representation |
| `__str__(self)` | `str(obj)`, `print(obj)` | Human-readable string representation |
| `__len__(self)` | `len(obj)` | Returns integer length |
| `__getitem__(self, key)` | `obj[key]` | Index / subscript access |
| `__setitem__(self, key, value)` | `obj[key] = value` | Index assignment |
| `__contains__(self, item)` | `item in obj` | Membership test |
| `__iter__(self)` | `for x in obj`, `iter(obj)` | Returns an iterator |
| `__next__(self)` | `next(obj)` | Yields the next element |
| `__eq__(self, other)` | `obj == other` | Equality comparison |
| `__lt__(self, other)` | `obj < other` | Less-than comparison |
| `__add__(self, other)` | `obj + other` | Addition operator |
| `__call__(self, ...)` | `obj(...)` | Makes an instance callable |

### 2.2 `__repr__` vs. `__str__`

- `__repr__` should return a string that, when passed to `eval()`, ideally recreates the object. It is the developer-facing representation, used in the REPL and in `repr()`.
- `__str__` should return a human-readable description. Used by `print()` and `str()`.
- If only `__repr__` is defined, `str()` falls back to it.

```python
class Vector:
    """Represents a 2D mathematical vector."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x!r}, {self.y!r})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        """Implements vector addition via the + operator."""
        return Vector(self.x + other.x, self.y + other.y)

    def __len__(self):
        """Returns the integer length for compatibility; vectors have 2 components."""
        return 2

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2

print(repr(v1))    # Developer representation.
print(str(v1))     # Human-readable.
print(v3)          # __str__ via print.
print(len(v1))
```

```text
Vector(1, 2)
(1, 2)
(4, 6)
2
```

---

## 3. Inheritance and the Method Resolution Order (MRO)

### 3.1 Single Inheritance

**Inheritance** allows a class (**subclass**) to acquire the attributes and methods of another class (**superclass**), extending or overriding them as needed.

**Syntax:**

```
class SubClass(SuperClass):
    ...
```

```python
class Animal:
    """Base class representing a generic animal."""

    def __init__(self, name):
        self.name = name

    def speak(self):
        """Returns the animal's vocalization (to be overridden)."""
        return "..."

class Dog(Animal):
    """Subclass representing a dog; overrides speak()."""

    def speak(self):
        return f"{self.name} says: Woof!"

class Cat(Animal):
    """Subclass representing a cat; overrides speak()."""

    def speak(self):
        return f"{self.name} says: Meow!"

animals = [Dog("Rex"), Cat("Whiskers"), Dog("Buddy")]
for animal in animals:
    print(animal.speak())
```

```text
Rex says: Woof!
Whiskers says: Meow!
Buddy says: Woof!
```

### 3.2 `super()` — Delegating to the Parent

`super()` returns a proxy object that delegates method calls to the parent class in the MRO. Its primary use is to call the parent's `__init__` when the subclass extends it.

```python
class Employee(Animal):
    """Extends Animal with an employee ID."""

    def __init__(self, name, employee_id):
        super().__init__(name)          # Delegates to Animal.__init__.
        self.employee_id = employee_id  # Additional attribute specific to Employee.

    def speak(self):
        return f"Employee {self.employee_id} ({self.name}) says: Hello."

e = Employee("Alice", "E-001")
print(e.speak())
print(e.name)         # Inherited from Animal.__init__ via super().
print(e.employee_id)
```

```text
Employee E-001 (Alice) says: Hello.
Alice
E-001
```

### 3.3 Multiple Inheritance and the MRO

Python supports **multiple inheritance**: a class may inherit from more than one parent. To resolve ambiguity in method lookup, Python uses the **C3 Linearization** algorithm to produce the **Method Resolution Order (MRO)** — a deterministic, linearized sequence of classes to search.

```
class C(A, B):
    ...
```

The MRO is computed such that:
1. A class always precedes its parents.
2. The order of parents in the class definition is preserved.
3. No class appears before all classes that inherit from it.

```python
class X:
    def hello(self):
        return "X.hello"

class Y:
    def hello(self):
        return "Y.hello"

class Z(X, Y):
    pass

z = Z()
print(z.hello())        # Resolves to X.hello because X precedes Y in MRO.
print(Z.__mro__)        # Displays the full MRO.
```

```text
X.hello
(<class '__main__.Z'>, <class '__main__.X'>, <class '__main__.Y'>, <class 'object'>)
```

> **[Key Insight]** All Python classes implicitly inherit from `object`, which is always the last entry in the MRO. `object` provides default implementations of `__repr__`, `__str__`, `__eq__`, and other fundamental dunder methods.

---

## 4. Encapsulation

### 4.1 Access Control Conventions

Python does not enforce access control at the language level (there are no `private` or `protected` keywords). Instead, it uses naming conventions:

| Convention | Syntax | Meaning |
| :--- | :--- | :--- |
| Public | `attr` | No restriction; freely accessible |
| Protected | `_attr` | By convention, internal use; not enforced by the interpreter |
| Name-mangled | `__attr` | Interpreter rewrites to `_ClassName__attr`; accidental external access is prevented |

### 4.2 Name Mangling

Any identifier with two leading underscores and at most one trailing underscore inside a class body is subject to **name mangling**: the interpreter prepends `_ClassName` to the name.

```python
class BankAccount:
    """Models a bank account with a private balance."""

    def __init__(self, initial_balance):
        self.__balance = initial_balance   # Mangled to _BankAccount__balance.

    def deposit(self, amount):
        """Adds `amount` to the balance."""
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        """Returns the current balance."""
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())       # 1500 — accessed via public method.

# Direct access using the mangled name (possible, but strongly discouraged).
print(account._BankAccount__balance)
```

```text
1500
1500
```

### 4.3 The `@property` Decorator

`@property` converts a method into a **managed attribute** (a descriptor). It exposes a clean attribute-style interface while executing arbitrary logic on access. This is the standard Python alternative to explicit getter/setter methods.

**Three components:**

| Decorator | Role |
| :--- | :--- |
| `@property` | Defines the getter (read access) |
| `@<attr>.setter` | Defines the setter (write access) |
| `@<attr>.deleter` | Defines the deleter (`del obj.attr`) |

```python
class Temperature:
    """Stores temperature in Celsius; exposes a validated Celsius property."""

    def __init__(self, celsius):
        self._celsius = None      # Private storage attribute.
        self.celsius = celsius    # Triggers the setter for validation.

    @property
    def celsius(self):
        """Returns the current temperature in Celsius."""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Sets the temperature, raising ValueError for physically impossible values."""
        if value < -273.15:
            raise ValueError(f"Temperature {value} is below absolute zero.")
        self._celsius = value

    @property
    def fahrenheit(self):
        """Computes and returns the equivalent temperature in Fahrenheit (read-only)."""
        return self._celsius * 9 / 5 + 32

t = Temperature(100)
print(t.celsius)      # 100
print(t.fahrenheit)   # 212.0
t.celsius = 37
print(t.celsius)      # 37
```

```text
100
212.0
37
```

---

## 5. Static and Class Methods

### 5.1 Instance Methods, Class Methods, and Static Methods

| Decorator | First Parameter | Access to | Use Case |
| :--- | :--- | :--- | :--- |
| None (default) | `self` (instance) | Instance attributes and class | Normal instance operations |
| `@classmethod` | `cls` (class itself) | Class attributes only | Alternative constructors, factory methods |
| `@staticmethod` | None | Neither instance nor class implicitly | Utility functions logically grouped with the class |

```python
class Circle:
    """Represents a circle, with factory and utility methods."""

    PI = 3.141592653589793   # Class attribute.

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Computes the area of this circle instance."""
        return Circle.PI * self.radius ** 2

    @classmethod
    def from_diameter(cls, diameter):
        """Alternative constructor; creates a Circle from a diameter value.

        Args:
            diameter (float): The diameter of the circle.

        Returns:
            Circle: A new Circle instance with radius = diameter / 2.
        """
        return cls(diameter / 2)   # cls refers to Circle (or any subclass).

    @staticmethod
    def is_valid_radius(value):
        """Validates that a radius value is positive.

        Args:
            value (float): The candidate radius.

        Returns:
            bool: True if `value` is strictly positive, False otherwise.
        """
        return value > 0

c1 = Circle(5)
c2 = Circle.from_diameter(10)   # Creates Circle with radius 5.

print(c1.area())
print(c2.radius)
print(Circle.is_valid_radius(-3))
```

```text
78.53981633974483
5.0
False
```

---

## 6. Composition and Aggregation

### 6.1 Composition vs. Inheritance

**Inheritance** models an **is-a** relationship: `Dog` is an `Animal`.
**Composition** models a **has-a** relationship: `Car` has an `Engine`.

Composition is often preferred over deep inheritance hierarchies because it produces more modular, testable, and maintainable code.

### 6.2 Composition Example: Engine → Car

```python
class Engine:
    """Represents a combustion engine with a defined horsepower rating."""

    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        """Simulates starting the engine."""
        return f"Engine ({self.horsepower} hp) started."

class Car:
    """Represents a car composed of an Engine and additional attributes."""

    def __init__(self, make, model, horsepower):
        self.make = make
        self.model = model
        self._engine = Engine(horsepower)   # The Car owns its Engine.

    def start(self):
        """Starts the car by delegating to the internal engine."""
        return f"{self.make} {self.model}: {self._engine.start()}"

car = Car("Toyota", "Supra", 340)
print(car.start())
```

```text
Toyota Supra: Engine (340 hp) started.
```

### 6.3 Aggregation Example: Book → Library

**Aggregation** is a weaker form of composition: the contained objects can exist independently of the container.

```python
class Book:
    """Represents a book with a title and price."""

    def __init__(self, title, price):
        self.title = title
        self.price = price

class Library:
    """Aggregates a collection of Book objects."""

    def __init__(self, name):
        self.name = name
        self.books = []   # The Library aggregates existing Book objects.

    def add_book(self, book):
        """Adds a Book to the library's collection.

        Args:
            book (Book): The book to add.
        """
        self.books.append(book)

    def total_value(self):
        """Computes the total price of all books using a generator expression.

        Returns:
            float: The sum of all book prices.
        """
        return sum(book.price for book in self.books)  # Generator expression avoids intermediate list.

    def catalog(self):
        """Returns a formatted string listing all books and their prices.

        Returns:
            str: Newline-separated catalog of book entries.
        """
        return "\n".join(f"  {book.title}: ${book.price:.2f}" for book in self.books)

b1 = Book("Clean Code", 35.00)
b2 = Book("The Pragmatic Programmer", 42.00)
b3 = Book("Design Patterns", 55.00)

lib = Library("Tech Library")
lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)

print(lib.catalog())
print(f"Total value: ${lib.total_value():.2f}")
```

```text
  Clean Code: $35.00
  The Pragmatic Programmer: $42.00
  Design Patterns: $55.00
Total value: $132.00
```

> **[Key Insight]** The expression `sum(book.price for book in self.books)` uses a **generator expression** (parentheses, not square brackets) rather than a list comprehension. It yields each `book.price` one at a time without constructing an intermediate list in memory — important when `self.books` may be very large. `sum()` accepts any iterable, including generators.

---

## Solved Exercises

### Exercise 1: Basic Class Construction

**Problem:** Implement a class `Rectangle` with attributes `width` and `height`, methods `area()` and `perimeter()`, and a `__repr__` method.

**Solution:**

```python
class Rectangle:
    """Represents an axis-aligned rectangle defined by width and height."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Computes the rectangle's area.

        Returns:
            float: Product of width and height.
        """
        return self.width * self.height

    def perimeter(self):
        """Computes the rectangle's perimeter.

        Returns:
            float: Twice the sum of width and height.
        """
        return 2 * (self.width + self.height)

    def __repr__(self):
        return f"Rectangle(width={self.width!r}, height={self.height!r})"

r = Rectangle(4, 7)
print(repr(r))
print(r.area())
print(r.perimeter())
```

```text
Rectangle(width=4, height=7)
28
22
```

---

### Exercise 2: Class Attributes and Instance Shadowing

**Problem:** Predict the output of the following code.

```python
class Config:
    debug = False
    timeout = 30

c1 = Config()
c2 = Config()

c1.debug = True    # Creates an instance attribute on c1; does NOT modify the class attribute.

print(Config.debug)
print(c1.debug)
print(c2.debug)
```

**Solution:**

```text
False
True
False
```

`c1.debug = True` creates a new instance attribute `debug` on `c1`. The class attribute `Config.debug` remains `False`. `c2.debug` reads the class attribute (there is no instance attribute on `c2`), so it returns `False`.

---

### Exercise 3: `__eq__` and `__lt__` for Custom Comparison

**Problem:** Implement a class `Student` with attributes `name` and `gpa`. Implement `__eq__` (equality by `name` and `gpa`) and `__lt__` (ordering by `gpa`). Then sort a list of students.

**Solution:**

```python
class Student:
    """Represents a student; supports equality and ordering by GPA."""

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __repr__(self):
        return f"Student({self.name!r}, gpa={self.gpa})"

    def __eq__(self, other):
        """Compares students by both name and GPA."""
        if not isinstance(other, Student):
            return NotImplemented
        return self.name == other.name and self.gpa == other.gpa

    def __lt__(self, other):
        """Orders students by GPA in ascending order."""
        return self.gpa < other.gpa

students = [Student("Alice", 3.7), Student("Bob", 3.2), Student("Carol", 3.9)]
students.sort()   # Uses __lt__ via Timsort.
print(students)
```

```text
[Student('Bob', gpa=3.2), Student('Alice', gpa=3.7), Student('Carol', gpa=3.9)]
```

---

### Exercise 4: Inheritance and Method Override

**Problem:** Create a class hierarchy: `Shape` (base) → `Circle` and `Square` (subclasses). `Shape` has an abstract `area()` method. Demonstrate polymorphic dispatch.

**Solution:**

```python
class Shape:
    """Base class for geometric shapes; subclasses must implement area()."""

    def area(self):
        """Returns the area of the shape (override in subclasses)."""
        raise NotImplementedError(f"{type(self).__name__} must implement area()")

class Circle(Shape):
    """A circle defined by its radius."""

    PI = 3.141592653589793

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.PI * self.radius ** 2

class Square(Shape):
    """A square defined by its side length."""

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

shapes = [Circle(5), Square(4), Circle(3), Square(7)]
for shape in shapes:
    print(f"{type(shape).__name__}: area = {shape.area():.4f}")
```

```text
Circle: area = 78.5398
Square: area = 16.0000
Circle: area = 28.2743
Square: area = 49.0000
```

---

### Exercise 5: `super()` in Multiple Inheritance

**Problem:** Trace the call to `super().__init__()` through the following MRO and predict the output.

```python
class A:
    def __init__(self):
        print("A.__init__")
        super().__init__()

class B(A):
    def __init__(self):
        print("B.__init__")
        super().__init__()

class C(A):
    def __init__(self):
        print("C.__init__")
        super().__init__()

class D(B, C):
    def __init__(self):
        print("D.__init__")
        super().__init__()

d = D()
print(D.__mro__)
```

**Solution:**

The MRO of `D` is `[D, B, C, A, object]`. Each `super().__init__()` call follows this linear chain:

```text
D.__init__
B.__init__
C.__init__
A.__init__
(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
```

`super()` in `B.__init__` does not call `A.__init__` directly — it calls the next class in `D`'s MRO, which is `C`. This is the cooperative multiple inheritance mechanism that prevents `A.__init__` from being called twice.

---

### Exercise 6: `@property` with Validation

**Problem:** Implement a class `PositiveCounter` whose `value` property only accepts positive integers, raising `ValueError` otherwise.

**Solution:**

```python
class PositiveCounter:
    """A counter that enforces a strictly positive integer value."""

    def __init__(self, initial):
        self.value = initial   # Uses the setter for validation.

    @property
    def value(self):
        """Returns the current counter value."""
        return self._value

    @value.setter
    def value(self, v):
        """Sets the counter value, raising ValueError if v is not a positive integer."""
        if not isinstance(v, int) or v <= 0:
            raise ValueError(f"Value must be a positive integer, got {v!r}.")
        self._value = v

c = PositiveCounter(10)
print(c.value)
c.value = 5
print(c.value)

try:
    c.value = -3
except ValueError as e:
    print(e)
```

```text
10
5
Value must be a positive integer, got -3.
```

---

### Exercise 7: Composition — Stack Using a List

**Problem:** Implement a `Stack` class using composition (an internal `list`) rather than inheriting from `list`. Implement `push()`, `pop()`, `peek()`, `is_empty()`, and `__len__`.

**Solution:**

```python
class Stack:
    """A LIFO data structure implemented via composition with a Python list."""

    def __init__(self):
        self._data = []   # Internal list; not exposed directly.

    def push(self, item):
        """Pushes an item onto the top of the stack.

        Args:
            item: The item to push.
        """
        self._data.append(item)

    def pop(self):
        """Removes and returns the top item.

        Returns:
            The top item.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self):
        """Returns the top item without removing it.

        Returns:
            The top item.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("peek at empty stack")
        return self._data[-1]

    def is_empty(self):
        """Returns True if the stack contains no elements."""
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f"Stack({self._data!r})"

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s)
print(s.peek())
print(s.pop())
print(len(s))
```

```text
Stack([1, 2, 3])
3
3
2
```

---

### Exercise 8: Aggregation with Generator Expressions

**Problem:** Extend the `Library` / `Book` model. Given a list of books, compute: the total value, the average price, the most expensive book, and a list of all books priced above $40.

**Solution:**

```python
class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price
    def __repr__(self):
        return f"Book({self.title!r}, ${self.price:.2f})"

class Library:
    def __init__(self, books):
        self.books = books   # Aggregates independently existing Book objects.

    def total_value(self):
        return sum(b.price for b in self.books)

    def average_price(self):
        return self.total_value() / len(self.books)

    def most_expensive(self):
        return max(self.books, key=lambda b: b.price)

    def books_above(self, threshold):
        return [b for b in self.books if b.price > threshold]

catalog = [
    Book("SICP", 55.00),
    Book("CLRS", 75.00),
    Book("Python Cookbook", 38.00),
    Book("Fluent Python", 48.00),
    Book("Learning Python", 30.00),
]
lib = Library(catalog)

print(f"Total: ${lib.total_value():.2f}")
print(f"Average: ${lib.average_price():.2f}")
print(f"Most expensive: {lib.most_expensive()}")
print(f"Above $40: {lib.books_above(40)}")
```

```text
Total: $246.00
Average: $49.20
Most expensive: Book('CLRS', $75.00)
Above $40: [Book('SICP', $55.00), Book('CLRS', $75.00), Book('Fluent Python', $48.00)]
```

---

## Exam Tip: MRO, `super()`, and Name Mangling

**MRO exam pattern:** Given a class hierarchy with multiple inheritance, to determine method resolution order, apply the C3 linearization rule: start from the most derived class, and always prefer the leftmost parent. `ClassName.__mro__` displays the full sequence.

**`super()` in single inheritance:** `super().__init__(args)` must be called explicitly in the subclass `__init__` if the parent `__init__` sets attributes that the subclass depends on. Forgetting this call is the most common inheritance bug.

**Name mangling disambiguation:** `__attr` (two leading underscores, at most one trailing) is mangled. `__attr__` (two leading and two trailing underscores — dunder) is **not** mangled; it is a magic method slot. The difference is the trailing underscores.

**`@property` vs. direct attribute:** Defining `@property` does not prevent direct access to the underlying storage attribute (e.g., `self._celsius`). The convention of a single leading underscore signals that direct access is discouraged, but the interpreter does not enforce it.
