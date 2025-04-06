# get first element
"""
Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time.

"""

def get_first_element(lst):
    # Prints the first element of the list 
    print(f"\nThe first element of this list is: {lst[0]}\n")  # Access and print the first element

def main():
    # Main function to handle user input and demonstrate getting the first element of a list
    try:
        choice = input("\nDo you want to enter elements one by one or provide a full list? (enter/list): ").strip().lower()
        
        if choice == "list":
            user_list = input("\nEnter the list elements separated by spaces: ").split()
        else:
            num_elements = int(input("\nEnter the number of elements in the list: "))  # Get list size
            user_list = []  # Initialize an empty list

            for i in range(num_elements):  # Loop to collect user input for the list
                element = input(f"\nEnter element {i + 1}: ")  # Get each element
                user_list.append(element)  # Append element to list

        get_first_element(user_list)  # Call function to print first element
    
    except ValueError:
        print("\nInvalid Input! Please enter a valid number.\n")  # Handle invalid input


# This line ensures that the main() function runs when the script is executed
if __name__ == '__main__':
    main()