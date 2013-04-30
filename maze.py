#CONSTANTS
maze_num_rows = 50
maze_num_cols = 50

class Maze:
    
    ''''''' FIELDS '''''''
    
    # An maze_num_rows x maze_num_cols array of booleans
    board = []

    # A list of squares; has different uses in generator and solver
    usable_squares = []

    # Coordinates of the START square
    start = (None,None) 

    # Coordinates of the END square
    end = (None,None)

    # Current coordinates of maze solver or generator
    coordinates = (None,None)
    
    # Current direction maze generator is facing
    direction = None
    
    end_placement_countdown = None
    maze_incomplete = True
    runtime = None
    
    ''''''' METHODS '''''''
    
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

