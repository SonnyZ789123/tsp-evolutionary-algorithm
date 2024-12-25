from typing import Protocol

from config.custom_types import DistanceMatrix
from protocols.IndividualProtocol import IndividualProtocol


class PopulationProtocol(Protocol):
	size: int
	distance_matrix: DistanceMatrix
	individuals: list[IndividualProtocol]

	def mean_fitness(self) -> float:
		...

	def best_fitness(self) -> float:
		...

	def best_individual(self) -> IndividualProtocol:
		...
