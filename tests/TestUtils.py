import unittest

import numpy as np

from config.custom_types import DistanceMatrix
from protocols.IndividualProtocol import IndividualProtocol
from tests.MockIndividual import MockIndividual
from utils.cycle_utils import is_valid_cycle, get_cycle_length

MOCK_DISTANCE_MATRIX: DistanceMatrix = np.array([[-1, 1, 1, 1, 1, -1],
												 [1, -1, 1, 1, -1, 1],
												 [1, -1, -1, 1, 1, 1],
												 [1, 1, 1, -1, 1, 1],
												 [1, -1, 1, 1, -1, 1],
												 [1, 1, 2, 1, -1, -1]])

MOCK_DISTANCE_MATRIX2: DistanceMatrix = np.array([[1, 2, 1],
												 [9, 3, 2],
												 [1, 5, 4]])
MOCK_INDIVIDUAL: IndividualProtocol = MockIndividual(np.array([1, 0, 2]), MOCK_DISTANCE_MATRIX2, lambda _: -1, lambda _: None)


class TestUtils(unittest.TestCase):
	def test_is_valid_cycle(self):
		self.assertTrue(is_valid_cycle(np.array([0, 1, 2, 3, 4, 5]), MOCK_DISTANCE_MATRIX))
		self.assertFalse(is_valid_cycle(np.array([0, 0, 2, 3, 4, 5]), MOCK_DISTANCE_MATRIX))
		self.assertFalse(is_valid_cycle(np.array([0, 2, 1, 3, 4, 5]), MOCK_DISTANCE_MATRIX))
		self.assertFalse(is_valid_cycle(np.array([0, 2, 1, 3, 4, 5, 6]), MOCK_DISTANCE_MATRIX))
		self.assertTrue(is_valid_cycle(np.array([4, 2, 3, 5, 1, 0]), MOCK_DISTANCE_MATRIX))

	def test_get_cycle_length(self):
		self.assertEqual(get_cycle_length(MOCK_INDIVIDUAL.cycle, MOCK_INDIVIDUAL.distance_matrix), 9 + 1 + 5)

if __name__ == '__main__':
	unittest.main()
