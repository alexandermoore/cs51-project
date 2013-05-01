maze_num_rows = 10
maze_num_cols = 10

class Tm:
    
    '''***************** FIELDS *****************'''
    
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
    
    '''***************** METHODS *****************'''
    
    # A board customized to a specific initial state
    def __init__(self):
        self.board = self.make_board()
        self.board[0][2] = True
        self.board[0][5] = True
        self.board[1][0] = True
        self.board[1][1] = True
        self.board[1][2] = True
        self.board[1][3] = True
        self.board[1][4] = True
        self.board[1][5] = True
        self.board[2][2] = True
        self.board[3][0] = True
        self.board[3][1] = True
        self.board[3][2] = True
        self.board[4][2] = True
        self.start = (4,2)
        self.end = (0,5)

#        if display_maze_generation_in_real_time:
#            end = (0,0)


    def make_board(self):
        board = []
        for val in range(maze_num_rows):
            board.append([])
        for row in board:
            for val in range(maze_num_cols):
                row.append(False)
        return board

m = Tm()

''' runtime of 6 or 8 
self.board[0][0] = True
self.board[1][0] = True
        self.board[1][1] = True
        self.board[1][2] = True
        self.board[0][2] = True
        self.board[2][2] = True
        self.board[3][2] = True
        self.board[3][3] = True
        self.start = (0,0)
        self.end = (3,3)
''' 
