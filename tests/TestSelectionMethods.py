import unittest
from unittest.mock import patch
import numpy as np

from methods.SelectionMethods import SelectionMethods
from protocols.PopulationProtocol import PopulationProtocol
from classes.DistanceMatrix import DistanceMatrix
from tests.MockIndividual import MockIndividual
from tests.MockPopulation import MockPopulation

MOCK_DISTANCE_MATRIX = DistanceMatrix(np.array([[1, 1], [1, 1]]))
MOCK_INDIVIDUALS = [MockIndividual(np.array([1, 2]), MOCK_DISTANCE_MATRIX, lambda _: 1, lambda _: None) for _ in range(4)]


class TestSelectionMethods(unittest.TestCase):
	mock_population: PopulationProtocol

	def setUp(self):
		self.mock_population = MockPopulation(MOCK_DISTANCE_MATRIX, MOCK_INDIVIDUALS)

	@patch('numpy.random.randint')
	def test_random_selection_mocked(self, mock_randint):
		"""Test that random selection picks the expected individual when randint is mocked."""
		mock_randint.return_value = 2  # Mock randint to always return index 2
		selected_individual = SelectionMethods.random(self.mock_population)
		self.assertEqual(selected_individual, MOCK_INDIVIDUALS[2])
		mock_randint.assert_called_once_with(0, self.mock_population.size)


if __name__ == '__main__':
	unittest.main()
