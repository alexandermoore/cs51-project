from maze import *
import math
import random
#from solver import *

num_mazes = 10

class Generator:
    #FIELDS
	
    #parameters
    start_loc_col = 1
    start_loc_row = 1
    p_jump = 1
    p_forward = 1
    p_birds_eye = 1
    return_dist = 1
    end_time = 1
    
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
        start_loc_col = params[0]
        start_loc_row = params[1]
        p_jump = params[2]
        p_forward = params[3]
        p_birds_eye = params[4]
        return_dist = params[5]
        end_time = params[6]
        for val in range(num_mazes):
            m = Maze()
            self.generate(m)
            Solver.solve(m)
            self.mazes.append(m)
        self.calc_average_runtime
	
    def calc_avg_runtime(self):
        total_time = 0
        for maze in mazes:
             total_time = total_time + maze.runtime
        return total_time/len(mazes)
    
    def generate(self,m):
        #initialize maze
        start_row = int(math.floor(self.start_loc_row * (maze_num_rows-2) + 1.5))
        start_col = int(math.floor(self.start_loc_col * (maze_num_cols-2) + 1.5))
        m.start = (start_row, start_col)
        
        # enumeration
        North = 0
        East = 1
        South  = 2
        West = 3
        
        #variables for generate function
        self.coordinates = m.start
        self.direction = random.randrange (0, 3, 1)
        self.end_placement_countdown = math.floor(maze_num_cols * maze_num_rows * end_time / 2)
        self.maze_incomplete = True
        
        # gives self.coordinates of moving from square in self.direction dir
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
                print "error: moved not passed a valid self.direction"
            return
        
        # checks whether a path can be extended from square in the self.direction dir
        def check_dir(square,dir):
            shift_sq = move(square,dir)
            mid = m.board[shift_sq]
            far = m.board[move(shift_sq,dir)]
            left = m.board[move(shift_sq,(dir-1) % 4)]
            right = m.board[move(shift_sq,(dir+1) % 4)]
            border = (shift_sq[0] == 0) or (shift_sq[1] == 0) or (shift_sq[0] == maze_num_rows-1) or (shift_sq[1] == maze_num_cols-1)
            return (not(mid or far or left or right or border))
        
        # checks whether a new path can branch off from this square
        def check_sq(square):
            north = check_dir(square,North)
            east = check_dir(square,East)
            south = chech_dir(square,South)
            west = check_dir(square,West)
            return (north or east or south or west)
        
        # gets proposal_square
        def get_proposal_square():
            should_birds = random.random()
            if should_birds < p_birds_eye:
                # find closest square further than min_dist
                min_dist = math.sqrt(math.pow(self.coordinates[0] - m.start[0],2) + math.pow(self.coordinates[1] - m.start[1],2)) * return_dist
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
                if check_sq(m.usable_squares[proposal_square]):
                    success = True
                elif proposal_square == len(m.usable_squares)-1:
                    if proposal_square == 0:
                        # usable squares exhausted; set end of maze if not already set
                        if m.end == (False,False):
                            m.end = self.coordinates
                        break
                    # go back to start of usable_squares after reaching end
                    proposal_square = 0
                else:
                    # if proposal square fails, remove it and try next one
                    m.usable_squares.remove(m.usable_squares[proposal_square])
                    proposal_square = propoal_square + 1
                    
            if success == True:
                self.coordinates = usable_squares[proposal_square][0]
            return success
        
        # begin a new path (for instance, after jumping)
        def new_path():
            while not(check_dir(self.coordinates,self.direction)):
                self.direction = (self.direction + 1) % 4
            coorinates = move(self.coordinates,self.direction)
        
        # adds a given square to m.usable_squares
        def add_square(square):
            dist = math.sqrt(math.pow(square[0] - m.start[0],2) + math.pow(square[1] - m.start[1],2))
            insert_loc = 0
            while m.usable_squares[insert_loc][1] < dist:
                if insert_loc == len[m.usable_squares] - 1:
                    insert_loc = insert_loc + 1
                    break
                insert_loc = insert_loc + 1
            m.usable_squares.insert((square,dist),insert_loc)
        
        def continue_path():
            should_forward = random.random()
            should_right = random.random()
            while True:
                if should_forward < p_forward and check_dir(self.coordinates,self.direction):
                    move(self.coordinates,self.direction)
                elif should_right < 0.5 and check_dir(self.coordinates,(self.direction + 1) % 4):
                    self.direction = (self.direction + 1) % 4
                    move(self.coordinates,self.direction)
                elif check_dir(self.coordinates,(self.direction - 1) % 4):
                    self.direction = (self.direction - 1) % 4
                    move(self.coordinates,self.direction)
                elif check_dir(self.coordinates,(self.direction + 1) % 4):
                    self.direction = (self.direction + 1) % 4
                    move(self.coordinates,self.direction)
                else:
                    self.maze_incomplete = jump()
                    if self.maze_incomplete:
                        continue_path()
            return
   
        
        # begin tunneling from start
        m.usable_squares = [(self.coordinates,0)]
        m.board[self.coordinates[0]][self.coordinates[1]] = True
        new_path()
        
        # keep adding new squares to maze until no more can be added
        while self.maze_incomplete:
            add_square(self.coordinates)
            m.board[self.coordinates] = True
            if self.end_placement_countdown == 0:  
                m.end = self.coordinates
            self.end_placement_countdown = self.end_placement_countdown - 1
            should_jump = random.random()
            if should_jump < p_jump:
                self.maze_incomplete = jump()
            continue_path()
        
        ######### !!!!!!! Don't forget to reset variables after each maze !!!!!!!




g = Generator([0.5,0.5,0.5,0.5,0.5,0.5,0.5])

	