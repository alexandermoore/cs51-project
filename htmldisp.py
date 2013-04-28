import sys
import HTML
#from maze import*



# open an HTML file to show output in a browser
HTMLFILE = 'Maze_output.html'
f = open(HTMLFILE, 'w')

#board from ob
list = [[True, True, False, True, False], [True, False, True, False, True],[True, False, True, True, True]]
n_rows = 3
n_cols = 5
        

# Define START coordinates
start_x = 0
start_y = 0

# Define END coordinates
end_x = 2
end_y = 4

result = "<TABLE ID='TMaze' CELLSPACING=0 CELLPADDING=0> \n"

# set border
for i in range (n_rows):
    result += "<TR HEIGHT = 25>"

    for j in range (n_cols):
        result += "<TD WIDTH=24 style='"
        if i==0:
            result += "BORDER-TOP: 2px black solid;"
        if i==n_rows-1 or (list[i][j]==False and list[i][j+1]==False):
            result += "BORDER-BOTTOM: 2px black solid;"
        if j==0 or (list[i][j] == False):
            result += "BORDER-LEFT: 2px black solid;"
        if j==n_cols-1:
            result += "BORDER-RIGHT: 2px black solid;"
        result += "'>"

        # set start and end
        if i == start_x and j == start_y:
            result += 'S' 
        if i == end_x and j == end_y:
            result += 'E'

        else:
            result += "&nbsp;"
        result += "</TD>\n"

    result += "</TR>\n"
            
result += "</TABLE>\n"


#return result
f.write(result)
   
