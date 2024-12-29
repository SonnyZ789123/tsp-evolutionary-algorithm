import random
from typing import List
from warnings import deprecated

import numpy as np

from methods.InitializationMethods import InitializationMethods
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
		random.shuffle(leftover_merged)
		leftover = leftover_merged[:leftover_size]

		# Combine to form the next generation
		next_generation = selected_from_current + selected_from_offspring + leftover
		assert len(next_generation) == population.size
		population.individuals = next_generation

	@staticmethod
	@deprecated("Use offspring_fitness_based_with_crowding_updated instead.")
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

	@staticmethod
	def mixed_elitist_with_crowding(population: PopulationProtocol,
									offsprings: List[IndividualProtocol],
									proportion: float = 0.5, k: int = 5) -> None:
		"""
		Select the top proportion of the population, and the top proportion of the offsprings, but for every offspring
		crowding is used inside the offsprings to ensure diversity.
		:param population: The population.
		:param offsprings: The offsprings, the size has to be at least 2 * (1 - proportion) * population size.
		:param proportion: The top proportion of the seed population to keep.
		:param k: The number of individuals to consider in the k-tournament for the crowding.
		"""
		# Sort current population and offspring by fitness
		sorted_current = sorted(population.individuals, key=lambda individual: individual.fitness, reverse=True)
		sorted_offspring = sorted(offsprings, key=lambda individual: individual.fitness, reverse=True)

		selected_from_current = sorted_current[:round(population.size * proportion)]

		offsprings_size = population.size - round(population.size * proportion)
		# Crowding: fill the selected offspring but with each iteration remove a offspring that is similar to the
		# selected one
		selected_from_offspring = []
		for i in range(offsprings_size):
			current_offspring = sorted_offspring.pop(i)
			selected_from_offspring.append(current_offspring)
			closest = SelectionMethods.k_tournament(sorted_offspring, k,
													key=lambda individual: SimilarityMethods.hamming(
														current_offspring.cycle,
														individual.cycle))
			sorted_offspring.remove(closest)

		population.individuals = selected_from_current + selected_from_offspring
		assert len(population.individuals) == population.size

	@staticmethod
	def replace_worst_with_random(population: PopulationProtocol, k: float = 0.1) -> None:
		"""
		Replace the worst individuals with random individuals.
		:param population: The population.
		:param k: The worst proportion of the population to replace with random individuals.
		"""
		population.individuals.sort(key=lambda individual: individual.fitness)
		amount_to_replace = round(population.size * k)
		population.individuals = population.individuals[amount_to_replace:]
		for _ in range(amount_to_replace):
			population.individuals.append(
				InitializationMethods.generate_random_valid_individual(population.distance_matrix))
