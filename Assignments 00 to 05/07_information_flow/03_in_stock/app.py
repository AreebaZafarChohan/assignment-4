# in stock

"""
Sophia has a fruit store. She has written a function num_in_stock which takes a string fruit as a parameter and returns how many of that fruit are in her inventory. Write code in main() which will:

Prompt the user to enter a fruit ("Enter a fruit: ")

Call num_in_stock(fruit) to get the number of that fruit that Sophia has in stock

Print the number which are in stock if Sophia has that fruit in her inventory (there are more than 0 in stock)

Print "This fruit is not in stock." if Sophia has none of that fruit in her inventory.

Here's two sample runs of the program (user input in bold italics):

Enter a fruit: pear

This fruit is in stock! Here is how many:

1000

Enter a fruit: lychee

This fruit is not in stock.

"""

def num_in_stock(fruit):
    # Sample inventory for fruits (you can modify this list)
    inventory = {
        "mango": 1000,
        "watermelon": 500,
        "lychee": 300,
        "custardapple": 700,
        "pineapple": 1500,
    }
    
    # Check if the fruit is in the inventory and return the stock
    return inventory.get(fruit.lower(), 0)
    

def main():

    try:
        print("\nWelcome to my fruit shop!!!!")
        # Prompt the user to enter a fruit
        fruit = input("\nEnter a fruit: ").lower().replace(" ", "")  # Convert input to lowercase for case-insensitive comparison and remove all spaces
        
        if fruit.isalpha():
            # Get the number of fruits in stock by calling num_in_stock function
            stock = num_in_stock(fruit)

            # Print the result based on the stock available
            if stock > 0:
                print(f"\nThis fruit is in stock! Here is how many:\n{stock}\n")
            
            else:
                print("\nThis fruit is not in stock.\n")
        else:
            print("\nPlease enter a valid fruit name (only letters allowed).\n")
        
    except Exception as e:
        print(f"\nError: {e}\n")
    



# This ensures the main() function runs when the script is executed directly
if __name__ == '__main__':
    main()