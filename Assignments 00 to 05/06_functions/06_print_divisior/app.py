# print divisior

"""
Write the helper function print_divisors(num), which takes in a number and prints all of its divisors (all the numbers from 1 to num inclusive that num can be cleanly divided by (there is no remainder to the division). Don't forget to call your function in main()!

Here's a sample run (user input is in blue):

Enter a number: 12 Here are the divisors of 12 1 2 3 4 6 12

"""

def print_divisors(num):    
    for i in range(1, num + 1):  # Loop from 1 to num (inclusive)
        if num % i == 0:  # Check if i is a divisor of num
            print(i, end=" ")  # Print the divisor 


def main():
    
    try:
        
        user_input = int(input("\nEnter a number: "))  # Get user input
        print(f"\nHere are the divisors of {user_input}: ", end="") 
        print_divisors(user_input)  # Call function to print divisors
        print("\n")  # Move to the next line after printing all divisors
        
    except ValueError:
        print("\nInvalid input! Please enter a valid number.\n")  # Handle invalid input

# This ensures the main() function runs when the script is executed directly
if __name__ == '__main__':
    main()