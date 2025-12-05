import random
from art import logo

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Takes a list of cards and returns the score calculated from the cards"""
    # Returns zero for the function if there is a Blackjack
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    # Checks for an Ace 
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    # Returns the sum of all the cards in the list
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "It's a draw!"
    elif c_score == 0:
        return "The opponent has a Blackjack, you lose!"
    elif u_score == 0:
        return "You have a Blackjack, you win!"
    elif u_score > 21:
        return "Your score is higher than 21, you lose!"
    elif c_score > 21:
        return "The computer's score is higher than 21, you win!"
    elif u_score > c_score:
        return "Your score is higher than the computer's, you win!"
    else:
        return "You lose"

def play_game(): 
    print(logo)

    # Blank Lists   
    user_cards = []
    computer_cards = []

    # Placeholder values for initialization
    user_score = -1
    computer_score = -1

    # Used to 
    is_game_over = False   
    
    # Draws two cards and appends them to the blank lists user_cards and computer_cards
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # While loop that takes in the main logic for the game and plays until
    while not is_game_over:

        # Updates user_score and computer_score
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # if condition that checks for Blackjack or if the user has higher than 21
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # While loop that does the logic for the dealer cards
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

# Prompt for the start of the game; Can loop infinitely if user always hits 'y'
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()