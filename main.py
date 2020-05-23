# ping pong game

import turtle

win = turtle.Screen()
win.title("Pong by @MehakGill")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# scores
player_a_score = 0
player_b_score = 0
scorecard = turtle.Turtle()
scorecard.color("white")
scorecard.penup()
scorecard.hideturtle()
scorecard.goto(0, 280)
scorecard.write("Player A: {}, Player B: {}".format(player_a_score, player_b_score), \
                False, align="center", font=("Courier", 12, "normal"))

# add left paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)

# add right paddle
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)

# add ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1


# paddle movement functions
def left_paddle_up():
    left_paddle.sety(left_paddle.ycor() + 20)


def left_paddle_down():
    left_paddle.sety(left_paddle.ycor() - 20)


def right_paddle_up():
    right_paddle.sety(right_paddle.ycor() + 20)


def right_paddle_down():
    right_paddle.sety(right_paddle.ycor() - 20)


# listen to keypress
win.listen()
win.onkeypress(left_paddle_up, "w")
win.onkeypress(left_paddle_down, "s")
win.onkeypress(right_paddle_up, "Up")
win.onkeypress(right_paddle_down, "Down")

while True:
    win.update()

    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.dy *= -1

    if ball.xcor() <= -390:
        player_b_score += 1
        scorecard.clear()
        scorecard.write("Player A: {}, Player B: {}".format(player_a_score, player_b_score), \
                        False, align="center", font=("Courier", 12, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() >= 390:
        player_a_score += 1
        scorecard.clear()
        scorecard.write("Player A: {}, Player B: {}".format(player_a_score, player_b_score), \
                        False, align="center", font=("Courier", 12, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # ball and paddle intersection
    if ball.xcor() <= -350 and (left_paddle.ycor() - 50 < ball.ycor() < left_paddle.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1

    if ball.xcor() >= 350 and (right_paddle.ycor() - 50 < ball.ycor() < right_paddle.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1
