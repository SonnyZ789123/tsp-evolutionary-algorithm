from typing import List

from protocols.IndividualProtocol import IndividualProtocol
from protocols.PopulationProtocol import PopulationProtocol


class EliminationMethods:
	@staticmethod
	def age_based(population: PopulationProtocol, offsprings: List[IndividualProtocol]) -> None:
		"""
		Only keep the offsprings.
		:param population: The population
		:param offsprings: The offsprings
		"""
		if len(offsprings) > population.size:
			offsprings.sort(key=lambda individual: individual.fitness, reverse=True)
			population.individuals = offsprings[:population.size]
		else:
			population.individuals = offsprings

	@staticmethod
	def merged_fitness_based(population: PopulationProtocol, offsprings: List[IndividualProtocol]) -> None:
		"""
		Merge the population and offsprings, and keep the best individuals.
		:param population: Current population.
		:param offsprings: List of offsprings.
		"""
		merged_population = population.individuals + offsprings
		merged_population.sort(key=lambda individual: individual.fitness, reverse=True)
		population.individuals = merged_population[:population.size]

	@staticmethod
	def mixed_elitist(population: PopulationProtocol, offsprings: List[IndividualProtocol],
					  proportion: float = 0.5) -> None:
		"""
		Select the top proportion of the population and offsprings to form the next generation.
		:param population: The population.
		:param offsprings: The offsprings.
		:param proportion: The proportion relative to the population size for the current population. So for example if
		proportion is 0.5, then half of the current population will be selected and the top of the offsprings will be
		used to fill the population.
		:return:
		"""
		# Sort current population and offspring by fitness
		sorted_current = sorted(population.individuals, key=lambda individual: individual.fitness, reverse=True)
		sorted_offspring = sorted(offsprings, key=lambda individual: individual.fitness, reverse=True)

		# Take the top individuals from both groups
		selected_from_current = sorted_current[:round(population.size * proportion)]
		selected_from_offspring = sorted_offspring[:(population.size - round(population.size * proportion))]

		# Combine to form the next generation
		next_generation = selected_from_current + selected_from_offspring
		population.individuals = next_generation[:population.size]
