# 10x10 dots
# size 20 distance 50

# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)
import turtle
import random

color_list = [(43, 2, 176), (79, 253, 174), (226, 149, 109), (230, 225, 253),
              (160, 3, 82), (4, 211, 101), (3, 138, 64), (246, 42, 127),
              (109, 108, 247),
              (252, 253, 53), (184, 184, 251), (211, 106, 5), (35, 35, 252),
              (177, 112, 248), (139, 1, 0), (252, 36, 35), (50, 240, 56),
              (216, 114, 171), (16, 127, 144), (85, 248, 252),
              (188, 39, 109), (23, 5, 107), (8, 209, 215), (99, 8, 50),
              (231, 163, 205), (204, 119, 35), (112, 6, 4)]


tim = turtle.Turtle()

turtle.colormode(255)

tim.speed("fastest")
tim.penup()
tim.hideturtle()
y_index = -100
tim.goto(-100, y_index)

y_index = -100

for i in range(10):
    for i in range(10):
        ran_num = random.randint(0, len(color_list)-1)
        tim.dot(20, color_list[ran_num])
        tim.forward(50)
    y_index += 50
    tim.goto(-100, y_index)

screen = turtle.Screen()
screen.exitonclick()
