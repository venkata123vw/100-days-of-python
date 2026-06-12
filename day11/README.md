# Day 11 — Blackjack Capstone Project

## What I Learned
- Breaking a complex project into small focused functions
- Using `random.choice()` to simulate card dealing
- Handling edge cases — Ace converting from 11 to 1
- Returning 0 as a special value to represent Blackjack
- Comparing scores with multiple conditions
- Calling a function inside a while loop to replay the game

## Project Built
**Blackjack Card Game** — A fully functional command-line
Blackjack game. Player and computer are dealt 2 cards each.
Player can hit or pass. Computer draws until score reaches 17.
Handles Blackjack, bust, Ace conversion and win/loss/draw.

## My Code
- [Day-11.py](./Day-11.py)

## Key Takeaway
A complex game becomes simple when you split it into
functions. deal_card(), calculate_score(), compare() —
each does one job. Together they build something real.
