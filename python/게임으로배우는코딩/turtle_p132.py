import turtle
from time import sleep
t = turtle.Turtle()

colors = ['red', 'blue', 'green', 'yellow']

for i in colors :
    t.color(i)
    t.forward(150)
    t.left(90)

sleep(2)
