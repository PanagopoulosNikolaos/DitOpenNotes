# Tutorial 01: Implementing Custom Generic Collections in C++

This tutorial provides a step-by-step implementation guide for constructing generic, memory-safe data structures in modern C++, specifically focusing on a templated dynamic array (`Vector<T>`) and a templated singly-linked list (`LinkedList<T>`).

---

## 1. Principles of Custom Container Design

When implementing data structures in C++, adhere to:
1. **The Rule of Five:** Custom resource-managing classes must explicitly declare or delete the Destructor, Copy Constructor, Copy Assignment, Move Constructor, and Move Assignment.
2. **Exception Safety:** Ensure strong exception guarantees when allocating memory.
3. **Template Metaprogramming:** Use templates to allow arbitrary element types.

---

## 2. Implementing a Templated Dynamic Array (`Vector<T>`)

```cpp
#include <iostream>
#include <memory>
#include <stdexcept>
#include <utility>

template <typename T>
class Vector {
private:
    T* data_;
    size_t size_;
    size_t capacity_;

    void reallocate(size_t new_cap) {
        T* new_data = new T[new_cap];
        for (size_t i = 0; i < size_; ++i) {
            new_data[i] = std::move(data_[i]);
        }
        delete[] data_;
        data_ = new_data;
        capacity_ = new_cap;
    }

public:
    Vector() : data_(nullptr), size_(0), capacity_(0) {}

    explicit Vector(size_t initial_cap) 
        : data_(new T[initial_cap]), size_(0), capacity_(initial_cap) {}

    ~Vector() {
        delete[] data_;
    }

    // Copy constructor (Deep copy)
    Vector(const Vector& other) 
        : data_(new T[other.capacity_]), size_(other.size_), capacity_(other.capacity_) {
        for (size_t i = 0; i < size_; ++i) {
            data_[i] = other.data_[i];
        }
    }

    // Move constructor
    Vector(Vector&& other) noexcept 
        : data_(other.data_), size_(other.size_), capacity_(other.capacity_) {
        other.data_ = nullptr;
        other.size_ = 0;
        other.capacity_ = 0;
    }

    // Copy assignment
    Vector& operator=(const Vector& other) {
        if (this != &other) {
            Vector temp(other);
            std::swap(data_, temp.data_);
            std::swap(size_, temp.size_);
            std::swap(capacity_, temp.capacity_);
        }
        return *this;
    }

    // Move assignment
    Vector& operator=(Vector&& other) noexcept {
        if (this != &other) {
            delete[] data_;
            data_ = other.data_;
            size_ = other.size_;
            capacity_ = other.capacity_;
            other.data_ = nullptr;
            other.size_ = 0;
            other.capacity_ = 0;
        }
        return *this;
    }

    void push_back(const T& element) {
        if (size_ >= capacity_) {
            reallocate(capacity_ == 0 ? 2 : capacity_ * 2);
        }
        data_[size_++] = element;
    }

    void push_back(T&& element) {
        if (size_ >= capacity_) {
            reallocate(capacity_ == 0 ? 2 : capacity_ * 2);
        }
        data_[size_++] = std::move(element);
    }

    T& operator[](size_t index) { return data_[index]; }
    const T& operator[](size_t index) const { return data_[index]; }

    size_t size() const { return size_; }
    size_t capacity() const { return capacity_; }
};
```

---

## 3. Verification Test Routine

```cpp
int main() {
    Vector<std::string> vec;
    vec.push_back("Data");
    vec.push_back("Structures");
    vec.push_back("Algorithms");

    for (size_t i = 0; i < vec.size(); ++i) {
        std::cout << vec[i] << " ";
    }
    std::cout << "\nSize: " << vec.size() << ", Cap: " << vec.capacity() << std::endl;
    return 0;
}
```

### Expected Output:
```text
Data Structures Algorithms 
Size: 3, Cap: 4
```

