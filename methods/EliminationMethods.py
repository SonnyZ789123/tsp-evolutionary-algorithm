from typing import List

import numpy as np

from methods.SelectionMethods import SelectionMethods
from methods.SimilarityMethods import SimilarityMethods
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

	@staticmethod
	def mixed_elitist_rest_merged_random(population: PopulationProtocol, offsprings: List[IndividualProtocol],
										 proportion_size: float = 0.5,
										 mixed_elitist_proportion: float = 0.5) -> None:
		"""
		Select the top proportion of the population and offsprings to form the next generation. The rest of the population
		is filled with random individuals chosen from mergen the leftover population and offsprings.
		:param population: The population.
		:param offsprings: The offsprings.
		:param proportion_size: The proportion of the population size that is used for the population and offsprings.
		:param mixed_elitist_proportion: The proportion of the subpopulation that has been selected for the mixed elitist
		strategy.
		"""
		size = round(population.size * proportion_size)
		leftover_size = population.size - size

		# Sort current population and offspring by fitness
		sorted_current = sorted(population.individuals, key=lambda individual: individual.fitness, reverse=True)
		sorted_offspring = sorted(offsprings, key=lambda individual: individual.fitness, reverse=True)

		# Take the top individuals from both groups
		selected_from_current = sorted_current[:round(size * mixed_elitist_proportion)]
		leftover_from_current = sorted_current[round(size * mixed_elitist_proportion):]
		selected_from_offspring = sorted_offspring[:(size - round(size * mixed_elitist_proportion))]
		leftover_from_offspring = sorted_offspring[(size - round(size * mixed_elitist_proportion)):]

		leftover_merged = leftover_from_current + leftover_from_offspring
		np.random.shuffle(leftover_merged)
		leftover = leftover_merged[:leftover_size]

		# Combine to form the next generation
		next_generation = selected_from_current + selected_from_offspring + leftover
		assert len(next_generation) == population.size
		population.individuals = next_generation

	@staticmethod
	def offspring_fitness_based_with_crowding(population: PopulationProtocol, offsprings: List[IndividualProtocol],
											  proportion: float = 0.5, k: int = 5) -> None:
		"""
		Select the top proportion of the offsprings and for every offspring select the closest individual in the
		population to replace.
		:param population: The population.
		:param offsprings: The offsprings
		:param proportion: The proportion relative to the population size for the current population.
		:param k: The number of individuals to consider in the k-tournament for the crowding.
		"""
		size = round(population.size * proportion)
		sorted_offsprings = sorted(offsprings, key=lambda individual: individual.fitness, reverse=True)

		offsprings_selected = sorted_offsprings[:size]
		for offspring in offsprings_selected:
			closest = SelectionMethods.k_tournament(population.individuals, k,
													key=lambda individual: SimilarityMethods.hamming(offspring.cycle,
																									 individual.cycle))
			population.individuals.remove(closest)
			population.individuals.append(offspring)
