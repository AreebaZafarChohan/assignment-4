# multiple returns

"""
There are times where you are working with lots of different data within a function that you want to return. While generally, we want to keep functions to have a precise purpose, sometimes that purpose just deals with multiple bits of data.

To practice this, imagine we are working on a program where the user needs to enters data to sign up for a website. Fill out the get_user_data() function which:

Asks the user for their first name and stores it in a variable

Asks the user for their last name and stores it in a variable

Asks the user for their email address and stores it in a variable

Returns all three of these pieces of data in the order it was asked

You can return multiple pieces of data by separating each piece with a comma in the return line.

Here is an example run of the program:

What is your first name?: Jane

What is your last name?: Stanford

What is your email address?: janestanford@stanford.edu

Received the following user data: ('Jane', 'Stanford', 'janestanford@stanford.edu')

(Note. This idea is called tuple packing/unpacking. We "pack" our return values into a single data structure called a tuple. We can then "unpack" these values back into our original values or leave them as a tuple.)

"""

# this fucntion asks the user for their first name, last name, and email address, and returns them as a tuple
def get_user_data():
    # Prompt the user for their first name
    first_name = input("\nWhat is your first name?: ")
    
    # Prompt the user for their last name
    last_name = input("\nWhat is your last name?: ")
    
    # Prompt the user for their email address
    email = input("\nWhat is your email address?: ")
    
    return first_name, last_name, email  # Return all three pieces of data as a tuple

def main():
    # Call the get_user_data function and store the returned values
    user_data = get_user_data()
    
    # Print the received user data
    print(f"\nReceived the following user data: {user_data}\n")



# This ensures the main() function runs when the script is executed directly
if __name__ == '__main__':
    main()