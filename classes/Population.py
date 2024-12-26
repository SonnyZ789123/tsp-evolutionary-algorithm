from config.custom_types import DistanceMatrix
from methods.InitializationMethods import InitializationMethods, Heuristics
from protocols.IndividualProtocol import IndividualProtocol


class Population:
	size: int
	distance_matrix: DistanceMatrix
	individuals: list[IndividualProtocol]

	def __init__(self, size: int, distance_matrix: DistanceMatrix):
		# replace every occurrence of "Inf" with -1
		distance_matrix[distance_matrix == float('inf')] = -1

		self.size = size
		self.distance_matrix = distance_matrix
		self.individuals = InitializationMethods.generate_greedy_population(size, distance_matrix,
																			Heuristics.nearest_neighbour)

	def mean_fitness(self) -> float:
		return sum([individual.fitness for individual in self.individuals]) / self.size

	def best_fitness(self) -> float:
		return max([individual.fitness for individual in self.individuals])

	def best_individual(self) -> IndividualProtocol:
		return max(self.individuals, key=lambda individual: individual.fitness)

	def __str__(self):
		return "\n".join([str(individual) for individual in self.individuals])
