import unittest

import numpy as np

from config.custom_types import DistanceMatrix, INFINITY_REPRESENTATION
from methods.InitializationMethods import InitializationMethods, Heuristics
from utils.cycle_utils import is_valid_cycle

MOCK_DISTANCE_MATRIX: DistanceMatrix = np.array([[INFINITY_REPRESENTATION, 1, 1, 1, 1, INFINITY_REPRESENTATION],
												 [1, INFINITY_REPRESENTATION, 1, 1, INFINITY_REPRESENTATION, 1],
												 [1, INFINITY_REPRESENTATION, INFINITY_REPRESENTATION, 1, 1, 1],
												 [1, 1, 1, INFINITY_REPRESENTATION, 1, 1],
												 [1, INFINITY_REPRESENTATION, 1, 1, INFINITY_REPRESENTATION, 1],
												 [1, 1, 1, 1, INFINITY_REPRESENTATION, INFINITY_REPRESENTATION]])


class TestInitializationMethods(unittest.TestCase):
	def test_generate_random_valid_individual(self):
		individual = InitializationMethods.generate_random_valid_individual(MOCK_DISTANCE_MATRIX)
		self.assertEqual(len(individual.cycle), 6)
		self.assertTrue(is_valid_cycle(individual.cycle, MOCK_DISTANCE_MATRIX))

	def test_generate_random_valid_population(self):
		# Just calls generate_random_valid_individual the specified number of times, testing
		# generate_random_valid_individual is enough
		individuals = InitializationMethods.generate_random_valid_population(10, MOCK_DISTANCE_MATRIX)
		self.assertEqual(len(individuals), 10)
		for individual in individuals:
			self.assertTrue(is_valid_cycle(individual.cycle, MOCK_DISTANCE_MATRIX))

	def test_generate_greedy_individual_nearest_neighbour(self):
		individual = InitializationMethods.generate_greedy_individual(MOCK_DISTANCE_MATRIX,
																	  Heuristics.nearest_neighbour)
		self.assertEqual(len(individual.cycle), 6)
		self.assertTrue(is_valid_cycle(individual.cycle, MOCK_DISTANCE_MATRIX))


	def test_generate_greedy_population_nearest_neighbour(self):
		# Just calls generate_random_valid_individual the specified number of times, testing
		# generate_random_valid_individual is enough
		individuals = InitializationMethods.generate_greedy_population(10, MOCK_DISTANCE_MATRIX,
																	   Heuristics.nearest_neighbour)
		self.assertEqual(len(individuals), 10)
		for individual in individuals:
			self.assertTrue(is_valid_cycle(individual.cycle, MOCK_DISTANCE_MATRIX))


if __name__ == '__main__':
	unittest.main()
