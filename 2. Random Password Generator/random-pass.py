import random
import string

def generate_password(length=12, use_letters=True, use_numbers=True, use_specials=True):
    """Generates a strong random password based on user preferences."""
    
    if not (use_letters or use_numbers or use_specials):
        raise ValueError("At least one character type must be selected.")
    
    char_pool = ""
    if use_letters:
        char_pool += string.ascii_letters
    if use_numbers:
        char_pool += string.digits
    if use_specials:
        char_pool += string.punctuation
    
    return "".join(random.choice(char_pool) for _ in range(length))

if __name__ == "__main__":
    # User customization
    length = int(input("Enter password length: "))
    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_specials = input("Include special characters? (y/n): ").lower() == 'y'
    
    # Generate and display the password
    try:
        password = generate_password(length, use_letters, use_numbers, use_specials)
        print("Generated Password:", password)
    except ValueError as e:
        print("Error:", e)
