import numpy as np

from config.custom_types import DistanceMatrix, INFINITY_REPRESENTATION
from methods.InitializationMethods import InitializationMethods, Heuristics
from protocols.IndividualProtocol import IndividualProtocol
from utils.cycle_utils import is_valid_cycle, get_cycle_distances


class Population:
	size: int
	distance_matrix: DistanceMatrix
	individuals: list[IndividualProtocol]

	def __init__(self, size: int, distance_matrix: DistanceMatrix):
		# replace every occurrence of "Inf" with -1
		distance_matrix[distance_matrix == float('inf')] = INFINITY_REPRESENTATION

		self.size = size
		self.distance_matrix = distance_matrix
		greedy_individual = InitializationMethods.generate_greedy_individual(distance_matrix,
																			 Heuristics.nearest_neighbour)
		random_individuals = InitializationMethods.generate_random_valid_population(size - 1, distance_matrix)
		self.individuals = [greedy_individual] + random_individuals

	def mean_fitness(self) -> float:
		""" Calculate the mean fitness of the population, filtering out invalid cycles. """
		valid_individuals_fitness = [individual.fitness for individual in self.individuals if
									 is_valid_cycle(individual.cycle, self.distance_matrix)]
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
