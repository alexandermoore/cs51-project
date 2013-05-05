from generation import *
from display import *
from htmldisp import *
import sys

# DEBUGGING IS OFF
debug_on = False

''' debug_print
Prints the text if debugging or ignoring is enabled.
RETURNS: No return value
-txt (stirng) : The item to print
-ignore_debug (boolean) : Whether or not this print statement should occur regardless of whether or not you're debugging
'''
def debug_print(txt,ignore_debug) :
    if (debug_on or ignore_debug):
        print txt

''' txt_is_true
RETURNS: Whether or not the text is indicative of the idea "true"
-txt (string): The text to evaluate
'''
def txt_is_true(txt) :
    return (txt.lower() == 'true') or (txt.lower() == 'yes') or (txt.lower() == 'y') or (txt.lower() == '1')

''' check
Helps ensure that num_fittest + num_random + num_elites < population_size
Whoops we also need to check that num_elites < num_fittest
RETURNS: The result of the subtraction
-acc (int) : How much "population" is left.
-num (int) : How much to subtract.
'''
def check(acc,num) :
    if acc - num < 0 :
        throw_error("ERROR:\nnum_fittest + num_random + num_elites must be less than population_size.")
        return None
    else:
        return acc - num
        
''' throw_error
Throws an error and exits.
RETURNS: No return value
-err (string) : The error to print
'''    
def throw_error(err) :
    print err
    sys.exit()

'''
# Get commandline arguments (if running main directly)
if len(sys.argv) == 5 :
    pop_size = int(sys.argv[1])
    acc = pop_size
    
    num_fittest = int(sys.argv[2])
    acc = check(acc,num_fittest)
    
    num_random = int(sys.argv[3])
    acc = check(acc,num_random)
    
    num_elites = int(sys.argv[4])
    acc = check(acc,num_elites)
else:
    throw_error('Useage:\npython main.py [population_size] [num_fittest] [num_random] [num_elites]')
    #[display maze generation in realtime] [display all outputted mazes]')
'''

def main(pop_size, num_fittest, num_random, num_elites) :
    # Create a new generation
    current_gen = Generation(pop_size,num_fittest,num_random,num_elites)
    current_gen.spawn_random_generation()

    # Set the definition of "no more progress"
    negligible = 0.0

    best_fitness = None
    just_started = True

    # Actual loop
    gen_num = 0
    bad_gen_count = 0
    # Terminate after 3 successive negligible generations.
    bad_gen_termination = 3
    best_generator = None

    while(True) :
        gen_num = gen_num + 1
        debug_print("\nGENERATION #"+str(gen_num)+" COMPLETE",True)
        
        # run this generation and get its fitness
        new_fitness = current_gen.run()
        if just_started :
            best_fitness = new_fitness
        
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
        elif not just_started :
            bad_gen_count = bad_gen_count + 1
            debug_print("NO PROGRESS GENERATION #"+str(bad_gen_count)+" / "+str(bad_gen_termination)+"\n", True)
            if (bad_gen_count == bad_gen_termination) :
                break
        else :
            just_started = False
            # Make sure not to return None if best generator appears first by chance
            best_generator = current_gen.fittest[0]
        # Spawn the next generation from the previous generation (even if it was bad!)
        current_gen = current_gen.spawn_next_generation()

    
    # Print info about generator
    # This is specfic to our project, which uses 7 parameters.
    annotations = ["Start Location Row","Start Location Column","Jump Probability","Forward Probability","Birds-Eye Probability","Return Distance Ratio","End Time Ratio"]
    
    debug_print("\n\nBEST GENERATOR: ", True)
    for i in range(0, 7) :
        debug_print(annotations[i] + ": " + str(best_generator.parameter_list[i]), True)
    debug_print("\nAVG RUNTIME: " + str(best_generator.avg_runtime), True)

    # Display mazes
    debug_print("\nALL MAZES:", True)
    display_obj = MazeDisplay()
    htmldisplay_obj = HTMLDisplay()
    num_of_mazes = len(best_generator.mazes)
    for m in range(0, num_of_mazes) :
        if m == num_of_mazes - 1 :
            debug_print("\nVERY BEST MAZE:\n", True)
        display_obj.display(best_generator.mazes[m])
    htmldisplay_obj.display(best_generator.mazes[num_of_mazes - 1])

# Actually run the code with the correct parameters.
#main(pop_size, num_fittest, num_fittest, num_elites)