"""
Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:

E = m * c**2

Almost 100 years ago, Albert Einstein famously discovered that mass and energy are interchangeable and are related by the above equation. You should ask the user for mass (m) in kilograms and use a constant value for the speed of light -- C = 299792458 m/s.

Here's a sample run of the program (user input is in bold italics):

Enter kilos of mass: 100

e = m * C^2...

m = 100.0 kg

C = 299792458 m/s

8.987551787368176e+18 joules of energy!

"""

# Define the constant for the speed of light (C)
SPEED_OF_LIGHT = 299792458  # in meters per second

def main():
    try: #use try except for debugging, escape from errors and program crashing 
        while True:
            mass = float(input("\nEnter kilos of mass (or 0 to exit): ")) #take user input of mass and convert it into float
            if mass == 0: 
                print("Exiting program...")
                break # Exit loop if user enter 0
            
            # Calculate energy
            print("\ne = m * C^2...")
            print(f"m = {mass} kg")
            print(f"C = {SPEED_OF_LIGHT} m/s")

            energy = mass * SPEED_OF_LIGHT ** 2
            print(f"\n{energy:.15e} joules of energy!\n") #display energy value 

    except ValueError: 
        print("Invalid input! Please enter a valid number.")        

# This line ensures that the main() function runs when the script is executed
if __name__ == '__main__':
    main()