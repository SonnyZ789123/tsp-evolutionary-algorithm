import unittest

import numpy as np

from config.custom_types import DistanceMatrix
from tests.MockIndividual import MockIndividual

from methods.FitnessMethods import FitnessMethods

MOCK_DISTANCE_MATRIX: DistanceMatrix = np.array([[1, 2, 1],
								 [9, 3, 2],
								 [1, 5, 4]])
MOCK_INDIVIDUAL1 = MockIndividual(np.array([1, 0, 2]), MOCK_DISTANCE_MATRIX, lambda _: -1, lambda _: None)
MOCK_INDIVIDUAL2 = MockIndividual(np.array([0, 1, 2]), MOCK_DISTANCE_MATRIX, lambda _: -1, lambda _: None)


class TestFitnessMethods(unittest.TestCase):
	def test_negative_of_length(self):
		fitness1 = FitnessMethods.negative_of_length(MOCK_INDIVIDUAL1)
		expected_fitness1 = -(9 + 1 + 5)
		self.assertEqual(expected_fitness1, fitness1)

		fitness2 = FitnessMethods.negative_of_length(MOCK_INDIVIDUAL2)  # -(2 + 2 + 1) = -5
		self.assertGreater(fitness2, fitness1)


if __name__ == '__main__':
	unittest.main()
