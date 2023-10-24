"""
Practice using functions to draw a scene. In this assignment, I attempted to create a replica of Spongebob trapped in mud.
I used circles, semi-circles, rectangles, lines, and ovals. I was able to use my arms and shoes functions multiple times because of the 
creative way I thought to copy them. I ended up using a for loop to obviously tell the computer that each was a different object, just being created by the same function.
Also, I couldn't figure out how to change the background color of the python turtle window, so I just created a giant circle and colored it brown to look like mud. 
"""
__author__ = "730704135"
from turtle import Turtle, colormode, done


def main() -> None:
    """The entry point of my scene."""
    body: Turtle = Turtle()
    eye: Turtle = Turtle()
    nose: Turtle = Turtle()
    smile: Turtle = Turtle()
    arms: Turtle = Turtle()
    shoes: Turtle = Turtle()
    mud: Turtle = Turtle()
    draw_mud(mud, 600)
    draw_body(body, -137.5, -20, 275, 350, 10)
    draw_eyeL(eye, -68.75, 242.5, 47, 10)
    draw_eyeR(eye, 68.75, 242.5, 47, 10)
    draw_nose(nose, 0, 180, 20, 180)
    draw_smile(smile, 80, 180)
    draw_arms(arms, -200, 200)
    draw_arms(arms, 200, 200)
    draw_shoes(shoes, 60, 180, -200, -200)
    draw_shoes(shoes, 60, 180, 200, -200)
    done()


def draw_mud(mud_turtle: Turtle, mud_radius) -> None:
    """Draws mud for Spongebob to "bathe" in."""
    colormode(255)
    mud_turtle.ht()
    mud_turtle.penup()
    mud_turtle.goto(0, -500)
    mud_turtle.pendown()
    mud_turtle.begin_fill()
    mud_turtle.fillcolor(139, 69, 19)
    mud_turtle.circle(mud_radius)
    mud_turtle.end_fill()


def draw_body(rect_turtle: Turtle, rect_x: float, rect_y: float, rect_width: float, rect_height: float, line_width: float) -> None:
    """Draws a rectangle at the specified coordinates with the specified width and height and line width."""
    colormode(255)
    rect_turtle.ht()
    rect_turtle.penup()
    rect_turtle.goto(rect_x, rect_y)
    rect_turtle.pendown()
    rect_turtle.width(line_width / 6)
    rect_turtle.begin_fill()
    rect_turtle.fillcolor(255, 255, 0)
    i = 0
    while i < 4:
        if i == 0 or i % 2 == 0:
            rect_turtle.forward(rect_width)
            rect_turtle.left(90)
            i += 1
        else:
            rect_turtle.forward(rect_height)
            rect_turtle.left(90)
            i += 1    
    rect_turtle.end_fill()
    rect_turtle.speed(100)


def draw_eyeL(eye_turtle: Turtle, eye_x: float, eye_y: float, eye_radius: float, line_width: float) -> None:
    """Draws an eye at the specified coordinates with the specified side length and line width."""
    colormode(255)
    eye_turtle.pencolor(0, 0, 0)
    eye_turtle.ht()
    eye_turtle.penup()
    eye_turtle.goto(eye_x, eye_y - eye_radius)
    eye_turtle.pendown() 
    eye_turtle.width(line_width / 6)
    eye_turtle.begin_fill()
    eye_turtle.fillcolor(255, 255, 255)
    eye_turtle.circle(eye_radius)
    eye_turtle.end_fill()
    eye_turtle.width(line_width / 6)
    eye_turtle.penup()
    eye_turtle.goto(eye_x + eye_radius / 4, eye_y - eye_radius / 2)
    eye_turtle.pendown()
    eye_turtle.pencolor(105, 105, 105)
    eye_turtle.begin_fill()
    eye_turtle.fillcolor(135, 206, 235)
    eye_turtle.circle(eye_radius / 2)
    eye_turtle.end_fill()
    eye_turtle.width(line_width / 2)
    eye_turtle.penup()
    eye_turtle.goto(eye_x + eye_radius / 4, eye_y - 5)
    eye_turtle.pendown()
    eye_turtle.pencolor(0, 0, 0)
    eye_turtle.begin_fill()
    eye_turtle.fillcolor(0, 0, 0)
    eye_turtle.circle(eye_radius / 7)
    eye_turtle.end_fill()
    eye_turtle.speed(100)


