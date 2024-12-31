from typing import Callable, List, Protocol, Optional, Tuple

import numpy as np
import random
from warnings import deprecated

from numpy.typing import NDArray

import Reporter

# CONFIG ###############################################################################################################

DistanceMatrix = NDArray[float]  # A 2D numpy array
Cycle = NDArray[np.int64]  # A 1D numpy array
InitializationHeuristic = Callable[[int, DistanceMatrix, List[int]], int]
INFINITY_REPRESENTATION = 1e+10

########################################################################################################################

# UTILS ################################################################################################################

def is_valid_cycle(cycle: Cycle, distance_matrix: DistanceMatrix) -> bool:
	"""
	Check if the cycle is a valid cycle, i.e. the same dimension as the rows/columns distance_matrix, all cities are
	visited exactly once, and there is a non-infinity path between each city in the cycle.
	:param cycle: The cycle
	:param distance_matrix: The distance matrix
	:return: True if the cycle is valid, False otherwise
	"""
	cycle_length = len(cycle)

	if cycle_length != distance_matrix.shape[0]:
		return False

	available = list(range(cycle_length))
	for i in range(cycle_length):
		if distance_matrix[cycle[i], cycle[(i + 1) % cycle_length]] == INFINITY_REPRESENTATION:
			return False
		if cycle[i] not in available:
			return False
		available.remove(int(cycle[i]))
	return True


def get_cycle_length(cycle: Cycle, distance_matrix: DistanceMatrix) -> float:
	length = 0
	cycle_length = len(cycle)

	for i in range(len(cycle)):
		length += distance_matrix[cycle[i], cycle[(i + 1) % cycle_length]]

	return length


def get_cycle_distances(cycle: Cycle, distance_matrix: DistanceMatrix) -> list[float]:
	distances = []
	cycle_length = len(cycle)

	for i in range(len(cycle)):
		distances.append(round(float(distance_matrix[cycle[i], cycle[(i + 1) % cycle_length]]), 2))

	return distances

def normalize_list(values: List[float], bottom: int = 0, top: int = 100) -> List[float]:
	min_val = min(values)
	max_val = max(values)

	# Ensure the range is non-zero to avoid division by zero
	range_val = max_val - min_val
	if range_val == 0:
		return [100.0 for _ in values]  # All values are the same

	# Normalize values to [0, 1] and then scale to [bottom, top]
	normalized_range = top - bottom
	normalized = [((x - min_val) / range_val * normalized_range) + bottom for x in values]
	return normalized

########################################################################################################################

# PROTOCOLS ############################################################################################################

class IndividualProtocol(Protocol):
	distance_matrix: DistanceMatrix
	""" 
	The distance matrix representing the distances between the cities. The length of the rows should be equal 
	to the length of the columns, and the length should be equal to the length of the cycle. 
	"""
	fitness_sharing: float
	dirty: bool

	@property
	def fitness(self) -> float:
		""" The fitness of the individual, which can be negative. """
		...

	@property
	def cycle(self) -> Cycle:
		...

	@cycle.setter
	def cycle(self, cycle: Cycle) -> None:
		...

	def get_fitness_internal(self) -> float:
		""" The unmodified fitness of the individual. """
		...


class PopulationProtocol(Protocol):
	size: int
	distance_matrix: DistanceMatrix
	individuals: list[IndividualProtocol]

	def mean_fitness(self) -> float:
		...

	def best_fitness(self) -> float:
		...

	def best_individual(self) -> IndividualProtocol:
		...

	def variance_fitness(self) -> float:
		...

	def valid_invalid_individual_proportion(self) -> tuple[int, int]:
		...

	def update_fitness_sharing_proportions(self, similarity_threshold: Optional[float],
										   shape_exp: Optional[float]) -> None:
		...


class EvolutionaryAlgorithmProtocol(Protocol):
	population: PopulationProtocol

	@property
	def converged(self) -> bool:
		...

	def initialize_population(self) -> None:
		...

	def update_fitness_sharing_proportions(self) -> None:
		...

	def select(self) -> IndividualProtocol:
		...

	def mutation(self) -> None:
		...

	def recombination(self) -> None:
		...

	def elimination(self) -> None:
		...

	def insert_diversity(self) -> None:
		...

	def local_optimisation(self) -> None:
		...


class FitnessSettingsProtocol(Protocol):
	similarity_threshold: float
	""" The threshold for similarity between cycles, between 0 and 1. """
	shape_exp: float
	""" The exponent for the shape of the fitness sharing function, between 0.25 and 4 """


class InitializationSettingsProtocol(Protocol):
	population_size: int
	""" The size of the population, should be a positive even integer. """
	max_iterations: int


class ConvergenceSettingsProtocol(Protocol):
	# diff_mean_best_threshold: float
	# """ The threshold for difference between mean and best fitness, between 0 and 1. """
	var_fitness_threshold: float
	""" The threshold for variance of fitness, between 0 and 1. """
	best_fitness_count_threshold: int
	""" The amount of iterations the best fitness can stay the same before the algorithm converges. """


