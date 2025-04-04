# High-Low Game

import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    score = 0
    
    for i in range(NUM_ROUNDS):
        computer_num = random.randint(1,100)
        user_num = random.randint(1,100)

        print(f"Round {i + 1}")

        print(f"Your number is {user_num}")

        user_input = input("Do you think your number is higher or lower than the computer's?: ").lower()
        if ((user_num < computer_num) and (user_input == "lower")) or ((user_num > computer_num) and    (user_input == "higher")):
            print(f"You were right! The computer's number was {computer_num}")
            score += 1
            print(f"Your score is now {score}")
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_num}")
            print(f"Your score is now {score}")
        print(" ")
    if score == 5:
        print("Wow! You played perfectly!")
        print(" ")    
    elif score >= 2:
        print("Good job, you played really well!")
        print(" ") 
    else:
        print("Better luck next time!")
        print(" ")


if __name__ == "__main__":
    main()