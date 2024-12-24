from methods.InitializationMethods import InitializationMethods
from protocols.DistanceMatrixProtocol import DistanceMatrixProtocol
from protocols.IndividualProtocol import IndividualProtocol


class Population:
	size: int
	distance_matrix: DistanceMatrixProtocol
	individuals: list[IndividualProtocol]

	def __init__(self, size: int, distance_matrix: DistanceMatrixProtocol):
		self.size = size
		self.distance_matrix = distance_matrix
		self.individuals = InitializationMethods.generate_random_valid_population(size, distance_matrix)

	def mean_fitness(self) -> float:
		return sum([individual.fitness for individual in self.individuals]) / self.size

	def best_fitness(self) -> float:
		return max([individual.fitness for individual in self.individuals])

	def best_individual(self) -> IndividualProtocol:
		return max(self.individuals, key=lambda individual: individual.fitness)

	def __str__(self):
		return "\n".join([str(individual) for individual in self.individuals])