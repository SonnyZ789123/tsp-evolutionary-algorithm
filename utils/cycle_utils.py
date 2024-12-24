from config.custom_types import Cycle
from protocols.DistanceMatrixProtocol import DistanceMatrixProtocol


def is_valid_cycle(cycle: Cycle, distance_matrix: DistanceMatrixProtocol) -> bool:
	"""
	Check if the cycle is a valid cycle, i.e. the same dimension as the rows/columns distance_matrix, all cities are
	visited exactly once, and there is a non-infinity path between each city in the cycle.
	:param cycle: The cycle
	:param distance_matrix: The distance matrix
	:return: True if the cycle is valid, False otherwise
	"""
	cycle_length = len(cycle)

	if cycle_length != distance_matrix.value.shape[0]:
		return False

	available = list(range(cycle_length))
	for i in range(cycle_length):
		if distance_matrix.value[cycle[i], cycle[(i + 1) % cycle_length]] == -1:
			return False
		if cycle[i] not in available:
			return False
		available.remove(int(cycle[i]))
	return True
