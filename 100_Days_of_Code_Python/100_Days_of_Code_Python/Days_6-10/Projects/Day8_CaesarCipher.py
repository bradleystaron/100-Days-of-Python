alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount    # Gets the alphabet's index for each letter of the original text and adds the shift amount
        shifted_position = shifted_position % len(alphabet)         # To prevent index out of range error
        cipher_text += alphabet[shifted_position]                   # Finally, adds the letter from the shifted position of the alphabet list

    print(f"Here is the encoded result: {cipher_text}")

def decrypt(original_text, shift_amount):
    decrypted_message = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) - shift_amount
        shifted_position = shifted_position % len(alphabet)
        decrypted_message += alphabet[shifted_position]

    print(f"Here is the decrypted result: {decrypted_message}")


def caesar(coding_direction, original_text, shift_amount):
    if coding_direction == "encode":
        encrypt(original_text, shift_amount)
    
    elif coding_direction == "decode":
        decrypt(original_text, shift_amount)
    
    elif coding_direction != "encode" or "decode":
        print(f"{direction} is not a valid option, try again")

caesar(coding_direction=direction, original_text=text, shift_amount=shift)