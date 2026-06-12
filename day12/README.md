# Day 12 — Scope & Number Guessing Game

## What I Learned
- Local vs Global scope — variables inside functions
- Returning values from functions and using them elsewhere
- Breaking logic into focused functions — set_difficulty(), check_answer(), game()
- Using while loops with attempt counters
- Handling invalid input with return None
- Difficulty levels — Easy (10 attempts) vs Hard (5 attempts)

## Project Built
**Number Guessing Game** — Computer picks a secret number
between 1 and 100. Player chooses difficulty (easy/hard)
which sets the number of attempts. Game gives "too high"
or "too low" hints until the player guesses correctly or
runs out of attempts.

## My Code
- [Day-12.py](./Day-12.py)

## Key Takeaway
set_difficulty() returns a number — and that number controls
the entire game. Functions that return values are more
powerful than functions that just print things.
