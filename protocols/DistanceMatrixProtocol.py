from typing import Protocol

from custom_types import DistanceMatrixInternal


class DistanceMatrixProtocol(Protocol):
	_value: DistanceMatrixInternal

	@property
	def value(self) -> DistanceMatrixInternal:
		...