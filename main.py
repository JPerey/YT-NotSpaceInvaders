# Gameplan
'''
1. Create Screen ( width=540, height= 540, etc.) X
1a. provide space background for screen ( optional)
2. create border X
3. create player class with player attributes ( shape, position, pic, etc.) - separate file X
4. create player movement functions X
5. make screen listen for key presses X
6. check player cannot move past created border X

7. Create bullet class with attributes ( shape, position, etc.) - seperate file X
8. shoot bullet each time it is pressed( give bullet movement, way to return to player) X

9. create enemy class with enemy attributes ( shape, movement, border physics, etc.) - seperate file
10. give enemy bullet physics

11. create scoreboard class with attributes ( position, text, etc.) - seperate file
12 - make player/ enemy interaction - if enemy reaches player or bottom we lose
13 - create gameover screen

stretch -
14 - create multiple " levels"
15 - create gameplay loop
16 - add graphics

'''

from turtle import Turtle, Screen
from player import Player
from bullet_manager import Bullet
from enemy import Enemy
from functools import partial  # < needed to use partial functions

# Screen creation
screen = Screen()
screen.setup(width=540, height=540)
screen.title("Not Space Invaders")
screen.bgcolor("black")
screen.tracer(1, 0.1)  # <- will need to explain signifigance of this during shooting portion

# Border creation
border = Turtle()
border.shape("triangle")
border.penup()
border.color("white")
border.hideturtle()
border.speed(0)  # <- makes the movements of the specified turtle object instantaneous
border.goto(-240, -240)
border.pendown()
border.pensize(8)

for borderi in range(0, 4):
    border.forward(480)
    border.left(90)

# Object creation

player = Player()
bullet = Bullet()
enemy = Enemy()


# screen listening method and onkey methods

def game_loop():

    game_over = False
    enemy_limit = 5
    enemy_amount = 0
    while not game_over:

        screen.update()
        bullet.move_bullet()
        if enemy_amount < enemy_limit:
            enemy.create_enemy()
            enemy_amount += 1


# onkey methods

screen.onkey(player.move_left, "a")  # <- (method to be called when a particular button is pressed, button assignment)
screen.onkey(player.move_right, "d")
screen.onkey(partial(bullet.shoot_bullet, player), "space")  # < --- this will not work yet, need a partial function
screen.listen()  # <- tells the screen to listen for button presses

game_loop()

screen.exitonclick()  # <- needs to be added in order for screen to stay without dissapearing once code is done running
