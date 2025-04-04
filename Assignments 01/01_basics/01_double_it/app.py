# double_it

def main():
    # Ask the user for an initial number
    user_input = input("Enter a number to start doubling: ")

    if not user_input.isdigit():
            print("Invalid number. Please enter a valid number.")
    else:
        user_num = int(user_input)
        if user_num >= 100:
             print("Please enter a number smaller than 100.")    
        else:
            # Keep doubling until the value reaches 100 or more
            while user_num < 100:
                user_num = user_num * 2
                print(user_num)
                
if __name__ == "__main__":
    main()                