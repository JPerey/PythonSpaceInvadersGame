from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(-220, 240)
        self.score = 0
        self.print_score(add=0)

    def print_score(self, add=0):
        self.clear()
        self.goto(-220, 245)
        self.score += add
        self.write(f"{self.score} ", True, align="center", font=("Arial", 22, "normal"))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(" G A M E O V E R", True, align= "center", font=("Arial", 32, "normal"))
        self.goto(0,-30)
        self.write(f"S C O R E : {self.score}", True, align="center", font=("Arial", 20, "normal"))

    def game_won(self):
        self.clear()
        self.goto(0, 0)
        self.write(" Y O U  W O N", True, align= "center", font=("Arial", 32, "normal"))
        self.goto(0, -30)
        self.write(f"S C O R E : {self.score}", True, align="center", font=("Arial", 20, "normal"))
