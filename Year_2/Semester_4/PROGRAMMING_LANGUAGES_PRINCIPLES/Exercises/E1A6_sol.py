import hashlib


def findHashSuffix():
    """
    Finds a suffix number so the text's SHA256 hash ends with seven zeros.

    The function iterates through sequential integers, appending each to the 
    base string 'ΤΜΗΜΑ ΠΛΗΡΟΦΟΡΙΚΗΣ ΚΑΙ ΤΗΛΕΠΙΚΟΙΝΩΝΙΩΝ'. It calculates 
    the SHA256 hash and checks the last seven characters for zeroes.
    """
    # The base text which will be appended by an incremental value.
    base_text = "ΤΜΗΜΑ ΠΛΗΡΟΦΟΡΙΚΗΣ ΚΑΙ ΤΗΛΕΠΙΚΟΙΝΩΝΙΩΝ"
    
    # Starting value for the brute force search loop.
    suffix_value = 0

    # Continuously increments the value until a hash ending in seven zeros is found.
    while True:
        # Appends the current iteration number to the base string.
        test_string = base_text + str(suffix_value)
        
        # Generates a SHA256 hash and converts it to a hexadecimal string representation.
        # hashlib.sha256(test_string.encode()): Creates a 256-bit hash object.
        # .encode(): Converts the string into bytes required by the hash algorithm.
        # .hexdigest(): Returns the result as a human-readable hex string.
        hash_value = hashlib.sha256(test_string.encode()).hexdigest()

        # Checks whether the final seven hexadecimal characters are all zeros.
        if hash_value.endswith("0000000"):
            # Outputs the first found value that satisfies the condition.
            print(f"Found suffix number: {suffix_value}")
            print(f"Resulting hash: {hash_value}")
            break
        
        # Moves onto the next integer in the sequence.
        suffix_value += 1


if __name__ == "__main__":
    findHashSuffix()
