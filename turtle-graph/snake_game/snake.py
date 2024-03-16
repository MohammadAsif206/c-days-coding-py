from turtle import Screen, Turtle
from random import randint
import time

STAR_POS = [(0, 0), (-20, 0), (-40, 0)]
STEP = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segment_list = []
        self.create_snake()
        self.head = self.segment_list[0]

    def create_snake(self):
        for pos in STAR_POS:
            self.add_segment(pos)

    def move(self):
        for seq in range(len(self.segment_list) - 1, 0, -1):
            x = self.segment_list[seq - 1].xcor()
            y = self.segment_list[seq - 1].ycor()
            self.segment_list[seq].goto(x, y)
        self.head.forward(STEP)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_segment(self, pos):
        new_square = Turtle("square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(pos)
        self.segment_list.append(new_square)

    def extends(self):
        self.add_segment(self.segment_list[-1].position())
