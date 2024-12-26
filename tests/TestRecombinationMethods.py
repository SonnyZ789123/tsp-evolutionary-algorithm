import unittest
from unittest.mock import patch

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

MOCK_INDIVIDUAL3 = MockIndividual(np.array([2, 3, 5, 1, 4, 6]), MOCK_DISTANCE_MATRIX, lambda _: 5, lambda _: None)
MOCK_INDIVIDUAL4 = MockIndividual(np.array([3, 5, 4, 2, 1, 6]), MOCK_DISTANCE_MATRIX, lambda _: 1, lambda _: None)


class TestRecombinationMethods(unittest.TestCase):
	def test_deterministic_best_parent(self):
		offspring = RecombinationMethods.deterministic_best_parent(MOCK_INDIVIDUAL1, MOCK_INDIVIDUAL2)
		self.assertEqual(offspring, MOCK_INDIVIDUAL1)

	@patch('numpy.random.choice')
	def test_order_crossover(self, mock_choice):
		mock_choice.return_value = [2, 4]
		offspring1, offspring2 = RecombinationMethods.order_crossover(MOCK_INDIVIDUAL1, MOCK_INDIVIDUAL2)
		self.assertEqual(offspring1.cycle.tolist(), [5, 2, 3, 6, 1, 4])
		self.assertEqual(offspring2.cycle.tolist(), [1, 6, 3, 2, 5, 4])

		mock_choice.return_value = [3, 6]
		offspring1, offspring2 = RecombinationMethods.order_crossover(MOCK_INDIVIDUAL3, MOCK_INDIVIDUAL4)
		self.assertEqual(offspring1.cycle.tolist(), [3, 5, 2, 1, 4, 6])
		self.assertEqual(offspring2.cycle.tolist(), [3, 5, 4, 2, 1, 6])


if __name__ == '__main__':
	unittest.main()
