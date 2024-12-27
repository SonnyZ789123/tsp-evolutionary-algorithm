from config.custom_types import Cycle, DistanceMatrix
from methods.FitnessMethods import FitnessMethods
from methods.MutationMethods import MutationMethods


class Individual:
	cycle: Cycle
	distance_matrix: DistanceMatrix
	fitness_sharing: float = 1.0
	_fitness: float

	def __init__(self, cycle: Cycle, distance_matrix: DistanceMatrix):
		self.cycle = cycle
		self.distance_matrix = distance_matrix

	@property
	def fitness(self) -> float:
		return self.fitness_sharing * FitnessMethods.negative_of_length(self)

	def mutate(self) -> None:
		MutationMethods.reverse_subtour(self)

	def __str__(self) -> str:
		return str(self.cycle) + " : " + str(self.fitness)
