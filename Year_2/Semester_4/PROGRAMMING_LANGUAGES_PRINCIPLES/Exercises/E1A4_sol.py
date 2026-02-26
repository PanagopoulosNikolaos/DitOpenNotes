import string


def countZenCharacters():
    """
    Counts character frequencies for A through Z in the Zen of Python text.

    The text is provided as a multi-line string literal. The function converts 
    the text to uppercase for uniform comparison and counts each letter's  
    occurrences in the provided string.
    """
    zen_text = """
    The Zen of Python, by Tim Peters

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!
    """

    # Normalizes the string to uppercase to avoid case-sensitivity issues during search.
    upper_zen_text = zen_text.upper()

    # Iterates through each letter of the alphabet to find its total count in the string.
    for letter in string.ascii_uppercase:
        # Calculates and displays the occurrences for each English character.
        count = upper_zen_text.count(letter)
        print(f"Character {letter}: {count}")


if __name__ == "__main__":
    countZenCharacters()
