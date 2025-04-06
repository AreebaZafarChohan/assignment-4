import random

joke_list = [
    "Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'",
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why was the JavaScript developer sad? Because he didn't 'null' his ex!",
    "How do you comfort a JavaScript bug? You console it!",
    "Why did the database administrator break up with his girlfriend? There were too many relationships!",
    "Why did the Python programmer go to therapy? Because he had too many 'self' issues!",
    "Why do programmers hate nature? It has too many bugs!",
    "Why was the computer cold? Because it left its Windows open!",
    "What’s a programmer’s favorite hangout place? Foo Bar!",
    "Why did the frontend developer break up with the backend developer? Because they had too many 'conflicts'!",
    "Why do Java developers wear glasses? Because they don’t see sharp!",
    "Why did the programmer quit his job? Because he didn't get arrays!",
    "Why do programmers always mix up Christmas and Halloween? Because Oct 31 == Dec 25!",
    "Why did the function break up with the loop? Because it got tired of running in circles!",
    "Why did the CSS developer go to therapy? Because he had too many margin issues!",
    "What do you call a programmer from Finland? Nerdic!",
    "Why did the Git repository break up? Because it had too many commits!",
    "Why did the JavaScript function fail? Because it had too many callbacks!",
    "What did the C programmer say when he was hungry? 'printf('I'm hungry')'",
    "Why do programmers love coffee? Because it helps them debug their lives!"
]

prompt: str = "What do you want? "
sorry: str = 'Sorry I only tell jokes'

def random_joke():
    username = input("👋 Hey! What's your name? ")
    print(f"🎉 Welcome to 🤖 Joke Bot, dear {username}! 🎭😂")

    user_input = input("🧐 What do you want? ").lower()
    while True:
        if user_input == "joke":
            joke = random.choice(joke_list)
            print(f"🤣 Here's a joke for you, {username}: \n👉 {joke} 😆")
            rating = input("⭐ How would you rate this joke? (1-5) ")
            print(f"🙌 Thanks for rating {rating}/5!")
            next_joke = input("💬 Want another one? Type 'more' or 'exit' to quit: ").lower()
            if next_joke != "more":
                print(f"👋 Goodbye {username}! Have a fun day! 😊")
                break
        else:
            print(f"❌ {sorry}, {username} 😢")
            break  

if __name__ == "__main__":
    random_joke()