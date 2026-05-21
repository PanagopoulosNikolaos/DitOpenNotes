import tkinter as tk


def runExercise() -> None:
    """
    Runs the counter GUI application.
    """

    def incrementCounter() -> None:
        """
        Increments the counter value shown on the label.
        """
        count_val = int(count_label["text"])
        count_val += 1
        count_label["text"] = str(count_val)

    root = tk.Tk()
    root.geometry("200x30")
    root.title("Counter")
    count_label = tk.Label(root, text="0", width=10, background="white")
    count_label.pack(side=tk.LEFT)
    increment_button = tk.Button(root, text="Count", width=10)
    increment_button.pack(side=tk.RIGHT)
    increment_button.config(command=incrementCounter)

    # Centers the window on the screen and runs main loop.
    root.eval("tk::PlaceWindow . center")
    root.mainloop()


if __name__ == "__main__":
    runExercise()