class SelectionSettingsProtocol(Protocol):
	k_tournament_k: int
	""" The number of individuals in the tournament. """


class MutationSettingsProtocol(Protocol):
	alpha: float
	""" The probability of mutation. """
	alpha_decay_rate: float
	""" The decay rate of the mutation probability. """


class RecombinationSettingsProtocol(Protocol):
	...


class LocalOptimisationSettingsProtocol(Protocol):
	proportion_worst: float = 0.5
	""" The proportion of the worst individuals to consider for local optimisation. """
	opt_probability: float = 0.2
	""" The probability of local optimisation. """
	k_opt_branch_size: int
	""" The amount of neighbours to generate. """
	k_opt_k: int
	""" The value of k for k-opt, the depth of the search tree. """


class EliminationSettingsProtocol(Protocol):
	mixed_elitism_proportion: float
	""" The proportion of the population to keep in the next generation, between 0 and 1. """
	mixed_elitism_rest_merged_random_mixed_elitist_proportion: float
	""" The proportion of the subpopulation to keep in the next generation, between 0 and 1. """
	mixed_elitism_rest_merged_random_proportion_size: float
	""" The proportion of the population to use for mixed elitism, between 0 and 1. """
	offspring_fitness_based_with_crowding_proportion: float
	""" The proportion of the population to use for offspring fitness based with crowding, between 0 and 1. """
	offspring_fitness_based_with_crowding_k: int
	""" The number of individuals to consider in the k-tournament for the crowding. """
	mixed_elitist_with_crowding_proportion: float
	""" The proportion of the population to use for mixed elitist with crowding, between 0 and 1. """
	mixed_elitist_with_crowding_k: int
	""" The number of individuals to consider in the k-tournament for the crowding. """
	replace_worst_with_random_k: float
	""" The worst proportion of the population to replace with random individuals. """
	elitist_k_tournament_k: int
	""" The number of individuals to consider in the k-tournament for elitism. """
	elitist_k_tournament_keep_s_best_k: int = 3
	""" The number of individuals to keep from the k-tournament for elitism. """
	elitist_k_tournament_keep_s_best_s: int = 5
	""" The number of best individuals to keep. """


class SettingsProtocol(Protocol):
	problem_size: int
	fitness: FitnessSettingsProtocol
	initialization: InitializationSettingsProtocol
	convergence: ConvergenceSettingsProtocol
	selection: SelectionSettingsProtocol
	mutation: MutationSettingsProtocol
	recombination: RecombinationSettingsProtocol
	local_optimisation: LocalOptimisationSettingsProtocol
	elimination: EliminationSettingsProtocol


########################################################################################################################


# METHODS ##############################################################################################################

class ConvergenceMethods:
	_settings: ConvergenceSettingsProtocol

	def __init__(self, settings: ConvergenceSettingsProtocol):
		self._settings = settings

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

	def variance_fitness(self, population: PopulationProtocol) -> bool:
		"""
		Checks if the variance of the fitness is below a certain threshold.
		:param population: The population
		:return: True if the variance of the fitness is below the threshold, False otherwise
		"""
		individuals_fitness = [individual.fitness for individual in population.individuals]
		variance = np.var(individuals_fitness)
		return bool(variance < self._settings.var_fitness_threshold)


