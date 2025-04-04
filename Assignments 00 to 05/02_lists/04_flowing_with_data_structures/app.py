# flowing_with_data_structures
"""
In the information flow lesson, we discussed using a variable storing a number as an example of scope. We saw that changes we made to the number inside a function did not stay unless we returned it. This is true for what we call immutable data types which include things like numbers and strings.

However, there are also mutable data types where changes stay even if we don't return anything. Some examples of mutable data types are lists and dictionaries. This means that you should be mindful when modifying lists and dictionaries within helper functions since their changes stay whether or not you return them.

To see this in action, fill out the add_three_copies(...) function which takes a list and some data and then adds three copies of the data to the list. Don't return anything and see what happens! Compare this process to the x = change(x) example and note the differences.

Here is an example run of this program (user input in bold italics):

Enter a message to copy: Hello world!

List before: []

List after: ['Hello world!', 'Hello world!', 'Hello world!']

(Note. The concept of immutable/mutable data types is called mutability. Be careful because different programming languages have different rules regarding mutability!)

"""

def add_three_copies(lst, data):
    """ Adds three copies of 'data' to the list 'lst' """
    for _ in range(3):  # Loop 3 times
        lst.append(data)  # Append 'data' to the list
        print(lst)

def change_number(num):
    """ Adds 7 to the given number and prints the result """
    num += 7
    print(num)  # Print modified number      

def main():
    """ Main function to handle user input and demonstrate mutability vs. immutability """
    try:
        # Ask user if they want to test a mutable or immutable data type
        user_input = input("\nWhat do you want to try? (mutable/immutable): ").strip().lower()
        
        if user_input == "mutable":
            # Handling a mutable data type (list)
            user_input_str = input("\nEnter a message to copy: ")  # Get user input string
            my_list = []  # Create an empty list
            print(f"\nList before: {my_list}\n")
            
            add_three_copies(my_list, user_input_str)  # Call function to modify the list
            
            print(f"\nList after: {my_list}")  # Print modified list
            print("Lists are mutable, meaning changes made inside a function persist even outside of it.\n")

        elif user_input == "immutable":
            # Handling an immutable data type (number)
            user_input_num = int(input("\nEnter a number to copy: "))  # Convert input to integer
            
            num = 7  # Initialize a number
            print(f"\nNumber before: {num}\n")
            
            change_number(num)  # Call function to modify the number (but does not affect original)
            
            print(f"\nNumber after: {num}")  # Original number remains unchanged
            print("Numbers are immutable, meaning changes made inside a function do not persist outside of it.\n")

        else:
            print("Invalid choice! Please enter 'mutable' or 'immutable'.")  # Handle incorrect input
    
    except ValueError:
        print("Invalid Input! Please enter a valid number or message.")  # Handle invalid number input


# This line ensures that the main() function runs when the script is executed
if __name__ == '__main__':
    main()