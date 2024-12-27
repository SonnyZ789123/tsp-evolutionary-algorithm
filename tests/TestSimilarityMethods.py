import unittest

import numpy as np

from config.custom_types import Cycle
from methods.SimilarityMethods import SimilarityMethods


class TestUtils(unittest.TestCase):
	cycle1: Cycle
	cycle2: Cycle
	cycle_subtour_linear_streak_max_similarity: int

	def setUp(self):
		self.cycle1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
		self.cycle2 = np.array([1, 2, 5, 6, 8, 7, 3, 4, 9, 0])
		self.cycle_subtour_linear_streak_max_similarity = sum(range(1, 11))

	def test_cycle_subtour_linear_streak(self):
		similarity = SimilarityMethods.cycle_subtour_linear_streak(self.cycle1, self.cycle2)
		self.assertEqual(
			((1 + 2 + 3 + 4) + (1 + 2) + (1 + 2) + 1 + 1) / self.cycle_subtour_linear_streak_max_similarity, similarity)

	def test_cycle_subtour_linear_streak_min_similarity(self):
		self.cycle2 = np.array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
		similarity = SimilarityMethods.cycle_subtour_linear_streak(self.cycle1, self.cycle2)
		self.assertEqual(10 / self.cycle_subtour_linear_streak_max_similarity, similarity)

	def test_cycle_subtour_linear_streak_max_similarity(self):
		self.cycle2 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
		similarity = SimilarityMethods.cycle_subtour_linear_streak(self.cycle1, self.cycle2)
		self.assertEqual(1, similarity)


if __name__ == '__main__':
	unittest.main()
