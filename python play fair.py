key = input("Enter the key: ").upper().replace("J", "I").replace(" ", "")
matrix = []
alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
for char in key:
    if char not in matrix:
        matrix.append(char)

for char in alphabet:
    if char not in matrix:
        matrix.append(char)
playfair_matrix = []
for i in range(5):
    playfair_matrix.append(matrix[i*5:(i+1)*5])
plaintext = input("Enter the plaintext: ").upper().replace("J", "I").replace(" ", "")
prepared_text = ""
i = 0
while i < len(plaintext):
    char1 = plaintext[i]
    if i + 1 < len(plaintext):
        char2 = plaintext[i + 1]
    else:
        char2 = "X"  

    if char1 == char2:
        prepared_text += char1 + "X"
        i += 1
    else:
        prepared_text += char1 + char2
        i += 2

if len(prepared_text) % 2 != 0:
    prepared_text += "X"
ciphertext = ""
for i in range(0, len(prepared_text), 2):
    char1 = prepared_text[i]
    char2 = prepared_text[i + 1]

    row1, col1 = divmod(matrix.index(char1), 5)
    row2, col2 = divmod(matrix.index(char2), 5)

    if row1 == row2:
        ciphertext += playfair_matrix[row1][(col1 + 1) % 5] + playfair_matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:
        ciphertext += playfair_matrix[(row1 + 1) % 5][col1] + playfair_matrix[(row2 + 1) % 5][col2]
    else:
        ciphertext += playfair_matrix[row1][col2] + playfair_matrix[row2][col1]

print("Ciphertext:", ciphertext)
