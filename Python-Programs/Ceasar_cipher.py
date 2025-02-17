alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def encryption(plain_text, shift_keys):
    cipher_text = ""
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_keys) % 26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char
    print(f"Here is the text after encryption: {cipher_text}")


def decryption(cipher_text, shift_keys):
    plain_text = ""
    for char in cipher_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position - shift_keys) % 26
            plain_text += alphabet[new_position]
        else:
            cipher_text += char
    print(f"Here is the text after decryption: {plain_text}")


wanna_end = False
while not wanna_end:
    what_to_do = input("Type 'encrypt' to encryption, type 'decrypt' to decryption: ")
    text = input("Enter the text: ").lower()
    shift = int(input("Enter the shift number: "))
    if what_to_do == "encrypt":
        encryption(plain_text=text, shift_keys=shift)
    elif what_to_do == "decrypt":
        decryption(cipher_text=text, shift_keys=shift)
    play_again = input("Type 'yes' to continue or 'no' to end: ")
    if play_again.lower() != "yes":
        wanna_end = True
        print("Goodbye")
