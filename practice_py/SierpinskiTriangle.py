from turtle import *

bgcolor("black")
speed(1)


def drawTriangle(points, color):
    pencolor(color)
    fillcolor(color)
    up()
    goto(points[0][0], points[0][1])
    down()
    begin_fill()
    goto(points[1][0], points[1][1])
    goto(points[2][0], points[2][1])
    goto(points[0][0], points[0][1])
    end_fill()


def getMid(p1, p2):
    return ((p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)


def sierpinski(points, degree):
    colormap = ["#7B2CBF", "#5A189A", "#3C096C", "#240046", "#10002B"]
    drawTriangle(points, colormap[degree])
    if degree > 0:
        sierpinski([points[0],
                    getMid(points[0], points[1]),
                    getMid(points[0], points[2])],
                   degree-1)
        sierpinski([points[1],
                    getMid(points[0], points[1]),
                    getMid(points[1], points[2])],
                   degree-1)
        sierpinski([points[2],
                    getMid(points[2], points[1]),
                    getMid(points[0], points[2])],
                   degree-1)


if __name__ == "__main__":

    p = [
        [-100, -50],
        [0, 100],
        [100, -50]
    ]

    d = 4

    sierpinski(p, d)

    hideturtle()
    done()
