# Tour100 optimization (baseline 90851)

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

- Elapsed time for solving TSP: 74.04 seconds
- Best individual cycle length: 83606

---

- Elapsed time for solving TSP: 106.56 seconds
- Best individual cycle length: 83882

---

- Elapsed time for solving TSP: 94.00 seconds
- Best individual cycle length: 83283

---

- Elapsed time for solving TSP: 98.74 seconds
- Best individual cycle length: 79730

---

- Elapsed time for solving TSP: 116.88 seconds
- Best individual cycle length: 81357

---

> Average Elapsed Time: 98.04

> Average Cycle Length: 82371.64

Good enough.
