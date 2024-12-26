# Base 8 - Fix Sort Order

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
	mixed_elitism_proportion: float = 0.5
```

- initialization: 1 `generate_greedy_population` with `nearest_neighbour` and rest `generate_random_valid_population`
- convergence: `max_iterations`
- selection: `k_tournament`
- recombination: `order_crossover`
- mutation: `reverse_subtour`
- elimination: `age_based`
- fitness: `negative_of_length`
- Problem size: 50
- Elapsed time for solving TSP: 18.71 seconds
- Best individual cycle length: 27130