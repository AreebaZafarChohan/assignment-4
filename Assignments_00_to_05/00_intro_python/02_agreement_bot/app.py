# agreement bot

"""
Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).

Here's a sample run of the program (user input is in bold italics - note the space between the prompt and the user input!):

What's your favorite animal? cow

My favorite animal is also cow!

"""

def main():
    # takes user_input and convert it into lower case
    user_input = input("What is your favorite animal? ").lower()
    print(f"My favorite animal is also {user_input}!") # print the user_input with message


# This line ensures that the main() function runs when the script is executed 
if __name__ == '__main__':
    main()