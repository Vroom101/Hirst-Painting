import turtle as t
import random
color_list = [  (208, 160, 101), (150, 75, 37), (231, 213, 97), (245, 251, 247), (242, 247, 250), (132, 34, 21), (191, 156, 15), (87, 33, 21), (238, 174, 153), (21, 57, 80), (41, 117, 63), (31, 93, 135), (196, 98, 88), (2, 81, 115), (10, 99, 77), (194, 163, 165), (109, 159, 185), (73, 76, 40), (179, 209, 168), (106, 140, 129), (37, 27, 35), (78, 153, 168), (46, 50, 47), (134, 163, 150), (234, 178, 180), (2, 72, 136), (125, 64, 66), (118, 36, 39)]
swimmy = t.Turtle()
screen = t.Screen()
t.colormode(255)
swimmy.speed("fastest")
swimmy.penup()
swimmy.hideturtle()
swimmy.setheading(225)
swimmy.forward(300)
swimmy.setheading(0)
number_of_dots = 100
for dot_count in range(1 , number_of_dots+1):

    swimmy.dot(20 ,random.choice(color_list) )
    swimmy.forward(50)
    if dot_count % 10 == 0 :
        swimmy.setheading(90)
        swimmy.forward(50)
        swimmy.setheading(180)
        swimmy.forward(500)
        swimmy.setheading(0)
screen.exitonclick()