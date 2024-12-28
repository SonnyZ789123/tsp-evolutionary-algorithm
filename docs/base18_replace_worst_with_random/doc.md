# Base 18 - Replace worst with random

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
- problem size: 50 -> 750

For problem size >= 500, still no good result.

## Results

**Note in the first 5 I had the k to 0.1 instead of 0.3**

- tour100.csv
- Elapsed time for solving TSP: 58.08 seconds
- Best individual cycle length: 83970

---

- tour200.csv
- Elapsed time for solving TSP: 145.16 seconds
- Best individual cycle length: 39031

---

- tour200.csv
- Elapsed time for solving TSP: 144.40 seconds
- Best individual cycle length: 38815

---

- tour500.csv
- Elapsed time for solving TSP: 299.19 seconds
- Best individual cycle length: 159865

---

- tour750.csv
- Elapsed time for solving TSP: 297.41 seconds
- Best individual cycle length: 203767

---

- tour500.csv
- Elapsed time for solving TSP: 297.71 seconds
- Best individual cycle length: 162809

---

- tour50.csv
- Elapsed time for solving TSP: 44.83 seconds
- Best individual cycle length: 26686

---

- tour200.csv
- Elapsed time for solving TSP: 171.85 seconds
- Best individual cycle length: 38778

## Conclusion

I don't think these are significant improvements, but I am sure it promotes diversity so I will keep it in.