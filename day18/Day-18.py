import turtle
import random

# Setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Day 18 - Turtle Graphics")

t = turtle.Turtle()
t.speed(0)

# --- Challenge 1: Square ---
def draw_square():
    for _ in range(4):
        t.forward(100)
        t.right(90)

# --- Challenge 2: Dashed Line ---
def draw_dashed_line():
    for _ in range(10):
        t.pendown()
        t.forward(20)
        t.penup()
        t.forward(20)

# --- Challenge 3: Shapes ---
def draw_shape(sides):
    angle = 360 / sides
    for _ in range(sides):
        t.forward(100)
        t.right(angle)

# --- Challenge 4: Random Walk ---
def random_walk():
    directions = [0, 90, 180, 270]
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    t.pensize(5)
    for _ in range(100):
        t.color(random.choice(colors))
        t.forward(30)
        t.setheading(random.choice(directions))

# --- Challenge 5: Spirograph ---
def draw_spirograph():
    for _ in range(72):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        screen.colormode(255)
        t.color(r, g, b)
        t.circle(100)
        t.setheading(t.heading() + 5)

# --- Hirst Painting dots ---
def hirst_painting():
    t.penup()
    t.hideturtle()
    t.speed(0)
    colors = ["red","orange","yellow","green","blue","purple",
              "pink","white","coral","gold","cyan","magenta"]
    t.goto(-225, -225)
    for row in range(10):
        for col in range(10):
            t.dot(20, random.choice(colors))
            t.forward(50)
        t.backward(50 * 10)
        t.setheading(90)
        t.forward(50)
        t.setheading(0)

t.penup()
t.hideturtle()
hirst_painting()

screen.exitonclick()