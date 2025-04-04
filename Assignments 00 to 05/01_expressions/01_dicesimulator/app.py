"""
Program: dicesimulator
----------------------
Simulate rolling two dice, three times.  Prints
the results of each die roll.  This program is used
to show how variable scope works.
"""

import random 

def roll_dice():
    # Simulates rolling two dice in for loop three times and prints their total.
    for i in range(1,4):
        die_1 = random.randint(1,6)
        die_2 = random.randint(1,6)
        print(f"{i} time roll! \t die_1 is {die_1} and die_2 is {die_2} | Sum of {die_1} + {die_2} = {die_1 + die_2}")


def main():
    print("\nRoll the Dice!")

    die_1 = 715 # Local variable inside main()
    print(f"\ndie_1 in main() starts as: {die_1}\n")

    roll_dice() # call the roll_dice() function

    print(f"\ndie_1 in main() ends as: {die_1}\n")


# This line ensures that the main() function runs when the script is executed
if __name__ == '__main__':
    main()