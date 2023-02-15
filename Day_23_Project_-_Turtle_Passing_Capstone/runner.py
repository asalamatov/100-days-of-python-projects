from turtle import Turtle

class Runner(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('blue')
        self.penup()
        self.setheading(90)
        self.come_back()
    
    def move(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        
    def come_back(self):
        self.goto(0, -280)
        