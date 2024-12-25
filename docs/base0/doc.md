# Base 0

```python
class Initialization:
	population_size: int = 100
	max_iterations: int = 100


class Convergence:
	diff_mean_best_threshold: float = 0.01


class Selection:
	k: int = 1


class Mutation:
	alpha: float = 0.05


class Recombination:
	pass


class Elimination:
	pass
```

- tsp: 50
- initialization: `generate_random_valid_population`
- convergence: `difference_mean_and_best_fitness`
- selection: `random`
- recombination: `deterministic_best_parent`
- mutation: `swap`
- elimination: `age_based` keep only the offsprings
- fitness: `negative_of_length`

Really unpredictable results every time, not a good algorithm. The main problem lies in that the selection method is random. The recombination step used the selection method so it's possible that bad individuals are chosen. Also note that the graphs don't make sense, the best fitness goes down and we stop the algorithm when the difference between the mean and the best fitness goes up (???).