'''
Note this is a temporary file to allow me to change global settings without having to
import main (and hence run the whole program).
'''

try:
    import GUI
except SystemExit as e:
    print(e)
else:
    display_maze_generation_in_real_time = True
    display_all_outputted_mazes = False
    maze_num_rows = GUI.check_val.rows
    maze_num_cols = GUI.check_val.cols
    num_mazes = 10
