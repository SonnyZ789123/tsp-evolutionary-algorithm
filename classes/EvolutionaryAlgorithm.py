import random

from classes.Individual import Individual
from classes.Population import Population
from config.Settings import Settings
from methods.EliminationMethods import EliminationMethods
from methods.RecombinationMethods import RecombinationMethods
from methods.SelectionMethods import SelectionMethods
from methods.ConvergenceMethods import ConvergenceMethods
from protocols.DistanceMatrixProtocol import DistanceMatrixProtocol
from protocols.IndividualProtocol import IndividualProtocol
from protocols.PopulationProtocol import PopulationProtocol
from protocols.SettingsProtocol import SettingsProtocol


class EvolutionaryAlgorithm:
	settings: SettingsProtocol = Settings()
	population: PopulationProtocol
	_iteration: int = 0
	_offsprings: list[IndividualProtocol] = []
	_converged: bool

	def __init__(self, distance_matrix: DistanceMatrixProtocol):
		self.population = Population(self.settings.initialization.population_size, distance_matrix)

	@property
	def converged(self) -> bool:
		self._iteration += 1
		if self._iteration >= self.settings.initialization.max_iterations:
			return True
		if ConvergenceMethods.difference_mean_and_best_fitness(self.population, 0.01):
			return True
		return False

	def select(self) -> Individual:
		return SelectionMethods.random(self.population)

	def mutation(self):
		for individual in self._offsprings:
			if random.random() < self.settings.mutation.alpha:
				individual.mutate()

	def recombination(self) -> None:
		self._offsprings = []
		for _ in range(self.settings.initialization.population_size):
			parent1 = self.select()
			parent2 = self.select()
			offspring = RecombinationMethods.deterministic_best_parent(parent1, parent2)
			self._offsprings.append(offspring)

	def elimination(self) -> None:
		EliminationMethods.age_based(self.population, self._offsprings)