class EliminationMethods:
	_settings: EliminationSettingsProtocol

	def __init__(self, settings: EliminationSettingsProtocol):
		self._settings = settings

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

	def mixed_elitist(self, population: PopulationProtocol, offsprings: List[IndividualProtocol]) -> None:
		"""
		Select the top proportion of the population and offsprings to form the next generation.
		:param population: The population.
		:param offsprings: The offsprings.
		"""
		# Sort current population and offspring by fitness
		sorted_current = sorted(population.individuals, key=lambda individual: individual.fitness, reverse=True)
		sorted_offspring = sorted(offsprings, key=lambda individual: individual.fitness, reverse=True)

		# Take the top individuals from both groups
		selected_from_current = sorted_current[:round(population.size * self._settings.mixed_elitism_proportion)]
		selected_from_offspring = sorted_offspring[
								  :(population.size - round(population.size * self._settings.mixed_elitism_proportion))]

		# Combine to form the next generation
		next_generation = selected_from_current + selected_from_offspring
		population.individuals = next_generation[:population.size]

	def mixed_elitist_rest_merged_random(self, population: PopulationProtocol,
										 offsprings: List[IndividualProtocol]) -> None:
		"""
		Select the top proportion of the population and offsprings to form the next generation. The rest of the population
		is filled with random individuals chosen from mergen the leftover population and offsprings.
		:param population: The population.
		:param offsprings: The offsprings.
		strategy.
		"""
		size = round(population.size * self._settings.mixed_elitism_rest_merged_random_proportion_size)
		leftover_size = population.size - size

		# Sort current population and offspring by fitness
		sorted_current = sorted(population.individuals, key=lambda individual: individual.fitness, reverse=True)
		sorted_offspring = sorted(offsprings, key=lambda individual: individual.fitness, reverse=True)

		# Take the top individuals from both groups
		selected_from_current = sorted_current[
								:round(size * self._settings.mixed_elitism_rest_merged_random_mixed_elitist_proportion)]
		leftover_from_current = sorted_current[
								round(size * self._settings.mixed_elitism_rest_merged_random_mixed_elitist_proportion):]
		selected_from_offspring = sorted_offspring[:(
				size - round(size * self._settings.mixed_elitism_rest_merged_random_mixed_elitist_proportion))]
		leftover_from_offspring = sorted_offspring[(size - round(
			size * self._settings.mixed_elitism_rest_merged_random_mixed_elitist_proportion)):]

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
			closest = SelectionMethods.k_tournament_static(population.individuals, k,
														   key=lambda individual: SimilarityMethods.hamming(
															   offspring.cycle,
															   individual.cycle))
			population.individuals.remove(closest)
			population.individuals.append(offspring)

	def mixed_elitist_with_crowding(self, population: PopulationProtocol, offsprings: List[IndividualProtocol]) -> None:
		"""
		Select the top proportion of the population, and the top proportion of the offsprings, but for every offspring
		crowding is used inside the offsprings to ensure diversity.
		:param population: The population.
		:param offsprings: The offsprings, the size has to be at least 2 * (1 - proportion) * population size.
		"""
		# Sort current population and offspring by fitness
		sorted_current = sorted(population.individuals, key=lambda individual: individual.fitness, reverse=True)
		sorted_offspring = sorted(offsprings, key=lambda individual: individual.fitness, reverse=True)

		selected_from_current = sorted_current[
								:round(population.size * self._settings.mixed_elitist_with_crowding_proportion)]

		offsprings_size = population.size - round(
			population.size * self._settings.mixed_elitist_with_crowding_proportion)
		# Crowding: fill the selected offspring but with each iteration remove an offspring that is similar to the
		# selected one
		selected_from_offspring = []
		for i in range(offsprings_size):
			current_offspring = sorted_offspring.pop(i)
			selected_from_offspring.append(current_offspring)
			closest = SelectionMethods.k_tournament_static(sorted_offspring,
														   self._settings.mixed_elitist_with_crowding_k,
														   key=lambda individual: SimilarityMethods.hamming(
															   current_offspring.cycle,
															   individual.cycle))
			sorted_offspring.remove(closest)

		population.individuals = selected_from_current + selected_from_offspring
		assert len(population.individuals) == population.size

	def replace_worst_with_random(self, population: PopulationProtocol) -> None:
		"""
		Replace the worst individuals with random individuals.
		:param population: The population.
		"""
		population.individuals.sort(key=lambda individual: individual.fitness)
		amount_to_replace = round(population.size * self._settings.replace_worst_with_random_k)
		population.individuals = population.individuals[amount_to_replace:]
		for _ in range(amount_to_replace):
			population.individuals.append(
				InitializationMethods.generate_random_valid_individual(population.distance_matrix))

	def elitist_k_tournament(self, population: PopulationProtocol, offsprings: List[IndividualProtocol]) -> None:
		"""
		Choose a new population based on k-tournament selection.
		:param population: The population.
		:param offsprings: The offsprings.
		"""
		merged_population = population.individuals + offsprings
		new_generation = []
		for _ in range(population.size):
			selected = SelectionMethods.k_tournament_static(merged_population, self._settings.elitist_k_tournament_k)
			new_generation.append(selected)
			merged_population.remove(selected)

		assert len(new_generation) == population.size
		population.individuals = new_generation

	def elitist_k_tournament_keep_s_best(self, population: PopulationProtocol,
										 offsprings: List[IndividualProtocol]) -> None:
		"""
		Choose a new population based on k-tournament selection.
		:param population: The population.
		:param offsprings: The offsprings.
		"""
		merged_population = population.individuals + offsprings
		merged_population.sort(key=lambda individual: individual.fitness, reverse=True)
		new_generation = merged_population[:self._settings.elitist_k_tournament_keep_s_best_s]
		merged_population = merged_population[self._settings.elitist_k_tournament_keep_s_best_s:]
		for _ in range(population.size - self._settings.elitist_k_tournament_keep_s_best_s):
			selected = SelectionMethods.k_tournament_static(merged_population,
															self._settings.elitist_k_tournament_keep_s_best_k)
			new_generation.append(selected)
			merged_population.remove(selected)

		assert len(new_generation) == population.size
		population.individuals = new_generation


