rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

rock_scissor_paper = [rock, paper, scissors]

player_select = rock_scissor_paper[int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors."))]
computer_select = rock_scissor_paper[random.randint(0,2)]
result = 0

if player_select==rock:
    if computer_select==rock:
        result = "You Draw"
    elif computer_select==scissors:
        result = "You win"
    elif computer_select==paper:
        result = "You lose"
elif player_select==scissors:
    if computer_select==rock:
        result = "You Lose"
    elif computer_select==scissors:
        result = "You Draw"
    elif computer_select==paper:
        result = "You Win"
elif player_select==paper:
    if computer_select==rock:
        result = "You Win"
    elif computer_select==scissors:
        result = "You Lose"
    elif computer_select==paper:
        result = "You Draw"


print(f"player_select:\r{player_select}\rcomputer_select{computer_select}\r{result}")