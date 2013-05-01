from generation import *
from display import *
from htmldisp import *

# DEBUGGING IS OFF
debug_on = False

'''
debug_print
RETURNS: No return value
-txt : The item to print
-ignore_debug (boolean) : Whether or not this print statement should occur regardless of whether or not you're debugging
'''
def debug_print(txt,ignore_debug) :
    if (debug_on or ignore_debug):
        print txt

### SETTINGS
#intentionally long names for global variables to not clutter namespace
display_maze_generation_in_real_time = False
display_all_outputted_mazes = True

# Create a new generation
# 5 fittest breed next generation, population size of 10, 2 of which are random and 2 of which are the fittest from the previous generation.
# (num_fittest, pop_size, num_random, num_elites)
current_gen = Generation(5,10,2,2)
current_gen.spawn_random_generation()

# Set the definition of "no more progress"
negligible = 0.01

# Make sure new_fitness - best_fitness cannot be < negligible 
# on first run
best_fitness = -negligible - 1

# Actual loop
gen_num = 0
bad_gen_count = 0
# Terminate after 10 successive negligible generations.
bad_gen_termination = 3
best_generator = None

while(True) :
    gen_num = gen_num + 1
    debug_print("\nGENERATION #"+str(gen_num)+" COMPLETE",True)
    
    # run this generation and get its fitness
    new_fitness = current_gen.run()
    
    # Print some information about this generation
    debug_print("BEST FROM THIS GENERATION:", False)
    debug_print(new_fitness, False)
    debug_print("CURENT BEST:", False)
    debug_print(best_fitness, False)
    if (best_generator != None) :
        debug_print(best_generator.parameter_list, False)
    debug_print("DIFFERENCE FROM BEST GENERATOR:", False)
    debug_print(new_fitness-best_fitness, False)
    
    # If the change is non-negligible, record the fittest generator in the generation as the best.
    if (new_fitness - best_fitness > negligible) :
        bad_gen_count = 0
        best_generator = current_gen.fittest[0]
        best_fitness = new_fitness
    # Otherwise, say this is a bad generation and move on.
    else :
        bad_gen_count = bad_gen_count + 1
        debug_print("BAD GENERATION "+str(bad_gen_count)+" / "+str(bad_gen_termination)+"\n", False)
        if (bad_gen_count == bad_gen_termination) :
            break
    # Spawn the next generation from the previous generation (even if it was bad!)
    current_gen = current_gen.spawn_next_generation()


debug_print("\n\nBEST GENERATOR: ", True)
debug_print(best_generator.parameter_list, True)
debug_print(best_generator.avg_runtime, True)

# Display the fittest mazes
display_obj = MazeDisplay()
htmldisplay_obj = HTMLDisplay()
for m in best_generator.mazes :
    display_object.display(m)
debug_print("DISPLAYING FIRST ONE", False)
display_obj.display(best_generator.mazes[0])
htmldisplay_obj.display(best_generator.mazes[0])