class FitnessMethods:
	_settings: FitnessSettingsProtocol

	def __init__(self, settings: FitnessSettingsProtocol):
		self._settings = settings

	@staticmethod
	def negative_of_length(individual: IndividualProtocol) -> float:
		"""
		Calculate the fitness of the individual as the negative of the length of the cycle.
		:param individual: The individual
		"""
		return -get_cycle_length(individual.cycle, individual.distance_matrix)


class Heuristics:
	"""
	All methods should be of type InitializationHeuristic.
	"""

	@staticmethod
	def nearest_neighbour(city: int, distance_matrix: DistanceMatrix, available_cities: List[int]) -> int:
		"""
		Heuristic that selects the nearest neighbour to the given city.
		:return: The index of the nearest neighbour, or -1 if there are no available cities.
		"""
		distances: NDArray[float] = distance_matrix[city]
		# Get the indices of the available cities
		available_distances = [(next_city, distances[next_city]) for next_city in available_cities if
							   distances[next_city] != INFINITY_REPRESENTATION]
		if len(available_distances) == 0:
			return -1
		# Find the index of the minimum distance
		next_city_with_min_distance, distance = min(available_distances, key=lambda x: x[1])
		return next_city_with_min_distance


class InitializationMethods:
	_settings: InitializationSettingsProtocol

	def __init__(self, settings: InitializationSettingsProtocol):
		self._settings = settings

	@staticmethod
	def generate_random_valid_individual(distance_matrix: DistanceMatrix) -> IndividualProtocol:
		"""
		Generate a random valid individual by randomly selecting a city and checking if a path exists between that city
		and the previous picked city. If a path exists, add the city to the cycle. If not, pick another city.
		Assumes that there are enough valid paths.
		No backtracking is done.
		"""
		cycle_length = distance_matrix.shape[0]
		# Create a list [1, 2, 3, ..., cycle_length]
		available = list(range(cycle_length))
		cycle: List[int] = []

		# Randomly select the first element
		index = np.random.randint(0, len(available))
		city = available.pop(index)
		cycle.append(city)

		while len(available) > 0:
			# Valid next city if there is a path from the previous city that is not infinity
			valid_next_cities = [i for i in available if distance_matrix[cycle[-1], i] != INFINITY_REPRESENTATION]

			if len(valid_next_cities) == 0:
				return InitializationMethods.generate_random_valid_individual(distance_matrix)

			index = np.random.randint(0, len(valid_next_cities))
			cycle.append(valid_next_cities[index])
			available.remove(valid_next_cities[index])

		# Check that there is a path between the last and first picked city
		if distance_matrix[cycle[-1], cycle[0]] == INFINITY_REPRESENTATION:
			# If there is no path between the last and first picked city, try again
			return InitializationMethods.generate_random_valid_individual(distance_matrix)

		assert len(cycle) == cycle_length
		return Individual(np.array(cycle), distance_matrix)

	@staticmethod
	def generate_random_valid_population(size: int, distance_matrix: DistanceMatrix) -> List[
		IndividualProtocol]:
		""" Generate a population of random valid individuals. """
		individuals: List[IndividualProtocol] = []
		for _ in range(size):
			individuals.append(InitializationMethods.generate_random_valid_individual(distance_matrix))
		return individuals

	@staticmethod
	def generate_greedy_individual(distance_matrix: DistanceMatrix,
								   heuristic: InitializationHeuristic) -> IndividualProtocol:
		"""
		Generates an individual using a greedy heuristic.
		No backtracking is done, just tries again and hope that a better start_index is selected.
		:param distance_matrix: The distance matrix.
		:param heuristic: A heuristic function that takes a city index and a distance matrix and returns the next city
						  index. Assumes this will create a valid cycle.
		:return: An individual.
		"""
		cycle_length = distance_matrix.shape[0]
		available = list(range(cycle_length))
		cycle: List[int] = []

		# Randomly select the first element
		start_index = np.random.randint(0, len(available))
		cycle.append(available.pop(start_index))

		for _ in range(len(available)):  # Already added one city
			next_city = heuristic(cycle[-1], distance_matrix, available)
			if next_city == -1:
				# Just try again, no the best method, but it's only for initialization
				return InitializationMethods.generate_greedy_individual(distance_matrix, heuristic)
			cycle.append(next_city)
			available.remove(next_city)

		# Check that there is a path between the last and first picked city
		if distance_matrix[cycle[-1], cycle[0]] == INFINITY_REPRESENTATION:
			# If there is no path between the last and first picked city, try again
			return InitializationMethods.generate_greedy_individual(distance_matrix, heuristic)

		assert len(cycle) == cycle_length
		return Individual(np.array(cycle), distance_matrix)

	@staticmethod
	def generate_greedy_population(size: int, distance_matrix: DistanceMatrix,
								   heuristic: InitializationHeuristic) -> List[IndividualProtocol]:
		"""
		Generates a list of individuals using a greedy heuristic.
		No backtracking is done, just tries again and hope that a better start_index is selected.
		Assumes that not the distance matrix is not sparse (with infinite distances).
		:param size: The size of the population.
		:param distance_matrix: The distance matrix.
		:param heuristic: A heuristic function that takes a city index and a distance matrix and returns the next city
						  index. Assumes this will create a valid cycle.
		:return: The list of generated individuals.
		"""
		individuals: List[IndividualProtocol] = []
		for _ in range(size):
			individuals.append(InitializationMethods.generate_greedy_individual(distance_matrix, heuristic))
		return individuals

	@staticmethod
	def one_greedy_nearest_neighbour_rest_random_valid(size: int, distance_matrix: DistanceMatrix) -> List[
		IndividualProtocol]:
		greedy_individual = InitializationMethods.generate_greedy_individual(distance_matrix,
																			 Heuristics.nearest_neighbour)
		random_individuals = InitializationMethods.generate_random_valid_population(size - 1, distance_matrix)
		return [greedy_individual] + random_individuals


