from maze import *
import math
import random
#from solver import *
from display import *

num_mazes = 10

class Generator:
    #FIELDS
	
    #parameters
    start_loc_col = None
    start_loc_row = 'hello'
    p_jump = None
    p_forward = None
    p_birds_eye = None
    return_dist = None
    end_time = None
    
    # variables
    mazes = []
    avg_runtime = None
    parameter_list = []
    
    # enumeration
    North = 0
    East = 1
    South  = 2
    West = 3
    
	#METHODS
	
    ''' __init__
    Constructor. Initializes the parameters and creates each of mazes, including runtime. It then
    calculates the average runtime. The only input is a list of seven floats between 0 and 1.
    RETURNS: No return value.
    -params[0] : start_loc_col = starting location as ratio of column/maze_num_cols
    -params[1] : start_loc_row = starting location as ratio of row/maze_num_rows
    -params[2] : p_jump = probability of jumping somewhere else in the maze when adding next square
    -params[3] : p_forward = if continuing current path, probability of moving forward (as opposed 
    to turning)
    -params[4] : p_birds_eye = if jumping, probability of doing so through a "birds-eye" calculation 
    as opposed to picking a random square
    -params[5] : return_dist = if doing a "birds-eye" jump, return_dist is the ratio of the desired 
    distance from start (in the square jumped to) to the current distance from the start distance 
    from start to desired distance from start in the square jumped to
    -params[6] : end_time = rough approximation of what percentage of maze will be completed when 
    end is placed
    ''' 
    def __init__(self,params):
        self.start_loc_col = params[0]
        self.start_loc_row = params[1]
        self.p_jump = params[2]
        self.p_forward = params[3]
        self.p_birds_eye = params[4]
        self.return_dist = params[5]
        self.end_time = params[6]
        self.parameter_list = [self.start_loc_col,self.start_loc_row,self.p_jump,self.p_forward,self.p_birds_eye,self.return_dist,self.end_time]
        for val in range(num_mazes):
            m = Maze()
            maze_incomplete = True
            self.generate(m)
            display_object.display(m)
            self.pythagorean_solve(m)
            self.mazes.append(m)
        self.avg_runtime = self.calc_avg_runtime()
	
    ''' calc_avg_runtime
    Takes the average of the runtimes of all mazes in mazes[].
    RETURNS: average runtime of the mazes
    '''
    def calc_avg_runtime(self):
        total_time = 0
        for maze in self.mazes:
             total_time = total_time + maze.runtime
        return total_time/len(self.mazes)
    
    ''' generate
    Takes a maze object and builds the maze. This includes: adding the maze to the board, adding
    coordinates to start and end, but not adding a value to runtime. Leaves usable_squares empty.
    RETURNS: No return value.
    - m : a maze with a board consisting of all Falses; no start, end, or runtime values; and an
    empty usable_squares list.
    '''
    def generate(self,m):
        # Convert start parameters into row/column numbers in a fair way, giving each square an equal opportunity to be selected (+1.5 so the (maze_num_rows - 3)th square has a fair chance to be selected)
        start_row = int(self.start_loc_row * (maze_num_rows-3) + 1.5)
        start_col = int(self.start_loc_col * (maze_num_cols-3) + 1.5)
        m.start = (start_row, start_col)
        
        # enumeration
        North = 0
        East = 1
        South  = 2
        West = 3
        
        #variables for generate function
        m.coodinates = m.start
        m.direction = random.randrange (0, 3, 1)
        m.end_placement_countdown = math.floor((maze_num_cols - 1) * (maze_num_rows - 1) * self.end_time / 2)
        m.maze_incomplete = True
        
        ''' move
        Gives coordinates of moving from square in direction dir. DOES NOT change m.coodinates.
        Cannot be called from a square on the border.
        RETURNS: No return value.
        -square : the square being moved from
        -dir : the direction in which to move
        '''
        def move(square,dir):
            if (dir == North):
                return(square[0]+1,square[1])
            elif dir == South:
                return(square[0]-1,square[1])
            elif dir == East:
                return(square[0],square[1]+1)
            elif dir == West:
                return(square[0],square[1]-1)
            else:
                print "error: moved not passed a valid direction"
            return
        
        # checks whether a path can be extended from square in the direction dir
        ''' check_dir
        Checks whether or not it is valid to move in direction dir from square. It checks the
        five surrounding squares.
        '''
        def check_dir(square,dir):
            shift_sq = move(square,dir)
            border = (shift_sq[0] == 0) or (shift_sq[1] == 0) or (shift_sq[0] == maze_num_rows-1) or (shift_sq[1] == maze_num_cols-1)
            if border:
                return False
            mid = m.board[shift_sq[0]][shift_sq[1]]
            left = m.board[move(shift_sq,(dir-1) % 4)[0]][move(shift_sq,(dir-1) % 4)[1]]
            right = m.board[move(shift_sq,(dir+1) % 4)[0]][move(shift_sq,(dir+1) % 4)[1]]
            shift_sq_2 = move(shift_sq,dir)
            far = m.board[shift_sq_2[0]][shift_sq_2[1]]
            far_left = m.board[move(shift_sq_2,(dir-1) % 4)[0]][move(shift_sq_2,(dir-1) % 4)[1]]
            far_right = m.board[move(shift_sq_2,(dir+1) % 4)[0]][move(shift_sq_2,(dir+1) % 4)[1]]
            return (not(mid or far or left or right or far_left or far_right))
        
        # checks whether a new path can branch off from this square
        def check_sq(square):
            north = check_dir(square,North)
            east = check_dir(square,East)
            south = check_dir(square,South)
            west = check_dir(square,West)
            return (north or east or south or west)
        
        # gets proposal_square up to len[m.usable_squares]-1
        def get_proposal_square():
            proposal_square = 0
            should_birds = random.random()
            if should_birds < self.p_birds_eye:
                # find closest square further than min_dist
                min_dist = math.sqrt(math.pow(m.coodinates[0] - m.start[0],2) + math.pow(m.coodinates[1] - m.start[1],2)) * self.return_dist
                while m.usable_squares[proposal_square][1] < min_dist:
                    proposal_square = proposal_square + 1
            else:
                # choose random square
                proposal_square = random.randint(0,len(m.usable_squares) - 1)
            return proposal_square
        
        # jumps to some square in usable_squares or returns False if unsuccessful
        def jump():
            proposal_square = get_proposal_square()
            # try to find proposal square that can branch off a new path
            success = False
            while not(success):
                if check_sq(m.usable_squares[proposal_square][0]):
                    success = True
                else:
                    m.usable_squares.remove(m.usable_squares[proposal_square])
                    if len(m.usable_squares) == 0:
                        if m.end == (None,None):
                            m.end = m.coodinates
                        break
                    else:
                        proposal_square = (proposal_square + 1) % len(m.usable_squares)        
            if success == True:
                m.coodinates = m.usable_squares[proposal_square][0]
            return success
        
        # begin a new path (for instance, after jumping)
        def new_path():
            while not(check_dir(m.coodinates,m.direction)):
                m.direction = (m.direction + 1) % 4
            coorinates = move(m.coodinates,m.direction)
        
        # adds a given square to m.usable_squares
        def add_square(square):
            dist = math.sqrt(math.pow(square[0] - m.start[0],2) + math.pow(square[1] - m.start[1],2))
            insert_loc = 0
            while m.usable_squares[insert_loc][1] < dist:
                if insert_loc == len(m.usable_squares) - 1:
                    insert_loc = insert_loc + 1
                    break
                insert_loc = insert_loc + 1
            m.usable_squares.insert(insert_loc,(square,dist))
        
        def continue_path():
            should_forward = random.random()
            should_right = random.random()
            if should_forward < self.p_forward and check_dir(m.coodinates,m.direction):
                m.coodinates = move(m.coodinates,m.direction)
            elif should_right < 0.5 and check_dir(m.coodinates,(m.direction + 1) % 4):
                m.direction = (m.direction + 1) % 4
                m.coodinates = move(m.coodinates,m.direction)
            elif check_dir(m.coodinates,(m.direction - 1) % 4):
                m.direction = (m.direction - 1) % 4
                m.coodinates = move(m.coodinates,m.direction)
            elif check_dir(m.coodinates,(m.direction + 1) % 4):
                m.direction = (m.direction + 1) % 4
                m.coodinates = move(m.coodinates,m.direction)
            elif check_dir(m.coodinates,m.direction):
                m.coodinates = move(m.coodinates,m.direction)
            elif check_dir(m.coodinates,(m.direction + 2) % 4):
                m.direction = (m.direction + 2) % 4
                m.coodinates = move(m.coodinates,m.direction)
            else:
                m.maze_incomplete = jump()
                if m.maze_incomplete:
                    continue_path()
            return
        
        # begin tunneling from start
        m.usable_squares = [(m.coodinates,0)]
        m.board[m.coodinates[0]][m.coodinates[1]] = True
        new_path()
        
        # keep adding new squares to maze until no more can be added
        while m.maze_incomplete:
            add_square(m.coodinates)
            m.board[m.coodinates[0]][m.coodinates[1]] = True
            if m.end_placement_countdown == 0:  
                m.end = m.coodinates
            m.end_placement_countdown = m.end_placement_countdown - 1
            should_jump = random.random()
            if should_jump < self.p_jump:
                m.maze_incomplete = jump()
                if not(m.maze_incomplete):
                    break
            continue_path()
     #       display_object.display(m)
    
    ''' pythagorean_solve
    Gives a dummy value for runtime, which is equal to the distance between start and end
    RETURNS: No return value.
    - m : a maze that needs a runtime value
    '''
    def pythagorean_solve(self,m):
        dist = math.sqrt(math.pow(m.end[0] - m.start[0],2) + math.pow(m.end[1] - m.start[1],2))
        m.runtime = dist
        return




g = Generator([0.4,0.2,0.2,0.9,0.5,0.5,0.9])
        #self.start_loc_col = params[0] = 0.0 or 1.0
        #self.start_loc_row = params[1] = 0.0 or 1.0
        #self.p_jump = params[2] = 0.9
        #self.p_forward = params[3] = ??
        #self.p_birds_eye = params[4] = 1.0
        #self.return_dist = params[5] = 0.0
        #self.end_time = params[6] = 0.9
	