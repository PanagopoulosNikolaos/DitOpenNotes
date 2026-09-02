def reverseTextWithoutSpaces():
    """
    Accepts text from the user and returns it reversed and without spaces.

    This function prompts the user for a text input, removes all whitespace 
    characters including standard spaces, and then returns a reversed string  
    literal of the modification.
    """
    # Prompts the user to provide a text string for processing.
    user_text = input("Enter text: ")

    # Replaces all single space characters with an empty string to remove spaces.
    text_no_spaces = user_text.replace(" ", "")

    # Reverses the processed string using slicing with a negative step.
    reversed_text = text_no_spaces[::-1]

    # Displays the final string on the console.
    print(reversed_text)


if __name__ == "__main__":
    reverseTextWithoutSpaces()