class LocalOptimisationMethods:
	_settings: LocalOptimisationSettingsProtocol

	def __init__(self, settings: LocalOptimisationSettingsProtocol):
		self._settings = settings

	@staticmethod
	def _generate_neighbours(cycle: Cycle, neighbour_method: Callable[[Cycle], Cycle], branch_size: int, k: int) -> \
			List[
				Cycle]:
		if k == 0:
			return [cycle]

		neighbours = []
		for _ in range(branch_size):
			neighbour = neighbour_method(cycle)
			neighbours.extend(
				LocalOptimisationMethods._generate_neighbours(neighbour, neighbour_method, branch_size, k - 1))
		return neighbours

	def k_opt(self, individual: IndividualProtocol, neighbour_method: Callable[[Cycle], Cycle]) -> None:
		"""
		Apply k-opt local search to the individual.
		:param neighbour_method: The method to generate a neighbour
		:param individual: The individual
		"""
		neighbours = LocalOptimisationMethods._generate_neighbours(individual.cycle, neighbour_method,
																   self._settings.k_opt_branch_size,
																   self._settings.k_opt_k)
		neighbour_individuals = [Individual(cycle, individual.distance_matrix) for cycle in neighbours]
		best_neighbour = max(neighbour_individuals, key=lambda neighbour: neighbour.fitness)

		# use without fitness sharing because neighbours are not in the population
		if best_neighbour.fitness > individual.get_fitness_internal():
			individual.cycle = best_neighbour.cycle


class MutationMethods:
	_settings: MutationSettingsProtocol

	def __init__(self, settings: MutationSettingsProtocol):
		self._settings = settings

	@staticmethod
	def swap(individual: IndividualProtocol) -> None:
		"""
		Apply swap mutation to the individual.
		:param individual: The individual
		"""
		i, j = np.random.choice(len(individual.cycle), 2, replace=False)
		individual.cycle[i], individual.cycle[j] = individual.cycle[j], individual.cycle[i]

	@staticmethod
	def reverse_subtour(individual: IndividualProtocol) -> None:
		"""
		Reverses a random part of the cycle. If the resulting cycle is invalid, it is not changed.
		:param individual: The individual
		"""
		distance_matrix = individual.distance_matrix
		# list[i:j] returns a list from i to and including j-1
		# np.random.choice(cycle_length) returns a random number from 0 to size-1, but we want including cycle_length
		i, j = np.random.choice(len(individual.cycle) + 1, 2, replace=False)
		if i > j:
			i, j = j, i

		# Check if the cycle is valid
		mutated_cycle = individual.cycle.copy()
		mutated_cycle[i:j] = mutated_cycle[i:j][::-1]
		if is_valid_cycle(mutated_cycle, distance_matrix):
			individual.cycle = mutated_cycle

	@staticmethod
	def scramble(individual: IndividualProtocol) -> None:
		"""
		A random part of the cycle is selected and its elements are randomly shuffled. If the resulting cycle is invalid,
		it is not changed.
		:param individual: The individual
		"""
		distance_matrix = individual.distance_matrix
		# list[i:j] returns a list from i to and including j-1
		# np.random.choice(cycle_length) returns a random number from 0 to size-1, but we want including cycle_length
		i, j = np.random.choice(len(individual.cycle) + 1, 2, replace=False)
		if i > j:
			i, j = j, i

		# Check if the cycle is valid
		mutated_cycle = individual.cycle.copy()
		mutated_cycle[i:j] = np.random.permutation(mutated_cycle[i:j])
		if is_valid_cycle(mutated_cycle, distance_matrix):
			individual.cycle = mutated_cycle


