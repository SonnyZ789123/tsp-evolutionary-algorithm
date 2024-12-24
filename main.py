import numpy as np

from classes.DistanceMatrix import DistanceMatrix
from classes.EvolutionaryAlgorithm import EvolutionaryAlgorithm
from protocols.DistanceMatrixProtocol import DistanceMatrixProtocol
from protocols.EvolutionaryAlgorithmProtocol import EvolutionaryAlgorithmProtocol


def solve_tsp():
	# Read distance matrix from file.
	file = open("tour50.csv")
	distance_matrix_value = np.loadtxt(file, delimiter=",")
	file.close()

	distance_matrix: DistanceMatrixProtocol = DistanceMatrix(distance_matrix_value)

	assert distance_matrix.value.ndim == 2  # distance_matrix should be a 2D array
	assert distance_matrix.value.shape[0] == distance_matrix.value.shape[1]  # distance_matrix should be square
	evolutionary_algorithm: EvolutionaryAlgorithmProtocol = EvolutionaryAlgorithm(distance_matrix)

	while not evolutionary_algorithm.converged:
		evolutionary_algorithm.select()
		evolutionary_algorithm.mutation()
		evolutionary_algorithm.recombination()
		evolutionary_algorithm.elimination()

		print("mean fitness", evolutionary_algorithm.population.mean_fitness())
		print("best fitness", evolutionary_algorithm.population.best_fitness())
		print("best individual", evolutionary_algorithm.population.best_individual().cycle)

	return 0


if __name__ == "__main__":
	solve_tsp()