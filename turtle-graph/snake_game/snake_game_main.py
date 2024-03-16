from turtle import Screen, Turtle
from random import randint
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
DIR = ["Up", "Down", "Left", "Right"]
screen.tracer(0)
# TODO: Create Snake Body
sn = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(sn.up, DIR[0])
screen.onkey(sn.down, DIR[1])
screen.onkey(sn.left, DIR[2])
screen.onkey(sn.right, DIR[3])

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    sn.move()

    # detect collision
    if sn.head.distance(food) < 15:
        food.refresh()
        sn.extends()
        score.increase_score()
    # detect wall collision
    if sn.head.xcor() > 280 or sn.head.xcor() < -280 or sn.head.ycor() > 280 or sn.head.ycor() < -280:
        is_game_on = False
        score.game_over()

    # detect tail collision
    for seg in sn.segment_list[1:]:
        if sn.head.distance(seg) < 10:
            is_game_on = False
            score.game_over()

screen.exitonclick()
