from typing import Protocol
from custom_types import Cycle
from protocols.DistanceMatrixProtocol import DistanceMatrixProtocol


class IndividualProtocol(Protocol):
	cycle: Cycle
	distance_matrix: DistanceMatrixProtocol
	_fitness: float

	@property
	def fitness(self) -> float:
		...

	def mutate(self) -> None:
		...
