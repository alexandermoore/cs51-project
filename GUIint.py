import generator
from htmldisp import *
import webbrowser
import os
import activity_gui
from custom_gui import *


# Related to Activity GUI
rows = activity_gui.check_val.rows
cols = activity_gui.check_val.cols

# Run Genetic Algorithm
if activity_gui.check_radio.run_genetic==True:
    from genetic_gui import *
    from main import *
    size = check_val.size
    fittest = check_val.fittest
    random = check_val.random
    elites = check_val.elites
    main(size,fittest,random,elites)
    

# Build Custom Maze
else:
    from custom_gui import *
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
  
    
