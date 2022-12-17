from turtle import Turtle
import random

class Enemy(Turtle):

    def __init__(self):
        super().__init__()
        self.enemy_list = [] # < -- this is what will hold ALL our enemies, and will allow us to add and remove enemies


    def create_enemy(self):
        ship_enemy = Turtle()
        ship_enemy.speed(0)
        ship_enemy.shape("turtle")
        ship_enemy.fillcolor("white")
        ship_enemy.seth(270)
        ship_enemy.penup()
        ship_enemy.x = random.randint(-200, 100) #<--- enemy ships can now spawn in random places at the top of screen
        ship_enemy.y = 200
        ship_enemy.goto(ship_enemy.x, ship_enemy.y)
        ship_enemy.move_x = 5 #< --- some movement speed
        ship_enemy.move_y = 20 #< --- when a ship reaches the border of the screen, it will move down this distance



