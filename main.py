from typing import List

import numpy as np

from classes.DistanceMatrix import DistanceMatrix
from classes.EvolutionaryAlgorithm import EvolutionaryAlgorithm
from protocols.DistanceMatrixProtocol import DistanceMatrixProtocol
from protocols.EvolutionaryAlgorithmProtocol import EvolutionaryAlgorithmProtocol
from utils.plotting import generate_plot, normalize_to_0_100


def solve_tsp():
	# Read distance matrix from file.
	file = open("tour50.csv")
	distance_matrix_value = np.loadtxt(file, delimiter=",")
	file.close()

	distance_matrix: DistanceMatrixProtocol = DistanceMatrix(distance_matrix_value)

	assert distance_matrix.value.ndim == 2  # distance_matrix should be a 2D array
	assert distance_matrix.value.shape[0] == distance_matrix.value.shape[1]  # distance_matrix should be square
	evolutionary_algorithm: EvolutionaryAlgorithmProtocol = EvolutionaryAlgorithm(distance_matrix)

	mean_fitness_history: List[float] = []
	best_fitness_history: List[float] = []

	while not evolutionary_algorithm.converged:
		evolutionary_algorithm.select()
		evolutionary_algorithm.recombination()
		evolutionary_algorithm.mutation()
		evolutionary_algorithm.elimination()

		# For plotting
		mean_fitness_history.append(evolutionary_algorithm.population.mean_fitness())
		best_fitness_history.append(evolutionary_algorithm.population.best_fitness())

	generate_plot(list(range(len(mean_fitness_history))), normalize_to_0_100(mean_fitness_history), y_label="Mean fitness")
	generate_plot(list(range(len(best_fitness_history))), normalize_to_0_100(best_fitness_history), y_label="Best fitness")

	return 0


if __name__ == "__main__":
	solve_tsp()
