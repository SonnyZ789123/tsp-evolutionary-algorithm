from typing import List

from protocols.IndividualProtocol import IndividualProtocol
from protocols.PopulationProtocol import PopulationProtocol


class EliminationMethods:
	@staticmethod
	def age_based(population: PopulationProtocol, offsprings: List[IndividualProtocol]) -> None:
		print(population.size, len(offsprings))
		assert population.size == len(offsprings)
		population.individuals = offsprings
