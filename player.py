from turtle import Turtle


class Player(Turtle):  # <- turtle class needs to be in parens for inheritance

    def __init__(self):
        super().__init__()  # <- needed for inheritance
        self.shape("triangle")
        self.color("white")
        self.shapesize(1, 1)
        self.penup()
        self.goto(0, -220)
        self.setheading(90)
        self.x_move = 10  # <- distance increment that the player will move every time their movement methods are called

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
