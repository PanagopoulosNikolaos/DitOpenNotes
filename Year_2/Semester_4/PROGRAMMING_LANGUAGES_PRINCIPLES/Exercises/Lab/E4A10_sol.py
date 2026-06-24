import sys
import argparse

def runExercise():
    """
    Parses command line arguments to perform sum or reverse operations.
    """
    # Initializes the argument parser with a description of its purpose.
    parser = argparse.ArgumentParser(description="Command line utility for sum and reverse.")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Configures the 'sum' command to accept multiple numeric values.
    sum_parser = subparsers.add_parser("sum", help="Sum the following numbers")
    sum_parser.add_argument("numbers", nargs="+", type=float, help="List of numbers to sum")

    # Configures the 'reverse' command to accept and invert a string.
    reverse_parser = subparsers.add_parser("reverse", help="Reverse the following text")
    reverse_parser.add_argument("text", nargs="+", help="Text to be reversed")

    # Parses the arguments provided by the user in the terminal.
    args = parser.parse_args()

    if args.command == "sum":
        # Calculates and displays the total of the numeric list.
        result = sum(args.numbers)
        print(result)
    elif args.command == "reverse":
        # Joins word fragments and reverses the resulting string.
        full_text = " ".join(args.text)
        print(full_text[::-1])
    else:
        # Displays the help message if no valid command is provided.
        parser.print_help()

if __name__ == "__main__":
    runExercise()
