# triangle perimeter

"""
Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).

Here's a sample run of the program (user input is in bold italics):

What is the length of side 1? 3

What is the length of side 2? 4

What is the length of side 3? 5.5

The perimeter of the triangle is 12.5

"""
def main():
    print("Welcome to triangle primeter calculator!".capitalize()) # display welcome message
    side_1 = float(input("What is the length of side 1? ")) # take side 1 value of triangle from user in input
    side_2 = float(input("What is the length of side 2? ")) # take side 2 value of triangle from user in input
    side_3 = float(input("What is the length of side 3? ")) # take side 3 value of triangle from user in input

    sum_of_sides = side_1 + side_2 + side_3 # sum all sides of triangle
    print(f"The perimeter of the triangle is {sum_of_sides}") # display sum of triangle sides with message 

# This line ensures that the main() function runs when the script is executed 
if __name__ == "__main__":
    main()