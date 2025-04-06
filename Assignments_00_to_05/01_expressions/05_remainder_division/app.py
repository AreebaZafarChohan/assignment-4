"""
Program: Division Calculator
----------------------------
This program asks the user for two numbers and prints the 
result of dividing the first number by the second, 
along with the remainder.
"""

def main():
    try:
        # Get input from the user
        dividend = int(input("\nPlease enter an integer to be divided: "))
        divisor = int(input("Please enter an integer to divide by: "))

        # Handle division by zero
        if divisor == 0:
            print("\nError: Division by zero is not allowed.\n")
            return  # Exit the function if divisor is zero
        
        # Perform division and print result
        quotient = dividend // divisor
        remainder = dividend % divisor
        print(f"\nThe result of this division is {quotient} with a remainder of {remainder}\n")

    except ValueError:
        print("\nInvalid input! Please enter integers only.\n")        

# This line ensures that the main() function runs when the script is executed
if __name__ == '__main__':
    main()
