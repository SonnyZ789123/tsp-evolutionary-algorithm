from protocols.SettingsProtocol import FitnessSettingsProtocol, InitializationSettingsProtocol, ConvergenceSettingsProtocol, SelectionSettingsProtocol, \
	MutationSettingsProtocol, RecombinationSettingsProtocol, LocalOptimisationSettingsProtocol, EliminationSettingsProtocol


class Fitness:
	similarity_threshold: float = 0.5
	shape_exp: float = 3


class Initialization:
	population_size: int = 500
	max_iterations: int = 300


class Convergence:
	var_fitness_threshold: float = 0.01
	best_fitness_count_threshold: int = 25


class Selection:
	k_tournament_k: int = 3


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
	problem_size: int
	fitness: FitnessSettingsProtocol = Fitness()
	initialization: InitializationSettingsProtocol = Initialization()
	convergence: ConvergenceSettingsProtocol = Convergence()
	selection: SelectionSettingsProtocol = Selection()
	mutation: MutationSettingsProtocol = Mutation()
	recombination: RecombinationSettingsProtocol = Recombination()
	local_optimisation: LocalOptimisationSettingsProtocol = LocalOptimisation()
	elimination: EliminationSettingsProtocol = Elimination()

	def __init__(self, problem_size: int):
		self.problem_size = problem_size
		if problem_size < 100:
			self.elimination.mixed_elitism_proportion = 0.3
		elif 100 <= problem_size < 200:
			pass
		elif 200 <= problem_size < 400:
			self.initialization.population_size = 400
		elif 400 <= problem_size < 600:
			self.initialization.population_size = 200
		elif 600 <= problem_size < 800:
			self.initialization.population_size = 100
		else:
			self.initialization.population_size = 50
