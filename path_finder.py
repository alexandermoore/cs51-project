import math
from maze import *
from settings import *
from display import *

class PathFinder:
    def path_finder_solve(self,m):
        maze = []
        for row in m.board:
            maze.append(list(row))
        
        # enumeration
        North = 0
        East = 1
        South  = 2
        West = 3
        
        def move(square,dir):
            if (dir == North):
                return(square[0]+1,square[1])
            elif dir == South:
                return(square[0]-1,square[1])
            elif dir == East:
                return(square[0],square[1]+1)
            elif dir == West:
                return(square[0],square[1]-1)
            else:
                print "error: moved not passed a valid direction"
            return
        
        def check_square(row,column):
            if maze[row][column] == False:
                return False
            if (row,column) == m.start or (row,column) == m.end:
                return False
            true_neighbors = 0
            for dir in [North,East,South,West]:
                neighbor = move((row,column),dir)
                if maze[neighbor[0]][neighbor[1]]:
                    true_neighbors = true_neighbors + 1
            if true_neighbors == 1:
                return True
            elif true_neighbors == 0:
                print "error, square is isolated"
            else:
                return False
        
        def display():
            maze_for_display = Maze()
            maze_for_display.board = maze
            maze_for_display.start = m.start
            maze_for_display.end = m.end
            #display_object.display(maze_for_display)
            return
        
        def evaluate_path():
            runtime = 0
            coordinates = m.start
            while(coordinates != m.end):
                for dir in [North,East,South,West]:
                    neighbor = move(coordinates,dir)
                    if maze[neighbor[0]][neighbor[1]]:
                        current_dist = math.sqrt((coordinates[0] - m.start[0])**2 + (coordinates[1] - m.start[1])**2)
                        neighbor_dist = math.sqrt((neighbor[0] - m.start[0])**2 + (neighbor[1] - m.start[1])**2)
                        runtime += (neighbor_dist - current_dist + 1) * neighbor_dist
                        maze[coordinates[0]][coordinates[1]] = False
                        coordinates = neighbor
            m.runtime += runtime
            
        
        while(True):
            deletions = 0
            for row in range(0,maze_num_rows):
                for column in range(0,maze_num_cols):
                    if check_square(row,column):
                        maze[row][column] = False
                        deletions = deletions + 1
            if deletions == 0:
                break
        if display_maze_solution:
            display()
        evaluate_path()
                    

pf = PathFinder()


                    