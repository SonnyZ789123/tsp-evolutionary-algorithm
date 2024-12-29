from protocols.IndividualProtocol import IndividualProtocol
from protocols.SettingsProtocol import FitnessSettingsProtocol
from utils.cycle_utils import get_cycle_length


class FitnessMethods:
	_settings: FitnessSettingsProtocol

	def __init__(self, settings: FitnessSettingsProtocol):
		self._settings = settings

	@staticmethod
	def negative_of_length(individual: IndividualProtocol) -> float:
		"""
		Calculate the fitness of the individual as the negative of the length of the cycle.
		:param individual: The individual
		"""
		return -get_cycle_length(individual.cycle, individual.distance_matrix)