from typing import List

import numpy as np

from protocols.DistanceMatrixProtocol import DistanceMatrixProtocol
from protocols.IndividualProtocol import IndividualProtocol
from classes.Individual import Individual


class InitializationMethods:
	@staticmethod
	def generate_random_valid_individual(distance_matrix: DistanceMatrixProtocol) -> IndividualProtocol:
		"""
		Generate a random valid individual by randomly selecting a city and checking if a path exists between that city
		and the previous picked city. If a path exists, add the city to the cycle. If not, pick another city.
		Assumes that there are enough valid paths.
		No backtracking is done.
		"""
		cycle_length = distance_matrix.value.shape[0]
		# Create a list [1, 2, 3, ..., cycle_length]
		available = list(range(cycle_length))
		cycle: List[int] = []

		# Randomly select the first element
		index = np.random.randint(0, len(available))
		city = available.pop(index)
		cycle.append(city)

		while len(available) > 0:
			# Valid next city if there is a path from the previous city that is not infinity
			valid_next_cities = [i for i in available if distance_matrix.value[cycle[-1], i] != -1]

			if len(valid_next_cities) == 0:
				return InitializationMethods.generate_random_valid_individual(distance_matrix)

			index = np.random.randint(0, len(valid_next_cities))
			cycle.append(valid_next_cities[index])
			available.remove(valid_next_cities[index])

		# Check that there is a path between the last and first picked city
		if distance_matrix.value[cycle[-1], cycle[0]] != -1:
			assert len(cycle) == cycle_length
			return Individual(np.array(cycle), distance_matrix)

		# If there is no path between the last and first picked city, try again
		return InitializationMethods.generate_random_valid_individual(distance_matrix)

	@staticmethod
	def generate_random_valid_population(size: int, distance_matrix: DistanceMatrixProtocol) -> List[
		IndividualProtocol]:
		individuals: List[IndividualProtocol] = []
		for _ in range(size):
			individuals.append(InitializationMethods.generate_random_valid_individual(distance_matrix))
		return individuals
