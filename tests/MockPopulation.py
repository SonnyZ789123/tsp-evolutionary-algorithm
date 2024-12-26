from config.custom_types import DistanceMatrix
from protocols.IndividualProtocol import IndividualProtocol


class MockPopulation:
	size: int
	distance_matrix: DistanceMatrix
	individuals: list[IndividualProtocol]

	def __init__(self, distance_matrix, individuals: list[IndividualProtocol]):
		self.size = len(individuals)
		self.distance_matrix = distance_matrix
		self.individuals = individuals

	def mean_fitness(self) -> float:
		pass

	def best_fitness(self) -> float:
		pass

	def best_individual(self) -> IndividualProtocol:
		pass

	def variance_fitness(self) -> float:
		pass

	def valid_invalid_individual_proportion(self) -> tuple[int, int]:
		pass
