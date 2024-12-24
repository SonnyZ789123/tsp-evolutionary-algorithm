"""Class to make the distance matrix read-only"""
from config.custom_types import DistanceMatrixInternal


class DistanceMatrix:
	_value: DistanceMatrixInternal

	def __init__(self, value: DistanceMatrixInternal):
		self._value = value

	@property
	def value(self):
		return self._value  # Read-only access
