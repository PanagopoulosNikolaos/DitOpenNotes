import re
import unittest
import os


def validatePasswordsPartA(input_path):
    """
    Counts valid passwords according to the character-frequency rule (Part A).

    The rule states that the character 'c' must appear between x and y times.
    Example line: 1-3 a: abcde (1 to 3 'a's allowed).

    Args:
        input_path (str): The location of the input data file.

    Returns:
        int: The number of valid passwords in the file.
    """
    valid_count = 0

    if not os.path.exists(input_path):
        return 0

    with open(input_path, "r", encoding="utf-8") as f:
        # Each line consists of frequency bounds, character, and text.
        for line in f:
            # Matches x-y c: password.
            match = re.match(r"(\d+)-(\d+)\s+(\w):\s+(\w+)", line)
            if match:
                x_min = int(match.group(1))
                y_max = int(match.group(2))
                char = match.group(3)
                password = match.group(4)

                # Counts literal occurrences of the target character.
                freq = password.count(char)
                if x_min <= freq <= y_max:
                    valid_count += 1

    return valid_count


def validatePasswordsPartB(input_path):
    """
    Counts valid passwords according to the positional rule (Part B).

    The rule requires the character 'c' to appear at either position x OR position y.
    Positions are 1-indexed. Exclusive-OR condition: exactly one position must match.

    Args:
        input_path (str): The location of the input data file.

    Returns:
        int: The number of valid passwords in the file.
    """
    valid_count = 0

    if not os.path.exists(input_path):
        return 0

    with open(input_path, "r", encoding="utf-8") as f:
        for line in f:
            match = re.match(r"(\d+)-(\d+)\s+(\w):\s+(\w+)", line)
            if match:
                pos1 = int(match.group(1))
                pos2 = int(match.group(2))
                char = match.group(3)
                password = match.group(4)

                # Validates positional presence using XOR logic.
                # Adjusts for 1-indexed positions provided in source.
                cond1 = (pos1 <= len(password)) and (password[pos1 - 1] == char)
                cond2 = (pos2 <= len(password)) and (password[pos2 - 1] == char)

                if cond1 ^ cond2: # Performs logical XOR to ensure only one position matches.
                    valid_count += 1

    return valid_count


class TestPasswords(unittest.TestCase):
    """
    Verifies the password validation logic.

    Uses specific input file data to ensure the results match expected counts (660 and 530).
    """

    def test_part_a(self):
        """Validates that exactly 660 passwords pass the Part A criteria."""
        path = "aoc2020_d2_input.txt"
        if os.path.exists(path):
            self.assertEqual(validatePasswordsPartA(path), 660)
        else:
            print(f"Skipping test_part_a: {path} not found.")

    def test_part_b(self):
        """Validates that exactly 530 passwords pass the Part B criteria."""
        path = "aoc2020_d2_input.txt"
        if os.path.exists(path):
            self.assertEqual(validatePasswordsPartB(path), 530)
        else:
            print(f"Skipping test_part_b: {path} not found.")


if __name__ == "__main__":
    unittest.main()
