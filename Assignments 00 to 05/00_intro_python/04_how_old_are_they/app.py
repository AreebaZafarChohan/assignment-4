# how old they are 

"""
Write a program to solve this age-related riddle!

Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:

Anton is 21 years old.

Beth is 6 years older than Anton.

Chen is 20 years older than Beth.

Drew is as old as Chen's age plus Anton's age.

Ethan is the same age as Chen.

Your code should store each person's age to a variable and print their names and ages at the end. The autograder is sensitive to capitalization and punctuation, be careful! Your solution should look like this (the below numbers are made up -- your solution should have the correct values!):

Anton is 3

Beth is 4

Chen is 5

Drew is 6

Ethan is 7

"""

def main():
    anton_age : int = 21  # Anton's age is given as 21 years old
    beth_age : int = 6 + anton_age  # Beth is 6 years older than Anton, so add 6 to Anton's age to get Beth's
    chen_age : int = 20 + beth_age  # Chen is 20 years older than Beth, so add 20 to Beth's age to get Chen's
    drew_age  : int= chen_age + anton_age  # Drew is as old as Chen's age plus Anton's age, so add them together
    ethan_age : int = chen_age  # Ethan is the same age as Chen, so set Ethan's age equal to Chen's

   # display all friends ages!
    print(f"Anton is {anton_age}")
    print(f"Beth is  {beth_age}" )
    print(f"Chen is  {chen_age}" )
    print(f"Drew is  {drew_age}" )
    print(f"Ethan is {ethan_age}")


# This line ensures that the main() function runs when the script is executed 
if __name__ == '__main__':
    main()