def draw_eyeR(eye_turtle: Turtle, eye_x: float, eye_y: float, eye_radius: float, line_width: float) -> None:
    """Draws an eye at the specified coordinates with the specified side length and line width."""
    colormode(255)
    eye_turtle.pencolor(0, 0, 0)
    eye_turtle.ht()
    eye_turtle.penup()
    eye_turtle.goto(eye_x, eye_y - eye_radius)
    eye_turtle.pendown() 
    eye_turtle.width(line_width / 6)
    eye_turtle.begin_fill()
    eye_turtle.fillcolor(255, 255, 255)
    eye_turtle.circle(eye_radius)
    eye_turtle.end_fill()
    eye_turtle.width(line_width / 6)
    eye_turtle.penup()
    eye_turtle.goto(eye_x - eye_radius / 4, eye_y - eye_radius / 2)
    eye_turtle.pendown()    
    eye_turtle.pencolor(105, 105, 105)
    eye_turtle.begin_fill()    
    eye_turtle.fillcolor(135, 206, 235)
    eye_turtle.circle(eye_radius / 2)
    eye_turtle.end_fill()
    eye_turtle.width(line_width / 2)
    eye_turtle.penup()
    eye_turtle.goto(eye_x - eye_radius / 4, eye_y - 5)
    eye_turtle.pendown()
    eye_turtle.pencolor(0, 0, 0)
    eye_turtle.begin_fill()
    eye_turtle.fillcolor(0, 0, 0)
    eye_turtle.circle(eye_radius / 7)
    eye_turtle.end_fill()
    eye_turtle.speed(100)


def draw_nose(nose_turtle: Turtle, nose_x: float, nose_y: float, nose_radius: float, nose_limit: float) -> None:
    """Draws a nose at the specified coordinates with the specified radius."""
    nose_turtle.width(10 / 6)
    nose_turtle.ht()
    colormode(255)
    nose_turtle.color(0, 0, 0)
    nose_turtle.penup()
    nose_turtle.goto(nose_x, nose_y)
    nose_turtle.pendown()
    nose_turtle.circle(nose_radius, nose_limit)
    nose_turtle.speed(100)


def draw_smile(smile_turtle: Turtle, smile_radius: float, smile_limit: float) -> None:
    """Draws a smile with a specified radius and diameter."""
    smile_turtle.ht()
    smile_turtle.penup()
    smile_turtle.goto(smile_radius - 160, smile_radius + 50)
    smile_turtle.pendown()
    smile_turtle.width(10 / 6)
    smile_turtle.right(90)
    smile_turtle.circle(smile_radius, smile_limit)


def draw_arms(arms: Turtle, arms_x: float, arms_y: float) -> None:
    """Draws the arms of Spongebob."""
    colormode(255)
    arms.ht()
    arms.penup()
    arms.goto(arms_x, arms_y)
    arms.pendown()
    arms.color(255, 255, 0)
    arms.width(15)
    arms.setheading(270)
    
    for _ in range(1):
        arms.forward(200)
        arms.left(60)
        arms.forward(35)
        arms.backward(35)
        arms.right(120)
        arms.forward(35)
        arms.backward(35)
        arms.left(60)
        arms.forward(35)
    
    arms.penup()


def draw_shoes(shoes: Turtle, shoes_radius, shoes_limit, shoes_x, shoes_y) -> None:
    """Draws the shoes of Spongebob."""
    colormode(255)
    shoes.ht()
    shoes.penup()
    if shoes_x == -200:
        shoes.goto(shoes_x + 120, shoes_y)
    else:
        shoes.goto(shoes_x, shoes_y)
    shoes.pendown()
    shoes.setheading(90)
    shoes.begin_fill()
    shoes.fillcolor(0, 0, 0)

    for _ in range(1):
        shoes.circle(shoes_radius, shoes_limit)

    shoes.end_fill()
    shoes.penup()


if __name__ == "__main__":
    main()