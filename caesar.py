"""
  Encrypts the text using the Caesar Cipher algorithm, preserving the case of the letters.

  Parameters:
  - text (str): The text to be encrypted.
  - shiftnumber (int): The number of positions to shift the letters in the alphabet.

  Returns:
  - str: The encrypted text.

  Description:
  This function encrypts the given text using the Caesar Cipher algorithm while preserving the case of the letters.
  It shifts each letter in the text by the specified number of positions in the alphabet, considering whether
  the letter is uppercase or lowercase. Non-alphabetic characters remain unchanged.
  """


my_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def encrypt(text, shiftnumber):
    # Variable to store the final encrypted result
    final_result = ""

    # Loop through each character in the text
    for letter in text:
        if letter.isalpha():  # Check if the character is alphabetic
            # Find the alphabetic position of the letter (case insensitive)
            fn = my_letters.index(letter.capitalize())
            # Find the new position of the shifted letter
            ln = (fn + shiftnumber) % 26
            # Add the new letter to the final result
            final_result += my_letters[ln]
        else:
            # Add non-alphabetic characters as they are
            final_result += letter

    return final_result

def decrypt(text, shiftnumber):
    # Variable to store the final decrypted result
    decrypted_result = ""

    # Loop through each character in the text
    for letter in text:
        if letter.isalpha():  # Check if the character is alphabetic
            # Find the alphabetic position of the letter (case insensitive)
            fn = my_letters.index(letter.capitalize())
            # Find the original position of the shifted letter
            ln = (fn - shiftnumber) % 26
            # Add the new letter to the final result
            decrypted_result += my_letters[ln]
        else:
            # Add non-alphabetic characters as they are
            decrypted_result += letter

    return decrypted_result

def encryptascii(text, shiftnumber):
    # Variable to store the final encrypted result
    final_result = ""
    # Optimize the shift number by taking the modulo 26
    shiftnumber = shiftnumber % 26

    # Loop through each character in the text
    for letter in text:
        if letter.isalpha():  # Check if the character is alphabetic
            if (ord(letter.lower()) + shiftnumber) > ord('z'):
                # If the letter exceeds 'z'
                fn = ((ord(letter.lower()) - 26) + shiftnumber)
            else:
                fn = (ord(letter.lower()) + shiftnumber)
            # Find the new letter
            ln = chr(fn)
            # Add the new letter to the final result
            final_result += ln
        else:
            # Add non-alphabetic characters as they are
            final_result += letter

    return final_result

def decryptascii(text, shiftnumber):
    # Variable to store the final decrypted result
    decrypted_result = ""
    # Optimize the shift number by taking the modulo 26
    shiftnumber = shiftnumber % 26

    # Loop through each character in the text
    for letter in text:
        if letter.isalpha():  # Check if the character is alphabetic
            if (ord(letter.lower()) - shiftnumber) < ord('a'):
                # If the letter goes below 'a'
                fn = ((ord(letter.lower()) + 26) - shiftnumber)
            else:
                fn = (ord(letter.lower()) - shiftnumber)
            # Find the new letter
            ln = chr(fn)
            # Add the new letter to the final result
            decrypted_result += ln
        else:
            # Add non-alphabetic characters as they are
            decrypted_result += letter

    return decrypted_result

def encryptupperlower(text, shiftnumber):
    # Variable to store the final encrypted result
    final_result = ""

    # Loop through each character in the text
    for letter in text:
        if letter.isalpha():  # Check if the character is alphabetic
            if letter.islower():  # If it's a lowercase letter
                alphabet_start = ord('a')
            else:  # If it's an uppercase letter
                alphabet_start = ord('A')
            # Find the new position of the shifted letter
            fn = (ord(letter) - alphabet_start + shiftnumber) % 26
            # Find the new letter
            ln = chr(fn + alphabet_start)
            # Add the new letter to the final result
            final_result += ln
        else:
            # Add non-alphabetic characters as they are
            final_result += letter

    return final_result

def decryptupperlower(text, shiftnumber):
    # Variable to store the final decrypted result
    decrypted_result = ""

    # Loop through each character in the text
    for letter in text:
        if letter.isalpha():  # Check if the character is alphabetic
            if letter.islower():  # If it's a lowercase letter
                alphabet_start = ord('a')
            else:  # If it's an uppercase letter
                alphabet_start = ord('A')
            # Find the original position of the shifted letter
            fn = (ord(letter) - alphabet_start - shiftnumber) % 26
            # Find the new letter
            ln = chr(fn + alphabet_start)
            # Add the new letter to the final result
            decrypted_result += ln
        else:
            # Add non-alphabetic characters as they are
            decrypted_result += letter

    return decrypted_result

# Getting input from the user
text = input("Enter the text to be encrypted or decrypted: ")
shiftnumber = int(input("Enter the shift number: "))
print("Encrypted text:", encrypt(text, shiftnumber))
print("Encrypted text (ASCII):", encryptascii(text, shiftnumber))
print("Encrypted text (Upper and Lower case):", encryptupperlower(text, shiftnumber))
print("Decrypted text:", decrypt(text, shiftnumber))
print("Decrypted text (ASCII):", decryptascii(text, shiftnumber))
print("Decrypted text (Upper and Lower case):", decryptupperlower(text, shiftnumber))
