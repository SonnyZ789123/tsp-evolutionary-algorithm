from typing import List, Callable, Tuple

from config.custom_types import DistanceMatrix, Cycle
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


class Controller:
	settings: SettingsProtocol
	_initializationMethods: InitializationMethods
	_selectionMethods: SelectionMethods
	_recombinationMethods: RecombinationMethods
	_mutationMethods: MutationMethods
	_localOptimisationMethods: LocalOptimisationMethods
	_neighbourMethods: NeighbourMethods
	_eliminationMethods: EliminationMethods

	def __init__(self, settings: SettingsProtocol):
		self.settings = settings

		self._initializationMethods = InitializationMethods(settings.initialization)
		self._selectionMethods = SelectionMethods(settings.selection)
		self._recombinationMethods = RecombinationMethods(settings.recombination)
		self._mutationMethods = MutationMethods(settings.mutation)
		self._localOptimisationMethods = LocalOptimisationMethods(settings.local_optimisation)
		self._neighbourMethods = NeighbourMethods()
		self._eliminationMethods = EliminationMethods(settings.elimination)

	def generate_population_method(self) -> Callable[[DistanceMatrix], List[IndividualProtocol]]:
		return lambda distance_matrix: self._initializationMethods.one_greedy_nearest_neighbour_rest_random_valid(
			self.settings.initialization.population_size, distance_matrix)

	def selection_method(self) -> Callable[[List[IndividualProtocol]], IndividualProtocol]:
		return lambda individuals: self._selectionMethods.k_tournament(individuals)

	def recombination_method(self) -> Callable[
		[IndividualProtocol, IndividualProtocol], Tuple[IndividualProtocol, ...]]:
		return lambda parent1, parent2: self._recombinationMethods.order_crossover(parent1, parent2)

	def mutation_method(self) -> Callable[[IndividualProtocol], None]:
		return lambda individual: self._mutationMethods.reverse_subtour(individual)

	def local_optimisation_method(self) -> Callable[[IndividualProtocol], None]:
		return lambda offspring: self._localOptimisationMethods.k_opt(offspring, self.neighbour_method())

	def neighbour_method(self) -> Callable[[Cycle], Cycle]:
		return lambda cycle: self._neighbourMethods.swap_edges(cycle)

	def elimination_method(self) -> Callable[[PopulationProtocol, List[IndividualProtocol]], None]:
		if self.settings.problem_size < 100:
			return lambda population, offsprings: self._eliminationMethods.mixed_elitist(population, offsprings)

		if 100 <= self.settings.problem_size < 400:
			return lambda population, offsprings: self._eliminationMethods.elitist_k_tournament_keep_s_best(population,
																									   offsprings)
		if 400 <= self.settings.problem_size < 600:
			return lambda population, offsprings: self._eliminationMethods.elitist_k_tournament_keep_s_best(population,
																											offsprings)

		return lambda population, offsprings: self._eliminationMethods.elitist_k_tournament_keep_s_best(population,
																										offsprings)

	def insert_diversity_method(self) -> Callable[[PopulationProtocol], None]:
		if self.settings.problem_size < 100:
			return lambda _: None

		if 100 <= self.settings.problem_size < 400:
			return lambda _: None

		if 400 <= self.settings.problem_size < 600:
			return lambda _: None

		return lambda _: None
