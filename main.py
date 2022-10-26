# Gameplan
"""
1. create screen ( width= 500, height= 500, etc.) X
1a. provide space background for screen
2. create border X
3. create player class with player attributes ( shape, position, pic, etc.) - separate file X
4. create player movement functions X
5. make screen listen for key presses X
6. check player cannot move past border X

7. create bullet class with bullet attributes ( shape, position, etc.) - separate file X
8. shoot bullet every time key is pressed ( give bullet movement, give it a way to return to player position once
it reaches top of screen X
9. create enemy class with enemy attributes ( shape, movement, border physics, etc.) - separate file

10. give enemy/ bullet physics
11. create scoreboard class with scoreboard attributes ( position, text, etc.) - separate file
12. make enemy/ player interaction - if enemy reaches bottom then we lose
13. create gameover screen
14. create a highscore text file that saves your high score
15. create multiple "levels"
16. create gameplay while loop - once gameover ask player if they want to play again

DONE


"""
from turtle import Turtle, Screen
from player import Player
from bullet_manager import Bullet
from enemy import Enemy
from scoreboard import Scoreboard
from functools import partial

# variables

BLACK = ""
game_over = False

screen = Screen()
screen.setup(width=540, height=540)
screen.title(" Space Invaders - 2022")
screen.bgcolor("black")
screen.tracer(1, 0.1)

border = Turtle()
border.shape("triangle")
border.penup()
border.color("white")
border.hideturtle()
border.speed(0)
border.goto(-240, -240)
border.pendown()
border.pensize(8)
for borderi in range(0, 4):
    border.forward(480)
    border.left(90)

player = Player()
bullet = Bullet()
enemy = Enemy()
scoreboard = Scoreboard()


def game_loop():
    lvl = 1
    while not game_over:
        screen.update()
        bullet.move_bullet()
        enemy.move_enemy()

        for enemy_idx in enemy.enemy_list:
            if bullet.bullet_state == True and enemy_idx.distance(bullet) < 20:
                enemy_index = enemy.enemy_list.index(enemy_idx)
                enemy.enemy_death(enemy_idx, enemy_index)
                scoreboard.print_score(1)

        if lvl == 1:
            for i in range(0, 4):
                enemy.create_enemy()
                i += 1
            lvl += 1


# event listeners
screen.onkey(player.move_left, "a")
screen.onkey(player.move_right, "d")
screen.onkey(partial(bullet.shoot_bullet, player), "space")
screen.listen()

# method calls
game_loop()

screen.exitonclick()
