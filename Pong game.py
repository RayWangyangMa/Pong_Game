import turtle
import time

win = turtle.Screen()
win.title("Pong")
win.bgcolor("black")
win.setup(width=800, height=600)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 4  # Increased speed
ball.dy = -4  # Increased speed

# Score Variables
score_a = 0
score_b = 0

# Score Display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write(f"Player A: {score_a}  Player B: {score_b}",
                    align="center", font=("Courier", 24, "normal"))


def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    if y > -240:
        y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    if y > -240:
        y -= 20
    paddle_b.sety(y)


win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

while True:
    win.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 410:
        score_a += 1
        score_display.clear()
        score_display.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=(
            "Courier", 24, "normal"))
        time.sleep(1)  # pause for 1 second before resetting the ball
        ball.hideturtle()  # hide the ball
        ball.goto(0, 0)  # reset the ball to the center
        ball.showturtle()  # show the ball again
        ball.dx = 4  # reset the ball direction and speed
        ball.dy *= -1

    if ball.xcor() < -410:
        score_b += 1
        score_display.clear()
        score_display.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=(
            "Courier", 24, "normal"))
        time.sleep(1)  # pause for 1 second before resetting the ball
        ball.hideturtle()  # hide the ball
        ball.goto(0, 0)  # reset the ball to the center
        ball.showturtle()  # show the ball again
        ball.dx = -4  # reset the ball direction and speed
        ball.dy *= -1

    if (ball.dx > 0) and (350 > ball.xcor() > 340) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.color("blue")
        ball.dx *= -1.1  # Increase speed

    elif (ball.dx < 0) and (-350 < ball.xcor() < -340) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.color("red")
        ball.dx *= -1.1  # Increase speed
