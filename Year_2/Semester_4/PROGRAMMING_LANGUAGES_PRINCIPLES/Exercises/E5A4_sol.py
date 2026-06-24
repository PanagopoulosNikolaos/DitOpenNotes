import sys
import tkinter as tk
from tkinter import messagebox


class Complex:
    """
    Represents a mathematical complex number with real and imaginary parts.

    Supports basic operations: addition, subtraction, multiplication, and division.
    - __init__: Initializes the complex number with real and imaginary parts.
    - __add__: Adds two complex numbers.
    - __sub__: Subtracts one complex number from another.
    - __mul__: Multiplies two complex numbers.
    - __truediv__: Divides one complex number by another.
    - __str__: Returns the string representation of the complex number.
    """

    def __init__(self, real: float, imag: float):
        """
        Initializes a Complex number.

        Args:
            real (float): The real part.
            imag (float): The imaginary part.
        """
        self.real = real
        self.imag = imag

    def __add__(self, other_complex: "Complex") -> "Complex":
        """
        Adds two complex numbers.

        Args:
            other_complex (Complex): The complex number to add.

        Returns:
            Complex: The resulting complex sum.
        """
        real_new = self.real + other_complex.real
        imag_new = self.imag + other_complex.imag
        return Complex(real_new, imag_new)

    def __sub__(self, other_complex: "Complex") -> "Complex":
        """
        Subtracts a complex number.

        Args:
            other_complex (Complex): The complex number to subtract.

        Returns:
            Complex: The resulting complex difference.
        """
        real_new = self.real - other_complex.real
        imag_new = self.imag - other_complex.imag
        return Complex(real_new, imag_new)

    def __mul__(self, other_complex: "Complex") -> "Complex":
        """
        Multiplies two complex numbers.

        Args:
            other_complex (Complex): The complex number to multiply.

        Returns:
            Complex: The resulting complex product.
        """
        real_new = self.real * other_complex.real - self.imag * other_complex.imag
        imag_new = self.imag * other_complex.real + self.real * other_complex.imag
        return Complex(real_new, imag_new)

    def __truediv__(self, other_complex: "Complex") -> "Complex":
        """
        Divides by another complex number.

        Args:
            other_complex (Complex): The complex denominator.

        Returns:
            Complex: The resulting complex quotient.
        """
        temp_real = self.real * other_complex.real + self.imag * other_complex.imag
        temp_imag = other_complex.real * self.imag - self.real * other_complex.imag
        denum = other_complex.real**2 + other_complex.imag**2
        real_new = temp_real / denum
        imag_new = temp_imag / denum
        return Complex(real_new, imag_new)

    def __str__(self) -> str:
        """
        Returns string representation of complex number.

        Returns:
            str: Formatted string containing real and imaginary components.
        """
        return f"({self.real}, {self.imag}i)"


