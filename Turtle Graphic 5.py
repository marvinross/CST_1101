import turtle
wb = turtle.Screen()
wb.bgcolor("LightBlue")
a = turtle.Turtle()
a.speed(0)
a.pencolor("DarkBlue")
a.pensize(1)
x = 0

while x < 650:
    a.forward(2+x)
    a.right(90.899)
    x = x+1

wb.exitonclick()
