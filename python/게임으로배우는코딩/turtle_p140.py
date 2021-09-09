import turtle
from time import sleep

scr = turtle.Screen()
scr.setup(700, 700)
scr.title('Snake Game!')
scr.bgcolor('darkblue')

b = turtle.Turtle()
b.color('green')
b.penup()
b.goto(-300, -200)
b.pendown()
for i in range(4):
    b.ht()
    b.forward(600)
    b.left(90)

t = turtle.Tutle()
t.shape('turtle')
t.penup()

t.shape('turtle')
t.penup()

def left():
    t.left(90)
def right():
    t.right(90)

scr.onkey(left, "Left")
scr.onkey(right, "Right")
scr.listen()

while True:
    t.forward(1)
