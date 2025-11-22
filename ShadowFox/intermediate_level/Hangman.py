import random

stages = [
    """
     ------
     |    |
     |
     |
     |
     |
    _|_
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
    _|_
    """,
    """
     ------
     |    |
     |    O
     |    |
     |
     |
    _|_
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |
     |
    _|_
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |
     |
    _|_
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |
    _|_
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |
    _|_
    """
]

words = {
    "python": "A popular programming language",
    "india": "A country in South Asia",
    "apple": "A fruit and a tech company",
    "guitar": "A musical instrument",
    "sunflower": "A yellow flower that follows the sun"
}

word, hint = random.choice(list(words.items()))
guessed = ["_"] * len(word)
attempts = 6
wrong_guesses = 0

print("🎮 Welcome to Hangman!")
print(f"Hint: {hint}")

while wrong_guesses < attempts and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    print(stages[wrong_guesses])
    guess = input("Guess a letter or the whole word: ").lower()

    if guess == word:
        guessed = list(word)
        break
    elif len(guess) == 1 and guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed[i] = guess
        print("✅ Correct!")
    else:
        wrong_guesses += 1
        print(f"❌ Wrong! Attempts left: {attempts - wrong_guesses}")

if "_" not in guessed:
    print("\n🎉 You won! The word was:", word)
else:
    print(stages[-1])
    print("\n💀 Game over! The word was:", word)
