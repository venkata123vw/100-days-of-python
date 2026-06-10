# Day 10 — Functions with Outputs & Calculator

## What I Learned
- Functions that return values using `return`
- Storing functions as values inside a dictionary
- Calling functions dynamically using dictionary keys
- Recursive function calls — calling a function inside itself
- Using `.lower()` to handle user input case-insensitively
- Continuing calculation with previous answer or starting fresh

## Project Built
**Calculator** — A fully functional command-line calculator
that supports +, -, *, / operations. Built using 4 separate
functions stored in a dictionary. The user can chain
calculations continuously or start fresh — all inside
a recursive loop.

## My Code
- [Day-10.py](./Day-10.py)

## Key Takeaway
A dictionary can store functions as values — not just strings
or numbers. That single concept made the calculator elegant.
One dictionary replaced four if/elif statements completely.
