import random

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")


def set_difficulty():
    level = input("Choose the difficulty. Type 'easy' or 'hard': ").lower()

    if level == "easy":
        return 10
    elif level == "hard":
        return 5
    else:
        print("Invalid input.")
        return None


def check_answer(guess, answer, attempts):
    if guess > answer:
        print("Too high.")
        return attempts - 1

    elif guess < answer:
        print("Too low.")
        return attempts - 1

    else:
        print(f"You got it! The answer was {answer}.")
        return attempts


def game():
    secret_number = random.randint(1, 100)
    attempts = set_difficulty()

    if attempts is None:
        return

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        new_attempts = check_answer(guess, secret_number, attempts)

        if guess == secret_number:
            return

        attempts = new_attempts

        if attempts > 0:
            print("Guess again.\n")

    print("You've run out of guesses. You lose.")
    print(f"The number was {secret_number}.")


game()