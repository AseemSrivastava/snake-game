from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # List of starting positions(constants) of turtles
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    # Create new segment and add it to end of snake
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    # Add new segment to snake by calling add segment method
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):  # Loop for making all segments follow the snake head
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    # Method to turn snake towards up
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    # Method to turn snake towards down
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    # Method to turn snake towards left
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    # Method to turn snake towards right
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
