import random
from warnings import deprecated

import numpy as np

from classes.Controller import Controller
from classes.Population import Population
from config.Settings import Settings
from config.custom_types import DistanceMatrix
from protocols.IndividualProtocol import IndividualProtocol
from protocols.PopulationProtocol import PopulationProtocol
from protocols.SettingsProtocol import SettingsProtocol


class EvolutionaryAlgorithm:
	settings: SettingsProtocol
	distance_matrix: DistanceMatrix
	population: PopulationProtocol

	_best_fitness: float = -1
	_best_fitness_convergence_count: int = 0
	_iteration: int = 0
	_offsprings: list[IndividualProtocol] = []
	_converged: bool
	_controller: Controller

	def __init__(self, distance_matrix: DistanceMatrix):
		self.distance_matrix = distance_matrix
		problem_size = distance_matrix.shape[0]
		self.settings = Settings(problem_size)
		self._controller = Controller(self.settings)

	def initialize_population(self) -> None:
		initial_individuals = self._controller.generate_population_method()(self.distance_matrix)
		self.population = Population(initial_individuals, self.settings.initialization.population_size,
									 self.distance_matrix)

	@property
	def converged(self) -> bool:
		self._iteration += 1
		if self._iteration >= self.settings.initialization.max_iterations:
			return True
		# Keep the best fitness count threshold high enough because there is always a chance we randomly generate a
		# better solution
		new_best_fitness = self.population.best_fitness()
		if self._best_fitness == new_best_fitness:
			self._best_fitness_convergence_count += 1
			if self._best_fitness_convergence_count >= self.settings.convergence.best_fitness_count_threshold:
				return True
		else:
			self._best_fitness = new_best_fitness
			self._best_fitness_convergence_count = 0
		return False

	@deprecated("Does not work")
	def update_fitness_sharing_proportions(self) -> None:
		self.population.update_fitness_sharing_proportions(self.settings.fitness.similarity_threshold,
														   self.settings.fitness.shape_exp)

	def select(self) -> IndividualProtocol:
		return self._controller.selection_method()(self.population.individuals)

	def recombination(self) -> None:
		self._offsprings = []
		for _ in range(self.settings.initialization.population_size):
			parent1 = self.select()
			parent2 = self.select()
			offspring1, offspring2 = self._controller.recombination_method()(parent1, parent2)
			self._offsprings.append(offspring1)
			self._offsprings.append(offspring2)

	def mutation(self):
		for individual in self._offsprings:
			if random.random() < self.settings.mutation.alpha:
				self._controller.mutation_method()(individual)
				individual.dirty = True

		# quadratic decay of the mutation probability
		self.settings.mutation.alpha = self.settings.mutation.alpha * (
					1 - (self.settings.mutation.alpha_decay_rate * self._iteration) ** 2)

	def local_optimisation(self):
		self._offsprings.sort(key=lambda x: x.fitness)  # from low to high (worst to best)
		for i in range(round((self.population.size * self.settings.local_optimisation.proportion_worst))):
			if random.random() < self.settings.local_optimisation.opt_probability:
				self._controller.local_optimisation_method()(self._offsprings[i])

	def elimination(self) -> None:
		self._controller.elimination_method()(self.population, self._offsprings)

	def insert_diversity(self):
		self._controller.insert_diversity_method()(self.population)
