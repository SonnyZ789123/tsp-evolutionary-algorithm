from typing import List

from protocols.IndividualProtocol import IndividualProtocol
from protocols.PopulationProtocol import PopulationProtocol


class EliminationMethods:
	@staticmethod
	def age_based(population: PopulationProtocol, offsprings: List[IndividualProtocol]) -> None:
		assert population.size == len(offsprings)
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

