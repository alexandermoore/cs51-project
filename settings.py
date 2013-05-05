'''
Note this is a file to allow me to change global settings without having to
import main (and hence run the whole program).
'''
 
try:
    from activity_gui import *
    from custom_gui import *
    from genetic_gui import *
except SystemExit as e:
    print(e)
else:
    display_maze_generation_in_real_time = check_box.disp_steps
    display_maze_solution = check_box.disp_sol
    run_genetic_algorithm = check_radio.run_genetic
    maze_num_rows = check_val.rows
    maze_num_cols = check_val.cols
    # solver options: "inverse", "pythagorean", or "smart"
    maze_solver = check_option.solver

if run_genetic_algorithm:
    num_mazes = 10
    display_all_outputted_mazes = False
    display_maze_solution = False
else:
    num_mazes = 1
    display_all_outputted_mazes = True
    
