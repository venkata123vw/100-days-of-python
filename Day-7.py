import random

stages = ["""
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
"""]

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

word_length = len(chosen_word)

display = []

for _ in range(word_length):
    display += "_"

lives = 6
game_over = False

print("Welcome to Hangman!")

while not game_over:

    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You already guessed '{guess}'.")

    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print(f"'{guess}' is not in the word.")
        
        if lives == 0:
            game_over = True
            print("You lose!")
            print(f"The word was: {chosen_word}")

    print(" ".join(display))

    print(stages[6 - lives])

    if "_" not in display:
        game_over = True
        print("You win!")