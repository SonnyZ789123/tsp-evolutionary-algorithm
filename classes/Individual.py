from config.custom_types import Cycle
from methods.FitnessMethods import FitnessMethods
from methods.MutationMethods import MutationMethods
from protocols.DistanceMatrixProtocol import DistanceMatrixProtocol


class Individual:
	cycle: Cycle
	distance_matrix: DistanceMatrixProtocol
	_fitness: float

	def __init__(self, cycle: Cycle, distance_matrix: DistanceMatrixProtocol):
		self.cycle = cycle
		self.distance_matrix = distance_matrix

	@property
	def fitness(self) -> float:
		return FitnessMethods.negative_of_length(self)

	def mutate(self) -> None:
		MutationMethods.swap_mutation(self)

	def __str__(self) -> str:
		return str(self.cycle) + " : " + str(self.fitness)