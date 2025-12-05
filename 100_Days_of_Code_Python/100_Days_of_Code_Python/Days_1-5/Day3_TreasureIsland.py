# VER 1.1 Bug Fixed - needed to have parentheses at the .lower function

# This is the Treasure Island Game Program

print("Welcome to Treasure Island.")
print("Your Mission is to find the treasure!")

# Takes the users choice and lowers it so it can be used in an if else statement
choice1 = input("You are at a crossroad, where do you want to go? Type Left or Right. ").lower()

if choice1 == "left":
    choice2 = input("You are at a river, do you wait to cross until a boat arrives, or do you swim? Type Wait or Swim. ").lower()
    
    if choice2 == "wait":
        choice3 = input("You come up to three doors, which door do you enter? Type Red, Green, or Blue. ").lower()
        
        if choice3 == "green":
            print("You found the treasure. You Win!")
        elif choice3 == "blue":
            print("You got attacked by Beasts. Game Over.")
        elif choice3 == "red":
            print("You fell into a fire pit. Game Over.")
       
        else:
            print("Game Over.")
    else:
        print("You got eaten by the fish. Game Over.")
else:
    print("You fell into a hole. Game Over.")