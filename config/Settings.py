class Initialization:
	population_size: int = 100
	max_iterations: int = 100


class Convergence:
	diff_mean_best_threshold: float = 0.01


class Selection:
	k: int = 1


class Mutation:
	alpha: float = 0.05


class Recombination:
	pass


class Elimination:
	pass


class Settings:
	initialization: Initialization = Initialization()
	convergence: Convergence = Convergence()
	selection: Selection = Selection()
	mutation: Mutation = Mutation()
	recombination: Recombination = Recombination()
	elimination: Elimination = Elimination()
