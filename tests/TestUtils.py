import unittest

import numpy as np

from classes.DistanceMatrix import DistanceMatrix
from utils.cycle_utils import is_valid_cycle

MOCK_DISTANCE_MATRIX = DistanceMatrix(np.array([[-1, 1, 1, 1, 1, -1],
												[1, -1, 1, 1, -1, 1],
												[1, -1, -1, 1, 1, 1],
												[1, 1, 1, -1, 1, 1],
												[1, -1, 1, 1, -1, 1],
												[1, 1, 2, 1, -1, -1]]))


class TestUtils(unittest.TestCase):
	def test_is_valid_cycle(self):
		self.assertTrue(is_valid_cycle(np.array([0, 1, 2, 3, 4, 5]), MOCK_DISTANCE_MATRIX))
		self.assertFalse(is_valid_cycle(np.array([0, 0, 2, 3, 4, 5]), MOCK_DISTANCE_MATRIX))
		self.assertFalse(is_valid_cycle(np.array([0, 2, 1, 3, 4, 5]), MOCK_DISTANCE_MATRIX))
		self.assertFalse(is_valid_cycle(np.array([0, 2, 1, 3, 4, 5, 6]), MOCK_DISTANCE_MATRIX))
		self.assertTrue(is_valid_cycle(np.array([4, 2, 3, 5, 1, 0]), MOCK_DISTANCE_MATRIX))

if __name__ == '__main__':
	unittest.main()
