# Password Generator

import random
import string

def generate_password(numbers=1, length=12, use_special_chars=True, use_numbers=True):
    
    #Generates random passwords based on user preferences.

    #Parameters:
    # - numbers (int): Number of passwords to generate.
    # - length (int): Length of each password.
    # - use_special_chars (bool): Whether to include special characters.
    # - use_numbers (bool): Whether to include numbers.

    # Returns:
    # - list: A list of generated passwords.

    passwords = []  # List to store generated passwords

    for _ in range(numbers):
        # Define character sets
        lower_case = string.ascii_lowercase
        upper_case = string.ascii_uppercase
        digits = string.digits
        special_chars = string.punctuation

        # Start with basic characters (upper and lower case letters)
        char_pool = lower_case + upper_case

        # Add numbers and special characters if selected
        if use_numbers:
            char_pool += digits
        if use_special_chars:
            char_pool += special_chars

        # Generate a random password from the selected character pool
        password = "".join(random.choice(char_pool) for _ in range(length))
        passwords.append(password)  # Add password to list

    return passwords  # Return all generated passwords


def main():
    
    # Main function to take user input and generate passwords. Includes error handling for invalid inputs.
    

    print("\nWelcome to Password Generator")
    print("===============================")

    try:
        # Get number of passwords and length from user
        numbers = int(input("\nHow many passwords do you want to generate? "))
        length = int(input("Enter the desired password length: "))

        # Ensure valid input for password length
        if numbers < 1 or length < 1:
            print("\nError: Please enter positive values for password count and length.")
            return

        # Get user preferences for numbers and special characters
        include_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
        include_special = input("Include special characters? (y/n): ").strip().lower() == 'y'

        # Generate passwords
        passwords = generate_password(numbers, length, include_special, include_numbers)

        # Display generated passwords
        print("\nYour generated password(s):\n")
        for idx, password in enumerate(passwords, start=1):
            print(f"{idx}. {password}")
        print(" ")

    except ValueError:
        # Handle case when user enters non-numeric input for numbers/length
        print("\nError: Please enter a valid number for password count and length.\n")
    
    except Exception as e:
        # Handle any unexpected errors
        print(f"\nAn unexpected error occurred: {e}\n")


# Run the main function when script is executed
if __name__ == "__main__":
    main()
