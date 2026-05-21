from functools import reduce


def runExercise() -> None:
    """
    Computes order statistics and performs operations on a list of product orders.
    """
    # Sample orders data containing (order_id, product, price_per_unit, quantity).
    orders = [
        ("A101", "laptop", 1200, 1),
        ("A102", "mouse", 25, 2),
        ("A103", "keyboard", 75, 1),
        ("A104", "monitor", 300, 2),
        ("A105", "laptop", 1100, 1),
        ("A106", "mouse", 20, 3),
        ("A107", "monitor", 280, 1)
    ]

    # Computes the total value of each order by multiplying unit price and quantity.
    order_totals = list(map(
        lambda o: (o[0], o[1], o[2] * o[3]),
        orders
    ))

    print("Συνολική αξία κάθε παραγγελίας:")
    print(order_totals)

    # Filters out orders whose total value is less than or equal to 100 euros.
    orders_over_100 = list(filter(
        lambda o: o[2] > 100,
        order_totals
    ))

    print("\nΠαραγγελίες άνω των 100 ευρώ:")
    print(orders_over_100)

    # Aggregates order IDs grouped by product type.
    orders_by_product = reduce(
        lambda acc, o: {
            **acc,
            o[1]: acc.get(o[1], []) + [o[0]]
        },
        orders,
        {}
    )

    print("\nOrder IDs ανά προϊόν:")
    print(orders_by_product)

    # Aggregates total revenue for each unique product.
    revenue_by_product = reduce(
        lambda acc, o: {
            **acc,
            o[1]: acc.get(o[1], 0) + o[2] * o[3]
        },
        orders,
        {}
    )

    # Sorts the products in descending order based on their generated revenue.
    sorted_products = sorted(
        revenue_by_product.items(),
        key=lambda x: x[1],
        reverse=True
    )

    print("\nΠροϊόντα κατά συνολική αξία φθίνουσα:")
    print(sorted_products)

    # Identifies the single product with the highest total revenue.
    top_product = reduce(
        lambda a, b: a if a[1] > b[1] else b,
        sorted_products
    )

    print("\nΠροϊόν με τα μεγαλύτερα συνολικά έσοδα:")
    print(top_product)


if __name__ == "__main__":
    runExercise()
