from turtle import Turtle
import random

class Enemy(Turtle):

    def __init__(self):
        super().__init__()
        self.enemy_list = []
        # self.shape("turtle")
        # self.seth(270)
        # self.penup()
        # self.x = random.randint(-200, 100)
        # self.y = 200
        # self.goto(self.x, self.y)
        # self.move_x = 5
        # self.move_y = 20

    def create_enemy(self):
        ship_enemy = Turtle()
        ship_enemy.shape("turtle")
        ship_enemy.seth(270)
        ship_enemy.penup()
        ship_enemy.x = random.randint(-200, 100)
        ship_enemy.y = 200
        ship_enemy.goto(ship_enemy.x, ship_enemy.y)
        ship_enemy.move_x = 5
        ship_enemy.move_y = 20
        self.enemy_list.append(ship_enemy)

    def move_enemy(self):
        for enemy in self.enemy_list:
            new_x = enemy.xcor() + enemy.move_x
            enemy.goto(new_x, enemy.y)

            if enemy.xcor() > 200:
                enemy.y = enemy.y - enemy.move_y
                enemy.move_x = - (enemy.move_x * 1.05)
                enemy.goto(enemy.xcor(), enemy.y)

            if enemy.xcor() < -200:
                enemy.y = enemy.y - enemy.move_y
                enemy.move_x = - (enemy.move_x * 1.05)
                enemy.goto(enemy.xcor(), enemy.y)
                print(f"new y : {enemy.y}")



