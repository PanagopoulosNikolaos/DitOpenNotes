from functools import partial


def calculatePrice(price: float, quantity: int, discount: float, tax: float) -> float:
    """
    Calculates the final order price including discount and tax.

    Args:
        price (float): The unit price of the item.
        quantity (int): The number of items purchased.
        discount (float): The discount rate as a fraction (e.g., 0.10 for 10%).
        tax (float): The tax rate as a fraction (e.g., 0.24 for 24%).

    Returns:
        float: The total calculated price after applying discount and tax.
    """
    return price * quantity * (1 - discount) * (1 + tax)


def runExercise() -> None:
    """
    Demonstrates partial function application by calculating final order values.
    """
    # Pre-configures the function with a fixed tax rate of 24%.
    calculate_with_tax = partial(calculatePrice, tax=0.24)

    # Pre-configures the function with a fixed discount rate of 10%.
    calculate_with_discount = partial(calculatePrice, discount=0.10)

    # Pre-configures the function with both a 10% discount and a 24% tax rate.
    calculate_standard_order = partial(calculatePrice, discount=0.10, tax=0.24)

    print("Με σταθερό φόρο 24%:")
    print(calculate_with_tax(price=100, quantity=2, discount=0.10))

    print("\nΜε σταθερή έκπτωση 10%:")
    print(calculate_with_discount(price=100, quantity=2, tax=0.24))

    print("\nΜε σταθερό φόρο 24% και έκπτωση 10%:")
    print(calculate_standard_order(price=100, quantity=2))
    print(calculate_standard_order(price=50, quantity=5))
    print(calculate_standard_order(price=1200, quantity=1))


if __name__ == "__main__":
    runExercise()
