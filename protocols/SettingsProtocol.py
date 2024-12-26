from typing import Protocol


class InitializationProtocol(Protocol):
	population_size: int
	""" The size of the population, should be a positive even integer. """
	max_iterations: int


class ConvergenceProtocol(Protocol):
	diff_mean_best_threshold: float
	""" The threshold for difference between mean and best fitness, between 0 and 1. """
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


class EliminationProtocol(Protocol):
	...


class SettingsProtocol(Protocol):
	initialization: InitializationProtocol
	convergence: ConvergenceProtocol
	selection: SelectionProtocol
	mutation: MutationProtocol
	recombination: RecombinationProtocol
	elimination: EliminationProtocol
