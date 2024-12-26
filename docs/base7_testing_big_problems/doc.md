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

Most of the time the best solution is not changed in the first iteration, which is probably the greedy generated one. This is probably because of lack of diversity, in the elimination method because I currently take only the best ones. I can also try to add fitness sharing.