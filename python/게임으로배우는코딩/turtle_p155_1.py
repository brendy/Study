import turtle
import random
from time import sleep

scr = turtle.Screen()
scr.setup(700, 700)
scr.title('Snake Game!')
scr.bgcolor('darkblue')

b = turtle.Turtle() # 경계선
b.color('green')
b.penup()
b.goto(-330, -330)
b.pendown()
for i in range(4):
    b.ht()
    b.forward(660)
    b.left(90)

t = turtle.Turtle() # 거북이
t.shape('turtle')
t.color('orange')
t.penup()
t.goto(-200, 0)
t.pendown()

gg = turtle.Turtle() # 꼬리
gg.ht()
gg.color('darkblue')
gg.penup()
gg.goto(-210, 0)
gg.pendown()

food = turtle.Turtle() # 먹이
food.shape('circle')
food.color('Red')
food.penup()
food.speed(0)
food.goto(0, 0)

def left():
    t.left(90)
def right():
    t.right(90)

scr.onkey(left, "Left")
scr.onkey(right, "Right")
scr.listen()

i=0
x=[]
y=[]

while True:
    x.append(t.xcor())
    y.append(t.ycor())
    t.forward(10)
    if t.xcor() <= -330 or t.xcor() >= 330 :
        t.right(180)
    if t.ycor() <= -330 or t.ycor() >= 330 :
        t.right(180)
    if (abs(t.xcor() - food.xcor()) < 10) and (abs(t.ycor() - food.ycor()) < 10):
        food.goto(random.randint(-300, 300), random.randint(-300, 300))
        t.forward(10)
        x.append(t.xcor())
        y.append(t.ycor())
        i+=1
    sleep(0.3)
    gg.goto(x[0], y[0])
    del x[0]
    del y[0]
