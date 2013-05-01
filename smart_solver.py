import random
import operator
from operator import itemgetter
from math import sqrt
#from maze import * #uncomment when ready to test using generate
from tm import *

class SmartSolver:
   
    def smart_solver(self,m):	# maze to m

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

            dir_dict = dict()
            dir_dict["N"] = None
            dir_dict["S"] = None
            dir_dict["W"] = None
            dir_dict["E"] = None

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
            RETURNS: a tuple of next square's position
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
            -m: 
            -new: 
            -usable: 
            '''
            def walk(m,new,usable):
                m.r = new[0]
                m.c = new[1]
                m.runtime += 1
                if in_usable((m.r,m.c),usable) == False:
                    dist = distance(m)
                    usable.append([new,dist,True])
                if (m.r,m.c) == m.end:
                    return # AND WE ARE DONE!
                else:
                    solve(m,usable)

            ''' jump
            Goes to a square in usable that's 1. not False; 2. closest to the end
            Assumes usable is non-empty at this point
            RETURNS: Nothing (unless an error occurs).
            -
            '''
            def jump(m,usable,i): 
                if usable[i][2] == True:
                    usable[i][2] = False
                    new = usable[i][0]
                    walk(m,new,usable)                
                else:
                    if i < len(usable) - 1:
                        jump(m,usable,i+1)
                    else:
                        print "No available square in usable."

            ''' move
            Tries to walk to an adjacent square; if that fails, goes to another square
            RETURNS: Nothing.
            -m
            -visit_order: list of directions to vist, in order
            -usable:
            -i: first passed in 0
            '''
            def move(m,visit_order,usable,i): #OR def move(m,visit_order[i][0],usable):
                if i < 4:
                    if walkable(m,visit_order[i][0],usable)[0] == True:
                        new = walkable(m,visit_order[i][0],usable)[1]
                        walk(m,new,usable)
                    else:
                        move(m,visit_order,usable,i+1)
                else:
                    usable.sort(key=operator.itemgetter(1))
                    jump(m,usable,0)

            assign_weight(m,dir_dict)
            visit_order = sorted(dir_dict.iteritems(), key=itemgetter(1), reverse=True)    
            move(m,visit_order,usable,0)

            # dir_dict = {'S':0.20, 'E':0.33, 'W': 0.19, 'N':0.05}
            # visit_order = [('E',0.33),('S',0.20),('W',0.19),('N',0.05)]

        solve(m,usable)
        print m.runtime

maze = m
smart_solver = SmartSolver()
smart_solver.smart_solver(maze)	


	    
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

