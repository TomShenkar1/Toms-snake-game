from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.total_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 265)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.total_score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.total_score += 1
        self.update_score()

    def reset(self):
        if self.total_score > self.high_score:
            self.high_score = self.total_score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.total_score = 0
        self.update_score()





