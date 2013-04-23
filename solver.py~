import random
import maze

# Here's the latest code in progress:
from maze import *

class Solver:

    def solve(self,maze):

        # initially set to maze's start values
        cur_x = maze.start[0]
        cur_y = maze.start[1]

        # initialize compass variable to an arbitrary value
        compass = "N"		

        # get board
        board = maze.board

	# get runtime
	runtime = maze.runtime
	
	# print initial runtime
	#print runtime

        # walkable
        def walkable(new_x,new_y,board):
            if (new_x >= 0 and new_x < maze_num_cols and new_y >= 0 and new_y < maze_num_rows):
                if(board[new_x][new_y] == True):
                    return True
       	        else:
                    return False
	    else:    
                return False		

        # returns a runtime
        def walk(cur_x,cur_y,compass,maze):
            #print maze.end
            if compass == "N":
                # try to go left
                if walkable(cur_x,cur_y-1,board) == True:
                    cur_y = cur_y-1
		    maze.runtime += 1
#
                    print maze.runtime
		    compass = "W"		   
		    if (cur_x,cur_y) == maze.end:
                        #maze.runtime
		        return maze.runtime	
	            else:
                        #print "N left not walkable"
                        walk(cur_x,cur_y,compass,maze)

                # try to go forward	    	    
	        else:
                    if walkable(cur_x-1,cur_y,board) == True:
                        cur_x = cur_x-1
		        maze.runtime += 1
#
                        print maze.runtime
		        if (cur_x,cur_y) == maze.end:
                            #print maze.runtime
			    maze.runtime
		        else:
                            #print "N forward not walkble"
                            walk(cur_x,cur_y,compass,maze)

	            # try to go right
	       	    else:
                        #print cur_x,cur_y
			#print ["result",walkable(cur_x,cur_y+1,board)]
                        if walkable(cur_x,cur_y+1,board) == True:
                            #print "here" 
                            cur_y = cur_y+1
			    #print cur_y
			    maze.runtime += 1
#
			    print maze.runtime
			    compass = "E"
			    if (cur_x,cur_y) == maze.end:
                                #print maze.runtime
			        maze.runtime
			    else:
                                #print "N right not walkable"
                                walk(cur_x,cur_y,compass,maze)

    		        # move backward
		        else:
                            if walkable(cur_x+1,cur_y,board) == True:
                                cur_x = cur_x + 1
			        maze.runtime += 1
#
                                print maze.runtime 
			        compass = "S"
			        if (cur_x,cur_y) == maze.end:
                                    print maze.runtime
				    maze.runtime
			        else:
                                    walk(cur_x,cur_y,compass,maze)
			    else:
                                #print "there's a problem : N"
			        maze.runtime

            elif compass == "S":
                # try to go left
                if walkable(cur_x,cur_y+1,board) == True:
                    cur_y = cur_y + 1
		    maze.runtime += 1
#
                    print maze.runtime
		    compass = "E"
		    if (cur_x,cur_y) == maze.end:
                        #print maze.runtime
	                maze.runtime
		    else:
                        walk(cur_x,cur_y,compass,maze)

                # try to move forward 
                else:
                    if walkable(cur_x+1,cur_y,board) == True:
                        cur_x = cur_x + 1 
                        maze.runtime += 1
#
			print maze.runtime
                        if(cur_x,cur_y) == maze.end:
                            #print maze.runtime
                            maze.runtime
                        else:
                            walk(cur_x,cur_y,compass,maze)

                    # try to go right
                    else: 
                        if walkable(cur_x,cur_y-1,board) == True:
                            cur_y = cur_y - 1
                            maze.runtime += 1
#
			    print maze.runtime
                            compass = "W"
                            if (cur_x,cur_y) == maze.end:
                                #print maze.runtime
                                maze.runtime
                            else:
                                walk(cur_x,cur_y,compass,maze)

                        # move backward
                        else:
                            if walkable(cur_x-1,cur_y,board) == True:
                                cur_x = cur_x - 1
                                maze.runtime += 1
#
				print maze.runtime
                                compass = "N"
                                if (cur_x,cur_y) == maze.end:
                                    #print maze.runtime
                                    maze.runtime
                                else:
                                    walk(cur_x,cur_y,compass,maze)
                            else:
                                #print "there's a problem : S"
                                maze.runtime             

            elif compass == "W":
                # try to go left
                if walkable(cur_x+1,cur_y,board) == True:
                    cur_x = cur_x + 1
	            maze.runtime += 1
	            compass = "S"
		    if (cur_x,cur_y) == maze.end:
	                #print maze.runtime
	                maze.runtime
	            else:
	                walk(cur_x,cur_y,compass,maze)

                # try to move forward 
                else:
                    if walkable(cur_x,cur_y-1,board) == True:
                        cur_y = cur_y - 1 
                        maze.runtime += 1
#
			print maze.runtime
                        if(cur_x,cur_y) == maze.end:
                            #print maze.runtime
                            maze.runtime
                        else:
                            walk(cur_x,cur_y,compass,maze)

                    # try to go right
                    else: 
                        if walkable(cur_x-1,cur_y,board) == True:
                            cur_x = cur_x - 1
                            maze.runtime += 1
#
			    print maze.runtime
                            compass = "N"
                            if (cur_x,cur_y) == maze.end:
                                #print maze.runtime
                                maze.runtime
                            else:
                                walk(cur_x,cur_y,compass,maze)

                        # move backward
                        else:
                            if walkable(cur_x,cur_y+1,board) == True:
                                cur_y = cur_y + 1
                                maze.runtime += 1
#
				print maze.runtime
                                compass = "E"
                                if (cur_x,cur_y) == maze.end:
                                    #print maze.runtime
                                    maze.runtime
                                else:
                                    walk(cur_x,cur_y,compass,maze)
                            else:
                                #print "there's a problem : W"
                                maze.runtime             

            else: # compass = "E"
                # try to go left
                if walkable(cur_x-1,cur_y,board) == True:
                    cur_x = cur_x - 1
	            maze.runtime += 1
#
		    print maze.runtime
	            compass = "N"
	            if (cur_x,cur_y) == maze.end:
	                #print maze.runtime
	                maze.runtime
	            else:
	                walk(cur_x,cur_y,compass,maze)

                # try to move forward 
                else:
                    if walkable(cur_x,cur_y+1,board) == True:
                        cur_y = cur_y + 1 
                        maze.runtime += 1
#
			print maze.runtime
                        if(cur_x,cur_y) == maze.end:
                            #print maze.runtime
                            maze.runtime
                        else:
                            walk(cur_x,cur_y,compass,maze)

                    # try to go right
                    else: 
                        if walkable(cur_x+1,cur_y,board) == True:
                            cur_x = cur_x + 1
                            maze.runtime += 1
#
			    print maze.runtime
                            compass = "S"
                            if (cur_x,cur_y) == maze.end:
                                #print maze.runtime
                                maze.runtime
                            else:
                                walk(cur_x,cur_y,compass,maze)

                        # move backward
                        else:
                            if walkable(cur_x,cur_y-1,board) == True:
                                cur_y = cur_y - 1
                                maze.runtime += 1
#
				print maze.runtime
                                compass = "W"
                                if (cur_x,cur_y) == maze.end:
                                    #print maze.runtime
                                    maze.runtime
                                else:
                                    walk(cur_x,cur_y,compass,maze)
                            else:
                                #print "there's a problem : E"
                                maze.runtime

        walk(cur_x,cur_y,compass,maze)
	print maze.runtime
           
maze = maze.m
simple_solver = Solver()
simple_solver.solve(maze)
