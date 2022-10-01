from turtle import Turtle, Screen
import random




screen = Screen()

screen.setup(width=500, height=400)
user_stake = screen.textinput(title= "Whats your bet", prompt= "Which turtle do you think will win? ")
user_stake.lower()
screen.bgcolor("pink")



start_pos = [-120, -80, -40, 0, 40, 80]
color = ["blue", "red", "green", "purple", "black", "brown"]
race_turtle =[]


for num_tutle in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-240, y=start_pos[num_tutle])
    new_turtle.color(color[num_tutle])
    race_turtle.append(new_turtle)


game_on = False

if user_stake:
    game_on = True

while game_on:


    for turtle in race_turtle:

        if turtle.xcor() == 230:
            game_on = False

            winner = turtle.pencolor()
            if winner == user_stake:
                print(f"You won 😎 {winner} finished first")


            else:
                print(f"You lost 😢,{winner} finished first")

        distance = random.randint(1, 12)
        turtle.forward(distance)





screen.exitonclick()