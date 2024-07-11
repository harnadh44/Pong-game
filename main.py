from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.title("pong game")
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

ball = Ball()
scoreboard = Scoreboard()
paddle_l = Paddle((-350, 0))
paddle_r = Paddle((350, 0))

screen.onkeypress(paddle_r.go_up, "Up")
screen.onkeypress(paddle_r.go_down, "Down")
screen.onkeypress(paddle_l.go_up, "w")
screen.onkeypress(paddle_l.go_down, "s")

is_game_on = True

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detecting the collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R paddle misses:
    if ball.xcor() > 380:
        ball.restPosition()
        scoreboard.l_point()

    # Detect L paddle misses:
    if ball.xcor() < - 380:
        ball.restPosition()
        scoreboard.r_point()
screen.exitonclick()

