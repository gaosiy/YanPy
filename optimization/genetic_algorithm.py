import math
import random
import numpy
import progressbar
import nzsci.math.number as number


class GeneticAlgorithm:
    """
    Genetic Algorithm implementation, search the best parameters for a problem
    """

    def __init__(self, max_gen: int, pop_generation: int, p_cross: float,
                 p_mutation: float, n_genes: int, parameters_range: list, fitness_func):

        """
        Constructor.

        :param int max_gen: maximum generation number, the limit of iteration
        :param int pop_generation: population of one generation
        :param float p_cross: probability of cross interchange
        :param float p_mutation: probability of mutation
        :param int n_genes: number of genes (equals to the number of parameters)
        :param list parameters_range: a list of parameters' ranges, one row for each parameter [lower, upper, accuracy],
                                      for integer parameters, just set accuracy as 1
        :param function fitness_func: refer to the fitness function, which should be a function that receive parameters
                                    as input and return fitness value
        """
        self._max_gen_num = max_gen
        self._pop_generation = pop_generation
        self._p_cross = p_cross
        self._p_mutation = p_mutation
        self._n_genes = n_genes
        self._parameters_range = parameters_range

        self.fitness_func = fitness_func

        self._generation = []
        self._fitness_list = []
        self._best_fitness = 0.0
        self._dna_idx = []
        self._gene_length = []
        idx = 0
        for i in range(n_genes):
            lower_limit = parameters_range[i][0]
            upper_limit = parameters_range[i][1]
            accuracy = parameters_range[i][2]
            par_range = upper_limit - lower_limit
            gene_length = math.ceil(math.log2(par_range / accuracy)) + 1
            self._gene_length.append(gene_length)
            start_index = idx
            idx = idx + gene_length
            end_index = idx - 1
            self._dna_idx.append([start_index, end_index])
        self._dna_length = idx
        self._best_individual = list('-' * self._dna_length)
        return

    def info(self):
        """
        Display information of current object, includes:
            - max generation number
            - population of one generation,
            - probability of mutation
            - probability of cross
            - number of genes
            - range of parameters
        """
        print('Genetic Algorithm:')
        print('Max generation number:', self._max_gen_num)
        print('Population of one generation:', self._pop_generation)
        print('Probability of mutation:', self._p_mutation)
        print('Probability of cross:', self._p_cross)
        print('Number of genes(parameters):', self._n_genes)
        print('Range of parameters: [lower, upper, accuracy] ', self._parameters_range)
        return

    def encode(self, parameters: list):
        """
        Encode parameters into DNA, gray code

        :param list parameters: list of parameters
        :return: DNA
        :rtype: list
        """
        dna = ''
        for i in range(self._n_genes):
            gene_sequence_digit = (parameters[i] - self._parameters_range[i][0]) \
                                  / (self._parameters_range[i][1] - self._parameters_range[i][0]) \
                                  * (2 ** self._gene_length[i] - 1)
            gene_sequence_digit = int(round(gene_sequence_digit))
            gene_sequence_bin = number.int2gray(gene_sequence_digit, self._gene_length[i])
            dna = dna + gene_sequence_bin
        dna = list(dna)  # Turn string to list
        return dna

    def decode(self, dna: list):
        """
        Decode DNA to parameters

        :param list dna: string of DNA sequence\
        :return: parameters
        :rtype: list     
        """
        dna = ''.join(dna)  # Turn list to string
        parameters = []
        for i in range(self._n_genes):
            gene_sequence_bin = dna[self._dna_idx[i][0]:self._dna_idx[i][1] + 1]
            gene_sequence_digit = number.gray2int(gene_sequence_bin)
            parameter_i = \
                gene_sequence_digit / (2 ** self._gene_length[i] - 1) \
                * (self._parameters_range[i][1] - self._parameters_range[i][0]) \
                + self._parameters_range[i][0]
            parameters.append(parameter_i)
        return parameters

    def random_dna(self):
        """
        Create random DNA for initially generation

        :return: random DNA sequence
        :rtype: list
        """
        dna = ''
        for i in range(self._n_genes):
            gene_sequence_digit = random.randint(0, 2 ** self._gene_length[i])
            gene_sequence_bin = number.int2gray(gene_sequence_digit, self._gene_length[i])
            dna = dna + gene_sequence_bin
        dna = list(dna)  # Turn string to list
        return dna

    def ini_generation(self):
        """
        Generate initially generation
        """
        for i in range(self._pop_generation):
            self._generation.append(self.random_dna())
        self.fitness()
        self._best_fitness = max(self._fitness_list)
        idx = self._fitness_list.index(self._best_fitness)
        self._best_individual = self._generation[idx].copy()
        return

    def mutation(self):
        """
        Mutation at a random point for a preset probability (entire generation)
        """
        for i in range(self._pop_generation):
            ret = random.random()
            while ret == 0:
                ret = random.random()
            if ret < self._p_mutation:
                mutation_point = random.randint(0, self._dna_length - 1)
                if self._generation[i][mutation_point] == '0':
                    self._generation[i][mutation_point] = '1'
                else:
                    self._generation[i][mutation_point] = '0'
        return

    def cross(self):
        """
        Cross interchange at a random point for a preset probability (entire generation)
        """
        for i in range(self._pop_generation):
            ret = random.random()
            while ret == 0:
                ret = random.random()
            if ret < self._p_cross:
                pair = random.randint(0, self._pop_generation - 1)
                while pair == i:
                    pair = random.randint(0, self._pop_generation - 1)
                cross_point = random.randint(0, self._dna_length - 1)
                self._generation[i][cross_point:-1] = self._generation[pair][cross_point:-1]
        return

    def select(self):
        """
        Select better individuals with a championships strategy
        """
        n_candidates = 2
        generation = []
        for i in range(self._pop_generation):
            candidates = random.choices(self._generation, k=n_candidates)
            fitness_list = self.fitness(candidates=candidates)
            best_fitness = max(fitness_list)
            idx = fitness_list.index(best_fitness)
            generation.append(candidates[idx].copy())
        self._generation = generation
        return

    def elitist_reservation(self):
        """
        Elitist preservation: always preserve the best one
        """
        best_fitness = max(self._fitness_list)
        if best_fitness > self._best_fitness:
            idx = self._fitness_list.index(best_fitness)
            self._best_fitness = best_fitness
            self._best_individual = self._generation[idx].copy()
        else:
            worst_individual = min(self._fitness_list)
            idx = self._fitness_list.index(worst_individual)
            self._generation[idx] = self._best_individual.copy()
            self._fitness_list[idx] = self._best_fitness
        return

    def fitness(self, candidates: str or list = 'None'):
        """
        Calculate fitness for input candidates or for all individuals of current generation (default)

        :param list or str candidates: either be a list of candidates or 'None' (default, all individuals)
        :return: list of fitness
        :rtype: list
        """
        if candidates == 'None':
            self._fitness_list = []
            for dna in self._generation:
                parameters = self.decode(dna)
                self._fitness_list.append(self.fitness_func(parameters))
            return
        else:
            fitness_list = []
            for dna in candidates:
                parameters = self.decode(dna)
                fitness_list.append(self.fitness_func(parameters))
            return fitness_list

    def run(self):
        """
        Start main loop to iterate 'maxGen' generations to find the best individual
        """
        self.ini_generation()
        widgets = [
            'Progress:',
            progressbar.Percentage(),
            '   ',
            progressbar.Bar(),
            progressbar.DynamicMessage('Best'),
            '   ',
            progressbar.DynamicMessage('Average')
        ]
        with progressbar.ProgressBar(max_value=self._max_gen_num + 1, widgets=widgets) as bar:
            print('Genetic Algorithm is running:')
            for i in range(1, self._max_gen_num + 1):
                self.select()
                self.cross()
                self.mutation()
                self.fitness()
                self.elitist_reservation()
                best_fitness = self._best_fitness
                mean_fitness = numpy.mean(self._fitness_list)
                bar.update(i, Best=best_fitness, Average=mean_fitness)
        return

    def result(self):
        """
        Display the results
            - best individual
            - best fitness
            - mean fitness
        """
        mean_fitness = numpy.mean(self._fitness_list)
        print('Best:', ''.join(self._best_individual), '%.3f' % self._best_fitness, 'Mean:%.3f' % mean_fitness)
