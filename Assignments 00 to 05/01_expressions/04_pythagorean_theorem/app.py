"""
Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!

The Pythagorean theorem, named after the ancient Greek thinker, Pythagoras, is a fundamental relation in geometry. It states that in a right triangle, the square of the hypotenuse is equal to the sum of the square of the other two sides.

For instance, let's consider a right triangle ABC, with the right angle located at C. According to the Pythagorean theorem:

BC ** 2 = AB ** 2 + AC ** 2

Your code should read in the lengths of the sides AB and AC, and that outputs the length of the hypotenuse (BC). You will probably find math.sqrt() to be useful.

Here's a sample run of the program (user input is in bold italics):

Enter the length of AB: 3

Enter the length of AC: 4

The length of BC (the hypotenuse) is: 5.0

"""

from math import sqrt # import square root from math library

def main():
    #takes values of ab and ac from user and convert it into float
    length_of_ab = float(input("\nEnter the length of AB: ")) 
    length_of_ac = float(input("Enter the length of AC: "))

    # Calculate the hypotenuse using the two sides and print it out
    length_of_bc = sqrt(length_of_ab**2 + length_of_ac**2)
    
    #display calculated hypotenuse value with message
    print(f"\nThe length of BC (the hypotenuse) is: {length_of_bc}\n")


# This line ensures that the main() function runs when the script is executed
if __name__ == '__main__':
    main()