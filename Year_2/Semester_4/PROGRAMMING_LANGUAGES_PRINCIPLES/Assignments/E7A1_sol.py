from ortools.sat.python import cp_model


def solveCryptarithm() -> None:
    """
    Solves the SEND + MORE = MONEY cryptarithmetic puzzle using OR-Tools.
    """
    model = cp_model.CpModel()

    # Creates variables representing individual letters, constraining leading digits to be non-zero.
    s = model.new_int_var(1, 9, "S")
    e = model.new_int_var(0, 9, "E")
    n = model.new_int_var(0, 9, "N")
    d = model.new_int_var(0, 9, "D")
    m = model.new_int_var(1, 9, "M")
    o = model.new_int_var(0, 9, "O")
    r = model.new_int_var(0, 9, "R")
    y = model.new_int_var(0, 9, "Y")

    letters = [s, e, n, d, m, o, r, y]

    # Enforces that all letter variables must take distinct digits.
    model.add_all_different(letters)

    # Encodes the algebraic relation representing SEND + MORE = MONEY.
    send_val = s * 1000 + e * 100 + n * 10 + d
    more_val = m * 1000 + o * 100 + r * 10 + e
    money_val = m * 10000 + o * 1000 + n * 100 + e * 10 + y
    model.add(send_val + more_val == money_val)

    solver = cp_model.CpSolver()
    status = solver.solve(model)

    # Displays the decoded letters and equation if a solution is successfully found.
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print(f"S={solver.value(s)}, E={solver.value(e)}, N={solver.value(n)}, D={solver.value(d)}")
        print(f"M={solver.value(m)}, O={solver.value(o)}, R={solver.value(r)}, Y={solver.value(y)}")
        send_num = solver.value(s) * 1000 + solver.value(e) * 100 + solver.value(n) * 10 + solver.value(d)
        more_num = solver.value(m) * 1000 + solver.value(o) * 100 + solver.value(r) * 10 + solver.value(e)
        money_num = solver.value(m) * 10000 + solver.value(o) * 1000 + solver.value(n) * 100 + solver.value(e) * 10 + solver.value(y)
        print(f"{send_num} + {more_num} = {money_num}")
    else:
        print("No solution found.")


if __name__ == "__main__":
    solveCryptarithm()
