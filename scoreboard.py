from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", move=False, align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_game(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.color("red")
    #     self.write(f"GAME OVER", move=False, align=ALIGN, font=FONT)
