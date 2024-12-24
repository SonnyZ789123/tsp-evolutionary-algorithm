import unittest

import numpy as np

from classes.DistanceMatrix import DistanceMatrix
from tests.MockIndividual import MockIndividual

from methods.FitnessMethods import FitnessMethods

MOCK_DISTANCE_MATRIX = DistanceMatrix(np.array([[1, 2, 1],
												[9, 3, 2],
												[1, 5, 4]]))
MOCK_INDIVIDUAL = MockIndividual(np.array([1, 0, 2]), MOCK_DISTANCE_MATRIX, lambda _: -1, lambda _: None)


class TestFitnessMethods(unittest.TestCase):
	def test_negative_of_length(self):
		fitness = FitnessMethods.negative_of_length(MOCK_INDIVIDUAL)
		expected_fitness = -(9 + 1 + 5)
		self.assertEqual(expected_fitness, fitness)


if __name__ == '__main__':
	unittest.main()
