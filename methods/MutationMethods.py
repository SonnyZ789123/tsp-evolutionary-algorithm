import numpy as np

from protocols.IndividualProtocol import IndividualProtocol
from utils.cycle_utils import is_valid_cycle


class MutationMethods:
	@staticmethod
	def swap(individual: IndividualProtocol) -> None:
		"""
		Apply swap mutation to the individual.
		:param individual: The individual
		"""
		i, j = np.random.choice(len(individual.cycle), 2, replace=False)
		individual.cycle[i], individual.cycle[j] = individual.cycle[j], individual.cycle[i]

	@staticmethod
	def reverse_subtour(individual: IndividualProtocol) -> None:
		"""
		Reverses a random part of the cycle. If the resulting cycle is invalid, it is not changed.
		:param individual: The individual
		"""
		distance_matrix = individual.distance_matrix
		# list[i:j] returns a list from i to and including j-1
		# np.random.choice(cycle_length) returns a random number from 0 to size-1, but we want including cycle_length
		i, j = np.random.choice(len(individual.cycle) + 1, 2, replace=False)
		if i > j:
			i, j = j, i

		# Check if the cycle is valid
		mutated_cycle = individual.cycle.copy()
		mutated_cycle[i:j] = mutated_cycle[i:j][::-1]
		if is_valid_cycle(mutated_cycle, distance_matrix):
			individual.cycle = mutated_cycle

	@staticmethod
	def scramble(individual: IndividualProtocol) -> None:
		"""
		A random part of the cycle is selected and its elements are randomly shuffled. If the resulting cycle is invalid,
		it is not changed.
		:param individual: The individual
		"""
		distance_matrix = individual.distance_matrix
		# list[i:j] returns a list from i to and including j-1
		# np.random.choice(cycle_length) returns a random number from 0 to size-1, but we want including cycle_length
		i, j = np.random.choice(len(individual.cycle) + 1, 2, replace=False)
		if i > j:
			i, j = j, i

		# Check if the cycle is valid
		mutated_cycle = individual.cycle.copy()
		mutated_cycle[i:j] = np.random.permutation(mutated_cycle[i:j])
		if is_valid_cycle(mutated_cycle, distance_matrix):
			individual.cycle = mutated_cycle
