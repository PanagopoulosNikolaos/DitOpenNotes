import tkinter as tk


def runExercise() -> None:
    """
    Runs the temperature converter GUI application.
    """

    def celsiusCallback(*args) -> None:
        """
        Updates Fahrenheit value when Celsius input is modified.
        """
        if root.focus_get() != celsius_entry:
            return
        try:
            celsius_temperature = celsius_var.get()
            c = float(celsius_temperature)
            f = c * (9 / 5) + 32
            celsius_entry.config(background="white")
            fahr_var.set(f"{f:.1f}")
        except ValueError:
            celsius_entry.config(background="pink")

    def fahrCallback(*args) -> None:
        """
        Updates Celsius value when Fahrenheit input is modified.
        """
        if root.focus_get() != fahr_entry:
            return
        try:
            fahr_temperature = fahr_var.get()
            f = float(fahr_temperature)
            c = (f - 32) * 5 / 9
            fahr_entry.config(background="white")
            celsius_var.set(f"{c:.1f}")
        except ValueError:
            fahr_entry.config(background="pink")

    root = tk.Tk()
    celsius_var = tk.StringVar()
    celsius_var.set("0.0")
    fahr_var = tk.StringVar()
    fahr_var.set("32.0")

    root.geometry("350x30")
    root.title("TempConv")

    celsius_var.trace_add("write", celsiusCallback)
    fahr_var.trace_add("write", fahrCallback)
    celsius_entry = tk.Entry(root, width=10, textvariable=celsius_var)
    celsius_entry.grid(row=0, column=0)

    label1 = tk.Label(root, text="Celsius = ")
    label1.grid(row=0, column=1)
    fahr_entry = tk.Entry(root, width=10, textvariable=fahr_var)
    fahr_entry.grid(row=0, column=2)
    label2 = tk.Label(root, text="Fahrenheit")
    label2.grid(row=0, column=3)

    # Centers the window on the screen and runs main loop.
    root.eval("tk::PlaceWindow . center")
    root.mainloop()


if __name__ == "__main__":
    runExercise()
