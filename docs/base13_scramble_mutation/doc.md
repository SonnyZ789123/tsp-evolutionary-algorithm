# Base 13 - Scramble mutation

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
- mutation: `reverse_subtour` or `scramble`
- local optimisation: `k_opt`
- elimination: `mixed_elitism`
- fitness: `negative_of_length`
- problem size: 50 or 200

## `reverse_subtour` mutation for tour50 (baseline 27723)

- Elapsed time for solving TSP: 34.74 seconds
- Best individual cycle length: 27198

---

- Elapsed time for solving TSP: 31.98 seconds
- Best individual cycle length: 26695

---

- Elapsed time for solving TSP: 33.41 seconds
- Best individual cycle length: 26838

---

- Elapsed time for solving TSP: 33.56 seconds
- Best individual cycle length: 27155

---

- Elapsed time for solving TSP: 32.85 seconds
- Best individual cycle length: 27123

## `scramble` mutation for tour50

- Elapsed time for solving TSP: 33.04 seconds
- Best individual cycle length: 27201

---

- Elapsed time for solving TSP: 32.21 seconds
- Best individual cycle length: 27893

---

- Elapsed time for solving TSP: 32.61 seconds
- Best individual cycle length: 26972

---

- Elapsed time for solving TSP: 35.70 seconds
- Best individual cycle length: 28132

---

- Elapsed time for solving TSP: 39.48 seconds
- Best individual cycle length: 28005

---

- Elapsed time for solving TSP: 32.27 seconds
- Best individual cycle length: 26040

## `reverse_subtour` mutation for tour200 (baseline 39745)

- Elapsed time for solving TSP: 127.54 seconds
- Best individual cycle length: 38725

---

- Elapsed time for solving TSP: 119.31 seconds
- Best individual cycle length: 38956

---

- Elapsed time for solving TSP: 130.97 seconds
- Best individual cycle length: 39270

---

- Elapsed time for solving TSP: 118.95 seconds
- Best individual cycle length: 38805

## `scramble` mutation for tour200

- Elapsed time for solving TSP: 119.93 seconds
- Best individual cycle length: 39364

---

- Elapsed time for solving TSP: 119.90 seconds
- Best individual cycle length: 41256

---

- Elapsed time for solving TSP: 119.79 seconds
- Best individual cycle length: 40934

---

Elapsed time for solving TSP: 120.74 seconds
Best individual cycle length: 40259

## Conclusion

The `scramble` mutation is overall not better than `reverse_tour`. So I keep `reverse_tour` as the mutation operator for the rest of the experiments. The population does converge way too quickly, in previous experiments I have seen that increasing the mutation probability does not help. I am going to try to use LSO to make worse individuals more appealing.



