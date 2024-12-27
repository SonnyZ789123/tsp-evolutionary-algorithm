# Bsse 11 - Hamming Similarity Fitness Sharing

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


class Elimination:
	mixed_elitism_proportion: float = 0.5


class Settings:
	fitness: Fitness = Fitness()
	initialization: Initialization = Initialization()
	convergence: Convergence = Convergence()
	selection: Selection = Selection()
	mutation: Mutation = Mutation()
	recombination: Recombination = Recombination()
	elimination: Elimination = Elimination()

	def __init__(self, problem_size: int):
		self.initialization.population_size = 500

		if problem_size >= 400:
			self.initialization.population_size = 200
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
- elimination: `mixed_elitism`
- fitness: `negative_of_length` with fitness sharing `hamming_similarity`

## tour50 scores (baseline 27723)

- Elapsed time for solving TSP: 126.82 seconds
- Best individual cycle length: 27889

---

- Elapsed time for solving TSP: 126.81 seconds
- Best individual cycle length: 26871

---

- Elapsed time for solving TSP: 126.02 seconds
- Best individual cycle length: 28280

---

- Elapsed time for solving TSP: 127.53 seconds
- Best individual cycle length: 28240

## tour100 scores (baseline 90851)

- Elapsed time for solving TSP: 147.29 seconds 
- Best individual cycle length: 83742

---

- Elapsed time for solving TSP: 149.37 seconds
- Best individual cycle length: 87120

---

- Elapsed time for solving TSP: 159.71 seconds
- Best individual cycle length: 84709

---

- Elapsed time for solving TSP: 155.83 seconds
- Best individual cycle length: 84280

# tour200 scores (baseline 39745)

- Elapsed time for solving TSP: 150.38 seconds
- Best individual cycle length: 41360

---

- Elapsed time for solving TSP: 152.07 seconds
- Best individual cycle length: 38844

---

- Elapsed time for solving TSP: 146.61 seconds
- Best individual cycle length: 39879

---

- Elapsed time for solving TSP: 140.94 seconds
- Best individual cycle length: 40086

# tour500 scores (baseline 157034)

- Elapsed time for solving TSP: 297.82 seconds
- Best individual cycle length: 165036

--- 


