import random, sys, math
from maze import *



class generator:
# Function definition is here
    def generate(self,m):

        # variables that I get from elsewhere
        maze_x_dim = 20
        maze_y_dim = 20
        start_loc_x = 0.23
        start_loc_y = 0.87
        p_birds_eye = 0.76
        # if jumping randomly, then list of usable squares. if p_birds eye succeeds, do birds_eye implementation
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
        South = 1
        West  = 2
        East  = 3
        
        def check_square(dir,square):
        
        def jump():
            if m.usable_squares = []:  ##### this may be redundant
                m.end = coordinates
            jumped_to = random.choice(m.usable_squares)
            
            should_birds = random.random()
            if should_birds < p_birds_eye:
                return_dist = math.sqrt(math.pow(coordinates[0] - start_coord[0],2) + math.pow(coordinates[1] - start_coord[1],2))
                proposal_square = 0
                while m.usable_squares[proposal_square][1] < return_dist:
                    proposal_square = proposal_square + 1
                jumped_to = m.usable_squares[proposal_square]
            
            success = False
            while success = False
                
        
        

        
    
    
    
