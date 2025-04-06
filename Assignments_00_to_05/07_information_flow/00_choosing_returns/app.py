# choosing returns

"""
There are times where we want to return different things from a function based on some condition. To practice this idea, imagine that we want to check if someone is an adult. We might check their age and return different things depending on how old they are!

We've provided you with the ADULT_AGE variable which has the age a person is legally classified as an adult (in the United States). Fill out the is_adult(age) function, which returns True if the function takes an age that is greater than or equal to ADULT_AGE. If the function takes an age less than ADULT_AGE, return False instead.

Here are two sample runs of the program, one for each return option (user input in bold italics):

(Entered age is an adult age)

How old is this person?: 35

True

(Entered age is not an adult age)

How old is this person?: 7

False

"""
# Define the minimum adult age
ADULT_AGE: int = 18  # U.S. adult age

# Function that checks whether a user is an adult
def is_adult(age):
    if age >= ADULT_AGE:
        return True  # If age is 18 or older, return True
    else:
        return False  # If age is less than 18, return False

# Main function that takes user input
def main():
    try:
        # Get the user's age input
        user_age = int(input("\nHow old is this person?: "))
        
        # Call the function and print the result
        print(is_adult(user_age))
    
    except ValueError:
        # If the user enters an invalid input (like text), catch the error and show a message
        print("\nInvalid input! Please enter a valid number for age.\n")


# This ensures the main() function runs when the script is executed directly
if __name__ == '__main__':
    main()