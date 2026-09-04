"""Demonstrates truth table evaluation and boolean satisfiability checking."""

import itertools
from typing import Callable, List, Dict, Tuple


class TruthTableEvaluator:
    """Evaluates propositional logic formulas over all truth assignments.
    
    Generates truth tables, classifies formulas as tautologies,
    contradictions, or contingencies, and identifies satisfying models.
    """

    def __init__(self, variables: List[str]) -> None:
        """Initializes the evaluator with an ordered list of variable names.
        
        Args:
            variables (List[str]): Identifiers for propositional variables.
        """
        self.variables = sorted(list(set(variables))) # Normalizes unique symbols

    def generateAssignments(self) -> List[Dict[str, bool]]:
        """Generates all binary truth assignments for the variable set.
        
        Returns:
            List[Dict[str, bool]]: Sequence of variable-to-truth-value mappings.
        """
        assignments: List[Dict[str, bool]] = []
        n_vars = len(self.variables)

        for combo in itertools.product([False, True], repeat=n_vars):
            assignment = dict(zip(self.variables, combo))
            assignments.append(assignment) # Appends each boolean configuration

        return assignments

    def evaluateFormula(
        self, 
        formula: Callable[[Dict[str, bool]], bool]
    ) -> List[Tuple[Dict[str, bool], bool]]:
        """Evaluates a propositional function over all valuation assignments.
        
        Args:
            formula (Callable[[Dict[str, bool]], bool]): Boolean evaluation function.
            
        Returns:
            List[Tuple[Dict[str, bool], bool]]: Table of assignments paired with results.
        """
        table: List[Tuple[Dict[str, bool], bool]] = []
        for assignment in self.generateAssignments():
            result = formula(assignment)
            table.append((assignment, result))
        return table

    def classifyFormula(
        self, 
        formula: Callable[[Dict[str, bool]], bool]
    ) -> str:
        """Classifies the semantic character of a propositional formula.
        
        Args:
            formula (Callable[[Dict[str, bool]], bool]): Boolean evaluation function.
            
        Returns:
            str: Classification label ('Tautology', 'Contradiction', or 'Contingency').
        """
        evaluations = [res for _, res in self.evaluateFormula(formula)]
        all_true = all(evaluations)
        none_true = not any(evaluations)

        if all_true:
            return "Tautology"
        if none_true:
            return "Contradiction"
        return "Contingency"


def implication(p: bool, q: bool) -> bool:
    """Computes material implication p -> q.
    
    Args:
        p (bool): Antecedent value.
        q (bool): Consequent value.
        
    Returns:
        bool: False iff p is True and q is False.
    """
    return (not p) or q


def main() -> None:
    """Runs demonstration of formula classification and truth table generation."""
    evaluator = TruthTableEvaluator(["p", "q"])

    # Formula: (p -> q) <-> (~p \/ q)
    def lawEquivalence(vals: Dict[str, bool]) -> bool:
        p_val = vals["p"]
        q_val = vals["q"]
        lhs = implication(p_val, q_val)
        rhs = (not p_val) or q_val
        return lhs == rhs

    classification = evaluator.classifyFormula(lawEquivalence)
    print(f"Formula: (p -> q) <-> (~p \\/ q) is a {classification}\n")

    print(f"{'p':<6}{'q':<6}{'Result':<6}")
    print("-" * 18)
    for assignment, result in evaluator.evaluateFormula(lawEquivalence):
        p_str = str(assignment["p"])
        q_str = str(assignment["q"])
        res_str = str(result)
        print(f"{p_str:<6}{q_str:<6}{res_str:<6}")


if __name__ == "__main__":
    main()
