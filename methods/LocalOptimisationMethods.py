from typing import Callable, List

from classes.Individual import Individual
from config.custom_types import Cycle
from protocols.IndividualProtocol import IndividualProtocol
from protocols.SettingsProtocol import LocalOptimisationSettingsProtocol


class LocalOptimisationMethods:
	_settings: LocalOptimisationSettingsProtocol

	def __init__(self, settings: LocalOptimisationSettingsProtocol):
		self._settings = settings

	@staticmethod
	def _generate_neighbours(cycle: Cycle, neighbour_method: Callable[[Cycle], Cycle], pool_size: int, k: int) -> List[
		Cycle]:
		if k == 0:
			return [cycle]

		neighbours = []
		for _ in range(pool_size):
			neighbour = neighbour_method(cycle)
			neighbours.extend(
				LocalOptimisationMethods._generate_neighbours(neighbour, neighbour_method, pool_size, k - 1))
		return neighbours

	@staticmethod
	def k_opt(individual: IndividualProtocol, neighbour_method: Callable[[Cycle], Cycle],
			  pool_size: int = 3, k: int = 2) -> None:
		"""
		Apply k-opt local search to the individual.
		:param pool_size: The amount of neighbours to generate
		:param neighbour_method: The method to generate a neighbour
		:param individual: The individual
		:param k: The value of k for k-opt
		"""
		neighbours = LocalOptimisationMethods._generate_neighbours(individual.cycle, neighbour_method, pool_size, k)
		neighbour_individuals = [Individual(cycle, individual.distance_matrix) for cycle in neighbours]
		best_neighbour = max(neighbour_individuals, key=lambda neighbour: neighbour.fitness)

		# use without fitness sharing because neighbours are not in the population
		if best_neighbour.fitness > individual.get_fitness_internal():
			individual.cycle = best_neighbour.cycle
