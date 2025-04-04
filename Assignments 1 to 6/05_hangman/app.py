import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words).upper()  # Convert word to uppercase
    while "-" in word or " " in word:
        word = random.choice(words).upper()  # Ensure all words are uppercase
    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # Letters in the word
    alphabet = set(string.ascii_uppercase)  # Uppercase letters
    used_letters = set()  # What the user has guessed
    total_attempts = 0  # Count the total guesses made

    lives = 10

    while len(word_letters) > 0 and lives > 0:
        print(f"\nYou have {lives} lives left and you have used these letters: ", " ".join(sorted(used_letters)))
        
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        total_attempts += 1  # Increment attempts on every guess

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print("Letter is not in word.")    

        elif user_letter in used_letters:
            print("You have already used that character. Please try again.")

        else:
            print("Invalid character. Please try again.")

    if lives == 0:
        print(f"\nYou died! Sorry, the word was {word}.")
    else:
        print(f"\nCongratulations! You guessed the word {word} in {total_attempts} attempts with {lives} lives remaining!!")

# Run the game
hangman()
