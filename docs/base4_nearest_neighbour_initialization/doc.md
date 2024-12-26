# Base 4 - Nearest Neighbour Initialization

```Python
class Initialization:
	population_size: int = 500
	max_iterations: int = 100


class Convergence:
	var_fitness_threshold: float = 0.01


class Selection:
	k_tournament: int = 3


class Mutation:
	alpha: float = 0.05


class Recombination:
	pass


class Elimination:
	pass
```

- initialization: `generate_greedy_population` with `nearest_neighbour`
- convergence: `max_iterations`
- selection: `k_tournament`
- recombination: `order_crossover`
- mutation: `swap`
- elimination: `age_based` or `merged_fitness_based`
- fitness: `negative_of_length`
- Elapsed time: 13.08 seconds

The amount of iterations is around 1/3 of the previous base (20 instead of 60).    
