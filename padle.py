from turtle import Turtle
import time
poss=[(-320,20),(-320,00),(-320,-20)]
poss2=[(320,20),(320, 00),(320,-20)]
class Padle (Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.tltls=[]
        self.tltls1=[]
        self.tutles ()
        self.tutles1 ()
        self.head=self.tltls[0]
        self.tale=self.tltls[2]
        self.head1 = self.tltls1 [ 0 ]
        self.tale1= self.tltls1 [ 2 ]
        self.headin()
        self.moveup ( )
    def tutles(self) :
        for i in range ( 0 , 3 ) :
            tl0 = Turtle()
            tl0.shape ( "square" )
            tl0.shapesize(1)
            tl0.color ( "white" )
            tl0.penup ( )
            self.tltls.append ( tl0 )
            self.tltls [ i].goto ( poss [ i ] )
    def tutles1(self) :
        for i in range ( 0 , 3 ) :
            tl1 = Turtle()
            tl1.shape ( "square" )
            tl1.shapesize (1)
            tl1.color ( "white" )
            tl1.penup ( )
            self.tltls1.append ( tl1 )
            self.tltls1[i].goto ( poss2 [ i ] )
    def headin(self):
        self.head.lt(90)
        self.tale.rt(90)
        self.head1.lt ( 90 )
        self.tale1.rt ( 90 )
    def moveup(self):
        self.head.fd(20)
        for i in range (len(self.tltls)) :
            if i != 0 :
                self.tltls[i].goto(self.tltls[i-1].pos()[0],self.tltls[i-1].pos()[1]-20)
    def movedown (self):
        self.tale.fd(20)
        for i in range (len(self.tltls)-1,-1,-1) :
            if i != len(self.tltls)-1 :
                self.tltls[i].goto(self.tltls[i+1].pos()[0],self.tltls[i+1].pos()[1]-20)
    def moveup1(self) :
        self.head1.fd ( 20 )
        for i in range ( len ( self.tltls1 ) ) :
            if i != 0 :
                self.tltls1 [ i ].goto ( self.tltls1 [ i - 1 ].pos ( ) [ 0 ] , self.tltls1 [ i - 1 ].pos ( ) [ 1 ] - 20 )

    def movedown1(self) :
        self.tale1.fd ( 20 )
        for i in range ( len ( self.tltls1 ) - 1 , -1 , -1 ) :
            if i != len ( self.tltls1 ) - 1 :
                self.tltls1 [ i ].goto ( self.tltls1 [ i + 1 ].pos ( ) [ 0 ] , self.tltls1 [ i + 1 ].pos ( ) [ 1 ] - 20 )
