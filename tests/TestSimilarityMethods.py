import unittest

import numpy as np

from config.custom_types import Cycle
from methods.SimilarityMethods import SimilarityMethods


class TestUtils(unittest.TestCase):
	cycle1: Cycle
	cycle2: Cycle

	def setUp(self):
		self.cycle1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
		self.cycle2 = np.array([1, 2, 5, 6, 8, 7, 3, 4, 9, 0])

	def test_cycle_subtour_exponential(self):
		similarity = SimilarityMethods.cycle_subtour_exponential(self.cycle1, self.cycle2)
		self.assertEqual((1 + 2 + 4 + 8) + (1 + 2) + (1 + 2) + 1 + 1, similarity)


if __name__ == '__main__':
	unittest.main()
