from generation import *
from display import *

# Create a new generation
# 5 fittest breed next generation, population size of 250, 50 of which are random and 2 of which are the fittest from the previous generation.
# (num_fittest, pop_size, num_random, num_elites)
current_gen = Generation(5,10,2,2)
current_gen.spawn_random_generation()

# Set the definition of "no more progress"-- evolution
# after this)
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
    print "\nGENERATION #"+str(gen_num)
    
    # run this generation and get its fitness
    new_fitness = current_gen.run()
    
    # Print some information about this generation
    print "BEST FROM THIS GENERATION:"
    print new_fitness
    print "CURENT BEST:"
    print best_fitness
    if (best_generator != None) :
        print best_generator.parameter_list
    print "DIFFERENCE FROM BEST GENERATOR:"
    print new_fitness-best_fitness
    
    # If the change is non-negligible, record the fittest generator in the generation as the best.
    if (new_fitness - best_fitness > negligible) :
        bad_gen_count = 0
        best_generator = current_gen.fittest[0]
        best_fitness = new_fitness
    # Otherwise, say this is a bad generation and move on.
    else :
        bad_gen_count = bad_gen_count + 1
        print "BAD GENERATION "+str(bad_gen_count)+"\n"
        if (bad_gen_count == bad_gen_termination) :
            break
    # Spawn the next generation from the previous generation (even if it was bad!)
    current_gen = current_gen.spawn_next_generation()


print "\n\nBEST GENERATOR: "
print best_generator.parameter_list
print best_generator.avg_runtime

# Display the fittest mazes
display_object = MazeDisplay()
for m in best_generator.mazes :
    display_object.display(m)
