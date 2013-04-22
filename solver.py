import random
import maze

# Our solver doesn't work yet. :'( 

# Here's the latest code in progress:
from maze import *

solve(maze)

	# initially set to maze's start values
	cur_x = maze.start[0]
	cur_y = maze.start[1]

	# initialize compass variable to an arbitrary value
	compass = "N"	

	# initialize a counter
	sq_traversed = 0	

	#  get board
	board = maze.board

	# walkable
	def walkable(new_x,new_y,board):
		if (new_x >= 0 & new_x < maze_x_dim & new_y >= 0 & new_y < maze_y_dim):
			if(board[new_x][new_y] == True):
				True
			else:
				False
		else:
			False		

	# returns a runtime
	def walk(cur_x,cur_y,compass,board):
		if compass == "N":
			# try to go left
			if walkable(cur_x,cur_y-1,board) == True:
				cur_y = cur_y-1
				sq_traversed += 1
				compass = "W"

				# is this the end?
				if (cur_x,cur_y) == board.end:
					print sq_traversed
					sq_traversed	
				else:
					walk(cur_x,cur_y,compass,board)
			else:
				# try to go forward
				if walkable(cur_x-1,cur_y,board) == True:
					cur_x = cur_x-1
					sq_traversed += 1
					if (cur_x,cur_y) == board.end:
						print sq_traversed
						sq_traversed
					else:
						walk(cur_x,cur_y,compass,board)
				else:
					# try to go right
					if walkable(cur_x,cur_y+1,compass,board) == True:
						cur_y = cur_y+1
						sq_traversed += 1
						if (cur_x,cur_y) == board.end:
							print sq_traversed
							sq_traversed
						else:
							walk(cur_x,cur_y,compass,board)
					else:
						# move backward
						if walkable(cur_x+1,cur_y,compass,board) == True:
							cur_x = cur_x + 1
							print sq_traversed
							sq_traversed
							if (cur_x,cur_y) == board.end:
								print sq_traversed
								sq_traversed
							else:
								walk(cur_x,cur_y,compass,board)
						else:
							print "there's a problem"
							sq_traversed
					
					
	=====

	walk(cur_x,cur_y,compass)

