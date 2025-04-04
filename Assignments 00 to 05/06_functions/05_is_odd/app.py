# is odd

"""
10 even 11 odd 12 even 13 odd 14 even 15 odd 16 even 17 odd 18 even 19 odd

"""

def main():
    # Loop through numbers from 10 to 19
    for num in range(10, 20):
        # Check if the number is even or odd
        if num % 2 == 0:
            print(f"{num} even")
        else:
            print(f"{num} odd")
                

# This ensures the main() function runs when the script is executed directly
if __name__ == '__main__':
    main()