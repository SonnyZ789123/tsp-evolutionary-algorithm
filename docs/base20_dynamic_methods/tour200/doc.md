# Tour200 optimization (baseline 39745)

## Common

- initialization: 1 `generate_greedy_population` with `nearest_neighbour` and rest `generate_random_valid_population`
- convergence: `max_iterations` and `best_fitness_count`
- fitness: `negative_of_length`

## Iteration 1 (last iteration algorithm)

- selection: `k_tournament` with `k=3`
- recombination: `order_crossover`
- mutation: `reverse_subtour` with `alpha=0.1`
- local optimisation: `k_opt` with `proportion_worst=0.5`, `opt_probability=0.5`, `k_opt_pool_size=5`, `k_opt_k=2`
- elimination: `mixed_elitist_with_crowding` with `mixed_elitist_with_crowding_proportion=0.5`,
  `mixed_elitist_with_crowding_k=5`
- insert diversity: `replace_worst_with_random` with `replace_worst_with_random_k=0.3`

---

- Elapsed time for solving TSP: 186.92 seconds
- Best individual cycle length: 37978

---

- Elapsed time for solving TSP: 222.40 seconds
- Best individual cycle length: 38485

---

- Elapsed time for solving TSP: 277.72 seconds
- Best individual cycle length: 38319

---

- Elapsed time for solving TSP: 187.79 seconds
- Best individual cycle length: 38151

---

- Elapsed time for solving TSP: 132.30 seconds
- Best individual cycle length: 38232

---

> Average Elapsed Time: 201.43

> Average Cycle Length: 38233.17
 
Good enough.