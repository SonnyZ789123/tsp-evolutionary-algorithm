import unittest

import numpy as np

from config.custom_types import DistanceMatrix
from tests.MockIndividual import MockIndividual

from methods.RecombinationMethods import RecombinationMethods

MOCK_DISTANCE_MATRIX: DistanceMatrix = np.array([[1, 1, 1, 1, 1, 1],
												 [1, 1, 1, 1, 1, 1],
												 [1, 1, 1, 1, 1, 1],
												 [1, 1, 1, 1, 1, 1],
												 [1, 1, 1, 1, 1, 1],
												 [1, 1, 1, 1, 1, 1]])
MOCK_INDIVIDUAL1 = MockIndividual(np.array([1, 2, 3, 6, 5, 4]), MOCK_DISTANCE_MATRIX, lambda _: 5, lambda _: None)
MOCK_INDIVIDUAL2 = MockIndividual(np.array([4, 5, 3, 2, 1, 6]), MOCK_DISTANCE_MATRIX, lambda _: 1, lambda _: None)


class TestRecombinationMethods(unittest.TestCase):
	def test_deterministic_best_parent(self):
		offspring = RecombinationMethods.deterministic_best_parent(MOCK_INDIVIDUAL1, MOCK_INDIVIDUAL2)
		self.assertEqual(offspring, MOCK_INDIVIDUAL1)


if __name__ == '__main__':
	unittest.main()
