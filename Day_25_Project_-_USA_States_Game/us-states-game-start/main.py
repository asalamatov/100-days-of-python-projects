from turtle import Turtle, Screen
import turtle
import pandas

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()  # when turtle.mainloop() is used, screen.exitonclick() is not needed
#
# # screen.exitonclick()

data = pandas.read_csv("50_states.csv")
states_table = data["state"]
states_list = states_table.to_list()
guessed_states = []

# Update score
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in states_list if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in states_list:
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(float(state_data.x), float(state_data.y))
        # t.write(answer_state)
        # OR
        t.write(state_data.state.item())
        guessed_states.append(answer_state)

