from maze import *
from solver import *

class Generator:
	#CONSTANTS
    num_mazes = 10
    
    #FIELDS
    start_loc_x = 1
    start_loc_y = 1
    p_jump = 1
    p_forward = 1
    p_birds_eye = 1
    return_dist = 1
    end_time = 1
    mazes = []
    avg_runtime = False
    parameter_list = [start_loc_x,start_loc_y,p_jump,p_forward,p_birds_eye,return_dist,end_time,mazes,avg_runtime]
	
	#METHODS
	
	#Constructor takes in params, float list of [start_loc_x,start_loc_y,p_jump,p_forward,p_birds_eye,
	#return_dist,end_time]
    def __init__(self,params):
        start_loc_x = params[0]
        start_loc_y = params[1]
        p_jump = params[2]
        p_forward = params[3]
        p_birds_eye = params[4]
        return_dist = params[5]
        end_time = params[6]
        for val in range(num_mazes):
            m = Maze()
            generate(m)
            #simple_solver.solve(m)
            mazes.append(m)
        self.calc_average_runtime
	
    def calc_avg_runtime(self):
        total_time = 0
        for maze in mazes:
             total_time = total_time + maze.runtime
        return total_time/len(mazes)
    
    def generate(m):
        return False







	