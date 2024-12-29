from warnings import deprecated

import numpy as np

from protocols.PopulationProtocol import PopulationProtocol


class ConvergenceMethods:
	@staticmethod
	@deprecated("Flaky convergence method")
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

	@staticmethod
	def variance_fitness(population: PopulationProtocol, threshold: float) -> bool:
		"""
		Checks if the variance of the fitness is below a certain threshold.
		:param population: The population
		:param threshold: The threshold
		:return: True if the variance of the fitness is below the threshold, False otherwise
		"""
		individuals_fitness = [individual.fitness for individual in population.individuals]
		variance = np.var(individuals_fitness)
		return bool(variance < threshold)