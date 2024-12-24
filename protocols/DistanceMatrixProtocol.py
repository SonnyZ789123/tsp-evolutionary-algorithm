from typing import Protocol

from config.custom_types import DistanceMatrixInternal


class DistanceMatrixProtocol(Protocol):
	_value: DistanceMatrixInternal

	@property
	def value(self) -> DistanceMatrixInternal:
		...