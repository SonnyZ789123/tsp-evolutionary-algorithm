from config.custom_types import Cycle, DistanceMatrix
from methods.FitnessMethods import FitnessMethods
from methods.MutationMethods import MutationMethods
from protocols.IndividualProtocol import IndividualProtocol

# Mark this as Individual Protocol because of the getter and setter for the cycle property are throwing an incorrect
# type error
class Individual(IndividualProtocol):
	distance_matrix: DistanceMatrix
	fitness_sharing: float = 1.0
	dirty: bool = True
	_cycle: Cycle
	_fitness: float

	def __init__(self, cycle: Cycle, distance_matrix: DistanceMatrix):
		self._cycle = cycle
		self.distance_matrix = distance_matrix

	@property
	def fitness(self) -> float:
		if self.dirty:
			self._fitness = self.fitness_sharing * FitnessMethods.negative_of_length(self)
			self.dirty = False
		return self._fitness

	@property
	def prop(self) -> float:
		return 0.0

	# Ignore the type error because the type checker is just confused that the getter and setter in the protocol have
	# both the same name.
	@property
	def cycle(self) -> Cycle: # type: ignore
		return self._cycle

	@cycle.setter
	def cycle(self, cycle: Cycle) -> None:
		self._cycle = cycle
		self.dirty = True

	def get_fitness_internal(self) -> float:
		return FitnessMethods.negative_of_length(self)

	def mutate(self) -> None:
		MutationMethods.reverse_subtour(self)
		self.dirty = True

	def __str__(self) -> str:
		return str(self.cycle) + " : " + str(self.fitness)
