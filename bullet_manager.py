from turtle import Turtle


class Bullet(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("triangle")
        self.color("yellow")
        self.shapesize(.5, .5)
        self.seth(90)
        self.penup()
        self.speed(0)
        self.hideturtle()
        self.bullet_speed = 10
        self.player_x = 0
        self.bullet_state = False

    def move_bullet(self):
        if self.bullet_state:
            new_y = self.ycor() + self.bullet_speed
            self.goto(x=self.player_x, y=new_y)
            if self.ycor() > 220:
                self.hideturtle()
                self.bullet_state = False

    def shoot_bullet(self, player):
        self.bullet_state = True
        self.player_x = player.xcor() # < - we get this value passed to us whenever the space button is pressed
        self.goto(self.player_x, -210)
        self.showturtle()

