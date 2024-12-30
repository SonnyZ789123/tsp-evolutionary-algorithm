from protocols.SettingsProtocol import FitnessSettingsProtocol, InitializationSettingsProtocol, \
	ConvergenceSettingsProtocol, SelectionSettingsProtocol, \
	MutationSettingsProtocol, RecombinationSettingsProtocol, LocalOptimisationSettingsProtocol, \
	EliminationSettingsProtocol


class Fitness:
	similarity_threshold: float = 0.5
	shape_exp: float = 3


class Initialization:
	population_size: int = 500
	max_iterations: int = 300


class Convergence:
	var_fitness_threshold: float = 0.01
	best_fitness_count_threshold: int = 30


class Selection:
	k_tournament_k: int = 3


class Mutation:
	alpha: float = 0.1
	alpha_decay_rate: float = 0


class Recombination:
	pass


class LocalOptimisation:
	proportion_worst: float = 0.5
	opt_probability: float = 0.5
	k_opt_branch_size: int = 5
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
	elitist_k_tournament_k: int = 3
	elitist_k_tournament_keep_s_best_k: int = 3
	elitist_k_tournament_keep_s_best_s: int = 5


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
		elif 400 <= problem_size:
			self.initialization.population_size = 200
			self.convergence.best_fitness_count_threshold = 100
			self.local_optimisation.proportion_worst = 0.3
			self.local_optimisation.k_opt_branch_size = 5
			self.mutation.alpha = 0.5
			self.mutation.alpha_decay_rate = 0.001
			self.elimination.mixed_elitist_with_crowding_k = 7
			self.elimination.mixed_elitist_with_crowding_proportion = 0.4  # More from the offsprings (which have mutated)
		elif 600 <= problem_size:
			self.initialization.population_size = 100
		elif 800 <= problem_size:
			self.initialization.population_size = 50
