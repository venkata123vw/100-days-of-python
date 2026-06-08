# Day 8 — Caesar Cipher

## What I Learned

- Using the alphabet list as a lookup table for character positions
- Applying the modulo operator `%` to wrap around the alphabet (position % 26)
- Writing a single function that handles both encode and decode using direction parameter
- Negating the shift amount to reverse the cipher for decoding
- Iterating over strings with `for` loops and skipping non-alphabet characters
- Keeping non-letter characters (spaces, symbols) unchanged in the output
- Running a program in a loop until the user chooses to exit

## Project Built

**Caesar Cipher** — A command-line encryption tool that encodes and decodes secret messages using the Caesar Cipher technique. The user enters a message, a shift number, and a direction (encode/decode). The program shifts each letter by the given amount and handles wrap-around using modulo arithmetic.

## My Code

- [Day-8.py](https://github.com/venkata123vw/100-days-of-python/blob/main/Day-8.py)

## Key Takeaway

One function with a direction parameter is cleaner than two separate functions. Modulo arithmetic is the elegant trick that makes the cipher wrap around the alphabet seamlessly — a concept that shows up everywhere in programming.
