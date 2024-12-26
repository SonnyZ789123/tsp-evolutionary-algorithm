# Base 2

Comparing `age_based`  and `merged_fitness_based` elimination. See the plots. You can see that by `merged_fitness_based` elimination, the population converges faster. 

```python
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

- initialization: `generate_random_valid_population`
- convergence: `max_iterations`
- selection: `k_tournament`
- recombination: `deterministic_best_parent`
- mutation: `swap`
- elimination: `age_based` or `merged_fitness_based`
- fitness: `negative_of_length`
