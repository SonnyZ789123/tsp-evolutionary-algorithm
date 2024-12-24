import numpy as np

from classes.Individual import Individual
from protocols.DistanceMatrixProtocol import DistanceMatrixProtocol
from protocols.IndividualProtocol import IndividualProtocol


class Population:
	size: int
	distance_matrix: DistanceMatrixProtocol
	individuals: list[IndividualProtocol]

	def __init__(self, size: int, distance_matrix: DistanceMatrixProtocol):
		self.size = size
		self.distance_matrix = distance_matrix
		self.individuals = [Individual(np.random.permutation(distance_matrix.value.shape[0]), distance_matrix) for _ in
							range(size)]

	def __str__(self):
		return "\n".join([str(individual) for individual in self.individuals])