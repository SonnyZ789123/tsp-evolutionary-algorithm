from typing import Protocol

from protocols.PopulationProtocol import PopulationProtocol
from protocols.IndividualProtocol import IndividualProtocol


class EvolutionaryAlgorithmProtocol(Protocol):
	population: PopulationProtocol
	_converged: bool

	def select(self) -> IndividualProtocol:
		...

	def recombination(self) -> None:
		...

	def elimination(self) -> None:
		...

	@property
	def converged(self) -> bool:
		...
