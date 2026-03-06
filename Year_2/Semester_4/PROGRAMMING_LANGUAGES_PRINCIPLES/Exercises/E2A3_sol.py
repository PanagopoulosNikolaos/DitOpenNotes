import unittest


def longestWords(s):
    """
    Finds and returns the maximum length words in a string.

    The function removes dots and commas, identifies the longest words, 
    and returns them in ascending alphanumeric order.

    Args:
        s (str): The text or string to process.

    Returns:
        list: All words of the maximum length found in the string.
    """
    # Strips all punctuation marks specifically requested from the input text.
    cleaned_input = s.replace(".", " ").replace(",", " ")
    
    # Splits the cleaned text into individual words for length evaluation.
    word_list = cleaned_input.split()

    # Returns an empty list if the input text contains no words.
    if not word_list:
        return []

    # Identifies the maximum word length present in the current text sequence.
    max_len = max(len(word) for word in word_list)

    # Identifies all words whose character count matches the maximum length.
    result_words = [word for word in word_list if len(word) == max_len]
    
    final_result = sorted(result_words)
    
    return final_result


class TestLongestWords(unittest.TestCase):
    """
    Unit tests for a function extracting longest words from text.
    """

    def test(self):
        """
        Tests the functionality with various string patterns and punctuations.
        """
        s1 = ""
        self.assertEqual(longestWords(s1), [])
        s2 = "arta"
        self.assertEqual(longestWords(s2), ["arta"])
        s3 = "arta Άρτα"
        self.assertEqual(longestWords(s3), ["arta", "Άρτα"])
        s4 = "....arta,,, Άρτα....."
        self.assertEqual(longestWords(s4), ["arta", "Άρτα"])
        s5 = "ab,,cd..ef gh.."
        self.assertEqual(longestWords(s5), ["ab", "cd", "ef", "gh"])
        s6 = """Το Lorem Ipsum είναι απλά ένα κείμενο χωρίς νόημα για τους επαγγελματίες της τυπογραφίας και στοιχειοθεσίας Το Lorem Ipsum είναι το επαγγελματικό πρότυπο όσον αφορά το κείμενο χωρίς νόημα, από τον 15ο αιώνα, όταν ένας ανώνυμος τυπογράφος πήρε ένα δοκίμιο και ανακάτεψε τις λέξεις για να δημιουργήσει ένα δείγμα βιβλίου Όχι μόνο επιβίωσε πέντε αιώνες αλλά κυριάρχησε στην ηλεκτρονική στοιχειοθεσία παραμένοντας με κάθε τρόπο αναλλοίωτο Έγινε δημοφιλές τη δεκαετία του '60 με την έκδοση των δειγμάτων της Letraset όπου περιελάμβαναν αποσπάσματα του Lorem Ipsum και πιο πρόσφατα με το λογισμικό ηλεκτρονικής σελιδοποίησης όπως το Aldus PageMaker που περιείχαν εκδοχές του Lorem Ipsum"""
        self.assertEqual(longestWords(s6), ["στοιχειοθεσίας"])
        s7 = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
        self.assertEqual(longestWords(s7), ["reprehenderit"])


if __name__ == "__main__":
    unittest.main()
