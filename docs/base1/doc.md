# Base 1

```python
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

- initialization: `generate_random_valid_population`
- convergence: `variance_fitness` (commented out in the first graphs to see the full plot of the mean and best fitness)
- selection: `k_tournament`
- recombination: `deterministic_best_parent`
- mutation: `swap`
- elimination: `age_based` keep only the offsprings
- fitness: `negative_of_length`

The overall  best fitness is in the first iteration most of the time, then it goes down. And most of the time we stop the algorithm when the "best" fitness is at its worst.

I think it's best from now to first fix the randomness in the population when the mean and best fitness become equal. 