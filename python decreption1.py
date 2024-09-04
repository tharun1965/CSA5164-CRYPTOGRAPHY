encrypted_message = input("Enter the encrypted message: ")
shift = int(input("Enter the shift value: "))
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
decrypted_message = ''
for char in encrypted_message:
    if char in alphabet:
        index = alphabet.find(char)
        shifted_index = (index - shift) % 26
        decrypted_message += alphabet[shifted_index]
    else:
        decrypted_message += char
print("Decrypted message:", decrypted_message)
