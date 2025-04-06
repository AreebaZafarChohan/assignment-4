# get last element
"""
Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.
"""

def get_last_element(lst):
    # Prints the last element of the list
    print(f"\nThe last element of this list is {lst[-1]}\n")  # Access last element and print it

def main():
    # Main function to handle user input and demonstrate getting the last element of a list
    try:
        choice = input("\nDo you want to enter elements one by one or provide a full list? (enter/list): ").strip().lower()

        if choice == "list":
            user_list = input("\nEnter the list elements separated by spaces: ").split()
        else:
            user_list = []  # Initialize an empty list
            print("\nEnter elements one by one. Press ENTER without typing to stop.")
            while True:
                element = input("Enter element: ")  # Take input
                if element == "":  # Stop taking input if empty
                    break
                user_list.append(element)  # Append input to list

        if user_list:  # Ensure list is not empty
            get_last_element(user_list)  # Call function to print last element
        else:
            print("\nNo elements entered! The list is empty.\n")

    except ValueError:
        print("\nInvalid Input! Please enter a valid number.\n")  # Handle invalid input


# This line ensures that the main() function runs when the script is executed
if __name__ == '__main__':
    main()
