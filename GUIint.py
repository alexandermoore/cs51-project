import generator
from htmldisp import *
import webbrowser
import os

try:
    import GUI
except SystemExit as e:
    print(e)
else:   
    rows = GUI.check_val.rows
    cols = GUI.check_val.cols
    startx = GUI.check_val.startx
    starty = GUI.check_val.starty
    jump = GUI.check_val.jump
    forward = GUI.check_val.forward
    birds = GUI.check_val.birds
    rd = GUI.check_val.rd
    end = GUI.check_val.end

    display_object = HTMLDisplay()
    g = generator.Generator([startx,starty,jump,forward,birds,rd,end])
    display_object.display(g.mazes[0])

    # for mac
    os.system("open "+'Maze_output.html');
    # for windows
    # os.system("start "+'Maze_output.html');
  
    
