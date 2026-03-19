import re


def findPhoneNumbersStartingWithJ(filepath):
    """
    Finds phone numbers in entries that contain a word starting with 'J'.

    The function scans each line for any alphabetical word beginning with 'J'.
    If found, it considers the phone number from that line a match.

    Args:
        filepath (str): Path to 'simpsons_phone_book.txt'.

    Returns:
        list (str): A list of identifying phone numbers for matching names.
    """
    matches = []
    try:
        with open(filepath, "r") as f:
            for line in f:
                # \bJ\w* searches for alphabetical characters starting with 'J'.
                if re.search(r"\bJ\w*", line):
                    # Identifies phone numbers following typical formats (e.g., 555-1234).
                    phone_match = re.search(r"[\d\w-]{7,}", line)
                    if phone_match:
                        matches.append(phone_match.group(0))
    except FileNotFoundError:
        print(f"File {filepath} not found.")

    return matches


def findPhoneNumbersEndingWithEu(filepath):
    """
    Finds phone numbers in entries containing a word ending with 'eu'.

    Args:
        filepath (str): The name of the file to search.

    Returns:
        list (str): Match results for words with the 'eu' suffix.
    """
    matches = []
    try:
        with open(filepath, "r") as f:
            for line in f:
                # Matches words where 'eu' occurs before a word boundary or space.
                if re.search(r"\w*eu\b", line):
                    phone_match = re.search(r"[\d\w-]{7,}", line)
                    if phone_match:
                        matches.append(phone_match.group(0))
    except FileNotFoundError:
        pass

    return matches


def findPhoneNumbersWithLetters(filepath):
    """
    Identifies phone numbers that contain alphabetical characters.

    Args:
        filepath (str): The name of the file to process.

    Returns:
        list (str): Phonetic digits containing letters (e.g., 555-FLOWER).
    """
    matches = []
    try:
        with open(filepath, "r") as f:
            for line in f:
                # Extracts the phone number section and checks for [a-zA-Z].
                phone_candidate = re.search(r"[\d\w-]{7,}", line)
                if phone_candidate and re.search(r"[a-zA-Z]", phone_candidate.group(0)):
                    matches.append(phone_candidate.group(0))
    except FileNotFoundError:
        pass

    return matches


def listSortedLocalPhoneNumbers(filepath):
    """
    Extracts phone numbers without the '555' area code and returns them sorted.

    Args:
        filepath (str): The phone book file location.

    Returns:
        list (str): Sorted local phone numbers in xxxx-xxxx format.
    """
    local_numbers = []
    try:
        with open(filepath, "r") as f:
            for line in f:
                # Searches for numbers containing '555' as the area code.
                phone_match = re.search(r"555-([\d\w-]+)", line)
                if phone_match:
                    local_numbers.append(phone_match.group(1))

    except FileNotFoundError:
        pass

    # Orders the extracted local segments lexicographically.
    local_numbers.sort()
    return local_numbers


def runExercises():
    """
    Executes all defined phone book analysis tasks and prints the results.
    """
    filename = "simpsons_phone_book.txt"

    print("\n--- Simpson's Phone Book Analysis ---")

    print("\n1. Phone numbers for entries starting with 'J':")
    print(findPhoneNumbersStartingWithJ(filename))

    print("\n2. Phone numbers for words ending in 'eu':")
    print(findPhoneNumbersEndingWithEu(filename))

    print("\n3. Phone numbers containing letters:")
    print(findPhoneNumbersWithLetters(filename))

    print("\n4. Sorted numbers without '555' area code:")
    results = listSortedLocalPhoneNumbers(filename)
    for num in results:
        print(num)


if __name__ == "__main__":
    runExercises()
