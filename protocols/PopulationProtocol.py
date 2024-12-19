from typing import Protocol
from custom_types import DistanceMatrix

from protocols.IndividualProtocol import IndividualProtocol


class PopulationProtocol(Protocol):
	size: int
	distance_matrix: DistanceMatrix
	individuals: list[IndividualProtocol]
