# print ones digit

"""
Write a function called print_ones_digit , which takes as a parameter an integer num and prints its ones digit. The modulo (remainder) operator, %, should be helpful to you here. Call your function from main()!

Here's a sample run (user input is in blue):

Enter a number: 42 The ones digit is 2

"""

# Function to print the ones digit of a given number
def print_ones_digit(num):
    ones_digit = num % 10  # Get the remainder when divided by 10
    print(f"\nThe ones digit is {ones_digit}\n") # print ones_digit with message

def main():
    # Takes an integer input from the user and calls print_ones_digit().
    
    try:
        user_input = int(input("\nEnter a number to see its ones digit: "))  # Takes user input and converts it into an integer
        print_ones_digit(user_input)  # Call the function with user_input as argument
    except ValueError:
        print("\nInvalid input! Please enter a valid integer.\n")  # Handle non-integer input

# This ensures the main() function runs when the script is executed directly
if __name__ == '__main__':
    main()