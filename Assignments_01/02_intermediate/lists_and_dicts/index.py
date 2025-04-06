#2: Index Game

# List of items
my_list = ["Biryani", "Brownie", "Maggie", "Chocolate", "Zinger"]

def accessing_element(lst):
    try:
        index = int(input("Enter an index to access an element: "))
        if 0 <= index < len(lst):
            print(f"✅ Element at index {index}: {lst[index]}")
        else:
            print("❌ Invalid index! Please enter a number within range.")
    except ValueError:
        print("❌ Please enter a valid number.")

def modifying_element(lst):
    try:
        index = int(input("Enter an index to modify an element: "))
        if 0 <= index < len(lst):
            new_value = input("Enter a new value: ")
            lst[index] = new_value
            print(f"✅ Updated list: {lst}")
        else:
            print("❌ Invalid index! Please enter a number within range.")
    except ValueError:
        print("❌ Please enter a valid number.")

def slicing_element(lst):
    try:
        start = int(input("Enter a start index: "))
        end = int(input("Enter an end index: "))
        if 0 <= start < len(lst) and 0 <= end <= len(lst):
            print(f"✅ Sliced list: {lst[start:end]}")
        else:
            print("❌ Invalid indices! Please enter numbers within range.")
    except ValueError:
        print("❌ Please enter valid numbers.")

# Game loop
while True:
    print("\n🎮 Welcome to the List Manipulation Game!\n")
    print(" 1️⃣  Access an element")
    print(" 2️⃣  Modify an element")
    print(" 3️⃣  Slice the list")
    print(" 4️⃣  Exit the game")

    choice = input("\nSelect an option (1-4):")

    if choice == "1":
        accessing_element(my_list)
    elif choice == "2":
        modifying_element(my_list)
    elif choice == "3":
        slicing_element(my_list)
    elif choice == "4":
        print("\n🚀 Exiting the game. Goodbye!")
        break
    else:
        print("❌ Invalid choice! Please select a number between 1-4.")
