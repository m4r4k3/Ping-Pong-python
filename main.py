from turtle import Screen , Turtle
sc=Screen()
sc.tracer(0)
from padle import Padle
from pingpong import Pingpong
from ball import Ball
from scoreboard import Score
import time
n=0
sco=Score()
ball=Ball()
left = 0
right = 0
pp=Pingpong()
game_is_on=True
pd=Padle()
tl=Turtle()
t1=Turtle()
tl.pensize(3)
t1.pensize(3)
tl.color("white")
tl.hideturtle()
t1.hideturtle()
t1.color("white")
sc.setup(700,600)
sc.title("pong")
sc.bgcolor("black")
tl.lt(90)
t1.rt(90)
tl.speed("fastest")
t1.speed("fastest")
sc.update()
def nn ():
    global n
    n=1
while n== 0 :
    pp.ping()
    sc.update()
    time.sleep(0.2)
    pp.pong()
    sc.update()
    time.sleep(0.2)
    sc.listen()
    sc.onkey(nn , "space")
    sc.update()
pp.pongclear()
while tl.pos() [1] < 600:
    tl.fd(10)
    sc.update ( )
    tl.penup()
    sc.update ( )
    tl.fd(10)
    sc.update ( )
    tl.pendown()
    sc.update ( )
    t1.penup ( )
    sc.update ( )
    t1.fd ( 10 )
    sc.update ( )
    t1.pendown ( )
    sc.update ( )
    t1.fd ( 10 )
    sc.update ( )
while game_is_on :
    sco.weright(right,left)
    ball.movee()
    if ball.ycor()>=290 or ball.ycor()<=-290:
        ball.new_heading()
    if (pd.tltls[1].ycor()-30<=ball.ycor()) and (ball.ycor()<= pd.tltls[1].ycor()+30 ) and (ball.xcor()== pd.tltls[1].xcor()+20 ) :
        ball.xbounce()
    elif( pd.tltls1[1].ycor()-30<=ball.ycor()) and (ball.ycor()<= pd.tltls1[1].ycor()+30 ) and (ball.xcor()== pd.tltls1[1].xcor()-20 ):
        ball.xbounce ( )
    if ball.xcor() >= 350 :
        left+=1
        ball.xbounce ( )
        sco.tllist [ 0 ].clear()
    elif ball.xcor() <= -350 :
        right +=  1
        ball.xbounce ( )
        sco.tllist [ 1 ].clear ( )
    sc.listen()
    sc.onkeypress(pd.moveup,"z")
    sc.onkeypress(pd.movedown,"s")
    sc.listen()
    sc.onkeypress(pd.moveup1,"Up")
    sc.onkeypress( pd.movedown1 , "Down" )
    time.sleep(0.05)
    sc.update()
sc.exitonclick()