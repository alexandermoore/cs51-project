from settings import *

class Maze:
    
    '''***************** FIELDS *****************'''
    
    # An maze_num_rows x maze_num_cols array of booleans
    board = []

    # A list of squares; has different uses in generator and solver
    usable_squares = []

    # A list of squares for smart_solver; keeps track of squares visited
    usable = []

    # Coordinates of the START square
    start = (None,None) 

    # Coordinates of the END square
    end = (0,0)

    # Current coordinates of maze solver or generator
    coord = (None,None)
    
    # Current direction maze generator is facing
    direction = None
    
    end_placement_countdown = None
    maze_incomplete = True
    runtime = None
    
    '''***************** METHODS *****************'''
    
    ''' __init__
    Constructor. Initializes the parameters and creates each of mazes, including runtime. It then
    calculates the average runtime. The only input is a list of seven floats between 0 and 1.
    RETURNS: No return value.
    ''' 
    def __init__(self):
        self.board = self.make_board()
        self.runtime = 0
        if display_maze_generation_in_real_time:
            end = (0,0)


    def make_board(self):
        board = []
        for val in range(maze_num_rows):
            board.append([])
        for row in board:
            for val in range(maze_num_cols):
                row.append(False)
        return board


