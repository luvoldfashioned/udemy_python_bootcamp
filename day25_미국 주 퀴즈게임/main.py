# 1. Convert the quess to Title case
# 2. Check if th guess is among the 50 states
# 3. Write correct guesses onto the map
# 4. Use a loop to allow the user to keep guessing
# 5. Record the correct guesses in a list
# 6. Keep track of the score

# def get_mouse_click_coor(x, y):
#     print(x, y)


# # Event listener
# turtle.onscreenclick(get_mouse_click_coor)

# # 코드가 실행을 끝내도 화면이 계속 열려있도록 하는 함수
# turtle.mainloop()

import turtle
import pandas

states_data = pandas.read_csv("50_states.csv")
states_data["state"] = states_data["state"].str.lower()

# create screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# generate loop
# tracking right answer times
counter = 0
game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"{counter}/50 States Correct",
                                    prompt="What's another state's name?").lower()

    # game quit
    if answer_state is None:
        game_is_on = False

    if (states_data["state"] == answer_state).any():
        get_row = states_data[states_data.state == answer_state]
        get_x = int(get_row.x.iloc[0])
        get_y = int(get_row.y.iloc[0])

        text = turtle.Turtle()
        text.hideturtle()
        text.penup()
        text.goto(get_x, get_y)
        text.write(f"{answer_state}", align="center",
                   font=('Arial', 8, 'normal'))

        counter += 1

turtle.mainloop()
