import turtle
from time import sleep
t = turtle.Turtle()

for i in range(100) :
    t.forward(i*3)
    t.left(90)

sleep(2)
