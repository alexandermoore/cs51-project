import random, sys, math
from maze import *



class generator:
# Function definition is here
    def generate(self,m):

        # variables that I get from elsewhere (will be deleted in actual implementation)
        maze_x_dim = 20
        maze_y_dim = 20
        start_loc_x = 0.23
        start_loc_y = 0.87
        p_birds_eye = 0.76
        return_dist = 0.87
        p_jump = 0.789
        p_forward = 0.34
        end_time = .66
        
        #initialize maze
        m.start = (start_loc_x * maze_x_dim, start_loc_y * maze_y_dim)
        
        # local variables
        coordinates = m.start
        direction = random.randrange (0, 3, 1)
        place_end = maze_x_dim * maze_y_dim * end_time / 2
        
        # enumeration
        North = 0
        East = 1
        South  = 2
        West = 3
        
        # gives coordinates of moving from square in direction dir
        def move(square,dir):
            if dir = North:
                return(square[0]+1,square[1])
            elif dir = South:
                return(square[0]-1,square[1])
            elif dir = East:
                return(square[0],square[1]+1)
            elif dir = West:
                return(square[0],square[1]-1)
            else:
                print "error: moved not passed a valid direction"
        
        # checks whether a path can be extended from square in the direction dir
        def check_dir(square,dir):
            shift_sq = move(square,dir)
            mid = m.board[shift_sq]
            far = m.board[move(shift_sq,dir)]
            left = m.board[move(shift_sq,(dir-1) % 4)]
            right = m.board[move(shift_sq,(dir+1) % 4)]
            border = (shift_sq[0] = 0) or (shift_sq[1] = 0) or (shift_sq[0] = maze_x_dim-1) or (shift_sq[1] = maze_y_dim-1)
            return (not(mid or far or left or right or border))
        
        # checks whether a new path can branch off from this square
        def check_sq(square):
            north = check_dir(square,North)
            east = check_dir(square,East)
            south = chech_dir(square,South)
            west = check_dir(square,West)
            return (north or east or south or west)
        
        #jumps to some square in usable_squares or returns False if unsuccessful
        def jump():
            # index of square in usable_squares
            proposal_square = 0
            
            # decide how to jump
            should_birds = random.random()
            if should_birds < p_birds_eye:
                #find closest square to return_dist
                return_dist = math.sqrt(math.pow(coordinates[0] - start_coord[0],2) + math.pow(coordinates[1] - start_coord[1],2))
                while m.usable_squares[proposal_square][1] < return_dist:
                    proposal_square = proposal_square + 1
            else:
                #choose random square
                proposal_square = random.randint(0,len(m.usable_squares) - 1)
            
            # try to find proposal square that can branch off a new path
            success = False
            while success = False:
                if check_sq(m.usable_squares[proposal_square]):
                    success = True
                elif proposal_sq = len(m.usable_squares)-1:
                    if proposal_sq = 0:
                        # usable squares exhausted; set end of maze if not already set
                        if m.end = (False,False):
                            m.end = coordinates
                        break
                    # go back to start of usable_squares after reaching end
                    proposal_sq = 0
                else
                    # if proposal square fails, remove it and try next one
                    m.usable_squares.remove(m.usable_squares[proposal_square])
                    proposal_sq = propoal_sq + 1
            
            if success = True:
                coordinates = usable_squares[1]
            
            return success
        

        
    
    
    
