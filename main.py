import turtle
import pandas

screen= turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

num_states_correct = 0
states_data = pandas.read_csv("50_states.csv")
states = states_data.state.to_list()
states_used = []

while num_states_correct < 50:
    is_a_state = False
    answer_state = screen.textinput(title=f"{num_states_correct}/50 States Correct",
                                    prompt="What's another state name?")
    answer_state = answer_state.title()

    if answer_state == "Exit":
    #     need_to_learn = []
    #     for s in states:
    #         if s not in states_used:
    #             need_to_learn.append(s)
        need_to_learn = [s for s in states if s not in states_used]
        #The above line replaces the several above lines of code commented out
        states_to_learn = pandas.DataFrame(need_to_learn)
        states_to_learn.to_csv("States_to_learn.csv")
        break



    for state in states:
        if answer_state == state:
            is_a_state = True
            chosen_state = state
            num_states_correct = num_states_correct + 1
            states_used.append(chosen_state)
            break

    if is_a_state == False:
        continue

    else:
        state_text = turtle.Turtle()
        state_text.hideturtle()
        state_text.penup()
        mask = states_data.state == chosen_state
        chosen_state_x = int(states_data.loc[mask, "x"])
        chosen_state_y = int(states_data.loc[mask, "y"])
        state_text.goto(chosen_state_x,chosen_state_y)
        state_text.write(f"{chosen_state}", align="center", font="Ariel")








# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

#Shouldn't use the below line bc don't want screen to exit as soon as we click it
screen.exitonclick()
