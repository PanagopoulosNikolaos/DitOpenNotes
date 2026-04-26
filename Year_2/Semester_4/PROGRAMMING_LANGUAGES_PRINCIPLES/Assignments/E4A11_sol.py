import logging

def calculateDivision(x: float, y: float) -> float:
    """
    Performs division and logs the process and outcome.
    Args:
        x (float): The dividend.
        y (float): The divisor.
    Returns:
        float: The quotient, or None if division by zero occurs.
    """
    logger = logging.getLogger("ExerciseLogger")
    # Records the attempt at division for debugging purposes.
    logger.debug(f"Calculating {x} / {y}")
    
    try:
        result = x / y
        # Logs successful operations at the INFO level.
        logger.info(f"Result: {result}")
        return result
    except ZeroDivisionError:
        # Captures the error and logs the stack trace to help diagnose the failure.
        logger.exception("Division by zero!")
        return None

def runExercise():
    """
    Configures logging handlers and executes sample divisions.
    """
    logger = logging.getLogger("ExerciseLogger")
    # Sets the base logger level to DEBUG to ensure all levels are captured initially.
    logger.setLevel(logging.DEBUG)

    # Configures the console output to show only INFO and above.
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))

    # Configures the file output to capture everything from DEBUG upwards.
    file_handler = logging.FileHandler("e4a11.log", mode="w")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

    # Attaches both handlers to the logger to enable simultaneous output to different targets.
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

    # Executes a valid division to verify INFO logging.
    calculateDivision(10, 2)
    # Executes an invalid division to verify ERROR/exception logging.
    calculateDivision(5, 0)

if __name__ == "__main__":
    runExercise()
