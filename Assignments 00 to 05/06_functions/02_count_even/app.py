# count even

"""
Fill out the function count_even(lst) which

first populates a list by prompting the user for integers until they press enter (please use the prompt "Enter an integer or press enter to stop: "),

and then prints the number of even numbers in the list.

If you'd prefer to focus on the second task only, scroll down for our implementation of the first task!

"""

def count_even(lst):
    """
    Counts the number of even numbers in the given list.
    """
    even_count = 0  # Variable to store count of even numbers
    for num in lst:
        if num % 2 == 0:
            even_count += 1  # Increment count if number is even
    return even_count  # Return the count


def main():
    """
    Collects numbers from the user until they press enter, 
    then prints the count of even numbers.
    """
    user_list = []  # List to store user inputs

    while True:
        user_input = input('Enter an integer or press enter to stop: ')  # Get input as a string
        
        if user_input == "":  # Stop if input is empty
            break

        try:
            number = int(user_input)  # Convert to integer
            user_list.append(number)  # Add to list
        except ValueError:
            print("Invalid input! Please enter a valid number.")  # Error message

    # Count even numbers and print the result
    even_count = count_even(user_list)
    print(f"\nHere are your list: {user_list}")
    print(f"Total even numbers: {even_count}\n")


# Ensures that main() runs when the script is executed directly
if __name__ == '__main__':
    main()