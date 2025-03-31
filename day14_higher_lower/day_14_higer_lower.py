#1. Breakedown the Ploblem
#2. start with the easiest
#3. Turn the problem into comments

#import modules
from higher_lower_logo import logo, vs
import random
from game_data import data


#display logo
print(logo)

#main function
def high_low_game():
    run_game = True
    score = 0

    #first choices
    person1 = random.choice(data)
    person2 = random.choice(data)

    while person1 == person2:
        person2 = random.choice(data)

    while run_game:
        print(f"\r  Compare A: {person1['name']}, a {person1['description']}, from {person1['country']}")
        print(vs)
        print(f"    Compare B: {person2['name']}, a {person2['description']}, from {person2['country']}")
        
        user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        if not (user_answer == 'a' or user_answer == 'b'):
            print("You input wrong answer")
            return 0
        
        if (person1["follower_count"] > person2["follower_count"]) and user_answer == 'a':
            person1  = person2

        elif (person1["follower_count"] < person2["follower_count"]) and user_answer == 'b':
            person1  = person2

        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            return 0

        person2 = random.choice(data)
        score += 1
        print(logo)
        print(f"You're right! Current score: {score}.")

high_low_game()

