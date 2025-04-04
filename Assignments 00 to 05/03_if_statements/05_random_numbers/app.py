# random numbers

"""
Print 10 random numbers in the range 1 to 100.

Here is an example run:

45 79 61 47 52 10 16 83 19 12

Each time you run your program you should get different numbers

81 76 70 1 27 63 96 100 32 92

Recall that the python random library has a function randint which returns an integer in the range set by the parameters (inclusive). For example this call would produce a random integer between 1 and 6, which could include 1 and could include 6:

value = random.randint(1, 6)

"""

import random  # Importing the random module to generate random numbers

def main():
    print("\nGenerating 10 random numbers between 1 and 100:\n")

    # Generate a list of 10 random numbers using list comprehension
    numbers = [str(random.randint(1, 100)) for _ in range(10)]

    # Print the numbers in a single line, separated by spaces
    print(" ".join(numbers))
    print("")  

# This ensures the main() function runs when the script is executed directly
if __name__ == '__main__':
    main()
