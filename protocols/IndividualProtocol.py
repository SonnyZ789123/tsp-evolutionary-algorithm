from typing import Protocol

from config.custom_types import Cycle, DistanceMatrix


class IndividualProtocol(Protocol):
	distance_matrix: DistanceMatrix
	""" 
	The distance matrix representing the distances between the cities. The length of the rows should be equal 
	to the length of the columns, and the length should be equal to the length of the cycle. 
	"""
	fitness_sharing: float
	dirty: bool

	@property
	def fitness(self) -> float:
		""" The fitness of the individual, which can be negative. """
		...

	@property
	def cycle(self) -> Cycle:
		...

	@cycle.setter
	def cycle(self, cycle: Cycle) -> None:
		...

	def get_fitness_internal(self) -> float:
		""" The unmodified fitness of the individual. """
		...

	def mutate(self) -> None:
		...
