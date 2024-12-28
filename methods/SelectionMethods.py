from numbers import Number
from typing import List, Callable

import numpy as np

from protocols.IndividualProtocol import IndividualProtocol


class SelectionMethods:
	@staticmethod
	def k_tournament(individuals: List[IndividualProtocol], k: int,
					 key: Callable[[IndividualProtocol], float | int] = lambda x: x.fitness) -> IndividualProtocol:
		selected_indexes = np.random.choice(len(individuals), k, replace=False)
		selected = [individuals[i] for i in selected_indexes]
		return max(selected, key=key)
