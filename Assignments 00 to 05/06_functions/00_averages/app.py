# averages

"""
Write a function that takes two numbers and finds the average between the two.

"""

def find_average(a: float, b:float):
    # this function takes two numbers , add those numbers, divided by 2 and return it's average
    sum = a + b
    return sum / 2

def main():
    
    try:
        # takes user input and converts it into float
        num1 = float(input("\nEnter the first number: "))
        num2 = float(input("Enter the second number: "))

        # pass user input in find_average() function
        average_num = find_average(num1, num2)

        # print average number with user input and message
        print(f"\nThe average of {num1} and {num2} is {average_num}\n")
        
    except ValueError:
        print("\nInvalid input! Please enter a valid number.\n")

# This ensures the main() function runs when the script is executed directly
if __name__ == '__main__':
    main()