import time

# Function to encrypt or decrypt text using Caesar Cipher
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

# Step 1: Ask the user whether to encrypt or decrypt
mode = input("Do you want to (a) encrypt or (b) decrypt? Enter 'a' or 'b': ").lower()
if mode == 'a':
    mode = 'encrypt'
elif mode == 'b':
    mode = 'decrypt'
else:
    print("Invalid option. Exiting.")
    exit()

# Step 2: Ask the user for the text to encrypt or decrypt
text = input("Enter the text: ")

# Start measuring time
start_time = time.time()

# Step 3: Print out all possible translations (for each shift K from 1 to 25)
for shift in range(1, 26):
    result_text = caesar_cipher(text, shift, mode)
    print(f"K is {shift}: {result_text}")

# End measuring time
end_time = time.time()

# Print the time taken for the operation
print(f"\nTime taken: {end_time - start_time:.6f} seconds")
