import turtle as turtle_mode
import random

turtle_mode.colormode(255)
tim = turtle_mode.Turtle()
screen = turtle_mode.Screen()

# colorgram.extract("image.jpg",36)

# co = colors[0]
# color_tuple = ""
# color_list = []
# for c in range (len(colors)):
#     rgb = colors[c]
#
#     t = (rgb.rgb.r,rgb.rgb.g,rgb.rgb.b)
#     color_list.append(t)
# print(color_list)

color_list = [(227, 226, 224), (230, 227, 229), (230, 230, 233), (225, 229, 226), (40, 100, 154), (205, 160, 102),
              (150, 83, 53), (157, 58, 82), (225, 206, 121), (112, 160, 201), (55, 116, 82), (194, 83, 105),
              (198, 160, 41), (37, 52, 125), (139, 28, 47), (23, 33, 82), (196, 126, 160), (57, 30, 20), (85, 121, 193),
              (69, 32, 45), (210, 85, 66), (71, 172, 113), (150, 34, 30), (235, 168, 158), (92, 94, 7), (116, 181, 150),
              (67, 174, 182), (27, 91, 72), (223, 173, 183), (32, 61, 44), (178, 187, 214), (172, 204, 173),
              (21, 85, 95), (163, 204, 212), (235, 199, 7)]

tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
for d in range(1, number_of_dots+1):
    tim.pencolor("white")
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if d % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen.exitonclick()
