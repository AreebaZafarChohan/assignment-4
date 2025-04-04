# count names

"""
This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

An example run of the program looks like this (user input is in blue):

Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number: 4 Enter a number: 3 Enter a number: 12 Enter a number: 3 appears 3 times. 4 appears 2 times. 6 appears 1 times. 12 appears 1 times.

"""
    

def main():
    # Create an empty list to store the names
    names = []

    while True:
        # Ask the user to enter a name
        user_input = input("\nEnter a name (or press Enter to stop): ")
        
        if user_input == "":  # Stop if the input is empty
            break
        
        # Add the entered name to the list
        names.append(user_input)

    # Initialize an empty dictionary to store the frequency of each name
    name_count = {}

    # Count the frequency of each name
    for name in names:
        if name in name_count:
            name_count[name] += 1
        else:
            name_count[name] = 1             

    # After the loop ends, print the count of each name
    print("\nName counts:\n")
    for name, count in name_count.items():
        print(f"● {name} appears {count} time(s).\n")

# This ensures the main() function runs when the script is executed directly
if __name__ == '__main__':
    main()
