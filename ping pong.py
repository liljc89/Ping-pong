import turtle

win = turtle.Screen()
win.title("Pong by JC")
win.bgcolor("Navy")
win.setup(width=800, height=600)
win.tracer(0)

# Score
score_a = 0
score_b = 0

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #Speed of animation, not paddle speed in game
paddle_a.shape("square")
paddle_a.color("yellow")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) #default is 20 pixels by 20 pixels
paddle_a.penup() #penup to make sure it doesnt draw a line
paddle_a.goto(-350, 0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) #Speed of animation, not paddle speed in game
paddle_b.shape("square")
paddle_b.color("yellow")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) #default is 20 pixels by 20 pixels
paddle_b.penup() # penup to make sure it doesnt draw a line
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0) #Speed of animation, not paddle speed in game
ball.shape("square")
ball.color("yellow")
ball.penup() #penup to make sure it doesnt draw a line
ball.goto(0, 0) #its 0, 0 because that's the middle of the screen
ball.dx = .1 #ball moves by 2 pixels
ball.dy = -.1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "bold"))

# Function
def paddle_a_up():
    y = paddle_a.ycor()  #.ycor = y coordinates
    y += 20 #adding 20 pixels to y coordinates
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()  #.ycor = y coordinates
    y -= 20 #taking 20 pixels from y coordinates
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()  #.ycor = y coordinates
    y += 20 #adding 20 pixels to y coordinates
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()  #.ycor = y coordinates
    y -= 20 #taking 20 pixels from y coordinates
    paddle_b.sety(y)

# Keyboard binding
win.listen() #listen to keyboard input
win.onkeypress(paddle_a_up, "w") # when user presses "w", call the function paddle_a_up
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up") 
win.onkeypress(paddle_b_down, "Down")


#Main Game Loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))

    # Paddle Ball Collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1