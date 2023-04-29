import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


def state_present(state, x, y):
    tim = turtle.Turtle()
    tim.color("black")
    tim.hideturtle()
    tim.penup()
    tim.goto(y=y, x=x)
    tim.write(arg=state, font=('Arial', 8, 'normal'))

guessed_state=[]
correct_ans = 0
while correct_ans < 50:
    guess_input = turtle.textinput(prompt="What's another State name?",
                                   title=f"{correct_ans}/50 States correct").title()

    data = pandas.read_csv("50_states.csv")
    all_states = data.state.to_list()
    all_x = data.x.to_list()
    all_y = data.y.to_list()
    if guess_input=="Exit":
        break
    if all_states.count(guess_input) > 0:
        guessed_state.append(guess_input)
        index = all_states.index(guess_input)
        state_present(guess_input, int(all_x[index]), int(all_y[index]))
        correct_ans += 1

# long cut
# missing_states=[]
# for state in all_states:
#     if state not in guessed_state:
#         missing_states.append(state)

#list comprehension representation of the above code
missing_states=[state for state in all_states if state not in guessed_state]

new_data=pandas.DataFrame(missing_states)
new_data.to_csv("Missing_states")

