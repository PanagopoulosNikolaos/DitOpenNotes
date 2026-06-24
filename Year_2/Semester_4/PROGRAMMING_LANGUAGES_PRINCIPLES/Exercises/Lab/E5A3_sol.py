import datetime
from tkinter import BOTTOM, Button, Entry, Frame, Label, StringVar, Tk
import requests
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure


def runExercise() -> None:
    """
    Runs the temperature plotting GUI application.
    """

    def plotTemperatureData() -> None:
        """
        Fetches temperature data from Open-Meteo and plots a diagram.
        """
        lat = latitude_entry.get()
        lon = longitude_entry.get()

        date_time = datetime.datetime.now() - datetime.timedelta(days=5)

        temperatures = []
        dates = []

        start_date = date_time.strftime("%Y-%m-%d")
        end_date = datetime.datetime.now().strftime("%Y-%m-%d")

        weather_url = "https://archive-api.open-meteo.com/v1/archive"

        params = {
            "latitude": lat,
            "longitude": lon,
            "start_date": start_date,
            "end_date": end_date,
            "hourly": "temperature_2m",
            "timezone": "auto",
        }

        response = requests.get(weather_url, params=params)
        print(response.status_code)
        print(response.text[:500])

        weather_data = response.json()

        if response.status_code != 200:
            print("API error:", response.status_code, weather_data)
            return

        temperatures = [
            int(temp)
            for temp in weather_data["hourly"]["temperature_2m"]
            if temp is not None
        ]

        for _ in range(6):
            temp_date = str(date_time).split(" ")[0]
            temp_date = temp_date.split("-")
            dates.append(temp_date[2] + "/" + temp_date[1] + "/" + temp_date[0])
            date_time = date_time + datetime.timedelta(days=1)

        fig = Figure(figsize=(10, 5), dpi=100)
        plot1 = fig.add_subplot(111)
        plot1.plot(temperatures)
        plot1.set_title(f"Θερμοκρασία στις γεωγραφικές συντεταγμένες {lat=} {lon=}")
        plot1.set_ylabel("Θερμοκρασία (°C)")
        plot1.set_xticks([0, 24, 48, 72, 96, 120])
        plot1.set_xticklabels(dates)

        # Clears previous plots from the frame to prevent layering.
        for widget in plot_frame.winfo_children():
            widget.destroy()

        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()
        toolbar = NavigationToolbar2Tk(canvas, plot_frame)
        toolbar.update()
        canvas.get_tk_widget().pack()

    window = Tk()
    window.title("Διάγραμμα θερμοκρασιών για τις 5 τελευταίες ημέρες")
    window.geometry("1000x500")

    frame = Frame(window)
    frame.pack()

    plot_frame = Frame(window)
    plot_frame.pack(side=BOTTOM)

    Label(frame, text="Γεωγραφικό πλάτος (latitude)").grid(row=0, sticky="w")
    Label(frame, text="Γεωγραφικό μήκος (longitude)").grid(row=1, sticky="w")

    default_lat = StringVar(window, value="39.1606")
    default_lon = StringVar(window, value="20.9853")

    latitude_entry = Entry(frame, textvariable=default_lat)
    longitude_entry = Entry(frame, textvariable=default_lon)

    latitude_entry.grid(row=0, column=1, sticky="w")
    longitude_entry.grid(row=1, column=1, sticky="w")

    plot_button = Button(master=frame, command=plotTemperatureData, height=2, width=10, text="Plot")
    plot_button.grid(row=2, column=0, columnspan=2, sticky="news")

    window.mainloop()


if __name__ == "__main__":
    runExercise()
