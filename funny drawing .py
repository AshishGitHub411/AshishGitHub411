import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("#1e1e2f")
screen.title("Funky Face using Turtle 😜")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Function to draw filled circle
def circle(color, radius, x, y):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Head
circle("#ffcc70", 150, 0, 0)

# Eyes
circle("white", 30, -50, 40)
circle("white", 30, 50, 40)
circle("black", 12, -45, 45)
circle("black", 12, 55, 45)

# Funky eyebrows
t.width(6)
t.color("black")
t.penup()
t.goto(-80, 80)
t.pendown()
t.setheading(20)
t.forward(60)

t.penup()
t.goto(80, 80)
t.pendown()
t.setheading(160)
t.forward(60)

# Nose (triangle)
t.penup()
t.goto(0, 20)
t.pendown()
t.color("#ff6f61")
t.begin_fill()
t.setheading(-90)
for _ in range(3):
    t.forward(40)
    t.left(120)
t.end_fill()

# Funky mouth
t.penup()
t.goto(-70, -40)
t.pendown()
t.color("#d7263d")
t.width(8)
t.setheading(-30)
t.circle(80, 120)

# Cheeks
circle("#ff9aa2", 20, -80, -10)
circle("#ff9aa2", 20, 80, -10)

# Text
t.penup()
t.goto(0, -200)
t.color("white")
t.write("FUNKY FACE 😎", align="center",
        font=("Comic Sans MS", 20, "bold"))

turtle.done()
