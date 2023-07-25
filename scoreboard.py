from turtle import Turtle


x_cor = 0
y_cor = 270

FONT = ("Courier", 20, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        file = open("new_file.txt")
        self.score = 0
        self.high_score = int(file.read())
        self.print_score()
        file.close()

    def print_score(self):
        self.clear()
        self.color("red")
        self.penup()
        self.hideturtle()
        self.goto(x=x_cor, y=y_cor)
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align="center", font=FONT)
        self.draw_line()

    def increment(self):
        self.score += 1
        self.clear()
        self.draw_line()
        self.print_score()

    def restart(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        file = open("new_file.txt", mode="w")
        file.write(str(self.high_score))
        self.print_score()

    def draw_line(self):
        self.penup()
        self.color("white")
        self.goto(x=-300, y=270)
        self.pendown()
        self.forward(600)
