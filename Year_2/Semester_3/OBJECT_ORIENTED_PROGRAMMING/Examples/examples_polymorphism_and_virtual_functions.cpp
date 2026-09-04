// ==============================================================================
// File: examples_polymorphism_and_virtual_functions.cpp
// Description: Demonstrates abstract interfaces, polymorphic dispatch, and vtables.
// ==============================================================================

#include <iostream>
#include <vector>
#include <memory>
#include <cmath>

// Abstract Base Class
class Shape {
protected:
    std::string name_;

public:
    explicit Shape(std::string name) : name_(std::move(name)) {}
    virtual ~Shape() = default;

    [[nodiscard]] const std::string& getName() const noexcept {
        return name_;
    }

    [[nodiscard]] virtual double computeArea() const = 0;
    [[nodiscard]] virtual double computePerimeter() const = 0;
    virtual void printDetails() const {
        std::cout << "Shape: " << name_ 
                  << " | Area: " << computeArea() 
                  << " | Perimeter: " << computePerimeter() << "\n";
    }
};

class Rectangle : public Shape {
private:
    double width_;
    double height_;

public:
    Rectangle(double width, double height)
        : Shape("Rectangle"), width_(width), height_(height) {}

    [[nodiscard]] double computeArea() const override {
        return width_ * height_;
    }

    [[nodiscard]] double computePerimeter() const override {
        return 2.0 * (width_ + height_);
    }
};

class Circle : public Shape {
private:
    double radius_;

public:
    explicit Circle(double radius)
        : Shape("Circle"), radius_(radius) {}

    [[nodiscard]] double computeArea() const override {
        return M_PI * radius_ * radius_;
    }

    [[nodiscard]] double computePerimeter() const override {
        return 2.0 * M_PI * radius_;
    }
};

int main() {
    std::vector<std::unique_ptr<Shape>> shapes;
    shapes.push_back(std::make_unique<Rectangle>(4.0, 5.0));
    shapes.push_back(std::make_unique<Circle>(3.0));

    std::cout << "--- Polymorphic Shape Evaluation ---\n";
    for (const auto& shape : shapes) {
        shape->printDetails();
    }

    return 0;
}

