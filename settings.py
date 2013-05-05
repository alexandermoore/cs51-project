# Make global variables in scope
display_maze_generation_in_real_time = None
display_maze_solution = None
run_genetic_algorithm = None
maze_num_rows = None
maze_num_cols = None
maze_solver = None


import activity_gui
import custom_gui
import genetic_gui

display_maze_generation_in_real_time = custom_gui.check_box.disp_steps
display_maze_solution = custom_gui.check_box.disp_sol
run_genetic_algorithm = activity_gui.check_radio.run_genetic
maze_num_rows = activity_gui.check_val.rows
maze_num_cols = activity_gui.check_val.cols
# solver options: "inverse", "pythagorean", or "smart"
maze_solver = genetic_gui.check_option.solver


if run_genetic_algorithm:
    num_mazes = 10
    display_all_outputted_mazes = False
    display_maze_solution = False
else:
    num_mazes = 1
    display_all_outputted_mazes = True
    smart_solver = "pythagorean"
    
