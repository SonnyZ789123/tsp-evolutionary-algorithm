import time
from typing import List

import numpy as np

from config.custom_types import DistanceMatrix
from classes.EvolutionaryAlgorithm import EvolutionaryAlgorithm
from protocols.EvolutionaryAlgorithmProtocol import EvolutionaryAlgorithmProtocol
from utils.cycle_utils import get_cycle_length, get_cycle_distances
from utils.plotting import generate_plot


def solve_tsp():
	# Read distance matrix from file.
	file = open("tour50.csv")
	distance_matrix: DistanceMatrix = np.loadtxt(file, delimiter=",")
	file.close()

	assert distance_matrix.ndim == 2  # distance_matrix should be a 2D array
	assert distance_matrix.shape[0] == distance_matrix.shape[1]  # distance_matrix should be square
	evolutionary_algorithm: EvolutionaryAlgorithmProtocol = EvolutionaryAlgorithm(distance_matrix)

	mean_fitness_history: List[float] = []
	best_fitness_history: List[float] = []
	variance_fitness_history: List[float] = []

	# Time the algorithm
	start_time = time.time()

	while not evolutionary_algorithm.converged:
		evolutionary_algorithm.select()
		evolutionary_algorithm.recombination()
		evolutionary_algorithm.mutation()
		evolutionary_algorithm.elimination()

		# For plotting
		mean_fitness_history.append(evolutionary_algorithm.population.mean_fitness())
		best_fitness_history.append(evolutionary_algorithm.population.best_fitness())
		individuals_fitness = [individual.fitness for individual in evolutionary_algorithm.population.individuals]
		variance_fitness_history.append(float(np.var(individuals_fitness)))

	end_time = time.time()
	elapsed_time = end_time - start_time
	print(f"Elapsed time for solving TSP: {elapsed_time:.2f} seconds")

	# Plotting
	iteration_numbers = list(range(len(mean_fitness_history)))
	mean_fitness_history_rebased = [(i / 1000 + 110) for i in mean_fitness_history]
	best_fitness_history_rebased = [(i / 1000 + 110) for i in best_fitness_history]
	generate_plot(iteration_numbers, mean_fitness_history_rebased, y_label="Mean fitness/1000 + 110")
	generate_plot(iteration_numbers, best_fitness_history_rebased, y_label="Best fitness/1000 + 110")
	generate_plot(iteration_numbers, variance_fitness_history, y_label="Variance fitness")
	print(f"Best individual cycle length: {
	get_cycle_length(evolutionary_algorithm.population.best_individual().cycle, distance_matrix):.0f}")
	print(f"Best individual cycle: {evolutionary_algorithm.population.best_individual().cycle}")
	print(f"Best individual cycle distances: {
	get_cycle_distances(evolutionary_algorithm.population.best_individual().cycle, distance_matrix)}")

	return 0


if __name__ == "__main__":
	solve_tsp()
