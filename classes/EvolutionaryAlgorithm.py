import random
from warnings import deprecated

from classes.Population import Population
from config.Settings import Settings
from config.custom_types import DistanceMatrix
from methods.EliminationMethods import EliminationMethods
from methods.InitializationMethods import InitializationMethods
from methods.LocalOptimisationMethods import LocalOptimisationMethods
from methods.MutationMethods import MutationMethods
from methods.NeighbourMethods import NeighbourMethods
from methods.RecombinationMethods import RecombinationMethods
from methods.SelectionMethods import SelectionMethods
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

	_initializationMethods: InitializationMethods
	_selectionMethods: SelectionMethods
	_recombinationMethods: RecombinationMethods
	_mutationMethods: MutationMethods
	_localOptimisationMethods: LocalOptimisationMethods
	_eliminationMethods: EliminationMethods

	def __init__(self, distance_matrix: DistanceMatrix):
		self.distance_matrix = distance_matrix
		problem_size = distance_matrix.shape[0]
		self.settings = Settings(problem_size)

		self._initializationMethods = InitializationMethods(self.settings.initialization)
		self._selectionMethods = SelectionMethods(self.settings.selection)
		self._recombinationMethods = RecombinationMethods(self.settings.recombination)
		self._mutationMethods = MutationMethods(self.settings.mutation)
		self._localOptimisationMethods = LocalOptimisationMethods(self.settings.local_optimisation)
		self._eliminationMethods = EliminationMethods(self.settings.elimination)

	def initialize_population(self) -> None:
		initial_individuals = self._initializationMethods.one_greedy_nearest_neighbour_rest_random_valid(
			self.settings.initialization.population_size,
			self.distance_matrix)
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
		return self._selectionMethods.k_tournament(self.population.individuals)

	def recombination(self) -> None:
		self._offsprings = []
		for _ in range(self.settings.initialization.population_size):
			parent1 = self.select()
			parent2 = self.select()
			offspring1, offspring2 = self._recombinationMethods.order_crossover(parent1, parent2)
			self._offsprings.append(offspring1)
			self._offsprings.append(offspring2)

	def mutation(self):
		for individual in self._offsprings:
			if random.random() < self.settings.mutation.alpha:
				self._mutationMethods.reverse_subtour(individual)
				individual.dirty = True

	def local_optimisation(self):
		self._offsprings.sort(key=lambda x: x.fitness)  # from low to high (worst to best)
		for i in range(round((self.population.size * self.settings.local_optimisation.proportion_worst))):
			if random.random() < self.settings.local_optimisation.opt_probability:
				self._localOptimisationMethods.k_opt(self._offsprings[i], NeighbourMethods.swap_edges,
													 self.settings.local_optimisation.k_opt_pool_size,
													 self.settings.local_optimisation.k_opt_k)

	def elimination(self) -> None:
		self._eliminationMethods.mixed_elitist_with_crowding(self.population, self._offsprings)

	def insert_diversity(self):
		self._eliminationMethods.replace_worst_with_random(self.population)
