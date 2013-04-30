import random
import operator
from maze import *

class SmartSolver:
   
    def smart_solver(self,m):	# maze to m

	# initialize current position coordinates to start
	m.c = maze.start[0]
	m.r = maze.start[1]

	# plan_path to solve
    	def solve(m,compass):

	    end_r = m.end[0] 
	    end_c = m.end[1]
	    board = m.board
            dir_dict = dict()
            dir_dict["N"] = None
            dir_dict["S"] = None
            dir_dict["W"] = None
            dir_dict["E"] = None
	    
	    def more_likely(cur_r,cur_c,end_r,end_c,dir_dict):
	        if cur_r < end_r:
                    dir_dict["S"] = True
		elif cur_r > end_r:
                    dir_dict["N"] = True
		else: 
		    return
		if cur_c < end_c:
                    dir_dict["E"] = True
		elif cur_c > end_c:
		    dir_dict["W"] = True
		else:
		    return

	    more_likely(m.r,m.c,end_r,end_c,dir_dict)

            # At this point, the solver has a dir_dict that looks something like
            # {'S': True, 'E': None, 'N':True, "W': None}

            # The problem is I can't use a for loop to update the dictionary directly.
            # In my previous implementation, I had a list of lists, where the second value
            # was True or None. I then changed True/None to random.uniform(conditional range).
            # So I'm trying to figure out how to go around this problem. 

	    # dlist = some list equivalent of dir_dict

	    def assign_weight(dlist):
	        for d in dlist:
		    if d[1] == True:
      		        d[1] = random.uniform(0,1)
    		    else: 
      		        d[1] = random.uniform(0,0.25)
  		dlist.sort(key=operator.itemgetter(1))

	    assign_weight(dlist)
	    visit_order = [dlist[0][0],dlist[1][0],dlist[2][0],dlist[3][0]]

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
		    return

# Question: usable is a list that'll never be empty before its index is accessed (at least, that's how it's set up). 
# Should I still include an if branch that handles the empty case?
# comment for function : assumes the list is not empty (cleaner)
# or include the branch to check

  	   def step(board,visit_order,usable,end_r,end_c,i):
	       if i < 4:
	           if walkable(m.r,m.c,board,visit_order[i],usable) == True:
	               new_r,new_c = walkable(m.r,m.c,board,visit_order[i])[1]
		       dist = distance(m.r,m.c,end_r,end_c)
		       usable.append([(m.r,m.c),dist,True])
		       move(m.r,m.c,new_r,new_c,visit_order[i],m,self)
	           else:
		    step(board,visit_order,usable,end_r,end_c,i+1):
	        else:
	            usable.sort(key=operator.itemgetter(1))
	        jump(usable,0)

            step(board,visit_order,usable,end_r,end_c,0)

	solve(maze,compass)

maze = maze.m
smart_solver_object = SmartSolver()
smart_solver_object.smart_solver(maze)	

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
