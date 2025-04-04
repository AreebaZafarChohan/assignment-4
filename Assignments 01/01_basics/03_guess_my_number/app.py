# Guess my number
import random

def main():
    print("\nWelcome to a number guessing game 🔢🤔")
    print("\nI am thinking of a number between 0 and 99...")
    secret_num = random.randint(0,99)

    user_guess = int(input("Enter a guess: "))
    while secret_num != user_guess:
        if user_guess > secret_num:
            print("Your guess is too high ⚡☝")
        else:
            print("Your guess is too low 🔅👇")
        print(" ")
        user_guess: int = int(input("Enter a new guess: "))
    print("Congrats 🎉👏! The number was: " + str(secret_num))      

if __name__ == '__main__':
    main()