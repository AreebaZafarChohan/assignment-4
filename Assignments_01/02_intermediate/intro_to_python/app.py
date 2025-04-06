# Planetary Weight Calculator

# Gravity values for planets relative to Earth
GRAVITY = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

def main():
    print("🌍 Welcome to the Planetary Weight Calculator! 🚀")
    
    while True:
        try:
            # Get user weight on Earth
            user_weight = int(input("Enter your weight on Earth (kg): "))
            if user_weight <= 0:
                print("❌ Please enter a valid positive weight.\n")
                continue
            break
        except ValueError:
                print("❌ Invalid input! Please enter a numeric value.\n")

    # Display planet choices
    print("\nChoose a planet to find your equivalent weight:")
    for i, planet in enumerate(GRAVITY.keys(), 1):
        print(f"{i}. {planet}")

    while True:
        try:
            # Get planet choice
            choice = int(input("\nEnter the number of the planet: "))

            # Check if choice is valid
            if 1 <= choice <= len(GRAVITY):
                planet_name = list(GRAVITY.keys())[choice - 1]  # Get planet name from dictionary
                planet_weight = user_weight * GRAVITY[planet_name]  # Calculate equivalent weight
                print(f"\n🌌 Your weight on {planet_name} would be: {user_weight} * {GRAVITY[planet_name]} = {planet_weight:.2f} kg! 🚀")
                break
            else:
                print("\n❌ Invalid choice! Please select a number from the list.")
        except ValueError:
                    print("❌ Invalid input! Please enter a number.\n")
        

# Run the program
if __name__ == "__main__":
    main()
