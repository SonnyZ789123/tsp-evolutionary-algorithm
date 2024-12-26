import unittest
from unittest.mock import patch

import numpy as np

from config.custom_types import DistanceMatrix, INFINITY_REPRESENTATION
from protocols.IndividualProtocol import IndividualProtocol
from tests.MockIndividual import MockIndividual

from methods.MutationMethods import MutationMethods

MOCK_DISTANCE_MATRIX: DistanceMatrix = np.array([[1, 1, 1, 1, 1, INFINITY_REPRESENTATION],
												 [1, 1, 1, 1, 1, 1],
												 [1, 1, 1, 1, 1, 1],
												 [1, 1, 1, 1, 1, 1],
												 [1, 1, 1, 1, 1, 1],
												 [1, 1, 1, 1, 1, 1]])

class TestMutationMethods(unittest.TestCase):
	mock_individual: IndividualProtocol

	def setUp(self):
		self.mock_individual = MockIndividual(np.array([1, 2, 3, 0, 4, 5]), MOCK_DISTANCE_MATRIX, lambda _: 1, lambda _: None)

	@patch('numpy.random.choice')
	def test_swap(self, mock_choice):
		mock_choice.return_value = 2, 4
		MutationMethods.swap(self.mock_individual)
		self.assertEqual([1, 2, 4, 0, 3, 5], self.mock_individual.cycle.tolist())

	@patch('numpy.random.choice')
	def test_reverse_subtour(self, mock_choice):
		mock_choice.return_value = 4, 1
		MutationMethods.reverse_subtour(self.mock_individual)
		self.assertEqual([1, 0, 3, 2, 4, 5], self.mock_individual.cycle.tolist())

		mock_choice.return_value = 0, 3
		MutationMethods.reverse_subtour(self.mock_individual)
		self.assertEqual([3, 0, 1, 2, 4, 5], self.mock_individual.cycle.tolist())

		# Leaves the cycle unchanged if the resulting cycle is invalid
		mock_choice.return_value = 3, 5
		self.mock_individual = MockIndividual(np.array([1, 2, 3, 5, 0, 4]), MOCK_DISTANCE_MATRIX, lambda _: 1, lambda _: None)
		MutationMethods.reverse_subtour(self.mock_individual)
		self.assertEqual([1, 2, 3, 5, 0, 4], self.mock_individual.cycle.tolist())



if __name__ == '__main__':
	unittest.main()
