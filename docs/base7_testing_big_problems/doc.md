# Base 7 - Testing big problems

```Python
class Initialization:
	population_size: int = 100
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

- initialization: 1 `generate_greedy_population` with `nearest_neighbour` and rest `generate_random_valid_population`
- convergence: `max_iterations`
- selection: `k_tournament`
- recombination: `order_crossover`
- mutation: `reverse_subtour`
- elimination: `merged_fitness_based`
- fitness: `negative_of_length`

Most of the time the best solution is not changed in the first iteration, which is probably the greedy generated one. This is probably because of lack of diversity, in the elimination method because I currently take only the best ones. I can also try to add fitness sharing.