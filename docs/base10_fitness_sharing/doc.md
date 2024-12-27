# Base 10 - Fitness Sharing

```Python
class Fitness:
	similarity_threshold: float = 0.5
	shape_exp: float = 3


class Initialization:
	population_size: int = 100
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
```

- initialization: 1 `generate_greedy_population` with `nearest_neighbour` and rest `generate_random_valid_population`
- convergence: `max_iterations`
- selection: `k_tournament`
- recombination: `order_crossover`
- mutation: `reverse_subtour`
- elimination: `mixed_elitism`
- fitness: `negative_of_length`
- Problem size: 100
- Elapsed time for solving TSP: 32.01 seconds
- Best individual cycle length: 92439

**Does not work, only makes it worse. Converges way too quickly.**

