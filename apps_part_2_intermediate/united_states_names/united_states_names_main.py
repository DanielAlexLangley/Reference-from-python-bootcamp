
import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "united_states_names_blank_map.gif"
screen.addshape(image)
turtle.shape(image)
turtle_state = turtle.Turtle()
turtle_state.hideturtle()
turtle_state.penup()
data = pandas.read_csv("united_states_names_list.csv")
correct_states = []
missed_states = []

while len(correct_states) < 50:
    answer = screen.textinput(title=f"{len(correct_states)}/50 States Correct",
                              prompt="What's another state's name?").title()
    if answer == "Exit":
        for state_name in data.state:
            if state_name not in correct_states:
                missed_states.append(state_name)
        data_dict = {"Missed states": missed_states}
        new_data_frame = pandas.DataFrame(data_dict)
        new_data_frame.to_csv("states_to_learn.csv")
        break
    for state_name in data.state:
        if answer == state_name and answer not in correct_states:
            state_data = data[data.state == answer]
            turtle_state.goto(int(state_data.x), int(state_data.y))
            turtle_state.write(answer)
            correct_states.append(state_name)

# turtle.mainloop()
# This is a way to keep our screen open, even though the code has stopped running.
# This .mainloop() is an alternative to screen.exitonclick()
