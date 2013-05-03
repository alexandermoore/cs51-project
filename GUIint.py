import time
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

    time.sleep(4)

    display_object = HTMLDisplay()
    g = generator.Generator([startx,starty,jump,forward,birds,rd,end])
    display_object.display(g.mazes[0])

    # webbrowser.open('Maze_ouput.html')
    webbrowser.get("macosx").open('Maze_output.html')
    # for windows
    # os.startfile('Maze-output.html')
    #open("Maze_output.html")
    #os.startfile('Maze_output.html')
    # execfile("MazeOutput.html")
    # open Maze_output
    #print('Just kidding!')
    
