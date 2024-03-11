from turtle import *
import random

tim_t = Turtle()
tim_t.shape("turtle")
screen = Screen()


def draw_square():
    col = {"blue", "red", "yellow", "green"}
    i = 0
    while i < 200:
        i += 10
        j = i
        for c in col:
            tim_t.color(c)
            tim_t.forward(j + j)
            tim_t.left(90)
        for c in col:
            tim_t.color(c)
            tim_t.backward(j + j)
            tim_t.right(90)
        for c in col:
            tim_t.color(c)
            tim_t.forward(j + j)
            tim_t.right(90)
        for c in col:
            tim_t.color(c)
            tim_t.backward(j + j)
            tim_t.left(90)


# draw_square()
def draw_dashed_line():
    steps = 0
    dashed_line = {"black", "white"}
    while steps < 100:
        for s in dashed_line:
            steps += 5
            step = 5
            tim_t.color(s)
            tim_t.forward(step)


# draw_dashed_line()
# tim_t.left(245)
# tim_t.forward(100)
# tim_t.right(120)
# tim_t.forward(100)
# tim_t.right(125)
# tim_t.forward(100)

col = ["blue", "red", "yellow", "green", "black", "brown", "purple", "orange", ]


# def draw_shape(number_side):
#     angle = 360 / number_side
#     for _ in range(number_side):
#         c = random.choice(col)
#         tim_t.color(c)
#         tim_t.forward(100)
#         tim_t.right(angle)
#
#
# for shape_side in range(3, 11):
#     draw_shape(shape_side)

#
# def draw_shape_up(number_side):
#     angle = 360 / number_side
#     for _ in range(number_side):
#         c = random.choice(col)
#         tim_t.color(c)
#         tim_t.forward(100)
#         tim_t.left(angle)
#
#
# for number_side in range(3, 11):
#     draw_shape_up(number_side)
#
def draw_shape_l(number_side):
    angle = 360 / number_side
    for _ in range(number_side):
        c = random.choice(col)
        tim_t.color(c)
        tim_t.forward(100)
        tim_t.right(angle)



for shape_side in range(11,2, -1):
    draw_shape_l(shape_side)

# for i in range(3):
#     angle = 120
#     c = random.choice(col)
#     tim_t.color(c)
#     tim_t.right(angle)
#     tim_t.forward(100)
# for __ in range(4):
#     c = random.choice(col)
#     tim_t.color(c)
#     tim_t.right(90)
#     tim_t.forward(100)
# for __ in range(5):
#     c = random.choice(col)
#     tim_t.color(c)
#     tim_t.right(72)
#     tim_t.forward(100)
# for __ in range(6):
#     c = random.choice(col)
#     tim_t.color(c)
#     tim_t.right(60)
#     tim_t.forward(100)
# for __ in range(7):
#     c = random.choice(col)
#     tim_t.color(c)
#     tim_t.right(51.428571428)
#     tim_t.forward(100)
# for __ in range(8):
#     c = random.choice(col)
#     tim_t.color(c)
#     tim_t.right(45)
#     tim_t.forward(100)
# for __ in range(9):
#     c = random.choice(col)
#     tim_t.color(c)
#     tim_t.right(40)
#     tim_t.forward(100)
# for __ in range(10):
#     c = random.choice(col)
#     tim_t.color(c)
#     tim_t.right(36)
#     tim_t.forward(100)
#


# for steps in range(100):
#     for c in ("blue","red","green"):
#         color(c)
#         forward(steps)
#         right(30)

# while True:
#     tim_t.shape("turtle")
#
#     color("blue")
#     fd(200)
#     color("yellow")
#     left(170)
#     color("green")
#     if abs(pos()) < 1:
#         break
#
# for i in range(100):
#     steps = int(random() * 100)
#     angle = int (random() * 360)
#     tim_t.right(angle)
#     tim_t.fd(steps)


screen.exitonclick()
