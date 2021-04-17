from turtle import *

bgcolor("black")
colors = ["red", "green", "orange", "purple", "blue", "yellow"]
n = 11
# speed(0)

for i in range(n*5):
	if i == ((n*5)-1):
		pencolor(colors[i % 6])
		forward((i*11)/2)
	else:
		pencolor(colors[i % 6])
		forward(i*11)
		right(144)

hideturtle()
done()
