import turtle
import time
import random

win = turtle.Screen()
win.setup(width=800, height=600)
win.bgcolor("black")
win.title("screen")
win.tracer(0)

circle = turtle.Turtle()
for i in range(12):
    circle.right(30)
    circle.color(random.choice(["red", "blue", "green", "cyan", "brown", "gray"]))
    for i in range(360):
        circle.right(1)
        circle.forward(.5)
circle.hideturtle()

current_time = time.localtime()
cur_h = int(time.strftime("%H" , current_time))
cur_m = int(time.strftime("%M" ,current_time))
cur_s = int(time.strftime("%S" ,current_time))

sec_angle = 6 * cur_s

hour = turtle.Turtle()
hour.speed(0)
hour.color("blue")
hour.pensize(5)
hour.left(90)
hour.right((30 * cur_h) + (.5 * cur_m))
hour.forward(100)

minute = turtle.Turtle()
minute.speed(0)
minute.color("purple")
minute.pensize(5)
minute.left(90)
minute.right(6 * cur_m)
minute.forward(150)

second = turtle.Turtle()
second.speed(0)
second.color("cyan")
second.pensize(5)
second.left(90)
second.right(6 * cur_s)
second.forward(200)

body = turtle.Turtle()
body.speed(0)
body.pensize(5)
body.penup()
body.goto(0, 250)
body.pendown()
for i in range(360):
    if i % 30 == 0:
        body.left(90)
        body.color("green")
        body.forward(25)
        body.left(180)
        body.forward(50)
        body.left(180)
        body.forward(25)
        body.right(90)
        body.color("black")
    body.right(1)
    body.forward(4.35)
body.hideturtle()

def second_move():
    time.sleep(1)
    second.undo()
    second.right(6)
    second.forward(200)


def minute_move():
    minute.undo()
    minute.right(6)
    minute.forward(150)


def hour_move():
    hour.undo()
    hour.right(.5)
    hour.forward(100)


while True:
    win.update()

    second_move()
    sec_angle += 6

    if sec_angle >= 360:
        minute_move()
        hour_move()
        sec_angle = 0

