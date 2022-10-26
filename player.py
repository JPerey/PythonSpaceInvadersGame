from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("triangle")
        self.color("white")
        self.shapesize(1.5, 1.5)
        self.penup()
        self.goto(0, -220)
        self.seth(90)
        self.x_move = 10

    def move_left(self):
        new_x = self.xcor() - self.x_move
        if self.xcor() < -210:
            new_x = -210
        self.goto(new_x, -220)

    def move_right(self):
        new_x = self.xcor() + self.x_move
        if self.xcor() > 210:
            new_x = 210
        self.goto(new_x, -220)
