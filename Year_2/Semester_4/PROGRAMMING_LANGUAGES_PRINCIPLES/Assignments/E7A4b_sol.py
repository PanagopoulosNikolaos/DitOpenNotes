import os
from ortools.sat.python import cp_model


def loadInstances(filename: str, n: int) -> list[tuple[list[int], list[int], list[int]]]:
    """
    Loads scheduling instances from a benchmark text file.

    Args:
        filename (str): The path to the benchmark file.
        n (int): The number of jobs per instance in the file.

    Returns:
        list[tuple[list[int], list[int], list[int]]]: A list of parsed instances.
    """
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        tokens = content.split()
        numbers = [int(token) for token in tokens]

    instances = []
    instance_size = 3 * n
    num_instances = len(numbers) // instance_size

    for i in range(num_instances):
        start_idx = i * instance_size
        chunk = numbers[start_idx : start_idx + instance_size]
        p_times = chunk[0:n]
        weights = chunk[n : 2 * n]
        d_dates = chunk[2 * n : 3 * n]
        instances.append((p_times, weights, d_dates))

    return instances


def solveInstance(
    n: int,
    processing_times: list[int],
    weights: list[int],
    due_dates: list[int],
    time_limit_sec: float = 30.0
) -> None:
    """
    Solves a single weighted tardiness scheduling instance using CP-SAT.

    Args:
        n (int): The number of jobs.
        processing_times (list[int]): Processing times for each job.
        weights (list[int]): Penalization weights for each job.
        due_dates (list[int]): Due dates for each job.
        time_limit_sec (float): Max allowed solver runtime in seconds.
    """
    horizon = sum(processing_times)
    model = cp_model.CpModel()

    starts = []
    ends = []
    intervals = []
    tardinesses = []

    for i in range(n):
        p_time = processing_times[i]
        d_date = due_dates[i]

        # Creates scheduling decision variables for each job.
        start_var = model.new_int_var(0, horizon, f"start_{i}")
        end_var = model.new_int_var(0, horizon, f"end_{i}")
        interval_var = model.new_interval_var(
            start_var, p_time, end_var, f"interval_{i}"
        )

        starts.append(start_var)
        ends.append(end_var)
        intervals.append(interval_var)

        # Creates tardiness variables computed as max(end - due_date, 0).
        tardiness_var = model.new_int_var(0, horizon, f"tardiness_{i}")
        model.add(tardiness_var >= end_var - d_date)
        model.add(tardiness_var >= 0)
        tardinesses.append(tardiness_var)

    # Ensures that the machine processes only one job at any time.
    model.add_no_overlap(intervals)

    # Minimizes the total weighted tardiness objective.
    objective_terms = [tardinesses[i] * weights[i] for i in range(n)]
    model.minimize(sum(objective_terms))

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = time_limit_sec
    status = solver.solve(model)

    # Prints the optimized objective value and the resulting job schedule.
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        status_name = "Optimal" if status == cp_model.OPTIMAL else "Feasible"
        print(f"Status: {status_name}")
        print(f"Total Weighted Tardiness: {int(solver.objective_value)}")
        print("\nJob Sequence:")

        scheduled_jobs = []
        for i in range(n):
            scheduled_jobs.append((
                i,
                solver.value(starts[i]),
                solver.value(ends[i]),
                due_dates[i],
                weights[i],
                solver.value(tardinesses[i])
            ))
        scheduled_jobs.sort(key=lambda x: x[1])

        print("Sequence of jobs (by starting time):")
        sequence_str = " -> ".join(f"Job {job[0]}" for job in scheduled_jobs)
        print(sequence_str)
    else:
        print("No solution found.")


def runExercise() -> None:
    """
    Loads wt40.txt and solves the first benchmark instance.
    """
    file_path = os.path.join("Assignments", "wt40.txt")
    if not os.path.exists(file_path):
        # Fallback if executing from a different context directory.
        file_path = "wt40.txt"

    print("Loading instances from wt40.txt...")
    instances = loadInstances(file_path, 40)
    print(f"Successfully loaded {len(instances)} instances.")

    print("\nSolving Instance 1 of wt40.txt (40 jobs):")
    p_times, weights, d_dates = instances[0]
    solveInstance(40, p_times, weights, d_dates)


if __name__ == "__main__":
    runExercise()
