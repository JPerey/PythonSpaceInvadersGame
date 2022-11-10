#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3

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
9. create enemy class with enemy attributes ( shape, movement, border physics, etc.) - separate file X

10. give enemy/ bullet physics X
11. create scoreboard class with scoreboard attributes ( position, text, etc.) - separate file X
12. make enemy/ player interaction - if enemy reaches bottom then we lose X
13. create gameover screen X
14. create multiple "levels" X
15. create gameplay while loop - once gameover ask player if they want to play again

DONE


"""
from turtle import Turtle, Screen
from player import Player
from bullet_manager import Bullet
from enemy import Enemy
from scoreboard import Scoreboard
from functools import partial

# variables

play_again = "yes"

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
    game_over = False
    while not game_over:
        screen.update()
        bullet.move_bullet()
        enemy.move_enemy()

        for enemy_idx in enemy.enemy_list:
            if bullet.bullet_state == True and enemy_idx.distance(bullet) < 20:
                enemy_index = enemy.enemy_list.index(enemy_idx)
                enemy.enemy_death(enemy_idx, enemy_index)
                scoreboard.print_score(1)

            if enemy_idx.ycor() < -220:
                game_over = True
                scoreboard.game_over()

        if lvl == 1:
            for i in range(0, 4):
                enemy.create_enemy(lvl)
                i += 1
            lvl += 1

        elif lvl == 2 and len(enemy.enemy_list) == 0:
            for i in range(0, 8):
                enemy.create_enemy(lvl)
                i += 1
            lvl += 1

        elif lvl == 3 and len(enemy.enemy_list) == 0:
            for i in range(0, 10):
                enemy.create_enemy(lvl)
                i += 1
            lvl += 1

        elif lvl == 4 and len(enemy.enemy_list) == 0:
            for i in range(0, 10):
                enemy.create_enemy(lvl)
                i += 1
            lvl += 1

        elif lvl == 5 and len(enemy.enemy_list) == 0:
            for i in range(0, 10):
                enemy.create_enemy(lvl)
                i += 1
            lvl += 1
        if lvl == 6 and len(enemy.enemy_list) == 0:
            game_over = True
            scoreboard.game_won()


# event listeners
screen.onkey(player.move_left, "a")
screen.onkey(player.move_right, "d")
screen.onkey(partial(bullet.shoot_bullet, player), "space")
screen.listen()

# method calls
while play_again == "yes":
    game_loop()
    play_again = screen.textinput("Play again?", "Would you like to play again? 'yes' to play again:").lower()

screen.exitonclick()
