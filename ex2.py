import time

# Function to apply Caesar Cipher encryption or decryption
def caesar_cipher(text, shift, mode):
    result = ""
    if mode == 'decrypt':
        shift = -shift
    
    # Loop through each character in the input text
    for char in text:
        # Encrypt or decrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt or decrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # Keep non-alphabetic characters unchanged
        else:
            result += char
    return result

# Step 1: Ask the user for the first key (K1)
K1 = int(input("Enter the value of first K (shift): "))

# Step 2: Ask the user for the second key (K2)
K2 = int(input("Enter the value of second K (shift): "))

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

# Step 5: Perform double Caesar encryption/decryption for each combination of K1 and K2
print("\nAll possible translations for the given text with double Caesar Cipher:\n")
for shift1 in range(1, K1 + 1):
    for shift2 in range(1, K2 + 1):
        # Apply the first Caesar shift (K1)
        first_pass = caesar_cipher(text, shift1, mode)
        # Apply the second Caesar shift (K2)
        final_result = caesar_cipher(first_pass, shift2, mode)
        print(f"K1 is {shift1}, K2 is {shift2}: {final_result}")

# End measuring time
end_time = time.time()

# Print the time taken for the operation
print(f"\nTime taken: {end_time - start_time:.6f} seconds")
