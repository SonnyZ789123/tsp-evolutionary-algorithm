from typing import Protocol


class InitializationProtocol(Protocol):
	population_size: int


class SelectionProtocol(Protocol):
	k: int


class MutationProtocol(Protocol):
	...


class RecombinationProtocol(Protocol):
	...


class EliminationProtocol(Protocol):
	...


class SettingsProtocol(Protocol):
	initialization: InitializationProtocol
	selection: SelectionProtocol
	mutation: MutationProtocol
	recombination: RecombinationProtocol
	elimination: EliminationProtocol
