from turtle import *

colors = ["red", "green", "orange", "purple", "blue", "yellow"]
bgcolor("black")

n=224

for i in range(n):

    if i==(n-1):
        pencolor(colors[i%6])
        width(i/100+1)
        forward(i/2)
    else:

        pencolor(colors[i%6])
        width(i/100+1)
        forward(i)
        left(59)

hideturtle()
done()
