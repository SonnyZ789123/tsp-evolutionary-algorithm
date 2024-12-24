import numpy as np

from protocols.IndividualProtocol import IndividualProtocol


class MutationMethods:
	@staticmethod
	def swap_mutation(individual: IndividualProtocol) -> None:
		"""
		Apply swap mutation to the individual.
		:param individual: The individual
		"""
		# pick two random indices
		i, j = np.random.choice(len(individual.cycle), 2, replace=False)
		# swap the elements
		individual.cycle[i], individual.cycle[j] = individual.cycle[j], individual.cycle[i]