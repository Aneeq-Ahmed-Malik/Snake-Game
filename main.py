from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score = ScoreBoard()
score.draw_line()


game_is_on = True

screen.listen()

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.snakes[0].distance(food) < 15:
        food.refresh()
        snake.extend_body()
        score.increment()

    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 260 or snake.head.ycor() < -300:
        score.restart()
        snake.refresh()

    for segment in snake.snakes[1:]:
        if snake.head.distance(segment) < 10:
            score.restart()
            snake.refresh()


screen.exitonclick()
