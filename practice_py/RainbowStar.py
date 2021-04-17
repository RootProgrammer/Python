from turtle import *

bgcolor("black")
colors = ["red", "green", "orange", "purple", "blue"]

for i in range(5):
    pencolor(colors[i % 5])
    forward(333)
    right(144)

hideturtle()
done()
