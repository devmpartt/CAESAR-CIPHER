import time

# Function to encrypt text using Caesar Cipher
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

# Step 1: Ask the user for the key (shift value)
shift = int(input("Enter the value of K (shift): "))

# Step 2: Ask the user whether to encrypt or decrypt
mode = input("Do you want to (a) encrypt or (b) decrypt? Enter 'a' or 'b': ").lower()
if mode == 'a':
    mode = 'encrypt'
elif mode == 'b':
    mode = 'decrypt'
else:
    print("Invalid option. Exiting.")
    exit()

# Step 3: Ask the user for the text to encrypt or decrypt
text = input("Enter the text: ")

# Start measuring time
start_time = time.time()

# Step 4: Perform encryption or decryption
result_text = caesar_cipher(text, shift, mode)

# End measuring time
end_time = time.time()

# Print the result and the time taken
print(f"\nThe {mode}ed text is: {result_text}")
print(f"Time taken: {end_time - start_time:.6f} seconds")
