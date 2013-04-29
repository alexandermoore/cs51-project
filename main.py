from generation import *
# from display import *

# Create a new generation
# 5 fittest breed next generation, population size of 250, 50 of which are random and 2 of which are the fittest from the previous generation.
current_gen = Generation(5,5,2,1)
current_gen.spawn_random_generation()

# Set the definition of "no more progress"-- evolution
# after this)
negligible = 0.00001

# Make sure new_fitness - best_fitness cannot be < negligible 
# on first run
best_fitness = -negligible - 1

# Actual loop
gen_num = 0
bad_gen_count = 0
# Terminate after 10 successive negligible generations.
bad_gen_termination = 10
best_generator = None

while(True) :
    gen_num = gen_num + 1
    print "\nGENERATION #"+str(gen_num)
    # run this generation and get its fitness
    new_fitness = current_gen.run()
    print "BEST FROM THIS GENERATION:"
    print new_fitness
    print "CURENT BEST:"
    print best_fitness
    print "DIFFERENCE FROM BEST GENERATION:"
    print new_fitness-best_fitness
    # if change is non-negligible then spawn the next
    # generation and try again. Otherwise you've got an
    # optimal generation.
    if (new_fitness - best_fitness > negligible) :
        bad_gen_count = 0
        best_generator = current_gen.fittest[0]
        best_fitness = new_fitness
    else :
        bad_gen_count = bad_gen_count + 1
        print "BAD GENERATION "+str(bad_gen_count)+"\n"
        if (bad_gen_count == bad_gen_termination) :
            break
    # Spawn the next generation
    current_gen = current_gen.spawn_next_generation()


print "\n\nBEST GENERATOR: "
print best_generator.parameter_list
print best_generator.avg_runtime

# Display the fittest maze of them all	
#display_object = MazeDisplay()
#display_object.display(current_generation.fittest[0])
