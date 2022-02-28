
from turtle_snake_scoreboard import Scoreboard
from turtle import Screen
from turtle_snake_class import Snake
from turtle_snake_food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("green")
screen.title("My snake game")
# Tracer controls the animation. To turn off animation, put 0.
# If you disable animation like this, it will stay off.
# If you turn off animation, you have to manually update screen and refresh it every time you want to see an update.
# Use a while loop for that.
screen.tracer(0)

scoreboard = Scoreboard()
snake = Snake()
food = Food()

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

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
