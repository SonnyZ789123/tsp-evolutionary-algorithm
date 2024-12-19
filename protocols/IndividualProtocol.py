from typing import Protocol
from custom_types import DistanceMatrix, Cycle


class IndividualProtocol(Protocol):
	cycle: Cycle
	distance_matrix: DistanceMatrix
	_fitness: float

	@property
	def fitness(self) -> float:
		...

	def mutate(self) -> None:
		...

	def __str__(self) -> str:
		...
