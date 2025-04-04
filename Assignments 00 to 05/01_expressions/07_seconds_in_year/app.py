"""
Use Python to calculate the number of seconds in a year, and tell the user what the result is in a nice print statement that looks like this (of course the value 5 should be the calculated number instead):

There are 5 seconds in a year!

You should use constants for this exercise -- there are 365 days in a year, 24 hours in a day, 60 minutes in an hour, and 60 seconds per minute.

"""

# Constants
DAYS_IN_YEAR = 365
HOURS_IN_DAY = 24
MINUTES_IN_HOUR = 60
SECONDS_IN_MINUTE = 60

def main():
    # display the result of calculated seconds with message
    print(f"\nThere are {DAYS_IN_YEAR * HOURS_IN_DAY * MINUTES_IN_HOUR * SECONDS_IN_MINUTE} seconds in a year! 🔢 ✨\n")


# This line ensures that the main() function runs when the script is executed
if __name__ == '__main__':
    main()