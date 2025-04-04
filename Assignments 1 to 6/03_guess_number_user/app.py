import random

def computer_guess(x):
    print("\n_____________________________\n")
    print("Welcome to 'Guess the Number'! 🤖")
    print("Think of a number, and I'll try to guess it.")
    print("Type 'H' if my guess is too high.")
    print("Type 'L' if my guess is too low.")
    print("Type 'C' if I guessed correctly.")
    print("\n_____________________________\n")
    low = 1
    high = x
    guess_count = 0  # Keep track of the number of guesses
    feedback = ""

    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # If only one number is left, it must be the answer!

        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()

        # Validate user input
        while feedback not in ["h", "l", "c"]:
            feedback = input("Invalid input! Please enter H (high), L (low), or C (correct): ").lower()

        guess_count += 1

        if feedback == "h":
            high = guess - 1  # Reduce the high range
        elif feedback == "l":
            low = guess + 1  # Increase the low range

    responses = [
        "I'm a genius! 🤖",
        "That was easy! 😎",
        "I should work for the FBI! 🚀",
        "Took me a while, but I got it! 😉"
    ]

    print(f"🎉 Yay! I guessed your number, {guess}, correctly in {guess_count} attempts! {random.choice(responses)}")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        x = int(input("Enter the maximum number I should guess up to: "))
        computer_guess(x)
    else:
        print("Thanks for playing! 🎮")


# Start the game
x = int(input("Enter the maximum number I should guess up to: "))
computer_guess(x)
