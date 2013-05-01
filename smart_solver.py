import random
import operator
from maze import *

class SmartSolver:

    def smart_solver(self,maze):

        compass = "N"
        counter = 0

        cur_r = maze.start[0]
        cur_c = maze.start[1]

    	def plan_path(maze,compass,counter,cur_r,cur_c):

            end_r = maze.end[0]
            end_c = maze.end[1]
	    board = maze.board
	    birds_north = ["N",False]
	    birds_south = ["S",False]
	    birds_west = ["W",False]
	    birds_east = ["E",False]
	    
	    def more_likely(cur_r,cur_c,end_r,end_c,birds_north,birds_south,birds_west,birds_east):
	        if cur_r < end_r:
		    birds_south[1] = True
		elif cur_r > end_r:
		    birds_north[1] = True
		else: 
		    return
		if cur_c < end_c:
		    birds_east[1] = True
		elif cur_c > end_c:
		    birds_west[1] = True
		else:
		    return

	    more_likely(cur_r,cur_c,end_r,end_c,birds_north,birds_south,birds_west,birds_east)

	    back = None

	    def back_is(compass,back):
  	        if compass == "N":
    		    back = "S"
  		elif compass == "S":
    		    back = "N"
  		elif compass == "W":
    		    back = "E"
  		elif compass == "E":
    		    back = "W"
		else:
		    print "Compass only has four directions!"

	    dir_order = [birds_north,birds_south,birds_west,birds_east]
	    
	    def assign_weight(dir_order,compass,back):
	        for x in dir_order:
		    if x[1] == True:
      		        x[1] = 2#random.uniform(0,1)
    		    else: 
      		        x[1] = 1#random.uniform(0,0.5)
  		dir_order.sort(key=operator.itemgetter(1))
		back_is(compass,back)
  		for x in dir_order:
    		    if x[0] == back:
     		        dir_order.append(x)
      		        dir_order.pop(dir_order.index(x))
    		    else:
      		        None

	    assign_weight(dir_order,compass,back)
	    plan = [dir_order[0][0],dir_order[1][0],dir_order[2][0],dir_order[3][0]]
            #plan = ["N","E","S","W"]
            print plan

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
		
	    def walkable(cur_r,cur_c,board,direction_headed):
	        new_x,new_y = get_next_square(cur_r,cur_c,direction_headed)
                print new_x,new_y
		if (new_x >= 0 and new_x < maze_num_cols and new_y >= 0 and new_y < maze_num_rows):
		    if(board[new_x][new_y] == True):
                        #print "On board"
		        return (True,(new_x,new_y))
		    else:
                        #print "Path blocked"
		        return (False,(new_x,new_y))
		else:
                    #print "Off board"
		    return (False,(new_x,new_y))

	    def move(counter,cur_r,cur_c,new_r,new_c,compass,direction_headed,maze,self):
	        cur_r = new_r
		cur_c = new_c
                print "Move called" 
                print direction_headed
		counter +=1
                maze.runtime += 1
		compass = direction_headed
                print compass
		if (cur_r,cur_c) == maze.end:
		    return
		else:
                    if counter < 10:
                        plan_path(maze,compass,counter,cur_r,cur_c)
                    else:
                        return

	    if walkable(cur_r,cur_c,board,plan[0])[0] == True:
	        new_r,new_c = walkable(cur_r,cur_c,board,plan[0])[1]
                print plan[0],new_r,new_c
		move(counter,cur_r,cur_c,new_r,new_c,compass,plan[0],maze,self)	
	
	    elif walkable(cur_r,cur_c,board,plan[1])[0] == True:
	        new_r,new_c = walkable(cur_r,cur_c,board,plan[1])[1]
                print plan[1],new_r,new_c
  	        move(counter,cur_r,cur_c,new_r,new_c,compass,plan[1],maze,self)

	    elif walkable(cur_r,cur_c,board,plan[2])[0] == True:
                new_r,new_c = walkable(cur_r,cur_c,board,plan[2])[1]
                print plan[2],new_r,new_c
  	        move(counter,cur_r,cur_c,new_r,new_c,compass,plan[2],maze,self)

	    elif walkable(cur_r,cur_c,board,plan[3])[0] == True:
	        new_r,new_c = walkable(cur_r,cur_c,board,plan[3])[1]
                print plan[3],new_r,new_c
  	        move(counter,cur_r,cur_c,new_r,new_c,compass,plan[3],maze,self) 

	    else:
  	        print "I'm trapped! D:"

	plan_path(maze,compass,counter,cur_r,cur_c)
        print maze.runtime

my_maze = m
smart_solver = SmartSolver()
smart_solver.smart_solver(my_maze)	

	    


