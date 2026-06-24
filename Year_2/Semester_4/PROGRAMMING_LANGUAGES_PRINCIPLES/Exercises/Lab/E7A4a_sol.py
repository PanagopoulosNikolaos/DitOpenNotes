from ortools.sat.python import cp_model


def solveSingleMachineScheduling() -> None:
    """
    Schedules 10 jobs on a single machine to minimize total weighted tardiness.
    """
    processing_times = [12, 8, 15, 6, 20, 7, 10, 14, 9, 11]
    weights = [4, 2, 5, 3, 6, 1, 4, 7, 2, 5]
    due_dates = [25, 20, 35, 18, 45, 30, 28, 40, 32, 38]

    num_jobs = len(processing_times)
    horizon = sum(processing_times)

    model = cp_model.CpModel()

    starts = []
    ends = []
    intervals = []
    tardinesses = []

    for i in range(num_jobs):
        p_time = processing_times[i]
        d_date = due_dates[i]

        # Creates the start, end, and interval variables for each job.
        start_var = model.new_int_var(0, horizon, f"start_{i}")
        end_var = model.new_int_var(0, horizon, f"end_{i}")
        interval_var = model.new_interval_var(
            start_var, p_time, end_var, f"interval_{i}"
        )

        starts.append(start_var)
        ends.append(end_var)
        intervals.append(interval_var)

        # Creates the tardiness variable for each job.
        tardiness_var = model.new_int_var(0, horizon, f"tardiness_{i}")
        model.add(tardiness_var >= end_var - d_date)
        model.add(tardiness_var >= 0)
        tardinesses.append(tardiness_var)

    # Prevents overlapping intervals on the single machine.
    model.add_no_overlap(intervals)

    # Sets the objective: minimize the total weighted tardiness.
    objective_terms = [
        tardinesses[i] * weights[i] for i in range(num_jobs)
    ]
    model.minimize(sum(objective_terms))

    solver = cp_model.CpSolver()
    status = solver.solve(model)

    # Outputs the optimal schedule details if found.
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print(f"Optimal Total Weighted Tardiness: {int(solver.objective_value)}")
        print("\nJob Schedule:")
        print("Job | Start | End | Due Date | Weight | Tardiness")
        print("--------------------------------------------------")

        # Collects and sorts jobs by their start time to print in sequence.
        scheduled_jobs = []
        for i in range(num_jobs):
            scheduled_jobs.append((
                i,
                solver.value(starts[i]),
                solver.value(ends[i]),
                due_dates[i],
                weights[i],
                solver.value(tardinesses[i])
            ))
        scheduled_jobs.sort(key=lambda x: x[1])

        for job in scheduled_jobs:
            print(f"{job[0]:3d} | {job[1]:5d} | {job[2]:3d} | {job[3]:8d} | {job[4]:6d} | {job[5]:9d}")
    else:
        print("No solution found.")


if __name__ == "__main__":
    solveSingleMachineScheduling()
