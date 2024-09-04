import numpy as np

# Function to get a valid integer input
def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")

# Step 1: Get the 2x2 key matrix from the user
print("Enter the 2x2 key matrix (4 integers):")
key_matrix = np.zeros((2, 2), dtype=int)
for i in range(2):
    for j in range(2):
        key_matrix[i, j] = get_int_input(f"Enter value for key_matrix[{i}][{j}]: ")

# Step 2: Get the plaintext from the user
plaintext = input("Enter the plaintext: ").upper().replace(" ", "")

# If plaintext length is odd, add a filler character 'X'
if len(plaintext) % 2 != 0:
    plaintext += 'X'

# Step 3: Encrypt the plaintext
ciphertext = ""
for i in range(0, len(plaintext), 2):
    # Create the plaintext vector from two characters
    plaintext_vector = np.array([
        ord(plaintext[i]) - ord('A'),
        ord(plaintext[i + 1]) - ord('A')
    ])
    
    # Multiply the key matrix by the plaintext vector
    cipher_vector = (key_matrix @ plaintext_vector) % 26
    
    # Convert the cipher vector back to characters
    ciphertext += chr(cipher_vector[0] + ord('A'))
    ciphertext += chr(cipher_vector[1] + ord('A'))

# Step 4: Output the ciphertext
print("Ciphertext:", ciphertext)
