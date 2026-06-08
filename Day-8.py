logo = r"""
 ,adPPYba,  ,adPPYYba,  ,adPPYba,  ,adPPYba,  ,adPPYYba,  8b,dPPYba,
a8"     ""  ""     `Y8  a8P_____88  I8[    ""  ""     `Y8  88P'   "Y8
8b          ,adPPPPP88  8PP"""""""   `"Y8ba,   ,adPPPPP88  88
"8a,   ,aa  88,    ,88  "8b,   ,aa  aa    ]8I  88,    ,88  88
 `"Ybbd8"'  `"8bbdP"Y8   `"Ybbd8"'  `"YbbdP"'  `"8bbdP"Y8  88
"""

print(logo)

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
]


def cipher(original_text, shift_amount, direction):
    cipher_text = ""

    shift_amount = shift_amount % 26

    if direction == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % 26
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += letter

    print(f"\nResult: {cipher_text}")


should_continue = True

while should_continue:

    direction = input(
        "\nType 'encode' to encrypt, type 'decode' to decrypt:\n"
    ).lower()

    text = input("Type your message:\n").lower()

    shift = int(input("Type the shift number:\n"))

    cipher(
        original_text=text,
        shift_amount=shift,
        direction=direction
    )

    restart = input(
        "\nType 'yes' if you want to go again. "
        "Otherwise type 'no':\n"
    ).lower()

    if restart == "no":
        should_continue = False
        print("\nGoodbye!")