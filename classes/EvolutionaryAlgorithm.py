from classes.Individual import Individual
from classes.Population import Population
from config.Settings import Settings
from methods.EliminationMethods import EliminationMethods
from methods.RecombinationMethods import RecombinationMethods
from methods.SelectionMethods import SelectionMethods
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
		self.population = Population(10, distance_matrix)

	@property
	def converged(self) -> bool:
		self._iteration += 1
		return self.settings.initialization.max_iterations <= self._iteration

	def select(self) -> Individual:
		return SelectionMethods.random(self.population)

	def recombination(self) -> None:
		for _ in range(self.settings.initialization.population_size // 2):
			parent1 = self.select()
			parent2 = self.select()
			(offspring1, offspring2) = RecombinationMethods.partially_mapped_crossover(parent1, parent2)
			self._offsprings.append(offspring1)
			self._offsprings.append(offspring2)

	def elimination(self) -> None:
		new_individuals = EliminationMethods.age_based(self.population, self._offsprings)
		self.population.individuals = new_individuals