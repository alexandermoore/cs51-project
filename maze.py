class Maze:

    # An n x m list of booleans.
    board = []

    # A list of tuples. Each tuple is a coordinate and 
    # a square's distance from the start.
    usable_squares = [((0,0),3)]

    # Coordinates of the START square
    start = (0,0)

    # Coordinates of the END square
    end = (1,1)

    # Runtime
    runtime = 5    

    # A board customized to a specific initial state.
    def __init__(self):
        self.board = [[True,True,True,False,False,True,True,False,False,True],
           [True,False,True,False,True,True,False,False,True,False],
           [False,False,False,False,False,True,False,True,True,True],
           [False,True,False,True,False,False,False,False,False,True],
           [True,True,False,True,False,True,False,True,False,False],
           [True,False,False,True,True,False,False,True,False,True]]
        self.start = (0,1)
        self.end = (5,8)

mango = Maze()

