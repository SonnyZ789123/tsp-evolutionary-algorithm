import time
from typing import List

import numpy as np

import Reporter
from classes.EvolutionaryAlgorithm import EvolutionaryAlgorithm
from config.custom_types import DistanceMatrix
from protocols.EvolutionaryAlgorithmProtocol import EvolutionaryAlgorithmProtocol
from utils.cycle_utils import get_cycle_length
from utils.plotting import generate_fitness_plot, generate_log_plot


# Modify the class name to match your student number.
class r0829897:

	def __init__(self):
		self.reporter = Reporter.Reporter(self.__class__.__name__)

	# The evolutionary algorithm's main loop
	def optimize(self, filename):
		################################################### from the template
		# Read distance matrix from file.
		file = open(filename)
		distance_matrix: DistanceMatrix = np.loadtxt(file, delimiter=",")
		file.close()
		###################################################

		assert distance_matrix.ndim == 2  # distance_matrix should be a 2D array
		assert distance_matrix.shape[0] == distance_matrix.shape[1]  # distance_matrix should be square
		evolutionary_algorithm: EvolutionaryAlgorithmProtocol = EvolutionaryAlgorithm(distance_matrix)

		mean_fitness_history: List[float] = []
		best_fitness_history: List[float] = []
		time_between_iteration_history: List[float] = []
		previous_timeLeft = 300

		# Time the algorithm
		start_time = time.time()
		evolutionary_algorithm.initialize_population()
		while not evolutionary_algorithm.converged:
			# evolutionary_algorithm.update_fitness_sharing_proportions()
			evolutionary_algorithm.select()
			evolutionary_algorithm.recombination()
			evolutionary_algorithm.mutation()
			evolutionary_algorithm.local_optimisation()
			evolutionary_algorithm.elimination()
			evolutionary_algorithm.insert_diversity()

			mean_fitness = evolutionary_algorithm.population.mean_fitness()
			best_fitness = evolutionary_algorithm.population.best_fitness()
			best_solution = evolutionary_algorithm.population.best_individual().cycle

			# For plotting
			mean_fitness_history.append(mean_fitness)
			best_fitness_history.append(best_fitness)
			# variance_fitness_history.append(variance_fitness)

			###################################################
			# Call the reporter with: KEEP THIS
			#  - the mean objective function value of the population
			#  - the best objective function value of the population
			#  - a 1D numpy array in the cycle notation containing the best solution
			#    with city numbering starting from 0
			timeLeft = self.reporter.report(mean_fitness, best_fitness, best_solution)

			time_between_iteration_history.append(previous_timeLeft - timeLeft) # TODO: Remove this
			previous_timeLeft = timeLeft # TODO: Remove this

			if timeLeft < 0:
				break
			###################################################

		# TODO: Remove the plotting and writing in the file
		end_time = time.time()
		elapsed_time = end_time - start_time

		# Plotting
		iteration_numbers = list(range(len(mean_fitness_history)))
		mean_fitness_history_rebased = [-i for i in mean_fitness_history]
		best_fitness_history_rebased = [-i for i in best_fitness_history]
		generate_fitness_plot(iteration_numbers, mean_fitness_history_rebased, y_label="-Fitness",
							  title=f"Mean fitness for {filename}")
		generate_fitness_plot(iteration_numbers, best_fitness_history_rebased, y_label="-Fitness",
							  title=f"Best fitness for {filename}")
		best_cycle_length = get_cycle_length(evolutionary_algorithm.population.best_individual().cycle, distance_matrix)
		final_mean_fitness = mean_fitness_history_rebased[-1]
		average_time_between_iterations = np.mean(time_between_iteration_history)
		best_cycle = evolutionary_algorithm.population.best_individual().cycle

		with open('history.txt', 'a') as file:
			# Add text to the file
			file.write(filename + "\n")
			file.write(f"Time: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}\n")
			print(f"Elapsed time for solving TSP: {elapsed_time:.2f} seconds")
			file.write(f"Elapsed time for solving TSP: {elapsed_time:.2f} seconds\n")
			print(f"Best individual cycle length: {best_cycle_length:.0f}")
			file.write(f"Best individual cycle length: {best_cycle_length:.0f}\n")
			print(f"Final mean fitness: {final_mean_fitness:.2f}")
			file.write(f"Final mean fitness: {final_mean_fitness:.2f}\n")
			print(f"Average time between iterations: {average_time_between_iterations:.6f} seconds")
			file.write(f"Average time between iterations: {average_time_between_iterations:.6f} seconds\n")
			print(f"Best cycle: {best_cycle}")
			file.write(f"Best cycle: {best_cycle}\n")
			file.write("====================================================\n")

		return elapsed_time, best_cycle_length, final_mean_fitness
