# international voting age

"""
Write a program which asks a user for their age and lets them know if they can or can't vote in the following three fictional countries.

Around the world, different countries have different voting ages. In the fictional countries of Peturksbouipo, Stanlau, and Mayengua, the voting ages are very different:

the voting age in Peturksbouipo is 16 (in real life, this is the voting age in, for example, Scotland, Ethiopia, and Austria)

the voting age in Stanlau is 25 (in real life this is the voting age in the United Arab Emirates)

the voting age in Mayengua is 48 (in real life, as far as we can tell, this isn't the voting age anywhere)

Your code should prompt the for their age and print whether or not they can vote in Peturksbouipo, Stanlau, or Mayengua.

Here's a sample run of the program (user input is in blue):

How old are you? 20 You can vote in Peturksbouipo where the voting age is 16. You cannot vote in Stanlau where the voting age is 25. You cannot vote in Mayengua where the voting age is 48.

"""

# Define the minimum voting ages for each fictional country
PETURKSBOUIPO_AGE: int = 16  # Peturksbouipo's voting age
STANLAU_AGE: int  = 25       # Stanlau's voting age
MAYENGUA_AGE: int  = 48      # Mayengua's voting age

def main():
    """
    This function prompts the user for their age and checks if they are eligible
    to vote in the three fictional countries: Peturksbouipo, Stanlau, and Mayengua.
    """
    try:
        # Get the user's age as an integer
        user_age = int(input("\nHow old are you? "))
        
        # Check voting eligibility for Peturksbouipo
        if user_age >= PETURKSBOUIPO_AGE:
            print(f"\nYou can vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}.")
        else:
            print(f"\nYou cannot vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}.")
        
        # Check voting eligibility for Stanlau
        if user_age >= STANLAU_AGE:
            print(f"\nYou can vote in Stanlau where the voting age is {STANLAU_AGE}.")
        else:
            print(f"\nYou cannot vote in Stanlau where the voting age is {STANLAU_AGE}.")
        
        # Check voting eligibility for Mayengua
        if user_age >= MAYENGUA_AGE:
            print(f"\nYou can vote in Mayengua where the voting age is {MAYENGUA_AGE}.")
        else:
            print(f"\nYou cannot vote in Mayengua where the voting age is {MAYENGUA_AGE}.\n")
    
    except ValueError:
        # Handle invalid input (non-numeric values)
        print("Invalid input! Please enter a valid age as a number.")

# This line ensures that the main() function runs when the script is executed
if __name__ == '__main__':
    main()