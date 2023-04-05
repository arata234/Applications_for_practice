import pandas as pd
import turtle


if __name__ == "__main__":
    screen = turtle.Screen()
    screen.title("U.S. States Game")
    df = pd.read_csv("USA/50_states.csv")
    img ="USA/blank_states_img.gif"
    screen.addshape(img)
    turtle.shape(img)

    all_states = df.state.to_list()
    while all_states:
        answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
        if answer_state == "Exit":
            break
        if answer_state in all_states:
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            data = df[df.state==answer_state]
            t.goto(int(data.x), int(data.y))
            t.write(answer_state)
            all_states.remove(answer_state)
            print(all_states)

se = pd.Series(all_states)
se.to_csv("./USA/states_u_dont_know.csv", index=False, header=False)
    
