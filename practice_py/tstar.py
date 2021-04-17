from turtle import *

color("red", "blue")
shape("turtle")  # arrow, circle, classic, square, triangle, turtle
pensize(2)
speed(2)

begin_fill()

while True:
    forward(200)
    left(170)
    if abs(pos())<1:
        break

end_fill()

hideturtle()
done()
