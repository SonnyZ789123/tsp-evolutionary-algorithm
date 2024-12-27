import unittest
from unittest.mock import patch

import numpy as np

from config.custom_types import DistanceMatrix
from methods.NeighbourMethods import NeighbourMethods
from protocols.IndividualProtocol import IndividualProtocol
from tests.MockIndividual import MockIndividual

MOCK_DISTANCE_MATRIX: DistanceMatrix = np.array([[1, 1, 1, 1, 1, 1],
												 [1, 1, 1, 1, 1, 1],
												 [1, 1, 1, 1, 1, 1],
												 [1, 1, 1, 1, 1, 1],
												 [1, 1, 1, 1, 1, 1],
												 [1, 1, 1, 1, 1, 1]])


class TestNeighbourMethods(unittest.TestCase):
	mock_individual: IndividualProtocol

	def setUp(self):
		self.mock_individual = MockIndividual(np.array([1, 2, 3, 6, 5, 4]), MOCK_DISTANCE_MATRIX, lambda _: 5,
											  lambda _: None)

	@patch("numpy.random.choice")
	def test_swap_edges(self, choice):
		choice.return_value = 1, 5
		neighbour = NeighbourMethods.swap_edges(self.mock_individual.cycle)
		self.assertEqual(neighbour.tolist(), [1, 4, 3, 6, 5, 2])



if __name__ == '__main__':
	unittest.main()
