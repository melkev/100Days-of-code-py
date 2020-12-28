import turtle
import pandas

screen = turtle.Screen()
screen.title("u.s game")

img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

# Read a csv file with pandas library
data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()
guessed_states = []

while len(guessed_states) < 51:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 correct states",
                                    prompt="what's another state's name").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_state if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    # if answer_state is one of state in all the states of the csv file
    if answer_state in all_state:
        guessed_states.append(answer_state)
        # if they got is right:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        # create a turtle to write the name of the state at the state's x and y coordate
        t.write(state_data.state.item())

# states_to_learn.csv