class NeighbourMethods:
	@staticmethod
	def swap_edges(cycle: Cycle) -> Cycle:
		"""Swap two edges in the cycle of the individual."""
		# Select two random edges
		cycle_length = len(cycle)
		# from the slides [x y z a b c d], they picked (y z) and (c d) as edges to swap, and they did it by swapping the
		# elements z and c, so that the cycle becomes [x y c a b z d]
		# so just pick 2 random indices and swap the elements at those indices
		z_index, c_index = np.random.choice(range(cycle_length), 2, replace=False)
		neighbour_cycle = np.copy(cycle)
		neighbour_cycle[z_index], neighbour_cycle[c_index] = neighbour_cycle[c_index], neighbour_cycle[z_index]
		return neighbour_cycle


class RecombinationMethods:
	_settings: RecombinationSettingsProtocol

	def __init__(self, settings: RecombinationSettingsProtocol):
		self._settings = settings

	@staticmethod
	def deterministic_best_parent(parent1: IndividualProtocol, parent2: IndividualProtocol) -> IndividualProtocol:
		"""Return the parent with the best fitness."""
		return parent1 if parent1.fitness > parent2.fitness else parent2

	@staticmethod
	def order_crossover(parent1: IndividualProtocol, parent2: IndividualProtocol) -> Tuple[
		IndividualProtocol, IndividualProtocol]:
		"""
		Performs Order Crossover (OX) for two parents.
		:param parent1: First parent individual.
		:param parent2: Second parent individual.

		:return: Tuple of two offspring Individuals.
		"""
		cycle1 = parent1.cycle
		cycle2 = parent2.cycle

		size = len(cycle1)
		assert size == len(cycle2), "Parents should have the same length"

		# Randomly select two crossover points
		cut1, cut2 = sorted(np.random.choice(range(size), 2, replace=False))

		# Initialize offspring with -1 (indicating empty spots)
		offspring_cycle1 = -1 * np.ones(size, dtype=int)
		offspring_cycle2 = -1 * np.ones(size, dtype=int)

		# Copy the segment from parents to offspring
		offspring_cycle1[cut1:cut2] = cycle1[cut1:cut2]
		offspring_cycle2[cut1:cut2] = cycle2[cut1:cut2]

		# Fill remaining positions in offspring from the other parent
		# Starting from the cut2, traverse the parent 2 and add the gene to the offspring (also starting from cut 2) if
		# it is not already present
		def fill_remaining(offspring, parent):
			offspring_index = cut2
			for i in range(cut2, cut2 + size):
				if parent[i % size] not in offspring:
					offspring[offspring_index % size] = parent[i % size]
					offspring_index += 1
				if offspring_index % size == cut1:
					break

		# Use the other parent to fill the remaining positions in the offspring
		fill_remaining(offspring_cycle1, cycle2)
		fill_remaining(offspring_cycle2, cycle1)

		# Create offspring Individuals
		offspring1 = Individual(offspring_cycle1, parent1.distance_matrix)
		offspring2 = Individual(offspring_cycle2, parent2.distance_matrix)

		return offspring1, offspring2


class SelectionMethods:
	_settings: SelectionSettingsProtocol

	def __init__(self, settings: SelectionSettingsProtocol):
		self._settings = settings

	def k_tournament(self, individuals: List[IndividualProtocol],
					 key: Callable[[IndividualProtocol], float | int] = lambda x: x.fitness) -> IndividualProtocol:
		selected_indexes = np.random.choice(len(individuals), self._settings.k_tournament_k, replace=False)
		selected = [individuals[i] for i in selected_indexes]
		return max(selected, key=key)

	@staticmethod
	def k_tournament_static(individuals: List[IndividualProtocol], k: int,
							key: Callable[[IndividualProtocol], float | int] = lambda
									x: x.fitness) -> IndividualProtocol:
		selected_indexes = np.random.choice(len(individuals), k, replace=False)
		selected = [individuals[i] for i in selected_indexes]
		return max(selected, key=key)


