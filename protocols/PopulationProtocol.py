from typing import Protocol, Optional

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

	def variance_fitness(self) -> float:
		...

	def valid_invalid_individual_proportion(self) -> tuple[int, int]:
		...

	def update_fitness_sharing_proportions(self, similarity_threshold: Optional[float],
										   shape_exp: Optional[float]) -> None:
		...
