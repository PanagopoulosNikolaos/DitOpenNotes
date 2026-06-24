import pytest


def hammingDistance(s, t):
    """
    Computes the Hamming distance between two strings.

    Args:
        s (str): The first string for comparison.
        t (str): The second string for comparison.

    Returns:
        int: Number of mismatching characters or -1 if lengths differ.
    """
    # Verifies that both strings have equal lengths for character comparison.
    if len(s) != len(t):
        return -1
    
    mismatch_count = 0
    # Compares each character at the same index in the provided strings.
    for i in range(len(s)):
        # Increments mismatch counter when characters do not align.
        if s[i] != t[i]:
            mismatch_count += 1
            
    return mismatch_count


def test_HD():
    """
    Test suite for Hamming distance using the pytest framework.

    Each assertion verifies a specific string comparison scenario including 
    identical strings, unequal lengths, and completely different contents.
    """
    # The function name includes 'test_' to comply with pytest's discovery tool.
    assert hammingDistance("G", "") == -1
    assert hammingDistance("", "G") == -1
    assert hammingDistance("G", "A") == 1
    assert hammingDistance("G", "G") == 0
    assert hammingDistance("GA", "GA") == 0
    assert hammingDistance("GA", "AG") == 2
    assert hammingDistance("AGCT", "AGCT") == 0
    assert hammingDistance("AGCT", "TCGA") == 4
    assert hammingDistance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") == 7


if __name__ == "__main__":
    # Provides local entry point for executing the test file via pytest.
    pytest.main([__file__])
