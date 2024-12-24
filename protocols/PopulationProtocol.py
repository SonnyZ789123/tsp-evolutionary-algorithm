from typing import Protocol

from protocols.DistanceMatrixProtocol import DistanceMatrixProtocol
from protocols.IndividualProtocol import IndividualProtocol


class PopulationProtocol(Protocol):
	size: int
	distance_matrix: DistanceMatrixProtocol
	individuals: list[IndividualProtocol]

	def mean_fitness(self) -> float:
		...

	def best_fitness(self) -> float:
		...

	def best_individual(self) -> IndividualProtocol:
		...
