from maze import *
import math
import random
from solver import *
from display import *

num_mazes = 10

class Generator:
    #FIELDS
	
    #parameters
    start_loc_col = None
    start_loc_row = None
    p_jump = None
    p_forward = None
    p_birds_eye = None
    return_dist = None
    end_time = None
    
    # variables for class
    mazes = []
    avg_runtime = None
    parameter_list = [start_loc_col,start_loc_row,p_jump,p_forward,p_birds_eye,return_dist,end_time,mazes,avg_runtime]
    
    # enumeration
    North = 0
    East = 1
    South  = 2
    West = 3
    
    #variables for generate function
    coordinates = (None,None)
    direction = None
    end_placement_countdown = None
    maze_incomplete = None
    
	#METHODS
	
	#Constructor takes in params, float list of [start_loc_col,start_loc_row,p_jump,p_forward,p_birds_eye,
	#return_dist,end_time]
    def __init__(self,params):
        self.start_loc_col = params[0]
        self.start_loc_row = params[1]
        self.p_jump = params[2]
        self.p_forward = params[3]
        self.p_birds_eye = params[4]
        self.return_dist = params[5]
        self.end_time = params[6]
        for val in range(num_mazes):
            m = Maze()
            maze_incomplete = True
            self.generate(m)
            display_object.display(m)
            simple_solver.solve(m)
            self.mazes.append(m)
        self.calc_average_runtime
	
    def calc_avg_runtime(self):
        total_time = 0
        for maze in mazes:
             total_time = total_time + maze.runtime
        return total_time/len(mazes)
    
    def generate(self,m):
        #initialize maze
        start_row = int(math.floor(self.start_loc_row * (maze_num_rows-3) + 1.5))
        start_col = int(math.floor(self.start_loc_col * (maze_num_cols-3) + 1.5))
        m.start = (start_row, start_col)
        
        # enumeration
        North = 0
        East = 1
        South  = 2
        West = 3
        
        #variables for generate function
        self.coordinates = m.start
        self.direction = random.randrange (0, 3, 1)
        self.end_placement_countdown = math.floor(maze_num_cols * maze_num_rows * self.end_time / 2)
        self.maze_incomplete = True
        
        # gives coordinates of moving from square in direction dir
        def move(square,dir):
    #        print 'move'
            if (dir == North):
                return(square[0]+1,square[1])
            elif dir == South:
                return(square[0]-1,square[1])
            elif dir == East:
                return(square[0],square[1]+1)
            elif dir == West:
                return(square[0],square[1]-1)
            else:
                print "error: moved not passed a valid self.direction"
            return
        
        # checks whether a path can be extended from square in the direction dir
        def check_dir(square,dir):
            print square

            shift_sq = move(square,dir)
            border = (shift_sq[0] == 0) or (shift_sq[1] == 0) or (shift_sq[0] == maze_num_rows-1) or (shift_sq[1] == maze_num_cols-1)
            if border:
                return False
            mid = m.board[shift_sq[0]][shift_sq[1]]
            far = m.board[move(shift_sq,dir)[0]][move(shift_sq,dir)[1]]
            left = m.board[move(shift_sq,(dir-1) % 4)[0]][move(shift_sq,(dir-1) % 4)[1]]
            right = m.board[move(shift_sq,(dir+1) % 4)[0]][move(shift_sq,(dir+1) % 4)[1]]
            return (not(mid or far or left or right))
        
        # checks whether a new path can branch off from this square
        def check_sq(square):
            print 'check square'
            
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
                min_dist = math.sqrt(math.pow(self.coordinates[0] - m.start[0],2) + math.pow(self.coordinates[1] - m.start[1],2)) * self.return_dist
                while m.usable_squares[proposal_square][1] < min_dist:
                    proposal_square = proposal_square + 1
            else:
                # choose random square
                proposal_square = random.randint(0,len(m.usable_squares) - 1)
            return proposal_square
        
        # jumps to some square in usable_squares or returns False if unsuccessful
        def jump():
            print "jump"
            proposal_square = get_proposal_square()
            # try to find proposal square that can branch off a new path
            success = False
            while not(success):
                print "length(new): " + str(len(m.usable_squares))
                print proposal_square
                if check_sq(m.usable_squares[proposal_square][0]):
                    success = True
                else:
                    m.usable_squares.remove(m.usable_squares[proposal_square])
                    if len(m.usable_squares) == 0:
                        if m.end == (None,None):
                            m.end = self.coordinates
                        break
                    else:
                        proposal_square = (proposal_square + 1) % len(m.usable_squares)
                    
            if success == True:
                self.coordinates = m.usable_squares[proposal_square][0]
            return success
        
        # begin a new path (for instance, after jumping)
        def new_path():
            print "new path"
            
            while not(check_dir(self.coordinates,self.direction)):
                print self.direction
                self.direction = (self.direction + 1) % 4
            coorinates = move(self.coordinates,self.direction)
        
        # adds a given square to m.usable_squares
        def add_square(square):
            print "add square"
            
            dist = math.sqrt(math.pow(square[0] - m.start[0],2) + math.pow(square[1] - m.start[1],2))
            insert_loc = 0
            while m.usable_squares[insert_loc][1] < dist:
                if insert_loc == len(m.usable_squares) - 1:
                    insert_loc = insert_loc + 1
                    break
                insert_loc = insert_loc + 1
            m.usable_squares.insert(insert_loc,(square,dist))
        
        def continue_path():
            print "continue path"
            
            should_forward = random.random()
            should_right = random.random()
            if should_forward < self.p_forward and check_dir(self.coordinates,self.direction):
                print "forward"
                self.coordinates = move(self.coordinates,self.direction)
            elif should_right < 0.5 and check_dir(self.coordinates,(self.direction + 1) % 4):
                print "right"
                self.direction = (self.direction + 1) % 4
                self.coordinates = move(self.coordinates,self.direction)
            elif check_dir(self.coordinates,(self.direction - 1) % 4):
                print 'left'
                self.direction = (self.direction - 1) % 4
                self.coordinates = move(self.coordinates,self.direction)
            elif check_dir(self.coordinates,(self.direction + 1) % 4):
                print 'right cuz blocking'
                self.direction = (self.direction + 1) % 4
                self.coordinates = move(self.coordinates,self.direction)
            elif check_dir(self.coordinates,self.direction):
                print 'forward cuz blocking'
                self.coordinates = move(self.coordinates,self.direction)
            else:
                print 'must jump'
                self.maze_incomplete = jump()
                if self.maze_incomplete:
                    print "continue path repeat"
                    continue_path()
            print "done continuing path"
            return
   
        
        # begin tunneling from start
        m.usable_squares = [(self.coordinates,0)]
        m.board[self.coordinates[0]][self.coordinates[1]] = True
        new_path()
        
        # keep adding new squares to maze until no more can be added
        while self.maze_incomplete:
            add_square(self.coordinates)
            m.board[self.coordinates[0]][self.coordinates[1]] = True
            if self.end_placement_countdown == 0:  
                m.end = self.coordinates
            self.end_placement_countdown = self.end_placement_countdown - 1
            should_jump = random.random()
            if should_jump < self.p_jump:
                self.maze_incomplete = jump()
                if not(self.maze_incomplete):
                    break
            continue_path()
     #       display_object.display(m)
     #       print m.usable_squares





g = Generator([0.5,0.5,0.5,0.5,0.5,0.5,0.5])

	