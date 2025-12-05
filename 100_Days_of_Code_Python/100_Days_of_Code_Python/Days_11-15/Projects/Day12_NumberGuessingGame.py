import random

# Banner
print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")

# Sets difficulty level
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
    player_lives = 10
elif difficulty == "hard":
    player_lives = 5

computer_choice = random.choice(range(1, 101))

is_not_game_over = True

while is_not_game_over:
    user_choice = int(input("Make a guess: "))

    if user_choice == computer_choice:
        print(f"You guessed the number correctly! The answer was {computer_choice} You win.")
        is_not_game_over = False

    elif user_choice > computer_choice:
        print("Too high. \nGuess again.")
        player_lives -= 1
        print(f"You have {player_lives} attempts remaining to guess the number.")

    elif user_choice < computer_choice:
        print("Too low. \nGuess again.")
        player_lives -= 1
        print(f"You have {player_lives} attempts remaining to guess the number.")
    
    if player_lives == 0:
        is_not_game_over = False