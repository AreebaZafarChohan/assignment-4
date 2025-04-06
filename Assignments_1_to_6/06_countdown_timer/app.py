# countdown timer

import time

def timer(total_seconds):
    
    # A countdown timer that accepts the total number of seconds and displays the remaining time in hh:mm:ss format.
    while total_seconds > 0:
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        # Format the time as hh:mm:ss
        timeformat = '{:02}:{:02}:{:02}'.format(hours, minutes, seconds)
        
        print(f"\rTime remaining: {timeformat}", end="")
        time.sleep(1)
        total_seconds -= 1

    print("\nTime's up! 🚨\n")

def main():
    
    # Main function to accept user input and call the timer function.
    
    try:
        # Get hours, minutes, and seconds from the user
        hours = int(input("\nEnter hours: "))
        minutes = int(input("Enter minutes: "))
        seconds = int(input("Enter seconds: "))
        
        # Validate input to make sure it's not negative
        if hours < 0 or minutes < 0 or seconds < 0:
            print("\nPlease enter positive numbers for hours, minutes, and seconds.\n")
            return
        
        # Convert hours and minutes to seconds and calculate total time
        total_seconds = (hours * 3600) + (minutes * 60) + seconds
        
        if total_seconds <= 0:
            print("\nPlease enter a time greater than 0 seconds.\n")
            return
        
        print(f"\nTimer started for {hours} hour(s), {minutes} minute(s), and {seconds} second(s)...\n")
        timer(total_seconds)
    except ValueError:
        print("\nInvalid input! Please enter integer values.\n")

if __name__ == "__main__":
    main()
