# Tour500 optimization (baseline 197541)

## Common

- initialization: 1 `generate_greedy_population` with `nearest_neighbour` and rest `generate_random_valid_population`
- fitness: `negative_of_length`

## Iteration 1 (last iteration algorithm)

- population size: 100
- convergence: `max_iterations` and `best_fitness_count` with `best_fitness_count_threshold=100`
- selection: `k_tournament` with `k=3`
- recombination: `order_crossover`
  mutation: `reverse_subtour` with `alpha=0.5` and `alpha_decay_rate=0.001`
- local optimisation: `k_opt` with `proportion_worst=0.3`, `opt_probability=0.5`, `k_opt_pool_size=5`, `k_opt_k=2`
- elimination: `elitist_k_tournament_keep_s_best` with `elitist_k_tournament_keep_s_best_k=3`,
  `elitist_k_tournament_keep_s_best_s=5`.
- insert diversity: None

---

- Elapsed time for solving TSP: 303.93 seconds
- Best individual cycle length: 204123

---

- Elapsed time for solving TSP: 300.56 seconds
- Best individual cycle length: 208488

---

- Elapsed time for solving TSP: 302.27 seconds
- Best individual cycle length: 204396

---

- Elapsed time for solving TSP: 300.68 seconds
- Best individual cycle length: 214440

--- 

- Elapsed time for solving TSP: 304.39 seconds
- Best individual cycle length: 205025

## Iteration 2 (use `mixed_elitist_with_crowding` elimination and `replace_worst_with_random` insert diversity)

- population size: 100
- convergence: `max_iterations` and `best_fitness_count` with `best_fitness_count_threshold=100`
- selection: `k_tournament` with `k=3`
- recombination: `order_crossover`
  mutation: `reverse_subtour` with `alpha=0.5` and `alpha_decay_rate=0.001`
- local optimisation: `k_opt` with `proportion_worst=0.3`, `opt_probability=0.5`, `k_opt_pool_size=5`, `k_opt_k=2`
- elimination: `mixed_elitist_with_crowding` with `mixed_elitist_with_crowding_proportion=0.4`,
  `mixed_elitist_with_crowding_k=7`
- insert diversity: `replace_worst_with_random` with `replace_worst_with_random_k=0.3`

---

- Elapsed time for solving TSP: 303.32 seconds
- Best individual cycle length: 204349

---

- Elapsed time for solving TSP: 307.10 seconds
- Best individual cycle length: 207580

---

- Elapsed time for solving TSP: 301.44 seconds
- Best individual cycle length: 210904

---

- Elapsed time for solving TSP: 303.40 seconds
- Best individual cycle length: 206623

---

- Elapsed time for solving TSP: 302.41 seconds
- Best individual cycle length: 204742

---

> Average Elapsed Time: 303.53

> Average Cycle Length: 206839.71

Best individual cycle length is okay but is barely changed over time. Will use the other algorithm. 

