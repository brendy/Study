import turtle
from time import sleep
t = turtle.Turtle()

length = 20
angle = 45

t.forward(length)
t.right(angle)
t.forward(length)
t.left(angle)

length = length * 2

t.forward(length)
t.right(angle)
t.forward(length)
t.left(angle)

angle = angle * 2

t.forward(length)
t.right(angle)
t.forward(length)
t.left(angle)

sleep(5)
