import random
from art import logo


def deal_card():
    """Return a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    """Calculate and return the score of a hand."""

    # Blackjack
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # Convert Ace from 11 to 1 if score exceeds 21
    while sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
    """Determine the winner."""

    if user_score == computer_score:
        return " Draw!"
    if computer_score == 0:
        return " Lose, opponent has Blackjack!"
    if user_score == 0:
        return " Win with a Blackjack!"
    if user_score > 21:
        return " You went over. You lose!"
    if computer_score > 21:
        return " Opponent went over. You win!"
    if user_score > computer_score:
        return " You win!"
    return " You lose!"


def play_game():
    print(logo)

    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]

    game_over = False

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\nYour cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            choice = input(
                "Type 'y' to get another card, 'n' to pass: "
            ).lower()

            if choice == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print("\n----- Final Results -----")
    print(f"Your hand: {user_cards}, final score: {user_score}")
    print(f"Computer's hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("\nDo you want to play Blackjack? Type 'y' or 'n': ").lower() == "y":
    print("\n" * 20)
    play_game()