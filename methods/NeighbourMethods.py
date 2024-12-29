import numpy as np

from config.custom_types import Cycle


class NeighbourMethods:
	@staticmethod
	def swap_edges(cycle: Cycle) -> Cycle:
		"""Swap two edges in the cycle of the individual."""
		# Select two random edges
		cycle_length = len(cycle)
		# from the slides [x y z a b c d], they picked (y z) and (c d) as edges to swap, and they did it by swapping the
		# elements z and c, so that the cycle becomes [x y c a b z d]
		# so just pick 2 random indices and swap the elements at those indices
		z_index, c_index = np.random.choice(range(cycle_length), 2, replace=False)
		neighbour_cycle = np.copy(cycle)
		neighbour_cycle[z_index], neighbour_cycle[c_index] = neighbour_cycle[c_index], neighbour_cycle[z_index]
		return neighbour_cycle
