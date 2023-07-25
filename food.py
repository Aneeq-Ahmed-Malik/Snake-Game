from turtle import Turtle
import random

COLORS = ["red", "yellow", "green", "RoyalBlue", "magenta", "purple", "orange"]


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.refresh()

    def refresh(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 260)
        self.color(random.choice(COLORS))
        self.goto(random_x, random_y)
