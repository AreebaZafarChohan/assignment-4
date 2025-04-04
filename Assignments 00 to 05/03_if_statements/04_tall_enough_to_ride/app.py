# Tall Enough to Ride

"""
This program asks the user how tall they are and prints whether they are taller than a specified minimum height.
It keeps asking until the user enters nothing, at which point it exits.
"""

MINIMUM_HEIGHT = 50  # Minimum height requirement to ride

def main():
    while True:
        user_input = input("How tall are you?  (Press Enter to stop) ").strip()  # Get input and remove extra spaces
        
        if user_input == "":  # Check if input is empty (exit condition)
            print("\nExiting Program...\nGoodbye!\n")
            break

        try:
            user_height = int(user_input)  # Convert input to an integer
            
            if user_height >= MINIMUM_HEIGHT:
                print("\nYou're tall enough to ride!\n")
            else:
                print("\nYou're not tall enough to ride, but maybe next year!\n")    

        except ValueError:
            print("\nInvalid Input! Please enter a number.\n")            

# Ensures that the main() function runs when the script is executed
if __name__ == '__main__':
    main()
