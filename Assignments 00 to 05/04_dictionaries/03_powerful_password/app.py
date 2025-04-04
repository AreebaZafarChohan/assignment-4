# powerful password

"""
You want to be safe online and use different passwords for different websites. However, you are forgetful at times and want to make a program that can match which password belongs to which website without storing the actual password!

This can be done via something called hashing. Hashing is when we take something and convert it into a different, unique identifier. This is done using a hash function. Luckily, there are several resources that can help us with this.

For example, using a hash function called SHA256(...) something as simple as

hello

can be hashed into a much more complex

2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824

Fill out the login(...) function for a website that hashes their passwords. Login should return True if an email's stored password hash in stored_logins is the same as the hash of password_to_check.

(Hint. You will need to use the provided hash_password(...) function. You don't necessarily need to know how it works, just know that hash_password(...) returns the hash for the password!)

"""
import hashlib  # Importing hashlib for password hashing

def hash_password(password):
    """
    This function takes a password as input,
    converts it into bytes, hashes it using SHA-256,
    and returns the hashed password in hexadecimal format.
    """
    return hashlib.sha256(password.encode()).hexdigest()
    
def login(email, password_to_check, stored_logins):
    """
    This function checks if the given email exists in stored_logins
    and verifies if the provided password (hashed) matches the stored hash.
    
    Returns True if the email and password match, otherwise False.
    """
    # Hash the user-entered password
    hashed_input_password = hash_password(password_to_check)

    # Check if the email exists and the password hash matches
    if email in stored_logins and stored_logins[email] == hashed_input_password:
        return True
    
    return False  # Return False if login fails

def main():
    """
    This function stores user login data (hashed passwords),
    takes user input for email and password,
    and checks login validity using the login() function.
    """
    # Dictionary storing user emails and their hashed passwords
    stored_logins = {
        "test@example.com": hash_password("mypassword123"),
        "user@example.com": hash_password("securepass"),
        "areebazafar@gmail.com": hash_password("@na715")
    }
    
    # Prompt user for login details
    email = input("\nEnter your email: ")
    password = input("Enter your password: ")

    # Check login credentials
    if login(email, password, stored_logins):
        print("\nLogin successfully! ✅ 🎉\n")
    else:
        print("\nInvalid email or password! ❌\n")

# This ensures the main() function runs when the script is executed directly
if __name__ == '__main__':
    main()
