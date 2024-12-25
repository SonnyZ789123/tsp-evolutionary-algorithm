import unittest

import numpy as np

from config.custom_types import DistanceMatrix
from protocols.IndividualProtocol import IndividualProtocol
from protocols.PopulationProtocol import PopulationProtocol
from tests.MockIndividual import MockIndividual

from methods.EliminationMethods import EliminationMethods
from tests.MockPopulation import MockPopulation

MOCK_DISTANCE_MATRIX: DistanceMatrix = np.array([[1, 1, 1],
												 [1, 1, 1],
												 [1, 1, 1]])
POPULATION_SIZE = 10
MOCK_INDIVIDUALS = [MockIndividual(np.array([1, 2, 3]), MOCK_DISTANCE_MATRIX, lambda _: 1, lambda _: None) for _ in
					range(POPULATION_SIZE)]
MOCK_OFFSPRINGS = [MockIndividual(np.array([3, 2, 1]), MOCK_DISTANCE_MATRIX, lambda _: 3, lambda _: None) for _ in
				   range(POPULATION_SIZE)]
MOCK_POPULATION = MockPopulation(MOCK_DISTANCE_MATRIX, MOCK_INDIVIDUALS)


class TestEliminationMethods(unittest.TestCase):
	mock_population: PopulationProtocol
	mock_offsprings: list[IndividualProtocol]

	def setUp(self):
		self.mock_population = MOCK_POPULATION
		self.mock_offsprings = MOCK_OFFSPRINGS

	def test_age_based(self):
		EliminationMethods.age_based(self.mock_population, self.mock_offsprings)
		self.assertEqual(self.mock_population.individuals, self.mock_offsprings)


if __name__ == '__main__':
	unittest.main()
