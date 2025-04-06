# in range

"""
Implement the following function which takes in 3 integers as parameters:

def in_range(n, low, high) 

Returns True if n is between low and high, inclusive. high is guaranteed to be greater than low.

"""

# Function that checks if n is between low and high, inclusive
def in_range(n, low, high):
    
    # Return True if n is between low and high (inclusive)
    return low <= n <= high

def main():
    
    try:
        # Taking user input
        n = int(input("\nEnter a number: "))  # User inputs a number
        low = int(input("\nEnter the lower bound: "))  # User inputs the lower bound
        high = int(input("\nEnter the upper bound: "))  # User inputs the upper bound
        
        
        # Call in_range function and print the result
        if in_range(n, low, high):
            print(f"\n{n} is in the range between {low} and {high}.\n")
        else:
            print(f"\n{n} is not in the range between {low} and {high}.\n")
    
    except ValueError:
        print("\nError: Please enter valid integers for all inputs.\n")


# This ensures the main() function runs when the script is executed directly
if __name__ == '__main__':
    main()