import unittest

import numpy as np

from config.custom_types import DistanceMatrix
from methods.LocalOptimisationMethods import LocalOptimisationMethods
from methods.NeighbourMethods import NeighbourMethods
from protocols.IndividualProtocol import IndividualProtocol
from tests.MockIndividual import MockIndividual

MOCK_DISTANCE_MATRIX: DistanceMatrix = np.array([[1, 1, 1],
												 [1, 1, 1],
												 [1, 1, 1]])


class TestLocalOptimisationMethods(unittest.TestCase):
	mock_individual: IndividualProtocol

	def setUp(self):
		self.mock_individual = MockIndividual(np.array([1, 2, 3]), MOCK_DISTANCE_MATRIX, lambda _: 1, lambda _: None)

	def test_generate_neighbours(self):
		neighbours = LocalOptimisationMethods._generate_neighbours(self.mock_individual.cycle, NeighbourMethods.swap_edges,
															   3, 2)
		self.assertEqual(len(neighbours), 3 * 3)
		neighbours = LocalOptimisationMethods._generate_neighbours(self.mock_individual.cycle, NeighbourMethods.swap_edges,
															   2, 3)
		self.assertEqual(len(neighbours), 2 * 2 * 2)


if __name__ == '__main__':
	unittest.main()