class SimilarityMethods:
	@staticmethod
	def hamming(cycle1: Cycle, cycle2: Cycle) -> float:
		"""
		Calculate the Hamming distance as proportion between two cycles, after aligning the second cycle with the first element of the
		first cycle.
		:param cycle1: First cycle.
		:param cycle2: Second cycle.
		:return: Hamming distance between the two cycles, between 0 and 1.
		"""
		cycle_length = len(cycle1)
		assert cycle_length == len(cycle2), "Cycles should have the same length"
		start_index = np.where(cycle2 == cycle1[0])[0][0]
		cycle2 = np.roll(cycle2, -start_index)
		hamming = np.count_nonzero(cycle1 == cycle2)
		return hamming / cycle_length

	@staticmethod
	def cycle_subtour_linear_streak(cycle1: Cycle, cycle2: Cycle) -> int:
		"""
		Calculate the cycle subtour similarity with a linear streak between two cycles by actively looking for pieces of
		the cycle that are the same, and adding linear growing rewards to the similarity of long sub tours.
		:param cycle1: First cycle.
		:param cycle2: Second cycle.
		:return: Similarity between the two cycles, is a number between 0 and 1.
		"""
		cycle_length = len(cycle1)
		assert cycle_length == len(cycle2), "Cycles should have the same length"

		# The whool cycle is the same
		max_similarity = cycle_length / 2 * (cycle_length + 1)  # equals sum(range(1, cycle_length + 1))
		min_similarity = cycle_length

		similarity = 0
		# Using a streak, so that the similarity is weighted by the length of the streak.
		# So cycles with the same long subtour will have a higher similarity than cycles with many shorter sub tours.
		streak = 1
		i = 0

		# Take into account if the first element is part of a sub tour but not the first element of the sub tour.
		# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
		# [1, 2, 5, 6, 8, 7, 3, 4, 9, 0]
		# 0 is part of a sub tour, but not the first element of the sub tour, so it will think that only (0 1 2) is the
		# sub tour while it should be (9 0 1 2)
		city_i = cycle1[i]
		j = np.where(cycle2 == city_i)[0][0]

		# do the first time in reverse, so that the streak is correct, and we are sure we have the full first sub tour
		k = cycle_length - 1
		l = j - 1
		# but don't start on the first element, that's for the next while-loop
		while k >= 0 and cycle1[k] == cycle2[l % cycle_length]:
			similarity += streak
			streak += 1
			k -= 1
			l -= 1

		# we already found a part of a sub tour from k, but we do want to check cycle[k] because that didn't match
		end = k + 1
		# now start on the first element
		while i < end:
			city_i = cycle1[i]
			# find the index of i in cycle2
			j = np.where(cycle2 == city_i)[0][0]

			while (i < end and
				   cycle1[i] == cycle2[j % cycle_length]):
				similarity += streak
				streak += 1
				i += 1
				j += 1
			streak = 1

		return similarity / max_similarity


########################################################################################################################


# CLASSES ##############################################################################################################

class Fitness:
	similarity_threshold: float = 0.5
	shape_exp: float = 3


class Initialization:
	population_size: int = 500
	max_iterations: int = 300


class Convergence:
	var_fitness_threshold: float = 0.01
	best_fitness_count_threshold: int = 30


class Selection:
	k_tournament_k: int = 3


class Mutation:
	alpha: float = 0.1
	alpha_decay_rate: float = 0


class Recombination:
	pass


class LocalOptimisation:
	proportion_worst: float = 0.5
	opt_probability: float = 0.5
	k_opt_branch_size: int = 5
	k_opt_k: int = 2


class Elimination:
	mixed_elitism_proportion: float = 0.5
	mixed_elitism_rest_merged_random_mixed_elitist_proportion: float = 0.5
	mixed_elitism_rest_merged_random_proportion_size: float = 0.5
	offspring_fitness_based_with_crowding_proportion: float = 0.5
	offspring_fitness_based_with_crowding_k: int = 5
	mixed_elitist_with_crowding_proportion: float = 0.5
	mixed_elitist_with_crowding_k: int = 5
	replace_worst_with_random_k: float = 0.3
	elitist_k_tournament_k: int = 3
	elitist_k_tournament_keep_s_best_k: int = 3
	elitist_k_tournament_keep_s_best_s: int = 5


class Settings:
	problem_size: int
	fitness: FitnessSettingsProtocol = Fitness()
	initialization: InitializationSettingsProtocol = Initialization()
	convergence: ConvergenceSettingsProtocol = Convergence()
	selection: SelectionSettingsProtocol = Selection()
	mutation: MutationSettingsProtocol = Mutation()
	recombination: RecombinationSettingsProtocol = Recombination()
	local_optimisation: LocalOptimisationSettingsProtocol = LocalOptimisation()
	elimination: EliminationSettingsProtocol = Elimination()

	def __init__(self, problem_size: int):
		self.problem_size = problem_size
		if problem_size < 100:
			self.elimination.mixed_elitism_proportion = 0.3
		elif 100 <= problem_size < 200:
			pass
		elif 200 <= problem_size < 400:
			self.initialization.population_size = 400
		elif 400 <= problem_size:
			self.initialization.population_size = 200
			self.convergence.best_fitness_count_threshold = 100
			self.local_optimisation.proportion_worst = 0.3
			self.local_optimisation.k_opt_branch_size = 5
			self.mutation.alpha = 0.5
			self.mutation.alpha_decay_rate = 0.001
			self.elimination.mixed_elitist_with_crowding_k = 7
			self.elimination.mixed_elitist_with_crowding_proportion = 0.4  # More from the offsprings (which have mutated)
		elif 600 <= problem_size:
			self.initialization.population_size = 100
		elif 800 <= problem_size:
			self.initialization.population_size = 50


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


