'''
Note this is a file to allow me to change global settings without having to
import main (and hence run the whole program).
'''

try:
    from activity_gui import *
except SystemExit as e:
    print(e)
else:
    display_maze_generation_in_real_time = False
    display_all_outputted_mazes = False
    maze_num_rows = check_val.rows
    maze_num_cols = check_val.cols
    num_mazes = 10
