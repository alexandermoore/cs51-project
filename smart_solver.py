import random
import operator
from operator import itemgetter
from math import sqrt
from maze import * #uncomment when ready to test using generate
#from tm import *

class SmartSolver:
   
    def smart_solver(self,m):	

        # initialize current position to start
        m.r = m.start[0]
        m.c = m.start[1]
        m.runtime = 0
        start_end_dist = round(sqrt((m.end[0]-m.r)**2 + (m.end[1]-m.c)**2),4)
        usable = [[(m.r,m.c),start_end_dist,True]]

        ''' solve
        Goes through a maze
        RETURNS: runtime
        -m: maze object
        -usable: a list that keeps track of squares visited
        '''
        def solve(m,usable):

            def weigh_diff(dir_dict,d_more,d_less):
                dir_dict[d_more] = round(random.uniform(0,1),4)
                dir_dict[d_less] = round(random.uniform(0,0.25),4)

            def weigh_same(dir_dict,d_one,d_two):
                dir_dict[d_one] = round(random.uniform(0,0.25),4)
                dir_dict[d_two] = round(random.uniform(0,0.25),4)

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
            RETURNS: next square's position; a tuple
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
            Calculates the distance between a square and the end square.
            RETURNS: distance between the two squares
            -m: maze object; (m.r: current row; m.c: current column; m.end: tuple)
            '''
      	    def distance(m):  
                distance_from_end = round(sqrt((m.end[0]-m.r)**2 + (m.end[1]-m.c)**2),4)
                return distance_from_end
            
            ''' in_usable
            Checks whether a square is in the usable list.
            RETURNS: boolean
            -rc: position of a square
            -usable: sorted from least to greatest distance from end
            '''   
            def in_usable(rc,usable):
                for sq in usable:
                    if rc == sq[0]:
                        return True
                        break
                return False
 
            ''' walkable
            Checks whether a new square is 1. on board; 2. unobstructed; 3. not in usable
            RETURNS: either (True,(new_r,new_c)) or (False,None)
            -m: 
            -direction_headed:
            -usable:             
            '''                        
            def walkable(m,direction_headed,usable):
                new = get_next_square(m,direction_headed)
                if (new[0] >= 0 and new[0] < maze_num_rows and new[1] >= 0 and new[1] < maze_num_cols):
                    if(m.board[new[0]][new[1]] == True and in_usable(new,usable) == False):
                        return (True,new)
                    else:
                        return (False,None)
                else:
                    return (False,None)

            ''' walk
            Updates current position and runtime
            RETURNS: Nothing.
            -m: maze object
            -new: position of new square; tuple
            -usable: 
            '''
            def walk(m,new,usable):
                m.r = new[0]
                m.c = new[1]
                m.runtime += 1
                if in_usable((m.r,m.c),usable) == False:
                    dist = distance(m)
                    usable.append([new,dist,True])
                return

            ''' jump
            Goes to a square in usable that's 1. not False; 2. closest to the end
            Assumes usable is non-empty at this point
            RETURNS: Nothing.
            -m: maze object
            -usable: 
            '''
            def jump(m,usable):
                for i in usable:
                    if i[2] == True:
#                        print [i[0],usable]
                        new = i[0]
                        walk(m,new,usable)
#                        print ["new:",new,usable]
                        break
                return

            ''' move
            Tries to walk to an adjacent square; failing, goes to another square
            RETURNS: Nothing.
            -m
            -usable:
            '''
            def move(m,usable): 
                dir_dict = dict()

                while ((m.r,m.c) != (m.end)):
                    dir_dict["N"] = None
                    dir_dict["S"] = None
                    dir_dict["W"] = None
                    dir_dict["E"] = None
                    assign_weight(m,dir_dict)
                    visit_order = sorted(dir_dict.iteritems(), key=itemgetter(1), reverse=True)
                    success = False
                    for i in range(0,4):
                        if walkable(m,visit_order[i][0],usable)[0] == True:
                            new = walkable(m,visit_order[i][0],usable)[1]
                            success = True
                            walk(m,new,usable)
                            break                                          
                    if success == False:
                        d = distance(m)
                        ind = usable.index([(m.r,m.c),d,True])
                        usable[ind][2] = False              
                        usable.sort(key=operator.itemgetter(1))
                        jump(m,usable)
                return

            move(m,usable)

        solve(m,usable)
        print m.runtime

#maze = m
smart_solver = SmartSolver()
#smart_solver.smart_solver(maze)	


	    
"""
shell files: batch files
a sheebang
#!/bin/sh
python generate.py
python display.py
...
commands you want to execute
"""
# group function calls at the end
# Question: usable is a list that'll never be empty before its index is accessed (at least, that's how it's set up). 
# Should I still include an if branch that handles the empty case?
# comment for function : assumes the list is not empty (cleaner)
# or include the branch to check

# dir_dict = {'S':0.20, 'E':0.33, 'W': 0.19, 'N':0.05}
# visit_order = [('E',0.33),('S',0.20),('W',0.19),('N',0.05)]
