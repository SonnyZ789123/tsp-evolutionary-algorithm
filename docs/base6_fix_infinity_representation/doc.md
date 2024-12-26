# Base 6 - Fix Infinity Representation

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

- initialization: 50% `generate_random_valid_population` and 50% `generate_greedy_population` with `nearest_neighbour`
- convergence: `max_iterations`
- selection: `k_tournament`
- recombination: `order_crossover`
- mutation: `reverse_subtour`
- elimination: `merged_fitness_based`
- fitness: `negative_of_length`
- Elapsed time for solving TSP: 20.19 seconds
- Best individual cycle length: 25821

Note: increase in time could also be because of the additional calculating for the monitoring.