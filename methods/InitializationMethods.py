from typing import List

import numpy as np
from numpy.typing import NDArray

from config.custom_types import DistanceMatrix, InitializationHeuristic, INFINITY_REPRESENTATION
from protocols.IndividualProtocol import IndividualProtocol
from classes.Individual import Individual
from protocols.SettingsProtocol import InitializationSettingsProtocol


class Heuristics:
	"""
	All methods should be of type InitializationHeuristic.
	"""

	@staticmethod
	def nearest_neighbour(city: int, distance_matrix: DistanceMatrix, available_cities: List[int]) -> int:
		"""
		Heuristic that selects the nearest neighbour to the given city.
		:return: The index of the nearest neighbour, or -1 if there are no available cities.
		"""
		distances: NDArray[float] = distance_matrix[city]
		# Get the indices of the available cities
		available_distances = [(next_city, distances[next_city]) for next_city in available_cities if
							   distances[next_city] != INFINITY_REPRESENTATION]
		if len(available_distances) == 0:
			return -1
		# Find the index of the minimum distance
		next_city_with_min_distance, distance = min(available_distances, key=lambda x: x[1])
		return next_city_with_min_distance


class InitializationMethods:
	_settings: InitializationSettingsProtocol

	def __init__(self, settings: InitializationSettingsProtocol):
		self._settings = settings

	@staticmethod
	def generate_random_valid_individual(distance_matrix: DistanceMatrix) -> IndividualProtocol:
		"""
		Generate a random valid individual by randomly selecting a city and checking if a path exists between that city
		and the previous picked city. If a path exists, add the city to the cycle. If not, pick another city.
		Assumes that there are enough valid paths.
		No backtracking is done.
		"""
		cycle_length = distance_matrix.shape[0]
		# Create a list [1, 2, 3, ..., cycle_length]
		available = list(range(cycle_length))
		cycle: List[int] = []

		# Randomly select the first element
		index = np.random.randint(0, len(available))
		city = available.pop(index)
		cycle.append(city)

		while len(available) > 0:
			# Valid next city if there is a path from the previous city that is not infinity
			valid_next_cities = [i for i in available if distance_matrix[cycle[-1], i] != INFINITY_REPRESENTATION]

			if len(valid_next_cities) == 0:
				return InitializationMethods.generate_random_valid_individual(distance_matrix)

			index = np.random.randint(0, len(valid_next_cities))
			cycle.append(valid_next_cities[index])
			available.remove(valid_next_cities[index])

		# Check that there is a path between the last and first picked city
		if distance_matrix[cycle[-1], cycle[0]] == INFINITY_REPRESENTATION:
			# If there is no path between the last and first picked city, try again
			return InitializationMethods.generate_random_valid_individual(distance_matrix)

		assert len(cycle) == cycle_length
		return Individual(np.array(cycle), distance_matrix)

	@staticmethod
	def generate_random_valid_population(size: int, distance_matrix: DistanceMatrix) -> List[
		IndividualProtocol]:
		""" Generate a population of random valid individuals. """
		individuals: List[IndividualProtocol] = []
		for _ in range(size):
			individuals.append(InitializationMethods.generate_random_valid_individual(distance_matrix))
		return individuals

	@staticmethod
	def generate_greedy_individual(distance_matrix: DistanceMatrix,
								   heuristic: InitializationHeuristic) -> IndividualProtocol:
		"""
		Generates an individual using a greedy heuristic.
		No backtracking is done, just tries again and hope that a better start_index is selected.
		:param distance_matrix: The distance matrix.
		:param heuristic: A heuristic function that takes a city index and a distance matrix and returns the next city
						  index. Assumes this will create a valid cycle.
		:return: An individual.
		"""
		cycle_length = distance_matrix.shape[0]
		available = list(range(cycle_length))
		cycle: List[int] = []

		# Randomly select the first element
		start_index = np.random.randint(0, len(available))
		cycle.append(available.pop(start_index))

		for _ in range(len(available)):  # Already added one city
			next_city = heuristic(cycle[-1], distance_matrix, available)
			if next_city == -1:
				# Just try again, no the best method but it's only for initialization
				# TODO: do with backtracking
				return InitializationMethods.generate_greedy_individual(distance_matrix, heuristic)
			cycle.append(next_city)
			available.remove(next_city)

		# Check that there is a path between the last and first picked city
		if distance_matrix[cycle[-1], cycle[0]] == INFINITY_REPRESENTATION:
			# If there is no path between the last and first picked city, try again
			return InitializationMethods.generate_greedy_individual(distance_matrix, heuristic)

		assert len(cycle) == cycle_length
		return Individual(np.array(cycle), distance_matrix)

	@staticmethod
	def generate_greedy_population(size: int, distance_matrix: DistanceMatrix,
								   heuristic: InitializationHeuristic) -> List[IndividualProtocol]:
		"""
		Generates a list of individuals using a greedy heuristic.
		No backtracking is done, just tries again and hope that a better start_index is selected.
		Assumes that not the distance matrix is not sparse (with infinite distances).
		:param size: The size of the population.
		:param distance_matrix: The distance matrix.
		:param heuristic: A heuristic function that takes a city index and a distance matrix and returns the next city
						  index. Assumes this will create a valid cycle.
		:return: The list of generated individuals.
		"""
		individuals: List[IndividualProtocol] = []
		for _ in range(size):
			individuals.append(InitializationMethods.generate_greedy_individual(distance_matrix, heuristic))
		return individuals
