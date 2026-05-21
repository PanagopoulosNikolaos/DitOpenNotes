def runExercise() -> None:
    """
    Checks student status using all and any built-in functions.
    """
    # Sample dataset containing (student_name, passed_status).
    students = [
        ("Anna", True),
        ("Nikos", True),
        ("Maria", False),
        ("Giorgos", True)
    ]

    # Evaluates if every single student successfully passed the course.
    all_passed = all(passed for _, passed in students)

    # Evaluates if at least one student failed to pass the course.
    someone_failed = any(not passed for _, passed in students)

    print("All students passed:", all_passed)
    print("At least one student failed:", someone_failed)


if __name__ == "__main__":
    runExercise()
