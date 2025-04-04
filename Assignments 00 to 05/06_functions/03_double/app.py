# double

"""
This program doubles a given number.

The function `double(num)` takes an integer and returns its double.
The `main()` function asks the user for input, calls `double()`, and prints the result.
If the user enters an invalid input, an error message is displayed.
"""

def double(num):
    
    # Returns the result of multiplying the given number by 2.
    
    return num * 2  # Multiply the number by 2 and return it

def main():
    
    # Asks the user to enter a number, doubles it using double(), and prints the result. Handles invalid inputs gracefully.
    
    try:
        user_input = int(input("\nEnter a number to double it: "))  # Prompt user for input
        double_num = double(user_input)  # Call the double function
        print(f"\nDouble of {user_input} is {double_num}\n")  # Print the doubled result
        
    except ValueError:
        print("Invalid input! Please enter a valid number.")  # Error message for invalid input

# Ensures that main() runs when the script is executed directly
if __name__ == '__main__':
    main()
