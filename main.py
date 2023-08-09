import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(725, 491)

data = pandas.read_csv("50_states.csv")

states = data["state"]

correct_guess = []
while len(correct_guess) != 50:
    answer_input = turtle.textinput(title=f"{len(correct_guess)}/50 ", prompt="What's another state name? ").title()

    if answer_input == "Exit":
        missing_answers = [s for s in states if s not in correct_guess]

        states_to_learn = pandas.DataFrame(missing_answers)
        states_to_learn.to_csv("states_to_learn")
        break

    for state_name in states:
        if answer_input == state_name and answer_input not in correct_guess:
            # if the guess is right, place it in correct_guess list
            correct_guess.append(state_name)

            t = turtle.Turtle()
            t.hideturtle()
            t.penup()

            # get the coordinates of answer_input state
            coor = data[data.state == state_name]
            t.goto(int(coor.x), int(coor.y))

            # write state name
            t.write(state_name, align='center')
