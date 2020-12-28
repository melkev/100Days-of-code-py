from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# config screen
screen = Screen()
screen.setup(width=1000, height=800)
screen.bgcolor("black")
screen.title("snake game by python")
screen.tracer(0)

# object
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collisions with wall
    if snake.head.xcor() > 490 or snake.head.xcor() < -490 or snake.head.ycor() > 390 or snake.head.ycor() < -390:
        scoreboard.reset_score()
        snake.reset_game()

    # Detect collision with tail.
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset_score()

screen.exitonclick()
