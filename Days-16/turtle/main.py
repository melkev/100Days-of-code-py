
from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("SlateBlue4")
timmy.speed("slow")

while True:
    timmy.forward(80)
    timmy.left(130)
    if abs(timmy.pos()) < 1:
        break


my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()