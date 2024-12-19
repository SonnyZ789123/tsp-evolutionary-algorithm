class Initialization:
	population_size: int = 100


class Selection:
	k: int = 1


class Mutation:
	pass


class Recombination:
	pass


class Elimination:
	pass


class Settings:
	initialization: Initialization = Initialization()
	selection: Selection = Selection()
	mutation: Mutation = Mutation()
	recombination: Recombination = Recombination()
	elimination: Elimination = Elimination()
