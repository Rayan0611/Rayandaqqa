
# Define the set of valid symbols
SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."


def decrypt_caesar(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char in SYMBOLS:
            char_index = SYMBOLS.find(char)
            new_index = (char_index - shift) % len(SYMBOLS)
            decrypted_text += SYMBOLS[new_index]
        else:
            decrypted_text += char  
    return decrypted_text

# Creating More Possibilitys
def brute_force_caesar(ciphertext):
    for shift in range(len(SYMBOLS)):
        decrypted_text = decrypt_caesar(ciphertext, shift)
        print(f"Shift {shift}: {decrypted_text}")
        
        
        if shift % 10 == 0 and shift != 0:
            input("Press Enter to see more shifts...")


encrypted_message = input("Enter the encrypted message: ")

# For all invalid inputs
if not encrypted_message.strip():
    print("Error: No input provided.")
    exit()


for char in encrypted_message:
    if char not in SYMBOLS:
        print(f"Warning: Character '{char}' is not in SYMBOLS and will remain unchanged.")

# Conformation 
if input("Do you want to proceed with brute force? (yes/no): ").lower() != "yes":
    exit()

print("Attempting to decrypt...")
brute_force_caesar(encrypted_message)