class ViewGui(tk.Frame):
    """
    A GUI view class for the complex number calculator application.

    Provides entry widgets for two complex numbers and buttons for operations.
    - __init__: Sets up grid layout and widget components.
    - setController: Links the controller object to this view.
    - handleInputEvent: Parses user entries into Complex instances.
    - showResult: Updates GUI labels with calculation results.
    - addClicked: Triggers addition operation.
    - substractClicked: Triggers subtraction operation.
    - multiplyClicked: Triggers multiplication operation.
    - divideClicked: Triggers division operation.
    """

    def __init__(self, parent: tk.Widget):
        """
        Initializes the ViewGui frame.

        Args:
            parent (tk.Widget): The parent Tkinter widget.
        """
        super().__init__(parent)

        # Creates entry fields for first complex number.
        self.real1_label = tk.Label(self, text="Real 1: ")
        self.real1_label.grid(row=0, column=0)
        self.real1_var = tk.DoubleVar()
        self.real1_entry = tk.Entry(self, textvariable=self.real1_var, justify="right")
        self.real1_entry.grid(row=0, column=1)
        self.imag1_label = tk.Label(self, text="Imaginary 1: ")
        self.imag1_label.grid(row=0, column=2)
        self.imag1_var = tk.DoubleVar()
        self.imag1_entry = tk.Entry(self, textvariable=self.imag1_var, justify="right")
        self.imag1_entry.grid(row=0, column=3)

        # Creates entry fields for second complex number.
        self.real2_label = tk.Label(self, text="Real 2: ")
        self.real2_label.grid(row=1, column=0)
        self.real2_var = tk.DoubleVar()
        self.real2_entry = tk.Entry(self, textvariable=self.real2_var, justify="right")
        self.real2_entry.grid(row=1, column=1)
        self.imag2_label = tk.Label(self, text="Imaginary 2: ")
        self.imag2_label.grid(row=1, column=2)
        self.imag2_var = tk.DoubleVar()
        self.imag2_entry = tk.Entry(self, textvariable=self.imag2_var, justify="right")
        self.imag2_entry.grid(row=1, column=3)

        # Configures buttons for triggering calculations.
        self.add_button = tk.Button(self, text="Add", command=self.addClicked)
        self.add_button.grid(row=2, column=0, sticky=tk.W)
        self.substract_button = tk.Button(
            self, text="Substract", command=self.substractClicked
        )
        self.substract_button.grid(row=2, column=1, sticky=tk.W)
        self.multiply_button = tk.Button(
            self, text="Multiply", command=self.multiplyClicked
        )
        self.multiply_button.grid(row=2, column=2, sticky=tk.W)
        self.divide_button = tk.Button(self, text="Divide", command=self.divideClicked)
        self.divide_button.grid(row=2, column=3, sticky=tk.W)

        # Defines labels to display results.
        self.real_result_label = tk.Label(self, text="")
        self.real_result_label.grid(row=3, column=0)
        self.imag_result_label = tk.Label(self, text="")
        self.imag_result_label.grid(row=3, column=1)

        self.controller = None
        self.complex1 = None
        self.complex2 = None

    def setController(self, controller: "Controller") -> None:
        """
        Sets the controller instance.

        Args:
            controller (Controller): The controller to communicate with.
        """
        self.controller = controller

    def handleInputEvent(self) -> None:
        """
        Gathers raw text entries and parses them into Complex object states.
        """
        self.complex1 = Complex(
            float(self.real1_entry.get()), float(self.imag1_entry.get())
        )
        self.complex2 = Complex(
            float(self.real2_entry.get()), float(self.imag2_entry.get())
        )

    def showResult(self, complex_result: Complex) -> None:
        """
        Formats and displays calculation results on the interface.

        Args:
            complex_result (Complex): The complex output to display.
        """
        formatted_real = "{:.3f}".format(float(complex_result.real))
        formatted_imag = "{:.3f}".format(float(complex_result.imag))
        self.real_result_label["text"] = "Real Result: {}".format(formatted_real)
        self.imag_result_label["text"] = "Imaginary Result: {}".format(formatted_imag)

    def addClicked(self) -> None:
        """
        Handles GUI addition button clicks.
        """
        self.handleInputEvent()
        if self.controller:
            self.controller.add(self.complex1, self.complex2)

    def substractClicked(self) -> None:
        """
        Handles GUI subtraction button clicks.
        """
        self.handleInputEvent()
        if self.controller:
            self.controller.substract(self.complex1, self.complex2)

    def multiplyClicked(self) -> None:
        """
        Handles GUI multiplication button clicks.
        """
        self.handleInputEvent()
        if self.controller:
            self.controller.multiply(self.complex1, self.complex2)

    def divideClicked(self) -> None:
        """
        Handles GUI division button clicks.
        """
        self.handleInputEvent()
        if self.controller:
            self.controller.divide(self.complex1, self.complex2)


class ViewTui:
    """
    A text-based user interface (TUI) for the complex number calculator.

    Provides command-line prompts and outputs for mathematical operations.
    - __init__: Displays instructions and accepts user selection.
    - handleInputEvent: Prompt user for parts of complex numbers.
    - handleModellingStage: Builds Complex instances from user input.
    - showResult: Prints results onto the command-line stdout.
    - addClicked: Triggers addition operation.
    - substractClicked: Triggers subtraction operation.
    - multiplyClicked: Triggers multiplication operation.
    - divideClicked: Triggers division operation.
    """

    def __init__(self):
        """
        Initializes the CLI text interface.
        """
        print("~" * 82)
        print("~" * 30 + "  Complex Calculator  " + "~" * 30)
        print("~" * 82 + "\n")

        print("Choose operation::")
        self.operation_selection = int(
            input("1.Addition  2.Substraction  3.Multiplication  4.Division \n5.Quit\n")
        )

        self.controller = Controller(Complex(1, 2), self)
        self.complex1 = None
        self.complex2 = None
        self.real1 = 0.0
        self.imag1 = 0.0
        self.real2 = 0.0
        self.imag2 = 0.0

        if self.operation_selection == 1:
            self.addClicked()
        elif self.operation_selection == 2:
            self.substractClicked()
        elif self.operation_selection == 3:
            self.multiplyClicked()
        elif self.operation_selection == 4:
            self.divideClicked()
        elif self.operation_selection == 5:
            print("Quitting ...")
        else:
            print("Wrong Input!!!")

    def handleInputEvent(self) -> None:
        """
        Requests inputs for two complex numbers via standard input.
        """
        print("Input of 1st complex number:")
        print("Give real part of 1st complex number: ")
        self.real1 = float(input())
        print("Give imaginary part of 1st complex number: ")
        self.imag1 = float(input())

        print("Input of 2nd complex number:")
        print("Give real part of 2nd complex number: ")
        self.real2 = float(input())
        print("Give imaginary part of 2nd complex number: ")
        self.imag2 = float(input())

    def handleModellingStage(self) -> None:
        """
        Instantiates Complex objects using the gathered parts.
        """
        self.complex1 = Complex(self.real1, self.imag1)
        self.complex2 = Complex(self.real2, self.imag2)

    def showResult(self, complex_result: Complex) -> None:
        """
        Prints output of operations to command line.

        Args:
            complex_result (Complex): The complex number result.
        """
        print(
            "Real Result: {:.3f}, Imaginary Result: {:.3f}".format(
                complex_result.real, complex_result.imag
            )
        )

    def addClicked(self) -> None:
        """
        Triggers CLI addition sequence.
        """
        self.handleInputEvent()
        self.handleModellingStage()
        self.controller.add(self.complex1, self.complex2)

    def substractClicked(self) -> None:
        """
        Triggers CLI subtraction sequence.
        """
        self.handleInputEvent()
        self.handleModellingStage()
        self.controller.substract(self.complex1, self.complex2)

    def multiplyClicked(self) -> None:
        """
        Triggers CLI multiplication sequence.
        """
        self.handleInputEvent()
        self.handleModellingStage()
        self.controller.multiply(self.complex1, self.complex2)

    def divideClicked(self) -> None:
        """
        Triggers CLI division sequence.
        """
        self.handleInputEvent()
        self.handleModellingStage()
        self.controller.divide(self.complex1, self.complex2)


