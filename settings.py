# Make global variables in scope
display_maze_generation_in_real_time = None
display_maze_solution = None
run_genetic_algorithm = None
maze_num_rows = None
maze_num_cols = None
maze_solver = None


try:
    from activity_gui import *
except SystemExit as e:
    print(e)
else:
    display_maze_generation_in_real_time = False
    display_maze_solution = False
    run_genetic_algorithm = False
    maze_num_rows = check_val.rows
    maze_num_cols = check_val.cols
    # solver options: "inverse", "pythagorean", or "smart"
    maze_solver = "smart"

if run_genetic_algorithm:
    num_mazes = 10
    display_all_outputted_mazes = False
    display_maze_solution = False
else:
    num_mazes = 1
    display_all_outputted_mazes = True
    smart_solver = pythagorean
    
