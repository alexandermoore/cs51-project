from generation import *
# from display import *

# Create a new generation
# 5 fittest breed next generation, population size of 250, 50 of which are random and 2 of which are the fittest from the previous generation.
current_gen = Generation(5,5,1,1)
current_gen.spawn_random_generation()

# Set the definition of "no more progress"-- evolution
# after this)
negligible = 0.00001

# Make sure new_fitness - old_fitness cannot be > negligible 
# on first run
old_fitness = -negligible - 1

#Actual loop
gen_num = 0
while(True) :
    gen_num = gen_num + 1
    print "\nGENERATION #"+str(gen_num)
    # run this generation and get its fitness
    new_fitness = current_gen.run()
    print "BEST:"
    print current_gen.fittest[0].avg_runtime
    print "DIFFERENCE FROM LAST GENERATION:"
    print new_fitness-old_fitness
    # if change is non-negligible then spawn the next
    # generation and try again. Otherwise you've got an
    # optimal generation.
    if (new_fitness - old_fitness > negligible) :
        old_fitness = new_fitness
        current_gen = current_gen.spawn_next_generation()
    else :
        break


print "\n\nBEST GENERATOR: "
print current_gen.fittest[0].parameter_list

# Display the fittest maze of them all	
#display_object = MazeDisplay()
#display_object.display(current_generation.fittest[0])
