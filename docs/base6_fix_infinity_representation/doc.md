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
- Problem size: 50
- Elapsed time for solving TSP: 20.19 seconds
- Best individual cycle length: 25821

Note: increase in time could also be because of the additional calculating for the monitoring.

**Because of the 50% greedy nearest neighbour initialization, the population is too optimized for that local optimum. In tests with many cities (500-1000), the best solution stayed the same or changed very little in the first iteration. I thought randomly picking the first city in the greedy method changed it enough but for example [2 3 4 5 1] is the same as [2 3 4 5 1 2].** 