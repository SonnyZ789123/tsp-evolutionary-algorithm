# Base 17 - Mixed Elitist with Crowding

```python
class Fitness:
	similarity_threshold: float = 0.5
	shape_exp: float = 3


class Initialization:
	population_size: int = 500
	max_iterations: int = 130


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
- elimination: `mixed_elitist_with_crowding`
- fitness: `negative_of_length`
- problem size: 50 -> 500

As a way to have a more diverse population, and because the previous method `offspring_fitness_based_with_crowding` did
not work. Now it uses a mixed elitist approach, but with the offsprings I use some crowding. So for each offspring I 
pick for the next iteration, I remove the most similar individual from the available offsprings using k-tournament. 

## Results

tour50.csv
Elapsed time for solving TSP: 40.57 seconds
Best individual cycle length: 25801

---

tour100.csv
Elapsed time for solving TSP: 80.92 seconds
Best individual cycle length: 85729

---

tour200.csv
Elapsed time for solving TSP: 175.16 seconds
Best individual cycle length: 38435

---

tour500.csv
Elapsed time for solving TSP: 294.11 seconds
Best individual cycle length: 159247

---

tour750.csv
Elapsed time for solving TSP: 283.14 seconds
Best individual cycle length: 209288

## Conclusion

Pretty good results except for the 750 cities problem, it was way too slow (only 31 iterations) and stuck on a best 
solution most of the time. 