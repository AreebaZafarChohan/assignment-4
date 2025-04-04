"""
Program: Feet to Inches Converter
---------------------------------
This program converts feet to inches.
There are 12 inches in one foot.
"""

def main():
    try:
        #takes user input of feet and convert it into float
        feet = float(input("\nEnter the number of feet: "))

        #Calculate feet into inches
        inches = feet * 12

        print(f"{feet} {"foot is" if feet == 1  else 'feet are'} = {inches} inches!\n") #print inches value with message
    except ValueError:
        print("Invalid input! Please enter a valid number.\n")    

# This line ensures that the main() function runs when the script is executed
if __name__ == '__main__':
    main()