class Fitness:
	similarity_threshold: float = 0.5
	shape_exp: float = 3


class Initialization:
	population_size: int = 500
	max_iterations: int = 100


class Convergence:
	var_fitness_threshold: float = 0.01


class Selection:
	k_tournament: int = 3


class Mutation:
	alpha: float = 0.1


class Recombination:
	pass


class Elimination:
	mixed_elitism_proportion: float = 0.5


class Settings:
	fitness: Fitness = Fitness()
	initialization: Initialization = Initialization()
	convergence: Convergence = Convergence()
	selection: Selection = Selection()
	mutation: Mutation = Mutation()
	recombination: Recombination = Recombination()
	elimination: Elimination = Elimination()

	def __init__(self, problem_size: int):
		self.initialization.population_size = 500

		if problem_size >= 200:
			self.initialization.population_size = 200
		elif problem_size >= 500:
			self.initialization.population_size = 100
		elif problem_size >= 750:
			self.initialization.population_size = 50