# Mark this as Individual Protocol because of the getter and setter for the cycle property are throwing an incorrect
# type error
class Individual(IndividualProtocol):
	distance_matrix: DistanceMatrix
	fitness_sharing: float = 1.0
	dirty: bool = True
	_cycle: Cycle
	_fitness: float

	def __init__(self, cycle: Cycle, distance_matrix: DistanceMatrix):
		self._cycle = cycle
		self.distance_matrix = distance_matrix

	@property
	def fitness(self) -> float:
		if self.dirty:
			self._fitness = self.fitness_sharing * FitnessMethods.negative_of_length(self)
			self.dirty = False
		return self._fitness

	@property
	def prop(self) -> float:
		return 0.0

	# Ignore the type error because the type checker is just confused that the getter and setter in the protocol have
	# both the same name.
	@property
	def cycle(self) -> Cycle:  # type: ignore
		return self._cycle

	@cycle.setter
	def cycle(self, cycle: Cycle) -> None:
		self._cycle = cycle
		self.dirty = True

	def get_fitness_internal(self) -> float:
		return FitnessMethods.negative_of_length(self)

	def __str__(self) -> str:
		return str(self.cycle) + " : " + str(self.fitness)


class Population:
	size: int
	distance_matrix: DistanceMatrix
	individuals: list[IndividualProtocol]

	def __init__(self, individuals: List[IndividualProtocol], size: int, distance_matrix: DistanceMatrix):
		assert size == len(individuals)

		# replace every occurrence of "Inf" with -1
		distance_matrix[distance_matrix == float('inf')] = INFINITY_REPRESENTATION

		self.size = size
		self.distance_matrix = distance_matrix
		self.individuals = individuals

	def update_fitness_sharing_proportions(self, similarity_threshold: float = 0.5, shape_exp: float = 1) -> None:
		for individual in self.individuals:
			similarities_above_threshold: List[float] = []
			for other_individual in self.individuals:
				similarity = SimilarityMethods.hamming(individual.cycle, other_individual.cycle)
				if similarity > similarity_threshold:
					# similarity between 0 and 1
					similarities_above_threshold.append(similarity ** shape_exp)
			# limit subtracting to at most 25%
			individual.fitness_sharing = 0.75 + (0.25 * 1 / sum(similarities_above_threshold))

	def mean_fitness(self) -> float:
		""" Calculate the mean fitness of the population, filtering out invalid cycles. """
		valid_individuals_fitness = [individual.fitness for individual in self.individuals if
									 is_valid_cycle(individual.cycle, self.distance_matrix)]
		if len(valid_individuals_fitness) == 0:
			return -INFINITY_REPRESENTATION
		return sum(valid_individuals_fitness) / len(valid_individuals_fitness)

	def best_fitness(self) -> float:
		return max([individual.fitness for individual in self.individuals])

	def best_individual(self) -> IndividualProtocol:
		return max(self.individuals, key=lambda individual: individual.fitness)

	def variance_fitness(self) -> float:
		""" Calculate the variance of the fitness of the population, filtering out invalid cycles. """
		valid_individuals_fitness = [individual.fitness for individual in self.individuals if
									 is_valid_cycle(individual.cycle, self.distance_matrix)]
		return float(np.var(valid_individuals_fitness))

	def valid_invalid_individual_proportion(self) -> tuple[int, int]:
		""" Calculate the proportion of valid and invalid individuals in the population. """
		valid_individuals = [individual for individual in self.individuals if
							 is_valid_cycle(individual.cycle, self.distance_matrix)]
		return len(valid_individuals), self.size - len(valid_individuals)

	def __str__(self):
		return "\n".join([str(individual) for individual in self.individuals])


########################################################################################################################

# Modify the class name to match your student number.
class r0829897:

	def __init__(self):
		self.reporter = Reporter.Reporter(self.__class__.__name__)

	# The evolutionary algorithm's main loop
	def optimize(self, filename):
		# Read distance matrix from file.
		file = open(filename)
		distance_matrix: DistanceMatrix = np.loadtxt(file, delimiter=",")
		file.close()

		assert distance_matrix.ndim == 2  # distance_matrix should be a 2D array
		assert distance_matrix.shape[0] == distance_matrix.shape[1]  # distance_matrix should be square
		evolutionary_algorithm: EvolutionaryAlgorithmProtocol = EvolutionaryAlgorithm(distance_matrix)

		evolutionary_algorithm.initialize_population()
		while not evolutionary_algorithm.converged:
			evolutionary_algorithm.select()
			evolutionary_algorithm.recombination()
			evolutionary_algorithm.mutation()
			evolutionary_algorithm.local_optimisation()
			evolutionary_algorithm.elimination()
			evolutionary_algorithm.insert_diversity()

			mean_fitness = evolutionary_algorithm.population.mean_fitness()
			best_fitness = evolutionary_algorithm.population.best_fitness()
			best_solution = evolutionary_algorithm.population.best_individual().cycle

			# Call the reporter with:
			#  - the mean objective function value of the population
			#  - the best objective function value of the population
			#  - a 1D numpy array in the cycle notation containing the best solution
			#    with city numbering starting from 0
			timeLeft = self.reporter.report(mean_fitness, best_fitness, best_solution)
			if timeLeft < 0:
				break

		return 0
