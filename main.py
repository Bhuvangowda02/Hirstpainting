# import colorgram
#
#
# rgb_colors= []
# colors = colorgram.extract('img.jpg', 80)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b= color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as t
import random

t.colormode(255)
monkey = t.Turtle()
monkey.speed("fastest")
monkey.penup()
monkey.hideturtle()
color_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159,49),
              (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (223, 21, 120),
              (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11),
              (10, 228, 238), (73, 212, 168), (65, 231, 239), (217, 88, 51),(19,27,98),
              (176, 176, 233), (239, 168, 161), (249, 8, 48), (5, 246, 222), (243, 15, 14)]


monkey.setheading(225)
monkey.forward(300)
monkey.setheading(0)
dots = 100

for dot_count in range(1 , dots+1):
    monkey.dot(20, random.choice(color_list))
    monkey.forward(50)
    if dot_count % 10 == 0:
        monkey.setheading(90)
        monkey.forward(50)
        monkey.setheading(180)
        monkey.forward(500)
        monkey.setheading(0)

screen = t.Screen()
screen.exitonclick()
