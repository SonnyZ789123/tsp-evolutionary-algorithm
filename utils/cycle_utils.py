from config.custom_types import Cycle, DistanceMatrix, INFINITY_REPRESENTATION


def is_valid_cycle(cycle: Cycle, distance_matrix: DistanceMatrix) -> bool:
	"""
	Check if the cycle is a valid cycle, i.e. the same dimension as the rows/columns distance_matrix, all cities are
	visited exactly once, and there is a non-infinity path between each city in the cycle.
	:param cycle: The cycle
	:param distance_matrix: The distance matrix
	:return: True if the cycle is valid, False otherwise
	"""
	cycle_length = len(cycle)

	if cycle_length != distance_matrix.shape[0]:
		return False

	available = list(range(cycle_length))
	for i in range(cycle_length):
		if distance_matrix[cycle[i], cycle[(i + 1) % cycle_length]] == INFINITY_REPRESENTATION:
			return False
		if cycle[i] not in available:
			return False
		available.remove(int(cycle[i]))
	return True


def get_cycle_length(cycle: Cycle, distance_matrix: DistanceMatrix) -> float:
	length = 0
	cycle_length = len(cycle)

	for i in range(len(cycle)):
		length += distance_matrix[cycle[i], cycle[(i + 1) % cycle_length]]

	return length


def get_cycle_distances(cycle: Cycle, distance_matrix: DistanceMatrix) -> list[float]:
	distances = []
	cycle_length = len(cycle)

	for i in range(len(cycle)):
		distances.append(round(float(distance_matrix[cycle[i], cycle[(i + 1) % cycle_length]]), 2))

	return distances
