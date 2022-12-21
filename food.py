import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Initialize side of food
        self.color("blue")  # Initialize color of food
        self.speed("fastest")  # initialize the speed of food when it moves from one location to another
        self.refresh()

    # Chose a random location for food and shift it there
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
