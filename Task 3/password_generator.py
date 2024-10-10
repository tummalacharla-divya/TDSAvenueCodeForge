""" Password Generator
A password generator is a useful tool that 
generates strong and random passwords for 
users. This project aims to create a password 
generator application using Python allowing 
users to specify the length and complexity of 
the password."""
import secrets
import string

def generate_password(length, use_lowercase=True, use_uppercase=True, use_digits=True, use_symbols=True):
    # Define character pools
    character_pool = ""
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_digits:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation

    if len(character_pool) == 0:
        return "You must select at least one character type!"

    # Generate a secure random password
    password = ''.join(secrets.choice(character_pool) for _ in range(length))
    return password

def main():
    print("Welcome to the Advanced Password Generator!")
    
    try:
        length = int(input("Enter the desired password length: "))
        
        if length < 1:
            print("Password length must be at least 1.")
            return
        
        # Prompt the user for character types to include
        use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
        
        password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_symbols)
        print(f"Generated Password: {password}")
        
    except ValueError:
        print("Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()
