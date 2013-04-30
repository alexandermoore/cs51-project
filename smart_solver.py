import random
import operator
from operator import itemgetter
from math import sqrt
from maze import *

class SmartSolver:
   
    def smart_solver(self,m):	# maze to m

        # initialize current position to start
        #rc = [maze.start[0],maze.start[1]]
        rc = [0,0]
        m.runtime = 0
        usable = []
          
        def solve(m,rc,usable):

            end = [m.end[0],m.end[1]]    # when awake, think about whether end should stay here or go outside solve()
            board = m.board

            dir_dict = dict()
            dir_dict["N"] = None
            dir_dict["S"] = None
            dir_dict["W"] = None
            dir_dict["E"] = None
	    
            def weigh_diff(dir_dict,d_more,d_less):
                dir_dict[d_more] = random.uniform(0,1)
                dir_dict[d_less] = random.uniform(0,0.25)

            def weigh_same(dir_dict,d_one,d_two):
                dir_dict[d_one] = random.uniform(0,0.25)
                dir_dict[d_two] = random.uniform(0,0.25)

            """
            more_likely
            
            """
            def assign_weight(rc,end,dir_dict):
                if rc[0] < end[0]:
                    weigh_diff(dir_dict,"S","N")
                elif rc[0] > end[0]:
                    weigh_diff(dir_dict,"N","S")
                else: 
                    weigh_same(dir_dict,"N","S")
                if rc[1] < end[1]:
                    weigh_diff(dir_dict,"E","W")
                elif rc[1] > end[1]:
                    weigh_diff(dir_dict,"W","E")
                else:
                    weigh_same(dir_dict,"W","E")

            # expects direction_headed to be one of: "N", "S", "W", "E"
            def get_next_square(rc,direction_headed):
                if direction_headed == "N":
                    return rc[0]-1,rc[1]
                elif direction_headed == "S":
                    return rc[0]+1,rc[1]
                elif direction_headed == "W":
                    return rc[0],rc[1]-1
                else: # "E"
                    return rc[0],rc[1]+1

      	    def distance(rc,end):
                distance_from_end = sqrt((end[0]-rc[0])**2 + (end[1]-rc[1])**2)
                return distance_from_end

            # i should always be 0 when first passed in
            # usable should be sorted from smallest to greatest distance from end
            def in_usable(rc,usable,i):
                if i < len(usable):
                    if rc == usable[i][0]:
                        return True
                    else:
                        i += 1
                        in_usable(rc,usable,i)
                else:
                    return False
            
            def walkable(rc,board,direction_headed,usable):
                new = get_next_square(rc,direction_headed)
                print ["new",new]
                if (new[0] >= 0 and new[0] < maze_num_rows and new[1] >= 0 and new[1] < maze_num_cols):
                    if(board[new[0]][new[1]] == True and in_usable(new,usable,0) == False):
                        return (True,(new[0],new[1]))
                    else:
                        return (False,(None,None))
                else:
                    return (False,(None,None))
            
            def move(m,rc,new,usable):
                rc[0] = new[0]
                rc[1] = new[1]
                m.runtime += 1
                if rc == m.end:
                    return # AND WE ARE DONE!
                else:
                    solve(m,rc,usable)
            
            def jump(rc,usable,i): # Find the square in usable that's the closest to the end
                if usable[i][2] == True:
                    usable[i][2] = False
                    new = usable[i][0]
                    move(m,rc,new,usable) 
                else: # usable[i][2] == False:
                    i += 1
                    print i
                    if i < len(usable):
                        jump(rc,usable,i)
                    else:
                        print "No available square in usable."
            
            def step(m,rc,end,board,visit_order,usable,i):
                if i < 4:
                    if walkable(rc,board,visit_order[i][0],usable)[0] == True:
                        new = walkable(rc,board,visit_order[i][0],usable)[1]
                        dist = distance(new,end)
                        usable.append([new,dist,True])
                        move(m,rc,new,usable)
                    else:
                        step(m,rc,end,board,visit_order,usable,i+1)
                else:
                    usable.sort(key=operator.itemgetter(1))
                    jump(rc,usable,0)

            assign_weight(rc,end,dir_dict)    
            # dir_dict = {'S':0.20, 'E':0.33, 'W': 0.19, 'N':0.05}
            visit_order = sorted(dir_dict.iteritems(), key=itemgetter(1), reverse=True)
            # visit_order = [('E',0.33),('S',0.20),('W',0.19),('N',0.05)]
            step(m,rc,end,board,visit_order,usable,0)
            
        solve(m,rc,usable)

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
comman you want to execute
"""
# group function calls at the end

# Question: usable is a list that'll never be empty before its index is accessed (at least, that's how it's set up). 
# Should I still include an if branch that handles the empty case?
# comment for function : assumes the list is not empty (cleaner)
# or include the branch to check
