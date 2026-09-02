from ortools.sat.python import cp_model


def solveNQueens(n: int) -> None:
    """
    Solves the N-Queens puzzle using OR-Tools CP-SAT.

    Places N queens on an N x N chessboard such that no two queens
    threaten each other.

    Args:
        n (int): The size of the chessboard and the number of queens.
    """
    model = cp_model.CpModel()

    # Creates decision variables: queens[i] is the row index of the queen in column i.
    queens = [model.new_int_var(0, n - 1, f"queen_{i}") for i in range(n)]

    # Enforces that all queens must be in distinct rows.
    model.add_all_different(queens)

    # Enforces that all queens must be on distinct positive and negative diagonals.
    model.add_all_different([queens[i] + i for i in range(n)])
    model.add_all_different([queens[i] - i for i in range(n)])

    solver = cp_model.CpSolver()
    status = solver.solve(model)

    # Renders the board if a valid placement is found.
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        board = [["." for _ in range(n)] for _ in range(n)]
        for col in range(n):
            row = solver.value(queens[col])
            board[row][col] = "Q"

        for row_cells in board:
            print(" ".join(row_cells))
    else:
        print("No solution found.")


if __name__ == "__main__":
    solveNQueens(8)