# Old code kept just for reference
class Solver: 
    # Solves a maze using a given genetic algorithm and sets the runtime 
    # of the Maze to the number of squares the solver traversed
    # DFS: attempt to move left, then forward, then right; if all fail, move back. 
    # After taking a step, check if this square is the "end" square. 
    # If so, set the runtime to sq_traversed. 
    # def solve (my_maze: Maze) : unit =
    # my_maze = maze.Maze()

    # A counter keeping track of total number of squares traversed. 
    sq_traversed = 0

    # Compass initialized to an arbitrary direction. 
    compass = "N"

    # Moved
    moved = False

    # Visited
    visited_l = False
    visited_f = False
    visited_r = False
    visited_b = False

    # Next 
    # next_x = 0
    # next_y = 0

    # Direction...
    left_dir = {"N":(0,-1),"S":(0,1),"W":(1,0),"E":(-1,0)}
    forw_dir = {"N":(-1,0),"S":(1,0),"W":(0,-1),"E":(0,1)}
    right_dir = {"N":(0,1),"S":(0,-1),"W":(-1,0),"E":(1,0)}
    back_dir = {"N":(1,0),"S":(-1,0),"W":(0,1),"E":(0,-1)}

    # Checks to see if a move is possible
    def walkable(self,x,y): 
        # If the square is on the board, check whether the square is 
        # free of obstructions. 
        if (x >= 0 & x < m & y >= 0 & y < n):
            if (my_maze.board[x][y] == False):
                 True 
            else: 
                 False
        else: 
            False

    # Updates current position
    def try_move(self,d):
        if d == "L":
            cur_dir = self.left_dir[self.compass]
            next_x = (cur_dir[0] + self.cur_x)
            next_y = (cur_dir[1] + self.cur_y)

            # If you can walk in this direction, do it!
            # Then update sq_traversed, moved, and compass
            # If you can't walk in this direction, update visited_l.
            if self.walkable(next_x,next_y) == True:
                self.cur_x = next_x
                self.cur_y = next_y
                self.sq_traversed += 1
                self.moved = True
                if cur_dir == "N":
                   self.compass = "W"
                elif cur_dir == "S":
                   self.compass = "E"
                elif cur_dir == "W":
                   self.compass = "S"
                else:
                   self.compass = "N"
            else:
                self.visited_l = True
        elif d == "F": 
            cur_dir = self.forw_dir[compass]
            next_x = cur_dir[0] + cur_x
            next_y = cur_dir[1] + cur_y
            if self.walkable(next_x,next_y) == True:
                cur_x = next_x
                cur_y = next_y
                sq_traversed += 1
                moved = True
            else:
                visited_f = True
        elif d == "R":
            cur_dir = right_dir[compass]
            next_x = cur_dir[0] + cur_x
            next_y = cur_dir[1] + cur_y
            if self.walkable(next_x,next_y) == True:
                cur_x = next_x
                cur_y = next_y
                sq_traversed += 1
                moved = True
                if cur_dir == "N":
                    compass = "E"
                elif cur_dir == "S":
                    compass = "W"
                elif cur_dir == "W":
                    compass = "N"
                else:
                    compass = "S"
            else:
                visited_r = True
        else:
            cur_dir = back_dir[compass]
            next_x = cur_dir[0] + cur_x
            next_y = cur_dir[1] + cur_y
            if self.walkable(next_x,next_y) == True:
                cur_x = next_x
                cur_y = next_y
                sq_traversed += 1
                moved = True
                if cur_dir == "N":
                    compass = "S"
                elif cur_dir == "S":
                    compass = "N"
                elif cur_dir == "W":
                    compass = "E"
                else:
                    compass = "W"
                    
    # A random number x, is generated.
    # If x is between move_left_prob_lower and 
    # move_left_prob_right, solver checks left
    # These values must be between 0 and 1!
    # If you want the maze solver to check left first
    # with probability = 0.5, l_prob_lower = 0 and l_prob_upper = 0.5
    #  |----------|------|----|
    #  0    L    0.5  F 0.8 R 1
    # l_prob_lower = 0
    # l_prob_upper = 0.5
    # f_prob_lower = 0.5
    # f_prob_upper = 0.8
    # r_prob_lower = 0.8
    # r_prob_upper = 1

    
       # dart = uniform(0,1)
       # if (dart > l_prob_lower && l_prob_upper <= 0.5 && visited_l = false):
       #     try_move("L")
       # elif (dart > f_prob_lower && dart <= f_prob_upper && visited_f = false):
       #     try_move("F")
       # elif (dart < r_prob_lower && dart <= r_prob_upper && visited_r = false):
       #     try_move("R")
    def move(self,my_maze):
        # Dimensions of n by m my_maze
        n = len(my_maze.board)
        m = len(my_maze.board[0])

        # xy-coordinate of current position
        position = my_maze.start
        self.cur_x = position[0]
        self.cur_y = position[1]

        if self.visited_l == False:
            self.try_move("L")   
            if moved == True: 
                print "move l"
                if (cur_x,cur_y) == my_maze.end:
                    my_maze.runtime = sq_traversed
                    print sq_traversed
                else:
                    moved = False
                    self.move()
            else:
                visited_l = True
                self.move()
        elif (self.visited_l == True & self.visited_f == False):
            self.try_move("F")
            if moved == True:
                print "move f"
                if (cur_x,cur_y) == my_maze.end:
                    my_maze.runtime = sq_traversed
                    print sq_traversed
                else:
                    moved = False
                    self.move()
            else:
                visited_f = True
                self.move()
        elif (visited_l == True & visited_f == True & visited_r == False):
            self.try_move("R")
            if moved == True:
                print "move r"
                if (cur_x,cur_y) == my_maze.end:
                    my_maze.runtime = sq_traversed
                    print sq_traversed
                else:
                    moved = False
                    self.move()
            else:
                visited_r = True
                self.move()
        else:
             self.try_move("B")
             if self.moved == True:
                 print "move b"
                 if (cur_x,cur_y) == my_maze.end:
                     my_maze.runtime = sq_traversed
                     print self.sq_traversed
                     print my_maze.runtime
                 else:
                     self.moved = False
                     self.move()
             else:
                 self.visited_b = True
                 self.move()

my_m = maze.m
solver_object = Solver()
solver_object.move(my_m)

# Change every move() to solve()
