def rail_fence_encrypt(text, rails):
    fence = [['' for _ in range(len(text))] for _ in range(rails)]
    direction = None
    row, col = 0, 0
    for char in text:
        fence[row][col] = char
        col += 1
        if row == 0 or row == rails - 1:
            direction = not direction
        row += 1 if direction else -1
    ciphertext = ''.join([''.join(row) for row in fence])
    return ciphertext
def rail_fence_decrypt(ciphertext, rails):
    fence = [['' for _ in range(len(ciphertext))] for _ in range(rails)]
    direction = None
    row, col = 0, 0
    for char in ciphertext:
        fence[row][col] = '*'
        col += 1
        if row == 0 or row == rails - 1:
            direction = not direction
        row += 1 if direction else -1
    index = 0
    for r in range(rails):
        for c in range(len(ciphertext)):
            if fence[r][c] == '*':
                fence[r][c] = ciphertext[index]
                index += 1
    plaintext = []
    row, col = 0, 0
    for _ in ciphertext:
        plaintext.append(fence[row][col])
        col += 1
        if row == 0 or row == rails - 1:
            direction = not direction
        row += 1 if direction else -1

    return ''.join(plaintext)
text = input("Enter the text: ").replace(' ', '').lower()
rails = int(input("Enter the number of rails: "))
mode = input("Do you want to 'encrypt' or 'decrypt'?: ").strip().lower()
if mode not in ['encrypt', 'decrypt']:
    print("Invalid mode! Please enter 'encrypt' or 'decrypt'.")
else:
    if mode == 'encrypt':
        result = rail_fence_encrypt(text, rails)
    elif mode == 'decrypt':
        result = rail_fence_decrypt(text, rails)

    print(f"Result: {result}")