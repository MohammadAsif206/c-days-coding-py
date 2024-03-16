from turtle import Turtle, Screen
from random import  randint

tim = Turtle()
screen = Screen()

screen.setup(width=500,height=400)
user_bid = screen.textinput(title="Make your bid: ", prompt="Which turtle will win the race? Enter a color")
c = ["red","orange","yellow","green","blue","purple"]
pos = [-150,-100,-50,0,50,100]
list_turtle = []
for turtle in range(6):
    new_t = Turtle("turtle")
    new_t.penup()
    new_t.color(c[turtle])
    new_t.goto(-230, pos[turtle])
    list_turtle.append(new_t)
is_race_on = False
if user_bid:
    is_race_on = Turtle

while is_race_on:
    for turtle in list_turtle:
        if turtle.xcor()>230:
            is_race_on = False
            win_color = turtle.pencolor()
            if win_color == user_bid:
                print(f"You've won! The {win_color} is the winner")
            else:
                print(f"You've lost! The {win_color} is the winner")
        rd = randint(0,10)
        turtle.forward(rd)

# tr = Turtle(shape="turtle")
# to = Turtle(shape="turtle")
# ty = Turtle(shape="turtle")
# tg = Turtle(shape="turtle")
# tb = Turtle(shape="turtle")
# tp = Turtle(shape="turtle")
#
# tr.color(c[0])
# to.color(c[1])
# ty.color(c[2])
# tg.color(c[3])
# tb.color(c[4])
# tp.color(c[5])
# tr.penup()
# to.penup()
# ty.penup()
# tg.penup()
# tb.penup()
# tp.penup()
#
# print(user_bid)
#
#
#
# tr.goto(-200,-100)
# to.goto(-200,-150)
# ty.goto(-200,-50)
# tg.goto(-200,0)
# tb.goto(-200,50)
# tp.goto(-200,100)
#
# tim.shape("turtle")
# def move_forward():
#     tim.forward(50)
# def move_backward():
#     tim.backward(50)
# def move_left():
#     tim.left(50)
# def move_right():
#     tim.right(50)
#
# def cls():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# screen.listen()
# screen.onkey(move_forward,"w")
# screen.onkey(move_backward,"s")
# screen.onkey(move_left,"a")
# screen.onkey(move_right,"b")
# screen.onkey(cls,"c")


screen.exitonclick()
