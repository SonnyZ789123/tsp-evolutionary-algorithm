import unittest

import numpy as np

from config.custom_types import DistanceMatrix
from methods.InitializationMethods import InitializationMethods
from utils.cycle_utils import is_valid_cycle

MOCK_DISTANCE_MATRIX: DistanceMatrix = np.array([[-1, 1, 1, 1, 1, -1],
												 [1, -1, 1, 1, -1, 1],
												 [1, -1, -1, 1, 1, 1],
												 [1, 1, 1, -1, 1, 1],
												 [1, -1, 1, 1, -1, 1],
												 [1, 1, 1, 1, -1, -1]])


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


if __name__ == '__main__':
	unittest.main()
