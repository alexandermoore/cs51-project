import sys
import maze

def display (maze):
    #square = u"\u25A0" #small filled in square
    #square = u"\u20DE" #big enclosing square 
    #square = u"\u25FC"
    #square = u"\uFFED"
 
    # Choose shape to represent a non-walkable square
    square = "X"#unicode(u"\u25A9") #big square diagonal crosshatch

    # Get board from object maze
    list = maze.board

    # Define START coordinates
    start_x = maze.start[0]
    start_y = maze.start[1]

    # Define END coordinates
    end_x = maze.end[0]
    end_y = maze.end[1]

    # Update board (change booleans to "start" and "end")
    list[start_x][start_y] = "start"
    list[end_x][end_y] = "end"

    # Set border to number of columns 
    border_length = 0
    for i in list:
        border_length = len(i)

    # Create upper border
    sys.stdout.write("+")
    for i in range(border_length):
        sys.stdout.write("--")
    print "+\r"

    # Print board
    for i in list:
        sys.stdout.write("|")
        for j in i:
            if j == False : sys.stdout.write(square + ' ')
            elif j == "start" : sys.stdout.write("s ")
            elif j == "end" : sys.stdout.write("e ")
            else : sys.stdout.write("  ")
        print "|" + " \r"

    # Create lower border
    sys.stdout.write("+")
    for i in range(border_length):
        sys.stdout.write("--")
    print "+\r"

# Uncomment this to test the display function 
display(maze.m)
