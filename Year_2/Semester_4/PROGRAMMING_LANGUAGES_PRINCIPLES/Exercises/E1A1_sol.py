import math


def calculateMathResults():
    """
    Calculates the first 10 digits of a complex mathematical formula.

    This function computes the square root of 2^101 divided by the sum of pi^53 and 11^7.
    It prints the full numerical result and then extracts the first 10 digits by removing 
    the decimal point from the string representation.
    """
    # Computes the square root of the expression to achieve the base numerical value.
    result_value = math.sqrt(2**101 / (math.pi**53 + 11**7))

    # Displays the complete numeric result for direct inspection.
    print(result_value)

    # Processes the result into a string and removes decimal symbols for digit extraction.
    digit_string = str(result_value).replace(".", "")
    
    # Outputs the first ten characters of the processed digit string.
    print(digit_string[:10])


if __name__ == "__main__":
    calculateMathResults()
