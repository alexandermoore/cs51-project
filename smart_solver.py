import random
import operator
from maze import *

class SmartSolver:
   
    def smart_solver(self,m):	# maze to m

	# initialize current position coordinates to start
	m.c = maze.start[0]
	m.r = maze.start[1]

	# plan_path to solve
    	def solve(m):

	    end_r = m.end[0] 
	    end_c = m.end[1]
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

	    def more_likely(cur_r,cur_c,end_r,end_c,dir_dict):
	        if cur_r < end_r:
                    weigh_diff(dir_dict,"S","N")
		elif cur_r > end_r:
                    weigh_diff(dir_dict,"N","S")
		else: 
                    weigh_same(dir_dict,"N","S")

		if cur_c < end_c:
                    weigh_diff(dir_dict,"E","W")
		elif cur_c > end_c:
                    weigh_diff(dir_dict,"W","E")
		else:
                    weigh_same(dir_dict,"W","E")

	    more_likely(m.r,m.c,end_r,end_c,dir_dict)    # dir_dict = {'S':0.20, 'E':0.33, 'W': 0.19, 'N':0.05}
            visit_order = sorted(dir_dict.iteritems(), key=itemgetter(1), reverse=True)
            # visit_order = [('E',0.33),('S',0.20),('W',0.19),('N',0.05)]

            def get_next_square(cur_r,cur_c,direction_headed):
	        if direction_headed == "N":
		    return cur_r-1,cur_c
		elif direction_headed == "S":
		    return cur_r+1,cur_c
		elif direction_headed == "W":
		    return cur_r,cur_c-1
		elif direction_headed == "E":
		    return cur_r,cur_c+1
		else:
		    print "I'm lost!"

      	    def distance(r,c,end_r,end_c):
	        distance_from_end = (end_c-c)/(end_r-r)
		return distance_from_end

	    def in_usable(r,c,usable,i):
	        if i < len(usable):
		    if (r,c) == usable[i][0]:
		        return True
		    else:
		        i += 1
			in_usable(r,c,usable,i)
		else:
		    return False

	    def walkable(cur_r,cur_c,board,direction_headed,usable):
	        new_r,new_c = get_next_square(cur_r,cur_c,direction_headed)
		if (new_r >= 0 and new_r < maze_num_cols and new_c >= 0 and new_c < maze_num_rows):
		    if(board[new_r][new_c] == True and in_usable(new_r,new_c,usable,0) == False):
		        return (True,(new_r,new_c))
		    else:
		        return False
		else:
		    return False

	    def move(new_r,new_c,m,self):
	        m.r = new_r
		m.c = new_c
		m.runtime += 1
		if (m.r,m.c) == m.end:
		    return
		else:
		    solve(m)

	    def jump(usable,i):
	    # Find the square in usable that's the closest to the end
	        if usable[i][2] == True:
		    usable[i][2] = False
	            new_r,new_c = usable[i][0]
	            move(new_r,new_c,m,self)
		elif usable[i][2] == False:
		    i += 1
		    if i < len(usable):
		        jump(usable,i)
		    else:
			print "Trapped"
		else:
		    return ...

  	   def step(board,visit_order,usable,end_r,end_c,i):
	       if i < 4:
	           if walkable(m.r,m.c,board,visit_order[i][0],usable) == True:
	               new_r,new_c = walkable(m.r,m.c,board,visit_order[i][0])[1]
		       dist = distance(m.r,m.c,end_r,end_c)
		       usable.append([(m.r,m.c),dist,True])
		       move(m.r,m.c,new_r,new_c,visit_order[i][0],m,self)
	           else:
		    step(board,visit_order,usable,end_r,end_c,i+1):
	        else:
	            usable.sort(key=operator.itemgetter(1))
	        jump(usable,0)

            step(board,visit_order,usable,end_r,end_c,0)

	solve(maze)

maze = maze.m
smart_solver = SmartSolver()
smart_solver.smart_solver(maze)	

# d = dict()
# d["N"] = None
# d["N"] = 5
	    
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
