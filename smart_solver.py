import random
import operator
import math
from operator import itemgetter
from math import sqrt
from maze import *

class SmartSolver:
    
    smart_solver_runtime = 0
    
    def smart_solver(self,m):	

        # initialize current position to start square
        m.r = m.start[0]
        m.c = m.start[1]
        self.smart_solver_runtime = 0

        ''' solve
        Goes through a maze from start to end
        RETURNS: runtime (int)
        -m: maze object
        '''
        def solve(m):

            def weigh_diff(dir_dict,d_more,d_less):
                dir_dict[d_more] = round(random.uniform(0,1),4)
                dir_dict[d_less] = round(random.uniform(0,0.25),4)

            def weigh_same(dir_dict,d_one,d_two):
                dir_dict[d_one] = round(random.uniform(0,0.25),4)
                dir_dict[d_two] = round(random.uniform(0,0.25),4)

            ''' assign_weight
            Assigns a higher value to the direction(s) that take the solver towards the end
            RETURNS: nothing
            -dir_dict: a dict with direction as 'key' and float as 'value.' 
            '''
            def assign_weight(m,dir_dict):
                if m.r < m.end[0]:
                    weigh_diff(dir_dict,"S","N")
                elif m.r > m.end[0]:
                    weigh_diff(dir_dict,"N","S")
                else: 
                    weigh_same(dir_dict,"N","S")
                if m.c < m.end[1]:
                    weigh_diff(dir_dict,"E","W")
                elif m.c > m.end[1]:
                    weigh_diff(dir_dict,"W","E")
                else:
                    weigh_same(dir_dict,"W","E")

            ''' get_next_square
            RETURNS: next square's position (tuple)
            '''
            def get_next_square(m,direction_headed):
                if direction_headed == "N":
                    return m.r-1,m.c
                elif direction_headed == "S":
                    return m.r+1,m.c 
                elif direction_headed == "W":
                    return m.r,m.c-1 
                else: # "E"
                    return m.r,m.c+1

            ''' distance
            Calculates the distance between the current square and the end square.
            RETURNS: distance between the two squares (float)
            -m: maze object -> m.r: current row; m.c: current column; m.end: tuple
            '''
      	    def distance(m):  
                distance_from_end = round(sqrt((m.end[0]-m.r)**2 + (m.end[1]-m.c)**2),4)
                return distance_from_end
            
            ''' in_usable
            Checks whether a square is in the usable list.
            RETURNS: boolean
            -rc: position of a square
            '''   
            def in_usable(m,rc):
                for sq in m.usable:
                    if rc == sq[0]:
                        return True
                return False
 
            ''' walkable
            Checks whether a new square is 1. on board; 2. unobstructed; 3. not in usable
            RETURNS: either a tuple of boolean and tuple or None (True,(new_r,new_c)) or (False,None)
            -direction_headed: a char indicating direction ('N', 'S', 'W', or 'E')             
            '''                        
            def walkable(m,direction_headed):
                new = get_next_square(m,direction_headed)
                if (new[0] >= 0 and new[0] < maze_num_rows and new[1] >= 0 and new[1] < maze_num_cols):
                    if(m.board[new[0]][new[1]] == True and in_usable(m,new) == False):
                        return (True,new)
                    else:
                        return (False,None)
                else:
                    return (False,None)

            ''' walk
            Updates current position and runtime
            RETURNS: nothing
            -new: position of new square; tuple
            '''
            def walk(m,new):
                m.r = new[0]
                m.c = new[1]
                self.smart_solver_runtime += 1
                if in_usable(m,(m.r,m.c)) == False:
                    dist = distance(m)
                    m.usable.append([new,dist,True])
                return
 
            ''' jump
            Goes to a square in usable that's 1. not False; 2. closest to the end
            Assumes usable is non-empty at this point
            RETURNS: nothing
            -m: maze object 
            '''
            def jump(m):
                for i in m.usable:
                    if i[2] == True:
                        new = i[0]
                        walk(m,new)
                        break
                return

            ''' move
            Tries to walk to an adjacent square; failing, goes to another square
            RETURNS: nothing
            -m: maze object
            '''
            def move(m): 
                dir_dict = dict()
                end_dist = round(sqrt((m.end[0]-m.r)**2 + (m.end[1]-m.c)**2),4)
                # initialize m.usable list to contain the start square
                m.usable = [[(m.r,m.c),end_dist,True]]

                while ((m.r,m.c) != (m.end)):
                    dir_dict["N"] = None
                    dir_dict["S"] = None
                    dir_dict["W"] = None
                    dir_dict["E"] = None
                    assign_weight(m,dir_dict)

                    # visit_order is a list of directions in dir_dict sorted by value
                    visit_order = sorted(dir_dict.iteritems(), key=itemgetter(1), reverse=True)
                    success = False
                    for i in range(0,4):
                        if walkable(m,visit_order[i][0])[0] == True:
                            new = walkable(m,visit_order[i][0])[1]
                            success = True
                            walk(m,new)
                            break                                          
                    if success == False:
                        d = distance(m)
                        m.usable.sort(key = lambda x: x[1])
                        ind = m.usable.index([(m.r,m.c),d,True])
                        m.usable[ind][2] = False              
                        m.usable.sort(key=operator.itemgetter(1))
                        jump(m)
                return

            move(m)

        solve(m)
        m.runtime = math.sqrt(self.smart_solver_runtime)

smart_solver = SmartSolver()



