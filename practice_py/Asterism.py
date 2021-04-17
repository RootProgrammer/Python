from turtle import *

bgcolor("black")
colors = ["red", "green",  "blue", "orange", "purple"]
penup()
goto(-211, 45)
pendown()
speed(6)


def star(s):
    if s <= 10:
        return
    else:
        for i in range(5):
            pencolor(colors[i % 5])
            forward(s)
            star(s/3)
            right(144)


star(333)

hideturtle()
done()
