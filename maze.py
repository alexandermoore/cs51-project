#CONSTANTS
maze_num_rows = 30
maze_num_cols = 30

class Maze:
    
    '''***************** FIELDS *****************'''
    
    # An maze_num_rows x maze_num_cols array of booleans
    board = []

    # A list of squares; has different uses in generator and solver
    usable_squares = []

    # Coordinates of the START square
    start = (None,None) 

    # Coordinates of the END square
    end = (None,None)

<<<<<<< HEAD
    r = None
    c = None

=======
>>>>>>> 738bc9b3d7d8d33904b649b6582c38ddc79de1ee
    # Current coordinates of maze solver or generator
    coordinates = (None,None)
    
    # Current direction maze generator is facing
    direction = None
    
    end_placement_countdown = None
    maze_incomplete = True
    runtime = None
    
    '''***************** METHODS *****************'''
    
    # A board customized to a specific initial state
    def __init__(self):
        self.board = self.make_board()
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

m = Maze()

