# Import logo
import art
print(art.logo)

# Alphabet list
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Define function 
def caesar(original_text, shift_amount, encode_or_decode):
    #Initial string
    output_text = ""

    # Changes shift amount to negative number if "decode" selected
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        # For characters not in alphabet list, they will be shown as is (e.g., numbers or symbols)
        if letter not in alphabet:
            output_text += letter
        # Letters will be shifted forward (encode) or backward (decode) and added to output string
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            # Modulo creates loop for alphabet list (e.g., "z" shifted forwards by 2 will be "b")
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")


# Continues program as long as user responds with "yes"
program_continue = True

while program_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    try_again = input("Type 'yes' if you want to continue again. Otherwise, type 'no'.\n").lower()
    #If user replies "no", program ends
    if try_again == "no":
        program_continue = False
        print("Goodbye")


