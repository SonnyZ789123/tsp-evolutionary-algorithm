from typing import List

import numpy as np

from config.custom_types import DistanceMatrix, INFINITY_REPRESENTATION
from methods.SimilarityMethods import SimilarityMethods
from protocols.IndividualProtocol import IndividualProtocol
from utils.cycle_utils import is_valid_cycle


class Population:
	size: int
	distance_matrix: DistanceMatrix
	individuals: list[IndividualProtocol]

	def __init__(self, individuals: List[IndividualProtocol], size: int, distance_matrix: DistanceMatrix):
		assert size == len(individuals)

		# replace every occurrence of "Inf" with -1
		distance_matrix[distance_matrix == float('inf')] = INFINITY_REPRESENTATION

		self.size = size
		self.distance_matrix = distance_matrix
		self.individuals = individuals

	def update_fitness_sharing_proportions(self, similarity_threshold: float = 0.5, shape_exp: float = 1) -> None:
		for individual in self.individuals:
			similarities_above_threshold: List[float] = []
			for other_individual in self.individuals:
				similarity = SimilarityMethods.hamming(individual.cycle, other_individual.cycle)
				if similarity > similarity_threshold:
					# similarity between 0 and 1
					similarities_above_threshold.append(similarity ** shape_exp)
			# limit subtracting to at most 25%
			individual.fitness_sharing = 0.75 + (0.25 * 1 / sum(similarities_above_threshold))

	def mean_fitness(self) -> float:
		""" Calculate the mean fitness of the population, filtering out invalid cycles. """
		valid_individuals_fitness = [individual.fitness for individual in self.individuals if
									 is_valid_cycle(individual.cycle, self.distance_matrix)]
		if len(valid_individuals_fitness) == 0:
			return -INFINITY_REPRESENTATION
		return sum(valid_individuals_fitness) / len(valid_individuals_fitness)

	def best_fitness(self) -> float:
		return max([individual.fitness for individual in self.individuals])

	def best_individual(self) -> IndividualProtocol:
		return max(self.individuals, key=lambda individual: individual.fitness)

	def variance_fitness(self) -> float:
		""" Calculate the variance of the fitness of the population, filtering out invalid cycles. """
		valid_individuals_fitness = [individual.fitness for individual in self.individuals if
									 is_valid_cycle(individual.cycle, self.distance_matrix)]
		return float(np.var(valid_individuals_fitness))

	def valid_invalid_individual_proportion(self) -> tuple[int, int]:
		""" Calculate the proportion of valid and invalid individuals in the population. """
		valid_individuals = [individual for individual in self.individuals if
							 is_valid_cycle(individual.cycle, self.distance_matrix)]
		return len(valid_individuals), self.size - len(valid_individuals)

	def __str__(self):
		return "\n".join([str(individual) for individual in self.individuals])
