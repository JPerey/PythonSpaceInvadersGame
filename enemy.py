from turtle import Turtle
import random


class Enemy(Turtle):

    def __init__(self):
        super().__init__()
        self.enemy_list = []


    def create_enemy(self, lvl):
        ship_enemy = Turtle()
        ship_enemy.speed(0)
        ship_enemy.shape("turtle")
        ship_enemy.fillcolor("white")
        ship_enemy.seth(270)
        ship_enemy.penup()
        ship_enemy.speed(0)
        ship_enemy.x = random.randint(-200, 100)
        ship_enemy.y = 200
        ship_enemy.goto(ship_enemy.x, ship_enemy.y)
        ship_enemy.move_x = 5 * lvl
        ship_enemy.move_y = 20
        if lvl > 2:
            ship_enemy.move_y = 20 * lvl
        self.enemy_list.append(ship_enemy)

    def move_enemy(self):
        for enemy in self.enemy_list:
            new_x = enemy.xcor() + enemy.move_x
            enemy.goto(new_x, enemy.y)

            if enemy.xcor() > 210:
                enemy.y = enemy.y - enemy.move_y
                enemy.move_x = - (enemy.move_x * 1.05)
                enemy.goto(enemy.xcor(), enemy.y)

            if enemy.xcor() < -210:
                enemy.y = enemy.y - enemy.move_y
                enemy.move_x = - (enemy.move_x * 1.05)
                enemy.goto(enemy.xcor(), enemy.y)

            # if enemy.distance(bullet) < 20:
            #     enemy_index = self.enemy_list.index(enemy)
            #     self.enemy_death(enemy, enemy_index)

    def enemy_death(self, enemy, enemy_index):
        enemy.goto(600, 600)
        self.enemy_list.pop(enemy_index)
