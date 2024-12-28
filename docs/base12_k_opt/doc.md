# Base 12 - k-opt local search optimisation

```python
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
	alpha: float = 0.2
	k_opt_pool_size: int = 3
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
- fitness: `negative_of_length` with fitness sharing `hamming_similarity`
- problem size: 100

---

- Elapsed time for solving TSP: 154.49 seconds
- Best individual cycle length: 90843

---

- Elapsed time for solving TSP: 159.36 seconds
- Best individual cycle length: 85593

# tour200 (baseline 39745)

**with fitness sharing**

- Elapsed time for solving TSP: 148.50 seconds
- Best individual cycle length: 40091

---

**without fitness sharing**

- Elapsed time for solving TSP: 76.94 seconds
- Best individual cycle length: 38528

---

- Elapsed time for solving TSP: 78.06 seconds
- Best individual cycle length: 39258