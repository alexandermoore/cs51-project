import sys
import HTML
from maze import*


# open an HTML file to show output in a browser
HTMLFILE = 'HTML_tutorial_output.html'
f = open(HTMLFILE, 'w')

class HTMLDisplay:
    def display (self, maze):

        #board from ob
        list = maze.baord
        n_rows = maze.maze_num_rows
        n_cols = maze_num_cols
        

         # Define START coordinates
        start_x = maze.start[0]
        start_y = maze.start[1]

        # Define END coordinates
        end_x = maze.end[0]
        end_y = maze.end[1]

        return = "<TABLE ID='TMaze' CELLSPACING=0 CELLPADDING=0> \n"

        # set border
        for i in range n_rows
            result += "<TR HEIGHT = 25>"

            for j in range n_cols
                result += "<TD WIDTH=24 style='"
                if i==0:
                 result += "BORDER-TOP: 2px black solid;"
                if i==n_rows-1:
                  result += "BORDER-BOTTOM: 2px black solid;"
                if j==0:
                  result += "BORDER-LEFT: 2px black solid;"
                if j==self.n_cols-1:
                  result += "BORDER-RIGHT: 2px black solid;"
                result += "'>"

                if i == start_x and j == start_y:
                    result += 'S' # start
                elif i == end_x and j == end_y:
                    result += 'e' # end

    
    
