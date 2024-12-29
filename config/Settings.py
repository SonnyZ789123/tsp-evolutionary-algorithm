from protocols.SettingsProtocol import FitnessProtocol, InitializationProtocol, ConvergenceProtocol, SelectionProtocol, \
	MutationProtocol, RecombinationProtocol, LocalOptimisationProtocol, EliminationProtocol


class Fitness:
	similarity_threshold: float = 0.5
	shape_exp: float = 3


class Initialization:
	population_size: int = 500
	max_iterations: int = 150


class Convergence:
	var_fitness_threshold: float = 0.01
	best_fitness_count_threshold: int = 25


class Selection:
	k_tournament: int = 3


class Mutation:
	alpha: float = 0.1


class Recombination:
	pass


class LocalOptimisation:
	proportion_worst: float = 0.5
	opt_probability: float = 0.5
	k_opt_pool_size: int = 5
	k_opt_k: int = 2


class Elimination:
	mixed_elitism_proportion: float = 0.5
	mixed_elitism_rest_merged_random_mixed_elitist_proportion: float = 0.5
	mixed_elitism_rest_merged_random_proportion_size: float = 0.5
	offspring_fitness_based_with_crowding_proportion: float = 0.5
	offspring_fitness_based_with_crowding_k: int = 5
	mixed_elitist_with_crowding_proportion: float = 0.5
	mixed_elitist_with_crowding_k: int = 5
	replace_worst_with_random_k: float = 0.3


class Settings:
	fitness: FitnessProtocol = Fitness()
	initialization: InitializationProtocol = Initialization()
	convergence: ConvergenceProtocol = Convergence()
	selection: SelectionProtocol = Selection()
	mutation: MutationProtocol = Mutation()
	recombination: RecombinationProtocol = Recombination()
	local_optimisation: LocalOptimisationProtocol = LocalOptimisation()
	elimination: EliminationProtocol = Elimination()

	def __init__(self, problem_size: int):
		if problem_size >= 200:
			self.initialization.population_size = 400
			self.max_iterations = 200
		if problem_size >= 500:
			self.initialization.population_size = 200
		if problem_size >= 750:
			self.initialization.population_size = 100
