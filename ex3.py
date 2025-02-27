import time
import math

# Function to calculate modular inverse of a mod m (used for decryption)
def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Function to apply the Affine Cipher
def affine_cipher(text, a, b, mode):
    result = ""
    m = 26  # Size of the alphabet
    # Decrypt mode requires the modular inverse of a
    if mode == 'decrypt':
        a_inv = mod_inverse(a, m)
        if a_inv is None:
            raise ValueError("Key 'a' has no modular inverse. Choose a different 'a' that is coprime with 26.")
        b = -b
    else:
        a_inv = a  # Use the same a for encryption

    # Apply the affine transformation for each character
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            x = ord(char.upper()) - ord('A')
            if mode == 'encrypt':
                # Encryption: (a * x + b) % 26
                transformed = (a * x + b) % 26
            else:
                # Decryption: (a_inv * (x - b)) % 26
                transformed = (a_inv * (x + b)) % 26
            
            # Convert back to the corresponding character
            new_char = chr(transformed + ord('A'))
            if not is_upper:
                new_char = new_char.lower()
            result += new_char
        else:
            # Non-alphabetic characters remain unchanged
            result += char
    
    return result

# Step 1: Ask the user for key 'a'
a = int(input("Enter the value of key a (must be coprime with 26): "))
# Ensure 'a' is coprime with 26
if math.gcd(a, 26) != 1:
    raise ValueError("Key 'a' must be coprime with 26. Please choose a valid 'a'.")

# Step 2: Ask the user for key 'b'
b = int(input("Enter the value of key b: "))

# Step 3: Ask the user whether to encrypt or decrypt
mode = input("Do you want to (a) encrypt or (b) decrypt? Enter 'a' or 'b': ").lower()
if mode == 'a':
    mode = 'encrypt'
elif mode == 'b':
    mode = 'decrypt'
else:
    print("Invalid option. Exiting.")
    exit()

# Step 4: Ask the user for the text to encrypt or decrypt
text = input("Enter the text: ")

# Start measuring time
start_time = time.time()

# Step 5: Perform the Affine Cipher translation
try:
    result_text = affine_cipher(text, a, b, mode)
except ValueError as e:
    print(e)
    exit()

# End measuring time
end_time = time.time()

# Print the result and time taken
print(f"\nThe {mode}ed text is: {result_text}")
print(f"Time taken: {end_time - start_time:.6f} seconds")
