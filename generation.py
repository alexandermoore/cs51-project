import random
# from generator import *

class Generator :

    parameter_list = []
    avg_runtime = 1337.0
    def __init__(self,params) :
        self.parameter_list = [e for e in params]
        def test(p) :
            if abs(p - 0.5) <= 0.2 :
                return p
            else :
                return 0.0
        new_lst = [test(params[e]) for e in range(0,len(params))]
        self.avg_runtime = sum(new_lst)
    

class Generation :
    # Genetic algorithm parameters
    
    # The top "num_fittest" generators will be taken from each generation
    # for breeding.
    num_fittest = 5
    # Size of each new generation
    pop_size = 100
    # Fittest members of current population
    fittest = []
    # Generator objects in population
    generators = []
    # # of parameters in Generator class
    generator_param_count = 6
    # Number of random generators to add each time
    num_random = 0
    # Number of members from the fittest generators to keep in the population. Implements "elitism" so best genes are allowed to survive.
    num_elites = 2
    
    # Initialize num_fittest, pop_size, num_random and num_elites.
    # TYPES: __init__(Generation, int, int, int) : unit
    def __init__(self,num_fit,pop_sz,num_rnd,elites) :
        self.num_fittest = num_fit
        self.pop_size = pop_sz
        self.num_random = num_rnd
        self.num_elites = elites
    
    # Updates "fittest" with the most fit Generators.
    # TYPES: update_fittest() : unit   
    def update_fittest(self) :
        # Sort by avg_runtime and get top num_fittest
        self.generators.sort(key = lambda x: x.avg_runtime)
        self.generators.reverse()
        self.fittest = self.generators[:self.num_fittest]
        
    # Spawns a new Generation of Generators with random parameters.
    # TYPES: spawn_random_generation() : unit
    def spawn_random_generation(self) :
        self.generators = self.__make_random_generators(self.pop_size)
    
    def __make_random_generators(self,count) :
        rand_gens = []
        # Create pop_size new generators with random parameters.
        for i in range(0, count) :
            new_gen = Generator([random.random() for x in range (0,self.generator_param_count)])
            rand_gens.append(new_gen)
        return rand_gens
    
    # Helper function. Each generator in the list will be associated with
    # a range of numbers. 
    # If the randomly selected number is in an object's
    # range, then that objects is the one that was selected. This allows for
    # proper weighting of probabilities. The "range" need only be represented
    # by an upper bound, for the check works like so:
    #   Iterate through each element in the list-- if random number is less
    #   than an element's upper bound then it is selected.
    def __add_probabilities(self,gens) :
        prob_list = []
        upper_bound = 0
        for g in gens :
            upper_bound = upper_bound + g.avg_runtime
            prob_list.append((g, upper_bound))
        return prob_list
    
    # Gets a random probabilistically selected element from prob_list. 
    # Returns a tuple of the element and the rest of the list without the element.
    def __get_probabilistic_random(self,prob_list) :
        # Get upper bound for random number (2nd part of tuple in last element of list)
        upper_bound = prob_list[-1][1]
        # Choose a random number
        num = random.random()*upper_bound
        # Make a copy of prob_list so we don't modify the original
        prob_list_cpy = list(prob_list)
        # Figure out which element was selected
        # By default, winner = last element
        winner = prob_list[-1]
        for o in prob_list :
            if (num <= o[1]) :
                winner = o[0]
                prob_list_cpy.remove(o)
                break
        # return the random element
        return (winner, prob_list_cpy)
        
    # Spawns a new generation of generators created by breeding the 
    # Generators contained in fittest.
    # TYPES: spawn_next_generation() : Generation
    def spawn_next_generation(self) :
    
        # Add probabilities to the fittest for "roulette wheel" selection.
        prob_fittest = self.__add_probabilities(self.fittest)
        
        # Create children from the parents
        children = []
        for i in range(0, self.pop_size - self.num_random - self.num_elites) :
            children.append(self.__spawn_child(prob_fittest))
        
        # Create the new generation
        new_gen = Generation(self.num_fittest,self.pop_size,self.num_random,self.num_elites)
        # Change generators of the new generation to contain the children, random new generators and the elites from this generation.
        new_gen.generators = children + self.__make_random_generators(self.num_random) + self.fittest[:self.num_elites]
        return new_gen
    
    # Outputs one child of two probabilistically selected members of
    # prob_fittest. Probability weight is based on fitness (runtimes) and
    # should be contained in prob_fittest.
    # Private.
    # TYPES: __spawn_child( (Generator * int) List) : Generator
    def __spawn_child (self,prob_fittest) :
        # Select the first parent.
        p1_tuple = self.__get_probabilistic_random(prob_fittest)
        p1 = p1_tuple[0]
        # Select the second parent from the remaining potential parents.
        p2 = self.__get_probabilistic_random(p1_tuple[1])[0]
        # Breed a child and return it
        return self.__breed(p1, p2)
    
    # Mutates a gene.
    def __mutate(self,gene) :
        chance = 0.1
        stddev = 0.2
        # Gaussian distribution mutation
        if random.random() < chance :
            return min(1.0, max(0.0, random.gauss(gene,stddev)))
        else :
            return gene
            
        # Uniform distribution mutation
        # amplitude = 0.2
        #chance = 0.1
        #if random.random() < chance :
        #    gene = min(1.0, max(0.0, gene + amplitude*(random.random()-0.5)))
        #else :
        #    gene
        #return gene
    
    # Breeds generators g1 and g2 via some crossing over method.
    def __breed(self,g1, g2) :
        # THIS IS A WEIGHTED UNIFORM CROSSOVER.
        # http://en.wikipedia.org/wiki/Crossover_(genetic_algorithm)#Uniform_Crossover_and_Half_Uniform_Crossover
        # More fit = more likely to pass on genes.
        
        # Get each one's runtime to calculate weight.
        g1r = float(g1.avg_runtime)
        g2r = float(g2.avg_runtime)
        # g1's share of the total fitness.
        weight = g1r / (g1r + g2r)
        # Cross over parameters randomly
        params1 = g1.parameter_list
        params2 = g2.parameter_list
        newparams = []
        for i in range(0,self.generator_param_count) :
            # If in g1's share of fitness, pass on g1's parameter.
            # Otherwise pass on g2's parameter.
            if (random.random() < weight) :
                gene = params1[i]
            else :
                gene = params2[i]
            newparams = newparams + [self.__mutate(gene)]
        # Return the child with the new parameters
        return Generator(newparams)
    
    # Creates the list of most fit Generators and returns the average runtime
    # of the most fit generator.
    # TYPES: run : float
    def run(self) :
        self.update_fittest()
        return self.fittest[0].avg_runtime
    
  