import math
def create_grid(text, key_length, fill_char='x'):
    num_rows = math.ceil(len(text) / key_length)
    padded_text = text.ljust(num_rows * key_length, fill_char)
    grid = [padded_text[i:i + key_length] for i in range(0, len(padded_text), key_length)
    return grid
def encrypt(text, key):
    key_length = len(key)
    grid = create_grid(text, key_length)
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    ciphertext = ''.join(''.join(row[i] for row in grid) for i in key_order)
    return ciphertext
def decrypt(ciphertext, key):
    key_length = len(key)
    num_rows = math.ceil(len(ciphertext) / key_length)
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    cols = [ciphertext[i * num_rows:(i + 1) * num_rows] for i in range(key_length)]
    grid = [''] * num_rows
    for i, col_index in enumerate(key_order):
        for j in range(num_rows):
            grid[j] += cols[col_index][j]
    plaintext = ''.join(grid).rstrip('x')
    return plaintext
text = input("Enter the text: ").replace(' ', '').lower()
key = input("Enter the key: ").lower()
mode = input("Do you want to 'encrypt' or 'decrypt'?: ").strip().lower()
if mode not in ['encrypt', 'decrypt']:
    print("Invalid mode! Please enter 'encrypt' or 'decrypt'.")
else:
    if mode == 'encrypt':
        result = encrypt(text, key)
    elif mode == 'decrypt':
        result = decrypt(text, key)
    
    print(f"Result: {result}")