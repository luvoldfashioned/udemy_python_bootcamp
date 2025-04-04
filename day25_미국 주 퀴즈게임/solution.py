import turtle
import pandas as pd


# create screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_state = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        # missing_states = []
        # for state in all_state:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        # new_data = pd.DataFrame(missing_states)
        missing_states = [state for state in all_state if (state not in guessed_states)]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break



    # If answer_state is one of the states in all the states of the 50_states.csv
    if answer_state in all_state:
        guessed_states.append(answer_state)
        all_state.remove(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
