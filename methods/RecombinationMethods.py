from typing import Tuple

import numpy as np

from classes.Individual import Individual
from protocols.IndividualProtocol import IndividualProtocol
from protocols.SettingsProtocol import RecombinationSettingsProtocol


class RecombinationMethods:
	_settings: RecombinationSettingsProtocol

	def __init__(self, settings: RecombinationSettingsProtocol):
		self._settings = settings

	@staticmethod
	def deterministic_best_parent(parent1: IndividualProtocol, parent2: IndividualProtocol) -> IndividualProtocol:
		"""Return the parent with the best fitness."""
		return parent1 if parent1.fitness > parent2.fitness else parent2

	@staticmethod
	def order_crossover(parent1: IndividualProtocol, parent2: IndividualProtocol) -> Tuple[
		IndividualProtocol, IndividualProtocol]:
		"""
		Performs Order Crossover (OX) for two parents.
		:param parent1: First parent individual.
		:param parent2: Second parent individual.

		:return: Tuple of two offspring Individuals.
		"""
		cycle1 = parent1.cycle
		cycle2 = parent2.cycle

		size = len(cycle1)
		assert size == len(cycle2), "Parents should have the same length"

		# Randomly select two crossover points
		cut1, cut2 = sorted(np.random.choice(range(size), 2, replace=False))

		# Initialize offspring with -1 (indicating empty spots)
		offspring_cycle1 = -1 * np.ones(size, dtype=int)
		offspring_cycle2 = -1 * np.ones(size, dtype=int)

		# Copy the segment from parents to offspring
		offspring_cycle1[cut1:cut2] = cycle1[cut1:cut2]
		offspring_cycle2[cut1:cut2] = cycle2[cut1:cut2]

		# Fill remaining positions in offspring from the other parent
		# Starting from the cut2, traverse the parent 2 and add the gene to the offspring (also starting from cut 2) if
		# it is not already present
		def fill_remaining(offspring, parent):
			offspring_index = cut2
			for i in range(cut2, cut2 + size):
				if parent[i % size] not in offspring:
					offspring[offspring_index % size] = parent[i % size]
					offspring_index += 1
				if offspring_index % size == cut1:
					break

		# Use the other parent to fill the remaining positions in the offspring
		fill_remaining(offspring_cycle1, cycle2)
		fill_remaining(offspring_cycle2, cycle1)

		# Create offspring Individuals
		offspring1 = Individual(offspring_cycle1, parent1.distance_matrix)
		offspring2 = Individual(offspring_cycle2, parent2.distance_matrix)

		return offspring1, offspring2
