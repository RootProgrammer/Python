from turtle import *

bgcolor("black")

sides=int(input("Enter Side Number(>2): "))
length=70
angle=360.0/sides
colors=["red","green","orange","purple","blue","yellow"]
goto(-333,0)
left(90)

for i in range(sides):
    pencolor(colors[i%6])
    forward(length)
    right(angle)

hideturtle()
done()
