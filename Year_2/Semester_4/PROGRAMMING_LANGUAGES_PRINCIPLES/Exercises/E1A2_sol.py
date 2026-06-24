def countWordLengths():
    """
    Counts and prints the character length of each word in a predefined string.

    The string is 'How I want a drink alcoholic of course after the heavy 
    lectures involving quantum mechanics'. The function splits it by 
    whitespace and prints each word's length.
    """
    target_text = "How I want a drink alcoholic of course after the heavy lectures involving quantum mechanics"
    
    # Splits the string at whitespace boundaries and iterates through the resulting list.
    for word in target_text.split():
        # Prints each word followed by its numeric character count.
        print(f"{word}: {len(word)}")


if __name__ == "__main__":
    countWordLengths()