class Controller:
    """
    Controls flow of data between the Complex model and View representations.

    Receives operation events, invokes calculations on Model, and updates the View.
    - __init__: Initializes the controller with model and view objects.
    - add: Adds complex numbers and displays results.
    - substract: Subtracts complex numbers and displays results.
    - multiply: Multiplies complex numbers and displays results.
    - divide: Divides complex numbers and displays results.
    """

    def __init__(self, model: Complex = None, view=None):
        """
        Initializes Controller.

        Args:
            model (Complex): Complex model representation.
            view (object): Target view class.
        """
        self.model = model
        self.view = view

    def add(self, complex1: Complex, complex2: Complex) -> None:
        """
        Performs addition and sends result to view.

        Args:
            complex1 (Complex): The first complex number.
            complex2 (Complex): The second complex number.
        """
        self.model = complex1
        complex_result = self.model + complex2
        self.view.showResult(complex_result)

    def substract(self, complex1: Complex, complex2: Complex) -> None:
        """
        Performs subtraction and sends result to view.

        Args:
            complex1 (Complex): The first complex number.
            complex2 (Complex): The second complex number.
        """
        self.model = complex1
        complex_result = self.model - complex2
        self.view.showResult(complex_result)

    def multiply(self, complex1: Complex, complex2: Complex) -> None:
        """
        Performs multiplication and sends result to view.

        Args:
            complex1 (Complex): The first complex number.
            complex2 (Complex): The second complex number.
        """
        self.model = complex1
        complex_result = self.model * complex2
        self.view.showResult(complex_result)

    def divide(self, complex1: Complex, complex2: Complex) -> None:
        """
        Performs division, ensuring division by zero warnings are handled.

        Args:
            complex1 (Complex): The first complex number.
            complex2 (Complex): The second complex number.
        """
        self.model = complex1

        # Check command line arguments for specific layout instructions.
        if len(sys.argv) > 1 and sys.argv[1].upper() == "GUI":
            try:
                complex_result = self.model / complex2
                self.view.showResult(complex_result)
            except ZeroDivisionError:
                messagebox.showwarning(
                    title="Division Error",
                    message=" Can't divide by zero!!! \n Please input valid numbers!",
                )

        if len(sys.argv) > 1 and sys.argv[1].upper() == "TUI":
            try:
                complex_result = self.model / complex2
                self.view.showResult(complex_result)
            except ZeroDivisionError:
                print(" Can't divide by zero!!! \n Please input valid numbers!")


class App(tk.Tk):
    """
    Initializes the main Tkinter window for the GUI-mode application.

    Acts as the entry point for the window and wires Model, View, and Controller.
    - __init__: Initializes the Tk application and builds components.
    """

    def __init__(self):
        """
        Initializes the GUI calculator window.
        """
        super().__init__()
        self.title("Complex Calculator")
        model = Complex(1, 2)
        view_gui = ViewGui(self)
        view_gui.grid(row=0, column=0, padx=10, pady=10)
        controller_gui = Controller(model, view_gui)
        view_gui.setController(controller_gui)


if __name__ == "__main__":
    try:
        if sys.argv[1].upper() == "GUI":
            app = App()
            app.mainloop()
        elif sys.argv[1].upper() == "TUI":
            while True:
                view = ViewTui()
                if view.operation_selection == 5:
                    break

        if sys.argv[1].upper() not in ["GUI", "TUI"]:
            raise Exception("Wrong interface command line parameter")
    except IndexError:
        print("Input interface type, as command line parameter")
