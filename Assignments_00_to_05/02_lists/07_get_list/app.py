# get list
"""
Write a program which continuously asks the user to enter values which are added one by one into a list.
When the user presses enter without typing anything, print the list.

Here's a sample run (user input is in blue):

Enter a value: 1 
Enter a value: 2 
Enter a value: 3 
Enter a value: 
Here's the list: ['1', '2', '3']
"""

def main():
    my_list = []  # Initialize an empty list
    print("\nEnter values one by one. Press ENTER without typing anything to finish.\n")

    while True:
        user_input = input("Enter a value or (press Enter to exit program): ")  # Take user input
        
        if user_input == "":  # Stop taking input if empty
            print(f"\nHere's the list: {my_list}\n")  # Print the final list
            break
        else:
            my_list.append(user_input)  # Append input to list


# This line ensures that the main() function runs when the script is executed
if __name__ == '__main__':
    main()
