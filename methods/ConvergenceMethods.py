from protocols.PopulationProtocol import PopulationProtocol


class ConvergenceMethods:
	@staticmethod
	def difference_mean_and_best_fitness(population: PopulationProtocol, threshold: float) -> bool:
		"""
		Checks if the mean fitness and the best fitness are within a certain threshold, after normalizing.
		:param population: The population
		:param threshold: The threshold between 0 and 1
		:return: True if the mean fitness and the best fitness are within the threshold, False otherwise
		"""
		mean_fitness = population.mean_fitness()
		best_fitness = population.best_fitness()

		mean_fitness_normalized = abs((best_fitness - mean_fitness) / mean_fitness)
		return mean_fitness_normalized < threshold
