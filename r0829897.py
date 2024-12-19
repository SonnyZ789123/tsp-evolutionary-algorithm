from select import select

from numpy.typing import NDArray

import Reporter
import numpy as np

from EliminationMethods import EliminationMethods
from FitnessMethods import FitnessMethods
from MutationMethods import MutationMethods
from RecombinationMethods import RecombinationMethods
from SelectionMethods import SelectionMethods
from Settings import Settings
from protocols.EvolutionaryAlgorithmProtocol import EvolutionaryAlgorithmProtocol
from protocols.PopulationProtocol import PopulationProtocol
from protocols.IndividualProtocol import IndividualProtocol
from custom_types import Cycle, DistanceMatrix
from protocols.SettingsProtocol import SettingsProtocol


class Individual:
	cycle: Cycle
	distance_matrix: DistanceMatrix
	_fitness: float

	def __init__(self, cycle: Cycle, distance_matrix: DistanceMatrix):
		self.cycle = cycle
		self.distance_matrix = distance_matrix

	@property
	def fitness(self) -> float:
		return FitnessMethods.negative_of_length(self)

	def mutate(self) -> None:
		MutationMethods.swap_mutation(self)

	def __str__(self) -> str:
		return str(self.cycle) + " : " + str(self.fitness)


class Population:
	size: int
	distance_matrix: DistanceMatrix
	individuals: list[IndividualProtocol]

	def __init__(self, size: int, distance_matrix: NDArray[np.float64]):
		self.size = size
		self.distance_matrix = distance_matrix
		self.individuals = [Individual(np.random.permutation(distance_matrix.shape[0]), distance_matrix) for _ in
							range(size)]

	def __str__(self):
		return "\n".join([str(individual) for individual in self.individuals])


class EvolutionaryAlgorithm:
	settings: SettingsProtocol = Settings()
	population: PopulationProtocol
	_offsprings: list[IndividualProtocol] = []
	_converged: bool

	def __init__(self, distance_matrix: NDArray[np.float64]):
		self.population = Population(10, distance_matrix)

	@property
	def converged(self) -> bool:
		return False

	def select(self) -> Individual:
		return SelectionMethods.random(self.population)

	def recombination(self) -> None:
		for _ in range(self.settings.initialization.population_size // 2):
			parent1 = self.select()
			parent2 = self.select()
			(offspring1, offspring2) = RecombinationMethods.partially_mapped_crossover(parent1, parent2)
			self._offsprings.append(offspring1)
			self._offsprings.append(offspring2)

	def elimination(self) -> None:
		new_individuals = EliminationMethods.age_based(self.population, self._offsprings)
		self.population.individuals = new_individuals


def solve_tsp(distance_matrix: NDArray[np.float64]):
	"""
    :param distance_matrix: should be a 2D numpy array
    """
	assert distance_matrix.ndim == 2  # distance_matrix should be a 2D array
	assert distance_matrix.shape[0] == distance_matrix.shape[1]  # distance_matrix should be square
	evolutionary_algorithm: EvolutionaryAlgorithmProtocol = EvolutionaryAlgorithm(distance_matrix)

	while not evolutionary_algorithm.converged:
		evolutionary_algorithm.select()
		evolutionary_algorithm.recombination()
		evolutionary_algorithm.elimination()

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
		while (yourConvergenceTestsHere):
			meanObjective = 0.0
			bestObjective = 0.0
			bestSolution = np.array([1, 2, 3, 4, 5])

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
