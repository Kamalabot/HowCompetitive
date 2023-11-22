# Coding the snake game to test my capability
import os
# Snake will be a objects which will be initialized with a queue, that is made of list


class Snake:
    def __init__(self) -> None:
        self.body = [
            [2, 2],
            [3, 2],
            [3, 3],
            [3, 4]
        ]


# Create a game class that will have grid, move method
class Game:
    # Initialize the game with initial position of player
    def __init__(self, player: Snake) -> None:
        self.player = player

    def grid(self):
        # create a board variable
        board = []
        # create a loop with range of ten
        for i in range(0, 10):
            # create row list to hold elements
            row = []
            # create a loop to run all the ten cols
            for j in range(0, 10):
                #append empty spaces in rows
                row.append(' ')
            # append the filled row to board
            board.append(row)
        # update the board with snake position
        for coord in self.player.body:
            board[coord[1]][coord[0]] = '*'
        # clear the screen
        os.system('cls')
        # print the board
        for row in board:
            print("|".join(row))
    
    def move(self, direct):
        # create a dictionary containing the changes that will occur to the body
        move_dict = {
            "w": [0, -1],
            "s": [0, 1],
            "d": [1, 0],
            "a": [-1, 0]
        }
        # create the new extension 
        new_part = [self.player.body[-1][0] + move_dict[direct][0],
                    self.player.body[-1][1] + move_dict[direct][1]]
        # pop the end of the player body
        self.player.body.pop(0)
        # append the new_part
        self.player.body.append(new_part)



player = Snake()
game = Game(player)  # initialize the game
game.grid()  # print the grid

try:
    while True:
        # get the direction
        direction = input("w, a, s, d :")
        # move the player
        game.move(direction)
        # draw the grid with new player
        game.grid()
except KeyboardInterrupt as e:
    print("see you later...", e)
