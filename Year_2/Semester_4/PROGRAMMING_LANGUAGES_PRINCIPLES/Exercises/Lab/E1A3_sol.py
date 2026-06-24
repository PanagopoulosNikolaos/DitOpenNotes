def calculateGeometricSum():
    """
    Computes a geometric sum of form 1 + 1/2 + 1/4 + ... for n terms.

    Uses defensive programming to ensure the user provides a valid non-negative 
    integer. The sum is calculated by iterating from 0 up to n-1 and adding 
    2 to the power of negative i to the running total.
    """
    while True:
        try:
            # Prompts the user for a non-negative integer representing term count.
            user_input = input("Enter the number of terms (non-negative integer): ")
            term_count = int(user_input)
            
            # Validates that the input integer value is not negative.
            if term_count < 0:
                print("Error: Please enter a non-negative value.")
                continue
            break
        except ValueError:
            # Notifies the user when non-numeric or floating point values are input.
            print("Error: Input is not a valid integer. Please try again.")

    current_sum = 0.0
    # Calculates the sum for the provided number of terms by increasing powers of two.
    for i in range(term_count):
        current_sum += (1 / (2**i))

    # Displays the final calculated sum to the user.
    print(f"Sum of {term_count} terms: {current_sum}")


if __name__ == "__main__":
    calculateGeometricSum()
