# chaotic_counting

"""
Fill out the chaotic_counting() function, which prints the numbers from 1 to 10, but with a catch. We've written a done() function which returns True with likelihood DONE_LIKELIHOOD -- at each number, before printing the number, you should call done() and check if it returns True or not. If done() returns True, we're done counting, and you should use a return statement to end the chaotic_counting() function execution and resume execution of main(), which will print "I'm done.". We've written main() for you -- check it out! Notice that we'll only print "I'm done" from main() once chaotic_counting() is done with its execution.

Here's a sample run of this program:

I'm going to count until 10 or until I feel like stopping, whichever comes first. 1 2 3 I'm done.

"""

import random

# Probability that we stop counting (20% chance)
DONE_LIKELIHOOD = 0.2  

def done():
    # Randomly decides whether to stop counting or not.
    # Returns True with a probability of DONE_LIKELIHOOD.
    return random.random() < DONE_LIKELIHOOD  # Fix: Correctly return True/False

def chaotic_counting():
    # Prints numbers from 1 to 10 but may stop early based on done() function.
    for num in range(1, 11):
        if done():  # Check if we should stop counting
            return  # Exit function early
        print(num, end=" ")  # Print the number
    print(" ")    

def main():
    # Main function to start chaotic counting and print a completion message.
    print("\nI'm going to count until 10 or until I feel like stopping, whichever comes first.\n")
    chaotic_counting()  # Call the counting function
    print("\nI'm done.\n")

# Ensures that main() runs when the script is executed directly
if __name__ == '__main__':
    main()