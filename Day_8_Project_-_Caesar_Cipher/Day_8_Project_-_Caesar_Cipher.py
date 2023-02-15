from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
            shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            try:
                end_text += alphabet[new_position]
            except:
                end_text = "Sorry, Alphabet is out of range"
                continue
        else:
            end_text += char
        
    print("\n\nThe end text is: ", end_text)
    

end_program = False

while not end_program:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").strip()
    text = input("\nType your message:\n").lower().strip()
    shift = int(input("\nType the shift number:\n"))
    shift = shift%26
    caesar(text, shift, direction)
    
    if input("\n\nDo you want to continue? yes/no: \n").strip().lower() == 'no':
        end_program = True
        print("\n\nGoodbye!")