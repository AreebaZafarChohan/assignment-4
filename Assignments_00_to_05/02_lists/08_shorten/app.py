# shorten
"""
Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, and prints each item it removes until lst is MAX_LENGTH items long. If lst is already shorter than MAX_LENGTH you should leave it unchanged. We've written a main() function for you which gets a list and passes it into your function once you run the program. For the autograder to pass you will need MAX_LENGTH to be 3, but feel free to change it around to test your program.

"""

# shorten function: removes elements from the end of the list until MAX_LENGTH is reached
MAX_LENGTH = 7

def shorten(lst):
    """Remove elements from the end of the list until it is MAX_LENGTH long."""
    while len(lst) > MAX_LENGTH:
        removed_element = lst.pop()
        print(f"Removed Element: {removed_element}")

def main():
    """Main function to handle user input and shorten the list if necessary."""
    try:
        choice = input("\nDo you want to enter elements one by one or provide a full list? (enter/list): ").strip().lower()

        if choice == "list":
            user_list = input("\nEnter the list elements separated by spaces: ").split()
            print(f"\nOriginal list: {user_list}\n")
        else:
            user_list = []  # Initialize an empty list
            print("\nEnter elements one by one. Press ENTER without typing to stop.")
            while True:
                element = input("Enter element: ")  # Take input
                if element == "":  # Stop taking input if empty
                    break
                user_list.append(element)  # Append input to list

            print(f"\nOriginal list: {user_list}\n")  # Print full list after input

        if user_list:  # Ensure list is not empty before calling shorten()
            shorten(user_list)  # Shorten the list if necessary
            print(f"\nShortened list: {user_list}\n")  # Display final list
        else:
            print("\nNo elements entered! The list is empty.\n")

    except ValueError:
        print("\nInvalid Input! Please enter a valid number.\n")  # Handle invalid input

# This line ensures that the main() function runs when the script is executed
if __name__ == '__main__':
    main()