# Base 5 - Reverse Subtour Mutation

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
- Elapsed time for solving TSP: 15.84 seconds
- Best individual cycle length: 5043

`reverse_subtour` keeps the mutation more local, and imo makes more sense in the TSP. The results are similar the previous results.

**Just found out that the resulting best individual cycle contains invalid path, probably because of the recombination operator. Will make the `Infinity` value a very big value instead.**