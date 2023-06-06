from turtle import Turtle
class Pingpong (Turtle) :
    def __init__(self):
        super().__init__()
        self.hideturtle ( )
        self.co()
    def co (self):
        self.color ( "purple" )
    def ping (self):
        self.clear ( )
        self.color ( "purple" )
        self.write("ping" , False , align = "center", font=("bauhaus 93" , 50 , "normal"))
    def pong (self) :
        self.clear ( )
        self.color("cyan")
        self.write ( "pong" , False , align="center" , font = ("bauhaus 93" , 50 , "normal"))
    def pongclear (self):
        self.clear()