import random
import textwrap

WORD_BANK = {
    "easy": [
        "apple", "house", "table", "green", "chair", "water", "music", "happy"
    ],
    "medium": [
        "python", "jungle", "flower", "planet", "laptop", "guitar", "puzzle"
    ],
    "hard": [
        "meticulous", "synchronous", "architecture", "benevolent", "philanthropy",
        "quizzical"
    ]
}

HANGMAN_STAGES = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,

    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,

    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,

    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,

    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,

    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,

    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]


def choose_word(difficulty: str) -> str:
    return random.choice(WORD_BANK[difficulty]).lower()


def scramble_word(word: str) -> str:
    letters = list(word)
    random.shuffle(letters)
    scrambled = "".join(letters)
    if scrambled == word:
        random.shuffle(letters)
        scrambled = "".join(letters)
    return scrambled


def display_state(wrong_guesses: int, discovered: list, guessed_letters: set, hints_left: int):
    print(HANGMAN_STAGES[min(wrong_guesses, len(HANGMAN_STAGES) - 1)])
    print("Word:", " ".join(discovered))
    print("Guessed letters:", ", ".join(sorted(guessed_letters)) if guessed_letters else "None")
    print(f"Hints left: {hints_left}")
    print()


def get_valid_letter_input(prompt: str):
    while True:
        s = input(prompt).strip().lower()
        if not s:
            print("Please type a letter or a command.")
            continue
        if s == "hint" or s == "quit":
            return s
        if len(s) != 1 or not s.isalpha():
            print("Type a single letter (a-z), or 'hint' to use a hint, or 'quit' to exit.")
            continue
        return s


def reveal_one_letter(word: str, discovered: list, guessed_letters: set) -> bool:
    """Reveal one random unrevealed letter. Returns True if a letter was revealed."""
    unrevealed_indices = [i for i, ch in enumerate(discovered) if ch == "_"]
    if not unrevealed_indices:
        return False
    idx = random.choice(unrevealed_indices)
    letter = word[idx]

    for i, ch in enumerate(word):
        if ch == letter:
            discovered[i] = letter
    guessed_letters.add(letter)
    return True


def play_round(difficulty: str):
    word = choose_word(difficulty)
    discovered = ["_" for _ in word]
    guessed_letters = set()
    wrong = 0
    max_wrong = len(HANGMAN_STAGES) - 1

    hints_left = 2
    score = 0

    print("\nNew game started — good luck!\n")
    while True:
        display_state(wrong, discovered, guessed_letters, hints_left)

        if "_" not in discovered:
            print("🎉 Congratulations — you guessed the word:", word)
            score = max(0, (len(word) * 10) - (wrong * 5))
            print("Your score for this round:", score)
            return score

        if wrong >= max_wrong:
            print(HANGMAN_STAGES[-1])
            print("💀 Game over. The word was:", word)
            return 0

        choice = get_valid_letter_input("Type a letter, 'hint', or 'quit': ")

        if choice == "quit":
            print("Quitting this round.")
            return 0

        if choice == "hint":
            if hints_left <= 0:
                print("No hints left.")
                continue

            print("\nHint options:")
            print("  1) Reveal one letter")
            print("  2) Show scrambled version of the word")
            h_choice = input("Choose 1 or 2: ").strip()
            if h_choice == "1":
                if reveal_one_letter(word, discovered, guessed_letters):
                    hints_left -= 1
                    print("One letter revealed!")
                else:
                    print("No letters left to reveal.")
            elif h_choice == "2":
                scrambled = scramble_word(word)
                hints_left -= 1
                print("Scrambled word:", scrambled)
            else:
                print("Invalid hint choice. Cancelled.")
            continue

        letter = choice
        if letter in guessed_letters:
            print(f"You already guessed '{letter}'. Try another letter.")
            continue

        guessed_letters.add(letter)
        if letter in word:
            for i, ch in enumerate(word):
                if ch == letter:
                    discovered[i] = letter
            print(f"Nice! '{letter}' is in the word.")
        else:
            wrong += 1
            print(f"Sorry — '{letter}' is not in the word. Wrong guesses: {wrong}/{max_wrong}")

        print()


def choose_difficulty():
    print("Choose difficulty:")
    print("  1) Easy  (short common words)")
    print("  2) Medium (moderate words)")
    print("  3) Hard  (longer / rarer words)")
    while True:
        choice = input("Enter 1, 2, or 3: ").strip()
        if choice == "1":
            return "easy"
        if choice == "2":
            return "medium"
        if choice == "3":
            return "hard"
        print("Invalid input — choose 1, 2, or 3.")


def main():
    print(textwrap.dedent("""
        ===========================
            HANGMAN (Terminal)
        ===========================
        Guess the word letter by letter.
        Commands available during play:
          - type a single letter (a-z) to guess
          - type 'hint' to use a hint (max 2 per round)
          - type 'quit' to forfeit the round
    """))
    total_score = 0
    rounds_played = 0

    while True:
        difficulty = choose_difficulty()
        score = play_round(difficulty)
        total_score += score
        rounds_played += 1

        print(f"\nTotal score: {total_score}  |  Rounds played: {rounds_played}")
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Thanks for playing! Final score:", total_score)
            break


if __name__ == "__main__":
    main()
