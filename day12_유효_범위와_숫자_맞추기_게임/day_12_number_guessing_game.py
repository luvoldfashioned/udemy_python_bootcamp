#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from number_guessing_game_art import logo
import random
ANSWER = random.randint(1, 100)
print(ANSWER)

def game_level(mode):
    if mode == "hard":
        for i in range(5):
            print(f"You have {6-i} attempts remaining to guess the number")
            guess = int(input("Make a guess: "))
            if ANSWER == guess:
                return "win"
            elif ANSWER > guess:
                print("Too low")
            elif ANSWER < guess:
                print("Too high")

            
    elif mode == "easy":
        for i in range(10):
            print(f"You have {11-i} attempts remaining to guess the number")
            guess = int(input("Make a guess: "))
            if ANSWER == guess:
                return "win"
            elif ANSWER > guess:
                print("Too low")
            elif ANSWER < guess:
                print("Too high")
    
    return "lose"


def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    mode = input("Choose a difficulty. type 'easy' or 'hard': ")
    if not (mode == "easy" or mode == "hard"):
        return "wrong input"
        
    result = game_level(mode)
    
    if result == "win":
        print(f"You got it! The answer was {ANSWER}")
    elif result == "lose":
        print("You've run out of guesses, you lose.")


play_game()