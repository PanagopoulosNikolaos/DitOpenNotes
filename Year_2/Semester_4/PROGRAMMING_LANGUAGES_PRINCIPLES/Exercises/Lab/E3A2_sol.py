import os
import re
import unittest


def loadTextContext(filepath):
    """
    Reads the specified lines from the source text file to prepare for analysis.

    The first paragraph is context-extracted (lines 46 to 52) to match the
    70-word unique word requirement.

    Args:
        filepath (str): The absolute or relative path to the text file.

    Returns:
        str: The extracted lowercase text content.
    """
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return ""

    with open(filepath, "r", encoding="utf-8") as f:
        a_list = f.readlines()

    # Isolate the segment corresponding to the first paragraph of the narrative.
    # Lines 46-52 in 1-indexing correspond to indices 45-52 in 0-indexed slicing.
    raw_text = "".join(a_list[45:52])
    return raw_text.lower()


# Initialise the context text globally as per the requirement structure.
TEXT_CONTEXT = loadTextContext(os.path.join(os.path.dirname(__file__), "metamorphosis.txt"))


def q1():
    """
    Calculates the total number of unique lowercase alphabetical words.

    Args:
        None

    Returns:
        int: The count of unique words in the text.
    """
    results = re.findall(r"\b[a-z]+\b", TEXT_CONTEXT)
    return len(set(results))


def q1Alt1():
    """
    Alternative implementation for counting unique words using pre-compiled regex.

    Args:
        None

    Returns:
        int: The count of unique words.
    """
    pattern = re.compile(r"\b[a-z]+\b")
    results = pattern.findall(TEXT_CONTEXT)
    return len(set(results))


def q1Alt2():
    """
    Alternative implementation for counting unique words using the iter tool.

    Args:
        None

    Returns:
        int: The count of unique words.
    """
    pattern = re.compile(r"\b[a-z]+\b")
    results = set()
    for x in pattern.finditer(TEXT_CONTEXT):
        results.add(x.group(0))
    return len(results)


def q2():
    """
    Identifies unique words starting with 'h' and ending with 'e'.

    Args:
        None

    Returns:
        int: The count of unique words matching the pattern.
    """
    # Regex \bh matches start of word 'h', [a-z]* internal chars, and 'e\b' the end.
    results = re.findall(r"\bh[a-z]*e\b", TEXT_CONTEXT)
    return len(set(results))


def q3():
    """
    Identifies unique words consisting of exactly 5 characters.

    Args:
        None

    Returns:
        int: The count of unique 5-letter words.
    """
    # [a-z]{5} isolates character sequences of the specific length.
    results = re.findall(r"\b[a-z]{5}\b", TEXT_CONTEXT)
    return len(set(results))


def q4():
    """
    Identifies unique words containing the consecutive substring 'as'.

    Args:
        None

    Returns:
        int: The count of unique words containing 'as'.
    """
    # Matches any word boundary followed by optional letters and the literal sequence 'as'.
    results = re.findall(r"\b[a-z]*as[a-z]*\b", TEXT_CONTEXT)
    return len(set(results))


def q5():
    """
    Identifies unique words containing 'as' or 'sa' consecutively.

    Args:
        None

    Returns:
        int: The count of unique words matching the permutation criteria.
    """
    # Matches words containing 'as' or those starting with any letters but finishing with 'sa'.
    results = re.findall(r"\b[a-z]*as|sa[a-z]*\b", TEXT_CONTEXT)
    return len(set(results))


def q6():
    """
    Identifies unique words starting and ending with the same character.

    Args:
        None

    Returns:
        int: The count of unique matching multi-character words.
    """
    # Uses backreferences to compare the first character group to the end of the word.
    results = re.findall(r"\b([a-z])([a-z]*\1)\b", TEXT_CONTEXT)
    results = [x[0] + x[1] for x in results]
    return len(set(results))


def q7():
    """
    Identifies unique words starting and ending with the same two characters.

    Args:
        None

    Returns:
        int: The count of unique words with matching character-pair bookends.
    """
    # {2} isolates the starting pair; the backreference \1 ensures the end matches.
    results = re.findall(r"\b([a-z]{2})([a-z]*\1)\b", TEXT_CONTEXT)
    results = [x[0] + x[1] for x in results]
    return len(set(results))


class TestReExamples(unittest.TestCase):
    """
    Verifies the accuracy of all text analysis functions against the source text.
    """

    def test_q1(self):
        """Validates unique word count across different implementation methods."""
        self.assertEqual(q1(), 70)
        self.assertEqual(q1Alt1(), 70)
        self.assertEqual(q1Alt2(), 70)

    def test_q2(self):
        """Validates 'h...e' word count."""
        self.assertEqual(q2(), 2)

    def test_q3(self):
        """Validates specific word length count."""
        self.assertEqual(q3(), 12)

    def test_q4(self):
        """Validates 'as' substring count."""
        self.assertEqual(q4(), 2)

    def test_q5(self):
        """Validates 'as' or 'sa' permutation count."""
        self.assertEqual(q5(), 3)

    def test_q6(self):
        """Validates start/end character match count."""
        self.assertEqual(q6(), 3)

    def test_q7(self):
        """Validates start/end pair match count."""
        self.assertEqual(q7(), 1)


if __name__ == "__main__":
    unittest.main()
