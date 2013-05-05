import generator
from htmldisp import *
import webbrowser
import os
import activity_gui

try:
    from custom_gui import *
except SystemExit as e:
    print(e)
else:   
    rows = activity_gui.check_val.rows
    cols = activity_gui.check_val.cols
    # rows = 10
    # cols = 10
    startx = check_val.startx
    starty = check_val.starty
    jump = check_val.jump
    forward = check_val.forward
    birds = check_val.birds
    rd = check_val.rd
    end = check_val.end

    display_object = HTMLDisplay()
    g = generator.Generator([startx,starty,jump,forward,birds,rd,end])
    display_object.display(g.mazes[0])

    # for mac
    os.system("open "+'Maze_output.html');
    # for windows
    os.system("start "+'Maze_output.html');
  
    
