from turtle import Turtle
class Score (Turtle):
    def __init__(self):
        super().__init__()
        self.tllist = []
        self.turtles()
        self.going()
    def turtles(self):
        for i in range (0,3):
            tl0=Turtle()
            tl0.hideturtle ( )
            tl0.color ( "white" )
            tl0.penup ( )
            self.tllist.append(tl0)
    def going (self):
        self.tllist[0].goto((-30,250))
        self.tllist [1].goto( (30,250) )
    def weright (self,right,left) :
        self.tllist[1].write(f"{right}",align="center",font = ("arial",20,"normal"))
        self.tllist [ 0 ].write ( f"{left}" , align="center" , font=("arial" , 20 , "normal") )
