from protocols.IndividualProtocol import IndividualProtocol


class RecombinationMethods:
	@staticmethod
	def deterministic_best_parent(parent1: IndividualProtocol, parent2: IndividualProtocol) -> IndividualProtocol:
		"""Return the parent with the best fitness."""
		return parent1 if parent1.fitness > parent2.fitness else parent2
