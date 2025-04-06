# pop up shop

"""
There's a small fruit shop nearby your house that you like to buy from. Since you buy several fruit at a time, you want to keep track of how much the fruit will cost before you go. Luckily you wrote down what fruits were available and how much one of each fruit costs.

Write a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they want to buy, and then prints out the total combined cost of all of the fruits.

Here is an example run of the program (user input is in bold italics):

How many (apple) do you want?: 2

How many (durian) do you want?: 0

How many (jackfruit) do you want?: 1

How many (kiwi) do you want?: 0

How many (rambutan) do you want?: 1

How many (mango) do you want?: 3

Your total is $99.5

"""

def main():

    fav_fruits = {
        "grapes": 3.5,
        "oranges": 15.0,
        "pineapple": 10.0,
        "custard_apple": 2.5,
        "lychee": 5.0,
        "mango": 4.0
    }

    print("\nWelcome to the Fruit Shop! 🍇 🥝 🍒 🏪 🛒")

    total_price = 0

    try:
        for fruit in fav_fruits:
            price = fav_fruits[fruit]
            bought = int(input(f"\nHow many ({fruit}) do you want?: "))
            total_price += price * bought

        print(f"\nYour total is ${total_price} 💸💲")
        print(f"Thank you for shopping 💗🤝\n")    
    except ValueError:
        print("\nInvalid input! Please enter a valid number\n")            
    
# This ensures the main() function runs when the script is executed directly
if __name__ == '__main__':
    main()