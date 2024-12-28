# Base 19 - Fitness Cache

```python
class Fitness:
	similarity_threshold: float = 0.5
	shape_exp: float = 3


class Initialization:
	population_size: int = 500
	max_iterations: int = 150


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
	k_opt_pool_size: int = 5
	k_opt_k: int = 2


class Elimination:
	mixed_elitism_proportion: float = 0.5
	mixed_elitism_rest_merged_random_mixed_elitist_proportion: float = 0.5
	mixed_elitism_rest_merged_random_proportion_size: float = 0.5
	offspring_fitness_based_with_crowding_proportion: float = 0.5
	offspring_fitness_based_with_crowding_k: int = 5
	mixed_elitist_with_crowding_proportion: float = 0.5
	mixed_elitist_with_crowding_k: int = 5
	replace_worst_with_random_k: float = 0.3


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
		if problem_size >= 200:
			self.initialization.population_size = 400
			self.max_iterations = 200
		if problem_size >= 500:
			self.initialization.population_size = 200
		if problem_size >= 750:
			self.initialization.population_size = 100
```

- initialization: 1 `generate_greedy_population` with `nearest_neighbour` and rest `generate_random_valid_population`
- convergence: `max_iterations`
- selection: `k_tournament`
- recombination: `order_crossover`
- mutation: `reverse_subtour`
- local optimisation: `k_opt`
- elimination: `mixed_elitist_with_crowding`
- insert diversity: `replace_worst_with_random`
- fitness: `negative_of_length`
- problem size: 200 (baseline 39745)

## Without fitness cache

- Elapsed time for solving TSP: 266.68 seconds
- Best individual cycle length: 38489

---

- Elapsed time for solving TSP: 279.20 seconds
- Best individual cycle length: 39001

---

- Elapsed time for solving TSP: 293.39 seconds
- Best individual cycle length: 38359

---

- Elapsed time for solving TSP: 286.73 seconds
- Best individual cycle length: 38847

---

- Elapsed time for solving TSP: 278.66 seconds
- Best individual cycle length: 38662

## With fitness cache

- Elapsed time for solving TSP: 217.03 seconds
- Best individual cycle length: 38341

---

- Elapsed time for solving TSP: 209.13 seconds
- Best individual cycle length: 38570

---

- Elapsed time for solving TSP: 210.58 seconds
- Best individual cycle length: 38713

---

- Elapsed time for solving TSP: 212.40 seconds
- Best individual cycle length: 39549

---

- Elapsed time for solving TSP: 212.86 seconds
- Best individual cycle length: 39299

## Conclusion

- The fitness cache significantly reduces the elapsed time for solving TSP.