# Player 1 enters a word; Player 2 tries to guess it.
secret_word = input("Player 1, enter a secret word: ").lower()

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

guessed_letters = []
wrong_guesses = 0
max_chances = 6

print("\nWelcome to Hangman!")
print("You have 6 chances to guess the word.\n")

while wrong_guesses < max_chances:
    displayed_word = ""

    # Show a letter only if the player has guessed it.
    for letter in secret_word:
        if letter in guessed_letters:
            displayed_word = displayed_word + letter + " "
        else:
            displayed_word = displayed_word + "_ "

    print(HANGMAN_PICTURES[wrong_guesses])
    print("Word:", displayed_word)
    print("Chances left:", max_chances - wrong_guesses)

    # The word has no blanks, so the player wins.
    if "_" not in displayed_word:
        print("You won! Great job!")
        break

    guess = input("Guess one letter: ").lower()

    # Conditions check whether the input is valid, repeated, right, or wrong.
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.\n")
    elif guess in guessed_letters:
        print("You already guessed that letter.\n")
    elif guess in secret_word:
        guessed_letters.append(guess)
        print("Correct guess!\n")
    else:
        guessed_letters.append(guess)
        wrong_guesses = wrong_guesses + 1
        print("Wrong guess!")
        print("Wrong guesses:", wrong_guesses, "out of", max_chances, "\n")
        print(HANGMAN_PICTURES[wrong_guesses])

if wrong_guesses == max_chances:
    print("Game over! The word was:", secret_word)