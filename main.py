# Include all printable characters for encryption
import string

# Extended character set including letters, digits, and special symbols
alphabet = list(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation + " ")

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_amount) % len(alphabet)
            end_text += alphabet[new_position]
        else:
            # If character is not in the alphabet, add it unchanged
            end_text += char
    print(f"\nHere's the {cipher_direction}d result: {end_text}\n")

# Logo for fun (optional)
logo = """
  _____                          _               
 / ____|                        | |              
| |     ___  _ __  ___  ___  ___| |__   ___ _ __ 
| |    / _ \| '_ \/ __|/ _ \/ __| '_ \ / _ \ '__|
| |___| (_) | | | \__ \  __/ (__| | | |  __/ |   
 \_____\___/|_| |_|___/\___|\___|_| |_|\___|_|   
"""
print(logo)

# Main program loop
should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction not in ["encode", "decode"]:
        print("Invalid choice. Please type 'encode' or 'decode'.")
        continue

    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))

    # Ensure shift is within the range of the character set
    shift = shift % len(alphabet)

    # Call the Caesar cipher function
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()
    if restart == "no":
        should_end = True
        print("Goodbye!")
