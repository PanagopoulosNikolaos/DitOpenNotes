import matplotlib.pyplot as plt


def visualizeSchedule() -> None:
    """
    Renders a horizontal Gantt chart from scheduling metrics.
    """
    sample_schedule = [
        {"machine": 0, "job": 0, "start": 0, "finish": 20},
        {"machine": 0, "job": 1, "start": 20, "finish": 25},
        {"machine": 0, "job": 2, "start": 30, "finish": 45},
        {"machine": 1, "job": 0, "start": 30, "finish": 58},
        {"machine": 1, "job": 1, "start": 90, "finish": 110},
        {"machine": 1, "job": 2, "start": 120, "finish": 170},
        {"machine": 2, "job": 0, "start": 100, "finish": 220},
        {"machine": 2, "job": 1, "start": 200, "finish": 340},
        {"machine": 2, "job": 2, "start": 340, "finish": 420},
    ]

    plt.figure(figsize=(10, 6))
    ax = plt.gca()
    # Renders each schedule item as a horizontal bar chart representation.
    for row in sample_schedule:
        ax.barh(
            y=row["machine"],
            width=row["finish"] - row["start"],
            left=row["start"],
            color=f"C{row['job']}",
        )
    ax.set_xlabel("Time")
    ax.set_ylabel("Machine")
    ax.set_yticks(range(3))
    plt.show()


if __name__ == "__main__":
    visualizeSchedule()
