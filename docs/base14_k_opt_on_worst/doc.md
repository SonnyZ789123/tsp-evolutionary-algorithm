# Base 14 - k-opt on worst individuals

```Python
class Fitness:
	similarity_threshold: float = 0.5
	shape_exp: float = 3


class Initialization:
	population_size: int = 500
	max_iterations: int = 100


class Convergence:
	var_fitness_threshold: float = 0.01


class Selection:
	k_tournament: int = 3


class Mutation:
	alpha: float = 0.1


class Recombination:
	pass


class LocalOptimisation:
	proportion_worst: float = 0.5
	opt_probability: float = 0.5
	k_opt_pool_size: int = 3 # or 5 or 7 or 20 or 30 
	k_opt_k: int = 2


class Elimination:
	mixed_elitism_proportion: float = 0.5


class Settings:
	fitness: Fitness = Fitness()
	initialization: Initialization = Initialization()
	convergence: Convergence = Convergence()
	selection: Selection = Selection()
	mutation: Mutation = Mutation()
	recombination: Recombination = Recombination()
	local_optimisation: LocalOptimisation = LocalOptimisation()
	elimination: Elimination = Elimination()

	def __init__(self, problem_size: int):
		self.initialization.population_size = 500

		if problem_size >= 200:
			self.initialization.population_size = 400
		elif problem_size >= 500:
			self.initialization.population_size = 100
		elif problem_size >= 750:
			self.initialization.population_size = 50
```

- initialization: 1 `generate_greedy_population` with `nearest_neighbour` and rest `generate_random_valid_population`
- convergence: `max_iterations`
- selection: `k_tournament`
- recombination: `order_crossover`
- mutation: `reverse_subtour`
- local optimisation: `k_opt`
- elimination: `mixed_elitism`
- fitness: `negative_of_length`
- problem size: 50


## pool size = 3
- Elapsed time for solving TSP: 31.42 seconds
- Best individual cycle length: 27024

---

## pool size = 5
- Elapsed time for solving TSP: 36.91 seconds
- Best individual cycle length: 28265

Added a file that contains the amount of improved fitness per iteration.

---

## pool size = 7
- Elapsed time for solving TSP: 40.84 seconds
- Best individual cycle length: 27085

---

## pool size = 20
- Elapsed time for solving TSP: 119.44 seconds
- Best individual cycle length: 26343

Added a file that contains the amount of improved fitness per iteration.

---

## pool size = 30
- Elapsed time for solving TSP: 219.80 seconds
- Best individual cycle length: 25779

## Conclusion

Comparing pool size 5 and 20, the one with pool size 5 does not find any improvements around iteration 34 (probably due to convergence) and the one with pool size 20 finds improvements until iteration 44. But a high pool size makes the algorithm too slow, I will limit it to 5. Convergence is a bit slower but not significantly enough. I am going to try to increase the optimisation probability.

Looking at the results, increasing the optimisation probability does not seem to have a significant impact on the results. This is probably because there is low possibility that a better individual will be found. I will keep it at 0.5.
