key = input("Enter the key: ").upper().replace(" ", "")
plaintext = input("Enter the plaintext: ").upper().replace(" ", "")
extended_key = ""
key_index = 0
for i in range(len(plaintext)):
    extended_key += key[key_index]
    key_index = (key_index + 1) % len(key)
ciphertext = ""
for i in range(len(plaintext)):
    if plaintext[i].isalpha():
        shift = ord(extended_key[i]) - ord('A')
        encrypted_char = chr(((ord(plaintext[i]) - ord('A') + shift) % 26) + ord('A'))
        ciphertext += encrypted_char
    else:
        ciphertext += plaintext[i]
print("Ciphertext:", ciphertext)
