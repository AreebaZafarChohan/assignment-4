#  phonebook

"""
In this program we show an example of using dictionaries to keep track of information in a phonebook.

"""

def main():
    phone_book = {}

    while True:
        print("\n=============================")
        print("\nPhonebook Menu:")
        print("1. Add a contact")
        print("2. Search for a contact")
        print("3. View all contacts")
        print("4. Exit")
        print("=============================\n")

        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            name = input("\nEnter the name: ")
            phone_number = int(input("Enter the phone number: "))

            phone_book[name] = f"+92{phone_number}"
            print(f"\nContact for {name} added successfully ✅!\n")

        elif choice == "2":
            search_name = input("\nEnter the name to search a number: ")
            if search_name in phone_book:
                print(f"\nThe phone number for {search_name} is {phone_book[name]} 📞📘✅\n")
            else:
                print(f"\nNo contact found for {search_name}.\n")

        elif choice == "3":
            print("\nPhonebook Contacts:")
            if len(phone_book) > 0: 
                for name , number in phone_book.items():
                    print(f"(● {name}: {number} )")
            else:
                print("\nPhone book is empty!\n")    
                

        elif choice == "4":
            print("\nExiting the phonebook.\n")
            break

        else:
            print("\nInvalid choice. Please try again.\n")        


# This ensures the main() function runs when the script is executed directly
if __name__ == '__main__':
    main()