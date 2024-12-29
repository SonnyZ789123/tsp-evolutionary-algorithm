from typing import List, Callable

import numpy as np

from protocols.IndividualProtocol import IndividualProtocol
from protocols.SettingsProtocol import SelectionSettingsProtocol


class SelectionMethods:
	_settings: SelectionSettingsProtocol

	def __init__(self, settings: SelectionSettingsProtocol):
		self._settings = settings

	def k_tournament(self, individuals: List[IndividualProtocol],
					 key: Callable[[IndividualProtocol], float | int] = lambda x: x.fitness) -> IndividualProtocol:
		selected_indexes = np.random.choice(len(individuals), self._settings.k_tournament_k, replace=False)
		selected = [individuals[i] for i in selected_indexes]
		return max(selected, key=key)

	@staticmethod
	def k_tournament_static(individuals: List[IndividualProtocol], k: int,
					 key: Callable[[IndividualProtocol], float | int] = lambda x: x.fitness) -> IndividualProtocol:
		selected_indexes = np.random.choice(len(individuals), k, replace=False)
		selected = [individuals[i] for i in selected_indexes]
		return max(selected, key=key)
