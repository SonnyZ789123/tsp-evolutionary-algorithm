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
POPULATION_SIZE = 6


class TestEliminationMethods(unittest.TestCase):
	mock_population: PopulationProtocol
	mock_offsprings: list[IndividualProtocol]

	def setUp(self):
		mock_individuals = [MockIndividual(np.array([1, 2, 3]), MOCK_DISTANCE_MATRIX, lambda _: i, lambda _: None)
							for i in range(POPULATION_SIZE)]
		self.mock_population = MockPopulation(MOCK_DISTANCE_MATRIX, mock_individuals)
		self.mock_offsprings = [MockIndividual(np.array([3, 2, 1]), MOCK_DISTANCE_MATRIX, lambda _: i, lambda _: None)
								for i in range(POPULATION_SIZE)]

	def test_age_based(self):
		EliminationMethods.age_based(self.mock_population, self.mock_offsprings)
		self.assertEqual(self.mock_population.individuals, self.mock_offsprings)

	def test_mixed_elitist1(self):
		result = self.mock_population.individuals[0:3] + self.mock_offsprings[0:3]
		EliminationMethods.mixed_elitist(self.mock_population, self.mock_offsprings, 0.5)
		for individual in result:
			self.assertIn(individual, self.mock_population.individuals)

	def test_mixed_elitist2(self):
		result = self.mock_population.individuals[0:2] + self.mock_offsprings[0:4]
		EliminationMethods.mixed_elitist(self.mock_population, self.mock_offsprings, 0.3)
		for individual in result:
			self.assertIn(individual, self.mock_population.individuals)


if __name__ == '__main__':
	unittest.main()
