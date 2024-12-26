# Base 3 - Adding order crossover

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
- recombination: `order_crossover`
- mutation: `swap`
- elimination: `age_based` or `merged_fitness_based`
- fitness: `negative_of_length`

With `age_based` elimination, the mean and best fitness is significantly lower than previous attempts, and the fitness variance does not converge and is very high. Additionally, the mean and best fitness plots consistently go down.

With `merged_fitness_based` elimination, the mean and best fitness is significantly higher than previous attempts (`deterministic_best_parent` recombination), and the fitness variance converges very smoothly but after more iterations. Also note that the plots of the mean and best fitness are way smoother, which shows a nice convergence.

To explain that, with `age_based`, we see that the overall fitness goes down, is that the `order_crossover` recombination method results mostly in worse offsprings. Because `age_based` elimination only keeps the offsprings, the population gets worse and worse. With `merged_fitness_based`, the population is merged, and the best individuals are kept. This way, the population does not get worse and worse, and the fitness converges nicely. 