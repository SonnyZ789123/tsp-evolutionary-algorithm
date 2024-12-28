# Base 15 - Mixed elitist rest merged random

```Python
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


class LocalOptimisation:
	proportion_worst: float = 0.5
	opt_probability: float = 0.5
	k_opt_pool_size: int = 5
	k_opt_k: int = 2


class Elimination:
	mixed_elitism_proportion: float = 0.5
	mixed_elitism_rest_merged_random_mixed_elitist_proportion: float = 0.5
	mixed_elitism_rest_merged_random_proportion_size: float = 0.5


class Settings:
	fitness: Fitness = Fitness()
	initialization: Initialization = Initialization()
	convergence: Convergence = Convergence()
	selection: Selection = Selection()
	mutation: Mutation = Mutation()
	recombination: Recombination = Recombination()
	local_optimisation: LocalOptimisation = LocalOptimisation()
	elimination: Elimination = Elimination()

	def __init__(self, problem_size: int):
		self.initialization.population_size = 500

		if problem_size >= 200:
			self.initialization.population_size = 400
		elif problem_size >= 500:
			self.initialization.population_size = 100
		elif problem_size >= 750:
			self.initialization.population_size = 50
```

- initialization: 1 `generate_greedy_population` with `nearest_neighbour` and rest `generate_random_valid_population`
- convergence: `max_iterations`
- selection: `k_tournament`
- recombination: `order_crossover`
- mutation: `reverse_subtour`
- local optimisation: `k_opt`
- elimination: `mixed_elitism_rest_merged_random`
- fitness: `negative_of_length`
- problem size: 200

## Results

- Elapsed time for solving TSP: 130.20 seconds
- Best individual cycle length: 39795

--- 

- Elapsed time for solving TSP: 134.20 seconds
- Best individual cycle length: 38545

--- 

- Elapsed time for solving TSP: 131.59 seconds
- Best individual cycle length: 37689

--- 

- Elapsed time for solving TSP: 129.41 seconds
- Best individual cycle length: 39655

## Conclusion

Wanted to keep the algorithm from converging so quickly, not a significant improvement. There is a possibility that a invalid path with a infinite length is being picked.
