from typing import Protocol


class FitnessProtocol(Protocol):
	similarity_threshold: float
	""" The threshold for similarity between cycles, between 0 and 1. """
	shape_exp: float
	""" The exponent for the shape of the fitness sharing function, between 0.25 and 4 """


class InitializationProtocol(Protocol):
	population_size: int
	""" The size of the population, should be a positive even integer. """
	max_iterations: int


class ConvergenceProtocol(Protocol):
	# diff_mean_best_threshold: float
	# """ The threshold for difference between mean and best fitness, between 0 and 1. """
	var_fitness_threshold: float
	""" The threshold for variance of fitness, between 0 and 1. """


class SelectionProtocol(Protocol):
	k_tournament: int
	""" The number of individuals in the tournament. """


class MutationProtocol(Protocol):
	alpha: float
	""" The probability of mutation. """


class RecombinationProtocol(Protocol):
	...


class LocalOptimisationProtocol(Protocol):
	alpha: float
	""" The probability of local optimisation. """
	k_opt_pool_size: int
	""" The amount of neighbours to generate. """
	k_opt_k: int
	""" The value of k for k-opt, the depth of the search tree. """


class EliminationProtocol(Protocol):
	mixed_elitism_proportion: float
	""" The proportion of the population to keep in the next generation, between 0 and 1. """


class SettingsProtocol(Protocol):
	fitness: FitnessProtocol
	initialization: InitializationProtocol
	convergence: ConvergenceProtocol
	selection: SelectionProtocol
	mutation: MutationProtocol
	recombination: RecombinationProtocol
	local_optimisation: LocalOptimisationProtocol
	elimination: EliminationProtocol
