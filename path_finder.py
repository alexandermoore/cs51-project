from maze import *
from settings import *
from display import *

class PathFinder:
    def find_path(self,m):
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
        
        while(True):
            deletions = 0
            for row in range(0,maze_num_rows):
                for column in range(0,maze_num_cols):
                    if check_square(row,column):
                        maze[row][column] = False
                        deletions = deletions + 1
            if deletions == 0:
                break
        
        maze_for_display = Maze()
        maze_for_display.board = maze
        maze_for_display.start = m.start
        maze_for_display.end = m.end
        display_object.display(maze_for_display)
                    
pf = PathFinder()


                    