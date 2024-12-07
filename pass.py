import random
import string

# Function to generate a random password
def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    # Define the character sets based on user preferences
    characters = ""
    
    if use_upper:
        characters += string.ascii_uppercase  # A-Z
    if use_lower:
        characters += string.ascii_lowercase  # a-z
    if use_digits:
        characters += string.digits  # 0-9
    if use_symbols:
        characters += string.punctuation  # Special characters like !@#$%

    # If no character set is selected, inform the user and return
    if not characters:
        print("Error: You must select at least one character type (letters, digits, or symbols).")
        return None
    
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Function to get user input for password generation criteria
def get_user_input():
    print("Welcome to the Python Password Generator!")

    # Get the desired password length
    while True:
        try:
            length = int(input("Enter password length (min 8): "))
            if length < 8:
                print("Password length must be at least 8 characters.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Ask user which character types they want to include
    use_upper = input("Include uppercase letters (Y/N)? ").strip().lower() == 'y'
    use_lower = input("Include lowercase letters (Y/N)? ").strip().lower() == 'y'
    use_digits = input("Include digits (Y/N)? ").strip().lower() == 'y'
    use_symbols = input("Include special characters (Y/N)? ").strip().lower() == 'y'
    
    # Generate the password using the criteria provided by the user
    password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
    
    # Display the generated password if valid
    if password:
        print(f"Generated Password: {password}")

# Run the password generator
if __name__ == "__main__":
    get_user_input()
