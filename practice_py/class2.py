'''from turtle import *

color("green")
begin_fill()
forward(100)
left(120)
forward(100)
left(120)
forward(100)
end_fill()

done()'''

from random import *

n=randint(1,10)
ui=int(input("Guess The Number: "))

if n==ui:
    print("Congratulations!\nYou Won")
else:
    print("Sorry!!!\nYou Lost.\n")