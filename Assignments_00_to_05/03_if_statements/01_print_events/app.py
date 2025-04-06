# print events

"""
Write a program that prints the first 20 even numbers. There are several correct approaches, but they all use a loop of some sort. Do no write twenty print statements

The first even number is 0:

0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38

"""

def main():
    """
    This function prints all even numbers from 0 to 39.
    """
    print("\nThe first even number is 0:\n")  # Inform the user about the first even number
    
    for i in range(0, 40):  # Loop through numbers from 0 to 39
        if i % 2 == 0:  # Check if the number is even
            print(i, end=" ")  # Print the even number on the same line, separated by spaces

# This line ensures that the main() function runs when the script is executed
if __name__ == '__main__':
    main()