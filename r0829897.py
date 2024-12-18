import Reporter
import numpy as np

class Individual:
	def __init__(self, cycle, distance_matrix):
		self.cycle = cycle
		self.distanceMatrix = distance_matrix
		self._fitness = self.calculate_fitness()

	@property
	def fitness(self):
		return self._fitness

	def calculate_fitness(self):
		# TODO: calculate the fitness of the individual
		return 0

	def mutate(self):
		# Your code here.
		return 0

	def __str__(self):
		return str(self.cycle) + " : " + str(self.fitness)

class Population:
	def __init__(self, size, distance_matrix):
		self.size = size
		self.distanceMatrix = distance_matrix
		self.individuals = [Individual(np.random.permutation(distance_matrix.shape[0]), distance_matrix) for _ in range(size)]

	def __str__(self):
		return "\n".join([str(individual) for individual in self.individuals])

class EvolutionaryAlgorithm:
	def __init__(self, distance_matrix):
		self.population = Population(10, distance_matrix)

	def select(self):
		# Your code here.
		return 0

	def recombination(self):
		# Your code here.
		return 0

	def elemination(self):
		# Your code here.
		return 0

def solve_tsp(distance_matrix):
	evolutionary_algorithm = EvolutionaryAlgorithm(distance_matrix)

	convergenceTest = True
	while convergenceTest:
		evolutionary_algorithm.select()
		evolutionary_algorithm.recombination()
		evolutionary_algorithm.elemination()

	return 0

# Modify the class name to match your student number.
class r0829897:

	def __init__(self):
		self.reporter = Reporter.Reporter(self.__class__.__name__)

	# The evolutionary algorithm's main loop
	def optimize(self, filename):
		# Read distance matrix from file.		
		file = open(filename)
		distanceMatrix = np.loadtxt(file, delimiter=",")
		file.close()

		# TODO: Your code here.
		yourConvergenceTestsHere = True
		while( yourConvergenceTestsHere ):
			meanObjective = 0.0
			bestObjective = 0.0
			bestSolution = np.array([1,2,3,4,5])

			# Your code here.

			# Call the reporter with:
			#  - the mean objective function value of the population
			#  - the best objective function value of the population
			#  - a 1D numpy array in the cycle notation containing the best solution 
			#    with city numbering starting from 0
			timeLeft = self.reporter.report(meanObjective, bestObjective, bestSolution)
			if timeLeft < 0:
				break

		# TODO: Your code here.
		return 0

if __name__ == "__main__":
	solve_tsp(np.array([[0, 1, 2], [1, 0, 3], [2, 3, 0]]))