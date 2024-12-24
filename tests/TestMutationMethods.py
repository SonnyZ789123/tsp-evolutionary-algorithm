import unittest
from unittest.mock import patch

import numpy as np

from classes.DistanceMatrix import DistanceMatrix
from tests.MockIndividual import MockIndividual

from methods.MutationMethods import MutationMethods

MOCK_DISTANCE_MATRIX = DistanceMatrix(np.array([1, 1, 1, 1, 1, 1,
												1, 1, 1, 1, 1, 1,
												1, 1, 1, 1, 1, 1]))
MOCK_INDIVIDUAL1 = MockIndividual(np.array([1, 2, 3, 6, 5, 4]), MOCK_DISTANCE_MATRIX, lambda _: 1, lambda _: None)


class TestMutationMethods(unittest.TestCase):
	@patch('numpy.random.choice')
	def test_swap(self, mock_choice):
		mock_choice.return_value = 2, 4
		MutationMethods.swap(MOCK_INDIVIDUAL1)
		self.assertEqual(MOCK_INDIVIDUAL1.cycle.tolist(), [1, 2, 5, 6, 3, 4])


if __name__ == '__main__':
	unittest.main()
