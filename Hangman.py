import random

WORDS = [
    "python",
    "computer",
    "programming",
    "keyboard",
    "algorithm",
    "developer",
    "function",
    "variable",
]

HANGMAN_PICTURES = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========""",
]


def play_game():
    word = random.choice(WORDS).upper()
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong_guesses = 6

    print("\nWelcome to HANGMAN!")
    print("Guess the hidden word one letter at a time. You have 6 wrong guesses.\n")

    while wrong_guesses < max_wrong_guesses:
        shown_word = " ".join(letter if letter in guessed_letters else "_" for letter in word)
        print(HANGMAN_PICTURES[wrong_guesses])
        print(f"\nWord: {shown_word}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) or 'None'}")
        print(f"Wrong guesses left: {max_wrong_guesses - wrong_guesses}")

        if all(letter in guessed_letters for letter in word):
            print(f"\nYou won! The word was {word}.")
            return

        guess = input("\nEnter one letter: ").strip().upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)
        if guess in word:
            print("Correct guess!")
        else:
            wrong_guesses += 1
            print("Wrong guess!")

    print(HANGMAN_PICTURES[max_wrong_guesses])
    print(f"\nGame over! The word was {word}.")


def main():
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()