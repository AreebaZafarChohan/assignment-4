# print multiple

"""
Fill out print_multiple(message, repeats), which takes as parameters a string message to print, and an integer repeats number of times to print message. We've written the main() function for you, which prompts the user for a message and a number of repeats.

Here's a sample run of the program (user input is in blue):

Please type a message: Hello! Enter a number of times to repeat your message: 6 Hello! Hello! Hello! Hello! Hello! Hello!

"""

# Function to print a message multiple times
def print_multiple(message, repeats):
    """
    Takes a message (string) and repeats it a given number of times.
    Returns the concatenated string with spaces between repetitions.
    """
    return (message + " ") * repeats  # Repeat the message with a space

def main():
    """
    Main function to take user input and print the message multiple times.
    """
    user_input = input("\nPlease type a message: ")  # Get message input from user
    try:
        repitation = int(input("\nEnter a number of times to repeat your message: "))  # Get repeat count
        repeated_message = print_multiple(user_input, repitation)  # Call function to generate repeated message
        
        print("\n", repeated_message, "\n")  # Print the final repeated message
    except ValueError:
        print("Invalid input! Please enter a valid number.")  # Handle non-integer input

# Ensures the main function runs when the script is executed directly
if __name__ == '__main__':
    main()