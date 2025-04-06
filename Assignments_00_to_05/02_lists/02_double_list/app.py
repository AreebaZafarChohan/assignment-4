# double list
"""
Write a program that doubles each element in a list of numbers. For example, if you start with this list:

numbers = [1, 2, 3, 4]

You should end with this list:

numbers = [2, 4, 6, 8]

"""
from typing import List

def double_list_in_place(numbers: List[int]) -> None:
    """Doubles each element in the given list (modifies in place)."""
    for i in range(len(numbers)):  # Loop through indices
        numbers[i] *= 2  # Double the value in the same list

def main():
    numbers: List[int] = [1, 2, 3, 4]  # Original list
    print(f"\nBefore doubling: {numbers}")

    double_list_in_place(numbers)  # Modify list in place

    print(f"After doubling: {numbers}\n")  # Output modified list


# This line ensures that the main() function runs when the script is executed
if __name__ == '__main__':
    main()