from typing import Protocol

from protocols.IndividualProtocol import IndividualProtocol
from protocols.PopulationProtocol import PopulationProtocol


class EvolutionaryAlgorithmProtocol(Protocol):
	population: PopulationProtocol

	@property
	def converged(self) -> bool:
		...

	def select(self) -> IndividualProtocol:
		...

	def mutation(self) -> None:
		...

	def recombination(self) -> None:
		...

	def elimination(self) -> None:
		...
