import random

from classes.Population import Population
from config.Settings import Settings
from config.custom_types import DistanceMatrix
from methods.EliminationMethods import EliminationMethods
from methods.LocalOptimisationMethods import LocalOptimisationMethods
from methods.NeighbourMethods import NeighbourMethods
from methods.RecombinationMethods import RecombinationMethods
from methods.SelectionMethods import SelectionMethods
from protocols.IndividualProtocol import IndividualProtocol
from protocols.PopulationProtocol import PopulationProtocol
from protocols.SettingsProtocol import SettingsProtocol


class EvolutionaryAlgorithm:
	settings: SettingsProtocol
	population: PopulationProtocol
	_best_fitness: float = -1
	_best_fitness_convergence_count: int = 0
	_iteration: int = 0
	_offsprings: list[IndividualProtocol] = []
	_converged: bool

	def __init__(self, distance_matrix: DistanceMatrix):
		problem_size = distance_matrix.shape[0]
		self.settings = Settings(problem_size)
		self.population = Population(self.settings.initialization.population_size, distance_matrix)

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

	def update_fitness_sharing_proportions(self) -> None:
		self.population.update_fitness_sharing_proportions(self.settings.fitness.similarity_threshold,
														   self.settings.fitness.shape_exp)

	def select(self) -> IndividualProtocol:
		return SelectionMethods.k_tournament(self.population.individuals, self.settings.selection.k_tournament)

	def recombination(self) -> None:
		self._offsprings = []
		for _ in range(self.settings.initialization.population_size):
			parent1 = self.select()
			parent2 = self.select()
			offspring1, offspring2 = RecombinationMethods.order_crossover(parent1, parent2)
			self._offsprings.append(offspring1)
			self._offsprings.append(offspring2)

	def mutation(self):
		for individual in self._offsprings:
			if random.random() < self.settings.mutation.alpha:
				individual.mutate()

	def local_optimisation(self):
		self._offsprings.sort(key=lambda x: x.fitness)  # from low to high (worst to best)
		for i in range(round((self.population.size * self.settings.local_optimisation.proportion_worst))):
			if random.random() < self.settings.local_optimisation.opt_probability:
				LocalOptimisationMethods.k_opt(self._offsprings[i], NeighbourMethods.swap_edges,
											   self.settings.local_optimisation.k_opt_pool_size,
											   self.settings.local_optimisation.k_opt_k)

	def elimination(self) -> None:
		EliminationMethods.mixed_elitist_with_crowding(self.population, self._offsprings,
													   self.settings.elimination.mixed_elitist_with_crowding_proportion,
													   self.settings.elimination.mixed_elitist_with_crowding_k)

	def insert_diversity(self):
		EliminationMethods.replace_worst_with_random(self.population,
													 self.settings.elimination.replace_worst_with_random_k)
