from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')

r_paddle.pong_paddle()
l_paddle.pong_paddle()

game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()