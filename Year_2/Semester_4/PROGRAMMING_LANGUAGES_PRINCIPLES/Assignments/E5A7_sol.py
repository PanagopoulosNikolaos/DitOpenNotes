import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime


class Application(tk.Tk):
    """
    Main GUI application class for booking flights with validation constraints.

    Provides a window to select flight types and date inputs with validation.
    - __init__: Sets up window layout and grid widgets.
    - checkBox1: Validates starting date format correctness.
    - checkBox2: Validates return date format correctness.
    - onComboboxSelect: Enables/disables return date entry based on flight type.
    - validateDate: Triggers entry color shifts and button checks during changes.
    - compareDates: Validates return date is after starting date.
    - displayMessage: Opens a popup dialog confirming booking details.
    """

    def __init__(self):
        """
        Initializes the flight booking GUI application.
        """
        super().__init__()

        # Sets up main window geometry and layout configurations.
        self.title("Book Flight")
        self.geometry("300x120")
        for x in range(4):
            self.rowconfigure(x, weight=1)
        self.columnconfigure(0, weight=1)

        # Creates a combo box to choose between flight types.
        options = ["one-way flight", "return flight"]
        self.flight_options = ttk.Combobox(self, values=options, state="readonly")
        self.flight_options.set("one-way flight")
        self.flight_options.bind("<<ComboboxSelected>>", self.onComboboxSelect)
        self.flight_options.grid(row=0, sticky="nesw", padx=3, pady=3)

        # Creates date input for start date.
        self.entry_val1 = tk.StringVar()
        self.entry_val1.trace_add("write", self.validateDate)
        self.start_date = tk.Entry(self, textvariable=self.entry_val1)
        self.start_date.grid(row=1, sticky="nesw", padx=3, pady=3)

        # Creates date input for return date.
        self.entry_val2 = tk.StringVar()
        self.entry_val2.trace_add("write", self.validateDate)
        self.return_date = tk.Entry(self, textvariable=self.entry_val2)
        self.return_date["state"] = "disabled"
        self.return_date.grid(row=2, sticky="nesw", padx=4, pady=4)

        # Places validation action button.
        self.book_button = tk.Button(
            self, text="Book", command=self.displayMessage, state="disabled", foreground="gray"
        )
        self.book_button.grid(row=3, sticky="nesw", padx=5, pady=5)

    def checkBox1(self) -> bool:
        """
        Validates starting date string format.

        Returns:
            bool: True if formatting matches %d.%m.%Y, False otherwise.
        """
        try:
            datetime.strptime(self.start_date.get(), "%d.%m.%Y")
            return True
        except ValueError:
            return False

    def checkBox2(self) -> bool:
        """
        Validates return date string format.

        Returns:
            bool: True if formatting matches %d.%m.%Y, False otherwise.
        """
        try:
            datetime.strptime(self.return_date.get(), "%d.%m.%Y")
            return True
        except ValueError:
            return False

    def onComboboxSelect(self, event: tk.Event) -> None:
        """
        Handles state updates when the flight option changes.

        Args:
            event (tk.Event): Combobox selection event object.
        """
        if self.flight_options.get() == "one-way flight":
            self.return_date["state"] = "disabled"
            if self.checkBox1():
                self.book_button.configure(state="normal", foreground="black")
            else:
                self.book_button.configure(state="disabled", foreground="gray")
        else:
            self.return_date["state"] = "normal"
            if self.checkBox1() and self.checkBox2():
                self.book_button.configure(state="normal", foreground="black")
            else:
                self.book_button.configure(state="disabled", foreground="gray")

    def validateDate(self, *args) -> None:
        """
        Handles field-level verification and UI feedback.
        """
        focused_widget = self.focus_get()

        # Shifts background color dynamically depending on the parsing result.
        if focused_widget in [self.start_date, self.return_date]:
            if not focused_widget.get():
                focused_widget["bg"] = "white"
                self.book_button.configure(state="disabled", foreground="gray")
            else:
                try:
                    datetime.strptime(focused_widget.get(), "%d.%m.%Y")
                    focused_widget["bg"] = "white"
                    self.book_button.configure(state="normal", foreground="black")
                except ValueError:
                    focused_widget["bg"] = "red"
                    self.book_button.configure(state="disabled", foreground="gray")

        if self.flight_options.get() == "return flight":
            self.compareDates()

    def compareDates(self) -> None:
        """
        Verifies return date comes chronologically after departure date.
        """
        date_str1 = self.start_date.get()
        date_str2 = self.return_date.get()

        try:
            date1 = datetime.strptime(date_str1, "%d.%m.%Y")
            date2 = datetime.strptime(date_str2, "%d.%m.%Y")
            if date2 < date1:
                self.book_button.configure(state="disabled", fg="gray")
            else:
                self.book_button.configure(state="normal", fg="black")
        except ValueError:
            self.book_button.configure(state="disabled", fg="gray")

    def displayMessage(self) -> None:
        """
        Renders information message indicating successful booking.
        """
        if self.flight_options.get() == "one-way flight":
            messagebox.showinfo(
                "Booking information",
                f"You have booked a one-way flight for {self.start_date.get()}",
            )
        else:
            messagebox.showinfo(
                "Booking information",
                f"You have booked a return flight departing on {self.start_date.get()} and returning on {self.return_date.get()}",
            )


if __name__ == "__main__":
    app = Application()
    app.mainloop()
