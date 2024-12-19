from typing import Tuple
import numpy as np

from protocols.IndividualProtocol import IndividualProtocol
from r0829897 import Individual


class RecombinationMethods:
	@staticmethod
	def partially_mapped_crossover(parent1: IndividualProtocol, parent2: IndividualProtocol) -> Tuple[
		IndividualProtocol, IndividualProtocol]:
		"""
		Performs Partially Mapped Crossover (PMX) for two parents.
		parent1, parent2: Individual instances representing the cycles of the parents.

		Returns two offspring as numpy arrays.
		"""
		cycle1 = parent1.cycle
		cycle2 = parent2.cycle

		size = len(cycle1)
		assert size == len(cycle2), "Parents must have the same length"

		# Randomly choose two crossover points
		cut1, cut2 = sorted(np.random.choice(range(size), 2, replace=False))

		# Initialize offspring with -1 (indicating empty spots)
		offspring_cycle1 = -1 * np.ones(size, dtype=int)
		offspring_cycle2 = -1 * np.ones(size, dtype=int)

		# Copy the segment from parents to offspring
		offspring_cycle1[cut1:cut2] = cycle1[cut1:cut2]
		offspring_cycle2[cut1:cut2] = cycle2[cut1:cut2]

		# Fill the rest of the offspring ensuring valid permutations
		def fill_offspring(offspring, parent, start, end):
			for i in range(start, end):
				if parent[i] not in offspring:
					# Find the first available position
					while offspring[i] != -1:
						i = np.where(parent == offspring[i])[0][0]
					offspring[i] = parent[i]

			# Fill remaining empty spots
			for i in range(len(offspring)):
				if offspring[i] == -1:
					offspring[i] = parent[i]

		# Fill the remaining parts of the offspring
		fill_offspring(offspring_cycle1, cycle2, cut1, cut2)
		fill_offspring(offspring_cycle2, cycle1, cut1, cut2)

		offspring1 = Individual(offspring_cycle1, parent1.distance_matrix)
		offspring2 = Individual(offspring_cycle2, parent2.distance_matrix)

		return offspring1, offspring2
