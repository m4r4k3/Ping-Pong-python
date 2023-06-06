from turtle import Turtle
import random
class Ball (Turtle) :
    def __init__ (self):
        super().__init__()
        self.shapee()
        self.setheading(45)
        self.bbx= 20
        self.bby=10
    def shapee(self):
        self.color("white")
        self.shape('circle')
        self.speed("fastest")
        self.penup()
    def new_heading (self):
        self.bby*=-1
    def movee(self):
        self.goto((self.xcor()+self.bbx,self.ycor()+self.bby))
    def xbounce (self):
        self.bbx*=-1

