# print events

"""
Write a program that prints the first 20 even numbers. There are several correct approaches, but they all use a loop of some sort. Do no write twenty print statements

The first even number is 0:

0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38

"""

def main():
    """
    This function prints all even numbers from 0 to 38.
    """
    print("\nThe first even number is 0:")  # Informing the user about the first even number
    
    for i in range(0, 39):  # Loop from 0 to 38
        if i % 2 == 0:  # Check if the number is even
            print(i, end=" ")  # Print the even number with space in between

# This ensures the main() function runs when the script is executed directly
if __name__ == '__main__':
    main()