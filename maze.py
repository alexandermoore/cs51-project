#CONSTANTS
maze_num_rows = 30
maze_num_cols = 30

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
    end = (-1,-1)

    r = None
    c = None
    coordinates = (None,None)
    direction = None
    end_placement_countdown = None
    maze_incomplete = True

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

m = Maze()

