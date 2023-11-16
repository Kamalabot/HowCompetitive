# Code for implementing the Snake movement on board 
# drawn on the console. Using the queue
import sys
import os

# Snake Class that contains the body list (queue)


class Snake:
    def __init__(self):
        self.body = [
            [3, 1],
            [3, 2],
            [3, 3],
            [3, 4]
        ]
# Draw method that draws the board as rows and columns 

    def draw(self):
        """Draws the board of 10 * 10 & then places snake on top of it"""
        # instantiate a grid
        grid = []
        # create 10 rows
        for r in range(0, 10):
            # each row will be a list
            row = []
            # In each row create to 10 col
            for c in range(0, 10):
                # Create a white space for each cell
                row.append(" ")
            # append the created row into the grid
            grid.append(row)
        # draw the snake inside the grid
        for part in self.body:
            row, col = part
            grid[row][col] = '0'
        # display the grid with vertical lines
        os.system('cls')
        for row in grid:
            print('|'.join(row))

# Move method that moves the tail of the snake

    def move(self, direction):
        """Moves the head of the snake by appending a new cell to 
        body, and poping the first element"""
        # Change that is to made to the head depending on the direction
        moves = dict({
            "Up": [-1, 0],
            "Down": [1, 0],
            "Right": [0, 1],
            "Left": [0, -1]
        })
        # changing the head of the snake
        x, y = moves[direction]
        # getting the current head of the snake
        head = self.body[-1]
        # Updating the head to direction
        newHead = [head[0] + x, head[1] + y]
        # append the new head to body
        self.body.append(newHead)
        # pop the current tail
        self.body.pop(0)

# process the input from the stdin for play 
    def play(self):
        while True:
            self.draw()
            # get the words, Up, Down, Right, Left
            key = sys.stdin.readline().strip()
            # print(key)
            self.move(key)


game = Snake()
game.play()
# game.draw()
# print("-"*20)
# game.move('up')
# game.draw()
# print("-"*20)
# game.move('right')
# game.draw()