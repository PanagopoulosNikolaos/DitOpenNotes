"""Generates truth tables for propositional logic expressions.

Evaluates truth values of logical formulas across all 2^N valuations
of Boolean variables.
"""

import itertools
from typing import List, Dict, Callable


def generate_truth_table(variables: List[str], expression_name: str, eval_fn: Callable[[Dict[str, bool]], bool]) -> None:
    """Prints a formatted truth table for a given Boolean function.

    Args:
        variables (List[str]): List of variable names (e.g., ['p', 'q', 'r']).
        expression_name (str): Label of the proposition formula.
        eval_fn (Callable[[Dict[str, bool]], bool]): Function taking a variable-assignment
            dictionary and returning a Boolean truth value.

    Returns:
        None: Outputs the formatted truth table to stdout.
    """
    header = " | ".join(f"{var:^3}" for var in variables) + f" | {expression_name:^18}"
    separator = "-" * len(header)
    print(separator)
    print(header)
    print(separator)

    combinations = list(itertools.product([True, False], repeat=len(variables)))
    for combo in combinations:
        assignment = dict(zip(variables, combo))
        result = eval_fn(assignment)
        row = " | ".join(f"{'T' if assignment[v] else 'F':^3}" for v in variables)
        row += f" | {'T' if result else 'F':^18}"
        print(row)
    print(separator)


def implies(p: bool, q: bool) -> bool:
    """Computes logical implication: p -> q.

    Args:
        p (bool): Antecedent.
        q (bool): Consequent.

    Returns:
        bool: True unless p is True and q is False.
    """
    return (not p) or q


def iff(p: bool, q: bool) -> bool:
    """Computes logical equivalence (biconditional): p <-> q.

    Args:
        p (bool): First operand.
        q (bool): Second operand.

    Returns:
        bool: True if both operands have identical truth values.
    """
    return p == q


def main() -> None:
    """Executes truth table generation for standard logic formulas."""
    print("Truth Table 1: De Morgan Law verification: not (p and q) <-> (not p or not q)")
    generate_truth_table(
        variables=["p", "q"],
        expression_name="not(p & q) <-> not p | not q",
        eval_fn=lambda env: iff(not (env["p"] and env["q"]), (not env["p"]) or (not env["q"]))
    )

    print("\nTruth Table 2: Modus Ponens: ((p -> q) and p) -> q")
    generate_truth_table(
        variables=["p", "q"],
        expression_name="((p->q) & p) -> q",
        eval_fn=lambda env: implies(implies(env["p"], env["q"]) and env["p"], env["q"])
    )


if __name__ == "__main__":
    main()
