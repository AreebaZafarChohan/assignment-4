# greetings

"""
We've written a helper function for you called greet(name) which takes as input a string name and prints a greeting. Write some code in main() to get the user's name and then greet them, being sure to call the greet(name) helper function.

Here's a sample run of the program (user input in bold italics):

What's your name? Sophia

Greetings Sophia!

"""

# Function that takes the name as input and prints a greeting message
def greet(name):
    print(f"\nGreetings {name}!\n")  # Print the greeting with the user's name

def main():
    # Ask the user for their name and capitalize the first letter
    user_name = input("\nWhat's your name? ").capitalize()
    greet(user_name)  # Call the greet function with the user's name



# This ensures the main() function runs when the script is executed directly
if __name__ == '__main__':
    main()