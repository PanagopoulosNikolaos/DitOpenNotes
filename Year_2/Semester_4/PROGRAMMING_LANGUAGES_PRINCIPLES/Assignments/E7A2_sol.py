from ortools.sat.python import cp_model


def solveMapColoring() -> None:
    """
    Solves the map coloring problem for the contiguous 48 US states.

    Assigns one of four colors to each state such that no two adjacent
    states share the same color.
    """
    states = [
        "AL", "AZ", "AR", "CA", "CO", "CT", "DE", "FL",
        "GA", "ID", "IL", "IN", "IA", "KS", "KY", "LA",
        "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT",
        "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND",
        "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN",
        "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
    ]

    edges = [
        ("AL", "FL"), ("AL", "GA"), ("AL", "MS"), ("AL", "TN"),
        ("AZ", "CA"), ("AZ", "CO"), ("AZ", "NV"), ("AZ", "NM"), ("AZ", "UT"),
        ("AR", "LA"), ("AR", "MS"), ("AR", "MO"), ("AR", "OK"), ("AR", "TN"), ("AR", "TX"),
        ("CA", "NV"), ("CA", "OR"),
        ("CO", "KS"), ("CO", "NE"), ("CO", "NM"), ("CO", "OK"), ("CO", "UT"), ("CO", "WY"),
        ("CT", "MA"), ("CT", "NY"), ("CT", "RI"),
        ("DE", "MD"), ("DE", "NJ"), ("DE", "PA"),
        ("FL", "GA"),
        ("GA", "NC"), ("GA", "SC"), ("GA", "TN"),
        ("ID", "MT"), ("ID", "NV"), ("ID", "OR"), ("ID", "UT"), ("ID", "WA"), ("ID", "WY"),
        ("IL", "IN"), ("IL", "IA"), ("IL", "KY"), ("IL", "MO"), ("IL", "WI"),
        ("IN", "KY"), ("IN", "MI"), ("IN", "OH"),
        ("IA", "MN"), ("IA", "MO"), ("IA", "NE"), ("IA", "SD"), ("IA", "WI"),
        ("KS", "MO"), ("KS", "NE"), ("KS", "OK"),
        ("KY", "MO"), ("KY", "OH"), ("KY", "TN"), ("KY", "VA"), ("KY", "WV"),
        ("LA", "MS"), ("LA", "TX"),
        ("ME", "NH"),
        ("MD", "PA"), ("MD", "VA"), ("MD", "WV"),
        ("MA", "NH"), ("MA", "NY"), ("MA", "RI"), ("MA", "VT"),
        ("MI", "OH"), ("MI", "WI"),
        ("MN", "ND"), ("MN", "SD"), ("MN", "WI"),
        ("MS", "TN"),
        ("MO", "NE"), ("MO", "OK"), ("MO", "TN"),
        ("MT", "ND"), ("MT", "SD"), ("MT", "WY"),
        ("NE", "SD"), ("NE", "WY"),
        ("NV", "OR"), ("NV", "UT"),
        ("NH", "VT"),
        ("NJ", "NY"), ("NJ", "PA"),
        ("NM", "OK"), ("NM", "TX"), ("NM", "UT"),
        ("NY", "PA"), ("NY", "VT"),
        ("NC", "SC"), ("NC", "TN"), ("NC", "VA"),
        ("ND", "SD"),
        ("OH", "PA"), ("OH", "WV"),
        ("OK", "TX"),
        ("OR", "WA"),
        ("PA", "WV"),
        ("SD", "WY"),
        ("TN", "VA"),
        ("TX", "NM"),
        ("UT", "WY"),
        ("VA", "WV")
    ]

    model = cp_model.CpModel()

    # Maps each state to an integer variable representing one of four colors.
    color_vars = {state: model.new_int_var(0, 3, state) for state in states}

    # Adds adjacency constraints enforcing that neighboring states have different colors.
    for u, v in edges:
        model.add(color_vars[u] != color_vars[v])

    solver = cp_model.CpSolver()
    status = solver.solve(model)

    # Outputs the assignment of colors to states if a feasible coloring is found.
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        color_names = ["Red", "Green", "Blue", "Yellow"]
        for state in sorted(states):
            color_id = solver.value(color_vars[state])
            print(f"{state}: {color_names[color_id]}")
    else:
        print("No feasible coloring solution found.")


if __name__ == "__main__":
    solveMapColoring()
