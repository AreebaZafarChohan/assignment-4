# choosing returns

"""
Fill out the subtract_seven helper function to subtract 7 from num, and fill out the main() method to call the subtract_seven helper function! If you're stuck, revisit the add_five example from lecture.

"""

# Helper function to subtract 7 from the given number
def subtract_seven(num):
    return num - 7    # Subtract 7 from the number

def main():
    # Taking user input
    user_num = int(input("\nEnter a number: "))  # Get number from the user
    
    result = subtract_seven(user_num)  # Call the helper function to subtract 7
    print(f"\nResult after subtracting 7: {result}\n")  # Print the result
    print(f"Calculation: {user_num} - 7 = {result}\n") # print calculation



# This ensures the main() function runs when the script is executed directly
if __name__ == '__main__':
    main()