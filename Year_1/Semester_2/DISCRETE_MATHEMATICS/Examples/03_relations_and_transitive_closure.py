"""Demonstrates binary relation properties, equivalence classes, and transitive closure via Warshall's algorithm."""

from typing import Dict, List, Set, Tuple


class BinaryRelation:
    """Represents a binary relation over a finite set and provides analytical verification."""

    def __init__(self, elements: List[str], pairs: List[Tuple[str, str]]) -> None:
        """Initializes a binary relation over an underlying ground set.

        Args:
            elements (List[str]): Ground universe of unique elements.
            pairs (List[Tuple[str, str]]): Ordered pairs (a, b) present in the relation.
        """
        self.elements = sorted(list(set(elements))) # Eliminates duplicates and guarantees canonical ordering
        self.pairs: Set[Tuple[str, str]] = set()

        for a, b in pairs:
            if a in self.elements and b in self.elements:
                self.pairs.add((a, b)) # Discards ordered pairs with endpoints outside the universe

    def isReflexive(self) -> bool:
        """Determines whether the relation is reflexive: for all x in S, (x, x) in R.

        Returns:
            bool: True if every element is related to itself.
        """
        return all((x, x) in self.pairs for x in self.elements)

    def isSymmetric(self) -> bool:
        """Determines whether the relation is symmetric: (a, b) in R implies (b, a) in R.

        Returns:
            bool: True if reciprocity holds for all relation members.
        """
        return all((b, a) in self.pairs for (a, b) in self.pairs)

    def isAntisymmetric(self) -> bool:
        """Determines whether the relation is antisymmetric: (a, b) in R and (b, a) in R implies a == b.

        Returns:
            bool: True if no distinct elements possess mutual links.
        """
        for a, b in self.pairs:
            if a != b and (b, a) in self.pairs:
                return False # Mutual distinct pair violates antisymmetry
        return True

    def isTransitive(self) -> bool:
        """Determines whether the relation is transitive: (a, b) in R and (b, c) in R implies (a, c) in R.

        Returns:
            bool: True if two-step reachability collapses into a direct relation.
        """
        for a, b in self.pairs:
            for c, d in self.pairs:
                if b == c and (a, d) not in self.pairs:
                    return False # Found a path of length two without transitive bypass
        return True

    def isEquivalenceRelation(self) -> bool:
        """Evaluates whether the relation is an equivalence relation (reflexive, symmetric, and transitive).

        Returns:
            bool: True if all three equivalence criteria are fulfilled.
        """
        return self.isReflexive() and self.isSymmetric() and self.isTransitive()

    def isPartialOrder(self) -> bool:
        """Evaluates whether the relation is a partial order (reflexive, antisymmetric, and transitive).

        Returns:
            bool: True if all three poset criteria are fulfilled.
        """
        return self.isReflexive() and self.isAntisymmetric() and self.isTransitive()

    def getEquivalenceClasses(self) -> List[Set[str]]:
        """Partitions the underlying universe into disjoint equivalence classes.

        Returns:
            List[Set[str]]: List of distinct subsets forming the quotient partition.

        Raises:
            ValueError: If the relation is not an equivalence relation.
        """
        if not self.isEquivalenceRelation():
            raise ValueError("Equivalence classes are undefined for non-equivalence relations.")

        classes: List[Set[str]] = []
        visited: Set[str] = set()

        for x in self.elements:
            if x not in visited:
                eq_class = {y for y in self.elements if (x, y) in self.pairs}
                classes.append(eq_class)
                visited.update(eq_class) # Marks members to prevent duplicate subset emission

        return classes

    def computeReflexiveClosure(self) -> Set[Tuple[str, str]]:
        """Computes the reflexive closure R union {(x, x) for all x in S}.

        Returns:
            Set[Tuple[str, str]]: The smallest reflexive relation containing R.
        """
        closure = set(self.pairs)
        for x in self.elements:
            closure.add((x, x)) # Augments relation with missing diagonal elements
        return closure

    def computeSymmetricClosure(self) -> Set[Tuple[str, str]]:
        """Computes the symmetric closure R union {(b, a) for all (a, b) in R}.

        Returns:
            Set[Tuple[str, str]]: The smallest symmetric relation containing R.
        """
        closure = set(self.pairs)
        for a, b in self.pairs:
            closure.add((b, a)) # Appends reverse orientation for each directed pair
        return closure

    def computeTransitiveClosureWarshall(self) -> Set[Tuple[str, str]]:
        """Computes the transitive closure using Warshall's dynamic programming algorithm.

        Returns:
            Set[Tuple[str, str]]: The reachability relation computed in O(n^3) operations.
        """
        n = len(self.elements)
        index_map: Dict[str, int] = {elem: idx for idx, elem in enumerate(self.elements)}
        matrix = [[0] * n for _ in range(n)]

        # Constructs the initial boolean incidence matrix W(0)
        for a, b in self.pairs:
            matrix[index_map[a]][index_map[b]] = 1

        # Warshall's algorithm iterating through intermediate pivot vertex k
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    matrix[i][j] = matrix[i][j] or (matrix[i][k] and matrix[k][j])

        # Reconstructs pair tuples from the finalized reachability matrix W(n)
        transitive_closure: Set[Tuple[str, str]] = set()
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 1:
                    transitive_closure.add((self.elements[i], self.elements[j]))

        return transitive_closure


def main() -> None:
    """Demonstrates relation properties, equivalence class partitioning, and Warshall's closure."""
    universe = ["a", "b", "c", "d"]

    # Construct an equivalence relation with partitions {a, b} and {c, d}
    equiv_pairs = [
        ("a", "a"), ("b", "b"), ("c", "c"), ("d", "d"),
        ("a", "b"), ("b", "a"),
        ("c", "d"), ("d", "c")
    ]
    equiv_relation = BinaryRelation(universe, equiv_pairs)

    print("--- Equivalence Relation Verification ---")
    print(f"Reflexive:     {equiv_relation.isReflexive()}")
    print(f"Symmetric:     {equiv_relation.isSymmetric()}")
    print(f"Antisymmetric: {equiv_relation.isAntisymmetric()}")
    print(f"Transitive:    {equiv_relation.isTransitive()}")
    print(f"Is Equivalence: {equiv_relation.isEquivalenceRelation()}")
    print(f"Equivalence Classes: {equiv_relation.getEquivalenceClasses()}")

    # Construct a directed graph relation to compute transitive closure
    dag_pairs = [("a", "b"), ("b", "c"), ("c", "d")]
    dag_relation = BinaryRelation(universe, dag_pairs)

    print("\n--- Directed Graph Transitive Closure (Warshall's Algorithm) ---")
    print(f"Original Pairs: {sorted(list(dag_relation.pairs))}")
    print(f"Transitive:     {dag_relation.isTransitive()}")
    closure = dag_relation.computeTransitiveClosureWarshall()
    print(f"Transitive Closure ({len(closure)} pairs): {sorted(list(closure))}")


if __name__ == "__main__":
    main()

