import tkinter as tk
from tkinter import ttk


class Application(tk.Tk):
    """
    Main GUI application class implementing an adjustable timer.

    Provides elapsed time visualizations and slider-based duration adjustments.
    - __init__: Configures grid layout, widgets, and invokes starting timer.
    - runTimer: Periodically updates elapsed time displays and progress.
    - resetTimer: Resets the elapsed counters and schedules a timer restart.
    - updateDuration: Updates duration limits dynamically via scale controls.
    """

    def __init__(self):
        """
        Initializes the timer GUI application.
        """
        super().__init__()

        # Sets up main window geometry and layout variables.
        self.title("Timer")
        self.geometry("300x150")
        for x in range(4):
            self.grid_rowconfigure(x, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)

        self.et_label = ttk.Label(self, text="Elapsed Time:")
        self.et_label.grid(row=0, column=0)

        self.et_time = ttk.Label(self, text="0")
        self.et_time.grid(row=1, column=0)

        self.progress_bar = ttk.Progressbar(
            self, orient="horizontal", length=200, mode="determinate"
        )
        self.progress_bar.grid(row=0, column=1, padx=3, pady=10)

        self.d_label = ttk.Label(self, text="Duration:")
        self.d_label.grid(row=2, column=0)

        self.d_time = 10
        self.elapsed_ms = 0
        self.timer_id = None
        self.d_slider = ttk.Scale(
            self, from_=0, to=100, orient="horizontal", command=self.updateDuration
        )
        self.d_slider.set(10)
        self.d_slider.grid(row=2, column=1, sticky="nswe", padx=10)

        self.reset_button = ttk.Button(self, text="Reset", command=self.resetTimer)
        self.reset_button.grid(
            row=3, column=0, columnspan=2, sticky="nswe", padx=10, pady=10
        )

        # Starts the timer thread simulation.
        self.runTimer()

    def runTimer(self) -> None:
        """
        Updates the timer progress bar and duration metrics recursively.
        """
        self.et_time["text"] = "{:.1f}".format(self.elapsed_ms / 1000) + "s"
        diff = self.d_time - (self.elapsed_ms / 1000)

        if not (self.elapsed_ms / 1000) >= self.d_time:
            self.progress_bar["value"] = (
                ((self.d_time - diff) / self.d_time) * 100 if self.d_time else 0
            )
            self.elapsed_ms += 1
            # Reschedules callback after 1 millisecond.
            self.timer_id = self.after(1, self.runTimer)
        else:
            self.progress_bar["value"] = 100

    def resetTimer(self) -> None:
        """
        Halts existing recursive timer updates and resets the tracking state.
        """
        self.elapsed_ms = 0
        self.after_cancel(self.timer_id)
        self.runTimer()

    def updateDuration(self, value: str) -> None:
        """
        Applies changes from slider scales to current target durations.

        Args:
            value (str): The string value from the slider.
        """
        self.d_time = float(value)
        if self.d_time > self.elapsed_ms / 1000 and self.progress_bar["value"] == 100:
            self.runTimer()


if __name__ == "__main__":
    app = Application()
    app.mainloop()
