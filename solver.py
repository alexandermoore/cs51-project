import random
import maze

# first implement sth that takes in a bunch of parameters
# and then move onto dictionaries -> get help from Randy

# trying to merge
# Here's the latest code in progress:
from maze import *

class Solver:

    def solve(self,maze):

        cur_x = maze.start[0]
        cur_y = maze.start[1]
        compass = "N"		
        board = maze.board
	runtime = maze.runtime

        """ walkable
        Returns True or False.
        -new_x : row the square of interest is in
        -new_y : column the square of interest is in
        """
        def walkable(new_x,new_y,board):
            if (new_x >= 0 and new_x < maze_num_cols and new_y >= 0 and new_y < maze_num_rows):
                if(board[new_x][new_y] == True):
                    return True
       	        else:
                    return False
	    else:    
                return False		

        """
        Returns a runtime (an int)
        -cur_x (int) : 
        -cur_y (int) :
        -compass (char) : 
        -maze (maze object) :
        """
        def walk(cur_x,cur_y,compass,maze):
            if compass == "N":
                # try to go left
                if walkable(cur_x,cur_y-1,board) == True:
                    cur_y = cur_y-1
		    maze.runtime += 1
		    compass = "W"		   
		    if (cur_x,cur_y) == maze.end:
		        return	
	            else:
                        walk(cur_x,cur_y,compass,maze)

                # try to go forward	    	    
	        else:
                    if walkable(cur_x-1,cur_y,board) == True:
                        cur_x = cur_x-1
		        maze.runtime += 1
                        print maze.runtime
		        if (cur_x,cur_y) == maze.end:
			    return
		        else:
                            walk(cur_x,cur_y,compass,maze)

	            # try to go right
	       	    else:
                        if walkable(cur_x,cur_y+1,board) == True:
                            cur_y = cur_y+1
			    maze.runtime += 1
			    print maze.runtime
			    compass = "E"
			    if (cur_x,cur_y) == maze.end:
			        return
			    else:
                                walk(cur_x,cur_y,compass,maze)

    		        # move backward
		        else:
                            if walkable(cur_x+1,cur_y,board) == True:
                                cur_x = cur_x + 1
			        maze.runtime += 1
                                print maze.runtime 
			        compass = "S"
			        if (cur_x,cur_y) == maze.end:
                                    print maze.runtime
				    return
			        else:
                                    walk(cur_x,cur_y,compass,maze)
			    else:
			        return

            elif compass == "S":
                # try to go left
                if walkable(cur_x,cur_y+1,board) == True:
                    cur_y = cur_y + 1
		    maze.runtime += 1
                    print maze.runtime
		    compass = "E"
		    if (cur_x,cur_y) == maze.end:
	                return
		    else:
                        walk(cur_x,cur_y,compass,maze)

                # try to move forward 
                else:
                    if walkable(cur_x+1,cur_y,board) == True:
                        cur_x = cur_x + 1 
                        maze.runtime += 1
			print maze.runtime
                        if(cur_x,cur_y) == maze.end:
                            return
                        else:
                            walk(cur_x,cur_y,compass,maze)

                    # try to go right
                    else: 
                        if walkable(cur_x,cur_y-1,board) == True:
                            cur_y = cur_y - 1
                            maze.runtime += 1
			    print maze.runtime
                            compass = "W"
                            if (cur_x,cur_y) == maze.end:
                                return
                            else:
                                walk(cur_x,cur_y,compass,maze)

                        # move backward
                        else:
                            if walkable(cur_x-1,cur_y,board) == True:
                                cur_x = cur_x - 1
                                maze.runtime += 1
				print maze.runtime
                                compass = "N"
                                if (cur_x,cur_y) == maze.end:
                                    return
                                else:
                                    walk(cur_x,cur_y,compass,maze)
                            else:
                                return         

            elif compass == "W":
                # try to go left
                if walkable(cur_x+1,cur_y,board) == True:
                    cur_x = cur_x + 1
	            maze.runtime += 1
	            compass = "S"
		    if (cur_x,cur_y) == maze.end:
	                return
	            else:
	                walk(cur_x,cur_y,compass,maze)

                # try to move forward 
                else:
                    if walkable(cur_x,cur_y-1,board) == True:
                        cur_y = cur_y - 1 
                        maze.runtime += 1
			print maze.runtime
                        if(cur_x,cur_y) == maze.end:
                            return
                        else:
                            walk(cur_x,cur_y,compass,maze)

                    # try to go right
                    else: 
                        if walkable(cur_x-1,cur_y,board) == True:
                            cur_x = cur_x - 1
                            maze.runtime += 1
			    print maze.runtime
                            compass = "N"
                            if (cur_x,cur_y) == maze.end:
                                return
                            else:
                                walk(cur_x,cur_y,compass,maze)

                        # move backward
                        else:
                            if walkable(cur_x,cur_y+1,board) == True:
                                cur_y = cur_y + 1
                                maze.runtime += 1
                                compass = "E"
                                if (cur_x,cur_y) == maze.end:
                                    return
                                else:
                                    walk(cur_x,cur_y,compass,maze)
                            else:
                                return             

            else: # compass = "E"
                # try to go left
                if walkable(cur_x-1,cur_y,board) == True:
                    cur_x = cur_x - 1
	            maze.runtime += 1
	            compass = "N"
	            if (cur_x,cur_y) == maze.end:
	                return
	            else:
	                walk(cur_x,cur_y,compass,maze)

                # try to move forward 
                else:
                    if walkable(cur_x,cur_y+1,board) == True:
                        cur_y = cur_y + 1 
                        maze.runtime += 1
                        if(cur_x,cur_y) == maze.end:
                            return
                        else:
                            walk(cur_x,cur_y,compass,maze)

                    # try to go right
                    else: 
                        if walkable(cur_x+1,cur_y,board) == True:
                            cur_x = cur_x + 1
                            maze.runtime += 1
                            compass = "S"
                            if (cur_x,cur_y) == maze.end:
                                return
                            else:
                                walk(cur_x,cur_y,compass,maze)

                        # move backward
                        else:
                            if walkable(cur_x,cur_y-1,board) == True:
                                cur_y = cur_y - 1
                                maze.runtime += 1
                                compass = "W"
                                if (cur_x,cur_y) == maze.end:
                                    return
                                else:
                                    walk(cur_x,cur_y,compass,maze)
                            else:
                                return

        walk(cur_x,cur_y,compass,maze)
	print maze.runtime
           
maze = maze.m
simple_solver = Solver()
simple_solver.solve(maze)
