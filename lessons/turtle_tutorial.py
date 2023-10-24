from turtle import Turtle, colormode, done
side_length: int = 300
from random import randint
leo : Turtle = Turtle()
colormode(255)
leo.fillcolor(200, 5, 1)
leo.pencolor(1, 200, 2)
leo.penup()
leo.goto(-125, -125)
leo.pendown()
leo.begin_fill()
leo.speed(50)
i: int = 0
while i <= 2:
    leo.forward(side_length)
    leo.left(120)
    i += 1
leo.end_fill()
leo.hideturtle()


test: Turtle = Turtle()
test.pencolor(255, 1, 1)
test.penup()
test.goto(125, 125)
test.pendown()
test.speed(20)
test.width(20)
idx: int = 0
while idx < 41:
    if idx < 21:
        test.forward(10)
        test.left(18)
    else:
        test.right(18)
        test.forward(10)
    idx += 1



bob: Turtle = Turtle()
bob.pencolor(1, 1, 255)
bob.penup()
bob.goto(-125, -125)
bob.pendown()
bob.width(20)
bob.speed(20)
width: int = 50
i: int = 0
colors: list[str] = ["Black", "Blue", "Red", "Orange", "Purple", "Green"]
while (i < 20):
    width *= .95
    bob.width(width)
    bob.pencolor(f"{colors[randint(0, 5)]}")
    bob.forward(side_length)
    bob.left(120)
    i += 1
bob.hideturtle()
done()