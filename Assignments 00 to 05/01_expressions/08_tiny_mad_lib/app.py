"""
Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!

Mad Libs is a word game where players are prompted for one word at a time, and the words are eventually filled into the blanks of a word template to make an entertaining story! We've provided you with the beginning of a sentence (the SENTENCE_START constant) which will end in a user-inputted adjective, noun, and then verb.

Here's a sample run (user input is in bold italics):

Please type an adjective and press enter. tiny

Please type a noun and press enter. plant

Please type a verb and press enter. fly

Code in Place is fun. I learned to program and used Python to make my tiny plant fly!

"""

def main():
    SENTENCE_START: str = "While coding late at night, suddenly my" # fixed start sentence

    # Taking user input for adjective, noun, and verb
    adjective = input("\nPlease type an adjective and press enter: ")
    noun = input("Please type a noun and press enter: ")
    verb = input("Please type a verb and press enter: ")

    # Generating the final funny sentence
    # Example output
    # While coding late at night, suddenly my glitchy laptop started to code on its own! I think it's becoming self-aware! 😱
    
    print(f"\n{SENTENCE_START} {adjective} {noun} started to {verb} on its own! I think it's becoming self-aware! 😱\n")

# This line ensures that the main() function runs when the script is executed
if __name__ == '__main__':
    main()