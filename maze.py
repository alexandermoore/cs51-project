#CONSTANTS
maze_num_rows = 20
maze_num_cols = 20

class Maze:
        
    # An n x m list of booleans.
    board = []

    # A list of tuples. Each tuple is a coordinate and 
    # a square's distance from the start.
    # The list must be ordered from closest to start to furthest
    usable_squares = []

    # Coordinates of the START square
    start = (None,None) 

    # Coordinates of the END square
    end = (None,None)


    # Runtime
    runtime = None

    # A board customized to a specific initial state
    def __init__(self):
        self.board = self.make_board()

    def make_board(self):
        board = []
        for val in range(maze_num_rows):
            board.append([])
        for row in board:
            for val in range(maze_num_cols):
                row.append(False)
        return board
    
mango = Maze()

m = Maze()

