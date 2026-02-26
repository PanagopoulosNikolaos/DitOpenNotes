import unittest


class TestComprehensions(unittest.TestCase):
    """
    Unit tests for various list comprehension operations.
    """

    def test1(self):
        """
        Creates a new list containing the digit count for each value.
        """
        a_list = [56, 37, 771, 90, 16, 11]
        
        # Calculates the length of string representation for each integer in the source list.
        b_list = [len(str(val)) for val in a_list]
        
        self.assertEqual(b_list, [2, 2, 3, 2, 2, 2])

    def test2(self):
        """
        Creates a new list with the digits of each value in reversed order.
        """
        a_list = [56, 37, 771, 90, 16, 11]
        
        # Convetrs each integer to a string, reverses it, and converts back into an integer.
        b_list = [int(str(val)[::-1]) for val in a_list]
        
        self.assertEqual(b_list, [65, 73, 177, 9, 61, 11])

    def test3(self):
        """
        Filters the list to only include values greater than the mean average.
        """
        a_list = [56, 37, 771, 90, 16, 11]
        
        # Determines the arithmetic mean of all numeric elements currently stored in the list.
        average_value = sum(a_list) / len(a_list)
        
        # Filters elements that exceed the calculated mean using a list comprehension.
        b_list = [val for val in a_list if val > average_value]
        
        self.assertEqual(b_list, [771])

    def test4(self):
        """
        Creates a list of tuples containing the value and its even/odd status.
        """
        a_list = [56, 37, 771, 90, 16, 11]
        
        # Generates pairs containing the number and a boolean reflecting its divisibility by 2.
        b_list = [(val, val % 2 == 0) for val in a_list]
        
        self.assertEqual(b_list, [(56, True), (37, False), (771, False), (90, True), (16, True), (11, False)])


if __name__ == "__main__":
    unittest.main()
