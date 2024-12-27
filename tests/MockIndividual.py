from typing import Callable

from protocols.IndividualProtocol import IndividualProtocol
from config.custom_types import Cycle, DistanceMatrix


class MockIndividual:
	cycle: Cycle
	distance_matrix: DistanceMatrix
	fitness_sharing: float = 0.
	_fitness: float
	mock_fitness_method: Callable[[IndividualProtocol], float]
	mock_mutate_method: Callable[[IndividualProtocol], None]

	def __init__(self, cycle: Cycle, distance_matrix: DistanceMatrix,
				 mock_fitness_method: Callable[[IndividualProtocol], float],
				 mock_mutate_method: Callable[[IndividualProtocol], None]):
		self.cycle = cycle
		self.distance_matrix = distance_matrix
		self.mock_fitness_method = mock_fitness_method
		self.mock_mutate_method = mock_mutate_method

	@property
	def fitness(self) -> float:
		return self.mock_fitness_method(self)

	def get_fitness_internal(self) -> float:
		return self.mock_fitness_method(self)

	def mutate(self) -> None:
		self.mock_mutate_method(self)
