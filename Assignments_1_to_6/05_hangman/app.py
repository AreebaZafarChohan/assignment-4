import random
import string
from words import words  # make sure this is a list of words

# Hangman drawing stages (from full lives to zero)
hangman_stages = [
    '''
       +---+
       |   |
           |
           |
           |
           |
    =========''',
    '''
       +---+
       |   |
       O   |
           |
           |
           |
    =========''',
    '''
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========''',
    '''
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========''',
    '''
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========''',
    '''
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========''',
    '''
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========''',
    '''
       +---+
       |   |
      [O   |
      /|\\  |
      / \\  |
           |
    =========''',
    '''
       +---+
       |   |
      [O]  |
      /|\\  |
      / \\  |
           |
    =========''',
    '''
       +---+
       |   |
      [O]_ |
      /|\\  |
      / \\  |
           |
    =========''',
    '''
       +---+
       |   |
      [O]_/
      /|\\  |
      / \\  |
           |
    ========='''
]

def get_valid_word(words):
    word = random.choice(words).upper()
    while "-" in word or " " in word:
        word = random.choice(words).upper()
    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    total_attempts = 0

    lives = 10  # Max lives = len(hangman_stages) - 1

    while len(word_letters) > 0 and lives > 0:
        print(hangman_stages[10 - lives])  # Show current stage
        print(f"\nYou have {lives} lives left. Used letters: {' '.join(sorted(used_letters))}")
        
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word:", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        total_attempts += 1

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print("\n❌ Letter is not in the word.")
        elif user_letter in used_letters:
            print("\n⚠️ You have already used that letter.")
        else:
            print("\n❌ Invalid character. Try again.")

    # Game Over
    if lives == 0:
        print(hangman_stages[-1])
        print(f"\n💀 You lost! The word was: {word}")
    else:
        print(f"\n🎉 Congratulations! You guessed the word '{word}' in {total_attempts} attempts with {lives} lives left!\n")

# Run the game
hangman()
