from typing import Protocol

from protocols.IndividualProtocol import IndividualProtocol
from protocols.PopulationProtocol import PopulationProtocol


class EvolutionaryAlgorithmProtocol(Protocol):
	population: PopulationProtocol

	@property
	def converged(self) -> bool:
		...

	def update_fitness_sharing_proportions(self) -> None:
		...

	def select(self) -> IndividualProtocol:
		...

	def mutation(self) -> None:
		...

	def recombination(self) -> None:
		...

	def elimination(self) -> None:
		...
