from protocols.IndividualProtocol import IndividualProtocol


class FitnessMethods:
	@staticmethod
	def negative_of_length(individual: IndividualProtocol) -> float:
		"""
		Calculate the fitness of the individual as the negative of the length of the cycle.
		:param individual: The individual
		"""
		distance_matrix = individual.distance_matrix
		cycle = individual.cycle
		length = 0

		for i in range(len(cycle)):
			length += distance_matrix.value[cycle[i], cycle[(i + 1) % len(cycle)]]
		return -length