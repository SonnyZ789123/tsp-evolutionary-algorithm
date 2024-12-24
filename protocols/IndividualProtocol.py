from typing import Protocol
from config.custom_types import Cycle
from protocols.DistanceMatrixProtocol import DistanceMatrixProtocol


class IndividualProtocol(Protocol):
	cycle: Cycle
	""" The cycle of the individual, represented as a list of indices, from 1 to length of the distance matrix. """
	distance_matrix: DistanceMatrixProtocol
	""" 
	The distance matrix representing the distances between the cities. The length of the rows should be equal 
	to the length of the columns, and the length should be equal to the length of the cycle. 
	"""
	_fitness: float

	@property
	def fitness(self) -> float:
		""" The fitness of the individual, which can be negative. """
		...

	def mutate(self) -> None:
		...
