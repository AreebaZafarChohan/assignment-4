# leap year

"""
Write a program that reads a year from the user and tells whether a given year is a leap year or not.

A leap year (also known as an intercalary year or bissextile year) is a calendar year that contains an additional day (or, in the case of a lunisolar calendar, a month) added to keep the calendar year synchronized with the astronomical year or seasonal year. In the Gregorian calendar, each leap year has 366 days instead of 365, by extending February to 29 days rather than the common 28.

In the Gregorian calendar, three criteria must be checked to identify leap years:

The given year must be evenly divisible by 4;
If the year can also be evenly divided by 100, it is NOT a leap year; unless:
The year is also evenly divisible by 400. Then it is a leap year.
Your code should use the above criteria to check for a leap year and then print either "That's a leap year!" or "That's not a leap year."

"""

def main():
    
    try:
        # Take user input for the year
        year = int(input("\nPlease enter a year: "))
        
        # Check if the year is a leap year
        # A year is a leap year if:
        # 1. It is divisible by 4 and NOT divisible by 100, OR
        # 2. It is divisible by 400
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            print("\nThat's a leap year!\n")  # Print message if the year is a leap year
        else:
            print("\nThat's not a leap year.\n")  # Print message if the year is not a leap year
    
    except ValueError:
        print("\nInvalid input! Please enter a valid numeric year.\n")  # Handle invalid input

# This line ensures that the main() function runs when the script is executed
if __name__ == '__main__':
    main()
