#CONSTANTS
maze_x_dim = 20
maze_y_dim = 20

class Maze:
        
    # An n x m list of booleans.
    board = []

    # A list of tuples. Each tuple is a coordinate and 
    # a square's distance from the start.
    usable_squares = []

    # Coordinates of the START square
    start = (False,False) 

    # Coordinates of the END square
    end = (False,False)

    # Runtime
    runtime = False

    # A board customized to a specific initial state
    def __init__(self):
        self.board = self.make_board()
	self.start = (False,False)
	self.end = (False,False)

	#self.board[1][1] = True
	#self.board[2][1] = True
	#self.board[0][2] = True
	#self.board[2][2] = True
	#self.board[3][2] = True
	#self.board[4][2] = True
	#self.board[0][3] = True
	#self.board[1][3] = True
	#self.board[2][3] = True
	#self.board[4][3] = True
	#self.board[0][4] = True
	#self.board[2][4] = True
	#self.board[3][5] = True
	#self.board[2][6] = True
	#self.board[3][6] = True
	#self.board[2][5] = True
	#self.board[1][0] = True
        #self.start = (1,0)
        #self.end = (2,5)
    
    def make_board(self):
        board = []
        for val in range(maze_y_dim):
            board.append([])
        for row in board:
            for val in range(maze_x_dim):
                row.append(False)
        return board
    
m = Maze()

