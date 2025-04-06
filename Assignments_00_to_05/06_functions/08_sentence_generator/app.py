# sentence generator

"""
Implement the helper function make_sentence(word, part_of_speech) which will take a string word and an integer part_of_speech as parameters and, depending on the part of speech, place the word into one of three sentence templates (or one from your imagination!):

If part_of_speech is 0, we will assume the word is a noun and use the template: "I am excited to add this ____ to my vast collection of them!"

If part_of_speech is 1, we will assume the word is a verb use the template: "It's so nice outside today it makes me want to ____!"

If part_of_speech is 2, we will assume the word is an adjective and use the template: "Looking out my window, the sky is big and ____!" make_sentence(word, part_of_speech) should not return anything, just print the correct sentence with the word filled in the blank.

Here's a sample run of the program (user input is in blue):

Please type a noun, verb, or adjective: groovy Is this a noun, verb, or adjective? Type 0 for noun, 1 for verb, 2 for adjective: 2 Looking out my window, the sky is big and groovy!

"""

# Function to create a sentence based on the word and part of speech
def make_sentence(word, part_of_speech):
    
    # Parameters:
    # word (str): The word to insert into the sentence.
    # part_of_speech (int): Indicates whether the word is a noun (0), verb (1), or adjective (2).

    
    # and prints a sentence with the word placed in the appropriate context.

    # If part_of_speech is 0, assume the word is a noun
    if part_of_speech == 0:
        print(f"\nI am excited to add this {word} to my vast collection of them!\n")
    
    # If part_of_speech is 1, assume the word is a verb
    elif part_of_speech == 1:
        print(f"\nIt's so nice outside today it makes me want to {word}!\n")
    
    # If part_of_speech is 2, assume the word is an adjective
    elif part_of_speech == 2:
        print(f"\nLooking out my window, the sky is big and {word}!\n")   
    
    # Handle invalid input cases
    else:
        print("\nPart of speech must be 0, 1, or 2! Can't make a sentence.\n")


# Main function to take user input and generate a sentence
def main():
    
    # Takes user input for a word and its part of speech, then generates a sentence using make_sentence().

    # Prompt the user to enter a word
    user_word = input("\nPlease type a noun, verb, or adjective: ")
    
    # Ask the user to specify the part of speech
    print("\nIs this a noun, verb, or adjective?\n")
    user_input = int(input("Type 0 for noun, 1 for verb, 2 for adjective: "))

    # Generate and print the sentence
    make_sentence(user_word, user_input)

# This ensures the main() function runs when the script is executed directly
if __name__ == '__main__':
    main()