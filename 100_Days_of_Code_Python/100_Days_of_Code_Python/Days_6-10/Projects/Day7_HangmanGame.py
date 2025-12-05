# Hangman Project
import random
import hangman_art
import hangman_words

print(hangman_art.logo)

# Randomly chosen word from the list of words
chosen_word = random.choice(hangman_words.word_list)

placeholder = ""
for letter in chosen_word:
    placeholder += "_"

print(f" Word to guess: {placeholder}")

game_over = False
lives = 6
correct_letters = []

while not game_over:
    # Takes a user input as a string character
    letter_guess = input("Guess a letter: ").lower()

    if letter_guess in correct_letters:
        print(f"You already guessed {letter_guess}.")

    display = ""
    # Iterates through each letter from the random word
    for letter in chosen_word:
        if letter == letter_guess:
            display += letter
            correct_letters.append(letter_guess)
        elif letter in correct_letters: # if condition that checks if the letter is already in correct letters and if it is, it will add the letter to the display
            display += letter 
        else:
            display += "_"

    print(display)

    if letter_guess not in chosen_word:
        lives -= 1
        print(f"You guessed {letter_guess}, that's not in the word. You lose a life.")
        
        if lives == 0:
            print("You are out of lives, game over!")
            game_over = True

    print(hangman_art.stages[lives])  
    print(f"{lives}/6 LIVES LEFT")  

    if "_" not in display:
        print("You win!")
        game_over = True