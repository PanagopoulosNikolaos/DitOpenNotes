import unittest


def hammingDistance(s, t):
    """
    Calculates the Hamming distance between two strings.

    Args:
        s (str): The first string for comparison.
        t (str): The second string for comparison.

    Returns:
        int: The number of positions at which the corresponding characters 
             are different. Returns -1 if the strings have different lengths.
    """
    # Validates that both input strings possess equal length for comparison.
    if len(s) != len(t):
        return -1

    diff_count = 0
    # Iterates through the indices of the strings to identify character mismatches.
    for i in range(len(s)):
        # Increments the counter if characters at the current index do not match.
        if s[i] != t[i]:
            diff_count += 1

    return diff_count


class TestHammingDistance(unittest.TestCase):
    """
    Unit tests for the Hamming distance calculation function.
    """

    def test_HD(self):
        """
        Executes various test cases to verify Hamming distance accuracy.
        """
        self.assertEqual(hammingDistance("G", ""), -1)
        self.assertEqual(hammingDistance("", "G"), -1)
        self.assertEqual(hammingDistance("G", "A"), 1)
        self.assertEqual(hammingDistance("G", "G"), 0)
        self.assertEqual(hammingDistance("GA", "GA"), 0)
        self.assertEqual(hammingDistance("GA", "AG"), 2)
        self.assertEqual(hammingDistance("AGCT", "AGCT"), 0)
        self.assertEqual(hammingDistance("AGCT", "TCGA"), 4)
        self.assertEqual(hammingDistance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT"), 7)


if __name__ == "__main__":
    unittest.main()
