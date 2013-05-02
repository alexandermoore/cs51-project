maze_num_rows = 20
maze_num_cols = 20

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
        self.board[1][0] = True
        self.board[1][1] = True
        self.board[1][2] = True
        self.board[1][3] = True
        self.board[1][6] = True
        self.board[1][8] = True
        self.board[1][10] = True

        self.board[2][1] = True
        self.board[2][3] = True
        self.board[2][5] = True
        self.board[2][6] = True
        self.board[2][7] = True
        self.board[2][8] = True
        self.board[2][9] = True
        self.board[2][10] = True

        self.board[3][1] = True
        self.board[3][3] = True
        self.board[3][10] = True

        self.board[4][1] = True
        self.board[4][6] = True
        self.board[4][8] = True
        self.board[4][10] = True

        self.board[5][1] = True
        self.board[5][2] = True
        self.board[5][3] = True
        self.board[5][4] = True
        self.board[5][5] = True
        self.board[5][6] = True
        self.board[5][7] = True
        self.board[5][8] = True
        self.board[5][10] = True

        self.board[6][8] = True
        self.board[6][9] = True
        self.board[6][10] = True

        self.board[7][1] = True
        self.board[7][2] = True
        self.board[7][3] = True
        self.board[7][4] = True
        self.board[7][5] = True
        self.board[7][6] = True
        self.board[7][7] = True
        self.board[7][8] = True
        self.board[7][10] = True

        self.board[8][4] = True
        self.board[8][6] = True
        self.board[8][10] = True

        self.board[9][1] = True
        self.board[9][2] = True
        self.board[9][3] = True
        self.board[9][4] = True
        self.board[9][6] = True
        self.board[9][8] = True
        self.board[9][9] = True
        self.board[9][10] = True

        self.board[10][1] = True
        self.board[10][4] = True
        self.board[10][10] = True

        self.board[11][1] = True
        self.board[11][3] = True
        self.board[11][4] = True
        self.board[11][5] = True
        self.board[11][6] = True
        self.board[11][7] = True
        self.board[11][8] = True
        self.board[11][10] = True

        self.board[12][1] = True
        self.board[12][4] = True
        self.board[12][6] = True
        self.board[12][8] = True
        self.board[12][10] = True

        self.board[13][8] = True
        self.board[13][10] = True

        self.board[14][1] = True
        self.board[14][2] = True
        self.board[14][3] = True
        self.board[14][4] = True
        self.board[14][5] = True
        self.board[14][6] = True
        self.board[14][7] = True
        self.board[14][8] = True

        self.board[15][1] = True
        self.board[15][3] = True
        self.board[15][5] = True
        self.board[15][8] = True
        self.board[15][10] = True

        self.board[16][1] = True
        self.board[16][3] = True
        self.board[16][8] = True

        self.start = (4,8)
        self.end = (14,4)

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
''' runtime of 7, 10, 12 etc.
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
'''

