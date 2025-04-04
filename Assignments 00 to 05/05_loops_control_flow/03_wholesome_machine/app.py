# wholesome machine

"""
Write a program which prompts the user to type an affirmation of your choice (we'll use "I am capable of doing anything I put my mind to.") until they type it correctly. Sometimes, especially in the midst of such uncertain times, we just need to be reminded that we are resilient, capable, and strong; this little Python program may be able to help!

Here's a sample run of the program (user input is in blue):

Please type the following affirmation: I am capable of doing anything I put my mind to. Hmmm That was not the affirmation. Please type the following affirmation: I am capable of doing anything I put my mind to. I am capable of doing anything I put my mind to. That's right! :)

Note that you can call input() with no prompt and it will still wait for a user to type something!

"""

def main():
    """
    This function prompts the user to type a given affirmation correctly.
    If the user types it correctly, they receive a success message; otherwise,
    they are asked to try again until they get it right.
    """
    affirmation = "I am capable of doing anything I put my mind to."  # Define the affirmation statement

    while True:
        # Ask the user to type the affirmation
        user_input = input(f"\nPlease type the following affirmation: {affirmation} ")

        if user_input == affirmation:  # Check if the input matches the affirmation
            print("\nThat's right! :)\n")  # Success message
            break  # Exit the loop
        else:
            print("\nHmmm, that was not the affirmation. Please try again.\n")  # Prompt user to try again

# This ensures the main() function runs when the script is executed directly
if __name__ == '__main__':
    main()