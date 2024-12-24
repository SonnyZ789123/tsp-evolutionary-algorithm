import math
import unittest

import numpy as np

from classes.DistanceMatrix import DistanceMatrix
from methods.InitializationMethods import InitializationMethods

MOCK_DISTANCE_MATRIX = DistanceMatrix(np.array([[math.inf, 1, 1, 1, 1, math.inf],
												[1, math.inf, 1, 1, math.inf, 1],
												[1, math.inf, math.inf, 1, 1, 1],
												[1, 1, 1, math.inf, 1, 1],
												[1, math.inf, 1, 1, math.inf, 1],
												[1, 1, 1, 1, math.inf, math.inf]]))


class TestInitializationMethods(unittest.TestCase):
	def test_generate_random_valid_individual(self):
		individual = InitializationMethods.generate_random_valid_individual(MOCK_DISTANCE_MATRIX)
		self.assertEqual(len(individual.cycle), 6)

		available = list(range(6))
		for i in range(6):
			self.assertLess(MOCK_DISTANCE_MATRIX.value[individual.cycle[i], individual.cycle[(i + 1) % 6]], math.inf)
			self.assertIn(individual.cycle[i], available)
			available.remove(int(individual.cycle[i]))

	def test_generate_random_valid_population(self):
		# Just calls generate_random_valid_individual the specified number of times, testing
		# generate_random_valid_individual is enough
		individuals = InitializationMethods.generate_random_valid_population(10, MOCK_DISTANCE_MATRIX)
		self.assertEqual(len(individuals), 10)


if __name__ == '__main__':
	unittest.main()
