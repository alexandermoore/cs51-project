
class Maze:
    
    #CONSTANTS
    x_dim = 20
    y_dim = 20
    
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
    
    def make_board(self):
        board = []
        for val in range(y_dim):
            board.append([])
        for row in board:
            for val in range(x_dim):
                row.append(False)
        return board
    
    
m = Maze()

